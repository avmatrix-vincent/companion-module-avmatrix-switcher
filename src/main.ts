import { InstanceBase, runEntrypoint, InstanceStatus, SomeCompanionConfigField } from '@companion-module/base'
import {
	DEVICE_PORT,
	GetConfigFields,
	resolveDeviceModel,
	type DeviceChoice,
	type ModuleConfig,
	type SavedDevice,
} from './config.js'
import { UpdateVariableDefinitions } from './variables.js'
import { UpgradeScripts } from './upgrades.js'
import { UpdateActions } from './actions.js'
import { UpdateFeedbacks } from './feedbacks.js'
import { UpdatePresets } from './presets.js'
import { CommunicationManager, getUdpModelIndex, type DeviceInfo } from './communication.js'
import { parseDeviceResponse, handleDeviceResponse, buildCommand } from './commandHandler.js'
import { PROTOCOL_COMMANDS, buildSetData } from './features.js'

export class ModuleInstance extends InstanceBase<ModuleConfig> {
	config!: ModuleConfig
	private comm: CommunicationManager | undefined
	// 最近一次 UDP 广播扫描发现的设备，用于填充 Device 下拉框
	private discoveredDevices: DeviceInfo[] = []
	// 扫描互斥标记，避免重复扫描叠加
	private scanInProgress = false
	// 实例是否存活，用于丢弃 destroy 之后完成的扫描结果
	private instanceAlive = false
	private deviceState = {
		pgmSource: 0, // 1-4=HDMI1-4, 0xF0-0xF1=Pattern1-2
		pvwSource: 0,
		mvState: 0,
		// T-Bar 当前值（0~500 显示刻度，内部 0~4095）
		tbarValue: 0,
		// WIPE 模式（1~6，来自 0x0110 上报）
		wipeMode: 0,
		// SPEED 模式（1~2，来自 0x0110 上报）
		speedMode: 0,
		// Freeze 状态（0/1，来自 0x0110 上报）
		freezeActive: false,
		// 最近一次成功执行的 action key（用于执行闪烁反馈）
		lastAction: '',
		// FTB/MUTE 定时闪烁相位
		blinkOn: true,
		// AUTO/FTB/MUTE 激活态（按键执行后本地翻转，用于反馈）
		muteActive: false,
		ftbActive: false,
		autoActive: false,
	}
	// 执行闪烁定时器
	private flashTimer: ReturnType<typeof setTimeout> | undefined
	// FTB/MUTE 定时闪烁
	private blinkTimer: ReturnType<typeof setInterval> | undefined
	// 各“获取指令”(0x0120~0x01B0) 上报/回包解析后的字段值（按 features.ts 字段顺序）
	private reportState: Record<string, number[]> = {}
	// 当前正在执行的动作的唯一 key（供“仅被点击按钮”闪烁反馈）
	pendingFlashKey: string | undefined

	constructor(internal: unknown) {
		super(internal)
	}

	async init(config: ModuleConfig, _isFirstInit: boolean): Promise<void> {
		this.config = config
		this.instanceAlive = true

		this.log('info', 'Instance initialized')
		this.updateActions()
		this.updateFeedbacks()
		this.updatePresets()
		this.updateVariableDefinitions()

		// 先用上次持久化的设备列表填充下拉框，保证配置面板立刻可见
		this.discoveredDevices = this.savedDevicesToInfo(config.devices)

		// 已有地址则立即连接（不阻塞等待扫描，见下方说明）
		if (this.config.host) {
			this.updateStatus(InstanceStatus.Connecting, 'Connecting to device...')
			this.setupConnection()
		} else {
			this.updateStatus(InstanceStatus.Connecting, 'Scanning for supported devices...')
		}

		// 打开连接开关时扫描一次设备列表（仅一次，用于发现/刷新设备）。
		// 注意：不能 await —— 扫描约需数秒，阻塞 init 会超过 Companion 的 IPC
		// 超时上限，导致模块被判定为初始化失败并反复重启。
		void this.scanDevicesOnce()
	}

	async destroy(): Promise<void> {
		this.instanceAlive = false
		this.destroyConnection()
		this.log('debug', 'destroy')
	}

	/**
	 * 保存配置时触发（点 Save）。
	 * Device 下拉变化 -> 同步 Target IP 并自动连接到该设备（随后由心跳监测在线状态）。
	 */
	async configUpdated(config: ModuleConfig): Promise<void> {
		const previousDevice = this.config?.device
		const deviceChanged = !!config.device && config.device !== previousDevice

		this.config = config

		// Device 切换：Target IP 必须跟着所选设备走，保证界面显示值同步
		if (deviceChanged) {
			this.log('info', `[Config] Device switched to ${config.device}, syncing Target IP and reconnecting`)
			this.config = { ...config, host: config.device }
			this.saveConfig(this.config)
		} else {
			this.log('info', `[Config] Reconnecting to ${config.host}`)
		}

		// 已连接到同一设备则无需重连，避免打断正在运行的心跳
		if (!deviceChanged && this.comm && this.config.host === previousDevice) {
			this.log('debug', '[Config] Same device, keeping existing connection')
			return
		}

		this.reconnect()
	}

	/** 销毁旧连接并按当前 config 重新连接（含心跳） */
	private reconnect(): void {
		this.destroyConnection()
		this.updateStatus(InstanceStatus.Connecting, 'Connecting to device...')
		this.setupConnection()
	}

	/** 把持久化的设备列表还原成运行时结构（含 MAC，保证重启后可直接发心跳） */
	private savedDevicesToInfo(saved: SavedDevice[] | undefined): DeviceInfo[] {
		return (saved ?? []).map((d) => {
			// 优先用原始型号按映射表重算 Dev_Type，保证修改映射后自动生效
			const rawModel = d.rawModel ?? d.name
			const modelIndex = getUdpModelIndex(rawModel)
			return {
				host: d.host,
				port: DEVICE_PORT,
				model: rawModel,
				name: d.name,
				vendor: '',
				mac: d.mac ?? '',
				sn: '',
				productType: d.productType ?? 0,
				udpType: modelIndex !== 0xff ? modelIndex : (d.udpType ?? d.productType ?? 0xff),
				protocolVer: 0,
				lastSeen: 0,
			}
		})
	}

	/**
	 * 打开连接开关时扫描一次设备列表：
	 * - 结果写入 discoveredDevices 并持久化到 config，重启后仍可显示
	 * - 未指定设备时默认选中第一个，并让 Target IP 与之一致
	 */
	private async scanDevicesOnce(): Promise<void> {
		if (this.scanInProgress) {
			this.log('debug', '[Scan] Scan already in progress, skipping')
			return
		}
		this.scanInProgress = true

		try {
			const devices = await this.scanDevices()
			if (!this.instanceAlive) {
				this.log('debug', '[Scan] Instance destroyed during scan, discarding results')
				return
			}

			if (devices.length === 0) {
				this.log('warn', '[Scan] No supported device found, keeping previous device list')
				return
			}

			const saved: SavedDevice[] = devices.map((d) => ({
				host: d.host,
				name: resolveDeviceModel(d.model),
				mac: d.mac,
				productType: d.productType,
				udpType: d.udpType,
				rawModel: d.model,
			}))

			// 已选设备仍在线则保留其选择；否则默认第一个，并把 Target IP 绑定为其地址
			const selected = saved.find((d) => d.host === this.config.device)
			const target = selected ?? saved[0]
			const targetChanged = this.config.device !== target.host || this.config.host !== target.host

			const nextConfig: ModuleConfig = {
				...this.config,
				device: target.host,
				host: target.host,
				devices: saved,
			}
			// 仅在配置真正发生变化时才写回，避免无谓的配置保存与重连
			const configChanged =
				nextConfig.device !== this.config.device ||
				nextConfig.host !== this.config.host ||
				JSON.stringify(nextConfig.devices) !== JSON.stringify(this.config.devices)
			this.config = nextConfig
			if (configChanged) {
				this.saveConfig(this.config)
			}

			this.log('info', `[Scan] Device="${target.name}" TargetIP=${target.host} (${saved.length} device(s) available)`)

			// 扫描补齐了 MAC：把最新设备信息交给当前连接，使其具备心跳条件
			if (!targetChanged && this.comm) {
				this.comm.setTargetDevice(this.discoveredDevices.find((d) => d.host === target.host))
				// 连接已建立时确保心跳在跑（幂等，同时重置失败计数）
				if (this.comm.getStatus()) {
					this.comm.startHeartbeat()
				}
				return
			}

			// 设备发生变化（首次识别 / 所选设备已离线）：自动连接到该设备
			this.reconnect()
		} catch (error) {
			this.log('error', `[Scan] Unexpected scan failure: ${(error as Error).message}`)
		} finally {
			this.scanInProgress = false
		}
	}

	getConfigFields(): SomeCompanionConfigField[] {
		// Device 下拉由 UDP 扫描结果填充，Target IP 可手动编辑
		return GetConfigFields(this.buildDeviceChoices(), this.config)
	}

	/** 把扫描结果转成 Device 下拉的选项：只显示型号名称，值为设备 IP */
	private buildDeviceChoices(): DeviceChoice[] {
		return this.discoveredDevices.map((device) => ({
			host: device.host,
			label: resolveDeviceModel(device.model),
		}))
	}

	/**
	 * 扫描网络发现设备
	 */
	private async scanDevices(): Promise<DeviceInfo[]> {
		this.log('debug', '[Scan] Starting UDP broadcast device discovery')
		const scanner = new CommunicationManager({
			host: this.config?.host || '255.255.255.255',
			port: DEVICE_PORT,
			onLog: (level, message) => {
				this.log(level, message)
			},
		})

		try {
			await scanner.scanNetwork()
			const devices = scanner.getDiscoveredDevices()
			this.discoveredDevices = devices

			if (devices.length === 0) {
				this.log('warn', '[Scan] No supported device found')
				return []
			}

			this.log('debug', `[Scan] Found ${devices.length} supported device(s):`)
			for (const device of devices) {
				this.log('debug', `[Scan]   ${device.host} -> model="${device.model}" (${resolveDeviceModel(device.model)})`)
			}
			return devices
		} catch (error) {
			this.log('error', `[Scan] Device scan failed: ${(error as Error).message}`)
			return []
		} finally {
			scanner.disconnect()
		}
	}

	private setupConnection(): void {
		if (!this.config.host) {
			this.log('error', 'No device address configured for connection')
			this.updateStatus(InstanceStatus.BadConfig, 'No device address configured')
			return
		}

		// 当前连接目标对应的扫描信息（可能因手动输入 IP 而不存在）
		const targetDevice = this.discoveredDevices.find((d) => d.host === this.config.host)
		const modelLabel = targetDevice ? resolveDeviceModel(targetDevice.model) : 'Unknown (manual IP)'

		this.log('info', '========================================')
		this.log('info', 'Establishing UDP connection to device')
		this.log('info', `  Model: ${modelLabel}`)
		this.log('info', `  IP: ${this.config.host}`)
		this.log('info', `  Port: ${DEVICE_PORT}`)
		this.log('info', '========================================')

		this.comm = new CommunicationManager({
			host: this.config.host,
			port: DEVICE_PORT,
			onLog: (level, message) => {
				this.log(level, message)
			},
		})

		// 心跳包需要目标设备的 MAC 与型号，使用扫描结果中匹配的条目
		this.comm.setTargetDevice(targetDevice)

		this.comm.setCallbacks({
			onStatusChange: (status, message) => {
				this.updateStatus(status, message)
				this.checkFeedbacks('connection_status')
				if (status === InstanceStatus.Ok) {
					this.log('info', '========================================')
					this.log('info', `✓ Device online (responded to probe)`)
					this.log('info', `  Model: ${modelLabel}`)
					this.log('info', `  IP: ${this.config.host}:${DEVICE_PORT}`)
					this.log('info', '  Heartbeat: active, monitoring this device')
					this.log('info', '========================================')
					this.setVariableValues({ connection_status: 'Connected' })
					this.updatePresets()
				} else {
					this.log('warn', `Connection status: ${status} - ${message || 'unknown'}`)
					this.setVariableValues({ connection_status: 'Disconnected' })
					this.setPresetDefinitions({})
				}
			},
			onData: (data, host, port, cmd, session) => {
				this.handleDeviceData(data, host, port, cmd, session)
			},
			onReport: (packet) => {
				this.handleDeviceReport(packet)
			},
			onError: (err) => {
				this.log('error', `Connection error: ${err.message}`)
			},
		})

		this.setVariableValues({
			device_model: modelLabel,
			device_ip: `${this.config.host}:${DEVICE_PORT}`,
			connection_status: 'Connecting',
		})

		void this.comm.connect()
	}

	private destroyConnection(): void {
		if (this.comm) {
			this.comm.disconnect()
			this.comm = undefined
		}
		if (this.blinkTimer) {
			clearInterval(this.blinkTimer)
			this.blinkTimer = undefined
		}
	}

	/** 发送协议“设置指令”（Data = Param_Vaild(参数索引) + 值） */
	public async sendProtocolSet(commandKey: string, fieldIndex: number, value: number, label: string): Promise<boolean> {
		if (!this.comm) {
			this.log('error', `[Set] Cannot set ${label}: communication not initialized`)
			return false
		}
		const cmd = PROTOCOL_COMMANDS[commandKey]
		if (!cmd) {
			this.log('error', `[Set] Unknown command: ${commandKey}`)
			return false
		}
		const data = buildSetData(cmd, fieldIndex, value)
		this.log('info', `[Set] ${label} -> ${value} (cmd=0x${cmd.set.toString(16).padStart(4, '0')}, field=${fieldIndex})`)
		const ok = await this.comm.sendCommand(cmd.set, data)
		if (ok && this.pendingFlashKey) this.flash(this.pendingFlashKey)
		return ok
	}

	private handleDeviceData(data: Buffer, host: string, port: number, cmd?: number, session?: number): void {
		this.log('debug', `Device data from ${host}:${port}, length: ${data.length} bytes`)
		this.log('debug', `Raw hex: ${data.toString('hex')}`)
		const response = parseDeviceResponse(data.toString('ascii'), cmd, session, data)
		this.log('debug', `Parsed response type: ${response.type}, cmd: 0x${response.cmd.toString(16).padStart(4, '0')}`)

		handleDeviceResponse(response, {
			onPowerChange: (power) => {
				this.log('info', `[Device] Power state changed: ${power ? 'ON' : 'OFF'}`)
			},
			onStatusUpdate: (status) => {
				this.log('info', `[Device] Status update: ${status}`)
			},
			onError: (error) => {
				this.log('error', `[Device] Error: ${error}`)
			},
			onHeartbeat: (mac, controllable) => {
				this.log('debug', `Heartbeat received - MAC: ${mac}, Controllable: ${controllable ? 'Yes' : 'No'}`)
			},
			onCustomData: (data) => {
				// 按设备回包同步 PGM/PVW 当前值
				if (data.rawBuffer) {
					this.syncSwitchState(data.cmd, data.rawBuffer)
				} else {
					this.log('debug', `[Device] Custom data - Cmd: 0x${data.cmd.toString(16).padStart(4, '0')}, Raw: ${data.raw}`)
				}
			},
		})
	}

	private handleDeviceReport(packet: any): void {
		this.log(
			'info',
			`[Report] Device report - Cmd: 0x${packet.cmd.toString(16).padStart(4, '0')}, Type: 0x${packet.type.toString(16)}, Data(${packet.data.length}B): ${packet.data.toString('hex')}`,
		)
		// 按设备主动上报同步 PGM/PVW 当前值
		this.syncSwitchState(packet.cmd, packet.data)
	}

	/**
	 * 根据设备主动上报/回包同步状态（参考《AVM同步协议.md》3.2 节）。
	 * - cmd=0x000a：切换台状态（Data = PGM, PVW, MV）
	 * - cmd=0x0110：按键获取（10B）
	 *     [0]PGM(1~8) [1]PVW(1~8) [2]WIPE MODE(1~6) [3]SPEED MODE(1~2)
	 *     [4]FTB_State(0/1) [5]Freeze(0/1) [6..7]T_Bar_val(0~4095) [8..9]b_bar_pos
	 */
	private syncSwitchState(cmd: number | undefined, data: Buffer): void {
		if (cmd === undefined || !data) return

		if (cmd === 0x000a && data.length >= 3) {
			this.deviceState.pgmSource = data[0]
			this.deviceState.pvwSource = data[1]
			this.deviceState.mvState = data[2]
			this.applySwitchFeedback(cmd)
			return
		}

		if (cmd !== 0x0110) {
			this.handleGetReport(cmd, data)
			return
		}
		if (data.length < 10) return

		// 0x0110 按键获取（10B，见《AVM同步协议.md》3.2.1）：
		//   [0]PGM(1~8) [1]PVW(1~8) [2]WIPE MODE(1~6) [3]SPEED MODE(1~2)
		//   [4]FTB_State(0/1) [5]Freeze(0/1) [6..7]T_Bar_val(0~4095) [8..9]b_bar_pos
		const pgmVal = data[0]
		const pvwVal = data[1]
		const wipeMode = data[2]
		const speedMode = data[3]
		const ftbState = data[4]
		const freezeState = data[5]
		const tBarVal = data.readUInt16BE(6)
		const bBarPos = data.readUInt16BE(8)
		this.log(
			'info',
			`[Report 0x0110] PGM=${pgmVal}, PVW=${pvwVal}, WIPE=${wipeMode}, SPEED=${speedMode}, FTB=${ftbState}, Freeze=${freezeState}, T_Bar=${tBarVal}, b_bar_pos=${bBarPos}`,
		)

		// 1) PGM / PVW 当前源（1~6 直接；7->PAT1, 8->PAT2）→ 同步按钮颜色
		this.deviceState.pgmSource = this.toSourceValue(pgmVal)
		this.deviceState.pvwSource = this.toSourceValue(pvwVal)
		this.applySwitchFeedback(cmd)

		// 2) FTB / Freeze 状态（变化时闪烁）
		if (this.deviceState.ftbActive !== (ftbState === 1)) {
			this.deviceState.ftbActive = ftbState === 1
			this.flash('key:19')
			this.updateBlink()
		}
		if (this.deviceState.freezeActive !== (freezeState === 1)) {
			this.deviceState.freezeActive = freezeState === 1
			this.flash('key:33')
			this.updateBlink()
		}
		this.checkFeedbacks('ftb_active', 'freeze_active')

		// WIPE 模式（1~6）
		this.deviceState.wipeMode = wipeMode
		this.checkFeedbacks('wipe_active')

		// 3) T-Bar 位置（0~4095 -> 显示刻度 0~500）
		const disp = Math.round((tBarVal * 500) / 4095)
		this.deviceState.tbarValue = disp
		this.deviceState.speedMode = speedMode

		// 4) 全部上报值 -> 变量
		this.setVariableValues({
			pgm_source: this.sourceLabel(this.deviceState.pgmSource),
			pvw_source: this.sourceLabel(this.deviceState.pvwSource),
			pgm_value: pgmVal,
			pvw_value: pvwVal,
			wipe_mode: wipeMode,
			wipe_label: this.wipeLabel(wipeMode),
			speed_mode: speedMode,
			ftb_state: ftbState === 1 ? 'ON' : 'OFF',
			freeze_state: freezeState === 1 ? 'ON' : 'OFF',
			tbar_value: String(disp),
		})
	}

	/** WIPE 模式值 -> 文本 */
	private wipeLabel(v: number): string {
		return ['', 'WIPE1', 'WIPE2', 'WIPE3', 'WIPE4', 'MIX', 'DIP'][v] ?? String(v)
	}

	/** 上报源值(1~8) -> 内部源值(1~6 / 0xF0=PAT1 / 0xF1=PAT2) */
	private toSourceValue(v: number): number {
		if (v >= 1 && v <= 6) return v
		if (v === 7) return 0xf0
		if (v === 8) return 0xf1
		return 0
	}

	/** 处理其他“获取指令”(0x0120~0x01B0) 的主动上报/回包 */
	private handleGetReport(cmd: number, data: Buffer): void {
		const key = Object.keys(PROTOCOL_COMMANDS).find((k) => PROTOCOL_COMMANDS[k].get === cmd)
		if (!key) return
		this.applyGetReport(key, data)
		this.syncDerivedFromReport(key)
	}

	/** 按字段长度通用拆包，存入 reportState */
	private applyGetReport(key: string, data: Buffer): void {
		const fields = PROTOCOL_COMMANDS[key].fields
		const values: number[] = []
		let off = 0
		for (const f of fields) {
			if (off + f.size > data.length) break
			let v = 0
			for (let i = 0; i < f.size; i++) v = (v << 8) | data[off + i]
			values.push(v)
			off += f.size
		}
		this.reportState[key] = values
		this.log('info', `[Report] ${key} = [${values.join(', ')}]`)
	}

	/** 依据上报的获取指令刷新对应反馈/状态 */
	private syncDerivedFromReport(key: string): void {
		const vals = this.reportState[key] ?? []
		switch (key) {
			case 'codec':
				this.checkFeedbacks('stream_active')
				break
			case 'audio': {
				const mute = vals[0] === 1
				if (mute !== this.deviceState.muteActive) {
					this.deviceState.muteActive = mute
					this.flash('key:20')
					this.updateBlink()
				}
				this.checkFeedbacks('mute_active')
				break
			}
			case 'pip1':
				this.checkFeedbacks('pip1_status_active')
				break
			case 'pip2':
				this.checkFeedbacks('pip2_status_active')
				break
			case 'pip3':
				this.checkFeedbacks('pip3_status_active')
				break
			case 'luma':
				this.checkFeedbacks('luma_status_active')
				break
			case 'chroma':
				this.checkFeedbacks('chroma_status_active')
				break
			case 'dsk':
				this.checkFeedbacks('dsk_status_active')
				break
			case 'logo':
				this.checkFeedbacks('logo_status_active')
				break
			default:
				break
		}
	}

	/** 读取某“获取指令”解析后的字段值 */
	public getReportState(key: string): number[] {
		return this.reportState[key] ?? []
	}

	/** 刷新 PGM/PVW 反馈与变量 */
	private applySwitchFeedback(cmd: number): void {
		this.log(
			'info',
			`[Switch] PGM=${this.deviceState.pgmSource}, PVW=${this.deviceState.pvwSource} (cmd=0x${cmd.toString(16).padStart(4, '0')})`,
		)
		this.checkFeedbacks('pgm_active', 'pvw_active')
		this.setVariableValues({
			pgm_source: this.sourceLabel(this.deviceState.pgmSource),
			pvw_source: this.sourceLabel(this.deviceState.pvwSource),
		})
	}

	public async scanForDevices(): Promise<DeviceInfo[]> {
		// 手动触发扫描，与初始化扫描共用互斥标记，避免并发叠加
		if (this.scanInProgress) {
			this.log('info', '[Scan] Scan already in progress, ignoring duplicate request')
			return this.discoveredDevices
		}
		this.scanInProgress = true
		try {
			return await this.scanDevices()
		} finally {
			this.scanInProgress = false
		}
	}

	public async sendToDevice(commandId: string, params?: Record<string, unknown>): Promise<boolean> {
		if (!this.comm) {
			this.log('error', 'Communication not initialized')
			return false
		}

		const { cmd, data } = buildCommand(commandId, params)

		// 对于KEY_PRESS命令，根据keyVal映射到具体的按钮名称
		let actionLabel = commandId
		if (commandId === 'KEY_PRESS' && params?.keyVal !== undefined) {
			const keyVal = params.keyVal as number
			actionLabel = this.getButtonNameByKeyVal(keyVal)
		}

		this.log('info', `[Action] Executing: ${actionLabel} -> Command: 0x${cmd.toString(16).padStart(4, '0')}`)
		this.log('debug', `[Action] Data hex: ${data.toString('hex')}`)
		const success = await this.comm.sendCommand(cmd, data)

		if (success) {
			this.log('info', `[Action] ${actionLabel} sent successfully`)
			// 乐观更新 + 执行闪烁反馈（key 由动作包裹器统一设置）
			const keyVal = params?.keyVal as number | undefined
			if (commandId === 'KEY_PRESS' && typeof keyVal === 'number') {
				this.optimisticKey(keyVal)
			}
			if (this.pendingFlashKey) this.flash(this.pendingFlashKey)
		} else {
			this.log('error', `[Action] Failed to send: ${actionLabel}`)
		}

		return success
	}

	/**
	 * 发送成功后的乐观状态更新（以设备上报为准，随后会被校正）。
	 * keyVal 见 PSV0617 键值表。
	 */
	private optimisticKey(keyVal: number): void {
		if (keyVal >= 1 && keyVal <= 6) {
			this.deviceState.pgmSource = keyVal
			this.applySwitchFeedback(0x0110)
		} else if (keyVal === 7 || keyVal === 8) {
			this.deviceState.pgmSource = keyVal === 7 ? 0xf0 : 0xf1
			this.applySwitchFeedback(0x0110)
		} else if (keyVal >= 9 && keyVal <= 14) {
			this.deviceState.pvwSource = keyVal - 8
			this.applySwitchFeedback(0x0110)
		} else if (keyVal === 15 || keyVal === 16) {
			this.deviceState.pvwSource = keyVal === 15 ? 0xf0 : 0xf1
			this.applySwitchFeedback(0x0110)
		} else if (keyVal === 18) {
			this.deviceState.autoActive = !this.deviceState.autoActive
			this.checkFeedbacks('auto_active')
		} else if (keyVal === 19) {
			this.deviceState.ftbActive = !this.deviceState.ftbActive
			this.checkFeedbacks('ftb_active')
		} else if (keyVal === 20) {
			this.deviceState.muteActive = !this.deviceState.muteActive
			this.checkFeedbacks('mute_active')
		} else if (keyVal >= 27 && keyVal <= 30) {
			this.deviceState.wipeMode = keyVal - 26
			this.checkFeedbacks('wipe_active')
		} else if (keyVal === 31) {
			this.deviceState.wipeMode = 5
			this.checkFeedbacks('wipe_active')
		} else if (keyVal === 32) {
			this.deviceState.wipeMode = 6
			this.checkFeedbacks('wipe_active')
		} else if (keyVal === 33) {
			this.deviceState.freezeActive = !this.deviceState.freezeActive
			this.checkFeedbacks('freeze_active')
		}
	}

	/** 记录“最近执行的 action key”，约 400ms 后清除（供执行闪烁反馈） */
	private flash(key: string): void {
		this.deviceState.lastAction = key
		this.setVariableValues({ last_action: key })
		this.checkFeedbacks('last_action')
		if (this.flashTimer) clearTimeout(this.flashTimer)
		this.flashTimer = setTimeout(() => {
			this.deviceState.lastAction = ''
			this.setVariableValues({ last_action: '' })
			this.checkFeedbacks('last_action')
		}, 400)
	}

	/** FTB/MUTE/Freeze 定时闪烁：开启时按 ~500ms 切换相位并刷新反馈（红底白字 ↔ 黑底白字） */
	private updateBlink(): void {
		const need = this.deviceState.ftbActive || this.deviceState.muteActive || this.deviceState.freezeActive
		if (need && !this.blinkTimer) {
			this.blinkTimer = setInterval(() => {
				this.deviceState.blinkOn = !this.deviceState.blinkOn
				this.checkFeedbacks('ftb_active', 'mute_active', 'freeze_active')
			}, 500)
		} else if (!need && this.blinkTimer) {
			clearInterval(this.blinkTimer)
			this.blinkTimer = undefined
			this.deviceState.blinkOn = true
			this.checkFeedbacks('ftb_active', 'mute_active', 'freeze_active')
		}
	}

	/** 源值 -> 名称（用于变量/日志展示） */
	private sourceLabel(value: number): string {
		if (value >= 1 && value <= 6) return `IN${value}`
		if (value === 0xf0) return 'Pattern1'
		if (value === 0xf1) return 'Pattern2'
		return value ? `0x${value.toString(16)}` : 'N/A'
	}

	private getButtonNameByKeyVal(keyVal: number): string {
		// 严格对应 PSV0617 文档 3.1.2 键值对应表
		if (keyVal >= 1 && keyVal <= 6) return `PGM${keyVal}`
		if (keyVal === 7) return 'PGM_PATTERN1'
		if (keyVal === 8) return 'PGM_PATTERN2'
		if (keyVal >= 9 && keyVal <= 14) return `PVW${keyVal - 8}`
		if (keyVal === 15) return 'PVW_PATTERN1'
		if (keyVal === 16) return 'PVW_PATTERN2'
		if (keyVal === 17) return 'CUT'
		if (keyVal === 18) return 'AUTO'
		if (keyVal === 19) return 'FTB'
		if (keyVal === 20) return 'MUTE'
		if (keyVal === 21) return 'SPEED1'
		if (keyVal === 22) return 'SPEED2'
		if (keyVal === 23) return 'REC'
		if (keyVal >= 24 && keyVal <= 26) return `STREAM${keyVal - 23}`
		if (keyVal >= 27 && keyVal <= 30) return `WIPE${keyVal - 26}`
		if (keyVal === 31) return 'MIX'
		if (keyVal === 32) return 'DIP'
		if (keyVal === 33) return 'FREEZE'
		if (keyVal >= 34 && keyVal <= 39) return `F${keyVal - 33}`
		return `UNKNOWN_KEY_${keyVal}`
	}

	/**
	 * 移动 T-Bar（0x0010, Param_Vaild=1 T_Bar_val）
	 * 对外显示刻度 0~500，内部按 0~4095 等比例换算后下发。
	 * direction: 1=Up / 0=Down
	 */
	public async moveTBar(direction: number, step: number): Promise<boolean> {
		const base = this.deviceState.tbarValue
		let next = direction === 1 ? base + step : base - step
		if (next < 0) next = 0
		if (next > 500) next = 500
		this.deviceState.tbarValue = next
		this.setVariableValues({ tbar_value: String(next) })
		// 0~500 -> 0~4095 等比例换算
		const raw = Math.round((next * 4095) / 500)
		this.log('info', `[T-Bar] ${direction === 1 ? 'Up' : 'Down'} by ${step} -> ${next}/500 (raw=${raw})`)
		return this.sendToDevice('KEY_PRESS', { tBarVal: raw })
	}

	public getDeviceConnectionStatus(): boolean {
		return this.comm?.getStatus() ?? false
	}

	public getDeviceState(): any {
		return { ...this.deviceState }
	}

	updateActions(): void {
		UpdateActions(this)
	}

	updateFeedbacks(): void {
		UpdateFeedbacks(this)
	}

	updatePresets(): void {
		UpdatePresets(this)
	}

	updateVariableDefinitions(): void {
		UpdateVariableDefinitions(this)
	}
}

runEntrypoint(ModuleInstance, UpgradeScripts)

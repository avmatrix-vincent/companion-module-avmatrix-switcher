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
import {
	CommunicationManager,
	getUdpModelIndex,
	UDPParser,
	type DeviceInfo,
	type ParsedPacket,
} from './communication.js'
import { parseDeviceResponse, handleDeviceResponse, buildCommand, type TBarSendMode } from './commandHandler.js'
import { buildSetData, type ProtocolCommand } from './features.js'
import { buildProtocolCommands, getActiveProfile, matchDeviceProfile } from './devices/index.js'
import { getProtocolFamily } from './devices/protocols.js'
import type { DeviceProfile, ProtocolFamily } from './devices/types.js'
import { LOG_RAW_PACKETS } from './debug.js'

export interface DeviceState {
	pgmSource: number
	pvwSource: number
	mvState: number
	tbarValue: number
	wipeMode: number
	speedMode: number
	freezeActive: boolean
	lastAction: string
	blinkOn: boolean
	muteActive: boolean
	ftbActive: boolean
	autoActive: boolean
	keyType: number
}

export class ModuleInstance extends InstanceBase<ModuleConfig> {
	config!: ModuleConfig
	// 当前设备所属产品档案：决定可用功能分组与协议命令表
	private deviceProfile: DeviceProfile = getActiveProfile(undefined)
	private protocolCommands: Record<string, ProtocolCommand> = buildProtocolCommands(this.deviceProfile)
	private protocolFamily: ProtocolFamily = getProtocolFamily(this.deviceProfile.protocolFamily)
	// 当前已注册的 action id 集合（供 presets 剔除引用到不存在 action 的按钮）
	private registeredActionIds: Set<string> = new Set()
	private comm: CommunicationManager | undefined
	// 最近一次 UDP 广播扫描发现的设备，用于填充 Device 下拉框
	private discoveredDevices: DeviceInfo[] = []
	// 扫描互斥标记，避免重复扫描叠加
	private scanInProgress = false
	// 实例是否存活，用于丢弃 destroy 之后完成的扫描结果
	private instanceAlive = false
	// 当前正在使用的连接 host（用于 configUpdated 判断是否需要重连）
	private connectedHost: string | undefined
	private deviceState: DeviceState = {
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
		// 当前激活的 Key 模块（0x0130：0=PIP / 1=Luma / 2=Chroma / 3=DSK；-1=未知，仅 H4K）
		keyType: -1,
	}
	// 执行闪烁定时器
	private flashTimer: ReturnType<typeof setTimeout> | undefined
	// FTB/MUTE 定时闪烁
	private blinkTimer: ReturnType<typeof setInterval> | undefined
	// 各“获取指令”(0x0120~0x01B0) 上报/回包解析后的字段值（按 features.ts 字段顺序）
	private reportState: Record<string, number[]> = {}
	// T-Bar 原始值（0~tBarMax，H4K 为 0~4095）；下发与显示都以它为基准
	private tbarRaw = 0
	// 推杆下发序号：连续点击时只让最后一次做回读校验，避免日志刷屏与重复重发
	private tbarSendSeq = 0
	// 设备上报的 T-Bar 原始值（仅由 0x0110 解析回写，不受本地乐观更新影响；-1=尚未收到上报）
	private lastReportedTBar = -1
	// 推杆本地基准锁定到期时间：H4K 连续点击期间不让设备回读覆盖 tbarRaw（否则每次 ±step 基准会漂移）
	private tbarHoldUntil = 0
	// 各“获取指令”最近一次收到回包/上报的时间（用于查询重试判定）
	private lastReplyAt: Map<string, number> = new Map()
	// WIPE 样式写后校验（仅 H4K）：记录刚下发的 WipeN、目标值以及下发前的三个 Wipe 值
	private pendingWipeCheck?: { n: number; value: number; before: number[]; at: number }
	// 当前正在执行的动作的唯一 key（供“仅被点击按钮”闪烁反馈）
	pendingFlashKey: string | undefined

	constructor(internal: unknown) {
		super(internal)
	}

	async init(config: ModuleConfig, _isFirstInit: boolean): Promise<void> {
		this.config = config
		this.instanceAlive = true

		this.log('info', 'Instance initialized')

		// 先用上次持久化的设备列表填充下拉框，保证配置面板立刻可见
		this.discoveredDevices = this.savedDevicesToInfo(config.devices)

		// 依据已保存的型号确定产品档案（协议族 + 功能集），再注册功能表
		const initialDevice = this.discoveredDevices.find((d) => d.host === config.host) ?? this.discoveredDevices[0]
		this.deviceProfile = getActiveProfile(initialDevice?.model, initialDevice?.productType)
		this.protocolCommands = buildProtocolCommands(this.deviceProfile)
		this.protocolFamily = getProtocolFamily(this.deviceProfile.protocolFamily)
		this.log(
			'info',
			`[Profile] Active device profile: ${this.deviceProfile.displayName} (${this.deviceProfile.id}), protocol=${this.deviceProfile.protocolFamily}`,
		)

		this.updateActions()
		this.updateFeedbacks()
		this.updatePresets()
		this.updateVariableDefinitions()

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
		// L1：确保“执行闪烁”定时器在实例销毁时一并释放，避免 destroy 后仍然 fire
		if (this.flashTimer) {
			clearTimeout(this.flashTimer)
			this.flashTimer = undefined
		}
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

		// M2：以实际建立的连接 host 为准，而不是旧的 config.device。
		// 避免“将 Target IP 改回与 Device 同值时因 device 未变而不重连”。
		if (!deviceChanged && this.comm && this.config.host === this.connectedHost) {
			this.log('debug', '[Config] Same connected host, keeping existing connection')
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
			const modelIndex = getUdpModelIndex(rawModel, d.productType)
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
				// M5：无扫描结果且无手动 Target IP 时，明确提示用户而不是永远 Connecting
				if (!this.config.host) {
					this.updateStatus(InstanceStatus.BadConfig, 'No supported device found – enter a Target IP')
				}
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

			// H3：只在首次配置（Device 与 Target IP 均为空）时自动选一个设备；
			// 否则仅刷新设备列表，保留用户已选的 Device / 手填的 Target IP。
			const firstSetup = !this.config.device && !this.config.host
			if (!firstSetup) {
				const stillOnline = saved.find((d) => d.host === this.config.device)
				const nextConfig: ModuleConfig = { ...this.config, devices: saved }
				const devicesChanged = JSON.stringify(nextConfig.devices) !== JSON.stringify(this.config.devices)
				this.config = nextConfig
				if (devicesChanged) this.saveConfig(this.config)

				if (stillOnline) {
					// 目标仍在线：刷新 profile（型号可能扫描后才能确认）并将新 MAC 信息交给心跳
					this.applyDeviceProfile(stillOnline.rawModel, stillOnline.productType)
					if (this.comm) {
						this.comm.setTargetDevice(this.discoveredDevices.find((d) => d.host === stillOnline.host))
						if (this.comm.getStatus()) this.comm.startHeartbeat()
					}
				}
				// 目标离线：不自动抢接管——可能是用户手填的 Target IP 或临时重启的设备，
				// 交给心跳自己处理（设备回来时会自然恢复在线）。
				return
			}

			// 首次配置：默认选中扫描到的第一个设备，将 Device 与 Target IP 统一写入配置
			const target = saved[0]
			const nextConfig: ModuleConfig = {
				...this.config,
				device: target.host,
				host: target.host,
				devices: saved,
			}
			this.config = nextConfig
			this.saveConfig(this.config)

			// 型号/设备类型变化时切换产品档案（协议族或功能集可能不同）
			this.applyDeviceProfile(target.rawModel, target.productType)

			this.log(
				'info',
				`[Scan] First-time setup: Device="${target.name}" TargetIP=${target.host} (${saved.length} device(s) available)`,
			)

			// 首次识别到设备：自动连接到该设备
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

	/** 当前生效的产品档案（供 actions / feedbacks / presets 按功能分组裁剪） */
	public getDeviceProfile(): DeviceProfile {
		return this.deviceProfile
	}

	/** 当前产品可用的协议命令表（协议族命令表 + 产品覆盖） */
	public getProtocolCommands(): Record<string, ProtocolCommand> {
		return this.protocolCommands
	}

	/** 当前产品所属协议族（输入路数 / PIP 数量 / WIPE 数量 / 键值表等能力） */
	public getProtocolFamilyInfo(): ProtocolFamily {
		return this.protocolFamily
	}

	/** 记录本次注册的 action id（由 actions.ts 在注册完成后调用） */
	public setRegisteredActionIds(ids: string[]): void {
		this.registeredActionIds = new Set(ids)
	}

	/** 当前已注册的 action id 集合 */
	public getRegisteredActionIds(): Set<string> {
		return this.registeredActionIds
	}

	/**
	 * 主动获取一轮设备状态（仅对声明了 stateQueryKeys / queryAllOnConnect 的协议族生效，如 H4K）。
	 * 参考上位机 SharkH4kProModel：查询走【独立的 0x01xx 指令码】，payload 为空（不带 Param_Vaild），
	 * 设备用同一 CMD + Pack_Type=1 回全量；参数变化时设备也会用同一 CMD + Pack_Type=2 主动上报。
	 */
	public async queryDeviceState(): Promise<void> {
		if (!this.comm) return

		const family = this.protocolFamily
		let keys: string[]
		if (family.queryAllOnConnect) {
			// 所有带获取码的指令都查一遍（H4K：state/transition/luma/chroma/pip1/dsk/logo/audio）
			keys = Object.keys(this.protocolCommands).filter((k) => this.protocolCommands[k].get !== undefined)
			// state（0x0110，PGM/PVW/T-Bar）优先
			keys.sort((a, b) => (a === 'state' ? -1 : b === 'state' ? 1 : 0))
		} else {
			keys = family.stateQueryKeys ?? []
		}
		if (keys.length === 0) return

		this.log('info', `[Query] Requesting device state: ${keys.join(', ')}`)
		// 第一轮：上位机做法 —— 0x01xx 指令码 + 空 payload
		await this.sendQueryRound(keys, 'get')
		await new Promise((resolve) => setTimeout(resolve, 700))

		// 没回包的指令用控制码 + Param_Vaild(全 0) 再查一次（仅 H4K 开启：部分 H4K 固件只认控制码）
		// 0617 / 0605 不做重试，保持原有单轮查询行为
		if (!family.queryAllOnConnect) return
		const missing = keys.filter((key) => !this.hasRecentReply(key))
		if (missing.length > 0) {
			this.log('info', `[Query] No reply for ${missing.join(', ')}, retrying with control code + Param_Vaild=0`)
			await this.sendQueryRound(missing, 'set')
			await new Promise((resolve) => setTimeout(resolve, 700))
			const stillMissing = missing.filter((key) => !this.hasRecentReply(key))
			if (stillMissing.length > 0) {
				this.log('warn', `[Query] Still no reply: ${stillMissing.join(', ')}`)
			}
		}
	}

	/** 发送一轮查询：get = 0x01xx + 空 Data；set = 控制码 + Param_Vaild(全 0) */
	private async sendQueryRound(keys: string[], mode: 'get' | 'set'): Promise<void> {
		for (const key of keys) {
			const cmd = this.protocolCommands[key]
			if (!cmd || !this.comm) continue
			if (mode === 'get') {
				await this.comm.sendCommand(cmd.get, Buffer.alloc(0))
			} else {
				await this.comm.sendCommand(cmd.set, Buffer.alloc(4))
			}
			// 间隔发送，避免 UDP 拥塞或设备处理不过来
			await new Promise((resolve) => setTimeout(resolve, 150))
		}
	}

	/** 最近 3 秒内是否收到过该指令的回包/上报 */
	private hasRecentReply(key: string): boolean {
		const at = this.lastReplyAt.get(key)
		return at !== undefined && Date.now() - at < 3000
	}

	/** 协议命令中是否存在某字段（供 actions 按产品能力裁剪选项） */
	public hasField(commandKey: string, fieldName: string): boolean {
		return this.protocolCommands[commandKey]?.fields.some((f) => f.name === fieldName) ?? false
	}

	/** 按「字段名」下发协议设置指令；字段不存在时自动跳过，保证多协议共用同一套 action */
	public async sendProtocolField(
		commandKey: string,
		fieldName: string,
		value: number,
		label: string,
	): Promise<boolean> {
		const cmd = this.protocolCommands[commandKey]
		if (!cmd) {
			this.log('debug', `[Set] ${label}: command "${commandKey}" not supported by current device`)
			return false
		}
		const fieldIndex = cmd.fields.findIndex((f) => f.name === fieldName)
		if (fieldIndex < 0) {
			this.log('debug', `[Set] ${label}: field "${fieldName}" not supported by current device`)
			return false
		}
		return this.sendProtocolSet(commandKey, fieldIndex, value, label)
	}

	/**
	 * 依据设备原始型号切换产品档案。
	 * 档案变化时重新注册 action / feedback / preset，使不同产品的功能相互隔离。
	 */
	public applyDeviceProfile(rawModel: string | undefined, deviceType?: number): void {
		const next = getActiveProfile(rawModel, deviceType)
		if (next.id === this.deviceProfile.id) return

		this.deviceProfile = next
		this.protocolCommands = buildProtocolCommands(next)
		this.protocolFamily = getProtocolFamily(next.protocolFamily)
		this.log(
			'info',
			`[Profile] Device profile -> ${next.displayName} (${next.id}), protocol=${next.protocolFamily}, Dev_Type=${next.udpDevType}`,
		)

		this.updateActions()
		this.updateFeedbacks()
		this.updatePresets()
		this.updateVariableDefinitions()
	}

	/** 把扫描结果转成 Device 下拉的选项：只显示已建档型号，值为设备 IP */
	private buildDeviceChoices(): DeviceChoice[] {
		return this.discoveredDevices
			.filter((device) => matchDeviceProfile(device.model, device.productType))
			.map((device) => ({
				host: device.host,
				label: resolveDeviceModel(device.model, device.productType),
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
			const allDevices = scanner.getDiscoveredDevices()
			// 仅保留已在产品档案中建档的型号，避免未知设备（如 SE2017）进入下拉框
			const devices = allDevices.filter((d) => matchDeviceProfile(d.model, d.productType))
			// M4：扫描结果为空时，保留先前的设备列表，避免下拉框 / MAC 信息丢失
			if (devices.length > 0) {
				this.discoveredDevices = devices
			}

			const ignored = allDevices.filter((d) => !matchDeviceProfile(d.model, d.productType))
			if (ignored.length > 0) {
				this.log(
					'warn',
					`[Scan] Ignored ${ignored.length} unsupported device(s): ${ignored.map((d) => `${d.model}@${d.host}`).join(', ')} (可在配置里手动指定 Device Model 并手填 Target IP)`,
				)
			}

			if (devices.length === 0) {
				this.log('warn', '[Scan] No supported device found')
				return []
			}

			this.log('debug', `[Scan] Found ${devices.length} supported device(s):`)
			for (const device of devices) {
				this.log(
					'debug',
					`[Scan]   ${device.host} -> model="${device.model}" (${resolveDeviceModel(device.model, device.productType)})`,
				)
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
		// 依据扫描到的型号（或设备类型标识）切换产品档案
		this.applyDeviceProfile(targetDevice?.model, targetDevice?.productType)
		const modelLabel = targetDevice
			? resolveDeviceModel(targetDevice.model, targetDevice.productType)
			: 'Unknown (manual IP)'

		this.log('info', '========================================')
		this.log('info', 'Establishing UDP connection to device')
		this.log('info', `  Model: ${modelLabel}`)
		this.log('info', `  IP: ${this.config.host}`)
		this.log('info', `  Port: ${DEVICE_PORT}`)
		this.log('info', '========================================')

		this.comm = new CommunicationManager({
			host: this.config.host,
			port: DEVICE_PORT,
			// H4K 无 0xEEEE 心跳，用协议内的 0x0001 做在线探测；其它协议族保持原逻辑
			probeCommand: this.protocolFamily.probeCommand,
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
					// M6：预设已在 init / applyDeviceProfile 中注册，不随在线状态摇予。
					// L2：重连后重新拉起闪烁（若 FTB/MUTE/Freeze 仍处于激活态）。
					this.updateBlink()
					// 主动获取一轮设备状态（H4K 无 0x0110 全量上报）
					void this.queryDeviceState()
				} else {
					this.log('warn', `Connection status: ${status} - ${message || 'unknown'}`)
					this.setVariableValues({ connection_status: 'Disconnected' })
					// M6：不再因临时离线而清空预设，避免预设区域在展示时“突然消失”。
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

		// M2：记录当前正在建立的 host，供 configUpdated 对比判断是否需要重连
		this.connectedHost = this.config.host

		void this.comm.connect()
	}

	private destroyConnection(): void {
		if (this.comm) {
			this.comm.disconnect()
			this.comm = undefined
		}
		this.connectedHost = undefined
		if (this.blinkTimer) {
			clearInterval(this.blinkTimer)
			this.blinkTimer = undefined
			// L2：销毁时相位复位，使重连后能从头开始闪烁，不会因残留 off 相位造成“不闪”
			this.deviceState.blinkOn = true
		}
	}

	/** 发送协议“设置指令”（Data = Param_Vaild(参数索引) + 值） */
	public async sendProtocolSet(commandKey: string, fieldIndex: number, value: number, label: string): Promise<boolean> {
		if (!this.comm) {
			this.log('error', `[Set] Cannot set ${label}: communication not initialized`)
			return false
		}
		const cmd = this.protocolCommands[commandKey]
		if (!cmd) {
			this.log('error', `[Set] Unknown command: ${commandKey}`)
			return false
		}
		const data = buildSetData(cmd, fieldIndex, value, this.protocolFamily.paramValidMode)
		if (data.length === 0) {
			this.log('error', `[Set] ${label}: invalid field index ${fieldIndex}`)
			return false
		}
		// 只输出命令/字段/值；Param_Vaild（报文头部字节）仅本地调试时输出
		const validInfo = LOG_RAW_PACKETS ? `, valid=0x${data.readUInt32BE(0).toString(16)}` : ''
		this.log(
			'info',
			`[Set] ${label} -> ${value} (cmd=0x${cmd.set.toString(16).padStart(4, '0')}, field=${fieldIndex}${validInfo})`,
		)
		const ok = await this.comm.sendCommand(cmd.set, data)
		if (ok && this.pendingFlashKey) this.flash(this.pendingFlashKey)
		return ok
	}

	private handleDeviceData(data: Buffer, host: string, port: number, cmd?: number, session?: number): void {
		this.log('debug', `Device data from ${host}:${port}, length: ${data.length} bytes`)
		// onData 回调传入的已经是 payload（Data 段，偏移 25 起）。
		// H4K（parseQueryReplies）：直接按 payload 解析，这样 Pack_Type=1 的查询应答才能同步状态；
		// 0617/0605：保持历史行为（原逻辑再当整帧解析一次），不改旧族的状态同步路径。
		const payload: Buffer | undefined = this.protocolFamily.parseQueryReplies ? data : UDPParser.parse(data)?.data
		const response = parseDeviceResponse(data.toString('ascii'), cmd, session, data, {
			legacyPowerCommands: this.protocolFamily.legacyPowerCommands,
		})
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
			onCustomData: (custom) => {
				// 按设备回包同步状态（传入解析后的 payload）
				if (payload && payload.length > 0) {
					this.syncSwitchState(custom.cmd, payload)
				} else {
					this.log(
						'debug',
						`[Device] Custom data - Cmd: 0x${custom.cmd.toString(16).padStart(4, '0')}${LOG_RAW_PACKETS ? `, Raw: ${custom.raw}` : ''}`,
					)
				}
			},
		})
	}

	private handleDeviceReport(packet: ParsedPacket): void {
		// mapped：该上报 CMD 能匹配到协议表里的哪个“获取指令”（匹配不到就是命令表里没建档）
		const mapped = Object.keys(this.protocolCommands).find((k) => this.protocolCommands[k].get === packet.cmd)
		this.log(
			'debug',
			`[Report] Device report - Cmd: 0x${packet.cmd.toString(16).padStart(4, '0')}, Type: 0x${packet.type.toString(16)}, Data(${packet.data.length}B)${LOG_RAW_PACKETS ? `: ${packet.data.toString('hex')}` : ''}, mapped=${mapped ?? 'NONE'}`,
		)
		// 按设备主动上报同步 PGM/PVW 当前值
		this.syncSwitchState(packet.cmd, packet.data)
	}

	/**
	 * 根据设备主动上报/回包同步状态。
	 * - cmd=0x000a：切换台状态（Data = PGM, PVW, MV）
	 * - cmd=0x0110：状态上报，字节布局按协议族（见 ProtocolFamily.stateReport）
	 *     0617：10B [0]PGM [1]PVW [2]WIPE [3]SPEED [4]FTB [5]Freeze [6..7]T_Bar_val [8..9]b_bar_pos
	 *     H4K ：9B  [0]PGM [1]PVW [2]WIPE [3]SPEED [4]FTB [5]Freeze [6]T_Bar_Pos [7..8]T_Bar_Val
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

		const spec = this.protocolFamily.stateReport
		if (cmd !== 0x0110 || !spec) {
			this.handleGetReport(cmd, data)
			return
		}
		// 设备主动上报（Pack_Type=2）只带字段本身；主动查询回包（Pack_Type=1）可能多带
		// 4 字节 Param_Vaild 前缀，按实际长度判定字段起始偏移。
		const base = data.length >= spec.size + 4 ? 4 : 0
		if (data.length < spec.size + base) {
			this.log('debug', `[Report 0x0110] payload too short: ${data.length}B (need ${spec.size + base}B)`)
			return
		}

		// 按协议族布局取值（H4K 的 T_Bar 位置/值顺序不同）
		const readField = (f?: { offset: number; size: number }): number => {
			if (!f) return 0
			return f.size === 1 ? data[base + f.offset] : data.readUInt16BE(base + f.offset)
		}
		const pgmVal = data[base + spec.pgm]
		const pvwVal = data[base + spec.pvw]
		const wipeMode = data[base + spec.wipeMode]
		const speedMode = data[base + spec.speedMode]
		const ftbState = data[base + spec.ftb]
		const freezeState = data[base + spec.freeze]
		const tBarPos = readField(spec.tBarPos)
		const tBarVal = readField(spec.tBarValue)
		const bBarPos = readField(spec.bBarPos)
		this.log(
			'info',
			`[Report 0x0110] PGM=${pgmVal}, PVW=${pvwVal}, WIPE=${wipeMode}, SPEED=${speedMode}, FTB=${ftbState}, Freeze=${freezeState}, T_Bar_Pos=${tBarPos}, T_Bar=${tBarVal}, b_bar_pos=${bBarPos} (${data.length}B, offset ${base})`,
		)

		// 1) PGM / PVW 当前源（按协议族的输入路数换算 Pattern）→ 同步按钮颜色
		this.lastReplyAt.set('state', Date.now())
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

		// 3) T-Bar 位置：以原始值（0~tBarMax，H4K 为 0~4095）为基准，显示换算成 0~500
		const tBarMax = this.protocolFamily.tBarMax ?? 4095
		const reported = Math.min(Math.max(tBarVal, 0), tBarMax)
		this.lastReportedTBar = reported
		// H4K（parseQueryReplies）：本地刚下发过的锁定期内、或回读与本地目标差异在一个档位内时，
		// 不被回读覆盖——否则设备平滑/标定误差会让下一次 ±step 的基准漂移，
		// 表现就是“点 10 档却走不到 10 档”。差异较大则视为物理推杆操作，跟随同步。
		const tbarTolerance = Math.max(Math.round(tBarMax * 0.04), 16)
		const holdLocalTBar =
			this.protocolFamily.parseQueryReplies === true &&
			(Date.now() < this.tbarHoldUntil || Math.abs(reported - this.tbarRaw) <= tbarTolerance)
		if (!holdLocalTBar) this.tbarRaw = reported
		const disp = tBarMax > 0 ? Math.round((this.tbarRaw * 500) / tBarMax) : 0
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

	/** Key Type（0x0130）值 -> 文本：0=PIP / 1=Luma / 2=Chroma / 3=DSK */
	public keyTypeLabel(v: number): string {
		return ['PIP', 'LUMA', 'CHROMA', 'DSK'][v] ?? `UNKNOWN(${v})`
	}

	/** 是否为 PIP/LUMA/CHROMA/DSK 及其 ON AIR 按键（用于刷新 0x0130 激活态） */
	private isKeyModuleKey(keyVal: number): boolean {
		const k = this.protocolFamily.keyMap
		const groups = [k.pip, k.pipOnAir, k.luma, k.lumaOnAir, k.chroma, k.chromaOnAir, k.dsk, k.dskOnAir]
		return keyVal > 0 && groups.includes(keyVal)
	}

	/** 主动查询一次 Key Type（0x0130 空 payload），用于按 Key 键后的激活态刷新（仅 H4K） */
	public async queryKeyTypeOnce(): Promise<void> {
		if (!this.comm) return
		const cmd = this.protocolCommands['keyType']
		if (!cmd) return
		await this.comm.sendCommand(cmd.get, Buffer.alloc(0))
	}

	/**
	 * 本地先行标记激活层（不发 0x0030），400ms 后以 0x0130 回读校准。
	 * 仅用于 H4K；旧族无 keyType 命令直接返回。
	 */
	public markKeyTypeLocal(k: number): void {
		if (!this.protocolCommands['keyType']) return
		this.deviceState.keyType = k
		this.setVariableValues({ key_type: k, key_type_label: this.keyTypeLabel(k) })
		this.checkFeedbacks()
		setTimeout(() => {
			void this.queryKeyTypeOnce()
		}, 400)
	}

	/**
	 * 仅 H4K：PIP / LUMA / CHROMA 三者互斥，不能同时激活。
	 * 打开某一层之前把另外两层的 Status 置 0（DSK 是下游叠加，不参与互斥）。
	 * 旧族（0617/0605）没有 keyType 命令，直接返回，行为不变。
	 */
	public async closeOtherKeys(keep: string): Promise<void> {
		if (!this.protocolCommands['keyType']) return
		for (const k of ['pip1', 'luma', 'chroma']) {
			if (k === keep) continue
			if (!this.hasField(k, 'Status')) continue
			await this.sendProtocolField(k, 'Status', 0, `${k.toUpperCase()} OFF (mutex)`)
		}
	}

	/**
	 * 上报源值 -> 内部源值（1~N / 0xF0=Pattern1 / 0xF1=Pattern2，N 按协议族）。
	 * 0617 与 H4K 的 0x0110 均为 1 基：1~N = IN1~INn，N+1 = PAT1，N+2 = PAT2，0 = BLACK。
	 */
	private toSourceValue(v: number): number {
		const n = this.protocolFamily.inputCount
		const idx = v - 1
		if (idx >= 0 && idx < n) return idx + 1
		if (idx === n) return 0xf0
		if (idx === n + 1) return 0xf1
		return 0
	}

	/**
	 * 处理“获取指令”的回包/上报：
	 * - 设备主动上报（Pack_Type=2）：CMD 为同步指令码（如 0x0120）
	 * - 上位机主动获取（Pack_Type=1）：设备用【控制指令码】回全量（如 0x0020，见协议文档 3.2 通用说明）
	 *   设置成功时也会用同一控制指令码回 1 字节 Report Code，靠数据长度排除。
	 */
	private handleGetReport(cmd: number, data: Buffer): void {
		const commands = this.protocolCommands
		const hex = (v: number): string => `0x${v.toString(16).padStart(4, '0')}`

		// 1) 主动上报：CMD 就是同步指令码
		let key = Object.keys(commands).find((k) => commands[k].get === cmd)
		let source: 'report' | 'query' = 'report'

		// 2) 主动获取的回复：CMD 是控制指令码，且数据长度覆盖完整字段
		//    注意：1 字节一定是设置应答（Report Code），不能当成字段值（如 keyType 只有 1 个字段时会歧义）
		if (!key) {
			key = Object.keys(commands).find((k) => {
				const c = commands[k]
				if (c.set !== cmd || c.fields.length === 0) return false
				const need = c.fields.reduce((sum, f) => sum + f.size, 0)
				return data.length > 1 && data.length >= need
			})
			source = 'query'
		}

		if (!key) {
			// H4K：设置指令的应答（Data = 1 字节 Report Code），输出下来才能判断设备到底有没有接受
			if (this.protocolFamily.queryAllOnConnect && data.length === 1) {
				const isSetReply = Object.keys(commands).some((k) => commands[k].set === cmd)
				if (isSetReply) {
					this.log(
						'info',
						`[Reply] 0x${cmd.toString(16).padStart(4, '0')} Report Code=${data[0]} (${data[0] === 0 ? 'success' : 'fail'})`,
					)
					return
				}
			}
			// 记录未映射的上报/回包（如 H4K 的 0x0001/0x0002），便于排查协议差异
			// H4K 用 info 输出：设备主动上报了但命令表里没有对应“获取码”时必须看得见
			const unhandled = `[Report] Unhandled cmd=${hex(cmd)} (${data.length}B)${LOG_RAW_PACKETS ? ` data=${data.toString('hex')}` : ''}`
			if (this.protocolFamily.parseQueryReplies) this.log('info', unhandled)
			else this.log('debug', unhandled)
			return
		}

		if (source === 'query') {
			this.log('info', `[Query Reply] ${hex(cmd)} -> ${key} (${data.length}B)`)
		}
		this.applyGetReport(key, data)
		this.syncDerivedFromReport(key)
		this.lastReplyAt.set(key, Date.now())
	}

	/** 按字段长度通用拆包，存入 reportState（GET 回包布局与 SET 可能不同） */
	private applyGetReport(key: string, data: Buffer): void {
		const cmd = this.protocolCommands[key]
		// H4K 的 GET 与 SET 字段不一致（如 luma GET 16B / SET 21B、audio GET 29B / SET 34B）
		const getFields = cmd.getFields ?? cmd.fields
		const setFields = cmd.fields
		const lenOf = (fs: typeof getFields): number => fs.reduce((sum, f) => sum + f.size, 0)
		const getLen = lenOf(getFields)
		const setLen = lenOf(setFields)

		// 布局选择（仅 H4K）：
		// - 主动上报 / 查询应答用 GET 布局（0x0130 = 1B、0x0131 = 16B、0x0132 = 32B）
		// - 个别固件改用控制指令码上报且带 SET 布局尾部字段（含 Reset 等）
		// 按实际长度精确判定，避免多出的字节被当成前缀导致整段字段错位。
		// 0617/0605 保持历史行为（只用 GET 布局）。
		let fields = getFields
		let layout: 'GET' | 'SET' = 'GET'
		if (this.protocolFamily.parseQueryReplies && cmd.getFields && setLen !== getLen) {
			const isGetLen = data.length === getLen || data.length === getLen + 4
			const isSetLen = data.length === setLen || data.length === setLen + 4
			if (!isGetLen && isSetLen) {
				fields = setFields
				layout = 'SET'
			}
		}
		const need = lenOf(fields)
		// 主动上报（Pack_Type=2）只带字段本身；个别固件的查询回包会在前面多带 4 字节 Param_Vaild
		const base = need > 0 && data.length >= need + 4 ? 4 : 0
		const values: number[] = []
		let off = base
		for (const f of fields) {
			if (off + f.size > data.length) break
			let v = 0
			for (let i = 0; i < f.size; i++) v = (v << 8) | data[off + i]
			values.push(v)
			off += f.size
		}
		this.reportState[key] = values
		// H4K 打印“字段名=值”，直接可以看出每个上报字段到底解析成了什么；旧族保持原格式
		const detail = fields
			.slice(0, values.length)
			.map((f, i) => `${f.name}=${values[i]}`)
			.join(' ')
		const msg = this.protocolFamily.parseQueryReplies
			? `[Report] ${key} (0x${cmd.get.toString(16).padStart(4, '0')}, ${layout}) ${detail}`
			: `[Report] ${key} = [${values.join(', ')}]`
		this.log('info', `${msg} (${data.length}B, offset ${base})`)
	}

	/** 依据上报的获取指令刷新对应反馈/状态 */
	private syncDerivedFromReport(key: string): void {
		const vals = this.reportState[key] ?? []
		switch (key) {
			case 'transition': {
				this.verifyWipeReport(vals)
				// 各 Wipe 通道的样式值 -> 变量/反馈（0x0120 回读；H4K 3 组，0617 4 组）
				const wipeVars: Record<string, string> = {}
				for (let n = 1; n <= 4; n++) {
					const v = vals[n - 1]
					wipeVars[`wipe${n}_style`] = v === undefined ? '' : String(v)
					wipeVars[`wipe${n}_style_label`] = v === undefined ? '' : this.wipeStyleLabel(v)
				}
				this.setVariableValues(wipeVars)
				this.checkFeedbacks('wipe_active', 'wipe_style_active')
				break
			}
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
			case 'keyType': {
				// 0x0130：当前激活的 Key 模块（0=PIP / 1=Luma / 2=Chroma / 3=DSK）
				const kt = vals[0]
				if (kt !== undefined) {
					if (kt !== this.deviceState.keyType) {
						this.log('info', `[Key Type] Active module -> ${this.keyTypeLabel(kt)} (${kt})`)
					}
					this.deviceState.keyType = kt
					this.setVariableValues({ key_type: kt, key_type_label: this.keyTypeLabel(kt) })
				}
				this.checkFeedbacks('key_type_active')
				break
			}
			default:
				break
		}
	}

	/** 读取某“获取指令”解析后的字段值 */
	public getReportState(key: string): number[] {
		return this.reportState[key] ?? []
	}

	/**
	 * 取某“获取指令”回包里某字段的下标（按 GET 布局）。
	 * 反馈不能写死索引：H4K 的 LUMA/DSK 没有 Tie 字段，Status 在 0 而不是 1。
	 */
	public getReportFieldIndex(commandKey: string, fieldName: string): number {
		const cmd = this.protocolCommands[commandKey]
		if (!cmd) return -1
		const fields = cmd.getFields ?? cmd.fields
		return fields.findIndex((f) => f.name === fieldName)
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

		const { cmd, data } = buildCommand(commandId, params, { keyPressFormat: this.protocolFamily.keyPressFormat })

		// 对于KEY_PRESS命令，根据keyVal映射到具体的按钮名称
		let actionLabel = commandId
		if (commandId === 'KEY_PRESS' && params?.keyVal !== undefined) {
			const keyVal = params.keyVal as number
			actionLabel = this.getButtonNameByKeyVal(keyVal)
		}

		this.log('info', `[Action] Executing: ${actionLabel} -> Command: 0x${cmd.toString(16).padStart(4, '0')}`)
		if (LOG_RAW_PACKETS) this.log('debug', `[Action] Data hex: ${data.toString('hex')}`)
		const success = await this.comm.sendCommand(cmd, data)

		if (success) {
			this.log('info', `[Action] ${actionLabel} sent successfully`)
			// 乐观更新 + 执行闪烁反馈（key 由动作包裹器统一设置）
			const keyVal = params?.keyVal as number | undefined
			if (commandId === 'KEY_PRESS' && typeof keyVal === 'number') {
				this.optimisticKey(keyVal)
				// H4K：按下 PIP/LUMA/CHROMA/DSK（含 ON AIR）键后刷新当前激活的 Key 模块（0x0130）
				if (this.protocolCommands['keyType'] && this.isKeyModuleKey(keyVal)) {
					setTimeout(() => {
						void this.queryKeyTypeOnce()
					}, 300)
				}
			}
			if (this.pendingFlashKey) this.flash(this.pendingFlashKey)
		} else {
			this.log('error', `[Action] Failed to send: ${actionLabel}`)
		}

		return success
	}

	/**
	 * 发送成功后的乐观状态更新（以设备上报为准，随后会被校正）。
	 * 键值表按当前协议族取（0617 与 H4K 的键值完全不同）。
	 */
	private optimisticKey(keyVal: number): void {
		const keys = this.protocolFamily.keyMap
		const pgmIdx = keys.pgm.indexOf(keyVal)
		const pvwIdx = keys.pvw.indexOf(keyVal)
		const pgmPatternIdx = keys.pgmPattern.indexOf(keyVal)
		const pvwPatternIdx = keys.pvwPattern.indexOf(keyVal)
		const wipeIdx = keys.wipe.indexOf(keyVal)

		if (pgmIdx >= 0) {
			this.deviceState.pgmSource = pgmIdx + 1
			this.applySwitchFeedback(0x0110)
		} else if (pgmPatternIdx >= 0) {
			this.deviceState.pgmSource = pgmPatternIdx === 0 ? 0xf0 : 0xf1
			this.applySwitchFeedback(0x0110)
		} else if (pvwIdx >= 0) {
			this.deviceState.pvwSource = pvwIdx + 1
			this.applySwitchFeedback(0x0110)
		} else if (pvwPatternIdx >= 0) {
			this.deviceState.pvwSource = pvwPatternIdx === 0 ? 0xf0 : 0xf1
			this.applySwitchFeedback(0x0110)
		} else if (keyVal === keys.auto) {
			// L4：AUTO 视为瞬时动作——短暂点亮后自动释放，避免“常亮不灭”。
			this.deviceState.autoActive = true
			this.checkFeedbacks('auto_active')
			setTimeout(() => {
				this.deviceState.autoActive = false
				this.checkFeedbacks('auto_active')
			}, 800)
		} else if (keyVal === keys.ftb) {
			this.deviceState.ftbActive = !this.deviceState.ftbActive
			this.checkFeedbacks('ftb_active')
			// L3：本地翻转后同步拉起/停止闪烁，避免“常亮不闪”
			this.updateBlink()
		} else if (keyVal === keys.mute) {
			this.deviceState.muteActive = !this.deviceState.muteActive
			this.checkFeedbacks('mute_active')
			this.updateBlink()
		} else if (wipeIdx >= 0) {
			this.deviceState.wipeMode = wipeIdx + 1
			this.checkFeedbacks('wipe_active')
		} else if (keyVal === keys.mix) {
			this.deviceState.wipeMode = 5
			this.checkFeedbacks('wipe_active')
		} else if (keyVal === keys.dip) {
			this.deviceState.wipeMode = 6
			this.checkFeedbacks('wipe_active')
		} else if (keyVal === keys.freeze) {
			this.deviceState.freezeActive = !this.deviceState.freezeActive
			this.checkFeedbacks('freeze_active')
			this.updateBlink()
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
		// 键值表按当前协议族取（0617 与 H4K 键值完全不同）
		const keys = this.protocolFamily.keyMap
		const indexLabel = (arr: number[], prefix: string): string | undefined => {
			const i = arr.indexOf(keyVal)
			return i >= 0 ? `${prefix}${i + 1}` : undefined
		}
		const named: Array<[number, string]> = [
			[keys.cut, 'CUT'],
			[keys.auto, 'AUTO'],
			[keys.ftb, 'FTB'],
			[keys.mute, 'MUTE'],
			[keys.speed1, 'SPEED1'],
			[keys.speed2, 'SPEED2'],
			[keys.mix, 'MIX'],
			[keys.dip, 'DIP'],
			[keys.flipFlop, 'FLIP-FLOP'],
			[keys.freeze, 'FREEZE'],
			[keys.chroma, 'CHROMA'],
			[keys.chromaOnAir, 'CHROMA_ON_AIR'],
			[keys.luma, 'LUMA'],
			[keys.lumaOnAir, 'LUMA_ON_AIR'],
			[keys.pip, 'PIP'],
			[keys.pipOnAir, 'PIP_ON_AIR'],
			[keys.dsk, 'DSK'],
			[keys.dskOnAir, 'DSK_ON_AIR'],
			[keys.logo, 'LOGO'],
			[keys.logoOnAir, 'LOGO_ON_AIR'],
		]

		return (
			indexLabel(keys.pgm, 'PGM') ??
			indexLabel(keys.pgmPattern, 'PGM_PATTERN') ??
			indexLabel(keys.pvw, 'PVW') ??
			indexLabel(keys.pvwPattern, 'PVW_PATTERN') ??
			indexLabel(keys.wipe, 'WIPE') ??
			named.find(([v]) => v !== 0 && v === keyVal)?.[1] ??
			indexLabel(keys.fKeys, 'F') ??
			`UNKNOWN_KEY_${keyVal}`
		)
	}

	/**
	 * 移动 T-Bar（0x0010）：0617 为 Param_Vaild=1 + T_Bar_val；H4K 为位域 + Key_type=2 + Key_val
	 * 对外显示刻度 0~500，内部按 0~tBarMax（4095）等比例换算后下发。
	 * direction: 1=Up / 0=Down
	 */
	public async moveTBar(direction: number, step: number): Promise<boolean> {
		const tBarMax = this.protocolFamily.tBarMax ?? 4095
		// L5：未连接时不做乐观更新，避免变量与设备真值不一致
		if (!this.comm?.getStatus()) {
			this.log('warn', '[T-Bar] Not connected, ignoring move request')
			return false
		}
		// 以原始值（0~tBarMax）为基准递增，避免 0~500 来回换算的累计误差
		const prevRaw = this.tbarRaw
		const stepRaw = Math.max(1, Math.round((step * tBarMax) / 500))
		const raw = Math.min(Math.max(direction === 1 ? this.tbarRaw + stepRaw : this.tbarRaw - stepRaw, 0), tBarMax)
		// 连续点击需要基准递进：发送前先乐观更新 tbarRaw，发送失败时回滚
		this.tbarRaw = raw
		// 本地基准锺 5s：期间设备回读不覆写 tbarRaw，保证连续点击严格按 step 递增
		this.tbarHoldUntil = Date.now() + 5000
		const next = tBarMax > 0 ? Math.round((raw * 500) / tBarMax) : 0
		// H4K：0x0010 + 动态 valid + Key_type=2 + 推杆值；0617：Param_Vaild=1 + T_Bar_val
		const format = this.protocolFamily.keyPressFormat
		const percent = tBarMax > 0 ? Math.round((raw * 100) / tBarMax) : 0
		const mode: TBarSendMode = this.protocolFamily.tBarSendMode ?? 'pos'
		this.log(
			'info',
			`[T-Bar] ${direction === 1 ? 'Up' : 'Down'} by ${step} -> ${next}/500 (raw=${raw}, ` +
				(format === 'keytype' ? this.tbarModeDesc(mode, raw, percent) : 'Param_Vaild=1/T_Bar_val') +
				')',
		)
		const ok = await this.sendToDevice('KEY_PRESS', { tBarVal: raw, tBarMode: mode })
		if (!ok) {
			// 发送失败 → 回滚本地基准，不更新显示变量
			this.tbarRaw = prevRaw
			this.tbarHoldUntil = 0
			return false
		}
		// 发送成功后才写回显示与变量
		this.deviceState.tbarValue = next
		this.setVariableValues({ tbar_value: String(next) })
		// 推杆下发后回读 0x0110 校验；设备推杆有平滑/限速，延后 800ms 再读（上位机实测：设 3767 回读 3427）
		if (format === 'keytype' && this.protocolFamily.stateReport) {
			const seq = ++this.tbarSendSeq
			setTimeout(() => {
				void this.verifyTBarApplied(raw, mode, seq)
			}, 800)
		}
		return true
	}

	/** 主动查询一次设备状态（0x0110 空 payload），用于推杆/切换后的回读确认 */
	public async queryStateOnce(): Promise<void> {
		if (!this.comm) return
		const stateCmd = this.protocolCommands['state']
		await this.comm.sendCommand(stateCmd?.get ?? 0x0110, Buffer.alloc(0))
	}

	/** 主动查询一次 Transition 状态（0x0120 空 payload），用于核对 Wipe1/2/3 是否落到正确通道（仅 H4K） */
	public async queryTransitionOnce(): Promise<void> {
		if (!this.comm) return
		const cmd = this.protocolCommands['transition']
		if (!cmd) return
		await this.comm.sendCommand(cmd.get, Buffer.alloc(0))
	}

	/** 各 Wipe 通道的样式值（[Wipe1, Wipe2, Wipe3, ...]，仅在收到 0x0120 回读后有值） */
	public getTransitionReport(): number[] {
		return this.reportState['transition'] ?? []
	}

	/** WIPE 样式值 -> 文本（按协议族枚举查表，查不到时回退为数字） */
	private wipeStyleLabel(v: number): string {
		const styles = this.protocolFamily.wipeStyles ?? []
		return styles.find((s) => s.id === v)?.label ?? String(v)
	}

	/** 登记 WIPE 样式写后校验目标（仅 H4K 的 trans_wipeN 动作会调用） */
	public armWipeCheck(n: number, value: number): void {
		const before = (this.reportState['transition'] ?? []).slice(0, 3)
		this.pendingWipeCheck = { n, value, before, at: Date.now() }
	}

	/**
	 * 用 0x0120 回读值校验下发的 WIPE 样式：
	 * 日志会输出下发前后的 Wipe1/2/3 与发生变化的字段，便于判断字段映射是否错位
	 * （若发送 Wipe2 但另一个字段变了 → 设备的划像编号与字段不对应）。
	 */
	private verifyWipeReport(vals: number[]): void {
		const pending = this.pendingWipeCheck
		if (!pending) return
		this.pendingWipeCheck = undefined
		if (Date.now() - pending.at > 5000) return
		const before = pending.before.length === 3 ? pending.before : []
		const after = vals.slice(0, 3)
		const changed = after
			.map((v, i) => ({ i, v, old: before[i] }))
			.filter((c) => before.length === 0 || c.v !== c.old)
			.map((c) => `Wipe${c.i + 1}:${before[c.i] ?? '?'}->${c.v}`)
		const actual = vals[pending.n - 1]
		const ok = actual === pending.value
		this.log(
			ok ? 'info' : 'warn',
			`[Wipe${pending.n}] sent=${pending.value} | before=[${before.join(', ')}] after=[${after.join(', ')}] ` +
				`changed=[${changed.join(', ') || '无'}] -> Wipe${pending.n}=${actual} ${ok ? 'OK' : 'MISMATCH'}`,
		)
	}

	/** 推杆下发方式 -> 报文内容描述（便于对照日志） */
	private tbarModeDesc(mode: TBarSendMode, raw: number, percent: number): string {
		switch (mode) {
			case 'pos':
				return `Key_type=2, Key_Pos=${percent}%/valid=0x05（Mode=pos）`
			case 'both':
				return `Key_type=2, Key_Val=${raw}+Key_Pos=${raw <= 0 ? 0 : raw >= 4095 ? 2 : 1}(档位)/valid=0x07（Mode=both）`
			case 'valPct':
				return `Key_type=2, Key_Val=${percent}(百分比)/valid=0x03（Mode=valPct）`
			default:
				return `Key_type=2, Key_Val=${raw}/valid=0x03（Mode=val）`
		}
	}

	/** 回读值是否与目标值一致（设备推杆有平滑/限速，容差取 10%，但“未动”仍判失败） */
	private tbarMatches(device: number, target: number): boolean {
		if (device < 0) return false
		const tBarMax = this.protocolFamily.tBarMax ?? 4095
		const tolerance = Math.max(Math.round(tBarMax * 0.1), 16)
		// 目标非 0 时，设备仍报 0 说明根本没接受（不能因落入 ±10% 容差就判成功）
		if (target > 0 && device === 0) return false
		return Math.abs(device - target) <= tolerance
	}

	/**
	 * 推杆回读校验（严格按文档 3.1.3）：
	 * Param_Vaild 4 字节：Bit0=Key_type、Bit1=Key_val（Bit2 及以上保留）；
	 * 推杆时 Key_type=2，推杆数据填在 Key_val。
	 * 下发后主动查询 0x0110，用设备上报值（而非本地乐观值）判定是否真的生效；
	 * 未生效不改用其他编码，只把显示恢复为设备真值，避免 UI 与设备不一致。
	 */
	private async verifyTBarApplied(target: number, mode: TBarSendMode, seq: number): Promise<void> {
		const tBarMax = this.protocolFamily.tBarMax ?? 4095
		// 连续点击时只校验最后一次（新的操作会开启新序号）
		if (seq !== this.tbarSendSeq) return

		const got = await this.waitFreshStateReport()
		if (seq !== this.tbarSendSeq) return
		const deviceRaw = this.lastReportedTBar
		if (!got) {
			this.log('warn', `[T-Bar] No fresh 0x0110 reply; cannot verify target ${target} (last known ${deviceRaw})`)
			return
		}
		if (this.tbarMatches(deviceRaw, target)) {
			this.log('info', `[T-Bar] Verified: device T_Bar=${deviceRaw} (target ${target}, mode=${mode})`)
			return
		}
		this.log(
			'warn',
			`[T-Bar] 未生效: 下发 ${target}, 设备回读 ${deviceRaw} (mode=${mode}); ` +
				`若持续为 0，说明设备不接受该值（或推杆数据量程/单位与 0~${tBarMax} 不符），已恢复显示为设备真值`,
		)
		this.tbarRaw = Math.max(deviceRaw, 0)
		this.tbarHoldUntil = 0 // 释放本地基准锁定，让回读重新接管
		const disp = tBarMax > 0 ? Math.round((this.tbarRaw * 500) / tBarMax) : 0
		this.deviceState.tbarValue = disp
		this.setVariableValues({ tbar_value: String(disp) })
	}

	/** 主动查询 0x0110 并等待一条“新”的回包（最多约 1s），返回是否收到 */
	private async waitFreshStateReport(): Promise<boolean> {
		const before = this.lastReplyAt.get('state') ?? 0
		await this.queryStateOnce()
		for (let i = 0; i < 20; i++) {
			await new Promise((resolve) => setTimeout(resolve, 50))
			if ((this.lastReplyAt.get('state') ?? 0) > before) return true
		}
		return false
	}

	public getDeviceConnectionStatus(): boolean {
		return this.comm?.getStatus() ?? false
	}

	public getDeviceState(): DeviceState {
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

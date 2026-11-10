import { AsyncLocalStorage } from 'node:async_hooks'
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
import { buildProtocolCommands, getActiveProfile, getProfileById, matchDeviceProfile } from './devices/index.js'
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
	// Product profile of the current device: decides the available feature groups and command table
	private deviceProfile: DeviceProfile = getActiveProfile(undefined)
	private protocolCommands: Record<string, ProtocolCommand> = buildProtocolCommands(this.deviceProfile)
	private protocolFamily: ProtocolFamily = getProtocolFamily(this.deviceProfile.protocolFamily)
	// Ids of the actions currently registered (presets drop buttons referencing missing actions)
	private registeredActionIds: Set<string> = new Set()
	private comm: CommunicationManager | undefined
	// Devices found by the last UDP broadcast scan, used to fill the Device dropdown
	private discoveredDevices: DeviceInfo[] = []
	// Scan mutex, so overlapping scans are not started
	private scanInProgress = false
	// L1: the scanner of the scan in progress, so destroy() can abort it
	private scanner: CommunicationManager | undefined
	// Whether the instance is alive, so scan results completing after destroy() are discarded
	private instanceAlive = false
	// Host of the current connection (configUpdated uses it to decide whether a reconnect is needed)
	private connectedHost: string | undefined
	private deviceState: DeviceState = {
		pgmSource: 0, // 1-4=HDMI1-4, 0xF0-0xF1=Pattern1-2
		pvwSource: 0,
		mvState: 0,
		// Current T-Bar value (0~500 display scale, 0~4095 internally)
		tbarValue: 0,
		// Wipe mode (1~6, from the 0x0110 report)
		wipeMode: 0,
		// Speed mode (1~2, from the 0x0110 report)
		speedMode: 0,
		// Freeze state (0/1, from the 0x0110 report)
		freezeActive: false,
		// Key of the last successfully executed action (drives the action-flash feedback)
		lastAction: '',
		// FTB/MUTE blink phase
		blinkOn: true,
		// AUTO/FTB/MUTE active state (flipped locally after a key press, used by feedbacks)
		muteActive: false,
		ftbActive: false,
		autoActive: false,
		// Currently active key module (0x0130: 0=PIP / 1=Luma / 2=Chroma / 3=DSK; -1=unknown, H4K only)
		keyType: -1,
	}
	// Action flash timer
	private flashTimer: ReturnType<typeof setTimeout> | undefined
	// L2: one-shot timers started by button presses, cancelled on destroy()
	private pendingTimers = new Set<ReturnType<typeof setTimeout>>()
	// FTB/MUTE blink timer
	private blinkTimer: ReturnType<typeof setInterval> | undefined
	// Parsed field values of every "get command" (0x0120~0x01B0) report/reply (in features.ts field order)
	private reportState: Record<string, number[]> = {}
	// Raw T-Bar value (0~tBarMax, 0~4095 on H4K); used as the base for sending and display
	private tbarRaw = 0
	// T-Bar send sequence: only the last one is verified on rapid clicks, avoiding log spam and resends
	private tbarSendSeq = 0
	// T-Bar value reported by the device (written only from a parsed 0x0110; -1 = not received yet)
	private lastReportedTBar = -1
	// Local T-Bar base lock expiry: while clicking on H4K, read-backs must not override tbarRaw (otherwise the base drifts)
	private tbarHoldUntil = 0
	// Time of the last reply/report per get command (used by the query retry check)
	private lastReplyAt: Map<string, number> = new Map()
	// Wipe style write check (H4K only): records the WipeN just sent, the target value and the three Wipe values before
	private pendingWipeCheck?: { n: number; value: number; before: number[]; at: number }
	// L7: per-action flash key, isolated per async context so concurrent actions cannot affect each other
	private flashKeyContext = new AsyncLocalStorage<string>()

	constructor(internal: unknown) {
		super(internal)
	}

	async init(config: ModuleConfig, isFirstInit: boolean): Promise<void> {
		this.config = config
		this.instanceAlive = true

		this.log('info', 'Instance initialized')

		// Fill the dropdown with the persisted device list first, so the config panel is usable immediately
		this.discoveredDevices = this.savedDevicesToInfo(config.devices)

		// Manual Device Model (when enabled) always wins; otherwise the scanned model / fallback is used.
		const initialDevice = this.discoveredDevices.find((d) => d.host === config.host)
		const fallbackDevice = initialDevice ?? this.discoveredDevices[0]
		const manualProfileId = config.manualModel ? config.deviceModel : undefined
		if (config.manualModel && !manualProfileId) {
			this.log('warn', '[Config] Manual Device Model is on but no model selected, using auto-detect')
		}
		this.deviceProfile =
			getProfileById(manualProfileId) ?? getActiveProfile(fallbackDevice?.model, fallbackDevice?.productType)
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

		// Connect immediately when an address exists (do not block on the scan, see below)
		if (this.config.host) {
			this.updateStatus(InstanceStatus.Connecting, 'Connecting to device...')
			this.setupConnection()
		} else {
			this.updateStatus(InstanceStatus.Connecting, 'Scanning for supported devices...')
		}

		// Scan only on first initialisation, or when there is no persisted device list yet.
		// A dev-mode reload or a config save runs init again with isFirstInit=false; scanning
		// every time made the module look like it kept re-discovering devices.
		// Note: it must NOT be awaited - a scan takes seconds and blocking init would exceed
		// Companion's IPC timeout, making the module look like it failed to initialise and restart.
		if (isFirstInit || this.discoveredDevices.length === 0) void this.scanDevicesOnce()
	}

	async destroy(): Promise<void> {
		this.instanceAlive = false
		// L1: abort a running scan first, otherwise its sockets keep broadcasting
		// after the connection has been destroyed.
		if (this.scanner) {
			this.scanner.disconnect()
			this.scanner = undefined
		}
		this.destroyConnection()
		// Make sure the action-flash timer is released on destroy, so it cannot fire afterwards
		if (this.flashTimer) {
			clearTimeout(this.flashTimer)
			this.flashTimer = undefined
		}
		// L2: cancel every short follow-up timer started by a button press
		for (const t of this.pendingTimers) clearTimeout(t)
		this.pendingTimers.clear()
		this.log('debug', 'destroy')
	}

	/** Register a one-shot timer so destroy() can cancel it (L2). */
	public schedule(fn: () => void, ms: number): void {
		const t = setTimeout(() => {
			this.pendingTimers.delete(t)
			fn()
		}, ms)
		this.pendingTimers.add(t)
	}

	/**
	 * Run an action with its own flash key (L7).
	 * AsyncLocalStorage keeps the key in the action's async context, so two actions running at
	 * the same time never overwrite each other's key (the previous shared field could flash the
	 * wrong button or clear another action's key).
	 */
	public runWithFlashKey<R>(key: string, fn: () => R): R {
		return this.flashKeyContext.run(key, fn)
	}

	/**
	 * Called when the config is saved (Save button).
	 * A Device dropdown change syncs the Target IP and connects to that device (online state is tracked by the heartbeat).
	 */
	async configUpdated(config: ModuleConfig): Promise<void> {
		const previousDevice = this.config?.device
		const previousModel = this.config?.deviceModel ?? ''
		const previousManual = this.config?.manualModel ?? false
		const deviceChanged = !!config.device && config.device !== previousDevice
		// Turning the manual switch on/off also changes which protocol is used
		const modelChanged =
			(config.deviceModel ?? '') !== previousModel || (config.manualModel ?? false) !== previousManual

		this.config = config

		// Device changed: the Target IP must follow the selected device so the UI stays in sync
		if (deviceChanged) {
			this.log('info', `[Config] Device switched to ${config.device}, syncing Target IP and reconnecting`)
			this.config = { ...config, host: config.device }
			this.saveConfig(this.config)
		} else if (modelChanged) {
			this.log(
				'info',
				`[Config] Device model ${config.manualModel ? `manual (${config.deviceModel || 'auto-detect'})` : 'automatic'}, reconnecting`,
			)
		} else {
			this.log('info', `[Config] Reconnecting to ${config.host}`)
		}

		// M2: compare against the actually connected host instead of the old config.device.
		// This avoids "changing Target IP back to the Device value does not reconnect because device is unchanged".
		if (!deviceChanged && !modelChanged && this.comm && this.config.host === this.connectedHost) {
			this.log('debug', '[Config] Same connected host, keeping existing connection')
			return
		}

		this.reconnect()
	}

	/** Destroy the old connection and reconnect using the current config (including the heartbeat) */
	private reconnect(): void {
		this.destroyConnection()
		this.updateStatus(InstanceStatus.Connecting, 'Connecting to device...')
		this.setupConnection()
	}

	/** Restore the persisted device list into runtime structures (with MAC, so heartbeats work right after a restart) */
	private savedDevicesToInfo(saved: SavedDevice[] | undefined): DeviceInfo[] {
		return (saved ?? []).map((d) => {
			// Recompute Dev_Type from the raw model first, so mapping changes take effect automatically
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
	 * Scan the device list on first init, or when no persisted device list exists:
	 * - results go into discoveredDevices and are persisted to config, so they survive a restart
	 * - when no device is selected, the first one is selected and the Target IP follows it
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
				// M5: with no scan result and no manual Target IP, tell the user instead of staying in Connecting forever
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

			// H3: only auto-select a device on first setup (both Device and Target IP empty);
			// otherwise just refresh the list and keep the selected Device / manual Target IP.
			const firstSetup = !this.config.device && !this.config.host
			if (!firstSetup) {
				const stillOnline = saved.find((d) => d.host === this.config.device)
				const nextConfig: ModuleConfig = { ...this.config, devices: saved }
				const devicesChanged = JSON.stringify(nextConfig.devices) !== JSON.stringify(this.config.devices)
				this.config = nextConfig
				if (devicesChanged) this.saveConfig(this.config)

				if (stillOnline) {
					// Target still online: refresh the profile (the model may only be known after a scan) and give the new MAC to the heartbeat.
					// A manual Device Model still wins over the scanned model.
					const manualProfileId = this.config.manualModel ? this.config.deviceModel : undefined
					this.applyDeviceProfile(stillOnline.rawModel, stillOnline.productType, manualProfileId)
					if (this.comm) {
						this.comm.setTargetDevice(this.discoveredDevices.find((d) => d.host === stillOnline.host))
						if (this.comm.getStatus()) this.comm.startHeartbeat()
					}
				}
				// Target offline: do not take over - it may be a manually typed IP or a device that is rebooting.
				// The heartbeat handles it and the device comes back online when it returns.
				return
			}

			// First setup: select the first discovered device and write Device and Target IP into the config
			const target = saved[0]
			const nextConfig: ModuleConfig = {
				...this.config,
				device: target.host,
				host: target.host,
				devices: saved,
			}
			this.config = nextConfig
			this.saveConfig(this.config)

			// Switch the product profile when the model/device type changes (protocol family or feature set may differ).
			// A manual Device Model still wins over the scanned model.
			const manualProfileId = this.config.manualModel ? this.config.deviceModel : undefined
			this.applyDeviceProfile(target.rawModel, target.productType, manualProfileId)

			this.log(
				'info',
				`[Scan] First-time setup: Device="${target.name}" TargetIP=${target.host} (${saved.length} device(s) available)`,
			)

			// First identification of a device: connect to it automatically
			this.reconnect()
		} catch (error) {
			this.log('error', `[Scan] Unexpected scan failure: ${(error as Error).message}`)
		} finally {
			this.scanInProgress = false
		}
	}

	getConfigFields(): SomeCompanionConfigField[] {
		// The Device dropdown is filled from the UDP scan; the Target IP can be edited manually.
		// The AUTO SCAN entry shows the model detected for the current Target IP (if any).
		const currentHost = this.config?.host
		const detected = currentHost ? this.discoveredDevices.find((d) => d.host === currentHost) : undefined
		const detectedProfile = detected ? getActiveProfile(detected.model, detected.productType) : undefined
		return GetConfigFields(
			this.buildDeviceChoices(),
			detectedProfile ? { id: detectedProfile.id, name: detectedProfile.displayName } : undefined,
			this.config,
		)
	}

	/** Currently active product profile (actions / feedbacks / presets are filtered by its feature groups) */
	public getDeviceProfile(): DeviceProfile {
		return this.deviceProfile
	}

	/** Protocol command table available for this product (family table + product overrides) */
	public getProtocolCommands(): Record<string, ProtocolCommand> {
		return this.protocolCommands
	}

	/** Protocol family of the current product (input count / PIP count / wipe count / key map, etc.) */
	public getProtocolFamilyInfo(): ProtocolFamily {
		return this.protocolFamily
	}

	/** Record the action ids registered this time (called by actions.ts after registration) */
	public setRegisteredActionIds(ids: string[]): void {
		this.registeredActionIds = new Set(ids)
	}

	/** Ids of the currently registered actions */
	public getRegisteredActionIds(): Set<string> {
		return this.registeredActionIds
	}

	/**
	 * Query one round of device state (only for families declaring stateQueryKeys / queryAllOnConnect, e.g. H4K).
	 * Reference host app SharkH4kProModel: queries use the dedicated 0x01xx command codes with an empty payload
	 * (no Param_Vaild); the device answers with the same CMD + Pack_Type=1, and also sends Pack_Type=2 reports on changes.
	 */
	public async queryDeviceState(): Promise<void> {
		if (!this.comm) return

		const family = this.protocolFamily
		let keys: string[]
		if (family.queryAllOnConnect) {
			// Query every command that has a get code (H4K: state/transition/luma/chroma/pip1/dsk/logo/audio)
			keys = Object.keys(this.protocolCommands).filter((k) => this.protocolCommands[k].get !== undefined)
			// state (0x0110, PGM/PVW/T-Bar) first
			keys.sort((a, b) => (a === 'state' ? -1 : b === 'state' ? 1 : 0))
		} else {
			keys = family.stateQueryKeys ?? []
		}
		if (keys.length === 0) return

		this.log('info', `[Query] Requesting device state: ${keys.join(', ')}`)
		// First round: the host app approach - 0x01xx command code with an empty payload
		await this.sendQueryRound(keys, 'get')
		await new Promise((resolve) => setTimeout(resolve, 700))
		// L2: stop the retry loop once the instance has been destroyed
		if (!this.instanceAlive) return

		// Commands without a reply are queried again with the control code + Param_Vaild(all 0)
		// (H4K only: some H4K firmware only accepts the control code). 0617 / 0605 keep the single-round behaviour.
		if (!family.queryAllOnConnect) return
		const missing = keys.filter((key) => !this.hasRecentReply(key))
		if (missing.length > 0) {
			this.log('info', `[Query] No reply for ${missing.join(', ')}, retrying with control code + Param_Vaild=0`)
			await this.sendQueryRound(missing, 'set')
			await new Promise((resolve) => setTimeout(resolve, 700))
			if (!this.instanceAlive) return
			const stillMissing = missing.filter((key) => !this.hasRecentReply(key))
			if (stillMissing.length > 0) {
				this.log('warn', `[Query] Still no reply: ${stillMissing.join(', ')}`)
			}
		}
	}

	/** Send one query round: get = 0x01xx + empty Data; set = control code + Param_Vaild(all 0) */
	private async sendQueryRound(keys: string[], mode: 'get' | 'set'): Promise<void> {
		for (const key of keys) {
			if (!this.instanceAlive) return
			const cmd = this.protocolCommands[key]
			if (!cmd || !this.comm) continue
			if (mode === 'get') {
				await this.comm.sendCommand(cmd.get, Buffer.alloc(0))
			} else {
				await this.comm.sendCommand(cmd.set, Buffer.alloc(4))
			}
			// Space the sends out, to avoid UDP congestion or overwhelming the device
			await new Promise((resolve) => setTimeout(resolve, 150))
		}
	}

	/** Whether a reply/report for this command arrived within the last 3 seconds */
	private hasRecentReply(key: string): boolean {
		const at = this.lastReplyAt.get(key)
		return at !== undefined && Date.now() - at < 3000
	}

	/** Whether a protocol command has a given field (actions use it to trim options by product capability) */
	public hasField(commandKey: string, fieldName: string): boolean {
		return this.protocolCommands[commandKey]?.fields.some((f) => f.name === fieldName) ?? false
	}

	/** Send a protocol set command by field name; missing fields are skipped so all protocols share one action set */
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
	 * Switch the product profile based on the raw device model.
	 * When the profile changes, actions / feedbacks / presets are re-registered so products stay isolated.
	 */
	public applyDeviceProfile(rawModel: string | undefined, deviceType?: number, profileId?: string): void {
		// An explicit profile id (manual Device Model) wins; otherwise match the scanned model / device type
		const next = getProfileById(profileId) ?? getActiveProfile(rawModel, deviceType)
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

	/** Map scan results to Device dropdown choices; only known models are listed. */
	private buildDeviceChoices(): DeviceChoice[] {
		return this.discoveredDevices
			.filter((device) => matchDeviceProfile(device.model, device.productType))
			.map((device) => ({
				host: device.host,
				// L4: include the IP so two units of the same model can be told apart
				label: `${resolveDeviceModel(device.model, device.productType)} (${device.host})`,
			}))
	}

	/** Discover devices on the network */
	private async scanDevices(): Promise<DeviceInfo[]> {
		this.log('debug', '[Scan] Starting UDP broadcast device discovery')
		const scanner = new CommunicationManager({
			host: this.config?.host || '255.255.255.255',
			port: DEVICE_PORT,
			onLog: (level, message) => {
				this.log(level, message)
			},
		})
		this.scanner = scanner

		try {
			await scanner.scanNetwork()
			const allDevices = scanner.getDiscoveredDevices()
			// Keep only models with a profile, so unknown devices (e.g. SE2017) never reach the dropdown
			const devices = allDevices.filter((d) => matchDeviceProfile(d.model, d.productType))
			// M4: when the scan is empty, keep the previous device list so the dropdown / MAC info is not lost
			if (devices.length > 0) {
				this.discoveredDevices = devices
			}

			const ignored = allDevices.filter((d) => !matchDeviceProfile(d.model, d.productType))
			if (ignored.length > 0) {
				this.log(
					'warn',
					`[Scan] Ignored ${ignored.length} unsupported device(s): ${ignored.map((d) => `${d.model}@${d.host}`).join(', ')} (set Device Model manually and type the Target IP)`,
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
			if (this.scanner === scanner) this.scanner = undefined
		}
	}

	private setupConnection(): void {
		if (!this.config.host) {
			this.log('error', 'No device address configured for connection')
			this.updateStatus(InstanceStatus.BadConfig, 'No device address configured')
			return
		}

		// Scan info of the current target (may be missing when the IP was typed manually)
		const targetDevice = this.discoveredDevices.find((d) => d.host === this.config.host)
		// Manual Device Model (when enabled) wins over the scanned model
		const manualProfile = this.config.manualModel ? getProfileById(this.config.deviceModel) : undefined
		this.applyDeviceProfile(targetDevice?.model, targetDevice?.productType, manualProfile?.id)
		const modelLabel = targetDevice
			? resolveDeviceModel(targetDevice.model, targetDevice.productType)
			: (manualProfile?.displayName ?? 'Unknown (manual IP)')

		this.log('info', '========================================')
		this.log('info', 'Establishing UDP connection to device')
		this.log('info', `  Model: ${modelLabel}`)
		this.log('info', `  IP: ${this.config.host}`)
		this.log('info', `  Port: ${DEVICE_PORT}`)
		this.log('info', '========================================')

		this.comm = new CommunicationManager({
			host: this.config.host,
			port: DEVICE_PORT,
			// H4K has no 0xEEEE heartbeat; its own 0x0001 command is used as the liveness probe. Other families keep the previous logic
			probeCommand: this.protocolFamily.probeCommand,
			// L6: H4K reports are fully handled by onReport; skip the duplicate data path
			skipReportDataCallback: this.protocolFamily.parseQueryReplies === true,
			onLog: (level, message) => {
				this.log(level, message)
			},
		})

		// The heartbeat needs the target MAC and model, taken from the matching scan entry
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
					// M6: presets are registered in init / applyDeviceProfile and no longer follow the online state.
					// L2: restart blinking after a reconnect (if FTB/MUTE/Freeze is still active).
					this.updateBlink()
					// Query one round of device state (H4K has no full 0x0110 report)
					void this.queryDeviceState()
				} else {
					this.log('warn', `Connection status: ${status} - ${message || 'unknown'}`)
					this.setVariableValues({ connection_status: 'Disconnected' })
					// M6: do not clear presets on a temporary disconnect, so the preset area does not vanish
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

		// M2: record the host being connected, so configUpdated can compare and decide whether to reconnect
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
			// L2: reset the phase on destroy so blinking restarts from the beginning after a reconnect
			this.deviceState.blinkOn = true
		}
	}

	/** Send a protocol set command (Data = Param_Vaild(parameter index) + value) */
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
		// Log only command/field/value; Param_Vaild (packet header bytes) is logged only for local debugging
		const validInfo = LOG_RAW_PACKETS ? `, valid=0x${data.readUInt32BE(0).toString(16)}` : ''
		this.log(
			'debug',
			`[Set] ${label} -> ${value} (cmd=0x${cmd.set.toString(16).padStart(4, '0')}, field=${fieldIndex}${validInfo})`,
		)
		const ok = await this.comm.sendCommand(cmd.set, data)
		const flashKey = this.flashKeyContext.getStore()
		if (ok && flashKey) this.flash(flashKey)
		return ok
	}

	private handleDeviceData(data: Buffer, host: string, port: number, cmd?: number, session?: number): void {
		this.log('debug', `Device data from ${host}:${port}, length: ${data.length} bytes`)
		// onData already receives the payload (Data section, from offset 25).
		// H4K (parseQueryReplies): parse the payload directly, so Pack_Type=1 query replies can sync state;
		// 0617/0605: keep the historic behaviour (parse the whole frame again) and do not touch the old state path.
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
				// Sync state from the device reply (using the parsed payload)
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
		// mapped: which "get command" of the command table this report CMD matches (NONE = not registered)
		const mapped = Object.keys(this.protocolCommands).find((k) => this.protocolCommands[k].get === packet.cmd)
		this.log(
			'debug',
			`[Report] Device report - Cmd: 0x${packet.cmd.toString(16).padStart(4, '0')}, Type: 0x${packet.type.toString(16)}, Data(${packet.data.length}B)${LOG_RAW_PACKETS ? `: ${packet.data.toString('hex')}` : ''}, mapped=${mapped ?? 'NONE'}`,
		)
		// Sync the current PGM/PVW values from the device report
		this.syncSwitchState(packet.cmd, packet.data)
	}

	/**
	 * Sync state from a device report/reply.
	 * - cmd=0x000a: switcher state (Data = PGM, PVW, MV)
	 * - cmd=0x0110: state report, byte layout per protocol family (see ProtocolFamily.stateReport)
	 *     0617: 10B [0]PGM [1]PVW [2]WIPE [3]SPEED [4]FTB [5]Freeze [6..7]T_Bar_val [8..9]b_bar_pos
	 *     H4K : 9B  [0]PGM [1]PVW [2]WIPE [3]SPEED [4]FTB [5]Freeze [6]T_Bar_Pos [7..8]T_Bar_Val
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
		// An active report (Pack_Type=2) carries only the fields; a query reply (Pack_Type=1) may add a
		// 4-byte Param_Vaild prefix, so the field start offset is derived from the actual length.
		const base = data.length >= spec.size + 4 ? 4 : 0
		if (data.length < spec.size + base) {
			this.log('debug', `[Report 0x0110] payload too short: ${data.length}B (need ${spec.size + base}B)`)
			return
		}

		// Read fields using the family layout (H4K orders T-Bar position/value differently)
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
			'debug',
			`[Report 0x0110] PGM=${pgmVal}, PVW=${pvwVal}, WIPE=${wipeMode}, SPEED=${speedMode}, FTB=${ftbState}, Freeze=${freezeState}, T_Bar_Pos=${tBarPos}, T_Bar=${tBarVal}, b_bar_pos=${bBarPos} (${data.length}B, offset ${base})`,
		)

		// 1) Current PGM / PVW source (Pattern converted by the family input count) -> sync button colours
		this.lastReplyAt.set('state', Date.now())
		this.deviceState.pgmSource = this.toSourceValue(pgmVal)
		this.deviceState.pvwSource = this.toSourceValue(pvwVal)
		this.applySwitchFeedback(cmd)

		// 2) FTB / Freeze state (blink on change)
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

		// Wipe mode (1~6)
		this.deviceState.wipeMode = wipeMode
		this.checkFeedbacks('wipe_active')

		// 3) T-Bar position: based on the raw value (0~tBarMax, 0~4095 on H4K), displayed as 0~500
		const tBarMax = this.protocolFamily.tBarMax ?? 4095
		const reported = Math.min(Math.max(tBarVal, 0), tBarMax)
		this.lastReportedTBar = reported
		// H4K (parseQueryReplies): within the hold window after a local send, or when the read-back differs
		// from the local target by less than one step, the read-back must not override it - otherwise smoothing /
		// calibration error drifts the base of the next +/- step ("10 steps does not reach 10").
		// A larger difference means the physical T-Bar moved, so it is followed.
		const tbarTolerance = Math.max(Math.round(tBarMax * 0.04), 16)
		const holdLocalTBar =
			this.protocolFamily.parseQueryReplies === true &&
			(Date.now() < this.tbarHoldUntil || Math.abs(reported - this.tbarRaw) <= tbarTolerance)
		if (!holdLocalTBar) this.tbarRaw = reported
		const disp = tBarMax > 0 ? Math.round((this.tbarRaw * 500) / tBarMax) : 0
		this.deviceState.tbarValue = disp
		this.deviceState.speedMode = speedMode

		// 4) Publish all reported values as variables
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

	/** Wipe mode value -> text */
	private wipeLabel(v: number): string {
		return ['', 'WIPE1', 'WIPE2', 'WIPE3', 'WIPE4', 'MIX', 'DIP'][v] ?? String(v)
	}

	/** Key Type (0x0130) value -> text: 0=PIP / 1=Luma / 2=Chroma / 3=DSK */
	public keyTypeLabel(v: number): string {
		return ['PIP', 'LUMA', 'CHROMA', 'DSK'][v] ?? `UNKNOWN(${v})`
	}

	/** Whether a key value is a PIP/LUMA/CHROMA/DSK or ON AIR key (used to refresh the 0x0130 active layer) */
	private isKeyModuleKey(keyVal: number): boolean {
		const k = this.protocolFamily.keyMap
		const groups = [k.pip, k.pipOnAir, k.luma, k.lumaOnAir, k.chroma, k.chromaOnAir, k.dsk, k.dskOnAir]
		return keyVal > 0 && groups.includes(keyVal)
	}

	/** Query Key Type once (0x0130 with empty payload) to refresh the active layer after a key press (H4K only) */
	public async queryKeyTypeOnce(): Promise<void> {
		if (!this.comm) return
		const cmd = this.protocolCommands['keyType']
		if (!cmd) return
		await this.comm.sendCommand(cmd.get, Buffer.alloc(0))
	}

	/**
	 * Mark the active layer locally (without writing 0x0030), then calibrate it from the 0x0130 read-back 400 ms later.
	 * H4K only; families without the keyType command return immediately.
	 */
	public markKeyTypeLocal(k: number): void {
		if (!this.protocolCommands['keyType']) return
		this.deviceState.keyType = k
		this.setVariableValues({ key_type: k, key_type_label: this.keyTypeLabel(k) })
		this.checkFeedbacks()
		this.schedule(() => void this.queryKeyTypeOnce(), 400)
	}

	/**
	 * H4K only: PIP / LUMA / CHROMA are mutually exclusive and cannot be active together.
	 * Before enabling one layer, set the Status of the other two to 0 (DSK is a downstream overlay and not part of the mutex).
	 * Old families (0617/0605) have no keyType command and return immediately, so their behaviour is unchanged.
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
	 * Reported source value -> internal source value (1~N / 0xF0=Pattern1 / 0xF1=Pattern2, N per family).
	 * The 0x0110 report is 1-based on both 0617 and H4K: 1~N = IN1~INn, N+1 = PAT1, N+2 = PAT2, 0 = BLACK.
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
	 * Handle replies/reports of "get commands":
	 * - Device active report (Pack_Type=2): CMD is the sync command code (e.g. 0x0120)
	 * - Host query (Pack_Type=1): the device answers with the control command code (e.g. 0x0020, see protocol doc 3.2);
	 *   a successful set also answers with the same control code and a 1-byte Report Code, excluded by length.
	 */
	private handleGetReport(cmd: number, data: Buffer): void {
		const commands = this.protocolCommands
		const hex = (v: number): string => `0x${v.toString(16).padStart(4, '0')}`

		// 1) Active report: CMD is the sync command code
		let key = Object.keys(commands).find((k) => commands[k].get === cmd)
		let source: 'report' | 'query' = 'report'

		// 2) Query reply: CMD is the control command code and the data covers all fields
		//    Note: a 1-byte payload is always a set reply (Report Code) and must not be read as a field value
		//    (ambiguous for commands with a single field such as keyType)
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
			// H4K: set-command reply (Data = 1-byte Report Code); logging it shows whether the device accepted the value
			if (this.protocolFamily.queryAllOnConnect && data.length === 1) {
				const isSetReply = Object.keys(commands).some((k) => commands[k].set === cmd)
				if (isSetReply) {
					this.log(
						'debug',
						`[Reply] 0x${cmd.toString(16).padStart(4, '0')} Report Code=${data[0]} (${data[0] === 0 ? 'success' : 'fail'})`,
					)
					return
				}
			}
			// Record unmapped reports/replies (e.g. H4K 0x0001/0x0002) to help diagnose protocol differences
			const unhandled = `[Report] Unhandled cmd=${hex(cmd)} (${data.length}B)${LOG_RAW_PACKETS ? ` data=${data.toString('hex')}` : ''}`
			this.log('debug', unhandled)
			return
		}

		if (source === 'query') {
			this.log('debug', `[Query Reply] ${hex(cmd)} -> ${key} (${data.length}B)`)
		}
		this.applyGetReport(key, data)
		this.syncDerivedFromReport(key)
		this.lastReplyAt.set(key, Date.now())
	}

	/** Split a reply into fields by size and store it in reportState (GET layout may differ from SET) */
	private applyGetReport(key: string, data: Buffer): void {
		const cmd = this.protocolCommands[key]
		// H4K GET and SET fields differ (e.g. luma GET 16B / SET 21B, audio GET 29B / SET 34B)
		const getFields = cmd.getFields ?? cmd.fields
		const setFields = cmd.fields
		const lenOf = (fs: typeof getFields): number => fs.reduce((sum, f) => sum + f.size, 0)
		const getLen = lenOf(getFields)
		const setLen = lenOf(setFields)

		// Layout selection (H4K only):
		// - active reports / query replies use the GET layout (0x0130 = 1B, 0x0131 = 16B, 0x0132 = 32B)
		// - some firmware reports with the control command code and the SET layout tail fields (including Reset)
		// Derive it from the exact length, so extra bytes are not mistaken for a prefix and shift every field.
		// 0617/0605 keep the historic behaviour (GET layout only).
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
		// An active report (Pack_Type=2) carries only the fields; some firmware adds a 4-byte Param_Vaild prefix to query replies
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
		// H4K logs "field=value" so every parsed field is visible; old families keep the previous format
		const detail = fields
			.slice(0, values.length)
			.map((f, i) => `${f.name}=${values[i]}`)
			.join(' ')
		const msg = this.protocolFamily.parseQueryReplies
			? `[Report] ${key} (0x${cmd.get.toString(16).padStart(4, '0')}, ${layout}) ${detail}`
			: `[Report] ${key} = [${values.join(', ')}]`
		this.log('info', `${msg} (${data.length}B, offset ${base})`)
	}

	/** Refresh the matching feedback/state from a reported get command */
	private syncDerivedFromReport(key: string): void {
		const vals = this.reportState[key] ?? []
		switch (key) {
			case 'transition': {
				this.verifyWipeReport(vals)
				// Per-wipe style values -> variables / feedbacks (0x0120 read-back; 3 wipes on H4K, 4 on 0617)
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
				// 0x0130: currently active key module (0=PIP / 1=Luma / 2=Chroma / 3=DSK)
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

	/** Read a parsed field value of a get command */
	public getReportState(key: string): number[] {
		return this.reportState[key] ?? []
	}

	/**
	 * Index of a field in a get-command reply (GET layout).
	 * Feedbacks must not hard-code indices: H4K LUMA/DSK have no Tie field, so Status is at 0 instead of 1.
	 */
	public getReportFieldIndex(commandKey: string, fieldName: string): number {
		const cmd = this.protocolCommands[commandKey]
		if (!cmd) return -1
		const fields = cmd.getFields ?? cmd.fields
		return fields.findIndex((f) => f.name === fieldName)
	}

	/** Refresh PGM/PVW feedbacks and variables */
	private applySwitchFeedback(cmd: number): void {
		this.log(
			'debug',
			`[Switch] PGM=${this.deviceState.pgmSource}, PVW=${this.deviceState.pvwSource} (cmd=0x${cmd.toString(16).padStart(4, '0')})`,
		)
		this.checkFeedbacks('pgm_active', 'pvw_active')
		this.setVariableValues({
			pgm_source: this.sourceLabel(this.deviceState.pgmSource),
			pvw_source: this.sourceLabel(this.deviceState.pvwSource),
		})
	}

	public async scanForDevices(): Promise<DeviceInfo[]> {
		// Manual scan shares the mutex with the start-up scan, so they cannot overlap
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

		// Guard the builder: it throws when no valid key/T-Bar data is supplied (e.g. a key map without
		// a value for a wipe channel). Returning false keeps the action promise resolved instead of crashing.
		let built: { cmd: number; data: Buffer }
		try {
			built = buildCommand(commandId, params, { keyPressFormat: this.protocolFamily.keyPressFormat })
		} catch (error) {
			this.log('error', `[Action] Cannot build ${commandId}: ${(error as Error).message}`)
			return false
		}
		const { cmd, data } = built

		// For KEY_PRESS commands, map keyVal to the button name
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
			// Optimistic update + action flash (the key is set by the action wrapper)
			const keyVal = params?.keyVal as number | undefined
			if (commandId === 'KEY_PRESS' && typeof keyVal === 'number') {
				this.optimisticKey(keyVal)
				// H4K: after pressing a PIP/LUMA/CHROMA/DSK (or ON AIR) key, refresh the active key module (0x0130)
				if (this.protocolCommands['keyType'] && this.isKeyModuleKey(keyVal)) {
					this.schedule(() => void this.queryKeyTypeOnce(), 300)
				}
			}
			const flashKey = this.flashKeyContext.getStore()
			if (flashKey) this.flash(flashKey)
		} else {
			this.log('error', `[Action] Failed to send: ${actionLabel}`)
		}

		return success
	}

	/**
	 * Optimistic state update after a successful send (the device report is authoritative and corrects it later).
	 * The key map is taken from the current family (0617 and H4K key values are completely different).
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
			// AUTO is treated as a momentary action: light briefly, then release automatically
			this.deviceState.autoActive = true
			this.checkFeedbacks('auto_active')
			// L2: registered timer, so destroy() releases it
			this.schedule(() => {
				this.deviceState.autoActive = false
				this.checkFeedbacks('auto_active')
			}, 800)
		} else if (keyVal === keys.ftb) {
			this.deviceState.ftbActive = !this.deviceState.ftbActive
			this.checkFeedbacks('ftb_active')
			// Start/stop blinking after the local flip, so the button never stays solid without blinking
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

	/** Record the "last executed action key" and clear it after ~400 ms (drives the action-flash feedback) */
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

	/** FTB/MUTE/Freeze blink: while active, toggle the phase every ~500 ms and refresh feedbacks (red on white <-> black on white) */
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

	/** Source value -> name (used by variables/logs) */
	private sourceLabel(value: number): string {
		if (value >= 1 && value <= 6) return `IN${value}`
		if (value === 0xf0) return 'Pattern1'
		if (value === 0xf1) return 'Pattern2'
		return value ? `0x${value.toString(16)}` : 'N/A'
	}

	private getButtonNameByKeyVal(keyVal: number): string {
		// The key map is taken from the current family (0617 and H4K key values are completely different)
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
	 * Move the T-Bar (0x0010): 0617 uses Param_Vaild=1 + T_Bar_val; H4K uses the bitmask + Key_type=2 + Key_val.
	 * The UI scale is 0~500 and is converted proportionally to 0~tBarMax (4095) before sending.
	 * direction: 1=Up / 0=Down
	 */
	public async moveTBar(direction: number, step: number): Promise<boolean> {
		const tBarMax = this.protocolFamily.tBarMax ?? 4095
		// No optimistic update while disconnected, so variables never disagree with the device
		if (!this.comm?.getStatus()) {
			this.log('warn', '[T-Bar] Not connected, ignoring move request')
			return false
		}
		// Increment from the raw value (0~tBarMax) to avoid cumulative rounding errors from 0~500 conversions
		const prevRaw = this.tbarRaw
		const stepRaw = Math.max(1, Math.round((step * tBarMax) / 500))
		const raw = Math.min(Math.max(direction === 1 ? this.tbarRaw + stepRaw : this.tbarRaw - stepRaw, 0), tBarMax)
		// Rapid clicks must advance the base: update tbarRaw optimistically before sending and roll back on failure
		this.tbarRaw = raw
		// Lock the local base for 5 s: device read-backs must not override tbarRaw, so rapid clicks advance by exactly one step
		this.tbarHoldUntil = Date.now() + 5000
		const next = tBarMax > 0 ? Math.round((raw * 500) / tBarMax) : 0
		// H4K: 0x0010 + dynamic valid + Key_type=2 + T-Bar value; 0617: Param_Vaild=1 + T_Bar_val
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
			// Send failed -> roll back the local base and do not update the display variables
			this.tbarRaw = prevRaw
			this.tbarHoldUntil = 0
			return false
		}
		// Write the display and variables only after a successful send
		this.deviceState.tbarValue = next
		this.setVariableValues({ tbar_value: String(next) })
		// Verify the T-Bar by reading back 0x0110; the device smooths/limits movement, so wait 800 ms (measured: set 3767, read back 3427)
		if (format === 'keytype' && this.protocolFamily.stateReport) {
			const seq = ++this.tbarSendSeq
			this.schedule(() => void this.verifyTBarApplied(raw, mode, seq), 800)
		}
		return true
	}

	/** Query device state once (0x0110 empty payload) to confirm read-backs after T-Bar moves or switches */
	public async queryStateOnce(): Promise<void> {
		if (!this.comm) return
		const stateCmd = this.protocolCommands['state']
		await this.comm.sendCommand(stateCmd?.get ?? 0x0110, Buffer.alloc(0))
	}

	/** Query transition state once (0x0120 empty payload) to check whether Wipe1/2/3 landed on the right channel (H4K only) */
	public async queryTransitionOnce(): Promise<void> {
		if (!this.comm) return
		const cmd = this.protocolCommands['transition']
		if (!cmd) return
		await this.comm.sendCommand(cmd.get, Buffer.alloc(0))
	}

	/** Per-wipe style values ([Wipe1, Wipe2, Wipe3, ...]; only filled after a 0x0120 read-back) */
	public getTransitionReport(): number[] {
		return this.reportState['transition'] ?? []
	}

	/** Wipe style value -> text (looked up in the family enumeration, falling back to the number) */
	private wipeStyleLabel(v: number): string {
		const styles = this.protocolFamily.wipeStyles ?? []
		return styles.find((s) => s.id === v)?.label ?? String(v)
	}

	/** Arm the wipe-style write check target (only called by the H4K trans_wipeN actions) */
	public armWipeCheck(n: number, value: number): void {
		const before = (this.reportState['transition'] ?? []).slice(0, 3)
		this.pendingWipeCheck = { n, value, before, at: Date.now() }
	}

	/**
	 * Verify the sent wipe style against the 0x0120 read-back:
	 * the log prints Wipe1/2/3 before/after and which field changed, making wrong field mappings easy to spot
	 * (if sending Wipe2 changes another field, the device wipe number and the field do not correspond).
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
				`changed=[${changed.join(', ') || 'none'}] -> Wipe${pending.n}=${actual} ${ok ? 'OK' : 'MISMATCH'}`,
		)
	}

	/** T-Bar send mode -> packet description (useful when reading the log) */
	private tbarModeDesc(mode: TBarSendMode, raw: number, percent: number): string {
		switch (mode) {
			case 'pos':
				return `Key_type=2, Key_Pos=${percent}%/valid=0x05 (Mode=pos)`
			case 'both':
				return `Key_type=2, Key_Val=${raw}+Key_Pos=${raw <= 0 ? 0 : raw >= 4095 ? 2 : 1}(gear)/valid=0x07 (Mode=both)`
			case 'valPct':
				return `Key_type=2, Key_Val=${percent}(percent)/valid=0x03 (Mode=valPct)`
			default:
				return `Key_type=2, Key_Val=${raw}/valid=0x03 (Mode=val)`
		}
	}

	/** Whether a read-back matches the target (the device smooths/limits movement, so allow 10%, but "not moved" still fails) */
	private tbarMatches(device: number, target: number): boolean {
		if (device < 0) return false
		const tBarMax = this.protocolFamily.tBarMax ?? 4095
		const tolerance = Math.max(Math.round(tBarMax * 0.1), 16)
		// With a non-zero target, a device value of 0 means it did not accept the value (must not pass via the +/-10% tolerance)
		if (target > 0 && device === 0) return false
		return Math.abs(device - target) <= tolerance
	}

	/**
	 * T-Bar read-back verification (per doc 3.1.3):
	 * Param_Vaild (4 bytes): Bit0=Key_type, Bit1=Key_val (Bit2+ reserved); for T-Bar Key_type=2 and the data goes in Key_val.
	 * After sending, query 0x0110 and use the reported value (not the local optimistic one) to decide whether it took effect.
	 * If it did not, no other encoding is tried: the display is restored to the device truth so the UI never disagrees.
	 */
	private async verifyTBarApplied(target: number, mode: TBarSendMode, seq: number): Promise<void> {
		const tBarMax = this.protocolFamily.tBarMax ?? 4095
		// On rapid clicks only the last one is verified (a new action starts a new sequence)
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
			`[T-Bar] Not applied: sent ${target}, device read-back ${deviceRaw} (mode=${mode}); ` +
				`if it stays 0 the device does not accept the value (or the T-Bar range/unit does not match 0~${tBarMax}); the display was restored to the device value`,
		)
		this.tbarRaw = Math.max(deviceRaw, 0)
		this.tbarHoldUntil = 0 // Release the local base lock so read-backs take over again
		const disp = tBarMax > 0 ? Math.round((this.tbarRaw * 500) / tBarMax) : 0
		this.deviceState.tbarValue = disp
		this.setVariableValues({ tbar_value: String(disp) })
	}

	/** Query 0x0110 and wait for a "new" reply (about 1 s max); returns whether one arrived */
	private async waitFreshStateReport(): Promise<boolean> {
		const before = this.lastReplyAt.get('state') ?? 0
		await this.queryStateOnce()
		for (let i = 0; i < 20; i++) {
			await new Promise((resolve) => setTimeout(resolve, 50))
			if (!this.instanceAlive) return false
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

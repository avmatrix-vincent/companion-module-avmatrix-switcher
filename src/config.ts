import { Regex, type SomeCompanionConfigField } from '@companion-module/base'

// 设备控制协议使用的固定端口，无需用户配置
export const DEVICE_PORT = 7000

// UDP 广播扫描返回的型号代码 -> 界面显示名称
export const MODEL_CODE_MAP: Record<string, string> = {
	VS0605: 'SHARK S6',
	VS0617: 'SHARK S6 PLUS',
}

/**
 * 将扫描到的原始型号代码转换为界面显示名称
 * 例如 VS0605E -> SHARK S6，VS0617 -> SHARK S6 PLUS
 */
export function resolveDeviceModel(rawModel: string | undefined): string {
	const code = (rawModel ?? '').trim().toUpperCase()
	for (const [prefix, name] of Object.entries(MODEL_CODE_MAP)) {
		if (code.startsWith(prefix)) return name
	}
	return (rawModel ?? '').trim() || 'Unknown Device'
}

export interface ModuleConfig {
	/** Device 下拉选中的设备 IP（来自 UDP 扫描结果） */
	device: string
	/** Target IP，可手动编辑；连接时以该值为准 */
	host: string
	/** 上次扫描到的设备列表，持久化保存，避免重启后下拉框为空 */
	devices?: SavedDevice[]
}

/** 持久化到 config 的设备条目 */
export interface SavedDevice {
	host: string
	name: string
	/** 设备 MAC，心跳包与断线判定必需；扫描时写入 */
	mac?: string
	/** 设备类型（心跳包 Dev_Type 用）；扫描时写入 */
	productType?: number
	/** 心跳报文用的 Dev_Type（按型号映射）；扫描时写入 */
	udpType?: number
	/** 设备原始型号（如 VS0617E），用于按映射表重算 Dev_Type */
	rawModel?: string
}

/** Device 下拉的一个候选项 */
export interface DeviceChoice {
	host: string
	label: string
}

export function GetConfigFields(devices: DeviceChoice[], current?: ModuleConfig): SomeCompanionConfigField[] {
	// 首个选项为占位项，保证下拉始终有可选值（扫描到设备后会被替换）
	const choices =
		devices.length > 0
			? devices.map((d) => ({ id: d.host, label: d.label }))
			: [{ id: '', label: 'No supported device found' }]

	const defaultDevice =
		current?.device && choices.some((c) => c.id === current.device) ? current.device : choices[0].id

	// Target IP 与所选 Device 的 IP 保持一致；用户手动改过则保留其输入
	const defaultHost = current?.host || current?.device || devices[0]?.host || ''

	return [
		{
			type: 'dropdown',
			id: 'device',
			label: 'Device',
			width: 12,
			choices,
			default: defaultDevice,
			tooltip: 'UDP 广播扫描到的设备，默认选中第一个',
		},
		{
			type: 'textinput',
			id: 'host',
			label: 'Target IP',
			width: 12,
			regex: Regex.IP,
			default: defaultHost,
			tooltip: '所选设备的 IP，可手动修改',
		},
	]
}

export interface DeviceCommand {
	id: string
	name: string
	cmd: number
	description?: string
	buildData?: (params?: Record<string, unknown>) => Buffer
}

export interface DeviceResponse {
	raw: string
	type: string
	cmd: number
	session: number
	data: Record<string, unknown>
	rawBuffer?: Buffer
}

// ===== 按键值表：严格对应 PSV0617 协议文档 3.1.2 键值对应表 =====

// PGM源：PGM1~6 = 1~6
export const PGM_KEY_VALUES: Record<string, number> = {
	PGM1: 1,
	PGM2: 2,
	PGM3: 3,
	PGM4: 4,
	PGM5: 5,
	PGM6: 6,
}

// PVW源：PVW1~6 = 9~14
export const PVW_KEY_VALUES: Record<string, number> = {
	PVW1: 9,
	PVW2: 10,
	PVW3: 11,
	PVW4: 12,
	PVW5: 13,
	PVW6: 14,
}

// Pattern：PGM pattern1/2 = 7/8，PVW pattern1/2 = 15/16
export const PATTERN_KEY_VALUES: Record<string, number> = {
	PGM_PATTERN1: 7,
	PGM_PATTERN2: 8,
	PVW_PATTERN1: 15,
	PVW_PATTERN2: 16,
}

// 切换/特效：CUT=17, Auto=18, FTB=19, MIX=31, DIP=32, FREEZE=33
export const TRANSITION_KEY_VALUES: Record<string, number> = {
	CUT: 17,
	AUTO: 18,
	FTB: 19,
	MIX: 31,
	DIP: 32,
	FREEZE: 33,
}

// 功能键：Mute=20, Speed1=21, Speed2=22, REC=23, Stream1~3=24~26
export const FUNCTION_KEY_VALUES: Record<string, number> = {
	MUTE: 20,
	SPEED1: 21,
	SPEED2: 22,
	REC: 23,
	STREAM1: 24,
	STREAM2: 25,
	STREAM3: 26,
}

// Wipe 选择：Wipe1~4 = 27~30
export const WIPE_KEY_VALUES: Record<string, number> = {
	WIPE1: 27,
	WIPE2: 28,
	WIPE3: 29,
	WIPE4: 30,
}

// 快捷键：F1~F6 = 34~39
export const SHORTCUT_KEY_VALUES: Record<string, number> = {
	F1: 34,
	F2: 35,
	F3: 36,
	F4: 37,
	F5: 38,
	F6: 39,
}

// 0x0010 按键指令数据长度（Param_Vaild(4) + 单个参数值(2)）
const KEY_PRESS_DATA_LENGTH = 6

/**
 * 构建 0x0010 按键控制指令的数据（按设备实测样例）
 *
 * 数据格式（6字节大端）:
 *   Bytes 0-3: Param_Vaild - 参数索引（0=Key_val, 1=T_Bar_val, 2=b_bar_pos）
 *   Bytes 4-5: 对应参数的值
 *
 * 实测样例 PGM1: 00 00 00 00 00 01（Param_Vaild=0 表示 Key_val，值=1）
 */
function buildKeyPressData(params?: Record<string, unknown>): Buffer {
	const keyVal = params?.keyVal as number | undefined
	const tBarVal = params?.tBarVal as number | undefined
	const bBarPos = params?.bBarPos as number | undefined

	let paramIndex: number
	let value: number
	if (keyVal !== undefined && keyVal !== 0xffff) {
		paramIndex = 0 // NO.0 Key_val
		value = keyVal
	} else if (tBarVal !== undefined && tBarVal !== 0xffff) {
		paramIndex = 1 // NO.1 T_Bar_val
		value = tBarVal
	} else if (bBarPos !== undefined && bBarPos !== 0xffff) {
		paramIndex = 2 // NO.2 b_bar_pos
		value = bBarPos
	} else {
		throw new Error('No valid key data to set')
	}

	const data = Buffer.alloc(KEY_PRESS_DATA_LENGTH)
	data.writeUInt32BE(paramIndex, 0)
	data.writeUInt16BE(value & 0xffff, 4)

	return data
}

export const DeviceCommands: Record<string, DeviceCommand> = {
	// 按键控制指令（PGM/PVW切换等）
	KEY_PRESS: {
		id: 'KEY_PRESS',
		name: 'Key Press',
		cmd: 0x0010,
		description: 'Button control command (PGM/PVW source switch)',
		buildData: buildKeyPressData,
	},
	// PGM/PVW切屏
	PGM_PVW_CUT: {
		id: 'PGM_PVW_CUT',
		name: 'PGM/PVW Cut',
		cmd: 0x0009,
		description: 'Cut switch between PGM and PVW',
	},
	// 查询类命令
	GET_SWITCH_STATE: {
		id: 'GET_SWITCH_STATE',
		name: 'Get Switch State',
		cmd: 0x000a,
		description: 'Get PGM/PVW/MV current source',
	},
	GET_INPUT_STATUS: {
		id: 'GET_INPUT_STATUS',
		name: 'Get Input Status',
		cmd: 0x0004,
		description: 'Get input signal status',
	},
	GET_VERSION: {
		id: 'GET_VERSION',
		name: 'Get Version',
		cmd: 0x0001,
		description: 'Get device version info',
	},
}

export function parseDeviceResponse(
	rawData: string,
	cmd?: number,
	session?: number,
	rawBuffer?: Buffer,
): DeviceResponse {
	const response: DeviceResponse = {
		raw: rawData,
		type: 'unknown',
		cmd: cmd || 0,
		session: session || 0,
		data: {},
		rawBuffer,
	}

	// 心跳包解析（0xeeee）
	if (cmd === 0xeeee) {
		response.type = 'heartbeat'
		if (rawBuffer && rawBuffer.length >= 23) {
			const macBytes = rawBuffer.slice(16, 22)
			const mac = Array.from(macBytes)
				.map((b) => b.toString(16).padStart(2, '0'))
				.join(':')
			const controllable = rawBuffer[22] === 0x00
			response.data = { mac, controllable }
		}
		return response
	}

	// 电源响应
	if (cmd === 0x0001) {
		response.type = 'power_on'
		response.data = { power: true }
		return response
	}
	if (cmd === 0x0002) {
		response.type = 'power_off'
		response.data = { power: false }
		return response
	}

	// 状态响应
	if (cmd === 0x0003) {
		response.type = 'status'
		response.data = { status: rawData }
		return response
	}

	// 错误响应
	if (rawData.includes('ERROR')) {
		response.type = 'error'
		response.data = { error: rawData }
	}

	return response
}

export function handleDeviceResponse(
	response: DeviceResponse,
	callbacks: {
		onPowerChange?: (power: boolean) => void
		onStatusUpdate?: (status: unknown) => void
		onError?: (error: unknown) => void
		onHeartbeat?: (mac: string, controllable: boolean) => void
		onCustomData?: (data: DeviceResponse) => void
	},
): void {
	switch (response.type) {
		case 'power_on':
			callbacks.onPowerChange?.(true)
			break
		case 'power_off':
			callbacks.onPowerChange?.(false)
			break
		case 'status':
			callbacks.onStatusUpdate?.(response.data.status)
			break
		case 'heartbeat':
			callbacks.onHeartbeat?.(response.data.mac as string, response.data.controllable as boolean)
			break
		case 'error':
			callbacks.onError?.(response.data.error)
			break
		default:
			callbacks.onCustomData?.(response)
			break
	}
}

export function buildCommand(commandId: string, params?: Record<string, unknown>): { cmd: number; data: Buffer } {
	const command = DeviceCommands[commandId]
	if (!command) {
		return { cmd: 0x0001, data: Buffer.alloc(0) }
	}

	const data = command.buildData ? command.buildData(params) : Buffer.alloc(0)

	return { cmd: command.cmd, data }
}

/**
 * 生成动作执行反馈的 key（唯一标识某个按钮上的某个动作实例：动作 ID + 选项）
 * 主模块执行时会用同样的公式生成，从而只有“被点击的那个按钮”命中闪烁反馈。
 */
export function flashKeyFor(actionId: string, options?: Record<string, unknown>): string {
	const o = options ?? {}
	const parts = Object.keys(o)
		.sort()
		.map((k) => `${k}=${String(o[k])}`)
	return `${actionId}|${parts.join('&')}`
}

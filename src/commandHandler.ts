import type { KeyPressFormat } from './devices/types.js'

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

// Key value tables live in src/devices/protocols.ts (one map per protocol family).

// Key-press (0x0010) data length: Param_Vaild(4) + one parameter value(2)
const KEY_PRESS_DATA_LENGTH = 6

/**
 * Build the data of a 0x0010 key-press command (based on measured samples).
 *
 * Layout (6 bytes, big-endian):
 *   Bytes 0-3: Param_Vaild - parameter index (0=Key_val, 1=T_Bar_val, 2=b_bar_pos)
 *   Bytes 4-5: value of that parameter
 *
 * Measured sample PGM1: 00 00 00 00 00 01 (Param_Vaild=0 means Key_val, value=1)
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

/**
 * H4K 0x0010 packet (fixed 8 bytes, matching the host app SharkH4kProModel.async_set_keyboard):
 *   valid(4)  : Bit0=Key_Type Bit1=Key_Val Bit2=Key_Pos
 *               **set dynamically from the fields actually sent** (a default value clears its bit)
 *   Key_Type(1): 1=key 2=T-Bar
 *   Key_Val(2) : key=key value; T-Bar pos mode keeps the 0xFFFF default (bit clear), val mode=0~4095
 *   Key_Pos(1) : T-Bar pos mode=position percentage 0~100; otherwise keeps the 0xFF default
 *
 * T-Bar send modes (the device accepts only one; the poll loop switches after reading back):
 *   - 'val'   : valid=0x03, only Key_Val (0~4095)
 *   - 'pos'   : valid=0x05, only Key_Pos (0~100 percentage)
 *   - 'both'  : valid=0x07, Key_Val(0~4095) + Key_Pos(gear 0 bottom / 1 middle / 2 top)
 *               - matches the measured host app packet (data=00000007 02 0eb7 01)
 *   - 'valPct': valid=0x03, Key_Val as a percentage (0~100)
 */
export type TBarSendMode = 'val' | 'pos' | 'both' | 'valPct'

function buildKeyPressKeyTypeData(keyType: 1 | 2, keyVal: number, tBarMode: TBarSendMode = 'pos'): Buffer {
	const T_BAR_MAX = 4095
	const data = Buffer.alloc(8)
	// Defaults (their bit stays clear)
	let vKeyVal = 0xffff
	let vKeyPos = 0xff

	if (keyType === 2) {
		const v = Math.min(Math.max(keyVal, 0), T_BAR_MAX)
		const pct = Math.round((v * 100) / T_BAR_MAX)
		// Key_Pos gear: 0=bottom / 1=middle / 2=top (same semantics as T_Bar_Pos in 0x0110)
		const gear = v <= 0 ? 0 : v >= T_BAR_MAX ? 2 : 1
		switch (tBarMode) {
			case 'pos':
				vKeyPos = pct
				break
			case 'both':
				vKeyVal = v
				vKeyPos = gear
				break
			case 'valPct':
				vKeyVal = pct
				break
			default:
				vKeyVal = v
				break
		}
	} else {
		vKeyVal = keyVal & 0xffff
	}

	// Dynamic valid bits: Key_Type is always set; Key_Val / Key_Pos only when not at their default
	let valid = 1 << 0
	if (vKeyVal !== 0xffff) valid |= 1 << 1
	if (vKeyPos !== 0xff) valid |= 1 << 2
	if (valid === 0x00) throw new Error('No valid key data to set')

	data.writeUInt32BE(valid >>> 0, 0)
	data.writeUInt8(keyType & 0xff, 4)
	data.writeUInt16BE(vKeyVal & 0xffff, 5)
	data.writeUInt8(vKeyPos & 0xff, 7)
	return data
}

function buildKeyPressDataKeyType(params?: Record<string, unknown>): Buffer {
	// T-Bar takes priority: a tBarVal is always sent as Key_type=2, never as a key value
	const tBarVal = params?.tBarVal as number | undefined
	const tBarMode = (params?.tBarMode as TBarSendMode | undefined) ?? 'pos'
	if (tBarVal !== undefined && tBarVal !== 0xffff) {
		return buildKeyPressKeyTypeData(2, tBarVal, tBarMode)
	}

	const keyVal = params?.keyVal as number | undefined
	if (keyVal !== undefined && keyVal !== 0xffff) {
		return buildKeyPressKeyTypeData(1, keyVal)
	}

	throw new Error('No valid key data to set')
}

export const DeviceCommands: Record<string, DeviceCommand> = {
	// Button control command (PGM/PVW switching etc.)
	KEY_PRESS: {
		id: 'KEY_PRESS',
		name: 'Key Press',
		cmd: 0x0010,
		description: 'Button control command (PGM/PVW source switch)',
		buildData: buildKeyPressData,
	},
}

export function parseDeviceResponse(
	rawData: string,
	cmd?: number,
	session?: number,
	rawBuffer?: Buffer,
	options?: { legacyPowerCommands?: boolean },
): DeviceResponse {
	const response: DeviceResponse = {
		raw: rawData,
		type: 'unknown',
		cmd: cmd || 0,
		session: session || 0,
		data: {},
		rawBuffer,
	}

	// Heartbeat packet (0xeeee)
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

	// Power response (0617 / 0605 semantics only; H4K 0x0001/0x0002 are version/input info)
	const legacyPower = options?.legacyPowerCommands !== false
	if (legacyPower && cmd === 0x0001) {
		response.type = 'power_on'
		response.data = { power: true }
		return response
	}
	if (legacyPower && cmd === 0x0002) {
		response.type = 'power_off'
		response.data = { power: false }
		return response
	}

	// Status response
	if (cmd === 0x0003) {
		response.type = 'status'
		response.data = { status: rawData }
		return response
	}

	// Error response
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

export function buildCommand(
	commandId: string,
	params?: Record<string, unknown>,
	options?: { keyPressFormat?: KeyPressFormat },
): { cmd: number; data: Buffer } {
	// Key-press command: the Data layout depends on the protocol family
	if (commandId === 'KEY_PRESS') {
		const data = options?.keyPressFormat === 'keytype' ? buildKeyPressDataKeyType(params) : buildKeyPressData(params)
		return { cmd: 0x0010, data }
	}

	const command = DeviceCommands[commandId]
	if (!command) {
		return { cmd: 0x0001, data: Buffer.alloc(0) }
	}

	const data = command.buildData ? command.buildData(params) : Buffer.alloc(0)

	return { cmd: command.cmd, data }
}

/**
 * Build the action-flash key (uniquely identifies one action instance on a button: action id + options).
 * The main module uses the same formula, so only the clicked button hits the flash feedback.
 */
export function flashKeyFor(actionId: string, options?: Record<string, unknown>): string {
	const o = options ?? {}
	const parts = Object.keys(o)
		.sort()
		.map((k) => `${k}=${String(o[k])}`)
	return `${actionId}|${parts.join('&')}`
}

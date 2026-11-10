import { H4K_PROTOCOL_COMMANDS, PROTOCOL_COMMANDS } from '../features.js'
import type { KeyMap, ProtocolFamily, ProtocolFamilyId, StateReportSpec } from './types.js'

/** 0617 0x0110: PGM/PVW/WIPE/SPEED/FTB/Freeze(6B) + T_Bar_val(2B) + b_bar_pos(2B) = 10B */
const CCP_0617_STATE_REPORT: StateReportSpec = {
	size: 10,
	pgm: 0,
	pvw: 1,
	wipeMode: 2,
	speedMode: 3,
	ftb: 4,
	freeze: 5,
	tBarValue: { offset: 6, size: 2 },
	bBarPos: { offset: 8, size: 2 },
}

/** H4K 0x0110: PGM/PVW/WIPE/SPEED/FTB/Freeze(6B) + T_Bar_Pos(1B) + T_Bar_Val(2B) = 9B */
const H4K_STATE_REPORT: StateReportSpec = {
	size: 9,
	pgm: 0,
	pvw: 1,
	wipeMode: 2,
	speedMode: 3,
	ftb: 4,
	freeze: 5,
	tBarPos: { offset: 6, size: 1 },
	tBarValue: { offset: 7, size: 2 },
}

/** 0617 key sources: 0=BLACK, 1~6=IN1~6, 7=Color Bar */
const CCP_0617_KEY_SOURCES = [
	{ id: 0, label: 'BLACK' },
	{ id: 1, label: 'IN1' },
	{ id: 2, label: 'IN2' },
	{ id: 3, label: 'IN3' },
	{ id: 4, label: 'IN4' },
	{ id: 5, label: 'IN5' },
	{ id: 6, label: 'IN6' },
	{ id: 7, label: 'Color Bar' },
]

/** 0617 PIP sources: 0=BLACK, 1~6=IN1~6, 7=Color Bar, 8/9=Color1/2, 10/11=PAT1/2 */
const CCP_0617_PIP_SOURCES = [
	...CCP_0617_KEY_SOURCES,
	{ id: 8, label: 'Color 1' },
	{ id: 9, label: 'Color 2' },
	{ id: 10, label: 'PAT1' },
	{ id: 11, label: 'PAT2' },
]

/** H4K key sources: 0=IN1, 1=IN2, 2=IN3, 3=IN4 (see protocol doc 3.1.6~3.1.9) */
const H4K_KEY_SOURCES = [
	{ id: 0, label: 'IN1' },
	{ id: 1, label: 'IN2' },
	{ id: 2, label: 'IN3' },
	{ id: 3, label: 'IN4' },
]

/** H4K PIP sources: 0=IN1, 1=IN2, 2=IN3, 3=IN4 (see protocol doc 3.1.8) */
const H4K_PIP_SOURCES = [...H4K_KEY_SOURCES]

/** 0617 wipe styles: 0~10 */
const CCP_0617_WIPE_STYLES = Array.from({ length: 11 }, (_, n) => ({ id: n, label: `Wipe Style ${n}` }))

/** H4K wipe styles: 0~27 (28 patterns measured on the device, in 3.1.4 KEY_PATTERN_* order) */
const H4K_WIPE_NAMES = [
	'FULL_RECT_H',
	'FULL_RECT_V',
	'FULL_RECT_MID_H',
	'FULL_RECT_MID_V',
	'CORNER_RECT_TL',
	'CORNER_RECT_TR',
	'CORNER_RECT_BR',
	'CORNER_RECT_BL',
	'CORNER_RECT_T',
	'CORNER_RECT_B',
	'CORNER_RECT_L',
	'CORNER_RECT_R',
	'BOX',
	'CROSS',
	'CORNER_DIAG_TL',
	'CORNER_DIAG_TR',
	'CORNER_DIAG_BR',
	'CORNER_DIAG_BL',
	'CORNER_TRI_T',
	'CORNER_TRI_B',
	'CORNER_TRI_L',
	'CORNER_TRI_R',
	'DUAL_DIAG_TLBR',
	'DUAL_DIAG_TRBL',
	'DUAL_TRI_H',
	'DUAL_TRI_V',
	'X',
	'DIAMOND',
]
// Dropdown ids match the protocol (0~27, sent value = id, no offset); the id is prefixed to the label for verification
const H4K_WIPE_STYLES = H4K_WIPE_NAMES.map((label, n) => ({ id: n, label: `${n}: ${label}` }))

/** 0617 / PSV0617 (SHARK S6 PLUS) key value table */
const CCP_0617_KEY_MAP: KeyMap = {
	pgm: [1, 2, 3, 4, 5, 6],
	pvw: [9, 10, 11, 12, 13, 14],
	pgmPattern: [7, 8],
	pvwPattern: [15, 16],
	cut: 17,
	auto: 18,
	ftb: 19,
	mute: 20,
	speed1: 21,
	speed2: 22,
	stream: [24, 25, 26],
	wipe: [27, 28, 29, 30],
	mix: 31,
	dip: 32,
	flipFlop: 32,
	freeze: 33,
	chroma: 0,
	chromaOnAir: 0,
	luma: 0,
	lumaOnAir: 0,
	pip: 0,
	pipOnAir: 0,
	dsk: 0,
	dskOnAir: 0,
	logo: 0,
	logoOnAir: 0,
	fKeys: [34, 35, 36, 37, 38, 39],
}

/** SHARK H4K key value table (see protocol doc 3.1.3) */
const H4K_KEY_MAP: KeyMap = {
	pgm: [1, 2, 3, 4],
	pvw: [7, 8, 9, 10],
	pgmPattern: [5, 6],
	pvwPattern: [11, 12],
	cut: 13,
	auto: 14,
	ftb: 15,
	mute: 16,
	speed1: 17,
	speed2: 18,
	stream: [], // H4K has no Stream keys/commands
	wipe: [29, 30, 31],
	mix: 32,
	dip: 33, // Doc: 33=INV, used here as the DIP/reverse key
	flipFlop: 34,
	freeze: 35,
	chroma: 19,
	chromaOnAir: 20,
	luma: 21,
	lumaOnAir: 22,
	pip: 23,
	pipOnAir: 24,
	dsk: 25,
	dskOnAir: 26,
	logo: 27,
	logoOnAir: 28,
	fKeys: [36, 37, 38, 39],
}

/**
 * Protocol family registry.
 * - avm-0617: PSV0617 / VS0617 (SHARK S6 PLUS), VS0405E / VS0405EH (SHARK S5 / H5)
 *   Same protocol and feature set: Param_Vaild = field index, 6 sources / 3 PIP / 4 wipes / stream
 * - avm-h4k : SHARK H4K / SHARK H4K PLUS (Dev_Type 0x06/0x07/0x08),
 *   Param_Vaild = bitmask, 4 sources / 1 PIP / 3 wipes / no stream
 * - avm-0605: standalone protocol of VS0605 (SHARK S6)
 *   TODO: replace with the dedicated 0605 command table once its protocol doc is available.
 *         For now it clones the 0617 table, so S6 behaviour is unchanged and shares no objects with 0617.
 */
export const PROTOCOL_FAMILIES: Record<ProtocolFamilyId, ProtocolFamily> = {
	'avm-0617': {
		id: 'avm-0617',
		displayName: 'AVM CCP (0617)',
		commands: PROTOCOL_COMMANDS,
		paramValidMode: 'index',
		keyPressFormat: 'index',
		keyMap: CCP_0617_KEY_MAP,
		inputCount: 6,
		pipCount: 3,
		wipeCount: 4,
		logoCount: 8,
		hasStream: true,
		stateReport: CCP_0617_STATE_REPORT,
		tBarMax: 4095,
		keySources: CCP_0617_KEY_SOURCES,
		pipSources: CCP_0617_PIP_SOURCES,
		wipeStyles: CCP_0617_WIPE_STYLES,
	},
	'avm-h4k': {
		id: 'avm-h4k',
		displayName: 'AVM H4K (H4K / H4K PLUS)',
		commands: H4K_PROTOCOL_COMMANDS,
		paramValidMode: 'bitmask',
		keyPressFormat: 'keytype',
		keyMap: H4K_KEY_MAP,
		inputCount: 4,
		pipCount: 1,
		wipeCount: 3,
		logoCount: 2,
		hasStream: false,
		stateReport: H4K_STATE_REPORT,
		tBarMax: 4095, // T-Bar data 0~4095
		// H4K has no 0xEEEE heartbeat; 0x0001 (read version) is used as the liveness probe
		probeCommand: 0x0001,
		// On H4K, 0x0001/0x0002 are version/input info, not power commands
		legacyPowerCommands: false,
		keySources: H4K_KEY_SOURCES,
		pipSources: H4K_PIP_SOURCES,
		wipeStyles: H4K_WIPE_STYLES,
		// Wipe styles: dropdown 0~27 is the device style value, 0 = first pattern (sent value = id, no offset)
		wipeStyleOffset: 0,
		mergeWipeStyleAction: true,
		// H4K has no All AFV: do not register the action/preset (the AllAfv field stays in the layout)
		hideAllAfvAction: true,
		// H4K has no global audio reset: do not register the action/preset (the Reset field stays in the layout)
		hideAudioResetAction: true,
		// T-Bar: measured from the host app SharkH4kProModel - valid=0x07, Key_type=2,
		// Key_Val = T-Bar data (0~4095), Key_Pos = gear (0 bottom / 1 middle / 2 top)
		tBarSendMode: 'both',
		// 0x0110 reports PGM/PVW/T-Bar; query every command with a get code after connecting
		queryAllOnConnect: true,
		// Handle Pack_Type=1 query replies (H4K 0x0110 only answers queries, it has no active reports)
		parseQueryReplies: true,
		stateQueryKeys: ['state', 'transition', 'luma', 'chroma', 'pip1', 'dsk', 'logo', 'audio'],
	},
	'avm-0605': {
		id: 'avm-0605',
		displayName: 'AVM CCP (0605 standalone protocol)',
		commands: { ...PROTOCOL_COMMANDS },
		paramValidMode: 'index',
		keyPressFormat: 'index',
		keyMap: CCP_0617_KEY_MAP,
		inputCount: 6,
		pipCount: 3,
		wipeCount: 4,
		logoCount: 8,
		hasStream: true,
		stateReport: CCP_0617_STATE_REPORT,
		tBarMax: 4095,
		keySources: CCP_0617_KEY_SOURCES,
		pipSources: CCP_0617_PIP_SOURCES,
		wipeStyles: CCP_0617_WIPE_STYLES,
	},
}

export function getProtocolFamily(id: ProtocolFamilyId): ProtocolFamily {
	return PROTOCOL_FAMILIES[id] ?? PROTOCOL_FAMILIES['avm-0617']
}

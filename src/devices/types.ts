import type { ParamValidMode, ProtocolCommand } from '../features.js'

/** Protocol family: one wire format per family (packet layout / command codes / field order / key map) */
export type ProtocolFamilyId = 'avm-0605' | 'avm-0617' | 'avm-h4k'

/** Key-press (0x0010) data layout version */
export type KeyPressFormat =
	| 'index' // 0617: Param_Vaild = parameter index (0=Key_val / 1=T_Bar_val / 2=b_bar_pos) + 2-byte value
	| 'keytype' // H4K: Param_Vaild bitmask (Bit0=Key_type / Bit1=Key_val) + Key_type(1) + Key_val(2)

/** Key value table of a product (fixed inside a family; products may override it) */
export interface KeyMap {
	pgm: number[]
	pvw: number[]
	pgmPattern: number[]
	pvwPattern: number[]
	cut: number
	auto: number
	ftb: number
	mute: number
	speed1: number
	speed2: number
	/** Stream 1~3 keys (empty when the family has no streaming) */
	stream: number[]
	wipe: number[]
	mix: number
	dip: number
	flipFlop: number
	freeze: number
	/** H4K-only keys; 0 when the family does not support them */
	chroma: number
	chromaOnAir: number
	luma: number
	lumaOnAir: number
	pip: number
	pipOnAir: number
	dsk: number
	dskOnAir: number
	logo: number
	logoOnAir: number
	fKeys: number[]
}

/**
 * Byte layout of the 0x0110 state report (differs per protocol).
 * - 0617: 10 bytes, [6..7]=T_Bar_val, [8..9]=b_bar_pos
 * - H4K : 9 bytes, [6]=T_Bar_Pos, [7..8]=T_Bar_Val
 */
export interface StateReportSpec {
	/** Minimum valid length */
	size: number
	pgm: number
	pvw: number
	wipeMode: number
	speedMode: number
	ftb: number
	freeze: number
	/** T-Bar position (present on H4K, absent on 0617) */
	tBarPos?: { offset: number; size: number }
	/** T-Bar value */
	tBarValue: { offset: number; size: number }
	/** 0617 b_bar_pos */
	bBarPos?: { offset: number; size: number }
}

export interface ProtocolFamily {
	id: ProtocolFamilyId
	displayName: string
	commands: Record<string, ProtocolCommand>
	/** Param_Vaild encoding used by set commands */
	paramValidMode: ParamValidMode
	/** Key-press (0x0010) packet layout version */
	keyPressFormat: KeyPressFormat
	/** Key value table */
	keyMap: KeyMap
	/** Number of PGM/PVW inputs */
	inputCount: number
	/** Number of PIP layers */
	pipCount: number
	/** Number of wipes */
	wipeCount: number
	/** Number of logos */
	logoCount: number
	/** Whether streaming is available (requires Codec 0x00A0) */
	hasStream: boolean
	/** Byte layout of the 0x0110 state report */
	stateReport?: StateReportSpec
	/** Max raw T-Bar value (0~4095 on both 0617 and H4K) */
	tBarMax?: number
	/**
	 * Liveness probe command for families without a heartbeat (empty Data).
	 * Example: H4K has no 0xEEEE heartbeat, so 0x0001 (read version) is used for probing;
	 * 0617 / 0605 leave this unset and keep using 0xEEEE (with MAC) / 0xFFFF (without MAC).
	 */
	probeCommand?: number
	/**
	 * Whether 0x0001/0x0002 keep the 0617 power on/off semantics.
	 * On H4K, 0x0001 is read-version and 0x0002 is input info, so this must be false.
	 */
	legacyPowerCommands?: boolean
	/** Key source dropdown items (enumeration start differs per protocol) */
	keySources: Array<{ id: number; label: string }>
	/** PIP source dropdown items */
	pipSources: Array<{ id: number; label: string }>
	/** Wipe style dropdown items (0617=0~10; H4K=0~27, sent value = dropdown id, 0 = first pattern) */
	wipeStyles: Array<{ id: number; label: string }>
	/**
	 * Wipe style send offset: sent value = dropdown id - wipeStyleOffset.
	 * All families currently use 0 (the dropdown id is the sent value); kept for future devices
	 * whose style enumeration starts at a different value.
	 */
	wipeStyleOffset?: number
	/**
	 * T-Bar send mode (only used when keyPressFormat='keytype'):
	 * - 'val': valid=0x03, Key_Val 0~4095 (H4K doc: Key_Val carries T-Bar data when Key_type=2)
	 * - 'pos': valid=0x05, Key_Pos 0~100%
	 * - 'both': valid=0x07, Key_Val 0~4095 + Key_Pos gear 0/1/2 (measured from the host app)
	 * - 'valPct': valid=0x03, Key_Val as a 0~100 percentage
	 */
	tBarSendMode?: 'pos' | 'val' | 'both' | 'valPct'
	/**
	 * Hide the "All AFV" action (H4K has no such feature).
	 * UI registration only; the AllAfv protocol field stays in the fixed layout (removing it would shift 34B/29B).
	 */
	hideAllAfvAction?: boolean
	/**
	 * Hide the "Audio Reset" action and preset (H4K has no global audio reset).
	 * UI registration only; the Reset field stays in the fixed layout (removing it would shift all later fields).
	 */
	hideAudioResetAction?: boolean
	/**
	 * Offer the combined "wipe channel + style" action (trans_wipe_style).
	 * Enabled on H4K only; 0617/0605 keep their existing trans_wipe1~4 actions unchanged.
	 */
	mergeWipeStyleAction?: boolean
	/**
	 * Query every command that has a get code right after connecting (enabled on H4K).
	 * When off, only stateQueryKeys are queried (or nothing at all).
	 */
	queryAllOnConnect?: boolean
	/**
	 * Command keys queried right after connecting:
	 * families without a full state report (e.g. 0617 0x0110) are polled with 0x00xx + Param_Vaild=0.
	 */
	stateQueryKeys?: string[]
	/**
	 * Whether to handle device query replies (Pack_Type=1).
	 * When on, the payload passed to onData is parsed as state data directly (H4K).
	 * When off (default), only active reports (Pack_Type=2) are handled, so 0617/0605 are unaffected.
	 */
	parseQueryReplies?: boolean
}

/**
 * Product feature group keys.
 * action / feedback / preset ids are assigned to a group by prefix (see FEATURE_ID_RULES in index.ts);
 * a product profile only declares which groups it supports.
 */
export type DeviceFeatureKey =
	| 'source' // PGM/PVW source switching
	| 'transition' // CUT/AUTO/FTB/WIPE/MIX/DIP/FREEZE/T-Bar
	| 'stream' // Stream 1~3
	| 'pip'
	| 'luma'
	| 'chroma'
	| 'dsk'
	| 'logo'
	| 'audio'
	| 'system' // Connection, scanning and other common features; always enabled

export interface DeviceProfile {
	/** Internal profile id (e.g. shark-s6-plus) */
	id: string
	/** Display name (e.g. SHARK S6 PLUS) */
	displayName: string
	/** Prefixes of the discovery model field; order does not matter, longest prefix wins */
	modelPrefixes: string[]
	/** Dev_Type used in heartbeat packets (matches the host app get_udp_model_index) */
	udpDevType: number
	/**
	 * Device type id from the discovery reply (productType, byte offset 22).
	 * When declared, it is matched before the model string (more reliable; model is only 10 bytes).
	 * Example: H4K PLUS = 0x06/0x07, H4K = 0x08.
	 */
	productTypes?: number[]
	/** Protocol family used by this product (decides the command table) */
	protocolFamily: ProtocolFamilyId
	/** Feature groups enabled on this product */
	features: DeviceFeatureKey[]
	/** Product-specific command overrides (merged over the family table; same key wins) */
	protocolOverrides?: Record<string, ProtocolCommand>
}

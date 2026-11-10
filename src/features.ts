/**
 * AVM protocol feature registry (data driven).
 *
 * Based on "AVM UDP Communication Protocol V1.0.0 (PSV0617)":
 * - A set command's Data is Param_Vaild (4 bytes) + each field value
 * - A get command's Data is the field values concatenated (no Param_Vaild)
 * - Fields are listed in the NO.x order of the protocol doc; a field's byte offset is the sum of the preceding sizes
 *
 * Only simple on/off (0/1) fields are registered here, to auto-generate actions / feedbacks / presets.
 * Fields needing text input, IP, time or complex enums are intentionally omitted.
 *
 * Note: Param_Vaild is a 4-byte bitmask addressing NO.0~31 only, so fields with NO.>=32
 * (e.g. Audio MIC_EN=33, System IP_DHCP=33) are not supported yet.
 */

export interface ProtocolField {
	name: string
	size: number
}

export interface ProtocolCommand {
	/** Set command */
	set: number
	/** Query / report command */
	get: number
	/** Set-command field list (order = valid bit index) */
	fields: ProtocolField[]
	/**
	 * Field layout of query/report replies.
	 * Defaults to `fields`; H4K differs between GET and SET (e.g. luma GET 16B / SET 21B,
	 * audio GET 29B without Reset_All / SET 34B), so it must be declared explicitly.
	 */
	getFields?: ProtocolField[]
}

export const PROTOCOL_COMMANDS: Record<string, ProtocolCommand> = {
	// Transition set 0x0020 / get 0x0120
	transition: {
		set: 0x0020,
		get: 0x0120,
		fields: [
			{ name: 'Wipe1', size: 1 },
			{ name: 'Wipe2', size: 1 },
			{ name: 'Wipe3', size: 1 },
			{ name: 'Wipe4', size: 1 },
			{ name: 'Softness', size: 1 },
			{ name: 'Direction', size: 1 },
			{ name: 'Mix', size: 1 },
			{ name: 'DirColor', size: 3 },
			{ name: 'Speed1', size: 1 },
			{ name: 'Speed2', size: 1 },
			{ name: 'TBarABMode', size: 1 },
			{ name: 'TBarStatus', size: 1 },
		],
	},
	// LUMA set 0x0031 / get 0x0131
	luma: {
		set: 0x0031,
		get: 0x0131,
		fields: [
			{ name: 'Tie', size: 1 },
			{ name: 'Status', size: 1 },
			{ name: 'FillSource', size: 1 },
			{ name: 'KeySource', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Clip', size: 1 },
			{ name: 'Gain', size: 1 },
			{ name: 'Invert', size: 1 },
			{ name: 'MaskEnable', size: 1 },
			{ name: 'MaskLeft', size: 1 },
			{ name: 'MaskTop', size: 1 },
			{ name: 'MaskRight', size: 1 },
			{ name: 'MaskBottom', size: 1 },
			{ name: 'Reset', size: 1 },
		],
	},
	// CHROMA set 0x0032 / get 0x0132
	chroma: {
		set: 0x0032,
		get: 0x0132,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'KeySource', size: 1 },
			{ name: 'KeyType', size: 1 },
			{ name: 'KeyColor', size: 3 },
			{ name: 'FetchPosX', size: 2 },
			{ name: 'FetchPosY', size: 2 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Similarity', size: 1 },
			{ name: 'Smooth', size: 1 },
			{ name: 'Spill', size: 1 },
			{ name: 'Opacity', size: 1 },
			{ name: 'Brightness', size: 1 },
			{ name: 'Contrast', size: 1 },
			{ name: 'Saturation', size: 1 },
			{ name: 'MaskEnable', size: 1 },
			{ name: 'MaskLeft', size: 1 },
			{ name: 'MaskTop', size: 1 },
			{ name: 'MaskRight', size: 1 },
			{ name: 'MaskBottom', size: 1 },
			{ name: 'Reset', size: 1 },
		],
	},
	// PIP Border set 0x0036 / get 0x0136
	pipBorder: {
		set: 0x0036,
		get: 0x0136,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'Color', size: 1 },
			{ name: 'Width', size: 1 },
		],
	},
	// PIP1 set 0x0033 / get 0x0133
	pip1: {
		set: 0x0033,
		get: 0x0133,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'Source', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Reset', size: 1 },
		],
	},
	// PIP2 set 0x0034 / get 0x0134
	pip2: {
		set: 0x0034,
		get: 0x0134,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'Source', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Reset', size: 1 },
		],
	},
	// PIP3 set 0x0035 / get 0x0135
	pip3: {
		set: 0x0035,
		get: 0x0135,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'Source', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Reset', size: 1 },
		],
	},
	// DSK set 0x0040 / get 0x0140
	dsk: {
		set: 0x0040,
		get: 0x0140,
		fields: [
			{ name: 'Tie', size: 1 },
			{ name: 'Status', size: 1 },
			{ name: 'FillSource', size: 1 },
			{ name: 'KeySource', size: 1 },
			{ name: 'Clip', size: 1 },
			{ name: 'Gain', size: 1 },
			{ name: 'Invert', size: 1 },
			{ name: 'MaskEnable', size: 1 },
			{ name: 'MaskLeft', size: 1 },
			{ name: 'MaskTop', size: 1 },
			{ name: 'MaskRight', size: 1 },
			{ name: 'MaskBottom', size: 1 },
			{ name: 'Reset', size: 1 },
		],
	},
	// LOGO set 0x0041 / get 0x0141
	logo: {
		set: 0x0041,
		get: 0x0141,
		fields: [
			{ name: 'Status', size: 1 }, // 0
			{ name: 'Select', size: 1 }, // 1
			{ name: 'PosX', size: 1 }, // 2
			{ name: 'PosY', size: 1 }, // 3
			{ name: 'Size', size: 1 }, // 4
			{ name: 'Opacity', size: 1 }, // 5
			{ name: 'Reset', size: 1 }, // 6
		],
	},
	// Audio set 0x0050 / get 0x0150
	audio: {
		set: 0x0050,
		get: 0x0150,
		fields: [
			{ name: 'Mute', size: 1 },
			{ name: 'AllAfv', size: 1 },
			{ name: 'Reset', size: 1 },
			{ name: 'MasterEnable', size: 1 },
			{ name: 'MasterVolume', size: 1 },
			{ name: 'EarEnable', size: 1 },
			{ name: 'EarVolume', size: 1 },
			{ name: 'EarSource', size: 1 },
			{ name: 'In1Enable', size: 1 },
			{ name: 'In1Volume', size: 1 },
			{ name: 'In1Afv', size: 1 },
			{ name: 'In1Delay', size: 1 },
			{ name: 'In2Enable', size: 1 },
			{ name: 'In2Volume', size: 1 },
			{ name: 'In2Afv', size: 1 },
			{ name: 'In2Delay', size: 1 },
			{ name: 'In3Enable', size: 1 },
			{ name: 'In3Volume', size: 1 },
			{ name: 'In3Afv', size: 1 },
			{ name: 'In3Delay', size: 1 },
			{ name: 'In4Enable', size: 1 },
			{ name: 'In4Volume', size: 1 },
			{ name: 'In4Afv', size: 1 },
			{ name: 'In4Delay', size: 1 },
			{ name: 'In5Enable', size: 1 },
			{ name: 'In5Volume', size: 1 },
			{ name: 'In5Afv', size: 1 },
			{ name: 'In5Delay', size: 1 },
			{ name: 'In6Enable', size: 1 },
			{ name: 'In6Volume', size: 1 },
			{ name: 'In6Afv', size: 1 },
			{ name: 'In6Delay', size: 1 },
			{ name: 'MicXlrMode', size: 1 },
			{ name: 'Mic1Enable', size: 1 },
			{ name: 'Mic1Guitar', size: 1 },
			{ name: 'Mic1PreGain', size: 1 },
			{ name: 'Mic1Volume', size: 1 },
			{ name: 'Mic1Delay', size: 1 },
			{ name: 'Mic2Enable', size: 1 },
			{ name: 'Mic2Guitar', size: 1 },
			{ name: 'Mic2PreGain', size: 1 },
			{ name: 'Mic2Volume', size: 1 },
			{ name: 'Mic2Delay', size: 1 },
			{ name: 'XlrEnable', size: 1 },
			{ name: 'XlrVolume', size: 1 },
			{ name: 'XlrDelay', size: 1 },
			{ name: 'LineInEnable', size: 1 },
			{ name: 'LineInVolume', size: 1 },
			{ name: 'LineInDelay', size: 1 },
		],
	},
	// Output set 0x0090 / get 0x0190
	output: {
		set: 0x0090,
		get: 0x0190,
		fields: [
			{ name: 'SocHdmiOut1', size: 1 },
			{ name: 'SocSdiOut2', size: 1 },
			{ name: 'SocSdiOut3', size: 1 },
			{ name: 'SocStreamOut', size: 1 },
			{ name: 'SocLcdOut', size: 1 },
			{ name: 'SocUvcOut', size: 1 },
			{ name: 'FrameRateMode', size: 1 },
			{ name: 'FormatHdmiOut1', size: 1 },
			{ name: 'FormatSdiOut2', size: 1 },
			{ name: 'FormatSdiOut3', size: 1 },
			{ name: 'ColorSpace', size: 1 },
			{ name: 'Brightness', size: 1 },
			{ name: 'Contrast', size: 1 },
			{ name: 'Saturation', size: 1 },
			{ name: 'FtbMuteSpeed', size: 1 },
			{ name: 'FtbWithMute', size: 1 },
		],
	},
	// Codec set 0x00A0 / get 0x01A0
	codec: {
		set: 0x00a0,
		get: 0x01a0,
		fields: [
			{ name: 'Bitrate', size: 1 },
			{ name: 'RateControl', size: 1 },
			{ name: 'VideoEncoding', size: 1 },
			{ name: 'Res', size: 1 },
			{ name: 'Fps', size: 1 },
			{ name: 'IFrame', size: 2 },
			{ name: 'Volume', size: 1 },
			{ name: 'SamplingRate', size: 1 },
			{ name: 'AudioBitrate', size: 1 },
			{ name: 'Stream1Enable', size: 1 },
			{ name: 'Stream2Enable', size: 1 },
			{ name: 'Stream3Enable', size: 1 },
			{ name: 'RecordFillFormat', size: 1 },
			{ name: 'RecordOverwrite', size: 1 },
			{ name: 'RecordStorage', size: 1 },
			{ name: 'RecordFormat', size: 1 },
		],
	},
}

/**
 * H4K protocol family command table (SHARK H4K / SHARK H4K PLUS, Dev_Type 0x06 / 0x07 / 0x08).
 *
 * Based on "AVM H4K UDP Communication Protocol Structured Specification V1.0.1".
 * Note: VS0405E / VS0405EH (SHARK S5 / H5) do NOT use this table; they belong to avm-0617 like VS0617.
 *
 * - Same frame structure as 0617 (A55A / 29+n / A66A + 16-bit checksum)
 * - Difference: Param_Vaild of set commands is a bitmask (Bit0 = first field), while 0617 uses a field index;
 *   field names follow the 0617 naming so actions can be reused.
 * - No Codec (0x00A0) / Output (0x0090) commands, so there is no streaming feature.
 */
export const H4K_PROTOCOL_COMMANDS: Record<string, ProtocolCommand> = {
	// State report/query 0x0110 (PGM/PVW/WIPE/SPEED/FTB/Freeze/T-Bar)
	// The byte layout is parsed by ProtocolFamily.stateReport in main.ts; this field table is only used for queries and length checks
	state: {
		set: 0x0110,
		get: 0x0110,
		fields: [],
		getFields: [
			{ name: 'PGM', size: 1 },
			{ name: 'PVW', size: 1 },
			{ name: 'WipeMode', size: 1 },
			{ name: 'SpeedMode', size: 1 },
			{ name: 'FtbStatus', size: 1 },
			{ name: 'FreezeStatus', size: 1 },
			{ name: 'TBarPos', size: 1 },
			{ name: 'TBarVal', size: 2 },
		],
	},
	// Transition set 0x0020 / sync 0x0120
	transition: {
		set: 0x0020,
		get: 0x0120,
		fields: [
			{ name: 'Wipe1', size: 1 },
			{ name: 'Wipe2', size: 1 },
			{ name: 'Wipe3', size: 1 },
			{ name: 'Softness', size: 1 },
			{ name: 'Direction', size: 1 },
			{ name: 'Speed1', size: 1 },
			{ name: 'Speed2', size: 1 },
			{ name: 'TBarABMode', size: 1 },
			{ name: 'TBarStatus', size: 1 },
		],
	},
	// Luma Key set 0x0031 / query 0x0131 (SET 21B with Reset; GET 16B without Reset)
	luma: {
		set: 0x0031,
		get: 0x0131,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'KeySource', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Tolerance', size: 1 },
			{ name: 'ToleranceMin', size: 1 },
			{ name: 'ToleranceMax', size: 1 },
			{ name: 'Clip', size: 1 },
			{ name: 'ClipMin', size: 1 },
			{ name: 'ClipMax', size: 1 },
			{ name: 'MaskEnable', size: 1 },
			{ name: 'MaskLeft', size: 1 },
			{ name: 'MaskTop', size: 1 },
			{ name: 'MaskRight', size: 1 },
			{ name: 'MaskBottom', size: 1 },
			{ name: 'Reset', size: 1 },
		],
		getFields: [
			{ name: 'Status', size: 1 },
			{ name: 'KeySource', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Tolerance', size: 1 },
			{ name: 'ToleranceMin', size: 1 },
			{ name: 'ToleranceMax', size: 1 },
			{ name: 'Clip', size: 1 },
			{ name: 'ClipMin', size: 1 },
			{ name: 'ClipMax', size: 1 },
			{ name: 'MaskEnable', size: 1 },
			{ name: 'MaskLeft', size: 1 },
			{ name: 'MaskTop', size: 1 },
			{ name: 'MaskRight', size: 1 },
			{ name: 'MaskBottom', size: 1 },
		],
	},
	// Chroma Key set 0x0032 / query 0x0132 (SET 37B with Reset; GET 32B without Reset)
	// Note: bit10/bit11 are Similarity/Smooth on 0617 and Tolerance/Softness in the H4K doc (same positions)
	chroma: {
		set: 0x0032,
		get: 0x0132,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'KeySource', size: 1 },
			{ name: 'KeyType', size: 1 },
			{ name: 'KeyColor', size: 3 },
			{ name: 'FetchPosX', size: 2 },
			{ name: 'FetchPosY', size: 2 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Angle', size: 1 },
			{ name: 'Tolerance', size: 1 },
			{ name: 'Softness', size: 1 },
			{ name: 'Clip', size: 1 },
			{ name: 'ClipMin', size: 1 },
			{ name: 'ClipMax', size: 1 },
			{ name: 'Correction', size: 1 },
			{ name: 'CorrectionVal', size: 1 },
			{ name: 'Brightness', size: 1 },
			{ name: 'Contrast', size: 1 },
			{ name: 'Saturation', size: 1 },
			{ name: 'ColorRed', size: 1 },
			{ name: 'ColorGreen', size: 1 },
			{ name: 'ColorBlue', size: 1 },
			{ name: 'MaskEnable', size: 1 },
			{ name: 'MaskLeft', size: 1 },
			{ name: 'MaskTop', size: 1 },
			{ name: 'MaskRight', size: 1 },
			{ name: 'MaskBottom', size: 1 },
			{ name: 'Reset', size: 1 },
		],
		getFields: [
			{ name: 'Status', size: 1 },
			{ name: 'KeySource', size: 1 },
			{ name: 'KeyType', size: 1 },
			{ name: 'KeyColor', size: 3 },
			{ name: 'FetchPosX', size: 2 },
			{ name: 'FetchPosY', size: 2 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Angle', size: 1 },
			{ name: 'Tolerance', size: 1 },
			{ name: 'Softness', size: 1 },
			{ name: 'Clip', size: 1 },
			{ name: 'ClipMin', size: 1 },
			{ name: 'ClipMax', size: 1 },
			{ name: 'Correction', size: 1 },
			{ name: 'CorrectionVal', size: 1 },
			{ name: 'Brightness', size: 1 },
			{ name: 'Contrast', size: 1 },
			{ name: 'Saturation', size: 1 },
			{ name: 'ColorRed', size: 1 },
			{ name: 'ColorGreen', size: 1 },
			{ name: 'ColorBlue', size: 1 },
			{ name: 'MaskEnable', size: 1 },
			{ name: 'MaskLeft', size: 1 },
			{ name: 'MaskTop', size: 1 },
			{ name: 'MaskRight', size: 1 },
			{ name: 'MaskBottom', size: 1 },
		],
	},
	// PIP set 0x0033 / query 0x0133 (SET 13B with Reset; GET 8B without Reset)
	// H4K has a single PIP layer; the pip1 command key is reused so existing actions/feedbacks work
	pip1: {
		set: 0x0033,
		get: 0x0133,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'Source', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Reset', size: 1 },
			{ name: 'BorderEnable', size: 1 },
			{ name: 'BorderColor', size: 1 },
			{ name: 'BorderWidth', size: 1 },
		],
		getFields: [
			{ name: 'Status', size: 1 },
			{ name: 'Source', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'BorderEnable', size: 1 },
			{ name: 'BorderColor', size: 1 },
			{ name: 'BorderWidth', size: 1 },
		],
	},
	// DSK set 0x0034 / query 0x0134 (same layout as LUMA; SET 21B / GET 16B)
	// Note: DSK is 0x0040 on 0617
	dsk: {
		set: 0x0034,
		get: 0x0134,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'KeySource', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Tolerance', size: 1 },
			{ name: 'ToleranceMin', size: 1 },
			{ name: 'ToleranceMax', size: 1 },
			{ name: 'Clip', size: 1 },
			{ name: 'ClipMin', size: 1 },
			{ name: 'ClipMax', size: 1 },
			{ name: 'MaskEnable', size: 1 },
			{ name: 'MaskLeft', size: 1 },
			{ name: 'MaskTop', size: 1 },
			{ name: 'MaskRight', size: 1 },
			{ name: 'MaskBottom', size: 1 },
			{ name: 'Reset', size: 1 },
		],
		getFields: [
			{ name: 'Status', size: 1 },
			{ name: 'KeySource', size: 1 },
			{ name: 'Size', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Tolerance', size: 1 },
			{ name: 'ToleranceMin', size: 1 },
			{ name: 'ToleranceMax', size: 1 },
			{ name: 'Clip', size: 1 },
			{ name: 'ClipMin', size: 1 },
			{ name: 'ClipMax', size: 1 },
			{ name: 'MaskEnable', size: 1 },
			{ name: 'MaskLeft', size: 1 },
			{ name: 'MaskTop', size: 1 },
			{ name: 'MaskRight', size: 1 },
			{ name: 'MaskBottom', size: 1 },
		],
	},
	// Logo set 0x0040 / query 0x0140 (GET 5B: Status/Select/PosX/PosY/Logo_valid_pos)
	// Note: Logo is 0x0041 on 0617
	logo: {
		set: 0x0040,
		get: 0x0140,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'Select', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'Reset', size: 1 },
		],
		getFields: [
			{ name: 'Status', size: 1 },
			{ name: 'Select', size: 1 },
			{ name: 'PosX', size: 1 },
			{ name: 'PosY', size: 1 },
			{ name: 'ValidPos', size: 1 },
		],
	},
	// Audio set 0x0050 / query 0x0150 (SET 34B with Reset_All; GET 29B without Reset_All)
	// 4 inputs + 2 MIC, no XLR / LineIn / Guitar / PreGain
	audio: {
		set: 0x0050,
		get: 0x0150,
		fields: [
			{ name: 'Mute', size: 1 },
			{ name: 'AllAfv', size: 1 },
			{ name: 'Reset', size: 1 },
			{ name: 'MasterEnable', size: 1 },
			{ name: 'MasterVolume', size: 1 },
			{ name: 'EarEnable', size: 1 },
			{ name: 'EarVolume', size: 1 },
			{ name: 'EarSource', size: 1 },
			{ name: 'In1Enable', size: 1 },
			{ name: 'In1Volume', size: 1 },
			{ name: 'In1Afv', size: 1 },
			{ name: 'In1Delay', size: 1 },
			{ name: 'In2Enable', size: 1 },
			{ name: 'In2Volume', size: 1 },
			{ name: 'In2Afv', size: 1 },
			{ name: 'In2Delay', size: 1 },
			{ name: 'In3Enable', size: 1 },
			{ name: 'In3Volume', size: 1 },
			{ name: 'In3Afv', size: 1 },
			{ name: 'In3Delay', size: 1 },
			{ name: 'In4Enable', size: 1 },
			{ name: 'In4Volume', size: 1 },
			{ name: 'In4Afv', size: 1 },
			{ name: 'In4Delay', size: 1 },
			{ name: 'Mic1Mode', size: 1 },
			{ name: 'Mic1Enable', size: 1 },
			{ name: 'Mic1Volume', size: 1 },
			{ name: 'Mic2Mode', size: 1 },
			{ name: 'Mic2Enable', size: 1 },
			{ name: 'Mic2Volume', size: 1 },
		],
		getFields: [
			{ name: 'Mute', size: 1 },
			{ name: 'AllAfv', size: 1 },
			{ name: 'MasterEnable', size: 1 },
			{ name: 'MasterVolume', size: 1 },
			{ name: 'EarEnable', size: 1 },
			{ name: 'EarVolume', size: 1 },
			{ name: 'EarSource', size: 1 },
			{ name: 'In1Enable', size: 1 },
			{ name: 'In1Volume', size: 1 },
			{ name: 'In1Afv', size: 1 },
			{ name: 'In1Delay', size: 1 },
			{ name: 'In2Enable', size: 1 },
			{ name: 'In2Volume', size: 1 },
			{ name: 'In2Afv', size: 1 },
			{ name: 'In2Delay', size: 1 },
			{ name: 'In3Enable', size: 1 },
			{ name: 'In3Volume', size: 1 },
			{ name: 'In3Afv', size: 1 },
			{ name: 'In3Delay', size: 1 },
			{ name: 'In4Enable', size: 1 },
			{ name: 'In4Volume', size: 1 },
			{ name: 'In4Afv', size: 1 },
			{ name: 'In4Delay', size: 1 },
			{ name: 'Mic1Mode', size: 1 },
			{ name: 'Mic1Enable', size: 1 },
			{ name: 'Mic1Volume', size: 1 },
			{ name: 'Mic2Mode', size: 1 },
			{ name: 'Mic2Enable', size: 1 },
			{ name: 'Mic2Volume', size: 1 },
		],
	},
	// Key Type: currently active key module (0=PIP / 1=Luma / 2=Chroma / 3=DSK) - read only
	// Only GET 0x0130 (1B) is used; layer switching presses the PIP/LUMA/CHROMA/DSK KEY / ON AIR keys (0x0010)
	// instead of writing 0x0030 (fields left empty to avoid generating set actions)
	keyType: {
		set: 0x0030,
		get: 0x0130,
		fields: [],
		getFields: [{ name: 'KeyType', size: 1 }],
	},
}

function writeFieldValue(buf: Buffer, offset: number, size: number, value: number): void {
	switch (size) {
		case 1:
			buf.writeUInt8(value & 0xff, offset)
			break
		case 2:
			buf.writeUInt16BE(value & 0xffff, offset)
			break
		case 3:
			buf.writeUInt8((value >>> 16) & 0xff, offset)
			buf.writeUInt8((value >>> 8) & 0xff, offset + 1)
			buf.writeUInt8(value & 0xff, offset + 2)
			break
		case 4:
			buf.writeUInt32BE(value >>> 0, offset)
			break
		default:
			break
	}
}

/**
 * Param_Vaild encoding used by set commands.
 * - index  : write the field index (0617 / PSV0617)
 * - bitmask: write 1<<index (H4K / 0405 family)
 */
export type ParamValidMode = 'index' | 'bitmask'

/**
 * Build the Data of a set command:
 * - index mode (0617): Param_Vaild(4) = field index + that field's value
 * - bitmask mode (H4K): Param_Vaild(4) = 1<<index, and Data is sent in the fixed field layout
 *   with every field value (0 for untouched fields), otherwise the device reads the value at the wrong offset.
 */
export function buildSetData(
	cmd: ProtocolCommand,
	fieldIndex: number,
	value: number,
	paramValidMode: ParamValidMode = 'index',
): Buffer {
	const field = cmd.fields[fieldIndex]
	if (!field) return Buffer.alloc(0)

	if (paramValidMode === 'bitmask') {
		const totalSize = cmd.fields.reduce((sum, f) => sum + f.size, 0)
		const data = Buffer.alloc(4 + totalSize)
		data.writeUInt32BE((1 << fieldIndex) >>> 0, 0)
		let offset = 4
		for (let i = 0; i < cmd.fields.length; i++) {
			const f = cmd.fields[i]
			writeFieldValue(data, offset, f.size, i === fieldIndex ? value : 0)
			offset += f.size
		}
		return data
	}

	const data = Buffer.alloc(4 + field.size)
	data.writeUInt32BE(fieldIndex >>> 0, 0)
	writeFieldValue(data, 4, field.size, value)
	return data
}

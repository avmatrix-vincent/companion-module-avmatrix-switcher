/**
 * AVM 协议功能注册表（数据驱动）
 *
 * 依据《AVM UDP通信协议 V1.0.0(PSV0617)》：
 * - 每条指令的 Data 由「Param_Vaild(4字节) + 各字段值」组成（设置用）
 * - 获取指令的 Data 为「各字段值顺序拼接」（无 Param_Vaild）
 * - 字段按附件文档的 NO.x 顺序排列，字段字节偏移 = 前面字段大小之和
 *
 * 本文件只登记「简单开关(0/1)」类字段，用于自动生成 action / feedback / preset。
 * 需要文本输入、IP、时间、复杂枚举的字段一律不做。
 *
 * 注意：Param_Vaild 为 4 字节位掩码，只能寻址 NO.0~31；
 * 因此 NO.>=32 的字段（如 Audio MIC_EN=33、System IP_DHCP=33）暂不支持。
 */

export interface ProtocolField {
	name: string
	size: number
}

export interface ProtocolCommand {
	/** 设置指令 */
	set: number
	/** 查询/上报指令 */
	get: number
	/** 设置指令字段列表（顺序即 valid 位下标） */
	fields: ProtocolField[]
	/**
	 * 查询/上报回包的字段布局。
	 * 缺省与 fields 相同；H4K 的 GET 与 SET 不一致（如 luma GET 16B / SET 21B，
	 * audio GET 29B 无 Reset_All / SET 34B），必须单独声明。
	 */
	getFields?: ProtocolField[]
}

export const PROTOCOL_COMMANDS: Record<string, ProtocolCommand> = {
	// Transition 设置 0x0020 / 获取 0x0120
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
	// LUMA 设置 0x0031 / 获取 0x0131
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
	// CHROMA 设置 0x0032 / 获取 0x0132
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
	// PIP Border 设置 0x0036 / 获取 0x0136
	pipBorder: {
		set: 0x0036,
		get: 0x0136,
		fields: [
			{ name: 'Status', size: 1 },
			{ name: 'Color', size: 1 },
			{ name: 'Width', size: 1 },
		],
	},
	// PIP1 设置 0x0033 / 获取 0x0133
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
	// PIP2 设置 0x0034 / 获取 0x0134
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
	// PIP3 设置 0x0035 / 获取 0x0135
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
	// DSK 设置 0x0040 / 获取 0x0140
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
	// LOGO 设置 0x0041 / 获取 0x0141
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
	// Audio 设置 0x0050 / 获取 0x0150
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
	// Output 设置 0x0090 / 获取 0x0190
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
	// Codec 设置 0x00A0 / 获取 0x01A0
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
 * H4K 协议族（SHARK H4K / SHARK H4K PLUS，Dev_Type 0x06 / 0x07 / 0x08）命令表
 *
 * 依据《AVM H4K UDP 通信协议 结构化规范 V1.0.1》。
 * 注意：VS0405E / VS0405EH（SHARK S5 / H5）不使用本表，它们与 VS0617 同属 avm-0617。
 *
 * - 帧结构与 0617 相同（A55A / 29+n / A66A + 16bit 累加和）
 * - 差异：设置指令的 Param_Vaild 是「位域」（Bit0=第 1 个字段…），
 *   而 0617 是「字段索引」；字段命名统一沿用 0617 的写法，便于 action 复用。
 * - 无 Codec(0x00A0) / Output(0x0090) 指令，故不含 stream 功能。
 */
export const H4K_PROTOCOL_COMMANDS: Record<string, ProtocolCommand> = {
	// 状态上报/查询 0x0110（PGM/PVW/WIPE/SPEED/FTB/Freeze/T-Bar）
	// 字节布局按 main.ts 的 ProtocolFamily.stateReport 解析，字段表仅用于发出查询与长度校验
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
	// Transition 设置 0x0020 / 同步 0x0120
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
	// Luma Key 设置 0x0031 / 查询 0x0131（SET 21B 含 Reset；GET 16B 无 Reset）
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
	// Chroma Key 设置 0x0032 / 查询 0x0132（SET 37B 含 Reset；GET 32B 无 Reset）
	// 注意：bit10/bit11 在 0617 叫 Similarity/Smooth，H4K 文档叫 Tolerance/Softness（位置相同）
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
	// PIP 设置 0x0033 / 查询 0x0133（SET 13B 含 Reset；GET 8B 无 Reset）
	// H4K 仅 1 路，沿用 pip1 作为命令键以复用现有 action/feedback
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
	// DSK 设置 0x0034 / 查询 0x0134（布局同 LUMA；SET 21B / GET 16B）
	// 注意：0617 的 DSK 是 0x0040
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
	// Logo 设置 0x0040 / 查询 0x0140（GET 5B：Status/Select/PosX/PosY/Logo_valid_pos）
	// 注意：0617 的 Logo 是 0x0041
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
	// Audio 设置 0x0050 / 查询 0x0150（SET 34B 含 Reset_All；GET 29B 无 Reset_All）
	// 4 路输入 + 2 路 MIC，无 XLR / LineIn / Guitar / PreGain
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
	// Key Type：当前激活的 Key 模块（0=PIP / 1=Luma / 2=Chroma / 3=DSK）—— 只读
	// 只用 GET 0x0130（1B）；切层直接按 PIP/LUMA/CHROMA/DSK 的 Key / ON AIR 按键（0x0010），
	// 不通过 0x0030 写入（fields 置空，避免生成多余的设置动作）
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
 * 设置指令的 Param_Vaild 编码方式
 * - index  ：写字段索引（0617 / PSV0617）
 * - bitmask：写位域 1<<索引（H4K / 0405 系列）
 */
export type ParamValidMode = 'index' | 'bitmask'

/**
 * 构建设置指令 Data：
 * - index 模式（0617）：Param_Vaild(4) = 字段索引 + 该字段值
 * - bitmask 模式（H4K）：Param_Vaild(4) = 1<<索引，且 Data 按【固定字段布局】输出
 *   全部字段值（未设置的填 0），否则设备会把值错位读到第一个字段。
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

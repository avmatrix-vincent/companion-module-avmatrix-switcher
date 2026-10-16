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
	/** 获取指令 */
	get: number
	/** 字段列表（顺序即 NO.x） */
	fields: ProtocolField[]
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
 * 构建设置指令 Data（按设备实测样例）：
 * Param_Vaild(4字节) + 目标参数的值
 * Param_Vaild 为“参数索引”（该参数在字段列表中的下标，即文档 NO.x）。
 * 例如 Transition Softness（NO.4, 值 50）=> 00 00 00 04 32
 */
export function buildSetData(cmd: ProtocolCommand, fieldIndex: number, value: number): Buffer {
	const field = cmd.fields[fieldIndex]
	if (!field) return Buffer.alloc(0)
	const data = Buffer.alloc(4 + field.size)
	data.writeUInt32BE(fieldIndex >>> 0, 0)
	writeFieldValue(data, 4, field.size, value)
	return data
}

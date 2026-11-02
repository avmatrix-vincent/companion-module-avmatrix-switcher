import type { ParamValidMode, ProtocolCommand } from '../features.js'

/** 协议族：同一族内通信方式一致（报文结构 / 命令码 / 字段顺序 / 按键表） */
export type ProtocolFamilyId = 'avm-0605' | 'avm-0617' | 'avm-h4k'

/** 按键报文 Data 结构版本 */
export type KeyPressFormat =
	| 'index' // 0617：Param_Vaild=参数索引（0=Key_val / 1=T_Bar_val / 2=b_bar_pos）+ 2 字节值
	| 'keytype' // H4K：Param_Vaild 位域（Bit0=Key_type / Bit1=Key_val）+ Key_type(1) + Key_val(2)

/** 产品按键值表（同一协议族内固定；不同产品若不同可各自覆盖） */
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
	/** Stream 1~3 按键（无该能力的协议为空数组） */
	stream: number[]
	wipe: number[]
	mix: number
	dip: number
	flipFlop: number
	freeze: number
	/** 以下为 H4K 特有独立按键，0617 不支持时置 0 */
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
 * 0x0110 状态上报的字节布局（各协议不同）。
 * - 0617：10 字节，[6..7]=T_Bar_val，[8..9]=b_bar_pos
 * - H4K ：9 字节，[6]=T_Bar_Pos，[7..8]=T_Bar_Val
 */
export interface StateReportSpec {
	/** 最小有效长度 */
	size: number
	pgm: number
	pvw: number
	wipeMode: number
	speedMode: number
	ftb: number
	freeze: number
	/** T-Bar 位置（H4K 有；0617 无） */
	tBarPos?: { offset: number; size: number }
	/** T-Bar 值 */
	tBarValue: { offset: number; size: number }
	/** 0617 的 b_bar_pos */
	bBarPos?: { offset: number; size: number }
}

export interface ProtocolFamily {
	id: ProtocolFamilyId
	displayName: string
	commands: Record<string, ProtocolCommand>
	/** 设置指令 Param_Vaild 编码方式 */
	paramValidMode: ParamValidMode
	/** 按键（0x0010）报文结构版本 */
	keyPressFormat: KeyPressFormat
	/** 按键值表 */
	keyMap: KeyMap
	/** PGM/PVW 输入路数 */
	inputCount: number
	/** PIP 路数 */
	pipCount: number
	/** WIPE 样式数量 */
	wipeCount: number
	/** Logo 可选数量 */
	logoCount: number
	/** 是否有 Stream（依赖 Codec 0x00A0） */
	hasStream: boolean
	/** 0x0110 状态上报的字节布局 */
	stateReport?: StateReportSpec
	/** T-Bar 原始值上限（0617 / H4K 均为 0~4095） */
	tBarMax?: number
	/**
	 * 无心跳指令的协议族使用的探活指令（Data 为空）。
	 * 例：H4K 无 0xEEEE 心跳，用 0x0001（读版本号）作为在线探测；
	 * 0617 / 0605 不设此项，仍用 0xEEEE（有 MAC）/ 0xFFFF（无 MAC）。
	 */
	probeCommand?: number
	/**
	 * 是否保留 0617 的 0x0001/0x0002 = 电源开/关 语义。
	 * H4K 中 0x0001=读版本号、0x0002=输入信息，必须置 false，否则响应会被误判。
	 */
	legacyPowerCommands?: boolean
	/** 键源下拉项（各协议的枚举起点不同） */
	keySources: Array<{ id: number; label: string }>
	/** PIP 源下拉项 */
	pipSources: Array<{ id: number; label: string }>
	/** WIPE 样式下拉项（0617=0~10；H4K=0~27，下发值 = 下拉 id，0 = 第一张图） */
	wipeStyles: Array<{ id: number; label: string }>
	/**
	 * WIPE 样式下发偏移：发送值 = 下拉 id - wipeStyleOffset。
	 * 当前各协议族均为 0（下拉 id 即下发值）；保留字段供未来设备样式枚举起点不同时使用。
	 */
	wipeStyleOffset?: number
	/**
	 * 推杆下发方式（仅 keyPressFormat='keytype' 的族生效）：
	 * - 'val'：valid=0x03，Key_Val 0~4095（H4K 文档：Key_type=2 时 Key_Val 为推杆数据）
	 * - 'pos'：valid=0x05，Key_Pos 0~100%
	 * - 'both'：valid=0x07，Key_Val 0~4095 + Key_Pos 档位 0/1/2（上位机实测报文）
	 * - 'valPct'：valid=0x03，Key_Val 用百分比 0~100
	 */
	tBarSendMode?: 'pos' | 'val' | 'both' | 'valPct'
	/**
	 * 是否隐藏 “All AFV” 动作（H4K 无此功能）。
	 * 仅影响 UI 注册；audio 协议字段 AllAfv 仍保留在固定布局中（不能删，否则 34B/29B 会错位）。
	 */
	hideAllAfvAction?: boolean
	/**
	 * 是否隐藏 “Audio Reset” 动作及预设（H4K 不提供音频整体复位）。
	 * 仅影响 UI 注册；audio 协议字段 Reset 仍保留在固定布局中（不能删，否则后续 31 个字段全部错位）。
	 */
	hideAudioResetAction?: boolean
	/**
	 * 是否额外提供“WIPE 通道 + 样式”合并动作（trans_wipe_style）。
	 * 仅 H4K 开启；0617/0605 保持原有的 trans_wipe1~4 动作列表不变。
	 */
	mergeWipeStyleAction?: boolean
	/**
	 * 连接后是否自动查询所有带获取码的指令（H4K 打开）。
	 * 关闭时仅使用 stateQueryKeys（或完全不查询）。
	 */
	queryAllOnConnect?: boolean
	/**
	 * 连接后需要主动查询的命令键：
	 * 对无全量状态上报（如 0617 的 0x0110）的协议族，通过 0x00xx + Param_Vaild=0 主动获取。
	 */
	stateQueryKeys?: string[]
	/**
	 * 是否处理设备的查询应答（Pack_Type=1）。
	 * 打开后 onData 回调传入的 payload 直接作为状态数据解析（H4K）。
	 * 关闭（默认）时保持旧行为：只处理主动上报（Pack_Type=2），不影响 0617/0605。
	 */
	parseQueryReplies?: boolean
}

/**
 * 产品功能分组键。
 * action / feedback / preset 通过 id 前缀自动归入某一分组（见 index.ts 的 FEATURE_ID_RULES），
 * 产品档案只需声明自己支持哪些分组。
 */
export type DeviceFeatureKey =
	| 'source' // PGM/PVW 源切换
	| 'transition' // CUT/AUTO/FTB/WIPE/MIX/DIP/FREEZE/T-Bar
	| 'stream' // Stream 1~3
	| 'pip'
	| 'luma'
	| 'chroma'
	| 'dsk'
	| 'logo'
	| 'audio'
	| 'system' // 连接、扫描等通用功能，始终启用

export interface DeviceProfile {
	/** 产品档案内部标识（如 shark-s6-plus） */
	id: string
	/** 界面显示名称（如 SHARK S6 PLUS） */
	displayName: string
	/** 扫描回包 model 字段的前缀；顺序无关，匹配时按最长前缀优先 */
	modelPrefixes: string[]
	/** 心跳报文使用的 Dev_Type（与上位机 get_udp_model_index 一致） */
	udpDevType: number
	/**
	 * 广播发现回包里的设备类型标识（productType，字节偏移 22）。
	 * 声明后优先按类型识别（比 model 字符串可靠，model 只有 10 字节）。
	 * 例：H4K PLUS=0x06/0x07，H4K=0x08。
	 */
	productTypes?: number[]
	/** 该产品使用的协议族（决定通信命令表） */
	protocolFamily: ProtocolFamilyId
	/** 该产品启用的功能分组 */
	features: DeviceFeatureKey[]
	/** 产品私有/覆盖的协议命令（在协议族命令表之上合并，键相同则覆盖） */
	protocolOverrides?: Record<string, ProtocolCommand>
}

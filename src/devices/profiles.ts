import type { DeviceFeatureKey, DeviceProfile } from './types.js'

/** 0617 基线功能集（PSV0617 / SHARK S6 PLUS 的全部功能） */
const S6_PLUS_FEATURES: DeviceFeatureKey[] = [
	'source',
	'transition',
	'stream',
	'pip',
	'luma',
	'chroma',
	'dsk',
	'logo',
	'audio',
	'system',
]

/**
 * S5（VS0405E）：协议族与 0617 相同（avm-0617），功能项独立维护。
 * 目前与 0617 一致；后续若有差异，只需在本数组增删分组。
 */
const S5_FEATURES: DeviceFeatureKey[] = [...S6_PLUS_FEATURES]

/**
 * H5（VS0405EH）：协议族与 0617 相同（avm-0617），功能项独立维护。
 * 同 S5，按实际能力裁剪 features 即可。
 */
const H5_FEATURES: DeviceFeatureKey[] = [...S6_PLUS_FEATURES]

/**
 * H4K 系列（SHARK H4K / SHARK H4K PLUS）：使用 avm-h4k 协议族。
 * H4K 协议无 Codec(0x00A0) 指令，因此去掉 'stream'；
 * 输入 4 路 / PIP 1 路 / WIPE 3 个 / Logo 2 个 由协议族能力控制。
 */
const H4K_FEATURES: DeviceFeatureKey[] = S6_PLUS_FEATURES.filter((f) => f !== 'stream')

/**
 * 产品档案表（新增产品只需在此追加一项）
 * 注意：VS0405EH 以 VS0405E 开头，依赖最长前缀优先匹配才能与 S5 区分。
 */
export const DEVICE_PROFILES: DeviceProfile[] = [
	{
		id: 'shark-s6',
		displayName: 'SHARK S6',
		modelPrefixes: ['VS0605'],
		udpDevType: 1,
		protocolFamily: 'avm-0605',
		features: [...S6_PLUS_FEATURES],
	},
	{
		id: 'shark-s6-plus',
		displayName: 'SHARK S6 PLUS',
		modelPrefixes: ['VS0617', 'PSV0617'],
		udpDevType: 9,
		protocolFamily: 'avm-0617',
		features: S6_PLUS_FEATURES,
	},
	{
		id: 'shark-s5',
		displayName: 'SHARK S5',
		modelPrefixes: ['VS0405E'],
		udpDevType: 0x0a, // 0x0A = 10
		protocolFamily: 'avm-0617',
		features: S5_FEATURES,
	},
	{
		id: 'shark-h5',
		displayName: 'SHARK H5',
		modelPrefixes: ['VS0405EH'],
		udpDevType: 0x0b, // 0x0B = 11
		protocolFamily: 'avm-0617',
		features: H5_FEATURES,
	},
	{
		// H4K PLUS：设备类型标识 0x06 / 0x07（优先按此识别，model 字符串仅兜底）
		id: 'shark-h4k-plus',
		displayName: 'SHARK H4K PLUS',
		modelPrefixes: ['SHARK H4K PLUS', 'SHARK H4KPLUS', 'H4K PLUS', 'H4KPLUS', 'H4K-PLUS'],
		productTypes: [0x06, 0x07],
		udpDevType: 0x06,
		protocolFamily: 'avm-h4k',
		features: H4K_FEATURES,
	},
	{
		// H4K：设备类型标识 0x08
		// 注意：'SHARK H4K' / 'H4K' 都是短前缀，依赖最长前缀优先才不会抢走 H4K PLUS
		id: 'shark-h4k',
		displayName: 'SHARK H4K',
		modelPrefixes: ['SHARK H4K', 'H4K'],
		productTypes: [0x08],
		udpDevType: 0x08,
		protocolFamily: 'avm-h4k',
		features: H4K_FEATURES,
	},
]

/** 未识别型号时使用的档案（保持原有行为：按 S6 PLUS 全功能处理） */
export const DEFAULT_DEVICE_PROFILE: DeviceProfile =
	DEVICE_PROFILES.find((p) => p.id === 'shark-s6-plus') ?? DEVICE_PROFILES[0]

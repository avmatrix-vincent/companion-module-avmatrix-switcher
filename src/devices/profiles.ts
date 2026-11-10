import type { DeviceFeatureKey, DeviceProfile } from './types.js'

/** 0617 baseline feature set (all features of PSV0617 / SHARK S6 PLUS) */
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
 * S5 (VS0405E): same protocol family as 0617 (avm-0617); features are maintained separately.
 * Currently identical to 0617; add or remove groups here if the capabilities diverge later.
 */
const S5_FEATURES: DeviceFeatureKey[] = [...S6_PLUS_FEATURES]

/**
 * H5 (VS0405EH): same protocol family as 0617 (avm-0617); features are maintained separately.
 * Like S5, trim the features array to the actual capabilities.
 */
const H5_FEATURES: DeviceFeatureKey[] = [...S6_PLUS_FEATURES]

/**
 * H4K family (SHARK H4K / SHARK H4K PLUS): uses the avm-h4k protocol family.
 * The H4K protocol has no Codec (0x00A0) command, so 'stream' is removed;
 * 4 inputs / 1 PIP / 3 wipes / 2 logos are controlled by the protocol family capabilities.
 */
const H4K_FEATURES: DeviceFeatureKey[] = S6_PLUS_FEATURES.filter((f) => f !== 'stream')

/**
 * Product profile table (add a new product by appending one entry here).
 * Note: VS0405EH starts with VS0405E, so longest-prefix matching is required to tell it from S5.
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
		productTypes: [0x0a],
		udpDevType: 0x0a, // 0x0A = 10
		protocolFamily: 'avm-0617',
		features: S5_FEATURES,
	},
	{
		id: 'shark-h5',
		displayName: 'SHARK H5',
		modelPrefixes: ['VS0405EH'],
		productTypes: [0x0b],
		udpDevType: 0x0b, // 0x0B = 11
		protocolFamily: 'avm-0617',
		features: H5_FEATURES,
	},
	{
		// H4K PLUS: device type id 0x06 / 0x07 (matched first; the model string is only a fallback)
		id: 'shark-h4k-plus',
		displayName: 'SHARK H4K PLUS',
		modelPrefixes: ['SHARK H4K PLUS', 'SHARK H4KPLUS', 'H4K PLUS', 'H4KPLUS', 'H4K-PLUS'],
		productTypes: [0x06, 0x07],
		udpDevType: 0x06,
		protocolFamily: 'avm-h4k',
		features: H4K_FEATURES,
	},
	{
		// H4K: device type id 0x08
		// Note: 'SHARK H4K' / 'H4K' are short prefixes; longest-prefix matching keeps them from taking H4K PLUS
		id: 'shark-h4k',
		displayName: 'SHARK H4K',
		modelPrefixes: ['SHARK H4K', 'H4K'],
		productTypes: [0x08],
		udpDevType: 0x08,
		protocolFamily: 'avm-h4k',
		features: H4K_FEATURES,
	},
]

/** Profile used when the model is unknown (keeps the previous behaviour: full S6 PLUS feature set) */
export const DEFAULT_DEVICE_PROFILE: DeviceProfile =
	DEVICE_PROFILES.find((p) => p.id === 'shark-s6-plus') ?? DEVICE_PROFILES[0]

import type { ProtocolCommand } from '../features.js'
import { DEFAULT_DEVICE_PROFILE, DEVICE_PROFILES } from './profiles.js'
import { getProtocolFamily } from './protocols.js'
import type { DeviceFeatureKey, DeviceProfile } from './types.js'

export type { DeviceFeatureKey, DeviceProfile, ProtocolFamily, ProtocolFamilyId } from './types.js'
export { DEFAULT_DEVICE_PROFILE, DEVICE_PROFILES } from './profiles.js'
export { PROTOCOL_FAMILIES, getProtocolFamily } from './protocols.js'

function normalizeModel(rawModel: string | undefined): string {
	return (rawModel ?? '').trim().toUpperCase()
}

/**
 * 匹配产品档案。
 * 优先级：
 *  1) 设备类型标识（广播回包 productType，H4K 系 6/7/8 可唯一区分；比 model 字符串可靠）
 *  2) 型号前缀，最长前缀优先（VS0405EH 优于 VS0405E）
 */
export function matchDeviceProfile(rawModel: string | undefined, deviceType?: number): DeviceProfile | undefined {
	// 1) 设备类型标识优先（仅对声明了 productTypes 的产品生效，不影响 0617 / 0605）
	if (typeof deviceType === 'number') {
		const byType = DEVICE_PROFILES.find((p) => p.productTypes?.includes(deviceType))
		if (byType) return byType
	}

	// 2) 型号前缀（最长优先）
	const code = normalizeModel(rawModel)
	if (!code) return undefined

	let matched: DeviceProfile | undefined
	let matchedLength = 0
	for (const profile of DEVICE_PROFILES) {
		for (const prefix of profile.modelPrefixes) {
			const p = normalizeModel(prefix)
			if (p && code.startsWith(p) && p.length > matchedLength) {
				matched = profile
				matchedLength = p.length
			}
		}
	}
	return matched
}

/** 取当前设备的产品档案；未识别型号回退默认档案 */
export function getActiveProfile(rawModel: string | undefined, deviceType?: number): DeviceProfile {
	return matchDeviceProfile(rawModel, deviceType) ?? DEFAULT_DEVICE_PROFILE
}

/** 型号代码 / 设备类型 -> 界面显示名（未识别时保留原始代码） */
export function resolveDeviceModel(rawModel: string | undefined, deviceType?: number): string {
	const profile = matchDeviceProfile(rawModel, deviceType)
	if (profile) return profile.displayName
	return (rawModel ?? '').trim() || 'Unknown Device'
}

/**
 * 型号代码 / 设备类型 -> 心跳 Dev_Type。
 * 若设备类型能唯一标识该产品，直接用实测值（H4K PLUS 的 0x06/0x07 原样下发）；
 * 否则按型号查表；未识别返回 0xFF，由调用方回退 productType。
 */
export function getUdpModelIndex(rawModel: string | undefined, deviceType?: number): number {
	const profile = matchDeviceProfile(rawModel, deviceType)
	if (!profile) return 0xff
	if (typeof deviceType === 'number' && profile.productTypes?.includes(deviceType)) return deviceType
	return profile.udpDevType
}

/** 协议族命令表 + 产品覆盖，得到该产品实际使用的命令表 */
export function buildProtocolCommands(profile: DeviceProfile): Record<string, ProtocolCommand> {
	const base = getProtocolFamily(profile.protocolFamily).commands
	return profile.protocolOverrides ? { ...base, ...profile.protocolOverrides } : base
}

/** 该产品是否启用某功能分组（system 始终启用） */
export function hasFeature(profile: DeviceProfile, feature: DeviceFeatureKey): boolean {
	return feature === 'system' || profile.features.includes(feature)
}

/** action / feedback / preset 的 id -> 功能分组；未命中规则视为 system */
const FEATURE_ID_RULES: Array<[RegExp, DeviceFeatureKey]> = [
	[/^pip\d/, 'pip'],
	[/^luma/, 'luma'],
	[/^chroma/, 'chroma'],
	[/^dsk/, 'dsk'],
	[/^logo/, 'logo'],
	[/^audio/, 'audio'],
	[/^mute_active/, 'audio'],
	[/^tbar/, 'transition'],
	[/^trans/, 'transition'],
	[/^switch_transition/, 'transition'],
	[/^switch_(cut|auto|ftb|mute)$/, 'transition'],
	[/^auto_active/, 'transition'],
	[/^ftb_active/, 'transition'],
	[/^freeze_active/, 'transition'],
	[/^wipe_active/, 'transition'],
	[/^wipe_style/, 'transition'],
	[/^stream_active/, 'stream'],
	[/^switch_stream/, 'stream'],
	[/^pgm/, 'source'],
	[/^pvw/, 'source'],
	[/^set_source/, 'source'],
]

export function featureOfId(id: string): DeviceFeatureKey {
	for (const [pattern, feature] of FEATURE_ID_RULES) {
		if (pattern.test(id)) return feature
	}
	return 'system'
}

export function isIdEnabled(profile: DeviceProfile, id: string): boolean {
	return hasFeature(profile, featureOfId(id))
}

/** 按产品档案裁剪 action / feedback / preset 定义表 */
export function filterByProfile<T>(definitions: Record<string, T>, profile: DeviceProfile): Record<string, T> {
	const result: Record<string, T> = {}
	for (const [id, def] of Object.entries(definitions)) {
		if (isIdEnabled(profile, id)) result[id] = def
	}
	return result
}

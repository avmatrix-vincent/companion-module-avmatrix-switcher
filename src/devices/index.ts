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
 * Match a device profile.
 * Priority:
 *  1) Device type id (productType from the discovery reply; 6/7/8 uniquely identify the H4K family)
 *  2) Model prefix, longest prefix first (VS0405EH before VS0405E)
 */
export function matchDeviceProfile(rawModel: string | undefined, deviceType?: number): DeviceProfile | undefined {
	// 1) Device type id first (only for profiles declaring productTypes; 0617 / 0605 unaffected)
	if (typeof deviceType === 'number') {
		const byType = DEVICE_PROFILES.find((p) => p.productTypes?.includes(deviceType))
		if (byType) return byType
	}

	// 2) Model prefix (longest match wins)
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

/** Profile for the current device; unknown models fall back to the default profile. */
export function getActiveProfile(rawModel: string | undefined, deviceType?: number): DeviceProfile {
	return matchDeviceProfile(rawModel, deviceType) ?? DEFAULT_DEVICE_PROFILE
}

/** Look up a profile by its id (used by the manual Device Model config). */
export function getProfileById(id: string | undefined): DeviceProfile | undefined {
	if (!id) return undefined
	return DEVICE_PROFILES.find((p) => p.id === id)
}

/** Model code / device type -> display name (keeps the raw code when unknown). */
export function resolveDeviceModel(rawModel: string | undefined, deviceType?: number): string {
	const profile = matchDeviceProfile(rawModel, deviceType)
	if (profile) return profile.displayName
	return (rawModel ?? '').trim() || 'Unknown Device'
}

/**
 * Model code / device type -> heartbeat Dev_Type.
 * When the device type uniquely identifies the product, use the measured value
 * (H4K PLUS 0x06/0x07 is sent as-is); otherwise look it up by model.
 * Returns 0xFF when unknown, so the caller can fall back to productType.
 */
export function getUdpModelIndex(rawModel: string | undefined, deviceType?: number): number {
	const profile = matchDeviceProfile(rawModel, deviceType)
	if (!profile) return 0xff
	if (typeof deviceType === 'number' && profile.productTypes?.includes(deviceType)) return deviceType
	return profile.udpDevType
}

/** Protocol-family command table plus product overrides. */
export function buildProtocolCommands(profile: DeviceProfile): Record<string, ProtocolCommand> {
	const base = getProtocolFamily(profile.protocolFamily).commands
	return profile.protocolOverrides ? { ...base, ...profile.protocolOverrides } : base
}

/** Whether a feature group is enabled on this product (system is always enabled). */
export function hasFeature(profile: DeviceProfile, feature: DeviceFeatureKey): boolean {
	return feature === 'system' || profile.features.includes(feature)
}

/** action / feedback / preset id -> feature group; unknown ids count as system. */
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

/** Filter action / feedback / preset definitions by product profile. */
export function filterByProfile<T>(definitions: Record<string, T>, profile: DeviceProfile): Record<string, T> {
	const result: Record<string, T> = {}
	for (const [id, def] of Object.entries(definitions)) {
		if (isIdEnabled(profile, id)) result[id] = def
	}
	return result
}

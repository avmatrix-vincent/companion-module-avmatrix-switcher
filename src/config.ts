import { Regex, type SomeCompanionConfigField } from '@companion-module/base'

// Fixed UDP port used by the device control protocol (not user configurable)
export const DEVICE_PORT = 7000

// Model -> display name / Dev_Type / protocol family / feature set is maintained in src/devices
// Add a new model by editing src/devices/profiles.ts only
import { DEVICE_PROFILES, resolveDeviceModel } from './devices/index.js'
export { resolveDeviceModel, DEVICE_PROFILES }

export interface ModuleConfig {
	/** Device IP selected in the Device dropdown (from UDP discovery) */
	device: string
	/** Target IP, editable by hand; the connection always uses this value */
	host: string
	/** Whether the manual Device Model should be used instead of the scan result */
	manualModel?: boolean
	/** Manual device model (profile id), used when manualModel is enabled and the device is not discovered */
	deviceModel?: string
	/** Devices found by the last scan, persisted so the dropdown is not empty after a restart */
	devices?: SavedDevice[]
}

/** Device entry persisted in the config */
export interface SavedDevice {
	host: string
	name: string
	/** Device MAC, required for heartbeat and disconnect detection; written by the scan */
	mac?: string
	/** Device type (used as heartbeat Dev_Type); written by the scan */
	productType?: number
	/** Heartbeat Dev_Type (mapped from the model); written by the scan */
	udpType?: number
	/** Raw model code (e.g. VS0617E), used to recompute Dev_Type from the mapping table */
	rawModel?: string
}

/** One entry of the Device dropdown */
export interface DeviceChoice {
	host: string
	label: string
}

/** Product model detected from the scan, shown in the AUTO SCAN entry */
export interface AutoModelChoice {
	id: string
	name: string
}

export function GetConfigFields(
	devices: DeviceChoice[],
	autoModel?: AutoModelChoice,
	current?: ModuleConfig,
): SomeCompanionConfigField[] {
	// The first option is a placeholder so the dropdown always has a value (replaced once a device is found)
	const choices =
		devices.length > 0
			? devices.map((d) => ({ id: d.host, label: d.label }))
			: [{ id: '', label: 'No supported device found' }]

	const defaultDevice = current?.device && choices.some((c) => c.id === current.device) ? current.device : choices[0].id

	// Target IP follows the selected Device; a manually edited value is kept
	const defaultHost = current?.host || current?.device || devices[0]?.host || ''

	// Manual model selection. The first entry follows the scan: it shows the detected model, so the
	// user can see what AUTO SCAN resolved to; when nothing was found the user must pick a model.
	const autoLabel = autoModel ? `AUTO SCAN (${autoModel.name})` : 'AUTO SCAN (no device found)'
	const modelChoices = [
		{ id: '', label: autoLabel },
		...DEVICE_PROFILES.map((p) => ({ id: p.id, label: p.displayName })),
	]

	return [
		{
			type: 'dropdown',
			id: 'device',
			label: 'Device',
			width: 12,
			choices,
			default: defaultDevice,
			tooltip: 'Devices found by UDP broadcast scan; the first one is selected by default',
		},
		{
			type: 'textinput',
			id: 'host',
			label: 'Target IP',
			width: 12,
			regex: Regex.IP,
			default: defaultHost,
			tooltip: 'IP of the selected device; can be edited manually (useful when the device is on another subnet)',
		},
		{
			type: 'checkbox',
			id: 'manualModel',
			label: 'Manual Device Model',
			width: 12,
			default: current?.manualModel ?? false,
			tooltip:
				'Turn on to always use the model selected below, even when the scan finds the device. Leave off to always use the scan result.',
		},
		{
			type: 'dropdown',
			id: 'deviceModel',
			label: 'Device Model',
			width: 12,
			choices: modelChoices,
			default: current?.deviceModel ?? '',
			// Only relevant when the manual switch above is on
			isVisible: (options) => !!options.manualModel,
			tooltip:
				'Used whenever Manual Device Model is on. Select the model that matches the hardware (for example SHARK H4K) so the correct protocol is used.',
		},
	]
}

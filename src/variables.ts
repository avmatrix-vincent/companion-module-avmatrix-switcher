import type { ModuleInstance } from './main.js'

export function UpdateVariableDefinitions(self: ModuleInstance): void {
	self.setVariableDefinitions([
		{ variableId: 'device_model', name: 'Device model' },
		{ variableId: 'device_ip', name: 'Device IP address and port' },
		{ variableId: 'connection_status', name: 'Connection status' },
		{ variableId: 'pgm_source', name: 'PGM source (label)' },
		{ variableId: 'pvw_source', name: 'PVW source (label)' },
		{ variableId: 'pgm_value', name: 'PGM reported value (1-8)' },
		{ variableId: 'pvw_value', name: 'PVW reported value (1-8)' },
		{ variableId: 'wipe_mode', name: 'WIPE mode (1-6)' },
		{ variableId: 'wipe_label', name: 'WIPE mode (label)' },
		{ variableId: 'speed_mode', name: 'SPEED mode (1-2)' },
		{ variableId: 'ftb_state', name: 'FTB state (OFF/ON)' },
		{ variableId: 'freeze_state', name: 'Freeze state (OFF/ON)' },
		{ variableId: 'tbar_value', name: 'T-Bar current value (0-500)' },
		{ variableId: 'last_action', name: 'Last executed action key' },
	])
}

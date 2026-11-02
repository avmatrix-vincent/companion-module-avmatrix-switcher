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
		// 各 Wipe 通道的样式（0x0120 回读；H4K 3 组，0617 4 组）
		{ variableId: 'wipe1_style', name: 'WIPE1 style value' },
		{ variableId: 'wipe1_style_label', name: 'WIPE1 style (label)' },
		{ variableId: 'wipe2_style', name: 'WIPE2 style value' },
		{ variableId: 'wipe2_style_label', name: 'WIPE2 style (label)' },
		{ variableId: 'wipe3_style', name: 'WIPE3 style value' },
		{ variableId: 'wipe3_style_label', name: 'WIPE3 style (label)' },
		{ variableId: 'wipe4_style', name: 'WIPE4 style value' },
		{ variableId: 'wipe4_style_label', name: 'WIPE4 style (label)' },
		{ variableId: 'speed_mode', name: 'SPEED mode (1-2)' },
		{ variableId: 'ftb_state', name: 'FTB state (OFF/ON)' },
		{ variableId: 'freeze_state', name: 'Freeze state (OFF/ON)' },
		{ variableId: 'tbar_value', name: 'T-Bar current value (0-500)' },
		// 当前激活的 Key 模块（0x0130，仅 H4K）：0=PIP / 1=Luma / 2=Chroma / 3=DSK
		{ variableId: 'key_type', name: 'Active key module value (0-3, H4K)' },
		{ variableId: 'key_type_label', name: 'Active key module (PIP/LUMA/CHROMA/DSK)' },
		{ variableId: 'last_action', name: 'Last executed action key' },
	])
}

import type { ModuleInstance } from './main.js'
import { combineRgb, CompanionBooleanFeedbackDefinition } from '@companion-module/base'
import { filterByProfile } from './devices/index.js'

export function UpdateFeedbacks(self: ModuleInstance): void {
	const feedbacks: Record<string, CompanionBooleanFeedbackDefinition> = {}
	// N3: option lists follow the active protocol (6 inputs / 4 wipes on 0617, 4 / 3 on H4K)
	const family = self.getProtocolFamilyInfo()
	const sourceChoices = (prefix: 'PGM' | 'PVW'): Array<{ id: number; label: string }> => [
		...Array.from({ length: family.inputCount }, (_, i) => ({ id: i + 1, label: `${prefix}${i + 1}` })),
		{ id: 0xf0, label: 'Pattern1' },
		{ id: 0xf1, label: 'Pattern2' },
	]

	// Connection status (active while offline -> grey)
	feedbacks['connection_status'] = {
		name: 'Device Disconnected (Grey when offline)',
		description: 'Active while the switcher is not responding (disconnected / connecting)',
		type: 'boolean',
		defaultStyle: {
			bgcolor: combineRgb(128, 128, 128),
			color: combineRgb(255, 255, 255),
		},
		options: [],
		callback: () => {
			return !self.getDeviceConnectionStatus()
		},
	}

	// Current PGM source -> red button
	feedbacks['pgm_active'] = {
		name: 'PGM Source Active (Red)',
		type: 'boolean',
		defaultStyle: {
			bgcolor: combineRgb(204, 0, 0),
			color: combineRgb(255, 255, 255),
		},
		options: [
			{
				id: 'source',
				type: 'dropdown',
				label: 'Source',
				choices: sourceChoices('PGM'),
				default: 1,
			},
		],
		callback: (feedback) => {
			const state = self.getDeviceState()
			return state.pgmSource === Number((feedback.options as Record<string, unknown>).source)
		},
	}

	// Current PVW source -> green button
	feedbacks['pvw_active'] = {
		name: 'PVW Source Active (Green)',
		type: 'boolean',
		defaultStyle: {
			bgcolor: combineRgb(0, 153, 0),
			color: combineRgb(255, 255, 255),
		},
		options: [
			{
				id: 'source',
				type: 'dropdown',
				label: 'Source',
				choices: sourceChoices('PVW'),
				default: 1,
			},
		],
		callback: (feedback) => {
			const state = self.getDeviceState()
			return state.pvwSource === Number((feedback.options as Record<string, unknown>).source)
		},
	}

	// AUTO / FTB / MUTE active state
	feedbacks['auto_active'] = {
		name: 'Auto Active',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(204, 0, 0), color: combineRgb(255, 255, 255) },
		options: [],
		callback: () => self.getDeviceState().autoActive,
	}
	feedbacks['ftb_active'] = {
		name: 'FTB Active (Red blink)',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(204, 0, 0), color: combineRgb(255, 255, 255) },
		options: [],
		callback: () => {
			const s = self.getDeviceState()
			return s.ftbActive && s.blinkOn
		},
	}
	feedbacks['mute_active'] = {
		name: 'Mute Active (Red blink)',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(204, 0, 0), color: combineRgb(255, 255, 255) },
		options: [],
		callback: () => {
			const s = self.getDeviceState()
			return s.muteActive && s.blinkOn
		},
	}

	// Freeze active (red blinking)
	feedbacks['freeze_active'] = {
		name: 'Freeze Active (Red blink)',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(204, 0, 0), color: combineRgb(255, 255, 255) },
		options: [],
		callback: () => {
			const s = self.getDeviceState()
			return s.freezeActive && s.blinkOn
		},
	}

	// Current WIPE mode (green): 1~4=WIPE1~4 / 5=MIX / 6=DIP
	feedbacks['wipe_active'] = {
		name: 'WIPE Mode Active (Green)',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(0, 153, 0), color: combineRgb(255, 255, 255) },
		options: [
			{
				id: 'mode',
				type: 'dropdown',
				label: 'Wipe Mode',
				choices: [
					...Array.from({ length: family.wipeCount }, (_, i) => ({ id: i + 1, label: `WIPE${i + 1}` })),
					{ id: 5, label: 'MIX' },
					{ id: 6, label: 'DIP' },
				],
				default: 1,
			},
		],
		callback: (feedback) => {
			return self.getDeviceState().wipeMode === Number((feedback.options as Record<string, unknown>).mode)
		},
	}

	// Per-wipe style (read back from 0x0120) -> green when the wipe currently uses that style
	feedbacks['wipe_style_active'] = {
		name: 'WIPE Style Active (Green)',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(0, 153, 0), color: combineRgb(255, 255, 255) },
		options: [
			{
				id: 'wipe',
				type: 'dropdown',
				label: 'Wipe',
				choices: Array.from({ length: family.wipeCount }, (_, i) => ({ id: i + 1, label: `WIPE${i + 1}` })),
				default: 1,
			},
			{
				id: 'style',
				type: 'dropdown',
				label: 'Style',
				choices: family.wipeStyles,
				default: family.wipeStyles[0]?.id ?? 0,
			},
		],
		callback: (feedback) => {
			const o = feedback.options as Record<string, unknown>
			const vals = self.getTransitionReport()
			return (vals[Number(o.wipe) - 1] ?? -1) === Number(o.style)
		},
	}

	// Stream 1~3 switches (Codec 0x01A0: STREAM_1/2/3_EN, fields 9/10/11) -> yellow on white
	feedbacks['stream_active'] = {
		name: 'Stream Active (Yellow)',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(255, 200, 0), color: combineRgb(255, 255, 255) },
		options: [
			{
				id: 'stream',
				type: 'dropdown',
				label: 'Stream',
				choices: [
					{ id: 1, label: 'Stream 1' },
					{ id: 2, label: 'Stream 2' },
					{ id: 3, label: 'Stream 3' },
				],
				default: 1,
			},
		],
		callback: (feedback) => {
			const n = Number((feedback.options as Record<string, unknown>).stream)
			return (self.getReportState('codec')[self.getReportFieldIndex('codec', 'Stream' + n + 'Enable')] ?? 0) === 1
		},
	}

	// Status feedback: PIP/LUMA/CHROMA/DSK/LOGO STATUS (0:OFF/1:KEY/2:ON AIR/3:KEY&ON AIR)
	// Green by default; the ON AIR preset overrides it to red on white.
	// H4K: a non-OFF state must also be the currently selected key layer (0x0130), otherwise
	// PIP/LUMA/CHROMA would all light up together; only the layer selected on the panel lights.
	const keyTypeOf: Record<string, number> = { pip1: 0, pip2: 0, pip3: 0, luma: 1, chroma: 2, dsk: 3 }
	// Map internal ids to readable names, avoiding entries like "pip1_status_active (Green/Red)"
	const statusFbLabels: Record<string, string> = {
		pip1: 'PIP1 Status',
		pip2: 'PIP2 Status',
		pip3: 'PIP3 Status',
		luma: 'LUMA Key Status',
		chroma: 'CHROMA Key Status',
		dsk: 'DSK Key Status',
		logo: 'LOGO Status',
	}
	const statusFb = (id: string, cmdKey: string, fieldName: string): void => {
		feedbacks[id] = {
			name: `${statusFbLabels[id] ?? id} (Green/Red)`,
			description: 'Active when the module status equals the selected value',
			type: 'boolean',
			defaultStyle: { bgcolor: combineRgb(0, 153, 0), color: combineRgb(255, 255, 255) },
			options: [
				{
					id: 'status',
					type: 'dropdown',
					label: 'Status',
					choices: [
						{ id: 0, label: 'OFF' },
						{ id: 1, label: 'KEY' },
						{ id: 2, label: 'ON AIR' },
						{ id: 3, label: 'KEY&ON AIR' },
					],
					default: 1,
				},
			],
			callback: (feedback) => {
				const want = Number((feedback.options as Record<string, unknown>).status)
				const actual = self.getReportState(cmdKey)[self.getReportFieldIndex(cmdKey, fieldName)] ?? -1
				if (actual !== want) return false
				// OFF only checks Status; a non-OFF state on H4K must also be the active key layer
				if (want === 0) return true
				if (!self.getProtocolCommands()['keyType']) return true
				const expect = keyTypeOf[cmdKey]
				if (expect === undefined) return true
				const current = self.getDeviceState().keyType
				// Before the first 0x0130 reply (-1) do not filter, keeping the previous behaviour
				if (typeof current !== 'number' || current < 0) return true
				return current === expect
			},
		}
	}
	statusFb('pip1_status_active', 'pip1', 'Status')
	statusFb('pip2_status_active', 'pip2', 'Status')
	statusFb('pip3_status_active', 'pip3', 'Status')
	statusFb('luma_status_active', 'luma', 'Status')
	statusFb('chroma_status_active', 'chroma', 'Status')
	statusFb('dsk_status_active', 'dsk', 'Status')
	statusFb('logo_status_active', 'logo', 'Status')

	// Currently active key module (0x0130, H4K only): PIP / Luma / Chroma / DSK highlight exclusively.
	// Whichever key layer is selected on the panel lights up - clearer than each Status field.
	if (self.getProtocolCommands()['keyType']) {
		feedbacks['key_type_active'] = {
			name: 'Key Module Selected (PIP/Luma/Chroma/DSK)',
			description: 'Active key module (read back from 0x0130, H4K only)',
			type: 'boolean',
			defaultStyle: { bgcolor: combineRgb(0, 153, 0), color: combineRgb(255, 255, 255) },
			options: [
				{
					type: 'dropdown',
					id: 'type',
					label: 'Key Type',
					choices: [
						{ id: 0, label: 'PIP' },
						{ id: 1, label: 'LUMA' },
						{ id: 2, label: 'CHROMA' },
						{ id: 3, label: 'DSK' },
					],
					default: 0,
				},
			],
			callback: (feedback) =>
				self.getDeviceState().keyType === Number((feedback.options as Record<string, unknown>).type),
		}
	}

	// Action flash: lights briefly when the last executed action key matches (orange on black)
	// Key format: key=key:<Key_val> (e.g. key:5); protocol set=set:<cmdKey>:<field> (e.g. set:luma:1); T-Bar=tbar
	feedbacks['last_action'] = {
		name: 'Last Action (Flash)',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(255, 140, 0), color: combineRgb(0, 0, 0) },
		options: [
			{
				id: 'key',
				type: 'textinput',
				label: 'Action key (e.g. set_source|source=5, or key:19 for FTB / key:20 for MUTE / key:33 for Freeze)',
				default: '',
				useVariables: true,
			},
		],
		callback: async (feedback, context) => {
			// N2: the option offers variables, so resolve them before comparing
			const key = await context.parseVariablesInString(String(feedback.options.key ?? ''))
			return key !== '' && self.getDeviceState().lastAction === key
		},
	}

	// Filter feedback definitions by the current product profile
	self.setFeedbackDefinitions(filterByProfile(feedbacks, self.getDeviceProfile()))
}

import type { ModuleInstance } from './main.js'
import { combineRgb, CompanionBooleanFeedbackDefinition } from '@companion-module/base'

export function UpdateFeedbacks(self: ModuleInstance): void {
	const feedbacks: Record<string, CompanionBooleanFeedbackDefinition> = {}

	// 连接状态（未连接时激活 → 灰）
	feedbacks['connection_status'] = {
		name: 'Connection Status',
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

	// PGM 当前源 → 红色按钮
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
				choices: [
					{ id: 1, label: 'PGM1' },
					{ id: 2, label: 'PGM2' },
					{ id: 3, label: 'PGM3' },
					{ id: 4, label: 'PGM4' },
					{ id: 5, label: 'PGM5' },
					{ id: 6, label: 'PGM6' },
					{ id: 0xf0, label: 'Pattern1' },
					{ id: 0xf1, label: 'Pattern2' },
				],
				default: 1,
			},
		],
		callback: (feedback) => {
			const state = self.getDeviceState()
			return state.pgmSource === Number((feedback.options as Record<string, unknown>).source)
		},
	}

	// PVW 当前源 → 绿色按钮
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
				choices: [
					{ id: 1, label: 'PVW1' },
					{ id: 2, label: 'PVW2' },
					{ id: 3, label: 'PVW3' },
					{ id: 4, label: 'PVW4' },
					{ id: 5, label: 'PVW5' },
					{ id: 6, label: 'PVW6' },
					{ id: 0xf0, label: 'Pattern1' },
					{ id: 0xf1, label: 'Pattern2' },
				],
				default: 1,
			},
		],
		callback: (feedback) => {
			const state = self.getDeviceState()
			return state.pvwSource === Number((feedback.options as Record<string, unknown>).source)
		},
	}

	// AUTO / FTB / MUTE 激活态
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

	// Freeze 激活（红底闪烁）
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

	// WIPE 当前模式（绿）：1~4=WIPE1~4 / 5=MIX / 6=DIP
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
					{ id: 1, label: 'WIPE1' },
					{ id: 2, label: 'WIPE2' },
					{ id: 3, label: 'WIPE3' },
					{ id: 4, label: 'WIPE4' },
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

	// Stream 1~3 开关（Codec 0x01A0：STREAM_1/2/3_EN，字段 9/10/11）→ 黄底白字
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
			return (self.getReportState('codec')[8 + n] ?? 0) === 1
		},
	}

	// 状态反馈：PIP/LUMA/CHROMA/DSK/LOGO 的 STATUS（0:OFF/1:KEY/2:ON AIR/3:KEY&ON AIR）
	// 默认绿底白字；预设里 ON AIR 按钮会覆盖为红底白字
	const statusFb = (id: string, cmdKey: string, fieldIndex: number): void => {
		feedbacks[id] = {
			name: `${id} (Green/Red)`,
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
			callback: (feedback) =>
				(self.getReportState(cmdKey)[fieldIndex] ?? -1) ===
				Number((feedback.options as Record<string, unknown>).status),
		}
	}
	statusFb('pip1_status_active', 'pip1', 0)
	statusFb('pip2_status_active', 'pip2', 0)
	statusFb('pip3_status_active', 'pip3', 0)
	statusFb('luma_status_active', 'luma', 1)
	statusFb('chroma_status_active', 'chroma', 0)
	statusFb('dsk_status_active', 'dsk', 1)
	statusFb('logo_status_active', 'logo', 0)

	// 执行闪烁：最近执行的 action key 命中时短暂亮起（橙底黑字）
	// key 约定：按键=key:<Key_val>（如 key:5）；协议设置=set:<cmdKey>:<field>（如 set:luma:1）；推杆=tbar
	feedbacks['last_action'] = {
		name: 'Last Action (Flash)',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(255, 140, 0), color: combineRgb(0, 0, 0) },
		options: [
			{
				id: 'key',
				type: 'textinput',
				label: 'Action key (e.g. key:5 / set:luma:1 / tbar)',
				default: '',
				useVariables: true,
			},
		],
		callback: (feedback) => {
			const key = String((feedback.options as unknown as Record<string, string>).key ?? '')
			return key !== '' && self.getDeviceState().lastAction === key
		},
	}

	self.setFeedbackDefinitions(feedbacks)
}

import type { ModuleInstance } from './main.js'
import { combineRgb, CompanionBooleanFeedbackDefinition } from '@companion-module/base'
import { filterByProfile } from './devices/index.js'

export function UpdateFeedbacks(self: ModuleInstance): void {
	const feedbacks: Record<string, CompanionBooleanFeedbackDefinition> = {}

	// 连接状态（未连接时激活 → 灰）
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

	// 各 Wipe 通道的样式（0x0120 回读）→ 绿：高亮“该 Wipe 当前就是这个样式”
	const wipeFamily = self.getProtocolFamilyInfo()
	feedbacks['wipe_style_active'] = {
		name: 'WIPE Style Active (Green)',
		type: 'boolean',
		defaultStyle: { bgcolor: combineRgb(0, 153, 0), color: combineRgb(255, 255, 255) },
		options: [
			{
				id: 'wipe',
				type: 'dropdown',
				label: 'Wipe',
				choices: Array.from({ length: wipeFamily.wipeCount }, (_, i) => ({ id: i + 1, label: `WIPE${i + 1}` })),
				default: 1,
			},
			{
				id: 'style',
				type: 'dropdown',
				label: 'Style',
				choices: wipeFamily.wipeStyles,
				default: wipeFamily.wipeStyles[0]?.id ?? 0,
			},
		],
		callback: (feedback) => {
			const o = feedback.options as Record<string, unknown>
			const vals = self.getTransitionReport()
			return (vals[Number(o.wipe) - 1] ?? -1) === Number(o.style)
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
			return (self.getReportState('codec')[self.getReportFieldIndex('codec', 'Stream' + n + 'Enable')] ?? 0) === 1
		},
	}

	// 状态反馈：PIP/LUMA/CHROMA/DSK/LOGO 的 STATUS（0:OFF/1:KEY/2:ON AIR/3:KEY&ON AIR）
	// 默认绿底白字；预设里 ON AIR 按钮会覆盖为红底白字
	// H4K：非 OFF 状态还要叠加“当前激活的 Key 层”（0x0130），否则 PIP/LUMA/CHROMA 都开着时
	// 三个按钮会一起变绿——只有当前面板选中的那一层才点亮。
	const keyTypeOf: Record<string, number> = { pip1: 0, pip2: 0, pip3: 0, luma: 1, chroma: 2, dsk: 3 }
	// 将内部 id 映射为可读名称，避免反馈列表中“pip1_status_active (Green/Red)”这种不友好的展示
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
				// OFF 只看 Status；非 OFF 在 H4K 上还必须是当前激活的 Key 层
				if (want === 0) return true
				if (!self.getProtocolCommands()['keyType']) return true
				const expect = keyTypeOf[cmdKey]
				if (expect === undefined) return true
				const current = self.getDeviceState().keyType
				// 还没收到 0x0130 回读时（-1）不过滤，保持旧行为
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

	// 当前激活的 Key 模块（0x0130，仅 H4K）：PIP / Luma / Chroma / DSK 互斥高亮
	// 面板上选中哪个 Key 层，对应按钮就亮——比各自的 Status 字段更直观
	if (self.getProtocolCommands()['keyType']) {
		feedbacks['key_type_active'] = {
			name: 'Key Module Selected (PIP/Luma/Chroma/DSK)',
			description: '当前激活的 Key 模块（0x0130 回读，仅 H4K）',
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
				label: 'Action key (e.g. set_source|source=5, or key:19 for FTB / key:20 for MUTE / key:33 for Freeze)',
				default: '',
				useVariables: true,
			},
		],
		callback: (feedback) => {
			const key = String((feedback.options as unknown as Record<string, string>).key ?? '')
			return key !== '' && self.getDeviceState().lastAction === key
		},
	}

	// 按当前产品档案裁剪反馈定义
	self.setFeedbackDefinitions(filterByProfile(feedbacks, self.getDeviceProfile()))
}

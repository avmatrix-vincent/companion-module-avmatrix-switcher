import type { ModuleInstance } from './main.js'
import { CompanionPresetDefinitions, CompanionButtonPresetDefinition, combineRgb } from '@companion-module/base'
import {
	PGM_KEY_VALUES,
	PVW_KEY_VALUES,
	PATTERN_KEY_VALUES,
	TRANSITION_KEY_VALUES,
	FUNCTION_KEY_VALUES,
	flashKeyFor,
} from './commandHandler.js'

// 底色黑：仅“当前源”命中 pgm_active/pvw_active 反馈时才变红/绿（未收到状态时全为黑）
const PGM_BG = combineRgb(0, 0, 0)
const PVW_BG = combineRgb(0, 0, 0)
const DARK = combineRgb(0, 0, 0)
const WHITE = combineRgb(255, 255, 255)

// 分组名用“零宽空格”前缀控序（不可见，不显示序号）；
// Companion 1.x 按分组名字符串排序，前缀数量递增即可控制先后。
const ZW = '\u200b'
const CAT_PGM = `${ZW}PGM`
const CAT_PVW = `${ZW}${ZW}PVW`
const CAT_SWITCH = `${ZW}${ZW}${ZW}Switch or Streams`
const catPip = (n: number): string => `${ZW.repeat(3 + n)}PIP${n}`
const CAT_LUMA = `${ZW.repeat(7)}LUMA KEY`
const CAT_CHROMA = `${ZW.repeat(8)}CHROMA KEY`
const CAT_DSK = `${ZW.repeat(9)}DSK KEY`
const CAT_LOGO = `${ZW.repeat(10)}LOGO KEY`
const CAT_TRANS = `${ZW.repeat(11)}TRANSITIONS`
const CAT_AUDIO = `${ZW.repeat(12)}Audio Setting`
const CAT_TBAR = `${ZW.repeat(13)}TBAR`

// 反馈样式：必须随 preset 的 feedback 条目一起提供（CompanionPresetFeedback.style），否则按钮不会应用该样式
const STYLE_RED = { bgcolor: combineRgb(204, 0, 0), color: combineRgb(255, 255, 255) }
const STYLE_GREEN = { bgcolor: combineRgb(0, 153, 0), color: combineRgb(255, 255, 255) }
const STYLE_YELLOW = { bgcolor: combineRgb(255, 200, 0), color: combineRgb(255, 255, 255) }
const STYLE_GREY = { bgcolor: combineRgb(80, 80, 80), color: combineRgb(255, 255, 255) }
const STYLE_FLASH = { bgcolor: combineRgb(255, 140, 0), color: combineRgb(0, 0, 0) }

/** 生成一个按钮 preset */
function buttonPreset(
	category: string,
	name: string,
	text: string,
	actionId: string,
	actionOptions: Record<string, number>,
	feedback?: { feedbackId: string; options: Record<string, number>; style?: Record<string, number> },
	bgcolor: number = DARK,
	flashKey?: string
): CompanionButtonPresetDefinition {
	const fbs: Array<{
		feedbackId: string
		options: Record<string, number | string>
		style?: Record<string, number>
	}> = []
	if (feedback) fbs.push(feedback)
	if (flashKey) fbs.push({ feedbackId: 'last_action', options: { key: flashKeyFor(flashKey, actionOptions) }, style: STYLE_FLASH })
	return {
		type: 'button',
		category,
		name,
		style: {
			text,
			size: '14',
			color: WHITE,
			bgcolor,
			show_topbar: false,
		},
		steps: [{ down: [{ actionId, options: actionOptions }], up: [] }],
		feedbacks: fbs,
	}
}

/**
 * Presets：菜单树结构（category 即树节点）
 *   PGM/PVW : 源 1~6 + PATTERN1/2（当前源 → 红/绿）
 *   Switch or Streams : Stream1~3 + CUT/AUTO/FTB/MUTE
 *   PIP1~3 / LUMA / CHROMA / DSK / LOGO : 状态四键（KEY/ON AIR/KEY&ON AIR/OFF）
 *   TRANSITIONS : WIPE1~4 / MIX / DIP / NORMAL / INV / FLIP-FLOP
 */
export function UpdatePresets(self: ModuleInstance): void {
	const presets: CompanionPresetDefinitions = {}

	// ===== PGM 组（当前源 → 红色） =====
	for (const [label, keyVal] of Object.entries(PGM_KEY_VALUES)) {
		presets[`pgm_${label.toLowerCase()}`] = buttonPreset(
			CAT_PGM,
			label,
			label,
			'set_source',
			{ source: keyVal },
			{ feedbackId: 'pgm_active', options: { source: keyVal }, style: STYLE_RED },
			PGM_BG
		)
	}
	for (const [label, keyVal] of Object.entries(PATTERN_KEY_VALUES)) {
		if (!label.startsWith('PGM_')) continue
		const displayLabel = label.replace('PGM_PATTERN', 'PATTERN')
		const disp = label.includes('1') ? 0xf0 : 0xf1
		presets[`pgm_${label.toLowerCase()}`] = buttonPreset(
			CAT_PGM,
			displayLabel,
			displayLabel,
			'set_source',
			{ source: keyVal },
			{ feedbackId: 'pgm_active', options: { source: disp }, style: STYLE_RED },
			PGM_BG
		)
	}

	// ===== PVW 组（当前源 → 绿色） =====
	for (const [label, keyVal] of Object.entries(PVW_KEY_VALUES)) {
		const sourceVal = keyVal - 8
		presets[`pvw_${label.toLowerCase()}`] = buttonPreset(
			CAT_PVW,
			label,
			label,
			'set_source',
			{ source: keyVal },
			{ feedbackId: 'pvw_active', options: { source: sourceVal }, style: STYLE_GREEN },
			PVW_BG
		)
	}
	for (const [label, keyVal] of Object.entries(PATTERN_KEY_VALUES)) {
		if (!label.startsWith('PVW_')) continue
		const displayLabel = label.replace('PVW_PATTERN', 'PATTERN')
		const disp = label.includes('1') ? 0xf0 : 0xf1
		presets[`pvw_${label.toLowerCase()}`] = buttonPreset(
			CAT_PVW,
			displayLabel,
			displayLabel,
			'set_source',
			{ source: keyVal },
			{ feedbackId: 'pvw_active', options: { source: disp }, style: STYLE_GREEN },
			PVW_BG
		)
	}

	// ===== Switch 组（Stream 1/2/3 + CUT/AUTO/FTB/MUTE） =====
	const switchButtons: Array<{
		id: string
		label: string
		actionId: string
		value: number
		fbId?: string
		fbOpts?: Record<string, number>
		fbStyle?: Record<string, number>
	}> = [
		{ id: 'stream1', label: 'Stream 1', actionId: 'switch_stream', value: FUNCTION_KEY_VALUES.STREAM1, fbId: 'stream_active', fbOpts: { stream: 1 }, fbStyle: STYLE_YELLOW },
		{ id: 'stream2', label: 'Stream 2', actionId: 'switch_stream', value: FUNCTION_KEY_VALUES.STREAM2, fbId: 'stream_active', fbOpts: { stream: 2 }, fbStyle: STYLE_YELLOW },
		{ id: 'stream3', label: 'Stream 3', actionId: 'switch_stream', value: FUNCTION_KEY_VALUES.STREAM3, fbId: 'stream_active', fbOpts: { stream: 3 }, fbStyle: STYLE_YELLOW },
		{ id: 'cut', label: 'CUT', actionId: 'switch_transition', value: TRANSITION_KEY_VALUES.CUT },
		{ id: 'auto', label: 'AUTO', actionId: 'switch_transition', value: TRANSITION_KEY_VALUES.AUTO, fbId: 'auto_active', fbOpts: {}, fbStyle: STYLE_RED },
		{ id: 'ftb', label: 'FTB', actionId: 'switch_transition', value: TRANSITION_KEY_VALUES.FTB, fbId: 'ftb_active', fbOpts: {}, fbStyle: STYLE_RED },
		{ id: 'mute', label: 'MUTE', actionId: 'switch_transition', value: FUNCTION_KEY_VALUES.MUTE, fbId: 'mute_active', fbOpts: {}, fbStyle: STYLE_RED },
	]
	for (const b of switchButtons) {
		presets[`switch_${b.id}`] = buttonPreset(
			CAT_SWITCH,
			b.label,
			b.label,
			b.actionId,
			{ value: b.value },
			b.fbId ? { feedbackId: b.fbId, options: b.fbOpts ?? {}, style: b.fbStyle ?? STYLE_RED } : undefined,
			DARK,
			b.actionId
		)
	}

	// ===== 状态四键（KEY / ON AIR / KEY&ON AIR / OFF）—— PIP/LUMA/CHROMA/DSK/LOGO 通用 =====
	const statusGroup = (category: string, tag: string, actionId: string, prefix: string, fbId: string): void => {
		const rows: Array<[string, string, number, Record<string, number>]> = [
			[`${prefix}_key`, 'KEY', 1, STYLE_GREEN],
			[`${prefix}_onair`, 'ON AIR', 2, STYLE_RED],
			[`${prefix}_keyonair`, 'KEY&ON AIR', 3, STYLE_GREEN],
			[`${prefix}_off`, 'OFF', 0, STYLE_GREY],
		]
		for (const [id, label, status, style] of rows) {
			presets[id] = buttonPreset(
				category,
				`${tag} ${label}`,
				`[${tag}]\n——\n${label}`,
				actionId,
				{ status },
				{ feedbackId: fbId, options: { status }, style }
			)
		}
	}

	// PIP1 / PIP2 / PIP3（状态四键 + Adjust）
	statusGroup(catPip(1), 'PIP1', 'pip1_status', 'pip1', 'pip1_status_active')
	presets['pip1_adjust'] = buttonPreset(catPip(1), 'PIP1 Adjust', '[PIP1]\n——\nADJUST', 'pip1_adjust', { source: 1, size: 100, posx: 50, posy: 50 })
	statusGroup(catPip(2), 'PIP2', 'pip2_status', 'pip2', 'pip2_status_active')
	presets['pip2_adjust'] = buttonPreset(catPip(2), 'PIP2 Adjust', '[PIP2]\n——\nADJUST', 'pip2_adjust', { source: 1, size: 100, posx: 50, posy: 50 })
	statusGroup(catPip(3), 'PIP3', 'pip3_status', 'pip3', 'pip3_status_active')
	presets['pip3_adjust'] = buttonPreset(catPip(3), 'PIP3 Adjust', '[PIP3]\n——\nADJUST', 'pip3_adjust', { source: 1, size: 100, posx: 50, posy: 50 })

	// LUMA / CHROMA / DSK / LOGO（状态四键；各自另加 Adjust）
	statusGroup(CAT_LUMA, 'LUMA', 'luma_status', 'luma', 'luma_status_active')
	presets['luma_adjust'] = buttonPreset(CAT_LUMA, 'LUMA Adjust', '[LUMA]\n——\nADJUST', 'luma_adjust', { size: 100, posx: 50, posy: 50, clip: 50, gain: 50 })
	statusGroup(CAT_CHROMA, 'CHROMA', 'chroma_status', 'chroma', 'chroma_status_active')
	presets['chroma_adjust'] = buttonPreset(CAT_CHROMA, 'CHROMA Adjust', '[CHROMA]\n——\nADJUST', 'chroma_adjust', { size: 100, posx: 50, posy: 50, similarity: 50, smooth: 0, spill: 0, opacity: 100, brightness: 50, contrast: 50, saturation: 50 })
	statusGroup(CAT_DSK, 'DSK', 'dsk_status', 'dsk', 'dsk_status_active')
	presets['dsk_adjust'] = buttonPreset(CAT_DSK, 'DSK Adjust', '[DSK]\n——\nADJUST', 'dsk_adjust', { clip: 50, gain: 50 })
	statusGroup(CAT_LOGO, 'LOGO', 'logo_status', 'logo', 'logo_status_active')
	presets['logo_adjust'] = buttonPreset(CAT_LOGO, 'LOGO Adjust', '[LOGO]\n——\nADJUST', 'logo_adjust', { posx: 50, posy: 50, size: 10, opacity: 100 })

	// ===== TRANSITIONS 组（WIPE1~4 / MIX / DIP / NORMAL / INV / FLIP-FLOP） =====
	const transButtons: Array<{
		id: string
		text: string
		name: string
		actionId: string
		opts: Record<string, number>
		fbId?: string
		fbOpts?: Record<string, number>
		flashKey: string
	}> = [
		{ id: 'trans_wipe1', text: '[TRANS]\n——\nWIPE1', name: 'TRANS WIPE1', actionId: 'trans_wipe1', opts: { style: 0 }, fbId: 'wipe_active', fbOpts: { mode: 1 }, flashKey: 'key:27' },
		{ id: 'trans_wipe2', text: '[TRANS]\n——\nWIPE2', name: 'TRANS WIPE2', actionId: 'trans_wipe2', opts: { style: 0 }, fbId: 'wipe_active', fbOpts: { mode: 2 }, flashKey: 'key:28' },
		{ id: 'trans_wipe3', text: '[TRANS]\n——\nWIPE3', name: 'TRANS WIPE3', actionId: 'trans_wipe3', opts: { style: 0 }, fbId: 'wipe_active', fbOpts: { mode: 3 }, flashKey: 'key:29' },
		{ id: 'trans_wipe4', text: '[TRANS]\n——\nWIPE4', name: 'TRANS WIPE4', actionId: 'trans_wipe4', opts: { style: 0 }, fbId: 'wipe_active', fbOpts: { mode: 4 }, flashKey: 'key:30' },
		{ id: 'trans_mix', text: '[TRANS]\n——\nMIX', name: 'TRANS MIX', actionId: 'trans_effect', opts: { value: TRANSITION_KEY_VALUES['MIX'] }, fbId: 'wipe_active', fbOpts: { mode: 5 }, flashKey: 'key:31' },
		{ id: 'trans_dip', text: '[TRANS]\n——\nDIP', name: 'TRANS DIP', actionId: 'trans_effect', opts: { value: TRANSITION_KEY_VALUES['DIP'] }, fbId: 'wipe_active', fbOpts: { mode: 6 }, flashKey: 'key:32' },
		{ id: 'trans_freeze', text: '[TRANS]\n——\nFREEZE', name: 'TRANS FREEZE', actionId: 'trans_effect', opts: { value: TRANSITION_KEY_VALUES['FREEZE'] }, fbId: 'freeze_active', fbOpts: {}, flashKey: 'key:33' },
		{ id: 'trans_normal', text: '[TRANS]\n——\nNORMAL', name: 'TRANS NORMAL', actionId: 'trans_direction', opts: { value: 0 }, flashKey: 'set:transition' },
		{ id: 'trans_inv', text: '[TRANS]\n——\nINV', name: 'TRANS INV', actionId: 'trans_direction', opts: { value: 1 }, flashKey: 'set:transition' },
		{ id: 'trans_flipflop', text: '[TRANS]\n——\nFLIP-FLOP', name: 'TRANS FLIP-FLOP', actionId: 'trans_direction', opts: { value: 2 }, flashKey: 'set:transition' },
	]
	for (const b of transButtons) {
		presets[b.id] = buttonPreset(
			CAT_TRANS,
			b.name,
			b.text,
			b.actionId,
			b.opts,
			b.fbId ? { feedbackId: b.fbId, options: b.fbOpts ?? {}, style: b.fbId === 'freeze_active' ? STYLE_RED : STYLE_GREEN } : undefined,
			DARK,
			b.actionId
		)
	}

	// ===== Audio Setting 组（每个按钮只控制一个功能） =====
	// 无通道的单键 / 单开关 / 单滑块
	const audioSimple: Array<{ id: string; text: string; name: string; actionId: string; opts: Record<string, number> }> = [
		{ id: 'audio_all_afv', text: '[AFV]\nAll AFV', name: 'Audio All AFV', actionId: 'audio_all_afv', opts: { value: 0 } },
		{ id: 'audio_reset', text: '[AUDIO]\nRESET', name: 'Audio Reset', actionId: 'audio_reset', opts: {} },
		{ id: 'audio_master_en', text: '[PGM OUT]\nENABLE', name: 'PGM OUT Enable', actionId: 'audio_master_en', opts: { value: 1 } },
		{ id: 'audio_master_vol', text: '[PGM OUT]\nVOLUME', name: 'PGM OUT Volume', actionId: 'audio_master_vol', opts: { value: 50 } },
		{ id: 'audio_ear_en', text: '[EAR]\nENABLE', name: 'Earphone Enable', actionId: 'audio_ear_en', opts: { value: 1 } },
		{ id: 'audio_ear_vol', text: '[EAR]\nVOLUME', name: 'Earphone Volume', actionId: 'audio_ear_vol', opts: { value: 50 } },
		{ id: 'audio_ear_src', text: '[EAR]\nSOURCE', name: 'Earphone Source', actionId: 'audio_ear_src', opts: { value: 0 } },
		{ id: 'audio_line_en', text: '[LINE IN]\nENABLE', name: 'Line In Enable', actionId: 'audio_line_en', opts: { value: 1 } },
		{ id: 'audio_line_vol', text: '[LINE IN]\nVOLUME', name: 'Line In Volume', actionId: 'audio_line_vol', opts: { value: 50 } },
		{ id: 'audio_line_delay', text: '[LINE IN]\nDELAY', name: 'Line In Delay', actionId: 'audio_line_delay', opts: { value: 0 } },
		{ id: 'audio_xlr_en', text: '[XLR]\nENABLE', name: 'XLR Enable', actionId: 'audio_xlr_en', opts: { value: 1 } },
		{ id: 'audio_xlr_vol', text: '[XLR]\nVOLUME', name: 'XLR Volume', actionId: 'audio_xlr_vol', opts: { value: 50 } },
		{ id: 'audio_xlr_delay', text: '[XLR]\nDELAY', name: 'XLR Delay', actionId: 'audio_xlr_delay', opts: { value: 0 } },
		{ id: 'audio_mic_xlr_mode', text: '[MIC/XLR]\nMODE', name: 'MIC/XLR Mode', actionId: 'audio_mic_xlr_mode', opts: { value: 0 } },
	]
	for (const b of audioSimple) {
		presets[b.id] = buttonPreset(CAT_AUDIO, b.name, b.text, b.actionId, b.opts, undefined, DARK, b.actionId)
	}

	// IN1~6 × (ENABLE / VOLUME / AFV / DELAY)
	for (const n of [1, 2, 3, 4, 5, 6]) {
		presets[`audio_in${n}_en`] = buttonPreset(CAT_AUDIO, `IN${n} Enable`, `[IN${n}]\nENABLE`, 'audio_in_en', { channel: n, value: 1 }, undefined, DARK, 'audio_in_en')
		presets[`audio_in${n}_vol`] = buttonPreset(CAT_AUDIO, `IN${n} Volume`, `[IN${n}]\nVOLUME`, 'audio_in_vol', { channel: n, value: 50 }, undefined, DARK, 'audio_in_vol')
		presets[`audio_in${n}_afv`] = buttonPreset(CAT_AUDIO, `IN${n} AFV`, `[IN${n}]\nAFV`, 'audio_in_afv', { channel: n, value: 0 }, undefined, DARK, 'audio_in_afv')
		presets[`audio_in${n}_delay`] = buttonPreset(CAT_AUDIO, `IN${n} Delay`, `[IN${n}]\nDELAY`, 'audio_in_delay', { channel: n, value: 0 }, undefined, DARK, 'audio_in_delay')
	}

	// MIC1~2 × (ENABLE / GUITAR / PRE-GAIN / VOLUME / DELAY)
	for (const n of [1, 2]) {
		presets[`audio_mic${n}_en`] = buttonPreset(CAT_AUDIO, `MIC${n} Enable`, `[MIC${n}]\nENABLE`, 'audio_mic_en', { channel: n, value: 1 }, undefined, DARK, 'audio_mic_en')
		presets[`audio_mic${n}_guitar`] = buttonPreset(CAT_AUDIO, `MIC${n} Guitar`, `[MIC${n}]\nGUITAR`, 'audio_mic_guitar', { channel: n, value: 0 }, undefined, DARK, 'audio_mic_guitar')
		presets[`audio_mic${n}_pregate`] = buttonPreset(CAT_AUDIO, `MIC${n} Pre-Gain`, `[MIC${n}]\nPRE-GAIN`, 'audio_mic_pregate', { channel: n, value: 0 }, undefined, DARK, 'audio_mic_pregate')
		presets[`audio_mic${n}_vol`] = buttonPreset(CAT_AUDIO, `MIC${n} Volume`, `[MIC${n}]\nVOLUME`, 'audio_mic_vol', { channel: n, value: 50 }, undefined, DARK, 'audio_mic_vol')
		presets[`audio_mic${n}_delay`] = buttonPreset(CAT_AUDIO, `MIC${n} Delay`, `[MIC${n}]\nDELAY`, 'audio_mic_delay', { channel: n, value: 0 }, undefined, DARK, 'audio_mic_delay')
	}

	// ===== TBAR 组（+ / -） =====
	presets['tbar_up'] = buttonPreset(CAT_TBAR, 'T-Bar +', '+', 'tbar_move', { direction: 1, step: 10 }, undefined, DARK, 'tbar_move')
	presets['tbar_down'] = buttonPreset(CAT_TBAR, 'T-Bar -', '-', 'tbar_move', { direction: 0, step: 10 }, undefined, DARK, 'tbar_move')
	// 只显示当前值（无动作），文本绑定变量 tbar_value
	presets['tbar_display'] = {
		type: 'button',
		category: CAT_TBAR,
		name: 'T-Bar Value',
		style: {
			text: '$(self:tbar_value)',
			size: '14',
			color: WHITE,
			bgcolor: DARK,
			show_topbar: false,
		},
		steps: [{ down: [], up: [] }],
		feedbacks: [],
	}

	self.setPresetDefinitions(presets)
}

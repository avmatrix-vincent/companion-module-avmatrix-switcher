import type { ModuleInstance } from './main.js'
import { CompanionPresetDefinitions, CompanionButtonPresetDefinition, combineRgb } from '@companion-module/base'
import { filterByProfile } from './devices/index.js'
import { flashKeyFor } from './commandHandler.js'

// Black background: a button only turns red/green when its source matches pgm_active/pvw_active (black until state arrives)
const PGM_BG = combineRgb(0, 0, 0)
const PVW_BG = combineRgb(0, 0, 0)
const DARK = combineRgb(0, 0, 0)
const WHITE = combineRgb(255, 255, 255)

// Category names are ordered with zero-width-space prefixes (invisible, no numbers shown);
// Companion 1.x sorts categories as strings, so a longer prefix moves a group later.
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

// Feedback styles must be provided next to the preset feedback entry (CompanionPresetFeedback.style), otherwise the button ignores them
const STYLE_RED = { bgcolor: combineRgb(204, 0, 0), color: combineRgb(255, 255, 255) }
const STYLE_GREEN = { bgcolor: combineRgb(0, 153, 0), color: combineRgb(255, 255, 255) }
const STYLE_YELLOW = { bgcolor: combineRgb(255, 200, 0), color: combineRgb(255, 255, 255) }
const STYLE_GREY = { bgcolor: combineRgb(80, 80, 80), color: combineRgb(255, 255, 255) }
const STYLE_FLASH = { bgcolor: combineRgb(255, 140, 0), color: combineRgb(0, 0, 0) }

/** Build one button preset */
function buttonPreset(
	category: string,
	name: string,
	text: string,
	actionId: string,
	actionOptions: Record<string, number | string>,
	feedback?: { feedbackId: string; options: Record<string, number>; style?: Record<string, number> },
	bgcolor: number = DARK,
	flashKey?: string,
): CompanionButtonPresetDefinition {
	const fbs: Array<{
		feedbackId: string
		options: Record<string, number | string>
		style?: Record<string, number>
	}> = []
	if (feedback) fbs.push(feedback)
	if (flashKey)
		fbs.push({ feedbackId: 'last_action', options: { key: flashKeyFor(flashKey, actionOptions) }, style: STYLE_FLASH })
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
 * Presets: menu tree (the category is the tree node)
 *   PGM/PVW : sources 1~N + PATTERN1/2 (current source -> red/green)
 *   Switch or Streams : Stream1~3 + CUT/AUTO/FTB/MUTE
 *   PIP1~3 / LUMA / CHROMA / DSK / LOGO : four status keys (KEY/ON AIR/KEY&ON AIR/OFF)
 *   TRANSITIONS : WIPE1~4 / MIX / DIP / NORMAL / INV / FLIP-FLOP
 */
export function UpdatePresets(self: ModuleInstance): void {
	const presets: CompanionPresetDefinitions = {}
	// Counts and key values follow the protocol family (0617: 6 sources / 3 PIP / 4 wipes; H4K: 4 / 1 / 3)
	const family = self.getProtocolFamilyInfo()
	const keys = family.keyMap
	// First wipe style id (the first pattern, fixed 0; wipeStyleOffset is a send offset, not a first id)
	const firstWipeStyle = family.wipeStyles?.[0]?.id ?? 0
	// L3: preset defaults must follow the active protocol (H4K PIP/key sources are 0-based)
	const isH4K = family.id === 'avm-h4k'
	const defaultPipSource = family.pipSources?.find((s) => s.label === 'IN1')?.id ?? family.pipSources?.[0]?.id ?? 0

	// ===== PGM group (current source -> red) =====
	keys.pgm.forEach((_, i) => {
		const label = `PGM${i + 1}`
		presets[`pgm_${label.toLowerCase()}`] = buttonPreset(
			CAT_PGM,
			label,
			label,
			'set_source',
			// M2: device-independent key id, resolved against the active protocol when pressed
			{ source: `pgm${i + 1}` },
			{ feedbackId: 'pgm_active', options: { source: i + 1 }, style: STYLE_RED },
			PGM_BG,
		)
	})
	keys.pgmPattern.forEach((_, i) => {
		const label = `PGM_PATTERN${i + 1}`
		const displayLabel = `PATTERN${i + 1}`
		const disp = i === 0 ? 0xf0 : 0xf1
		presets[`pgm_${label.toLowerCase()}`] = buttonPreset(
			CAT_PGM,
			displayLabel,
			displayLabel,
			'set_source',
			{ source: `pgm_pattern${i + 1}` },
			{ feedbackId: 'pgm_active', options: { source: disp }, style: STYLE_RED },
			PGM_BG,
		)
	})

	// ===== PVW group (current source -> green) =====
	keys.pvw.forEach((_, i) => {
		const label = `PVW${i + 1}`
		presets[`pvw_${label.toLowerCase()}`] = buttonPreset(
			CAT_PVW,
			label,
			label,
			'set_source',
			{ source: `pvw${i + 1}` },
			{ feedbackId: 'pvw_active', options: { source: i + 1 }, style: STYLE_GREEN },
			PVW_BG,
		)
	})
	keys.pvwPattern.forEach((_, i) => {
		const label = `PVW_PATTERN${i + 1}`
		const displayLabel = `PATTERN${i + 1}`
		const disp = i === 0 ? 0xf0 : 0xf1
		presets[`pvw_${label.toLowerCase()}`] = buttonPreset(
			CAT_PVW,
			displayLabel,
			displayLabel,
			'set_source',
			{ source: `pvw_pattern${i + 1}` },
			{ feedbackId: 'pvw_active', options: { source: disp }, style: STYLE_GREEN },
			PVW_BG,
		)
	})

	// ===== Switch group (Stream 1/2/3 + CUT/AUTO/FTB/MUTE) =====
	const switchButtons: Array<{
		id: string
		label: string
		actionId: string
		value: string
		fbId?: string
		fbOpts?: Record<string, number>
		fbStyle?: Record<string, number>
	}> = [
		{
			id: 'stream1',
			label: 'Stream 1',
			actionId: 'switch_stream',
			value: 'stream1',
			fbId: 'stream_active',
			fbOpts: { stream: 1 },
			fbStyle: STYLE_YELLOW,
		},
		{
			id: 'stream2',
			label: 'Stream 2',
			actionId: 'switch_stream',
			value: 'stream2',
			fbId: 'stream_active',
			fbOpts: { stream: 2 },
			fbStyle: STYLE_YELLOW,
		},
		{
			id: 'stream3',
			label: 'Stream 3',
			actionId: 'switch_stream',
			value: 'stream3',
			fbId: 'stream_active',
			fbOpts: { stream: 3 },
			fbStyle: STYLE_YELLOW,
		},
		{ id: 'cut', label: 'CUT', actionId: 'switch_transition', value: 'cut' },
		{
			id: 'auto',
			label: 'AUTO',
			actionId: 'switch_transition',
			value: 'auto',
			fbId: 'auto_active',
			fbOpts: {},
			fbStyle: STYLE_RED,
		},
		{
			id: 'ftb',
			label: 'FTB',
			actionId: 'switch_transition',
			value: 'ftb',
			fbId: 'ftb_active',
			fbOpts: {},
			fbStyle: STYLE_RED,
		},
		{
			id: 'mute',
			label: 'MUTE',
			actionId: 'switch_transition',
			value: 'mute',
			fbId: 'mute_active',
			fbOpts: {},
			fbStyle: STYLE_RED,
		},
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
			b.actionId,
		)
	}

	// ===== Four status keys (KEY / ON AIR / KEY&ON AIR / OFF) - shared by PIP/LUMA/CHROMA/DSK/LOGO =====
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
				{ feedbackId: fbId, options: { status }, style },
			)
		}
	}

	// PIP1 / PIP2 / PIP3 (four status keys + Adjust)
	statusGroup(catPip(1), 'PIP1', 'pip1_status', 'pip1', 'pip1_status_active')
	presets['pip1_adjust'] = buttonPreset(catPip(1), 'PIP1 Adjust', '[PIP1]\n——\nADJUST', 'pip1_adjust', {
		source: defaultPipSource,
		size: 100,
		posx: 50,
		posy: 50,
	})
	statusGroup(catPip(2), 'PIP2', 'pip2_status', 'pip2', 'pip2_status_active')
	presets['pip2_adjust'] = buttonPreset(catPip(2), 'PIP2 Adjust', '[PIP2]\n——\nADJUST', 'pip2_adjust', {
		source: defaultPipSource,
		size: 100,
		posx: 50,
		posy: 50,
	})
	statusGroup(catPip(3), 'PIP3', 'pip3_status', 'pip3', 'pip3_status_active')
	presets['pip3_adjust'] = buttonPreset(catPip(3), 'PIP3 Adjust', '[PIP3]\n——\nADJUST', 'pip3_adjust', {
		source: defaultPipSource,
		size: 100,
		posx: 50,
		posy: 50,
	})

	// LUMA / CHROMA / DSK / LOGO (four status keys; each also gets an Adjust button)
	statusGroup(CAT_LUMA, 'LUMA', 'luma_status', 'luma', 'luma_status_active')
	presets['luma_adjust'] = buttonPreset(CAT_LUMA, 'LUMA Adjust', '[LUMA]\n——\nADJUST', 'luma_adjust', {
		size: 100,
		posx: 50,
		posy: 50,
		// L3: H4K Clip is a dropdown (Off/On/Curve); 0617 uses a 0-100 slider
		clip: isH4K ? 0 : 50,
		...(isH4K ? {} : { gain: 50 }),
	})
	statusGroup(CAT_CHROMA, 'CHROMA', 'chroma_status', 'chroma', 'chroma_status_active')
	presets['chroma_adjust'] = buttonPreset(CAT_CHROMA, 'CHROMA Adjust', '[CHROMA]\n——\nADJUST', 'chroma_adjust', {
		size: 100,
		posx: 50,
		posy: 50,
		similarity: 50,
		smooth: 0,
		spill: 0,
		opacity: 100,
		brightness: 50,
		contrast: 50,
		saturation: 50,
	})
	statusGroup(CAT_DSK, 'DSK', 'dsk_status', 'dsk', 'dsk_status_active')
	presets['dsk_adjust'] = buttonPreset(CAT_DSK, 'DSK Adjust', '[DSK]\n——\nADJUST', 'dsk_adjust', { clip: 50, gain: 50 })
	statusGroup(CAT_LOGO, 'LOGO', 'logo_status', 'logo', 'logo_status_active')
	presets['logo_adjust'] = buttonPreset(CAT_LOGO, 'LOGO Adjust', '[LOGO]\n——\nADJUST', 'logo_adjust', {
		posx: 50,
		posy: 50,
		size: 10,
		opacity: 100,
	})

	// ===== TRANSITIONS group (WIPE1~4 / MIX / DIP / NORMAL / INV / FLIP-FLOP) =====
	const transButtons: Array<{
		id: string
		text: string
		name: string
		actionId: string
		opts: Record<string, number | string>
		fbId?: string
		fbOpts?: Record<string, number>
	}> = [
		{
			id: 'trans_wipe1',
			text: '[TRANS]\n——\nWIPE1',
			name: 'TRANS WIPE1',
			actionId: 'trans_wipe1',
			opts: { style: firstWipeStyle },
			fbId: 'wipe_active',
			fbOpts: { mode: 1 },
		},
		{
			id: 'trans_wipe2',
			text: '[TRANS]\n——\nWIPE2',
			name: 'TRANS WIPE2',
			actionId: 'trans_wipe2',
			opts: { style: firstWipeStyle },
			fbId: 'wipe_active',
			fbOpts: { mode: 2 },
		},
		{
			id: 'trans_wipe3',
			text: '[TRANS]\n——\nWIPE3',
			name: 'TRANS WIPE3',
			actionId: 'trans_wipe3',
			opts: { style: firstWipeStyle },
			fbId: 'wipe_active',
			fbOpts: { mode: 3 },
		},
		{
			id: 'trans_wipe4',
			text: '[TRANS]\n——\nWIPE4',
			name: 'TRANS WIPE4',
			actionId: 'trans_wipe4',
			opts: { style: firstWipeStyle },
			fbId: 'wipe_active',
			fbOpts: { mode: 4 },
		},
		{
			id: 'trans_mix',
			text: '[TRANS]\n——\nMIX',
			name: 'TRANS MIX',
			actionId: 'trans_effect',
			opts: { value: 'mix' },
			fbId: 'wipe_active',
			fbOpts: { mode: 5 },
		},
		{
			id: 'trans_dip',
			text: '[TRANS]\n——\nDIP',
			name: 'TRANS DIP',
			actionId: 'trans_effect',
			opts: { value: 'dip' },
			fbId: 'wipe_active',
			fbOpts: { mode: 6 },
		},
		{
			id: 'trans_freeze',
			text: '[TRANS]\n——\nFREEZE',
			name: 'TRANS FREEZE',
			actionId: 'trans_effect',
			opts: { value: 'freeze' },
			fbId: 'freeze_active',
			fbOpts: {},
		},
		{
			id: 'trans_normal',
			text: '[TRANS]\n——\nNORMAL',
			name: 'TRANS NORMAL',
			actionId: 'trans_direction',
			opts: { value: 0 },
		},
		{
			id: 'trans_inv',
			text: '[TRANS]\n——\nINV',
			name: 'TRANS INV',
			actionId: 'trans_direction',
			opts: { value: 1 },
		},
		{
			id: 'trans_flipflop',
			text: '[TRANS]\n——\nFLIP-FLOP',
			name: 'TRANS FLIP-FLOP',
			actionId: 'trans_direction',
			opts: { value: 2 },
		},
	]
	for (const b of transButtons) {
		presets[b.id] = buttonPreset(
			CAT_TRANS,
			b.name,
			b.text,
			b.actionId,
			b.opts,
			b.fbId
				? { feedbackId: b.fbId, options: b.fbOpts ?? {}, style: b.fbId === 'freeze_active' ? STYLE_RED : STYLE_GREEN }
				: undefined,
			DARK,
			b.actionId,
		)
	}

	// ===== Audio Setting group (one button per function) =====
	// Simple keys / toggles / sliders without a channel
	const audioSimple: Array<{ id: string; text: string; name: string; actionId: string; opts: Record<string, number> }> =
		[
			{
				id: 'audio_all_afv',
				text: '[AFV]\nAll AFV',
				name: 'Audio All AFV',
				actionId: 'audio_all_afv',
				opts: { value: 0 },
			},
			{ id: 'audio_reset', text: '[AUDIO]\nRESET', name: 'Audio Reset', actionId: 'audio_reset', opts: {} },
			{
				id: 'audio_master_en',
				text: '[PGM OUT]\nENABLE',
				name: 'PGM OUT Enable',
				actionId: 'audio_master_en',
				opts: { value: 1 },
			},
			{
				id: 'audio_master_vol',
				text: '[PGM OUT]\nVOLUME',
				name: 'PGM OUT Volume',
				actionId: 'audio_master_vol',
				opts: { value: 50 },
			},
			{
				id: 'audio_ear_en',
				text: '[EAR]\nENABLE',
				name: 'Earphone Enable',
				actionId: 'audio_ear_en',
				opts: { value: 1 },
			},
			{
				id: 'audio_ear_vol',
				text: '[EAR]\nVOLUME',
				name: 'Earphone Volume',
				actionId: 'audio_ear_vol',
				opts: { value: 50 },
			},
			{
				id: 'audio_ear_src',
				text: '[EAR]\nSOURCE',
				name: 'Earphone Source',
				actionId: 'audio_ear_src',
				opts: { value: 0 },
			},
			{
				id: 'audio_line_en',
				text: '[LINE IN]\nENABLE',
				name: 'Line In Enable',
				actionId: 'audio_line_en',
				opts: { value: 1 },
			},
			{
				id: 'audio_line_vol',
				text: '[LINE IN]\nVOLUME',
				name: 'Line In Volume',
				actionId: 'audio_line_vol',
				opts: { value: 50 },
			},
			{
				id: 'audio_line_delay',
				text: '[LINE IN]\nDELAY',
				name: 'Line In Delay',
				actionId: 'audio_line_delay',
				opts: { value: 0 },
			},
			{ id: 'audio_xlr_en', text: '[XLR]\nENABLE', name: 'XLR Enable', actionId: 'audio_xlr_en', opts: { value: 1 } },
			{
				id: 'audio_xlr_vol',
				text: '[XLR]\nVOLUME',
				name: 'XLR Volume',
				actionId: 'audio_xlr_vol',
				opts: { value: 50 },
			},
			{
				id: 'audio_xlr_delay',
				text: '[XLR]\nDELAY',
				name: 'XLR Delay',
				actionId: 'audio_xlr_delay',
				opts: { value: 0 },
			},
			{
				id: 'audio_mic_xlr_mode',
				text: '[MIC/XLR]\nMODE',
				name: 'MIC/XLR Mode',
				actionId: 'audio_mic_xlr_mode',
				opts: { value: 0 },
			},
		]
	for (const b of audioSimple) {
		// H4K has no Audio Reset: do not create the preset button
		if (b.actionId === 'audio_reset' && family.hideAudioResetAction) continue
		presets[b.id] = buttonPreset(CAT_AUDIO, b.name, b.text, b.actionId, b.opts, undefined, DARK, b.actionId)
	}

	// IN1~N x (ENABLE / VOLUME / AFV / DELAY), N follows the protocol family (0617=6 / H4K=4)
	for (let n = 1; n <= family.inputCount; n++) {
		presets[`audio_in${n}_en`] = buttonPreset(
			CAT_AUDIO,
			`IN${n} Enable`,
			`[IN${n}]\nENABLE`,
			'audio_in_en',
			{ channel: n, value: 1 },
			undefined,
			DARK,
			'audio_in_en',
		)
		presets[`audio_in${n}_vol`] = buttonPreset(
			CAT_AUDIO,
			`IN${n} Volume`,
			`[IN${n}]\nVOLUME`,
			'audio_in_vol',
			{ channel: n, value: 50 },
			undefined,
			DARK,
			'audio_in_vol',
		)
		presets[`audio_in${n}_afv`] = buttonPreset(
			CAT_AUDIO,
			`IN${n} AFV`,
			`[IN${n}]\nAFV`,
			'audio_in_afv',
			{ channel: n, value: 0 },
			undefined,
			DARK,
			'audio_in_afv',
		)
		presets[`audio_in${n}_delay`] = buttonPreset(
			CAT_AUDIO,
			`IN${n} Delay`,
			`[IN${n}]\nDELAY`,
			'audio_in_delay',
			{ channel: n, value: 0 },
			undefined,
			DARK,
			'audio_in_delay',
		)
	}

	// MIC1~2 × (ENABLE / GUITAR / PRE-GAIN / VOLUME / DELAY)
	for (const n of [1, 2]) {
		presets[`audio_mic${n}_en`] = buttonPreset(
			CAT_AUDIO,
			`MIC${n} Enable`,
			`[MIC${n}]\nENABLE`,
			'audio_mic_en',
			{ channel: n, value: 1 },
			undefined,
			DARK,
			'audio_mic_en',
		)
		presets[`audio_mic${n}_guitar`] = buttonPreset(
			CAT_AUDIO,
			`MIC${n} Guitar`,
			`[MIC${n}]\nGUITAR`,
			'audio_mic_guitar',
			{ channel: n, value: 0 },
			undefined,
			DARK,
			'audio_mic_guitar',
		)
		presets[`audio_mic${n}_pregain`] = buttonPreset(
			CAT_AUDIO,
			`MIC${n} Pre-Gain`,
			`[MIC${n}]\nPRE-GAIN`,
			'audio_mic_pregain',
			{ channel: n, value: 0 },
			undefined,
			DARK,
			'audio_mic_pregain',
		)
		presets[`audio_mic${n}_vol`] = buttonPreset(
			CAT_AUDIO,
			`MIC${n} Volume`,
			`[MIC${n}]\nVOLUME`,
			'audio_mic_vol',
			{ channel: n, value: 50 },
			undefined,
			DARK,
			'audio_mic_vol',
		)
		presets[`audio_mic${n}_delay`] = buttonPreset(
			CAT_AUDIO,
			`MIC${n} Delay`,
			`[MIC${n}]\nDELAY`,
			'audio_mic_delay',
			{ channel: n, value: 0 },
			undefined,
			DARK,
			'audio_mic_delay',
		)
	}

	// ===== TBAR group (+ / -) =====
	presets['tbar_up'] = buttonPreset(
		CAT_TBAR,
		'T-Bar +',
		'+',
		'tbar_move',
		{ direction: 1, step: 10 },
		undefined,
		DARK,
		'tbar_move',
	)
	presets['tbar_down'] = buttonPreset(
		CAT_TBAR,
		'T-Bar -',
		'-',
		'tbar_move',
		{ direction: 0, step: 10 },
		undefined,
		DARK,
		'tbar_move',
	)
	// Shows the current value only (no action); the text is bound to the tbar_value variable
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

	// Drop presets that reference an action not registered for this product (e.g. H4K has no Stream / XLR / PIP2 / PIP3)
	const actionIds = self.getRegisteredActionIds()
	const available: CompanionPresetDefinitions = {}
	for (const [id, preset] of Object.entries(presets)) {
		if (!preset) continue
		if (!('steps' in preset) || !preset.steps) {
			available[id] = preset
			continue
		}
		const usedActionIds = (
			preset.steps as Array<{ down?: Array<{ actionId: string }>; up?: Array<{ actionId: string }> }>
		)
			.flatMap((step) => [...(step.down ?? []), ...(step.up ?? [])])
			.map((action) => action.actionId)
		if (usedActionIds.every((actionId) => actionIds.has(actionId))) available[id] = preset
	}

	// Filter presets by the current product profile (unsupported buttons disappear with their category)
	self.setPresetDefinitions(filterByProfile(available, self.getDeviceProfile()))
}

import type { ModuleInstance } from './main.js'
import {
	CompanionActionDefinitions,
	CompanionInputFieldDropdown,
	CompanionInputFieldNumber,
} from '@companion-module/base'
import { isIdEnabled } from './devices/index.js'
import { flashKeyFor } from './commandHandler.js'

/** Option types used by Adjust actions (slider + dropdown) */
type AdjustOption = CompanionInputFieldNumber | CompanionInputFieldDropdown

/**
 * Whether the current protocol command has all of the given fields.
 * Example: H4K LUMA has no FillSource/Invert, so actions depending on them are not registered.
 */
function supports(self: ModuleInstance, cmdKey: string, ...fields: string[]): boolean {
	return fields.every((f) => self.hasField(cmdKey, f))
}

/** Key-source / PIP-source dropdown items of the current protocol (enumeration start differs) */
const keySourcesOf = (self: ModuleInstance) => self.getProtocolFamilyInfo().keySources
const pipSourcesOf = (self: ModuleInstance) => self.getProtocolFamilyInfo().pipSources

/** Default source value (the id of IN1) */
function defaultSourceId(sources: Array<{ id: number; label: string }>): number {
	return sources.find((s) => s.label === 'IN1')?.id ?? sources[0]?.id ?? 0
}

/**
 * Resolve a device-independent key id ("pgm1", "cut", "stream2", "pip_on_air") to the
 * key value of the active protocol.
 *
 * M2: action options store these ids instead of raw key values, so a button keeps
 * pressing the same logical key after the device profile changes.
 */
function resolveKeyId(self: ModuleInstance, id: unknown): number | undefined {
	const keys = self.getProtocolFamilyInfo().keyMap
	if (typeof id !== 'string' || id === '') return undefined
	const raw = id
	const numbered = /^(pgm_pattern|pvw_pattern|pgm|pvw|stream|wipe)_?(\d+)$/.exec(raw)
	if (numbered) {
		const index = Number(numbered[2]) - 1
		if (index < 0) return undefined
		switch (numbered[1]) {
			case 'pgm':
				return keys.pgm[index]
			case 'pvw':
				return keys.pvw[index]
			case 'pgm_pattern':
				return keys.pgmPattern[index]
			case 'pvw_pattern':
				return keys.pvwPattern[index]
			case 'stream':
				return keys.stream[index]
			case 'wipe':
				return keys.wipe[index]
		}
	}
	switch (raw) {
		case 'cut':
			return keys.cut
		case 'auto':
			return keys.auto
		case 'ftb':
			return keys.ftb
		case 'mute':
			return keys.mute
		case 'mix':
			return keys.mix
		case 'dip':
			return keys.dip
		case 'freeze':
			return keys.freeze
		case 'pip':
			return keys.pip
		case 'pip_on_air':
			return keys.pipOnAir
		case 'luma':
			return keys.luma
		case 'luma_on_air':
			return keys.lumaOnAir
		case 'chroma':
			return keys.chroma
		case 'chroma_on_air':
			return keys.chromaOnAir
		case 'dsk':
			return keys.dsk
		case 'dsk_on_air':
			return keys.dskOnAir
	}
	return undefined
}

// ==================== Shared options ====================

// Status: OFF / KEY / ON AIR / KEY&ON AIR (shared by PIP/LUMA/CHROMA/DSK/LOGO)
const STATUS_CHOICES = [
	{ id: 0, label: 'OFF' },
	{ id: 1, label: 'KEY' },
	{ id: 2, label: 'ON AIR' },
	{ id: 3, label: 'KEY&ON AIR' },
]

// ON / OFF
const ONOFF_CHOICES = [
	{ id: 1, label: 'ON' },
	{ id: 0, label: 'OFF' },
]

// Key-source / PIP-source dropdowns come from the protocol family (keySources / pipSources in devices/protocols.ts)

// CHROMA Key Color Type (0617: 0-4)
const CHROMA_KEY_TYPE_CHOICES = [
	{ id: 0, label: 'Green' },
	{ id: 1, label: 'Blue' },
	{ id: 2, label: 'Red' },
	{ id: 3, label: 'Custom' },
	{ id: 4, label: 'Fetch' },
]

// H4K Key Color Type: only RED / GREEN / BLUE (0/1/2)
const H4K_KEY_COLOR_CHOICES = [
	{ id: 0, label: 'Red' },
	{ id: 1, label: 'Green' },
	{ id: 2, label: 'Blue' },
]

// Transition Direction (0-2)
const DIRECTION_CHOICES = [
	{ id: 0, label: 'Normal' },
	{ id: 1, label: 'Invert' },
	{ id: 2, label: 'Flip-Flop' },
]

// Wipe style dropdown comes from the protocol family (0617: 0~10; H4K: 0~27, sent value = dropdown id, 0 = first pattern)

/** Build a number (slider) option */
function slider(id: string, label: string, min: number, max: number, def: number): CompanionInputFieldNumber {
	return { type: 'number', id, label: `${label} (${min}-${max})`, min, max, default: def, range: true, step: 1 }
}

/** Build an ON/OFF dropdown option */
function onoff(id: string, label: string, def = 0) {
	return { type: 'dropdown' as const, id, label, choices: ONOFF_CHOICES, default: def }
}

// ==================== PIP1~3 ====================
/**
 * PIP1~3 (set commands 0x0033/0x0034/0x0035)
 * Fields: 0=Status, 1=Source, 2=Size, 3=PosX, 4=PosY
 */
function registerPipActions(
	self: ModuleInstance,
	actions: CompanionActionDefinitions,
	n: number,
	commandKey: string,
): void {
	const tag = `PIP${n}`
	// Status (KEY / ON AIR / KEY&ON AIR / OFF combined into one dropdown)
	actions[`pip${n}_status`] = {
		name: `${tag} Status`,
		description: `Set ${tag} status`,
		options: [{ type: 'dropdown', id: 'status', label: 'Status', choices: STATUS_CHOICES, default: 0 }],
		callback: async (event) => {
			const status = Number(event.options.status)
			// H4K: PIP / LUMA / CHROMA are mutually exclusive, so close the other layers first (old families return immediately)
			if (status >= 1) await self.closeOtherKeys(commandKey)
			await self.sendProtocolField(commandKey, 'Status', status, `${tag} Status`)
			if (status >= 1) self.markKeyTypeLocal(0)
		},
	}
	// Parameters (Source/Size/PosX/PosY in one action; H4K adds the Border fields)
	const pipAdjustOptions: AdjustOption[] = [
		{
			type: 'dropdown',
			id: 'source',
			label: 'Source',
			choices: pipSourcesOf(self),
			default: defaultSourceId(pipSourcesOf(self)),
		},
		slider('size', 'Size', 12, 100, 100),
		slider('posx', 'PosX', 0, 100, 50),
		slider('posy', 'PosY', 0, 100, 50),
	]
	if (supports(self, commandKey, 'BorderEnable')) pipAdjustOptions.push(onoff('borderEnable', 'Border Enable'))
	if (supports(self, commandKey, 'BorderColor')) pipAdjustOptions.push(slider('borderColor', 'Border Color', 0, 100, 0))
	if (supports(self, commandKey, 'BorderWidth')) pipAdjustOptions.push(slider('borderWidth', 'Border Width', 0, 100, 0))
	actions[`pip${n}_adjust`] = {
		name: `${tag} Adjust`,
		description: `${tag} Source / Size / PosX / PosY / Border`,
		options: pipAdjustOptions,
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolField(commandKey, 'Source', Number(o.source), `${tag} Source`)
			await self.sendProtocolField(commandKey, 'Size', Number(o.size), `${tag} Size`)
			await self.sendProtocolField(commandKey, 'PosX', Number(o.posx), `${tag} PosX`)
			await self.sendProtocolField(commandKey, 'PosY', Number(o.posy), `${tag} PosY`)
			// H4K Border fields (absent on 0617, skipped automatically); legacy -1 values are treated as 0
			await self.sendProtocolField(
				commandKey,
				'BorderEnable',
				Math.max(0, Number(o.borderEnable ?? 0)),
				`${tag} Border Enable`,
			)
			await self.sendProtocolField(
				commandKey,
				'BorderColor',
				Math.max(0, Number(o.borderColor ?? 0)),
				`${tag} Border Color`,
			)
			await self.sendProtocolField(
				commandKey,
				'BorderWidth',
				Math.max(0, Number(o.borderWidth ?? 0)),
				`${tag} Border Width`,
			)
		},
	}
}

// ==================== LUMA ====================
/**
 * LUMA (0x0031)
 * Fields: 0=Tie,1=Status,2=FillSource,3=KeySource,4=Size,5=PosX,6=PosY,7=Clip,8=Gain,
 *         9=Invert,10=MaskEnable,11=MaskLeft,12=MaskTop,13=MaskRight,14=MaskBottom
 */
function registerLumaActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	actions['luma_status'] = {
		name: 'LUMA Status',
		description: 'Set LUMA status',
		options: [{ type: 'dropdown', id: 'status', label: 'Status', choices: STATUS_CHOICES, default: 0 }],
		callback: async (event) => {
			const status = Number(event.options.status)
			// H4K: PIP / LUMA / CHROMA are mutually exclusive, so close the other layers first (old families return immediately)
			if (status >= 1) await self.closeOtherKeys('luma')
			await self.sendProtocolField('luma', 'Status', status, 'LUMA Status')
			if (status >= 1) self.markKeyTypeLocal(1)
		},
	}
	if (supports(self, 'luma', 'FillSource')) {
		actions['luma_fill_source'] = {
			name: 'LUMA Fill Source',
			description: 'Select the LUMA fill source',
			options: [
				{
					type: 'dropdown',
					id: 'value',
					label: 'Source',
					choices: keySourcesOf(self),
					default: defaultSourceId(keySourcesOf(self)),
				},
			],
			callback: async (event) => {
				await self.sendProtocolField('luma', 'FillSource', Number(event.options.value), 'LUMA Fill Source')
			},
		}
	}
	actions['luma_key_source'] = {
		name: 'LUMA Key Source',
		description: 'Select the LUMA key source',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Source',
				choices: keySourcesOf(self),
				default: defaultSourceId(keySourcesOf(self)),
			},
		],
		callback: async (event) => {
			await self.sendProtocolField('luma', 'KeySource', Number(event.options.value), 'LUMA Key Source')
		},
	}
	// Build option fields from the protocol fields (e.g. H4K has no Gain, but has Tolerance/Clip ranges)
	// H4K Clip / Tolerance are enums (not 0-100 values), and Mask uses 0~100%
	const isH4K = !!self.getProtocolCommands()['keyType']
	const lumaAdjustOptions: AdjustOption[] = []
	if (supports(self, 'luma', 'Size')) lumaAdjustOptions.push(slider('size', 'Zoom Size', 12, 100, 100))
	if (supports(self, 'luma', 'PosX')) lumaAdjustOptions.push(slider('posx', 'Key PositionX', 0, 100, 50))
	if (supports(self, 'luma', 'PosY')) lumaAdjustOptions.push(slider('posy', 'Key PositionY', 0, 100, 50))
	if (supports(self, 'luma', 'Clip')) {
		if (isH4K) {
			lumaAdjustOptions.push({
				type: 'dropdown',
				id: 'clip',
				label: 'Clip',
				choices: [
					{ id: 0, label: 'Off' },
					{ id: 1, label: 'On' },
					{ id: 2, label: 'Curve' },
				],
				default: 0,
			})
		} else {
			lumaAdjustOptions.push(slider('clip', 'Clip', 0, 100, 50))
		}
	}
	if (supports(self, 'luma', 'Gain')) lumaAdjustOptions.push(slider('gain', 'Gain', 0, 100, 50))
	// H4K fields
	if (supports(self, 'luma', 'Tolerance')) {
		lumaAdjustOptions.push({
			type: 'dropdown',
			id: 'tolerance',
			label: 'Tolerance',
			choices: [
				{ id: 0, label: 'Default' },
				{ id: 1, label: 'Curve' },
				{ id: 2, label: 'Invert' },
				{ id: 3, label: 'Curve and Invert' },
			],
			default: 0,
		})
	}
	if (supports(self, 'luma', 'ToleranceMin')) lumaAdjustOptions.push(slider('toleranceMin', 'Tolerance Min', 0, 100, 0))
	if (supports(self, 'luma', 'ToleranceMax'))
		lumaAdjustOptions.push(slider('toleranceMax', 'Tolerance Max', 0, 100, 100))
	if (supports(self, 'luma', 'ClipMin')) lumaAdjustOptions.push(slider('clipMin', 'Clip Min', 0, 100, 0))
	if (supports(self, 'luma', 'ClipMax')) lumaAdjustOptions.push(slider('clipMax', 'Clip Max', 0, 100, 100))
	// H4K Mask uses 0~100% on every edge
	if (isH4K && supports(self, 'luma', 'MaskEnable')) lumaAdjustOptions.push(onoff('maskEnable', 'Mask Enable', 0))
	if (isH4K && supports(self, 'luma', 'MaskLeft')) lumaAdjustOptions.push(slider('maskLeft', 'Mask Left', 0, 100, 0))
	if (isH4K && supports(self, 'luma', 'MaskTop')) lumaAdjustOptions.push(slider('maskTop', 'Mask Top', 0, 100, 0))
	if (isH4K && supports(self, 'luma', 'MaskRight'))
		lumaAdjustOptions.push(slider('maskRight', 'Mask Right', 0, 100, 100))
	if (isH4K && supports(self, 'luma', 'MaskBottom'))
		lumaAdjustOptions.push(slider('maskBottom', 'Mask Bottom', 0, 100, 100))
	actions['luma_adjust'] = {
		name: 'LUMA Adjust',
		description: 'LUMA Zoom Size / Key PosX / Key PosY / Clip / Gain / Tolerance / Clip Range / Mask',
		options: lumaAdjustOptions,
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolField('luma', 'Size', Number(o.size), 'LUMA Zoom Size')
			await self.sendProtocolField('luma', 'PosX', Number(o.posx), 'LUMA Key PositionX')
			await self.sendProtocolField('luma', 'PosY', Number(o.posy), 'LUMA Key PositionY')
			// H4K fields (absent on 0617, skipped automatically); legacy -1 values are treated as 0
			const extras: Array<[string, string]> = [
				['tolerance', 'Tolerance'],
				['toleranceMin', 'ToleranceMin'],
				['toleranceMax', 'ToleranceMax'],
				['clipMin', 'ClipMin'],
				['clipMax', 'ClipMax'],
				['maskEnable', 'MaskEnable'],
				['maskLeft', 'MaskLeft'],
				['maskTop', 'MaskTop'],
				['maskRight', 'MaskRight'],
				['maskBottom', 'MaskBottom'],
			]
			for (const [opt, field] of extras) {
				if (o[opt] === undefined) continue
				await self.sendProtocolField('luma', field, Math.max(0, Number(o[opt])), `LUMA ${field}`)
			}
			await self.sendProtocolField('luma', 'Clip', Math.max(0, Number(o.clip ?? 0)), 'LUMA Clip')
			if (o.gain !== undefined) {
				await self.sendProtocolField('luma', 'Gain', Number(o.gain), 'LUMA Gain')
			}
		},
	}
	if (supports(self, 'luma', 'Invert')) {
		actions['luma_invert'] = {
			name: 'LUMA Invert Key',
			description: 'LUMA Invert Key (0:OFF / 1:ON)',
			options: [onoff('value', 'State')],
			callback: async (event) => {
				await self.sendProtocolField('luma', 'Invert', Number(event.options.value), 'LUMA Invert Key')
			},
		}
	}
	actions['luma_mask'] = {
		name: 'LUMA Mask',
		description: 'LUMA Mask enable + Left/Top/Right/Bottom (0~100%, left must not exceed right)',
		options: [
			onoff('enable', 'Enable'),
			slider('left', 'Mask Left', 0, isH4K ? 100 : 50, 0),
			slider('top', 'Mask Top', 0, isH4K ? 100 : 50, 0),
			slider('right', 'Mask Right', isH4K ? 0 : 50, 100, 100),
			slider('bottom', 'Mask Bottom', isH4K ? 0 : 50, 100, 100),
		],
		callback: async (event) => {
			const o = event.options
			const left = Number(o.left)
			const top = Number(o.top)
			const right = Number(o.right)
			const bottom = Number(o.bottom)
			await self.sendProtocolField('luma', 'MaskEnable', Number(o.enable), 'LUMA Mask Enable')
			// Documented constraint: left must not exceed right, top must not exceed bottom
			await self.sendProtocolField('luma', 'MaskLeft', Math.min(left, right), 'LUMA Mask Left')
			await self.sendProtocolField('luma', 'MaskTop', Math.min(top, bottom), 'LUMA Mask Top')
			await self.sendProtocolField('luma', 'MaskRight', Math.max(right, left), 'LUMA Mask Right')
			await self.sendProtocolField('luma', 'MaskBottom', Math.max(bottom, top), 'LUMA Mask Bottom')
		},
	}
}

// ==================== CHROMA ====================
/**
 * CHROMA (0x0032)
 * Fields: 0=Status,1=KeySource,2=KeyType,6=Size,7=PosX,8=PosY,9=Similarity,10=Smooth,
 *         11=Spill,12=Opacity,13=Brightness,14=Contrast,15=Saturation,
 *         16=MaskEnable,17=MaskLeft,18=MaskTop,19=MaskRight,20=MaskBottom
 */
function registerChromaActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	// H4K: Key Color Type is only Red/Green/Blue, Size 0~100, with Tolerance/Softness/Clip/Correction/Mask
	const isH4K = !!self.getProtocolCommands()['keyType']
	actions['chroma_status'] = {
		name: 'CHROMA Status',
		description: 'Set CHROMA status',
		options: [{ type: 'dropdown', id: 'status', label: 'Status', choices: STATUS_CHOICES, default: 0 }],
		callback: async (event) => {
			const status = Number(event.options.status)
			// H4K: PIP / LUMA / CHROMA are mutually exclusive, so close the other layers first (old families return immediately)
			if (status >= 1) await self.closeOtherKeys('chroma')
			await self.sendProtocolField('chroma', 'Status', status, 'CHROMA Status')
			if (status >= 1) self.markKeyTypeLocal(2)
		},
	}
	actions['chroma_key_source'] = {
		name: 'CHROMA Key Source',
		description: 'Select the CHROMA key source',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Source',
				choices: keySourcesOf(self),
				default: defaultSourceId(keySourcesOf(self)),
			},
		],
		callback: async (event) => {
			await self.sendProtocolField('chroma', 'KeySource', Number(event.options.value), 'CHROMA Key Source')
		},
	}
	actions['chroma_key_type'] = {
		name: 'CHROMA Key Color Type',
		description: 'CHROMA Key Color Type (H4K: Red/Green/Blue)',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Type',
				choices: isH4K ? H4K_KEY_COLOR_CHOICES : CHROMA_KEY_TYPE_CHOICES,
				default: 0,
			},
		],
		callback: async (event) => {
			await self.sendProtocolField('chroma', 'KeyType', Number(event.options.value), 'CHROMA Key Color Type')
		},
	}
	// Build option fields from the protocol fields (e.g. H4K has no Spill/Opacity, but adds Angle/Tolerance/Softness/Clip/Correction/Color)
	const chromaAdjustOptions: AdjustOption[] = []
	if (supports(self, 'chroma', 'Size'))
		chromaAdjustOptions.push(
			isH4K ? slider('size', 'Zoom Size', 0, 100, 100) : slider('size', 'Zoom Size', 12, 100, 100),
		)
	if (supports(self, 'chroma', 'PosX')) chromaAdjustOptions.push(slider('posx', 'Key PositionX', 0, 100, 50))
	if (supports(self, 'chroma', 'PosY')) chromaAdjustOptions.push(slider('posy', 'Key PositionY', 0, 100, 50))
	// 0617 fields (Similarity/Smooth/Spill/Opacity are its own fields)
	if (supports(self, 'chroma', 'Similarity')) chromaAdjustOptions.push(slider('similarity', 'Similarity', 0, 100, 50))
	if (supports(self, 'chroma', 'Smooth')) chromaAdjustOptions.push(slider('smooth', 'Smoothness', 0, 255, 0))
	if (supports(self, 'chroma', 'Spill')) chromaAdjustOptions.push(slider('spill', 'Spill', 0, 255, 0))
	if (supports(self, 'chroma', 'Opacity')) chromaAdjustOptions.push(slider('opacity', 'Opacity', 0, 100, 100))
	if (supports(self, 'chroma', 'Brightness')) chromaAdjustOptions.push(slider('brightness', 'Brightness', 0, 100, 50))
	if (supports(self, 'chroma', 'Contrast')) chromaAdjustOptions.push(slider('contrast', 'Contrast', 0, 100, 50))
	if (supports(self, 'chroma', 'Saturation')) chromaAdjustOptions.push(slider('saturation', 'Saturation', 0, 100, 50))
	// H4K fields (Angle / Tolerance / Softness / Clip range / Correction / RGB)
	if (supports(self, 'chroma', 'Angle')) chromaAdjustOptions.push(slider('angle', 'Angle', 0, 100, 50))
	if (supports(self, 'chroma', 'Tolerance')) chromaAdjustOptions.push(slider('tolerance', 'Tolerance', 0, 100, 50))
	if (supports(self, 'chroma', 'Softness')) chromaAdjustOptions.push(slider('softness', 'Softness', 0, 100, 0))
	if (supports(self, 'chroma', 'Clip')) {
		chromaAdjustOptions.push({
			type: 'dropdown',
			id: 'clip',
			label: 'Key Clip',
			choices: [
				{ id: 0, label: 'Off' },
				{ id: 1, label: 'On' },
				{ id: 2, label: 'Curve' },
			],
			default: 0,
		})
	}
	if (supports(self, 'chroma', 'ClipMin')) chromaAdjustOptions.push(slider('clipMin', 'Clip Min', 0, 100, 0))
	if (supports(self, 'chroma', 'ClipMax')) chromaAdjustOptions.push(slider('clipMax', 'Clip Max', 0, 100, 100))
	if (supports(self, 'chroma', 'Correction')) {
		chromaAdjustOptions.push({
			type: 'dropdown',
			id: 'correction',
			label: 'Correction',
			choices: [
				{ id: 0, label: 'Off' },
				{ id: 1, label: 'Red' },
				{ id: 2, label: 'Green' },
				{ id: 3, label: 'Blue' },
			],
			default: 0,
		})
	}
	if (supports(self, 'chroma', 'CorrectionVal'))
		chromaAdjustOptions.push(slider('correctionVal', 'Correction Value', 0, 100, 0))
	if (supports(self, 'chroma', 'ColorRed')) chromaAdjustOptions.push(slider('colorRed', 'Red Adjust', 0, 100, 50))
	if (supports(self, 'chroma', 'ColorGreen')) chromaAdjustOptions.push(slider('colorGreen', 'Green Adjust', 0, 100, 50))
	if (supports(self, 'chroma', 'ColorBlue')) chromaAdjustOptions.push(slider('colorBlue', 'Blue Adjust', 0, 100, 50))
	if (isH4K && supports(self, 'chroma', 'MaskEnable')) chromaAdjustOptions.push(onoff('maskEnable', 'Mask Enable', 0))
	if (isH4K && supports(self, 'chroma', 'MaskLeft'))
		chromaAdjustOptions.push(slider('maskLeft', 'Mask Left', 0, 100, 0))
	if (isH4K && supports(self, 'chroma', 'MaskTop')) chromaAdjustOptions.push(slider('maskTop', 'Mask Top', 0, 100, 0))
	if (isH4K && supports(self, 'chroma', 'MaskRight'))
		chromaAdjustOptions.push(slider('maskRight', 'Mask Right', 0, 100, 100))
	if (isH4K && supports(self, 'chroma', 'MaskBottom'))
		chromaAdjustOptions.push(slider('maskBottom', 'Mask Bottom', 0, 100, 100))
	actions['chroma_adjust'] = {
		name: 'CHROMA Adjust',
		description:
			'CHROMA Size/Pos/Angle/Tolerance/Softness/Clip/Correction/RGB/Mask (0617: Similarity/Smooth/Spill/Opacity)',
		options: chromaAdjustOptions,
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolField('chroma', 'Size', Number(o.size), 'CHROMA Zoom Size')
			await self.sendProtocolField('chroma', 'PosX', Number(o.posx), 'CHROMA Key PositionX')
			await self.sendProtocolField('chroma', 'PosY', Number(o.posy), 'CHROMA Key PositionY')
			// 0617 fields (absent on H4K, skipped automatically)
			const legacy: Array<[string, string]> = [
				['similarity', 'Similarity'],
				['smooth', 'Smooth'],
				['spill', 'Spill'],
				['opacity', 'Opacity'],
				['brightness', 'Brightness'],
				['contrast', 'Contrast'],
				['saturation', 'Saturation'],
			]
			for (const [opt, field] of legacy) {
				if (o[opt] === undefined) continue
				await self.sendProtocolField('chroma', field, Number(o[opt]), `CHROMA ${field}`)
			}
			// H4K fields (absent on 0617, skipped automatically)
			const extras: Array<[string, string]> = [
				['angle', 'Angle'],
				['tolerance', 'Tolerance'],
				['softness', 'Softness'],
				['clip', 'Clip'],
				['correction', 'Correction'],
				['correctionVal', 'CorrectionVal'],
				['colorRed', 'ColorRed'],
				['colorGreen', 'ColorGreen'],
				['colorBlue', 'ColorBlue'],
				['maskEnable', 'MaskEnable'],
				['maskLeft', 'MaskLeft'],
				['maskTop', 'MaskTop'],
				['maskRight', 'MaskRight'],
				['maskBottom', 'MaskBottom'],
			]
			// Clip_Min <= Clip_Max (computed first, then sent together)
			// H4K fields (absent on 0617, skipped automatically); legacy -1 values are treated as 0
			const cMin = Math.max(0, Math.min(Number(o.clipMin ?? 0), Number(o.clipMax ?? 100)))
			const cMax = Math.max(0, Math.max(Number(o.clipMin ?? 0), Number(o.clipMax ?? 100)))
			for (const [opt, field] of extras) {
				if (o[opt] === undefined) continue
				let v = Math.max(0, Number(o[opt]))
				if (field === 'ClipMin') v = cMin
				if (field === 'ClipMax') v = cMax
				await self.sendProtocolField('chroma', field, v, `CHROMA ${field}`)
			}
		},
	}
	actions['chroma_mask'] = {
		name: 'CHROMA Mask',
		description: 'CHROMA Mask enable + Left/Top/Right/Bottom (0~100%, left must not exceed right)',
		options: [
			onoff('enable', 'Enable'),
			slider('left', 'Mask Left', 0, isH4K ? 100 : 50, 0),
			slider('top', 'Mask Top', 0, isH4K ? 100 : 50, 0),
			slider('right', 'Mask Right', isH4K ? 0 : 50, 100, 100),
			slider('bottom', 'Mask Bottom', isH4K ? 0 : 50, 100, 100),
		],
		callback: async (event) => {
			const o = event.options
			const left = Number(o.left)
			const top = Number(o.top)
			const right = Number(o.right)
			const bottom = Number(o.bottom)
			await self.sendProtocolField('chroma', 'MaskEnable', Number(o.enable), 'CHROMA Mask Enable')
			await self.sendProtocolField('chroma', 'MaskLeft', Math.min(left, right), 'CHROMA Mask Left')
			await self.sendProtocolField('chroma', 'MaskTop', Math.min(top, bottom), 'CHROMA Mask Top')
			await self.sendProtocolField('chroma', 'MaskRight', Math.max(right, left), 'CHROMA Mask Right')
			await self.sendProtocolField('chroma', 'MaskBottom', Math.max(bottom, top), 'CHROMA Mask Bottom')
		},
	}
}

// ==================== DSK ====================
/**
 * DSK (0x0040)
 * Fields: 0=Tie,1=Status,2=FillSource,3=KeySource,4=Clip,5=Gain,6=Invert,
 *         7=MaskEnable,8=MaskLeft,9=MaskTop,10=MaskRight,11=MaskBottom
 */
function registerDskActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	actions['dsk_status'] = {
		name: 'DSK Status',
		description: 'Set DSK status',
		options: [{ type: 'dropdown', id: 'status', label: 'Status', choices: STATUS_CHOICES, default: 0 }],
		callback: async (event) => {
			await self.sendProtocolField('dsk', 'Status', Number(event.options.status), 'DSK Status')
		},
	}
	if (supports(self, 'dsk', 'FillSource')) {
		actions['dsk_fill_source'] = {
			name: 'DSK Fill Source',
			description: 'Select the DSK fill source',
			options: [
				{
					type: 'dropdown',
					id: 'value',
					label: 'Source',
					choices: keySourcesOf(self),
					default: defaultSourceId(keySourcesOf(self)),
				},
			],
			callback: async (event) => {
				await self.sendProtocolField('dsk', 'FillSource', Number(event.options.value), 'DSK Fill Source')
			},
		}
	}
	actions['dsk_key_source'] = {
		name: 'DSK Key Source',
		description: 'Select the DSK key source',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Source',
				choices: keySourcesOf(self),
				default: defaultSourceId(keySourcesOf(self)),
			},
		],
		callback: async (event) => {
			await self.sendProtocolField('dsk', 'KeySource', Number(event.options.value), 'DSK Key Source')
		},
	}
	if (supports(self, 'dsk', 'Tie')) {
		actions['dsk_tie'] = {
			name: 'DSK Tie',
			description: 'DSK Tie (0:OFF / 1:ON)',
			options: [onoff('value', 'State')],
			callback: async (event) => {
				await self.sendProtocolField('dsk', 'Tie', Number(event.options.value), 'DSK Tie')
			},
		}
	}
	const dskAdjustOptions: CompanionInputFieldNumber[] = []
	if (supports(self, 'dsk', 'Clip')) dskAdjustOptions.push(slider('clip', 'Clip', 0, 100, 50))
	if (supports(self, 'dsk', 'Gain')) dskAdjustOptions.push(slider('gain', 'Gain', 0, 100, 50))
	actions['dsk_adjust'] = {
		name: 'DSK Adjust',
		description: 'DSK Clip / Gain',
		options: dskAdjustOptions,
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolField('dsk', 'Clip', Number(o.clip), 'DSK Clip')
			await self.sendProtocolField('dsk', 'Gain', Number(o.gain), 'DSK Gain')
		},
	}
	if (supports(self, 'dsk', 'Invert')) {
		actions['dsk_invert'] = {
			name: 'DSK Invert',
			description: 'DSK Invert (0:OFF / 1:ON)',
			options: [onoff('value', 'State')],
			callback: async (event) => {
				await self.sendProtocolField('dsk', 'Invert', Number(event.options.value), 'DSK Invert')
			},
		}
	}
	actions['dsk_mask'] = {
		name: 'DSK Mask',
		description: 'DSK Mask enable + Left/Top/Right/Bottom',
		options: [
			onoff('enable', 'Enable'),
			slider('left', 'Mask Left', 0, 50, 0),
			slider('top', 'Mask Top', 0, 50, 0),
			slider('right', 'Mask Right', 50, 100, 100),
			slider('bottom', 'Mask Bottom', 50, 100, 100),
		],
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolField('dsk', 'MaskEnable', Number(o.enable), 'DSK Mask Enable')
			await self.sendProtocolField('dsk', 'MaskLeft', Number(o.left), 'DSK Mask Left')
			await self.sendProtocolField('dsk', 'MaskTop', Number(o.top), 'DSK Mask Top')
			await self.sendProtocolField('dsk', 'MaskRight', Number(o.right), 'DSK Mask Right')
			await self.sendProtocolField('dsk', 'MaskBottom', Number(o.bottom), 'DSK Mask Bottom')
		},
	}
}

// ==================== LOGO ====================
/**
 * LOGO (0x0041)
 * Fields: 0=Status,1=Select,2=PosX,3=PosY,4=Size,5=Opacity
 */
function registerLogoActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	actions['logo_status'] = {
		name: 'LOGO Status',
		description: 'Set LOGO status',
		options: [{ type: 'dropdown', id: 'status', label: 'Status', choices: STATUS_CHOICES, default: 0 }],
		callback: async (event) => {
			await self.sendProtocolField('logo', 'Status', Number(event.options.status), 'LOGO Status')
		},
	}
	actions['logo_select'] = {
		name: 'LOGO Select',
		description: 'Select the logo to display',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Logo',
				choices: Array.from({ length: self.getProtocolFamilyInfo().logoCount }, (_, n) => ({
					id: n,
					label: `Logo ${n + 1}`,
				})),
				default: 0,
			},
		],
		callback: async (event) => {
			await self.sendProtocolField('logo', 'Select', Number(event.options.value), 'LOGO Select')
		},
	}
	const logoAdjustOptions: CompanionInputFieldNumber[] = []
	if (supports(self, 'logo', 'PosX')) logoAdjustOptions.push(slider('posx', 'PositionX', 0, 100, 50))
	if (supports(self, 'logo', 'PosY')) logoAdjustOptions.push(slider('posy', 'PositionY', 0, 100, 50))
	if (supports(self, 'logo', 'Size')) logoAdjustOptions.push(slider('size', 'Size', 5, 20, 10))
	if (supports(self, 'logo', 'Opacity')) logoAdjustOptions.push(slider('opacity', 'Opacity', 20, 100, 100))
	actions['logo_adjust'] = {
		name: 'LOGO Adjust',
		description: 'LOGO PosX/PosY/Size/Opacity',
		options: logoAdjustOptions,
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolField('logo', 'PosX', Number(o.posx), 'LOGO PositionX')
			await self.sendProtocolField('logo', 'PosY', Number(o.posy), 'LOGO PositionY')
			await self.sendProtocolField('logo', 'Size', Number(o.size), 'LOGO Size')
			await self.sendProtocolField('logo', 'Opacity', Number(o.opacity), 'LOGO Opacity')
		},
	}
}

// ==================== TRANSITIONS ====================
/**
 * TRANSITIONS
 * 0x0020: 0~3 = Wipe1~4 style, 4 = Direction (0:Normal/1:Invert/2:Flip-Flop)
 * 0x0010 keys: Wipe1~4=27~30, MIX=31, DIP=32 (0617 values; H4K uses its own key map)
 */
function registerTransitionActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	// Wipe count and key values follow the protocol family (0617: 4; H4K: 3)
	const family = self.getProtocolFamilyInfo()
	const keys = family.keyMap
	for (let n = 1; n <= family.wipeCount; n++) {
		const keyVal = keys.wipe[n - 1]
		const label = `WIPE${n}`
		actions[`trans_wipe${n}`] = {
			name: `Transition ${label}`,
			description: `Set ${label} style and take it to air`,
			options: [
				{
					type: 'dropdown',
					id: 'style',
					label: `${label} Style`,
					choices: family.wipeStyles,
					default: family.wipeStyles[0]?.id ?? 0,
				},
			],
			callback: async (event) => {
				// Convert the style by the family offset (both H4K and 0617 use 0, so the dropdown id is the sent value)
				const styleValue = Number(event.options.style) - (family.wipeStyleOffset ?? 0)
				// H4K only: arm the write check so the 0x0120 read-back logs which WipeN actually received it
				if (family.queryAllOnConnect) self.armWipeCheck(n, styleValue)
				await self.sendProtocolField('transition', `Wipe${n}`, styleValue, `${label} Style`)
				if (keyVal !== undefined) {
					await self.sendToDevice('KEY_PRESS', { keyVal })
				} else {
					self.log('warn', `[Transition] ${label} has no key value; style was set but not taken to air`)
				}
				// H4K only: read back 0x0120 (the log prints Wipe1/2/3 on the device) to verify the style reached the right channel
				if (family.queryAllOnConnect) {
					self.schedule(() => void self.queryTransitionOnce(), 250)
				}
			},
		}
	}

	// Combined action: pick a wipe channel + style in one go (only for families with mergeWipeStyleAction, e.g. H4K;
	// 0617/0605 keep their trans_wipe1~4 action list completely unchanged)
	if (family.mergeWipeStyleAction) {
		actions['trans_wipe_style'] = {
			name: 'Transition WIPE Style (Wipe1/2/3)',
			description: 'Set the style of a WIPE channel, optionally pressing that WIPE key to switch to it',
			options: [
				{
					type: 'dropdown',
					id: 'wipe',
					label: 'Wipe Channel',
					choices: Array.from({ length: family.wipeCount }, (_, i) => ({ id: i + 1, label: `WIPE${i + 1}` })),
					default: 1,
				},
				{
					type: 'dropdown',
					id: 'style',
					label: 'Style',
					choices: family.wipeStyles,
					default: family.wipeStyles[0]?.id ?? 0,
				},
				{
					type: 'checkbox',
					id: 'press',
					label: 'Also press the WIPE key (switch to this channel)',
					default: true,
				},
			],
			callback: async (event) => {
				const n = Number(event.options.wipe)
				const styleValue = Number(event.options.style) - (family.wipeStyleOffset ?? 0)
				const press = Boolean(event.options.press)
				if (family.queryAllOnConnect) self.armWipeCheck(n, styleValue)
				await self.sendProtocolField('transition', `Wipe${n}`, styleValue, `WIPE${n} Style`)
				if (press) {
					const keyVal = keys.wipe[n - 1]
					if (keyVal !== undefined) await self.sendToDevice('KEY_PRESS', { keyVal })
				}
				// H4K only: read back 0x0120 to verify the style reached the right channel
				if (family.queryAllOnConnect) {
					self.schedule(() => void self.queryTransitionOnce(), 250)
				}
			},
		}
	}

	// MIX / DIP / FREEZE: 0x0010 keys (combined into one dropdown)
	actions['trans_effect'] = {
		name: 'Transition MIX / DIP / FREEZE',
		description: 'Press MIX / DIP / FREEZE',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Effect',
				choices: [
					{ id: 'mix', label: 'MIX' },
					{ id: 'dip', label: 'DIP' },
					{ id: 'freeze', label: 'FREEZE' },
				],
				default: 'mix',
			},
		],
		callback: async (event) => {
			const keyVal = resolveKeyId(self, event.options.value)
			if (keyVal !== undefined) await self.sendToDevice('KEY_PRESS', { keyVal })
		},
	}

	// Direction: Normal / Invert / Flip-Flop (combined into one dropdown)
	actions['trans_direction'] = {
		name: 'Transition Direction',
		description: 'Set transition direction: Normal / Invert / Flip-Flop',
		options: [{ type: 'dropdown', id: 'value', label: 'Direction', choices: DIRECTION_CHOICES, default: 0 }],
		callback: async (event) => {
			await self.sendProtocolField('transition', 'Direction', Number(event.options.value), 'Transition Direction')
		},
	}
}

// ==================== AUDIO ====================
/**
 * Audio (0x0050) fields:
 *   0=Mute,1=AllAfv,2=Reset,3=MasterEn,4=MasterVol,5=EarEn,6=EarVol,7=EarSoc,
 *   8~31=IN1~IN6 (EN/VOL/AFV/DELAY per channel),
 *   32=MicXlrMode(0:MIC/MIX,1:XLR), 33~37=MIC1(EN/Guitar/PreGain/VOL/Delay), 38~42=MIC2,
 *   43~45=XLR(EN/VOL/Delay), 46~48=LineIn(EN/VOL/Delay)
 * Note: XLR and MIC1~2 are mutually exclusive, controlled by MicXlrMode(32).
 */
const AUDIO_IN_CHOICES = [
	{ id: 1, label: 'IN1' },
	{ id: 2, label: 'IN2' },
	{ id: 3, label: 'IN3' },
	{ id: 4, label: 'IN4' },
	{ id: 5, label: 'IN5' },
	{ id: 6, label: 'IN6' },
]
const AUDIO_MIC_CHOICES = [
	{ id: 1, label: 'MIC1' },
	{ id: 2, label: 'MIC2' },
]
const AUDIO_MIC_XLR_MODE_CHOICES = [
	{ id: 0, label: 'MIC' },
	{ id: 1, label: 'XLR' },
]

/** Register the AUDIO group actions (set command 0x0050) - each action controls one function only */
function registerAudioActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	const family = self.getProtocolFamilyInfo()

	// 1) Channel-less switches (registered when the protocol has the field; XLR/LineIn are 0617 only)
	const simpleToggles: Array<[string, string, string]> = [
		['audio_all_afv', 'Audio All AFV', 'AllAfv'],
		['audio_master_en', 'Audio PGM OUT Enable', 'MasterEnable'],
		['audio_ear_en', 'Audio Earphone Enable', 'EarEnable'],
		['audio_xlr_en', 'Audio XLR Enable', 'XlrEnable'],
		['audio_line_en', 'Audio Line In Enable', 'LineInEnable'],
	]
	for (const [id, label, field] of simpleToggles) {
		if (!supports(self, 'audio', field)) continue
		// H4K has no All AFV (the protocol field stays in the layout, only the UI is not registered)
		if (id === 'audio_all_afv' && family.hideAllAfvAction) continue
		actions[id] = {
			name: label,
			description: label,
			options: [onoff('value', 'State')],
			callback: async (event) => {
				await self.sendProtocolField('audio', field, Number(event.options.value), label)
			},
		}
	}

	// 2) Channel-less sliders (Volume / Delay)
	const simpleSliders: Array<[string, string, string, number, number, number]> = [
		['audio_master_vol', 'Audio PGM OUT Volume', 'MasterVolume', 0, 72, 50],
		['audio_ear_vol', 'Audio Earphone Volume', 'EarVolume', 0, 72, 50],
		['audio_xlr_vol', 'Audio XLR Volume', 'XlrVolume', 0, 72, 50],
		['audio_xlr_delay', 'Audio XLR Delay', 'XlrDelay', 0, 100, 0],
		['audio_line_vol', 'Audio Line In Volume', 'LineInVolume', 0, 72, 50],
		['audio_line_delay', 'Audio Line In Delay', 'LineInDelay', 0, 100, 0],
	]
	for (const [id, label, field, min, max, def] of simpleSliders) {
		if (!supports(self, 'audio', field)) continue
		actions[id] = {
			name: label,
			description: label,
			options: [slider('value', 'Value', min, max, def)],
			callback: async (event) => {
				await self.sendProtocolField('audio', field, Number(event.options.value), label)
			},
		}
	}

	// 3) Earphone source (dropdown): input count follows the family; MIC / Line In only when supported
	//    - 0617: PGM + IN1~6 + MIC1/2 + Line In (10 entries, same as before)
	//    - H4K : PGM + IN1~4 + MIC1/2 (no IN5/IN6, no Line In)
	if (supports(self, 'audio', 'EarSource')) {
		const earSources: Array<{ id: number; label: string }> = [{ id: 0, label: 'PGM' }]
		for (let n = 1; n <= family.inputCount; n++) earSources.push({ id: n, label: `IN${n}` })
		if (supports(self, 'audio', 'Mic1Enable')) earSources.push({ id: 7, label: 'MIC1' })
		if (supports(self, 'audio', 'Mic2Enable')) earSources.push({ id: 8, label: 'MIC2' })
		if (supports(self, 'audio', 'LineInEnable')) earSources.push({ id: 9, label: 'Line In' })
		actions['audio_ear_src'] = {
			name: 'Audio Earphone Source',
			description: 'Select the earphone source',
			options: [{ type: 'dropdown', id: 'value', label: 'Source', choices: earSources, default: 0 }],
			callback: async (event) => {
				await self.sendProtocolField('audio', 'EarSource', Number(event.options.value), 'Earphone Source')
			},
		}
	}

	// 4) IN channels: one action per function (with a channel dropdown); channel count follows the family (0617=6 / H4K=4)
	const inFns: Array<[string, string, boolean, number, number, number, string]> = [
		['audio_in_en', 'Audio IN Enable', true, 0, 0, 0, 'Enable'],
		['audio_in_vol', 'Audio IN Volume', false, 0, 72, 50, 'Volume'],
		['audio_in_afv', 'Audio IN AFV', true, 0, 0, 0, 'Afv'],
		['audio_in_delay', 'Audio IN Delay', false, 0, 100, 0, 'Delay'],
	]
	for (const [id, label, isToggle, min, max, def, suffix] of inFns) {
		if (!supports(self, 'audio', `In1${suffix}`)) continue
		actions[id] = {
			name: label,
			description: `${label} (IN1~IN${family.inputCount})`,
			options: [
				{
					type: 'dropdown',
					id: 'channel',
					label: 'Channel',
					choices: AUDIO_IN_CHOICES.slice(0, family.inputCount),
					default: 1,
				},
				isToggle ? onoff('value', 'State') : slider('value', 'Value', min, max, def),
			],
			callback: async (event) => {
				const ch = Number(event.options.channel)
				await self.sendProtocolField('audio', `In${ch}${suffix}`, Number(event.options.value), label)
			},
		}
	}

	// 5) MIC1~2: one action per function (Guitar/PreGain/Delay are 0617 only)
	const micFns: Array<[string, string, boolean, number, number, number, string]> = [
		['audio_mic_en', 'Audio MIC Enable', true, 0, 0, 0, 'Enable'],
		['audio_mic_guitar', 'Audio MIC Guitar', true, 0, 0, 0, 'Guitar'],
		['audio_mic_pregain', 'Audio MIC Pre-Gain', false, 0, 14, 0, 'PreGain'],
		['audio_mic_vol', 'Audio MIC Volume', false, 0, 72, 50, 'Volume'],
		['audio_mic_delay', 'Audio MIC Delay', false, 0, 100, 0, 'Delay'],
	]
	for (const [id, label, isToggle, min, max, def, suffix] of micFns) {
		if (!supports(self, 'audio', `Mic1${suffix}`)) continue
		actions[id] = {
			name: label,
			description: `${label} (MIC1~2)`,
			options: [
				{ type: 'dropdown', id: 'channel', label: 'Channel', choices: AUDIO_MIC_CHOICES, default: 1 },
				isToggle ? onoff('value', 'State') : slider('value', 'Value', min, max, def),
			],
			callback: async (event) => {
				const ch = Number(event.options.channel)
				await self.sendProtocolField('audio', `Mic${ch}${suffix}`, Number(event.options.value), label)
			},
		}
	}

	// 6) Reset (not offered on H4K: hideAudioResetAction; the Reset field stays in the layout)
	if (supports(self, 'audio', 'Reset') && !family.hideAudioResetAction) {
		actions['audio_reset'] = {
			name: 'Audio Reset',
			description: 'Reset all audio settings to defaults',
			options: [],
			callback: async () => {
				await self.sendProtocolField('audio', 'Reset', 1, 'Audio Reset')
			},
		}
	}

	// 7) MIC / XLR mode (XLR and MIC are mutually exclusive; 0617 only)
	if (supports(self, 'audio', 'MicXlrMode')) {
		actions['audio_mic_xlr_mode'] = {
			name: 'Audio MIC / XLR Mode',
			description: 'Select the MIC/XLR mode',
			options: [{ type: 'dropdown', id: 'value', label: 'Mode', choices: AUDIO_MIC_XLR_MODE_CHOICES, default: 0 }],
			callback: async (event) => {
				await self.sendProtocolField('audio', 'MicXlrMode', Number(event.options.value), 'MIC/XLR Mode')
			},
		}
	}
}

// ==================== TBAR ====================
/** T-Bar move (0x0010, Param_Vaild=1 T_Bar_val; UI scale 0~500) */
function registerTbarActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	actions['tbar_move'] = {
		name: 'T-Bar Move',
		description: 'Move T-Bar Up/Down by step (display scale 0-500)',
		options: [
			{
				type: 'dropdown',
				id: 'direction',
				label: 'Direction',
				choices: [
					{ id: 1, label: 'Up' },
					{ id: 0, label: 'Down' },
				],
				default: 1,
			},
			slider('step', 'Step', 1, 500, 10),
			{
				type: 'static-text',
				id: 'current',
				label: 'Current Value (0-500)',
				value: 'The current T-Bar position is available as the variable tbar_value',
			},
		],
		callback: async (event) => {
			await self.moveTBar(Number(event.options.direction), Number(event.options.step))
		},
	}
}

// ==================== Entry point ====================
export function UpdateActions(self: ModuleInstance): void {
	const actions: CompanionActionDefinitions = {}

	// Source selection (PGM1~N / PVW1~N + Pattern): counts follow the protocol family (0617=6 / H4K=4)
	const family = self.getProtocolFamilyInfo()
	const keys = family.keyMap
	const sourceChoices: Array<{ id: string; label: string }> = []
	keys.pgm.forEach((_, i) => sourceChoices.push({ id: `pgm${i + 1}`, label: `PGM${i + 1}` }))
	keys.pgmPattern.forEach((_, i) => sourceChoices.push({ id: `pgm_pattern${i + 1}`, label: `PGM PATTERN${i + 1}` }))
	keys.pvw.forEach((_, i) => sourceChoices.push({ id: `pvw${i + 1}`, label: `PVW${i + 1}` }))
	keys.pvwPattern.forEach((_, i) => sourceChoices.push({ id: `pvw_pattern${i + 1}`, label: `PVW PATTERN${i + 1}` }))
	actions['set_source'] = {
		name: 'Source (PGM / PVW)',
		description: 'Select PGM/PVW source (with pattern)',
		options: [{ type: 'dropdown', id: 'source', label: 'Source', choices: sourceChoices, default: 'pgm1' }],
		callback: async (event) => {
			const keyVal = resolveKeyId(self, event.options.source)
			if (keyVal === undefined) {
				self.log('warn', `Unknown source key: ${event.options.source}`)
				return
			}
			const success = await self.sendToDevice('KEY_PRESS', { keyVal })
			if (!success) {
				self.log('warn', `Failed to send source key ${keyVal}`)
			}
		},
	}

	// Key Type is read-only (0x0130): no 0x0030 write is needed, switching layers just presses the PIP/LUMA/CHROMA/DSK KEY / ON AIR keys

	// Switch: Stream 1~N (requires the Codec command; H4K has no streaming)
	if (family.hasStream && keys.stream.length > 0) {
		actions['switch_stream'] = {
			name: 'Switch Stream',
			description: 'Toggle Stream 1 / 2 / 3',
			options: [
				{
					type: 'dropdown',
					id: 'value',
					label: 'Stream',
					choices: keys.stream.map((_, i) => ({ id: `stream${i + 1}`, label: `Stream ${i + 1}` })),
					default: 'stream1',
				},
			],
			callback: async (event) => {
				const keyVal = resolveKeyId(self, event.options.value)
				if (keyVal !== undefined) await self.sendToDevice('KEY_PRESS', { keyVal })
			},
		}
	}

	// Switch: CUT / AUTO / FTB / MUTE (combined into one dropdown)
	actions['switch_transition'] = {
		name: 'Switch CUT / AUTO / FTB / MUTE',
		description: 'Press CUT / AUTO / FTB / MUTE',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Key',
				choices: [
					{ id: 'cut', label: 'CUT' },
					{ id: 'auto', label: 'AUTO' },
					{ id: 'ftb', label: 'FTB' },
					{ id: 'mute', label: 'MUTE' },
				],
				default: 'cut',
			},
		],
		callback: async (event) => {
			const keyVal = resolveKeyId(self, event.options.value)
			if (keyVal !== undefined) await self.sendToDevice('KEY_PRESS', { keyVal })
		},
	}

	// H4K: send the KEY / ON AIR key directly (0x0010 keytype) - equivalent to the device panel key.
	// The device reports its own 0x0130 (active key layer), so no 0x0030 write is needed.
	if (family.keyPressFormat === 'keytype') {
		actions['key_module_press'] = {
			name: 'Key Module Press (KEY / ON AIR)',
			description: 'Press the KEY or ON AIR key of PIP/LUMA/CHROMA/DSK directly',
			options: [
				{
					type: 'dropdown',
					id: 'value',
					label: 'Key',
					choices: [
						{ id: 'pip', label: 'PIP KEY' },
						{ id: 'pip_on_air', label: 'PIP ON AIR' },
						{ id: 'luma', label: 'LUMA KEY' },
						{ id: 'luma_on_air', label: 'LUMA ON AIR' },
						{ id: 'chroma', label: 'CHROMA KEY' },
						{ id: 'chroma_on_air', label: 'CHROMA ON AIR' },
						{ id: 'dsk', label: 'DSK KEY' },
						{ id: 'dsk_on_air', label: 'DSK ON AIR' },
					],
					default: 'pip',
				},
			],
			callback: async (event) => {
				const keyVal = resolveKeyId(self, event.options.value)
				if (keyVal === undefined) return
				await self.sendToDevice('KEY_PRESS', { keyVal })
				// Pressing a PIP/LUMA/CHROMA KEY/ON AIR key: re-query 0x0130 shortly after to calibrate the highlight
				const k = self.getProtocolFamilyInfo().keyMap
				const pipKeys = [k.pip, k.pipOnAir]
				const lumaKeys = [k.luma, k.lumaOnAir]
				const chromaKeys = [k.chroma, k.chromaOnAir]
				if (pipKeys.includes(keyVal)) self.markKeyTypeLocal(0)
				else if (lumaKeys.includes(keyVal)) self.markKeyTypeLocal(1)
				else if (chromaKeys.includes(keyVal)) self.markKeyTypeLocal(2)
			},
		}
	}

	// PIP1~N: layer count follows the protocol family (0617=3 / H4K=1)
	for (let n = 1; n <= family.pipCount; n++) {
		registerPipActions(self, actions, n, `pip${n}`)
	}

	// LUMA (0x0031)
	registerLumaActions(self, actions)

	// CHROMA (0x0032)
	registerChromaActions(self, actions)

	// DSK (0x0040)
	registerDskActions(self, actions)

	// LOGO (0x0041)
	registerLogoActions(self, actions)

	// TRANSITIONS (0x0020 / 0x0010)
	registerTransitionActions(self, actions)

	// AUDIO (0x0050)
	registerAudioActions(self, actions)

	// TBAR (0x0010)
	registerTbarActions(self, actions)

	// Network scan (system)
	actions['scan_devices'] = {
		name: 'Scan Network for Devices',
		description: 'Discover devices on the local network via UDP broadcast',
		options: [],
		callback: async () => {
			const devices = await self.scanForDevices()
			self.log('info', `Scan complete - Found ${devices.length} device(s)`)
		},
	}

	// Filter by the current product profile: actions outside its feature set are not registered
	const profile = self.getDeviceProfile()
	for (const id of Object.keys(actions)) {
		if (!isIdEnabled(profile, id)) delete actions[id]
	}

	// Uniform wrapper: runs each action with its own flash key (L7: isolated per async context)
	for (const id of Object.keys(actions)) {
		const def = actions[id]
		if (!def) continue
		const orig = def.callback
		def.callback = async (event, context) => {
			return self.runWithFlashKey(flashKeyFor(id, event.options), async () => orig(event, context))
		}
	}

	self.setRegisteredActionIds(Object.keys(actions))
	self.setActionDefinitions(actions)
}

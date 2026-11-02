import type { ModuleInstance } from './main.js'
import {
	CompanionActionDefinitions,
	CompanionInputFieldDropdown,
	CompanionInputFieldNumber,
} from '@companion-module/base'
import { isIdEnabled } from './devices/index.js'
import { flashKeyFor } from './commandHandler.js'

/** Adjust 动作的选项类型（滑块 + 下拉） */
type AdjustOption = CompanionInputFieldNumber | CompanionInputFieldDropdown

/**
 * 判断当前协议是否包含某命令的全部字段。
 * 例：H4K 的 LUMA 没有 FillSource/Invert，依赖这些字段的动作就不注册。
 */
function supports(self: ModuleInstance, cmdKey: string, ...fields: string[]): boolean {
	return fields.every((f) => self.hasField(cmdKey, f))
}

/** 当前协议的键源 / PIP 源下拉项（各协议枚举起点不同） */
const keySourcesOf = (self: ModuleInstance) => self.getProtocolFamilyInfo().keySources
const pipSourcesOf = (self: ModuleInstance) => self.getProtocolFamilyInfo().pipSources

/** 取源下拉默认值（IN1 对应的 id） */
function defaultSourceId(sources: Array<{ id: number; label: string }>): number {
	return sources.find((s) => s.label === 'IN1')?.id ?? sources[0]?.id ?? 0
}

// ==================== 共用选项 ====================

// 状态：OFF / KEY / ON AIR / KEY&ON AIR（PIP/LUMA/CHROMA/DSK/LOGO 通用）
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

// 键源 / PIP 源的下拉项由协议族提供（见 devices/protocols.ts 的 keySources / pipSources）

// CHROMA Key Color Type（0617：0-4）
const CHROMA_KEY_TYPE_CHOICES = [
	{ id: 0, label: 'Green' },
	{ id: 1, label: 'Blue' },
	{ id: 2, label: 'Red' },
	{ id: 3, label: 'Custom' },
	{ id: 4, label: 'Fetch' },
]

// H4K Key Color Type：只有 RED / GREEN / BLUE（0/1/2）
const H4K_KEY_COLOR_CHOICES = [
	{ id: 0, label: 'Red' },
	{ id: 1, label: 'Green' },
	{ id: 2, label: 'Blue' },
]

// Transition Direction（0-2）
const DIRECTION_CHOICES = [
	{ id: 0, label: 'Normal' },
	{ id: 1, label: 'Invert' },
	{ id: 2, label: 'Flip-Flop' },
]

// Wipe 样式下拉由协议族提供（0617：0~10；H4K：0~27，下发值 = 下拉 id，0 = 第一张图）

/** 生成一个滑块(number)选项 */
function slider(id: string, label: string, min: number, max: number, def: number): CompanionInputFieldNumber {
	return { type: 'number', id, label: `${label} (${min}-${max})`, min, max, default: def, range: true, step: 1 }
}

/** 生成一个 ON/OFF 下拉选项 */
function onoff(id: string, label: string, def = 0) {
	return { type: 'dropdown' as const, id, label, choices: ONOFF_CHOICES, default: def }
}

// ==================== PIP1~3 ====================
/**
 * PIP1~3（设置指令 0x0033/0x0034/0x0035）
 * 字段：0=Status, 1=Source, 2=Size, 3=PosX, 4=PosY
 */
function registerPipActions(
	self: ModuleInstance,
	actions: CompanionActionDefinitions,
	n: number,
	commandKey: string,
): void {
	const tag = `PIP${n}`
	// 状态（KEY / ON AIR / KEY&ON AIR / OFF 整合为一个下拉）
	actions[`pip${n}_status`] = {
		name: `${tag} Status`,
		description: `Set ${tag} status`,
		options: [{ type: 'dropdown', id: 'status', label: 'Status', choices: STATUS_CHOICES, default: 0 }],
		callback: async (event) => {
			const status = Number(event.options.status)
			// H4K：PIP / LUMA / CHROMA 互斥，先关掉其他两层（旧族直接返回）
			if (status >= 1) await self.closeOtherKeys(commandKey)
			await self.sendProtocolField(commandKey, 'Status', status, `${tag} Status`)
			if (status >= 1) self.markKeyTypeLocal(0)
		},
	}
	// 参数（Source/Size/PosX/PosY 整合为一个动作；H4K 追加 Border 相关字段）
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
			// H4K Border 字段（0617 无这些字段，会自动跳过）；旧按钮遗留的 -1 按 0 处理
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
 * LUMA（0x0031）
 * 字段：0=Tie,1=Status,2=FillSource,3=KeySource,4=Size,5=PosX,6=PosY,7=Clip,8=Gain,
 *       9=Invert,10=MaskEnable,11=MaskLeft,12=MaskTop,13=MaskRight,14=MaskBottom
 */
function registerLumaActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	actions['luma_status'] = {
		name: 'LUMA Status',
		description: 'Set LUMA status',
		options: [{ type: 'dropdown', id: 'status', label: 'Status', choices: STATUS_CHOICES, default: 0 }],
		callback: async (event) => {
			const status = Number(event.options.status)
			// H4K：PIP / LUMA / CHROMA 互斥，先关掉其他两层（旧族直接返回）
			if (status >= 1) await self.closeOtherKeys('luma')
			await self.sendProtocolField('luma', 'Status', status, 'LUMA Status')
			if (status >= 1) self.markKeyTypeLocal(1)
		},
	}
	if (supports(self, 'luma', 'FillSource')) {
		actions['luma_fill_source'] = {
			name: 'LUMA Fill Source',
			description: 'LUMA Fill Source (0-7)',
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
		description: 'LUMA Key Source (0-7)',
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
	// 参数选项按协议字段动态拼装（例：H4K 无 Gain；H4K 有 Tolerance/Clip 范围）
	// H4K 的 Clip / Tolerance 是枚举（不是 0-100 数值），且有 Mask 0~100%
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
	// H4K 字段
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
	// H4K 的 Mask 每个边都是 0~100%
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
			// H4K 字段（0617 无这些字段，会自动跳过）；旧按钮遗留的 -1 按 0 处理
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
		description: 'LUMA Mask enable + Left/Top/Right/Bottom (0~100%，左侧不能大于右侧)',
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
			// 文档约束：左侧不能大于右侧，顶部不能大于底部
			await self.sendProtocolField('luma', 'MaskLeft', Math.min(left, right), 'LUMA Mask Left')
			await self.sendProtocolField('luma', 'MaskTop', Math.min(top, bottom), 'LUMA Mask Top')
			await self.sendProtocolField('luma', 'MaskRight', Math.max(right, left), 'LUMA Mask Right')
			await self.sendProtocolField('luma', 'MaskBottom', Math.max(bottom, top), 'LUMA Mask Bottom')
		},
	}
}

// ==================== CHROMA ====================
/**
 * CHROMA（0x0032）
 * 字段：0=Status,1=KeySource,2=KeyType,6=Size,7=PosX,8=PosY,9=Similarity,10=Smooth,
 *       11=Spill,12=Opacity,13=Brightness,14=Contrast,15=Saturation,
 *       16=MaskEnable,17=MaskLeft,18=MaskTop,19=MaskRight,20=MaskBottom
 */
function registerChromaActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	// H4K：Key Color Type 只有 Red/Green/Blue、Size 0~100、有 Tolerance/Softness/Clip/Correction/Mask
	const isH4K = !!self.getProtocolCommands()['keyType']
	actions['chroma_status'] = {
		name: 'CHROMA Status',
		description: 'Set CHROMA status',
		options: [{ type: 'dropdown', id: 'status', label: 'Status', choices: STATUS_CHOICES, default: 0 }],
		callback: async (event) => {
			const status = Number(event.options.status)
			// H4K：PIP / LUMA / CHROMA 互斥，先关掉其他两层（旧族直接返回）
			if (status >= 1) await self.closeOtherKeys('chroma')
			await self.sendProtocolField('chroma', 'Status', status, 'CHROMA Status')
			if (status >= 1) self.markKeyTypeLocal(2)
		},
	}
	actions['chroma_key_source'] = {
		name: 'CHROMA Key Source',
		description: 'CHROMA Key Source (0-7)',
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
	// 参数选项按协议字段动态拼装（例：H4K 无 Spill/Opacity，但有 Angle/Tolerance/Softness/Clip/Correction/Color 调整）
	const chromaAdjustOptions: AdjustOption[] = []
	if (supports(self, 'chroma', 'Size'))
		chromaAdjustOptions.push(
			isH4K ? slider('size', 'Zoom Size', 0, 100, 100) : slider('size', 'Zoom Size', 12, 100, 100),
		)
	if (supports(self, 'chroma', 'PosX')) chromaAdjustOptions.push(slider('posx', 'Key PositionX', 0, 100, 50))
	if (supports(self, 'chroma', 'PosY')) chromaAdjustOptions.push(slider('posy', 'Key PositionY', 0, 100, 50))
	// 0617（Similarity/Smooth/Spill/Opacity 为它自己的字段）
	if (supports(self, 'chroma', 'Similarity')) chromaAdjustOptions.push(slider('similarity', 'Similarity', 0, 100, 50))
	if (supports(self, 'chroma', 'Smooth')) chromaAdjustOptions.push(slider('smooth', 'Smoothness', 0, 255, 0))
	if (supports(self, 'chroma', 'Spill')) chromaAdjustOptions.push(slider('spill', 'Spill', 0, 255, 0))
	if (supports(self, 'chroma', 'Opacity')) chromaAdjustOptions.push(slider('opacity', 'Opacity', 0, 100, 100))
	if (supports(self, 'chroma', 'Brightness')) chromaAdjustOptions.push(slider('brightness', 'Brightness', 0, 100, 50))
	if (supports(self, 'chroma', 'Contrast')) chromaAdjustOptions.push(slider('contrast', 'Contrast', 0, 100, 50))
	if (supports(self, 'chroma', 'Saturation')) chromaAdjustOptions.push(slider('saturation', 'Saturation', 0, 100, 50))
	// H4K 字段（Angle / Tolerance / Softness / Clip 范围 / Correction / RGB）
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
			'CHROMA Size/Pos/Angle/Tolerance/Softness/Clip/Correction/RGB/Mask（0617：Similarity/Smooth/Spill/Opacity）',
		options: chromaAdjustOptions,
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolField('chroma', 'Size', Number(o.size), 'CHROMA Zoom Size')
			await self.sendProtocolField('chroma', 'PosX', Number(o.posx), 'CHROMA Key PositionX')
			await self.sendProtocolField('chroma', 'PosY', Number(o.posy), 'CHROMA Key PositionY')
			// 0617 字段（H4K 无这些字段，会自动跳过）
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
			// H4K 字段（0617 无这些字段，会自动跳过）
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
			// Clip_Min ≤ Clip_Max（先算好再统一下发）
			// H4K 字段（0617 无这些字段，会自动跳过）；旧按钮遗留的 -1 按 0 处理
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
		description: 'CHROMA Mask enable + Left/Top/Right/Bottom (0~100%，左侧不能大于右侧)',
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
 * DSK（0x0040）
 * 字段：0=Tie,1=Status,2=FillSource,3=KeySource,4=Clip,5=Gain,6=Invert,
 *       7=MaskEnable,8=MaskLeft,9=MaskTop,10=MaskRight,11=MaskBottom
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
			description: 'DSK Fill Source (0-7)',
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
		description: 'DSK Key Source (0-7)',
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
 * LOGO（0x0041）
 * 字段：0=Status,1=Select,2=PosX,3=PosY,4=Size,5=Opacity
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
		description: 'LOGO Select (0-7)',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Logo',
				choices: Array.from({ length: self.getProtocolFamilyInfo().logoCount }, (_, n) => ({
					id: n,
					label: `Logo ${n}`,
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
 * 0x0020：0~3=Wipe1~4 样式, 5=Direction(0:Normal/1:Invert/2:Flip-Flop)
 * 0x0010 按键：Wipe1~4=27~30, MIX=31, DIP=32
 */
function registerTransitionActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	// WIPE 数量与键值按协议族决定（0617：4 个；H4K：3 个）
	const family = self.getProtocolFamilyInfo()
	const keys = family.keyMap
	for (let n = 1; n <= family.wipeCount; n++) {
		const keyVal = keys.wipe[n - 1]
		const label = `WIPE${n}`
		actions[`trans_wipe${n}`] = {
			name: `Transition ${label}`,
			description: `Set ${label} style (0x0020, No.${n}) and press ${label} (0x0010, Key_val=${keyVal})`,
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
				// 样式值按协议族偏移换算（H4K / 0617 的 offset 均为 0，下拉 id 就是下发的样式值）
				const styleValue = Number(event.options.style) - (family.wipeStyleOffset ?? 0)
				// 仅 H4K：登记写后校验，回读 0x0120 时日志会打印实际落到哪个 WipeN
				if (family.queryAllOnConnect) self.armWipeCheck(n, styleValue)
				await self.sendProtocolField('transition', `Wipe${n}`, styleValue, `${label} Style`)
				await self.sendToDevice('KEY_PRESS', { keyVal })
				// 仅 H4K：回读 0x0120（日志会打印设备侧 Wipe1/2/3），用于核对样式是否落到正确通道
				if (family.queryAllOnConnect) {
					setTimeout(() => {
						void self.queryTransitionOnce()
					}, 250)
				}
			},
		}
	}

	// 合并动作：一次选择 WIPE 通道 + 样式（仅 H4K 等开启 mergeWipeStyleAction 的族；
	// 0617/0605 保持原有的 trans_wipe1~4 动作列表完全不变）
	if (family.mergeWipeStyleAction) {
		actions['trans_wipe_style'] = {
			name: 'Transition WIPE Style (Wipe1/2/3)',
			description: '设置指定 WIPE 通道的样式（0x0020），可选是否同时按下该 WIPE 键切换通道',
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
					label: '同时按下 WIPE 键（切换到该通道）',
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
				// 仅 H4K：回读 0x0120 核对样式是否落到正确通道
				if (family.queryAllOnConnect) {
					setTimeout(() => {
						void self.queryTransitionOnce()
					}, 250)
				}
			},
		}
	}

	// MIX / DIP / FREEZE：0x0010 按键（整合为一个下拉）
	actions['trans_effect'] = {
		name: 'Transition MIX / DIP',
		description: `Press MIX (${keys.mix}) / DIP (${keys.dip}) / FREEZE (${keys.freeze})`,
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Effect',
				choices: [
					{ id: keys.mix, label: 'MIX' },
					{ id: keys.dip, label: 'DIP' },
					{ id: keys.freeze, label: 'FREEZE' },
				],
				default: keys.mix,
			},
		],
		callback: async (event) => {
			await self.sendToDevice('KEY_PRESS', { keyVal: Number(event.options.value) })
		},
	}

	// Direction：Normal / Invert / Flip-Flop（整合为一个下拉）
	actions['trans_direction'] = {
		name: 'Transition Direction',
		description: 'Set Direction (0x0020): Normal / Invert / Flip-Flop',
		options: [{ type: 'dropdown', id: 'value', label: 'Direction', choices: DIRECTION_CHOICES, default: 0 }],
		callback: async (event) => {
			await self.sendProtocolField('transition', 'Direction', Number(event.options.value), 'Transition Direction')
		},
	}
}

// ==================== AUDIO ====================
/**
 * Audio（0x0050）字段：
 *   0=Mute,1=AllAfv,2=Reset,3=MasterEn,4=MasterVol,5=EarEn,6=EarVol,7=EarSoc,
 *   8~31=IN1~IN6（每通道 EN/VOL/AFV/DELAY 共 4 项）,
 *   32=MicXlrMode(0:MIC/MIX,1:XLR), 33~37=MIC1(EN/Guitar/PreGain/VOL/Delay), 38~42=MIC2,
 *   43~45=XLR(EN/VOL/Delay), 46~48=LineIn(EN/VOL/Delay)
 * 注：XLR 与 MIC1~2 互斥，由 MicXlrMode(32) 控制。
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

/** 注册 AUDIO 分组动作（设置指令 0x0050）—— 每个动作只负责一个功能 */
function registerAudioActions(self: ModuleInstance, actions: CompanionActionDefinitions): void {
	const family = self.getProtocolFamilyInfo()

	// 1) 无通道的开关（按协议字段存在性注册，XLR/LineIn 仅 0617 支持）
	const simpleToggles: Array<[string, string, string]> = [
		['audio_all_afv', 'Audio All AFV', 'AllAfv'],
		['audio_master_en', 'Audio PGM OUT Enable', 'MasterEnable'],
		['audio_ear_en', 'Audio Earphone Enable', 'EarEnable'],
		['audio_xlr_en', 'Audio XLR Enable', 'XlrEnable'],
		['audio_line_en', 'Audio Line In Enable', 'LineInEnable'],
	]
	for (const [id, label, field] of simpleToggles) {
		if (!supports(self, 'audio', field)) continue
		// H4K 无 ALL AFV 功能（协议字段仍在布局中，只是不注册 UI）
		if (id === 'audio_all_afv' && family.hideAllAfvAction) continue
		actions[id] = {
			name: label,
			description: `${label} (0x0050 ${field})`,
			options: [onoff('value', 'State')],
			callback: async (event) => {
				await self.sendProtocolField('audio', field, Number(event.options.value), label)
			},
		}
	}

	// 2) 无通道的滑块（Volume / Delay）
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
			description: `${label} (0x0050 ${field})`,
			options: [slider('value', 'Value', min, max, def)],
			callback: async (event) => {
				await self.sendProtocolField('audio', field, Number(event.options.value), label)
			},
		}
	}

	// 3) Earphone 源（下拉）：IN 路数按协议族裁剪，MIC / Line In 仅在协议支持时提供
	//    - 0617：PGM + IN1~6 + MIC1/2 + Line In（10 项，与原行为一致）
	//    - H4K ：PGM + IN1~4 + MIC1/2（无 IN5/IN6、无 Line In）
	if (supports(self, 'audio', 'EarSource')) {
		const earSources: Array<{ id: number; label: string }> = [{ id: 0, label: 'PGM' }]
		for (let n = 1; n <= family.inputCount; n++) earSources.push({ id: n, label: `IN${n}` })
		if (supports(self, 'audio', 'Mic1Enable')) earSources.push({ id: 7, label: 'MIC1' })
		if (supports(self, 'audio', 'Mic2Enable')) earSources.push({ id: 8, label: 'MIC2' })
		if (supports(self, 'audio', 'LineInEnable')) earSources.push({ id: 9, label: 'Line In' })
		actions['audio_ear_src'] = {
			name: 'Audio Earphone Source',
			description: 'Earphone Source (0x0050 EarSource)',
			options: [{ type: 'dropdown', id: 'value', label: 'Source', choices: earSources, default: 0 }],
			callback: async (event) => {
				await self.sendProtocolField('audio', 'EarSource', Number(event.options.value), 'Earphone Source')
			},
		}
	}

	// 4) IN 通道：每个功能一个动作（含通道下拉），通道数按协议族（0617=6 / H4K=4）
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
			description: `${label} (0x0050, IN1~${family.inputCount})`,
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

	// 5) MIC1~2：每个功能一个动作（Guitar/PreGain/Delay 仅 0617 支持）
	const micFns: Array<[string, string, boolean, number, number, number, string]> = [
		['audio_mic_en', 'Audio MIC Enable', true, 0, 0, 0, 'Enable'],
		['audio_mic_guitar', 'Audio MIC Guitar', true, 0, 0, 0, 'Guitar'],
		['audio_mic_pregate', 'Audio MIC Pre-Gain', false, 0, 14, 0, 'PreGain'],
		['audio_mic_vol', 'Audio MIC Volume', false, 0, 72, 50, 'Volume'],
		['audio_mic_delay', 'Audio MIC Delay', false, 0, 100, 0, 'Delay'],
	]
	for (const [id, label, isToggle, min, max, def, suffix] of micFns) {
		if (!supports(self, 'audio', `Mic1${suffix}`)) continue
		actions[id] = {
			name: label,
			description: `${label} (0x0050, MIC1~2)`,
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

	// 6) Reset（H4K 不提供：hideAudioResetAction，协议字段 Reset 仍保留在布局中）
	if (supports(self, 'audio', 'Reset') && !family.hideAudioResetAction) {
		actions['audio_reset'] = {
			name: 'Audio Reset',
			description: 'AUDIO_RESET (0x0050 Reset)',
			options: [],
			callback: async () => {
				await self.sendProtocolField('audio', 'Reset', 1, 'Audio Reset')
			},
		}
	}

	// 7) MIC / XLR 模式（XLR 与 MIC 互斥，仅 0617 支持）
	if (supports(self, 'audio', 'MicXlrMode')) {
		actions['audio_mic_xlr_mode'] = {
			name: 'Audio MIC / XLR Mode',
			description: 'MIC_XLR_MODE (0x0050 MicXlrMode): MIC(0) / XLR(1)',
			options: [{ type: 'dropdown', id: 'value', label: 'Mode', choices: AUDIO_MIC_XLR_MODE_CHOICES, default: 0 }],
			callback: async (event) => {
				await self.sendProtocolField('audio', 'MicXlrMode', Number(event.options.value), 'MIC/XLR Mode')
			},
		}
	}
}

// ==================== TBAR ====================
/** T-Bar 移动（0x0010, Param_Vaild=1 T_Bar_val；对外刻度 0~500） */
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

// ==================== 主入口 ====================
export function UpdateActions(self: ModuleInstance): void {
	const actions: CompanionActionDefinitions = {}

	// 源选择（PGM1~N / PVW1~N + Pattern）：键值与路数按协议族决定（0617=6 路 / H4K=4 路）
	const family = self.getProtocolFamilyInfo()
	const keys = family.keyMap
	const sourceChoices: Array<{ id: number; label: string }> = []
	keys.pgm.forEach((keyVal, i) => sourceChoices.push({ id: keyVal, label: `PGM${i + 1}` }))
	keys.pgmPattern.forEach((keyVal, i) => sourceChoices.push({ id: keyVal, label: `PGM PATTERN${i + 1}` }))
	keys.pvw.forEach((keyVal, i) => sourceChoices.push({ id: keyVal, label: `PVW${i + 1}` }))
	keys.pvwPattern.forEach((keyVal, i) => sourceChoices.push({ id: keyVal, label: `PVW PATTERN${i + 1}` }))
	actions['set_source'] = {
		name: 'Source (PGM / PVW)',
		description: 'Select PGM/PVW source (with pattern)',
		options: [{ type: 'dropdown', id: 'source', label: 'Source', choices: sourceChoices, default: 1 }],
		callback: async (event) => {
			const keyVal = Number(event.options.source)
			const success = await self.sendToDevice('KEY_PRESS', { keyVal })
			if (!success) {
				self.log('warn', `Failed to send source key ${keyVal}`)
			}
		},
	}

	// Key Type 只读（0x0130）：不需要 0x0030 写入，切 Key 层直接用 PIP/LUMA/CHROMA/DSK 的 Key / ON AIR 按键

	// Switch：Stream 1~N（依赖 Codec 指令，H4K 无此能力）
	if (family.hasStream && keys.stream.length > 0) {
		actions['switch_stream'] = {
			name: 'Switch Stream',
			description: 'Toggle Stream 1 / 2 / 3',
			options: [
				{
					type: 'dropdown',
					id: 'value',
					label: 'Stream',
					choices: keys.stream.map((keyVal, i) => ({ id: keyVal, label: `Stream ${i + 1}` })),
					default: keys.stream[0],
				},
			],
			callback: async (event) => {
				await self.sendToDevice('KEY_PRESS', { keyVal: Number(event.options.value) })
			},
		}
	}

	// Switch：CUT / AUTO / FTB / MUTE（整合为一个下拉）
	actions['switch_transition'] = {
		name: 'Switch CUT / AUTO / FTB / MUTE',
		description: 'Press CUT / AUTO / FTB / MUTE',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Key',
				choices: [
					{ id: keys.cut, label: 'CUT' },
					{ id: keys.auto, label: 'AUTO' },
					{ id: keys.ftb, label: 'FTB' },
					{ id: keys.mute, label: 'MUTE' },
				],
				default: keys.cut,
			},
		],
		callback: async (event) => {
			await self.sendToDevice('KEY_PRESS', { keyVal: Number(event.options.value) })
		},
	}

	// H4K：直接发 Key / ON AIR 按键（0x0010 keytype）—— 与设备面板按键等效，
	// 设备会自己把自己的 0x0130（当前激活 Key 层）上报上来，不需要 0x0030 写入
	if (family.keyPressFormat === 'keytype') {
		actions['key_module_press'] = {
			name: 'Key Module Press (KEY / ON AIR)',
			description: '直接按 PIP/LUMA/CHROMA/DSK 的 KEY 或 ON AIR 键',
			options: [
				{
					type: 'dropdown',
					id: 'value',
					label: 'Key',
					choices: [
						{ id: keys.pip, label: 'PIP KEY' },
						{ id: keys.pipOnAir, label: 'PIP ON AIR' },
						{ id: keys.luma, label: 'LUMA KEY' },
						{ id: keys.lumaOnAir, label: 'LUMA ON AIR' },
						{ id: keys.chroma, label: 'CHROMA KEY' },
						{ id: keys.chromaOnAir, label: 'CHROMA ON AIR' },
						{ id: keys.dsk, label: 'DSK KEY' },
						{ id: keys.dskOnAir, label: 'DSK ON AIR' },
					],
					default: keys.pip,
				},
			],
			callback: async (event) => {
				const keyVal = Number(event.options.value)
				await self.sendToDevice('KEY_PRESS', { keyVal })
				// 按的是 PIP/LUMA/CHROMA 的 KEY/ON AIR 键时，稍后回查 0x0130 校准高亮
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

	// PIP1~N：路数按协议族（0617=3 / H4K=1）
	for (let n = 1; n <= family.pipCount; n++) {
		registerPipActions(self, actions, n, `pip${n}`)
	}

	// LUMA（0x0031）
	registerLumaActions(self, actions)

	// CHROMA（0x0032）
	registerChromaActions(self, actions)

	// DSK（0x0040）
	registerDskActions(self, actions)

	// LOGO（0x0041）
	registerLogoActions(self, actions)

	// TRANSITIONS（0x0020 / 0x0010）
	registerTransitionActions(self, actions)

	// AUDIO（0x0050）
	registerAudioActions(self, actions)

	// TBAR（0x0010）
	registerTbarActions(self, actions)

	// 网络扫描（系统）
	actions['scan_devices'] = {
		name: 'Scan Network for Devices',
		description: 'Discover devices on the local network via UDP broadcast',
		options: [],
		callback: async () => {
			const devices = await self.scanForDevices()
			self.log('info', `Scan complete - Found ${devices.length} device(s)`)
		},
	}

	// 按当前产品档案裁剪：不属于该产品功能集的动作不注册
	const profile = self.getDeviceProfile()
	for (const id of Object.keys(actions)) {
		if (!isIdEnabled(profile, id)) delete actions[id]
	}

	// 统一包裹：执行时记录本次动作的唯一 key（供“仅被点击按钮”的橙色执行反馈）
	for (const id of Object.keys(actions)) {
		const def = actions[id]
		if (!def) continue
		const orig = def.callback
		def.callback = async (event, context) => {
			self.pendingFlashKey = flashKeyFor(id, event.options)
			try {
				return await orig(event, context)
			} finally {
				self.pendingFlashKey = undefined
			}
		}
	}

	self.setRegisteredActionIds(Object.keys(actions))
	self.setActionDefinitions(actions)
}

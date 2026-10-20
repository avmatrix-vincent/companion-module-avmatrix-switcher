import type { ModuleInstance } from './main.js'
import { CompanionActionDefinitions, CompanionInputFieldNumber } from '@companion-module/base'
import {
	PGM_KEY_VALUES,
	PVW_KEY_VALUES,
	PATTERN_KEY_VALUES,
	TRANSITION_KEY_VALUES,
	FUNCTION_KEY_VALUES,
	flashKeyFor,
} from './commandHandler.js'

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

// Key 源的源（0-7）：0=BLACK,1~6=IN1~6,7=Color Bar
const SOURCE_CHOICES = [
	{ id: 0, label: 'BLACK' },
	{ id: 1, label: 'IN1' },
	{ id: 2, label: 'IN2' },
	{ id: 3, label: 'IN3' },
	{ id: 4, label: 'IN4' },
	{ id: 5, label: 'IN5' },
	{ id: 6, label: 'IN6' },
	{ id: 7, label: 'Color Bar' },
]

// PIP 源（0-11）：0=BLACK,1~6=IN1~6,7=Color Bar,8=Color 1,9=Color 2,10=PAT1,11=PAT2
const PIP_SOURCE_CHOICES = [
	{ id: 0, label: 'BLACK' },
	{ id: 1, label: 'IN1' },
	{ id: 2, label: 'IN2' },
	{ id: 3, label: 'IN3' },
	{ id: 4, label: 'IN4' },
	{ id: 5, label: 'IN5' },
	{ id: 6, label: 'IN6' },
	{ id: 7, label: 'Color Bar' },
	{ id: 8, label: 'Color 1' },
	{ id: 9, label: 'Color 2' },
	{ id: 10, label: 'PAT1' },
	{ id: 11, label: 'PAT2' },
]

// CHROMA Key Color Type（0-4）
const CHROMA_KEY_TYPE_CHOICES = [
	{ id: 0, label: 'Green' },
	{ id: 1, label: 'Blue' },
	{ id: 2, label: 'Red' },
	{ id: 3, label: 'Custom' },
	{ id: 4, label: 'Fetch' },
]

// Transition Direction（0-2）
const DIRECTION_CHOICES = [
	{ id: 0, label: 'Normal' },
	{ id: 1, label: 'Invert' },
	{ id: 2, label: 'Flip-Flop' },
]

// Wipe 样式（0-10）
const WIPE_STYLE_CHOICES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((n) => ({ id: n, label: `Wipe Style ${n}` }))

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
			await self.sendProtocolSet(commandKey, 0, Number(event.options.status), `${tag} Status`)
		},
	}
	// 参数（Source/Size/PosX/PosY 整合为一个动作）
	actions[`pip${n}_adjust`] = {
		name: `${tag} Adjust`,
		description: `${tag} Source / Size / PosX / PosY`,
		options: [
			{ type: 'dropdown', id: 'source', label: 'Source', choices: PIP_SOURCE_CHOICES, default: 1 },
			slider('size', 'Size', 12, 100, 100),
			slider('posx', 'PosX', 0, 100, 50),
			slider('posy', 'PosY', 0, 100, 50),
		],
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolSet(commandKey, 1, Number(o.source), `${tag} Source`)
			await self.sendProtocolSet(commandKey, 2, Number(o.size), `${tag} Size`)
			await self.sendProtocolSet(commandKey, 3, Number(o.posx), `${tag} PosX`)
			await self.sendProtocolSet(commandKey, 4, Number(o.posy), `${tag} PosY`)
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
			await self.sendProtocolSet('luma', 1, Number(event.options.status), 'LUMA Status')
		},
	}
	actions['luma_fill_source'] = {
		name: 'LUMA Fill Source',
		description: 'LUMA Fill Source (0-7)',
		options: [{ type: 'dropdown', id: 'value', label: 'Source', choices: SOURCE_CHOICES, default: 1 }],
		callback: async (event) => {
			await self.sendProtocolSet('luma', 2, Number(event.options.value), 'LUMA Fill Source')
		},
	}
	actions['luma_key_source'] = {
		name: 'LUMA Key Source',
		description: 'LUMA Key Source (0-7)',
		options: [{ type: 'dropdown', id: 'value', label: 'Source', choices: SOURCE_CHOICES, default: 1 }],
		callback: async (event) => {
			await self.sendProtocolSet('luma', 3, Number(event.options.value), 'LUMA Key Source')
		},
	}
	actions['luma_adjust'] = {
		name: 'LUMA Adjust',
		description: 'LUMA Zoom Size / Key PosX / Key PosY / Clip / Gain',
		options: [
			slider('size', 'Zoom Size', 12, 100, 100),
			slider('posx', 'Key PositionX', 0, 100, 50),
			slider('posy', 'Key PositionY', 0, 100, 50),
			slider('clip', 'Clip', 0, 100, 50),
			slider('gain', 'Gain', 0, 100, 50),
		],
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolSet('luma', 4, Number(o.size), 'LUMA Zoom Size')
			await self.sendProtocolSet('luma', 5, Number(o.posx), 'LUMA Key PositionX')
			await self.sendProtocolSet('luma', 6, Number(o.posy), 'LUMA Key PositionY')
			await self.sendProtocolSet('luma', 7, Number(o.clip), 'LUMA Clip')
			await self.sendProtocolSet('luma', 8, Number(o.gain), 'LUMA Gain')
		},
	}
	actions['luma_invert'] = {
		name: 'LUMA Invert Key',
		description: 'LUMA Invert Key (0:OFF / 1:ON)',
		options: [onoff('value', 'State')],
		callback: async (event) => {
			await self.sendProtocolSet('luma', 9, Number(event.options.value), 'LUMA Invert Key')
		},
	}
	actions['luma_mask'] = {
		name: 'LUMA Mask',
		description: 'LUMA Mask enable + Left/Top/Right/Bottom',
		options: [
			onoff('enable', 'Enable'),
			slider('left', 'Mask Left', 0, 50, 0),
			slider('top', 'Mask Top', 0, 50, 0),
			slider('right', 'Mask Right', 50, 100, 100),
			slider('bottom', 'Mask Bottom', 50, 100, 100),
		],
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolSet('luma', 10, Number(o.enable), 'LUMA Mask Enable')
			await self.sendProtocolSet('luma', 11, Number(o.left), 'LUMA Mask Left')
			await self.sendProtocolSet('luma', 12, Number(o.top), 'LUMA Mask Top')
			await self.sendProtocolSet('luma', 13, Number(o.right), 'LUMA Mask Right')
			await self.sendProtocolSet('luma', 14, Number(o.bottom), 'LUMA Mask Bottom')
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
	actions['chroma_status'] = {
		name: 'CHROMA Status',
		description: 'Set CHROMA status',
		options: [{ type: 'dropdown', id: 'status', label: 'Status', choices: STATUS_CHOICES, default: 0 }],
		callback: async (event) => {
			await self.sendProtocolSet('chroma', 0, Number(event.options.status), 'CHROMA Status')
		},
	}
	actions['chroma_key_source'] = {
		name: 'CHROMA Key Source',
		description: 'CHROMA Key Source (0-7)',
		options: [{ type: 'dropdown', id: 'value', label: 'Source', choices: SOURCE_CHOICES, default: 1 }],
		callback: async (event) => {
			await self.sendProtocolSet('chroma', 1, Number(event.options.value), 'CHROMA Key Source')
		},
	}
	actions['chroma_key_type'] = {
		name: 'CHROMA Key Color Type',
		description: 'CHROMA Key Color Type (Green/Blue/Red/Custom/Fetch)',
		options: [{ type: 'dropdown', id: 'value', label: 'Type', choices: CHROMA_KEY_TYPE_CHOICES, default: 0 }],
		callback: async (event) => {
			await self.sendProtocolSet('chroma', 2, Number(event.options.value), 'CHROMA Key Color Type')
		},
	}
	actions['chroma_adjust'] = {
		name: 'CHROMA Adjust',
		description: 'CHROMA Size/PosX/PosY/Similarity/Smoothness/Spill/Opacity/Brightness/Contrast/Saturation',
		options: [
			slider('size', 'Zoom Size', 12, 100, 100),
			slider('posx', 'Key PositionX', 0, 100, 50),
			slider('posy', 'Key PositionY', 0, 100, 50),
			slider('similarity', 'Similarity', 0, 100, 50),
			slider('smooth', 'Smoothness', 0, 255, 0),
			slider('spill', 'Spill', 0, 255, 0),
			slider('opacity', 'Opacity', 0, 100, 100),
			slider('brightness', 'Brightness', 0, 100, 50),
			slider('contrast', 'Contrast', 0, 100, 50),
			slider('saturation', 'Saturation', 0, 100, 50),
		],
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolSet('chroma', 6, Number(o.size), 'CHROMA Zoom Size')
			await self.sendProtocolSet('chroma', 7, Number(o.posx), 'CHROMA Key PositionX')
			await self.sendProtocolSet('chroma', 8, Number(o.posy), 'CHROMA Key PositionY')
			await self.sendProtocolSet('chroma', 9, Number(o.similarity), 'CHROMA Similarity')
			await self.sendProtocolSet('chroma', 10, Number(o.smooth), 'CHROMA Smoothness')
			await self.sendProtocolSet('chroma', 11, Number(o.spill), 'CHROMA Spill')
			await self.sendProtocolSet('chroma', 12, Number(o.opacity), 'CHROMA Opacity')
			await self.sendProtocolSet('chroma', 13, Number(o.brightness), 'CHROMA Brightness')
			await self.sendProtocolSet('chroma', 14, Number(o.contrast), 'CHROMA Contrast')
			await self.sendProtocolSet('chroma', 15, Number(o.saturation), 'CHROMA Saturation')
		},
	}
	actions['chroma_mask'] = {
		name: 'CHROMA Mask',
		description: 'CHROMA Mask enable + Left/Top/Right/Bottom',
		options: [
			onoff('enable', 'Enable'),
			slider('left', 'Mask Left', 0, 50, 0),
			slider('top', 'Mask Top', 0, 50, 0),
			slider('right', 'Mask Right', 50, 100, 100),
			slider('bottom', 'Mask Bottom', 50, 100, 100),
		],
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolSet('chroma', 16, Number(o.enable), 'CHROMA Mask Enable')
			await self.sendProtocolSet('chroma', 17, Number(o.left), 'CHROMA Mask Left')
			await self.sendProtocolSet('chroma', 18, Number(o.top), 'CHROMA Mask Top')
			await self.sendProtocolSet('chroma', 19, Number(o.right), 'CHROMA Mask Right')
			await self.sendProtocolSet('chroma', 20, Number(o.bottom), 'CHROMA Mask Bottom')
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
			await self.sendProtocolSet('dsk', 1, Number(event.options.status), 'DSK Status')
		},
	}
	actions['dsk_fill_source'] = {
		name: 'DSK Fill Source',
		description: 'DSK Fill Source (0-7)',
		options: [{ type: 'dropdown', id: 'value', label: 'Source', choices: SOURCE_CHOICES, default: 1 }],
		callback: async (event) => {
			await self.sendProtocolSet('dsk', 2, Number(event.options.value), 'DSK Fill Source')
		},
	}
	actions['dsk_key_source'] = {
		name: 'DSK Key Source',
		description: 'DSK Key Source (0-7)',
		options: [{ type: 'dropdown', id: 'value', label: 'Source', choices: SOURCE_CHOICES, default: 1 }],
		callback: async (event) => {
			await self.sendProtocolSet('dsk', 3, Number(event.options.value), 'DSK Key Source')
		},
	}
	actions['dsk_tie'] = {
		name: 'DSK Tie',
		description: 'DSK Tie (0:OFF / 1:ON)',
		options: [onoff('value', 'State')],
		callback: async (event) => {
			await self.sendProtocolSet('dsk', 0, Number(event.options.value), 'DSK Tie')
		},
	}
	actions['dsk_adjust'] = {
		name: 'DSK Adjust',
		description: 'DSK Clip / Gain',
		options: [slider('clip', 'Clip', 0, 100, 50), slider('gain', 'Gain', 0, 100, 50)],
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolSet('dsk', 4, Number(o.clip), 'DSK Clip')
			await self.sendProtocolSet('dsk', 5, Number(o.gain), 'DSK Gain')
		},
	}
	actions['dsk_invert'] = {
		name: 'DSK Invert',
		description: 'DSK Invert (0:OFF / 1:ON)',
		options: [onoff('value', 'State')],
		callback: async (event) => {
			await self.sendProtocolSet('dsk', 6, Number(event.options.value), 'DSK Invert')
		},
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
			await self.sendProtocolSet('dsk', 7, Number(o.enable), 'DSK Mask Enable')
			await self.sendProtocolSet('dsk', 8, Number(o.left), 'DSK Mask Left')
			await self.sendProtocolSet('dsk', 9, Number(o.top), 'DSK Mask Top')
			await self.sendProtocolSet('dsk', 10, Number(o.right), 'DSK Mask Right')
			await self.sendProtocolSet('dsk', 11, Number(o.bottom), 'DSK Mask Bottom')
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
			await self.sendProtocolSet('logo', 0, Number(event.options.status), 'LOGO Status')
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
				choices: [0, 1, 2, 3, 4, 5, 6, 7].map((n) => ({ id: n, label: `Logo ${n}` })),
				default: 0,
			},
		],
		callback: async (event) => {
			await self.sendProtocolSet('logo', 1, Number(event.options.value), 'LOGO Select')
		},
	}
	actions['logo_adjust'] = {
		name: 'LOGO Adjust',
		description: 'LOGO PosX/PosY/Size/Opacity',
		options: [
			slider('posx', 'PositionX', 0, 100, 50),
			slider('posy', 'PositionY', 0, 100, 50),
			slider('size', 'Size', 5, 20, 10),
			slider('opacity', 'Opacity', 20, 100, 100),
		],
		callback: async (event) => {
			const o = event.options
			await self.sendProtocolSet('logo', 2, Number(o.posx), 'LOGO PositionX')
			await self.sendProtocolSet('logo', 3, Number(o.posy), 'LOGO PositionY')
			await self.sendProtocolSet('logo', 4, Number(o.size), 'LOGO Size')
			await self.sendProtocolSet('logo', 5, Number(o.opacity), 'LOGO Opacity')
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
	const wipes: Array<[number, number, string]> = [
		[1, 27, 'WIPE1'],
		[2, 28, 'WIPE2'],
		[3, 29, 'WIPE3'],
		[4, 30, 'WIPE4'],
	]
	for (const [n, keyVal, label] of wipes) {
		actions[`trans_wipe${n}`] = {
			name: `Transition ${label}`,
			description: `Set ${label} style (0x0020, NO.${n - 1}) and press ${label} (0x0010, Key_val=${keyVal})`,
			options: [
				{ type: 'dropdown', id: 'style', label: `${label} Style (0-10)`, choices: WIPE_STYLE_CHOICES, default: 0 },
			],
			callback: async (event) => {
				await self.sendProtocolSet('transition', n - 1, Number(event.options.style), `${label} Style`)
				await self.sendToDevice('KEY_PRESS', { keyVal })
			},
		}
	}

	// MIX / DIP：0x0010 按键（整合为一个下拉）
	actions['trans_effect'] = {
		name: 'Transition MIX / DIP',
		description: 'Press MIX (31) or DIP (32)',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Effect',
				choices: [
					{ id: TRANSITION_KEY_VALUES['MIX'], label: 'MIX' },
					{ id: TRANSITION_KEY_VALUES['DIP'], label: 'DIP' },
					{ id: TRANSITION_KEY_VALUES['FREEZE'], label: 'FREEZE' },
				],
				default: TRANSITION_KEY_VALUES['MIX'],
			},
		],
		callback: async (event) => {
			await self.sendToDevice('KEY_PRESS', { keyVal: Number(event.options.value) })
		},
	}

	// Direction：Normal / Invert / Flip-Flop（整合为一个下拉）
	actions['trans_direction'] = {
		name: 'Transition Direction',
		description: 'Set Direction (0x0020, NO.5): Normal / Invert / Flip-Flop',
		options: [{ type: 'dropdown', id: 'value', label: 'Direction', choices: DIRECTION_CHOICES, default: 0 }],
		callback: async (event) => {
			await self.sendProtocolSet('transition', 5, Number(event.options.value), 'Transition Direction')
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
const AUDIO_EAR_SOURCE_CHOICES = [
	{ id: 0, label: 'PGM' },
	{ id: 1, label: 'IN1' },
	{ id: 2, label: 'IN2' },
	{ id: 3, label: 'IN3' },
	{ id: 4, label: 'IN4' },
	{ id: 5, label: 'IN5' },
	{ id: 6, label: 'IN6' },
	{ id: 7, label: 'MIC1' },
	{ id: 8, label: 'MIC2' },
	{ id: 9, label: 'Line In' },
]
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
	// 1) 无通道的开关（Enable / AFV / Mode 等）
	const simpleToggles: Array<[string, string, number]> = [
		['audio_all_afv', 'Audio All AFV', 1],
		['audio_master_en', 'Audio PGM OUT Enable', 3],
		['audio_ear_en', 'Audio Earphone Enable', 5],
		['audio_xlr_en', 'Audio XLR Enable', 43],
		['audio_line_en', 'Audio Line In Enable', 46],
	]
	for (const [id, label, field] of simpleToggles) {
		actions[id] = {
			name: label,
			description: `${label} (0x0050 NO.${field})`,
			options: [onoff('value', 'State')],
			callback: async (event) => {
				await self.sendProtocolSet('audio', field, Number(event.options.value), label)
			},
		}
	}

	// 2) 无通道的滑块（Volume / Delay）
	const simpleSliders: Array<[string, string, number, number, number, number]> = [
		['audio_master_vol', 'Audio PGM OUT Volume', 4, 0, 72, 50],
		['audio_ear_vol', 'Audio Earphone Volume', 6, 0, 72, 50],
		['audio_xlr_vol', 'Audio XLR Volume', 44, 0, 72, 50],
		['audio_xlr_delay', 'Audio XLR Delay', 45, 0, 100, 0],
		['audio_line_vol', 'Audio Line In Volume', 47, 0, 72, 50],
		['audio_line_delay', 'Audio Line In Delay', 48, 0, 100, 0],
	]
	for (const [id, label, field, min, max, def] of simpleSliders) {
		actions[id] = {
			name: label,
			description: `${label} (0x0050 NO.${field})`,
			options: [slider('value', 'Value', min, max, def)],
			callback: async (event) => {
				await self.sendProtocolSet('audio', field, Number(event.options.value), label)
			},
		}
	}

	// 3) Earphone 源（下拉）
	actions['audio_ear_src'] = {
		name: 'Audio Earphone Source',
		description: 'Earphone Source (0x0050 NO.7)',
		options: [{ type: 'dropdown', id: 'value', label: 'Source', choices: AUDIO_EAR_SOURCE_CHOICES, default: 0 }],
		callback: async (event) => {
			await self.sendProtocolSet('audio', 7, Number(event.options.value), 'Earphone Source')
		},
	}

	// 4) IN1~6：每个功能一个动作（含通道下拉）；base = 8 + (ch-1)*4
	const inFns: Array<[string, string, number, boolean, number, number, number]> = [
		['audio_in_en', 'Audio IN Enable', 0, true, 0, 0, 0],
		['audio_in_vol', 'Audio IN Volume', 1, false, 0, 72, 50],
		['audio_in_afv', 'Audio IN AFV', 2, true, 0, 0, 0],
		['audio_in_delay', 'Audio IN Delay', 3, false, 0, 100, 0],
	]
	for (const [id, label, off, isToggle, min, max, def] of inFns) {
		actions[id] = {
			name: label,
			description: `${label} (0x0050, IN1~6)`,
			options: [
				{ type: 'dropdown', id: 'channel', label: 'Channel', choices: AUDIO_IN_CHOICES, default: 1 },
				isToggle ? onoff('value', 'State') : slider('value', 'Value', min, max, def),
			],
			callback: async (event) => {
				const base = 8 + (Number(event.options.channel) - 1) * 4
				await self.sendProtocolSet('audio', base + off, Number(event.options.value), label)
			},
		}
	}

	// 5) MIC1~2：每个功能一个动作（含通道下拉）；base = 33 + (ch-1)*5
	const micFns: Array<[string, string, number, boolean, number, number, number]> = [
		['audio_mic_en', 'Audio MIC Enable', 0, true, 0, 0, 0],
		['audio_mic_guitar', 'Audio MIC Guitar', 1, true, 0, 0, 0],
		['audio_mic_pregate', 'Audio MIC Pre-Gain', 2, false, 0, 14, 0],
		['audio_mic_vol', 'Audio MIC Volume', 3, false, 0, 72, 50],
		['audio_mic_delay', 'Audio MIC Delay', 4, false, 0, 100, 0],
	]
	for (const [id, label, off, isToggle, min, max, def] of micFns) {
		actions[id] = {
			name: label,
			description: `${label} (0x0050, MIC1~2)`,
			options: [
				{ type: 'dropdown', id: 'channel', label: 'Channel', choices: AUDIO_MIC_CHOICES, default: 1 },
				isToggle ? onoff('value', 'State') : slider('value', 'Value', min, max, def),
			],
			callback: async (event) => {
				const base = 33 + (Number(event.options.channel) - 1) * 5
				await self.sendProtocolSet('audio', base + off, Number(event.options.value), label)
			},
		}
	}

	// 6) Reset
	actions['audio_reset'] = {
		name: 'Audio Reset',
		description: 'AUDIO_RESET (0x0050 NO.2)',
		options: [],
		callback: async () => {
			await self.sendProtocolSet('audio', 2, 1, 'Audio Reset')
		},
	}

	// 7) MIC / XLR 模式（XLR 与 MIC1~2 互斥）
	actions['audio_mic_xlr_mode'] = {
		name: 'Audio MIC / XLR Mode',
		description: 'MIC_XLR_MODE (0x0050 NO.32): MIC(0) / XLR(1)',
		options: [{ type: 'dropdown', id: 'value', label: 'Mode', choices: AUDIO_MIC_XLR_MODE_CHOICES, default: 0 }],
		callback: async (event) => {
			await self.sendProtocolSet('audio', 32, Number(event.options.value), 'MIC/XLR Mode')
		},
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
			{ type: 'static-text', id: 'current', label: 'Current Value (0-500)', value: '$(self:tbar_value)' },
		],
		callback: async (event) => {
			await self.moveTBar(Number(event.options.direction), Number(event.options.step))
		},
	}
}

// ==================== 主入口 ====================
export function UpdateActions(self: ModuleInstance): void {
	const actions: CompanionActionDefinitions = {}

	// 源选择（PGM1~6 / PVW1~6 + Pattern）：整合为一个动作，用下拉选
	const sourceChoices: Array<{ id: number; label: string }> = []
	for (const [label, keyVal] of Object.entries(PGM_KEY_VALUES)) {
		sourceChoices.push({ id: keyVal, label })
	}
	for (const [label, keyVal] of Object.entries(PATTERN_KEY_VALUES)) {
		if (label.startsWith('PGM_')) sourceChoices.push({ id: keyVal, label: label.replace('_', ' ') })
	}
	for (const [label, keyVal] of Object.entries(PVW_KEY_VALUES)) {
		sourceChoices.push({ id: keyVal, label })
	}
	for (const [label, keyVal] of Object.entries(PATTERN_KEY_VALUES)) {
		if (label.startsWith('PVW_')) sourceChoices.push({ id: keyVal, label: label.replace('_', ' ') })
	}
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

	// Switch：Stream 1/2/3（整合为一个下拉）
	actions['switch_stream'] = {
		name: 'Switch Stream',
		description: 'Toggle Stream 1 / 2 / 3',
		options: [
			{
				type: 'dropdown',
				id: 'value',
				label: 'Stream',
				choices: [
					{ id: FUNCTION_KEY_VALUES.STREAM1, label: 'Stream 1' },
					{ id: FUNCTION_KEY_VALUES.STREAM2, label: 'Stream 2' },
					{ id: FUNCTION_KEY_VALUES.STREAM3, label: 'Stream 3' },
				],
				default: FUNCTION_KEY_VALUES.STREAM1,
			},
		],
		callback: async (event) => {
			await self.sendToDevice('KEY_PRESS', { keyVal: Number(event.options.value) })
		},
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
					{ id: TRANSITION_KEY_VALUES.CUT, label: 'CUT' },
					{ id: TRANSITION_KEY_VALUES.AUTO, label: 'AUTO' },
					{ id: TRANSITION_KEY_VALUES.FTB, label: 'FTB' },
					{ id: FUNCTION_KEY_VALUES.MUTE, label: 'MUTE' },
				],
				default: TRANSITION_KEY_VALUES.CUT,
			},
		],
		callback: async (event) => {
			await self.sendToDevice('KEY_PRESS', { keyVal: Number(event.options.value) })
		},
	}

	// PIP1 / PIP2 / PIP3
	registerPipActions(self, actions, 1, 'pip1')
	registerPipActions(self, actions, 2, 'pip2')
	registerPipActions(self, actions, 3, 'pip3')

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

	self.setActionDefinitions(actions)
}

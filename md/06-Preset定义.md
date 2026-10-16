# Companion 模块开发 - Preset 定义 (API 2.x)

> 文档来源：https://companion.free/for-developers/module-development/connection-basics/presets/

## 概述

Presets（预设）是现成按钮的描述，呈现在 Buttons 页面的 Presets 标签中。用户可以拖放预设到按钮网格，快速构建配置。

## API 调用

### setPresetDefinitions(structure, presets)

添加预设时调用此方法。与定义动作和反馈类似，但预设需要单独提供结构（structure）和定义（presets），以减少重复并提供更多灵活性。

**重要**：确保在 `setActionDefinitions()` 和 `setFeedbackDefinitions()` 之后调用，否则变量替换不完整，会报缺失定义的错误。

## 预设类型

目前只有一种预设类型，未来计划引入更多：

- `simple` - Simple Button Preset

API 1.x 中的 `text` 类型已被新的 structure 对象替代。

## Simple Button Preset 定义

最小示例：

```javascript
const presets = {}
presets['my_first_preset'] = {
  type: 'simple',
  name: 'My button', // 悬停时显示的名称，也用于搜索
  style: {
    text: '$(my-module:some-variable)', // 可使用模块变量
    size: 'auto',
    color: 0xffffff, // 或 combineRgb(255, 255, 255)
    bgcolor: 0x000000, // 或 combineRgb(0, 0, 0)
  },
  steps: [
    {
      down: [
        {
          actionId: 'my-action',
          options: {
            brightness: 100,
          },
        },
      ],
      up: [],
    },
  ],
  feedbacks: [],
}

const structure = [
  {
    id: 'section-main',
    name: 'Main',
    definitions: ['my_first_preset'],
  },
]

this.setPresetDefinitions(structure, presets)
```

### Actions（步骤）

`steps` 属性描述按钮按下时的行为。典型情况只有一个步骤（普通按钮行为）。

定义第二个步骤可制作锁定按钮（latching button）。默认每次释放按钮会切换到下一步，可通过设置 `options: { stepAutoProgress: false }` 禁用。

支持旋转编码器预设：

```ts
steps: [
  {
    down: [],
    up: [],
    rotate_left: [
      {
        actionId: 'my-action',
        options: {},
      },
    ],
    rotate_right: [
      {
        actionId: 'my-action',
        options: {},
      },
    ],
  },
],
```

持续时间组（带延迟）：

```ts
steps: [
  {
    down: [],
    up: [],
    2000: {
      options: { runWhileHeld: true },
      actions: [
        {
          actionId: 'my-action',
          options: {},
        },
      ],
    },
  },
],
```

每个动作可设置 `delay` 属性（毫秒），模拟 internal:wait 行为。

### Feedbacks

```javascript
feedbacks: [
  {
    feedbackId: 'my-feedback',
    options: {
      channel: 1,
    },
    style: {
      // 仅对 boolean feedback 有效
      color: combineRgb(255, 255, 255),
      bgcolor: combineRgb(255, 0, 0),
    },
  },
]
```

### Local Variables

设置按钮本地变量：

```javascript
localVariables: [
  {
    variableType: 'simple',
    variableName: 'input',
    startupValue: 1,
  },
],
```

然后可在预设中引用：`$(local:output)`

### 使用表达式

API 2.0 起，大多数字段支持表达式：

```javascript
feedbacks: [
  {
    feedbackId: 'my-feedback',
    options: {
      value1: 1,                                    // 普通值
      value2: { isExpression: false, value: 1 },    // 显式包装
      value3: { isExpression: true, value: '$(local:output) + 1' }, // 表达式
    },
    style: { ... },
  },
]
```

## Preset Structure

API 2.0 要求单独提供 structure 定义 UI 布局。

### 基础结构

```javascript
const structure = [
  {
    id: 'section-main',
    name: 'Main',
    description: 'The things you usually want',
    definitions: ['my_first_preset', 'my_second_preset'],
  },
]
```

### Simple Groups

在 section 内使用分组：

```javascript
const structure = [
  {
    id: 'section-main',
    name: 'Main',
    definitions: [
      {
        id: 'main-1',
        type: 'simple',
        name: 'First',
        description: 'A second line of text',
        presets: ['my_first_preset', 'my_second_preset'],
      },
      {
        id: 'main-2',
        type: 'simple',
        name: '',
        presets: ['my_first_preset', 'my_third_preset'],
      },
    ],
  },
]
```

### Template Groups

对于大量几乎相同的预设（如每个输入+输出组合），使用模板组减少数据量：

```javascript
{
  id: 'route_to_1',
  name: 'To Output 1',
  type: 'template',
  presets: ['route_preset'],
  localVariables: [
    {
      variableType: 'simple',
      variableName: 'output',
      startupValue: 1,
    },
  ],
}
```

## 代码示例

```typescript
import type { ModuleInstance } from './main.js'
import { CompanionPresetDefinitions, combineRgb } from '@companion-module/base'

export function UpdatePresets(self: ModuleInstance): void {
  const presets: CompanionPresetDefinitions = {}
  presets['mylabel'] = {
    type: 'button',
    category: 'Group One',
    name: 'Name',
    style: {
      text: 'My first Preset button',
      size: 'auto',
      color: combineRgb(255, 255, 255),
      bgcolor: combineRgb(0, 0, 0),
      show_topbar: false,
    },
    steps: [],
    feedbacks: [],
  }

  self.setPresetDefinitions(presets)
}
```

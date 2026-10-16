# Companion 模块开发 - Feedback 定义

> 文档来源：https://companion.free/for-developers/module-development/connection-basics/feedbacks/

## 概述

Feedbacks（反馈）允许 Companion 反映设备状态，使用该状态进行按钮样式变更、设置变量或触发其他行为。

## API 调用

### setFeedbackDefinitions(definitions)

在 `init()` 中调用以定义模块支持的反馈列表。也可以在其他时间调用更新列表。

**注意**：不要频繁调用，更新列表有性能开销。

### checkFeedbacks(...), checkAllFeedbacks() & checkFeedbacksById(...)

当反馈结果预期会改变时，调用这些方法通知 Companion 重新运行回调：

- `this.checkFeedbacks('your-feedback-id', 'another-feedback')` - 指定反馈 ID
- `this.checkAllFeedbacks()` - 所有反馈（API 2.0 替代无参的 checkFeedbacks）
- `this.checkFeedbacksById('abc', 'def')` - 按订阅 ID 触发，更精确控制

## 反馈类型

Companion 目前支持三种反馈类型：

### Boolean feedbacks（推荐）

回调返回简单的 true 或 false 值。用户可在触发器中使用，作为反馈逻辑的一部分，或应用自定义按钮样式。

### Value feedbacks

API 1.13 (Companion 4.1) 新增。用户可将此反馈的值存储到本地变量中。可返回任何 JSON 对象、数组或原始值。

### Advanced feedbacks（不推荐）

返回部分按钮样式属性，覆盖用户定义的样式。大多数情况下不再推荐使用，建议迁移为 boolean feedbacks。旧版本 Companion 中这是唯一可用的反馈类型。

## 反馈定义结构

所有反馈以单个 JavaScript 对象传递：

```js
{
  'feedback1': { /* 反馈1属性 */ },
  'feedback2': { /* 反馈2属性 */ },
}
```

最小 boolean feedback 定义：

```js
{
  type: 'boolean',
  name: 'My first feedback',
  defaultStyle: {
    bgcolor: 0xff0000, // 或 combineRgb(255, 0, 0)
    color: 0x000000,   // 或 combineRgb(0, 0, 0)
  },
  options: [
    {
      type: 'number',
      label: 'Source',
      id: 'source',
      default: 1,
    }
  ],
  callback: (feedback) => {
    return self.some_device_state.source == feedback.options.source
  },
}
```

## 回调执行

回调在反馈执行时调用，接收两个参数：

- `feedback`：包含选项的对象，以及一些额外标识符
- `context`（API 1.1+）：包含与执行相关的方法

可以安全地抛出错误，Companion 会捕获并视为 falsy。

### 同步与异步

API v1.1+ 支持 async 回调或返回 Promise。不建议在此处执行网络请求，但生成图像或使用原生代码时可能需要。确保设置合理的超时，否则反馈可能卡滞。

### 使用变量

API v1.1+ 支持在反馈回调中使用变量：

```js
{
  type: 'boolean',
  name: 'My first feedback',
  defaultStyle: {
    bgcolor: combineRgb(255, 0, 0),
    color: combineRgb(0, 0, 0),
  },
  options: [{
    type: 'text',
    label: 'text',
    id: 'text',
    default: '',
    useVariables: true
  }],
  callback: async (feedback, context) => {
    // 使用 context 中的 parseVariablesInString
    const text = await context.parseVariablesInString(feedback.options.text)
    return text === 'OK'
  },
}
```

### 反转 Boolean Feedback

API v1.5 (Companion 3.1) 起内置支持反转 boolean feedback 值。可设置 `showInvert: false` 影响自动检测行为。

如果反馈已提供匹配 true/false 状态的字段，建议移除并使用内置 invert 属性。可使用辅助函数 `CreateUseBuiltinInvertForFeedbacksUpgradeScript` 生成升级脚本。

## Subscribe & Unsubscribe 流程

对于需要按需加载设备状态的反馈，可注册额外回调：

```js
feedbacks['check_source'] = {
  name: 'Test feedback',
  options: [...],
  callback: (feedback) => { ... },
  subscribe: (feedback) => {
    // 反馈添加到按钮时调用
  },
  unsubscribe: (feedback) => {
    // 反馈从按钮移除时调用
  },
}
```

- 添加到按钮时：`subscribe` 或 `callback` 调用
- 从按钮移除时：`unsubscribe` 调用
- 选项更改时：仅 `callback` 调用

如需数据加载，应在 callback 中调度（不等待）并触发重新评估。

## UI 展示

- 按名称字母顺序排序
- `description`：更长的描述文本
- API 2.0+：`sortName`：自定义排序名称

## 代码示例

```typescript
import { combineRgb } from '@companion-module/base'
import type { ModuleInstance } from './main.js'

export function UpdateFeedbacks(self: ModuleInstance): void {
  self.setFeedbackDefinitions({
    ChannelState: {
      name: 'Example Feedback',
      type: 'boolean',
      defaultStyle: {
        bgcolor: combineRgb(255, 0, 0),
        color: combineRgb(0, 0, 0),
      },
      options: [
        {
          id: 'num',
          type: 'number',
          label: 'Test',
          default: 5,
          min: 0,
          max: 10,
        },
      ],
      callback: (feedback) => {
        return Number(feedback.options.num) > 5
      },
    },
  })
}
```

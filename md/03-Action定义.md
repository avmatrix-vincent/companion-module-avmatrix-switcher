# Companion 模块开发 - Action 定义

> 文档来源：https://companion.free/for-developers/module-development/connection-basics/actions/

## 概述

Actions（动作）是模块的核心，定义用户按下按钮或运行触发器时发生的行为。

## API 调用

### setActionDefinitions(definitions)

在 `init()` 方法中调用此方法定义模块支持的动作列表。也可以在其他时间调用以更新暴露的动作列表。

**注意**：不要频繁调用此方法，更新列表有性能开销。如果在短时间内多次调用，考虑合并为一次调用。

## 动作定义结构

所有动作以单个 JavaScript 对象传递：

```js
{
  'action1': { /* 动作1属性 */ },
  'action2': { /* 动作2属性 */ },
}
```

最小动作定义：

```js
{
  name: 'My first action',
  options: [],
  callback: (action) => {
    console.log('Hello World!')
  }
}
```

## 回调执行 (callback)

动作执行时调用回调函数，接收两个参数：

- `action`：包含执行时选项的对象，以及一些额外标识符
- `context`（API 1.1+）：包含与动作执行相关的一些有用方法

回调中可以安全地抛出错误，Companion 会捕获并记录，不会中断执行。

### 同步与异步执行

回调可以同步返回 undefined，也可以异步返回 Promise。

从 Companion 3.5 开始，动作可以定义为顺序执行（在管理界面中放入动作组），会等待异步回调返回的 Promise 解析后才继续后续动作。

```js
// 不等待请求完成的动作
{
  name: 'Fetch Google',
  options: [],
  callback: (action) => {
    fetch('https://google.com/').then(...)
  }
}

// 等待请求完成的动作
{
  name: 'Fetch Google and wait',
  options: [],
  callback: async (action) => {
    return fetch('https://google.com/').then(...)
  }
}
```

### 使用变量

- API v1.13 (Companion 4.1)：textinput 字段中的变量自动解析
- API v2.0 (Companion 4.3)：模块无法自行解析变量，Companion 根据选项字段描述自动解析
- API v1.1 到 v1.14：context 对象包含 `parseVariablesInString()` 方法

## Subscribe & Unsubscribe 流程

对于具有大量属性的设备，或者获取数据有成本的情况，可以注册额外的回调：

```js
actions['set_source'] = {
  name: 'Test action',
  options: [...],
  callback: (action) => { ... },
  subscribe: (action) => { 
    // 动作添加到按钮时调用
  },
  unsubscribe: (action) => { 
    // 动作从按钮移除时调用
  },
}
```

- `subscribe`：动作添加到按钮时调用
- `unsubscribe`：动作从按钮移除时调用
- 选项更改时：先调用 `unsubscribe`，再调用 `subscribe`，然后调用 `callback`

可以调用 `this.subscribeActions()` 或 `this.unsubscribeActions()` 强制为所有动作调用订阅/取消订阅，可传入 actionIds 限定特定动作类型。

API v1.13+：
- `skipUnsubscribeOnOptionsChange`：选项更改时避免过度的 unsubscribe 调用
- `optionsToIgnoreForSubscribe`：限制哪些字段能触发 subscribe 调用

API v2.0：使用 `optionsToMonitorForSubscribe` 替代 `optionsToIgnoreForSubscribe`。

## UI 展示

- Companion UI 按名称字母顺序排序动作
- `description`：添加更长的描述文本
- API 2.0+：`sortName`：自定义排序名称（替代 `name` 用于字母排序）

## TypeScript 类型（API 2.x）

```typescript
export type ActionsSchema = {
  route: {
    options: {
      source: number
      destination: number
    }
  }
}

export interface MyTypes {
  actions: ActionsSchema
}
```

然后使用 `CompanionActionDefinition<ActionsSchema['route']['options']>` 类型定义动作。

## 代码示例

```typescript
import type { ModuleInstance } from './main.js'

export function UpdateActions(self: ModuleInstance): void {
  self.setActionDefinitions({
    sample_action: {
      name: 'My First Action',
      options: [
        {
          id: 'num',
          type: 'number',
          label: 'Test',
          default: 5,
          min: 0,
          max: 100,
        },
      ],
      callback: async (event) => {
        console.log('Hello world!', event.options.num)
      },
    },
  })
}
```

# Companion 模块开发 - Variable 定义

> 文档来源：https://companion.free/for-developers/module-development/connection-basics/variables/

## 概述

Variables（变量）是模块向用户暴露值的方式，可用于按钮文本、动作或反馈的输入等。

基本工作流程：
1. 使用 `setVariableDefinitions()` 定义变量
2. 使用 `setVariableValues()` 设置或更新值

## API 调用

### setVariableDefinitions(definitions)

在 `init()` 中调用以定义模块暴露的变量列表。也可以在其他时间调用更新列表。

**注意**：不要频繁调用，更新列表有性能开销。

## 变量定义结构

### API 2.x

变量定义以单个 JavaScript 对象传递：

```js
const definitions = {
  variable1: { name: 'My first variable' },
  variable2: { name: 'My second variable' },
  variable3: { name: 'Another variable' },
}
```

### API 1.x

以数组形式传递：

```js
const definitions = [
  { variableId: 'variable1', name: 'My first variable' },
  { variableId: 'variable2', name: 'My second variable' },
]
```

**重要**：VariableId 只能使用字母 [a-zA-Z]、数字、下划线、连字符。

## 设置变量值

### setVariableValues(values)

在模块的任何位置调用此方法更新变量值。可以指定任意数量的变量，只有指定的变量会被更新。

```js
this.setVariableValues({
  'variable1': 'new value',
  'variable2': 99,
  'old_variable': undefined, // 取消设置值
  'array_variable': [1, 2, 3, 4],
})
```

变量可以是任何类型的值，用户可以使用表达式操作这些值。

**注意**：尽量批量更新变量值，避免频繁调用。

## TypeScript 类型（API 2.x）

作为传递给 InstanceBase 的 InstanceTypes 泛型参数的一部分，必须定义 variables 属性。默认为 `CompanionVariableValues`（松散类型）。

启用强类型：

```typescript
export type VariablesSchema = {
  myVar: string
  anotherVar: number | null
}

export interface MyTypes {
  variables: VariablesSchema
}
```

在 `setVariableDefinitions` 调用中，可将定义类型化为 `CompanionVariableDefinition<VariablesSchema>`。`setVariableValues` 将期望接收 `Partial<VariablesSchema>`。

## 代码示例

```typescript
import type { ModuleInstance } from './main.js'

export function UpdateVariableDefinitions(self: ModuleInstance): void {
  self.setVariableDefinitions([
    { variableId: 'variable1', name: 'My first variable' },
    { variableId: 'variable2', name: 'My second variable' },
    { variableId: 'variable3', name: 'Another variable' },
  ])
}
```

在模块其他位置更新值：

```typescript
this.setVariableValues({
  variable1: 'connected',
  variable2: 42,
})
```

# Companion 模块开发 - Learn 回调

> 文档来源：https://companion.free/for-developers/module-development/connection-advanced/learn-action-feedback-values/

## 概述

为了让用户更容易配置动作和反馈，可以实现 `learn` 回调。这允许动作或反馈的选项值被设置为匹配设备的当前状态。

例如：实现一个 learn 回调，将 Set-Position 动作的值设置为设备上画中画的当前位置。回调只需查询设备的当前状态并返回适当的值。

实现后，动作或反馈中会出现 Learn Values 按钮，用户可以触发 learn 事件。

## 实现方式

`learn` 回调对动作和反馈的实现方式相同，但参数略有差异。

### 基本示例

对于有一个 `input` 选项的动作：

```js
learn: (event) => {
  return {
    input: this.currentDeviceState.input,
  }
}
```

回调接收与其他回调相同的 action/feedback 对象，应返回包含新值的 event.options 形式的对象。只能返回普通值，不能返回表达式。

### 部分更新

可以只更新特定字段：

```js
learn: (event) => {
  return {
    input: this.currentDeviceState.inputs[event.options.output],
  }
}
```

## API 2.0 注意事项

API 2.0 起，**必须只返回学习到的选项**。返回所有选项会覆盖用户可能正在使用的表达式，因此应避免返回未更改的字段。

API 2.0 之前，建议包含所有选项，否则它们会变成 undefined。

## 中止学习

如果无法提供新值，可以返回 undefined 中止学习操作：

```js
learn: (event) => {
  const input = this.currentDeviceState.inputs[event.options.output]
  if (input === undefined) {
    // 状态中没有值
    return undefined
  }
  return {
    input: input,
  }
}
```

## 重要提示

- 不要在 learn 回调中更新任何内部状态。返回的值可能被应用到动作/反馈，也可能被丢弃
- 如果用户接受值，新值会像往常一样提供给动作的 subscribe 或反馈的 callback

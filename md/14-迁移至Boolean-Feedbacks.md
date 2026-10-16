# Companion 模块开发 - 迁移至 Boolean Feedbacks

> 文档来源：https://companion.free/for-developers/module-development/connection-advanced/migrating-legacy-to-boolean-feedbacks/

## 为什么要更新

从 Companion v3 开始，大多数反馈最好定义为 boolean feedbacks，因为它们给用户更多灵活性，最终界面更一致。

以前，由模块作者决定反馈应更改哪些属性，这往往限制反馈只能更改背景和文本颜色。如果用户想更改 PNG 或文本，就需要模块作者复制反馈并添加不同的样式选项。

使用 boolean feedbacks，模块作者只需让反馈返回 true 或 false，用户可以自己决定应更改哪些样式属性。

另一个好处：boolean feedbacks 可以在触发器系统中用作条件。

## 迁移步骤

### 1. 更新反馈定义

将 `type: 'advanced'` 改为 `type: 'boolean'`，将样式选项移到 `defaultStyle` 中，回调返回 boolean 值。

迁移前：

```javascript
feedbacks['set_source'] = {
  type: 'advanced',
  name: 'Brief description of the feedback here',
  description: 'Longer description of the feedback',
  options: [
    {
      type: 'colorpicker',
      label: 'Foreground color',
      id: 'fg',
      default: combineRgb(0, 0, 0)
    },
    {
      type: 'colorpicker',
      label: 'Background color',
      id: 'bg',
      default: combineRgb(255, 0, 0)
    },
    {
      type: 'number',
      label: 'Source',
      id: 'source',
      default: 1
    }
  ],
  callback: (feedback) => {
    if (this.currentSource == feedback.options.source) {
      return {
        bgcolor: feedback.options.bg,
        color: feedback.options.fg,
      }
    }
  },
}
```

迁移后：

```js
feedbacks['set_source'] = {
  type: 'boolean',
  name: 'Brief description of the feedback here',
  description: 'Longer description of the feedback',
  defaultStyle: {
    color: combineRgb(0, 0, 0),
    bgcolor: combineRgb(255, 0, 0),
  },
  options: [
    {
      type: 'number',
      label: 'Source',
      id: 'source',
      default: 1,
    },
  ],
  callback: (feedback) => {
    return this.currentSource == feedback.options.source
  },
}
```

### 2. 更新预设

预设中的反馈定义也需要更新。

迁移前：

```js
feedbacks: [
  {
    feedbackId: 'set_source',
    options: {
      bg: combineRgb(0, 255, 0),
      fg: combineRgb(255, 255, 255),
      input: src.id,
      mixeffect: me,
    },
  },
]
```

迁移后：

```js
feedbacks: [
  {
    feedbackId: 'set_source',
    options: {
      input: src.id,
      mixeffect: me,
    },
    style: {
      bgcolor: combineRgb(0, 255, 0),
      color: combineRgb(255, 255, 255),
    }
  },
]
```

### 3. 添加升级脚本

用户已在按钮上配置的反馈需要更新到新格式。可使用辅助函数：

```js
const upgradeToBooleanFeedbacks = CreateConvertToBooleanFeedbackUpgradeScript({
  set_source: true,
  set_output: true,
})

runEntrypoint(MyInstance, [myOtherUpgradeScript, upgradeToBooleanFeedbacks])
```

此脚本会自动处理将选项属性移动到 style 对象。

如果属性命名不匹配，可以自定义映射：

```js
CreateConvertToBooleanFeedbackUpgradeScript({
  set_source: {
    bg: 'bgcolor',
    fg: 'color',
  },
})
```

### 4. 测试

全面测试后完成迁移。

## 相关文档

- Upgrade Scripts
- Feedbacks

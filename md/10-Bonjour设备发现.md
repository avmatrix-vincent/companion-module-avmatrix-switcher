# Companion 模块开发 - Bonjour 设备发现

> 文档来源：https://companion.free/for-developers/module-development/connection-advanced/bonjour-device-discovery/

## 概述

Bonjour 是一种标准化的设备发现方法，使用 MDNS 协议。从 API 1.7 (Companion 3.2) 开始，Companion 支持通过 Bonjour 协议轻松发现设备，帮助用户简化配置。

## 配置步骤

### 1. 定义配置字段

在 `src/config.ts` 中定义 `bonjour-device` 类型的字段：

```js
{
  type: 'bonjour-device',
  id: 'bonjour_host',
  label: 'Bonjour Test',
  width: 6,
}
```

### 2. 配置 manifest.json

在 `companion/manifest.json` 中定义 `bonjourQueries`：

```js
"bonjourQueries": {
  "bonjour_host": {
    "type": "blackmagic",
    "protocol": "tcp",
    "txt": {
      "class": "AtemSwitcher"
    }
  }
}
```

这两个结构通过共同的 id 关联，未来会进一步自动化设备发现。

### 3. 处理手动输入

UI 中始终显示 Manual 选项，必须处理用户手动指定地址的情况（Bonjour 不可用的环境）。可配合额外字段实现：

```js
{
  type: 'textinput',
  id: 'host',
  label: 'Target IP',
  isVisibleExpression: `!$(options:bonjour_host)`,
  default: '',
  regex: Regex.IP,
}
```

使用 `isVisibleExpression` 根据是否选择了 Bonjour 设备来控制字段可见性。

### 4. 读取值

在模块代码中，`bonjour_host` 的值格式为 `10.0.0.1:8000` 或 `null`。

## 编写 Bonjour Query

目前支持部分查询选项。所有查询必须设置 `type` 和 `protocol`。

如需进一步过滤，可指定 `txt` 字段值。

API 演进：
- API 1.10：`bonjourQueries` 中的每项可以是数组，允许并行运行多个查询（支持使用不同查询的多个型号）
- API 1.12：支持按端口号过滤（建议仅作为最后手段，因为端口号通常可配置）
- API 2.0：支持 `addressFamily`，可指定返回 ipv4、ipv6 或两者（ipv4+6）

## 示例配置

```typescript
// config.ts
export function GetConfigFields(): SomeCompanionConfigField[] {
  return [
    {
      type: 'bonjour-device',
      id: 'bonjour_host',
      label: 'Device',
      width: 6,
    },
    {
      type: 'textinput',
      id: 'host',
      label: 'Target IP',
      width: 6,
      isVisibleExpression: `!$(options:bonjour_host)`,
      default: '',
      regex: Regex.IP,
    },
  ]
}
```

```json
// manifest.json
{
  "bonjourQueries": {
    "bonjour_host": {
      "type": "blackmagic",
      "protocol": "tcp",
      "txt": {
        "class": "AtemSwitcher"
      }
    }
  }
}
```

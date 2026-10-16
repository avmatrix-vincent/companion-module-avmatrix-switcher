# Companion 模块开发 - HTTP 处理器

> 文档来源：https://companion.free/for-developers/module-development/connection-advanced/http-handler/

## 概述

Companion 的 Web 服务器（用于提供 Web UI）也为每个连接提供一个路径，HTTP 请求可以透传到模块实例。模块可以选择响应，否则 Companion 会自动返回 404。

实例路径格式：`/instance/INSTANCE_NAME/`

例如：Companion 在 `http://127.0.0.1:8000/`，Google Sheets 连接名为 sheet，则 `http://127.0.0.1:8000/instance/sheet/` 的请求会转发到该模块的 HTTP 处理器。

由于每个实例作为 Companion 的子进程运行，只有 Express HTTP 请求的部分属性会传递给子进程。这满足大多数常见用例，但无法使用 HTTP 处理器实现 WebSocket。

## 使用场景

1. **暴露模块收集的数据**：如 Google Sheets 模块将电子表格数据以 JSON/CSV 格式提供，供 vMix 等应用作为数据源使用
2. **暴露动作功能**：外部设备或服务可以直接运行动作，而不需要通过 Companion API 按压按钮
3. **提供 HTML UI页面**：可配合 JSON 端点动态填充数据，POST 端点触发模块功能

## API 调用

### handleHttpRequest(request)

```js
handleHttpRequest(request: CompanionHTTPRequest): CompanionHTTPResponse | Promise<CompanionHTTPResponse> {
  // 处理 HTTP 请求并返回响应
}
```

## CompanionHTTPRequest 结构

| 属性 | 类型 | 说明 |
|------|------|------|
| baseUrl | string | 基础 URL |
| body? | string | 请求体 |
| headers | Record<string, string> | 请求头 |
| hostname | string | 主机名 |
| ip | string | 客户端 IP |
| method | string | HTTP 方法 |
| originalUrl | string | 原始 URL |
| path | string | 请求路径 |
| query | Record<string, string> | 查询参数 |

## CompanionHTTPResponse 结构

| 属性 | 类型 | 说明 |
|------|------|------|
| status? | number | HTTP 状态码 |
| headers? | Record<string, any> | 响应头 |
| body? | string | 响应体 |

## JSON 响应示例

```typescript
handleHttpRequest(request: CompanionHTTPRequest): CompanionHTTPResponse | Promise<CompanionHTTPResponse> {
  const endpoint = request.path.replace('/', '').toLowerCase()

  const dataResponse = () => {
    return {
      status: 200,
      body: JSON.stringify({
        value1: this.label,
        value2: 123,
        value3: this.someValue
      }),
      headers: {
        'Content-Type': 'application/json',
      },
    }
  }

  const configResponse = () => {
    return {
      status: 200,
      body: JSON.stringify(this.config),
      headers: {
        'Content-Type': 'application/json',
      },
    }
  }

  if (request.method === 'GET') {
    if (endpoint === 'data') return dataResponse()
    if (endpoint === 'config') return configResponse()
  }

  return {
    status: 404,
    body: JSON.stringify({ status: 404, error: `API endpoint ${endpoint} not found` })
  }
}
```

## HTML 响应示例

```typescript
import path from 'path'
import fs from 'fs'

handleHttpRequest(request: CompanionHTTPRequest): CompanionHTTPResponse | Promise<CompanionHTTPResponse> {
  const endpoint = request.path.replace('/', '').toLowerCase()

  if (request.method === 'GET') {
    const htmlDir = path.resolve(import.meta.dirname, 'html')
    const requestedFile = endpoint === '' ? 'index.html' : endpoint
    const filePath = path.resolve(htmlDir, requestedFile)
    
    // 安全检查：确保请求的文件在 html 目录内
    if (!filePath.startsWith(htmlDir + path.sep) && filePath !== htmlDir) {
      return { status: 403, body: 'Forbidden' }
    }

    const exists = fs.existsSync(filePath)
    if (!exists) {
      return {
        status: 404,
        body: JSON.stringify({ status: 404, error: `File not found` })
      }
    }

    return {
      status: 200,
      body: fs.readFileSync(filePath, 'utf8')
    }
  }

  return {
    status: 404,
    body: JSON.stringify({ status: 404, error: `Not found` })
  }
}
```

**生产环境强烈建议**：预加载允许提供的文件列表，仅响应特定文件，而不是使用通配符。

## 注意事项

- Content-Type 通常由 Companion 侧的 Express 处理，但某些文件类型可能需要手动设置响应头
- 除静态文件外，也可以像 JSON 示例那样动态生成 HTML 响应

# Companion 模块开发 - OAuth 认证

> 文档来源：https://companion.free/for-developers/module-development/connection-advanced/oauth

## 概述

某些模块需要针对外部服务或 API 进行认证。Companion 目前没有原生的 OAuth 支持，模块需要手动实现认证流程。

使用 OAuth 有两个关键挑战：
1. OAuth 需要稳定的重定向 URL，但 Companion 的访问 URL 可能每天变化
2. 用户需要填写各种字段，然后导航到 URL 开始认证

以下是目前推荐的 OAuth 支持方式，未来可能会改进。

## 处理 OAuth 回调/重定向 URL

OAuth 需要稳定的重定向 URL。为此创建了一个小型重定向站点：https://bitfocus.github.io/companion-oauth/callback

在认证 URL 中提供实例 id（`this.id`）作为 `state` 参数，重定向站点会将用户重定向到模块的 HTTP 处理器，在那里可以获取生成的认证码。

实现 `handleHttpRequest` 方法，监听 `/oauth/callback` 路径：

```js
async handleHttpRequest(request) {
  if (request.path === '/oauth/callback') {
    const authCode = request.query['code']
    if (!authCode) {
      return {
        status: 400,
        body: 'Missing auth code!',
      }
    }
    if (!this.config.clientID || !this.config.clientSecret || !this.config.redirectURL) {
      return {
        status: 400,
        body: 'Missing required config fields!',
      }
    }
    try {
      // 用 code 换取 token
      // const response = await axios.post('https://...', { code: authCode, ... })
      
      this.log('info', 'Authentication Success, saving tokens')
      this.config.accessToken = response.data.accessToken
      this.config.refreshToken = response.data.refreshToken
      this.saveConfig(this.config)
      this.configUpdated(this.config)
    } catch (err) {
      this.log('debug', `Failed to get access token: ${err?.message ?? err?.toString()}`)
      return {
        status: 500,
        body: `Failed to authenticate\n${err?.message ?? err?.toString()}`,
      }
    }
    return {
      status: 200,
      body: 'Success!\nYou can close this tab',
    }
  }
  return {
    status: 404,
  }
}
```

## 打开认证 URL

用户需要打开认证 URL 以开始 OAuth 流程。由于某些用户会远程配置 Companion，不能依赖自动打开 URL。

大多数模块目前的做法：
- 将需要的 URL 放在配置字段中供用户访问
- 将 URL 写入日志
- 部分模块也会自动打开浏览器

## 完整流程

1. 用户在模块配置中填写 clientID、clientSecret 等字段
2. 模块生成认证 URL（包含 state=this.id）
3. 用户点击或复制 URL 到浏览器
4. 外部服务认证后重定向到 bitfocus.github.io/companion-oauth/callback
5. 重定向站点将请求转发到 Companion 的 /instance/INSTANCE_NAME/oauth/callback
6. 模块的 handleHttpRequest 接收 code，换取 token
7. 保存 token 到配置，更新连接状态

## 注意事项

- 确保保存 accessToken 和 refreshToken 到配置中持久化
- 处理好 token 过期后的刷新逻辑
- 由于 Companion URL 可能变化，使用 bitfocus 的重定向站点是关键

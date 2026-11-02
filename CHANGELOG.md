# Changelog

本文件遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 规范，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Planned

- **NR1**: 规划迁移到 `@companion-module/base` v2.x（Companion 4.3+ / 5.0+），以获得表达式支持与最新模块 API。详见 v1.0.0 审核文档 “Next Release”。

## [1.0.1] - 2026-11-02

针对 `companion-module-avmatrix-switcher v1.0.0` 审核（`review-avmatrix-switcher-v1.0.0-20261030-090507`）所列问题的修复版本。

### Security

- **C1**: `.yarnrc.yml` 补齐模板的供应链加固配置：`enableScripts: false`、`npmMinimalAgeGate: 3d`、`npmPreapprovedPackages: ["@companion-module/*"]`，阻止依赖安装脚本执行并拦截发布不到 3 天的新版本。

### Fixed

- **H1**: `sendCommand()` / `sendCommandWithCallback()` 改为 `await this.udp.send(...)`，发送失败（网卡掉线 / 路由不可达）不再产生未处理的 Promise rejection 导致 Node 22 崩溃，而是进入 `try/catch` 并返回 `false`。
- **H2**: 手动填写 Target IP（跨网段、非扫描所得）时，心跳不再因缺少目标设备而跳过发送；改为按协议族 `probeCommand` 或 `0xFFFF` 发现包持续探测，并在连续 miss 后正确转为 Connection Failure。
- **H3**: 启动扫描仅在**首次配置**（Device 与 Target IP 均为空）时自动选择设备；其余情况只刷新设备列表，保留用户已选设备/手填 Target IP，不再被扫描结果覆盖并强制重连。
- **M1**: 扫描期间为每个网络接口创建的 UDP socket 记录到 `scanSockets`，在 `disconnect()` 与超时处理中统一关闭，修复销毁后仍发送/监听与失败扫描泄漏。
- **M2**: 新增 `connectedHost`，`configUpdated()` 以当前实际连接的 host 判断是否需要重连，修复“把 Target IP 改回与 Device 相同值后仍发往旧地址”的问题。
- **M3**: 心跳发送失败也计入 `heartbeatMissed`，Companion 主机断网时连接状态能正确转为 Connection Failure，不再保持绿色。
- **M4**: 扫描结果为空时不再清空 `discoveredDevices`，保留原有设备列表与 MAC/型号信息。
- **M5**: 扫描无设备且无 Target IP 时，状态置为 `BadConfig`（提示需填写 Target IP），不再永久停留在 Connecting。
- **M6**: 预设（Presets）在 `init()` / `applyDeviceProfile()` 注册后常驻，不再随连接状态变化被 `setPresetDefinitions({})` 清空。
- **L1**: `destroy()` 时清除 400ms 执行闪烁定时器 `flashTimer`。
- **L2**: 断开/重连时复位 `blinkOn` 相位并在恢复在线后调用 `updateBlink()`，修复 FTB/MUTE/Freeze 重连后停止闪烁。
- **L3**: 本地按下 FTB/MUTE/Freeze 翻转状态后调用 `updateBlink()`，修复“常亮不闪”。
- **L4**: AUTO 视为瞬时动作，短暂点亮后自动释放，修复 AUTO 按钮常亮且状态反转的问题。
- **L5**: `moveTBar()` 未连接时拒绝执行；发送失败回滚本地基准且不更新显示变量；仅在发送成功后写回 `tbar_value`。
- **L6**: 修正 “Last Action (Flash)” 反馈的示例 key，改为真实格式（如 `set_source|source=5`，以及上报用的 `key:NN`）。
- **L7**: PIP/LUMA/CHROMA/DSK/LOGO 状态反馈改用可读名称并补充 `description`；`connection_status` 更名为 “Device Disconnected” 并说明其语义。
- **L8**: 移除 T-Bar Move 动作中无效的 `$(self:tbar_value)` 静态文本，改为说明文字。
- **L9**: 配置项 tooltip 英文化（Device / Target IP）。
- **L10**: 移除 `companion/manifest.json` 中未发布的 `legacyIds: ["szavm"]`。
- **L11**: `[Recv]` / `[Send]` / `[Heartbeat]` / `[Report]` 等流量日志降为 `debug`，`warn` 级别不再被降级为 `info`，显著降低运行期日志噪声。

### Changed

- **N1**: 收紧类型：`handleDeviceReport(packet: ParsedPacket)`、`getDeviceState(): DeviceState`（新增 `DeviceState` 接口），提升上报路径的类型安全。

### Notes

- **N2**（预设分组零宽字符排序）：**有意保留**。移除后预设分组顺序将依赖 Companion 渲染实现，存在分组错乱回归风险，故本次不调整。
- 所有网络与生命周期层改动均未触碰 `avm-0617`（SHARK S6 PLUS / S5 / H5）与 `avm-0605`（SHARK S6）的协议命令表、键值表与状态解析布局，旧族行为保持不变。

### 复审对照表

| 编号 | 修复内容                        | 关键改动                                                         |
| ---- | ------------------------------- | ---------------------------------------------------------------- |
| C1   | `.yarnrc.yml` 供应链加固        | `enableScripts` / `npmMinimalAgeGate` / `npmPreapprovedPackages` |
| H1   | 发送失败不再崩进程              | `await udp.send()` 纳入 `try/catch`                              |
| H2   | 手动 IP 可正常连接              | 心跳无目标设备时仍发探测包并计 miss                              |
| H3   | 启动扫描不再抢连接/覆盖手填 IP  | 仅首次配置自动选设备                                             |
| M1   | 扫描 socket 泄漏                | `scanSockets` 统一回收                                           |
| M2   | 改回 Target IP 仍发旧地址       | 用 `connectedHost` 判定重连                                      |
| M3   | 断网仍显示绿色                  | 发送失败也计 miss                                                |
| M4   | 空扫描清空设备列表              | 仅非空才覆盖列表                                                 |
| M5   | 无设备无 IP 卡在 Connecting     | 置 `BadConfig` 提示                                              |
| M6   | 预设随在线状态消失              | 不再 `setPresetDefinitions({})`                                  |
| L1   | 闪烁定时器未清理                | `destroy()` 清 `flashTimer`                                      |
| L2   | 重连后停止闪烁                  | 复位 `blinkOn` + `updateBlink()`                                 |
| L3   | 本地按下常亮不闪                | 翻转后调 `updateBlink()`                                         |
| L4   | AUTO 常亮/状态反转              | 瞬时高亮后自动释放                                               |
| L5   | 未发送却改 T-Bar 变量           | 成功后才写变量，失败回滚                                         |
| L6   | Flash 反馈示例 key 错误         | 改为真实 key 格式                                                |
| L7   | 反馈以内部 ID 展示              | 可读名称 + `description`                                         |
| L8   | 显示字面量 `$(self:tbar_value)` | 改为说明文字                                                     |
| L9   | 配置 tooltip 为中文             | 英文化                                                           |
| L10  | 首发声明的 legacyId             | 移除 `szavm`                                                     |
| L11  | 报文/心跳 info 级刷屏、重复处理 | 降为 `debug`，`warn` 直通                                        |
| N1   | 松散类型                        | `ParsedPacket` / `DeviceState`                                   |
| N2   | 零宽字符排序                    | 有意保留（避免分组乱序）                                         |
| NR1  | base v2.x 迁移                  | 下个版本规划                                                     |

## [1.0.0] - 2026-10-30

### Added

- 首个正式发布版本。
- 基于 UDP（端口 7000）控制 Avmatrix 切换台。
- 支持 SHARK S6（VS0605）、SHARK S6 PLUS（VS0617），并兼容使用相同 UDP 协议的其它型号。
- UDP 广播自动发现设备，支持手动填写 Target IP（跨网段）。
- 提供 PGM / PVW 源、CUT / AUTO / FTB / MUTE、PIP / LUMA / CHROMA / DSK / LOGO、转场（WIPE）、T-Bar 等动作、反馈与预设。
- 状态跟随设备上报同步，硬件面板操作也会更新按键反馈。

### Notes

- 本版本经 Bitfocus 审核，结论为 “Changes Required”，相关问题的修复见 [1.0.1]。

# AVM PSV0617 UDP通信协议 — 同步协议（3.2节）

> 协议版本：V1.0.0  
> 芯片平台：PSV0617 (0x09)  
> 来源文档：AVM_PSV0617_UDP通信协议V1.0.0_test.docx

---

## 概述

同步协议用于**上位机主动获取**设备当前状态数据，以及**设备主动上报**状态变化。每条指令仅含 Data 部分定义，外层报文结构遵循协议通用格式（见 [报文结构](#报文结构)）。

### 报文结构

| 字段 | 字节数 | 说明 |
|---|---|---|
| Head | 2 | `0xA5 0x5A` 包头标识 |
| Protocol_Version | 2 | 大端，协议版本号，如 `0100` 表示 V1.0 |
| Length | 2 | 大端，包含 Head→Tail 的总长度：`25 + n + 4` |
| index | 2 | 大端，数据包序号 |
| Padding | 8 | 8 字节 `0x00` 填充 |
| Pack_Type | 1 | `0`：上位机→设备；`1`：设备回复；`2`：设备主动上报 |
| CMD | 2 | 大端，指令码 |
| Session | 4 | 请求/响应一一对应标识 |
| Data_Length | 2 | 大端，数据长度 |
| Data | n | 数据体 |
| Sum | 2 | 大端，25+n 字节的字节和校验 |
| Tail | 2 | `0xA6 0x6A` 包尾标识 |

---

## 目录

| 指令码 | 名称 | 说明 |
|---|---|---|
| 0x0110 | 按键获取 | 获取按键/推杆当前状态 |
| 0x0120 | Transition 获取 | 获取转场参数 |
| 0x0130 | KEY 源获取 | 获取抠像源配置 |
| 0x0131 | LUMA 获取 | 获取亮度抠像参数 |
| 0x0132 | CHROMA 获取 | 获取色度抠像参数 |
| 0x0133 | PIP1 获取 | 获取画中画1参数 |
| 0x0134 | PIP2 获取 | 获取画中画2参数 |
| 0x0135 | PIP3 获取 | 获取画中画3参数 |
| 0x0136 | PIP Border 获取 | 获取画中画边框参数 |
| 0x0140 | DSK 获取 | 获取下游键参数 |
| 0x0141 | LOGO 获取 | 获取台标参数 |
| 0x0150 | Audio 获取 | 获取音频参数 |
| 0x0160 | VIEW 选择获取 | 获取当前 VIEW 通道 |
| 0x0161 | VIEW 设置获取 | 获取各 VIEW 的源/翻转/图像参数 |
| 0x0170 | MV 获取 | 获取多画面分割布局与元素参数 |
| 0x0171 | UMD 字符获取 | 获取 UMD 字符标签 |
| 0x0180 | Library 获取 | 获取图案库配置 |
| 0x0190 | Output 获取 | 获取输出路由与格式 |
| 0x01A0 | Codec 获取 | 获取编码/录制参数 |
| 0x01B0 | SYSTEM 获取 | 获取系统配置 |

---

## 3.2.1 按键获取指令 0x0110

**说明：** 获取当前按键、推杆、转场模式等状态。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| PGM | 1 | — | PGM 选项：1.PGM1 / 2.PGM2 / 3.PGM3 / 4.PGM4 / 5.PGM5 / 6.PGM6 / 7.PGM_PAT1 / 8.PGM_PAT2 |
| PVW | 1 | — | PVW 选项：1.PVW1 / 2.PVW2 / 3.PVW3 / 4.PVW4 / 5.PVW5 / 6.PVW6 / 7.PVW_PAT1 / 8.PVW_PAT2 |
| WIPE MODE | 1 | — | WIPE 模式：1.WIPE1 / 2.WIPE2 / 3.WIPE3 / 4.WIPE4 / 5.MIX / 6.DIP |
| SPEED MODE | 1 | — | SPEED 模式：1.SPEED1 / 2.SPEED2 |
| FTB_State | 1 | — | FTB 状态：0.OFF / 1.ON |
| Freeze state | 1 | — | 静帧状态：0.Off / 1.On |
| T_Bar_val (NO.1) | 2 | — | 推杆数据（值范围 0~4095） |
| b_bar_pos (NO.2) | 2 | — | 推杆位置：0.底部 / 1.中间 / 2.顶部 |

---

## 3.2.2 Transition 获取 0x0120

**说明：** 获取转场（Transition）相关参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Wipe 1 (NO.0) | 1 | — | 划像1（样式 0-10） |
| Wipe 2 (NO.1) | 1 | — | 划像2（样式 0-10） |
| Wipe 3 (NO.2) | 1 | — | 划像3（样式 0-10） |
| Wipe 4 (NO.3) | 1 | — | 划像4（样式 0-10） |
| Softness (NO.4) | 1 | — | 柔化度 0-100 |
| Direction (NO.5) | 1 | — | 方向：0.Normal / 1.Invert / 2.Flip-Flop |
| MIX (NO.6) | 1 | — | 方向：0.OFF / 1.ON |
| Dir Color R/G/B (NO.7) | 3 | — | 方向颜色：R/G/B 各 0-255 |
| Speed 1 (NO.10) | 1 | — | 速率1，1-80 |
| Speed 2 (NO.11) | 1 | — | 速率2，1-80 |
| T-Bar A/B Mode (NO.12) | 1 | — | A/B 模式：0.OFF / 1.ON |
| T-Bar Status (NO.13) | 1 | — | 推杆状态：0.OFF / 1.ON |

---

## 3.2.3 KEY 源获取 0x0130

**说明：** 获取三路抠像源的通道与优先级配置。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Key1 Type (0) | 1 | — | 0: PIP / 1: Luma key |
| Key1 Priority (1) | 1 | — | 0: 优先级1 / 1: 优先级2 / 3: 优先级3 |
| Key2 Type (2) | 1 | — | 0: PIP / 1: Chroma key |
| Key2 Priority (3) | 1 | — | 0: 优先级1 / 1: 优先级2 / 3: 优先级3 |
| Key3 Type (4) | 1 | — | 0: PIP |
| Key3 Priority (5) | 1 | — | 0: 优先级1 / 1: 优先级2 / 3: 优先级3 |

---

## 3.2.4 LUMA 获取 0x0131

**说明：** 获取亮度抠像（Luma Key）参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| LUMA_TIE (0) | 1 | — | 0: Disable / 1: Enable |
| LUMA_STATUS (1) | 1 | — | 0: OFF / 1: KEY / 2: ONAIR / 3: KEY&ONAIR |
| FILL_SOC (2) | 1 | — | Fill 源：0.BLACK / 1.IN1 / 2.IN2 / 3.IN3 / 4.IN4 / 5.IN5 / 6.IN6 / 7.Color Bar |
| KEY_SOC (3) | 1 | — | Key 源：0.BLACK / 1.IN1 / 2.IN2 / 3.IN3 / 4.IN4 / 5.IN5 / 6.IN6 / 7.Color Bar |
| LUMA_SIZE (4) | 1 | — | Zoom size: 12-100 |
| LUMA_POSX (5) | 1 | — | Position X: 0~100 |
| LUMA_POSY (6) | 1 | — | Position Y: 0~100 |
| LUMA_CLIP (7) | 1 | — | 0~100 |
| LUMA_GAIN (8) | 1 | — | 0~100 |
| LUMA_INV (9) | 1 | — | 0: OFF / 1: ON |
| MASK_EN (10) | 1 | — | 0: OFF / 1: ON |
| LUMA_MASK_LEFT (11) | 1 | — | 0-50 |
| LUMA_MASK_TOP (12) | 1 | — | 0-50 |
| LUMA_MASK_RIGHT (13) | 1 | — | 50-100 |
| LUMA_MASK_BOTTOM (14) | 1 | — | 50-100 |

---

## 3.2.5 CHROMA 获取 0x0132

**说明：** 获取色度抠像（Chroma Key）参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| CHROMA_STATUS (0) | 1 | — | 0: OFF / 1: KEY / 2: ONAIR / 3: KEY&ONAIR |
| CHROMA_KEY_SOC (1) | 1 | — | Key 源：0.BLACK / 1.IN1 / 2.IN2 / 3.IN3 / 4.IN4 / 5.IN5 / 6.IN6 / 7.Color Bar |
| CHROMA_KEY_TYPE (2) | 1 | — | 0: Green / 1: Blue / 2: Red / 3: Custom / 4: Fetch |
| CHROMA_KEY_COLOR_R/G/B (3-5) | 3 | — | 抠像颜色 R/G/B，各 0~255 |
| CHROMA_KEY_FETCH_POS_X (6) | 2 | — | 取样点 X: 0~1920 |
| CHROMA_KEY_FETCH_POS_Y (7) | 2 | — | 取样点 Y: 0~1080 |
| CHROMA_SIZE (8) | 1 | — | Zoom size: 12-100 |
| CHROMA_POSX (9) | 1 | — | Position X: 0~100 |
| CHROMA_POSY (10) | 1 | — | Position Y: 0~100 |
| CHROMA_SIMILARITY (11) | 1 | — | 0~100 |
| CHROMA_SMOOTH (12) | 1 | — | 0~255 |
| CHROMA_SPILL (13) | 1 | — | 0~255 |
| CHROMA_OPACITY (14) | 1 | — | 0~100 |
| CHROMA_BRIGHTNESS (15) | 1 | — | 0~100 |
| CHROMA_CONTRAST (16) | 1 | — | 0~100 |
| CHROMA_SATURATION (17) | 1 | — | 0~100 |
| CHROMA_MASK_EN (18) | 1 | — | 0: OFF / 1: ON |
| CHROMA_MASK_LEFT (19) | 1 | — | 0-50 |
| CHROMA_MASK_TOP (20) | 1 | — | 0-50 |
| CHROMA_MASK_RIGHT (21) | 1 | — | 50-100 |
| CHROMA_MASK_BOTTOM (22) | 1 | — | 50-100 |

---

## 3.2.6 PIP1 获取 0x0133

**说明：** 获取画中画通道1的参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| PIP1_STATUS (0) | 1 | — | 0: OFF / 1: KEY / 2: ONAIR / 3: KEY&ONAIR |
| PIP1_SOC (1) | 1 | — | 源：0.BLACK / 1.IN1 / 2.IN2 / 3.IN3 / 4.IN4 / 5.IN5 / 6.IN6 / 7.Color Bar / 8.Color1 / 9.Color2 / 10.PAT1 / 11.PAT2 |
| PIP1_SIZE (2) | 1 | — | Zoom size: 12-100 |
| PIP1_POSX (3) | 1 | — | 0~100 |
| PIP1_POSY (4) | 1 | — | 0~100 |

---

## 3.2.7 PIP2 获取 0x0134

**说明：** 获取画中画通道2的参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| PIP2_STATUS (0) | 1 | — | 0: OFF / 1: KEY / 2: ONAIR / 3: KEY&ONAIR |
| PIP2_SOC (1) | 1 | — | 源：0.BLACK / 1.IN1 / 2.IN2 / 3.IN3 / 4.IN4 / 5.IN5 / 6.IN6 / 7.Color Bar / 8.Color1 / 9.Color2 / 10.PAT1 / 11.PAT2 |
| PIP2_SIZE (2) | 1 | — | Zoom size: 12-100 |
| PIP2_POSX (3) | 1 | — | 0~100 |
| PIP2_POSY (4) | 1 | — | 0~100 |

---

## 3.2.8 PIP3 获取 0x0135

**说明：** 获取画中画通道3的参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| PIP3_STATUS (0) | 1 | — | 0: OFF / 1: KEY / 2: ONAIR / 3: KEY&ONAIR |
| PIP3_SOC (1) | 1 | — | 源：0.BLACK / 1.IN1 / 2.IN2 / 3.IN3 / 4.IN4 / 5.IN5 / 6.IN6 / 7.Color Bar / 8.Color1 / 9.Color2 / 10.PAT1 / 11.PAT2 |
| PIP3_SIZE (2) | 1 | — | Zoom size: 12-100 |
| PIP3_POSX (3) | 1 | — | 0~100 |
| PIP3_POSY (4) | 1 | — | 0~100 |

---

## 3.2.9 PIP Border 获取 0x0136

**说明：** 获取画中画边框参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| PIP_BORDER_STATUS (0) | 1 | — | 0: OFF / 1: ON |
| PIP_BORDER_COLOR (1) | 1 | — | 0: White / 1: Red / 2: Green / 3: Blue / 4: Black |
| PIP_BORDER_WIDTH (2) | 1 | — | 0~15 |

---

## 3.2.10 DSK 获取 0x0140

**说明：** 获取下游键（Downstream Keyer）参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| DSK_TIE (0) | 1 | — | 0: OFF / 1: ON |
| DSK_STATUS (1) | 1 | — | 0: OFF / 1: KEY / 2: ONAIR / 3: KEY&ONAIR |
| DSK_FILL_SOC (2) | 1 | — | Fill 源：0.BLACK / 1.IN1 / 2.IN2 / 3.IN3 / 4.IN4 / 5.IN5 / 6.IN6 / 7.Color Bar |
| DSK_KEY_SOC (3) | 1 | — | Key 源：0.BLACK / 1.IN1 / 2.IN2 / 3.IN3 / 4.IN4 / 5.IN5 / 6.IN6 / 7.Color Bar |
| DSK_CLIP (4) | 1 | — | 0~100 |
| DSK_GAIN (5) | 1 | — | 0~100 |
| DSK_INV (6) | 1 | — | 0: OFF / 1: ON |
| DSK_MASK_EN (7) | 1 | — | 0: OFF / 1: ON |
| DSK_MASK_LEFT (8) | 1 | — | 0-50 |
| DSK_MASK_TOP (9) | 1 | — | 0-50 |
| DSK_MASK_RIGHT (10) | 1 | — | 50-100 |
| DSK_MASK_BOTTOM (11) | 1 | — | 50-100 |

---

## 3.2.11 LOGO 获取 0x0141

**说明：** 获取台标（LOGO）参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| LOGO_STATUS (0) | 1 | — | 0: OFF / 1: KEY / 2: ONAIR / 3: KEY&ONAIR |
| LOGO_SEL (1) | 1 | — | 0~7，选择 LOGO 样式 |
| LOGO_POSX (2) | 1 | — | 0~100 |
| LOGO_POSY (3) | 1 | — | 0~100 |
| LOGO_SIZE (4) | 1 | — | 5~20 |
| LOGO_OPACITY (5) | 1 | — | 20~100 |

---

## 3.2.12 Audio 获取 0x0150

**说明：** 获取全部音频参数，共 49 个参数（NO.0 ~ NO.48）。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| AUDIO_MUTE (0) | 1 | — | 0: OFF / 1: ON |
| AUDIO_ALL_AFV (1) | 1 | — | 0: OFF / 1: ON |
| AUDIO_RESET (2) | 1 | — | 1: En（复位） |
| AUDIO_MASTER_EN (3) | 1 | — | 0: OFF / 1: ON |
| AUDIO_MASTER_VOL (4) | 1 | — | 0-72 |
| AUDIO_EAR_EN (5) | 1 | — | 0: OFF / 1: ON |
| AUDIO_EAR_VOL (6) | 1 | — | 0-72 |
| AUDIO_EAR_SOC (7) | 1 | — | 0: PGM / 1: IN1 / 2: IN2 / 3: IN3 / 4: IN4 / 5: IN5 / 6: IN6 / 7: MIC1 / 8: MIC2 / 9: Line In |
| AUDIO_IN1_EN (8) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN1_VOL (9) | 1 | — | 0-72 |
| AUDIO_IN1_AFV (10) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN1_DELAY (11) | 1 | — | 0~100（显示 0~500ms） |
| AUDIO_IN2_EN (12) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN2_VOL (13) | 1 | — | 0-72 |
| AUDIO_IN2_AFV (14) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN2_DELAY (15) | 1 | — | 0~100（显示 0~500ms） |
| AUDIO_IN3_EN (16) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN3_VOL (17) | 1 | — | 0-72 |
| AUDIO_IN3_AFV (18) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN3_DELAY (19) | 1 | — | 0~100（显示 0~500ms） |
| AUDIO_IN4_EN (20) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN4_VOL (21) | 1 | — | 0-72 |
| AUDIO_IN4_AFV (22) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN4_DELAY (23) | 1 | — | 0~100（显示 0~500ms） |
| AUDIO_IN5_EN (24) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN5_VOL (25) | 1 | — | 0-72 |
| AUDIO_IN5_AFV (26) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN5_DELAY (27) | 1 | — | 0~100（显示 0~500ms） |
| AUDIO_IN6_EN (28) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN6_VOL (29) | 1 | — | 0-72 |
| AUDIO_IN6_AFV (30) | 1 | — | 0: OFF / 1: ON |
| AUDIO_IN6_DELAY (31) | 1 | — | 0~100（显示 0~500ms） |
| AUDIO_MIC_XLR_MODE (32) | 1 | — | 0: MIX / 1: XLR |
| AUDIO_MIC1_EN (33) | 1 | — | 0: OFF / 1: ON |
| AUDIO_MIC1_GUITAR (34) | 1 | — | 0: OFF / 1: ON |
| AUDIO_MIC1_PER_GAIN (35) | 1 | — | 0~14 |
| AUDIO_MIC1_VOL (36) | 1 | — | 0-72 |
| AUDIO_MIC1_DELAY (37) | 1 | — | 0~100（显示 0~500ms） |
| AUDIO_MIC2_EN (38) | 1 | — | 0: OFF / 1: ON |
| AUDIO_MIC2_GUITAR (39) | 1 | — | 0: OFF / 1: ON |
| AUDIO_MIC2_PER_GAIN (40) | 1 | — | 0~14 |
| AUDIO_MIC2_VOL (41) | 1 | — | 0-72 |
| AUDIO_MIC2_DELAY (42) | 1 | — | 0~100（显示 0~500ms） |
| AUDIO_XLR_EN (43) | 1 | — | 0: OFF / 1: ON |
| AUDIO_XLR_VOL (44) | 1 | — | 0-72 |
| AUDIO_XLR_DELAY (45) | 1 | — | 0~100（显示 0~500ms） |
| AUDIO_LINE_IN_EN (46) | 1 | — | 0: OFF / 1: ON |
| AUDIO_LINE_IN_VOL (47) | 1 | — | 0-72 |
| AUDIO_LINE_IN_DELAY (48) | 1 | — | 0~100（显示 0~500ms） |

---

## 3.2.13 VIEW 选择获取 0x0160

**说明：** 获取当前选中的 VIEW 通道。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| IN_VIEW_CONTROL (0) | 1 | — | 0: VIEW1 / 1: VIEW2 / 2: VIEW3 / 3: VIEW4 / 4: VIEW5 / 5: VIEW6 |

---

## 3.2.14 VIEW 设置获取 0x0161

**说明：** 获取全部 6 路 VIEW 的源通道、翻转方式及图像参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| VIEW1_SOC (0) | 1 | — | 0: IN1 / 1: IN2 / 2: IN3 / 3: IN4 / 4: IN5 / 5: IN6 |
| VIEW1_FILP (1) | 1 | — | 0: OFF / 1: Horizontal / 2: Vertical / 3: Rotate 180 |
| VIEW1_BRIGHTNESS (2) | 1 | — | 0~100 |
| VIEW1_CONTRAST (3) | 1 | — | 0~100 |
| VIEW1_SATURATION (4) | 1 | — | 0~100 |
| VIEW2_SOC (5) | 1 | — | 0: IN1 / 1: IN2 / 2: IN3 / 3: IN4 / 4: IN5 / 5: IN6 |
| VIEW2_FILP (6) | 1 | — | 0: OFF / 1: Horizontal / 2: Vertical / 3: Rotate 180 |
| VIEW2_BRIGHTNESS (7) | 1 | — | 0~100 |
| VIEW2_CONTRAST (8) | 1 | — | 0~100 |
| VIEW2_SATURATION (9) | 1 | — | 0~100 |
| VIEW3_SOC (10) | 1 | — | 0: IN1 / 1: IN2 / 2: IN3 / 3: IN4 / 4: IN5 / 5: IN6 |
| VIEW3_FILP (11) | 1 | — | 0: OFF / 1: Horizontal / 2: Vertical / 3: Rotate 180 |
| VIEW3_BRIGHTNESS (12) | 1 | — | 0~100 |
| VIEW3_CONTRAST (13) | 1 | — | 0~100 |
| VIEW3_SATURATION (14) | 1 | — | 0~100 |
| VIEW4_SOC (15) | 1 | — | 0: IN1 / 1: IN2 / 2: IN3 / 3: IN4 / 4: IN5 / 5: IN6 |
| VIEW4_FILP (16) | 1 | — | 0: OFF / 1: Horizontal / 2: Vertical / 3: Rotate 180 |
| VIEW4_BRIGHTNESS (17) | 1 | — | 0~100 |
| VIEW4_CONTRAST (18) | 1 | — | 0~100 |
| VIEW4_SATURATION (19) | 1 | — | 0~100 |
| VIEW5_SOC (20) | 1 | — | 0: IN1 / 1: IN2 / 2: IN3 / 3: IN4 / 4: IN5 / 5: IN6 |
| VIEW5_FILP (21) | 1 | — | 0: OFF / 1: Horizontal / 2: Vertical / 3: Rotate 180 |
| VIEW5_BRIGHTNESS (22) | 1 | — | 0~100 |
| VIEW5_CONTRAST (23) | 1 | — | 0~100 |
| VIEW5_SATURATION (24) | 1 | — | 0~100 |
| VIEW6_SOC (25) | 1 | — | 0: IN1 / 1: IN2 / 2: IN3 / 3: IN4 / 4: IN5 / 5: IN6 |
| VIEW6_FILP (26) | 1 | — | 0: OFF / 1: Horizontal / 2: Vertical / 3: Rotate 180 |
| VIEW6_BRIGHTNESS (27) | 1 | — | 0~100 |
| VIEW6_CONTRAST (28) | 1 | — | 0~100 |
| VIEW6_SATURATION (29) | 1 | — | 0~100 |
| VIEW_RESET (30) | 1 | — | 1: EN（复位） |
| FREEZE_CONTROL (31) | 1 | — | 0: pvw / 1: pgm |
| INPUT_SOC_IN5 (32) | 1 | — | 0: sdi / 1: hdmi |
| INPUT_SOC_IN6 (33) | 1 | — | 0: sdi / 1: hdmi |

---

## 3.2.15 MV 获取 0x0170

**说明：** 获取多画面分割（MultiView）布局与界面元素参数，分四个子组。

### Layout 组

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| LAYOUT_STYLE (0) | 1 | — | 0: Landscape / 1: Portrait |
| LAYOUT_PORT_POSX (1) | 1 | — | 0~100 |
| LAYOUT_PORT_POSY (2) | 1 | — | 0~100 |

### Audio Meter 组

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| AUDIO_METER_ALL_EN (3) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_IN1_EN (4) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_IN2_EN (5) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_IN3_EN (6) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_IN4_EN (7) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_IN5_EN (8) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_IN6_EN (9) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_PGM_EN (10) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_MIC_EN (11) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_LINE_IN_EN (12) | 1 | — | 0: OFF / 1: ON |
| AUDIO_METER_POS (13) | 1 | — | 0: Left / 1: Right |
| AUDIO_METER_OPACITY (14) | 1 | — | 0: 100 / 1: 75 / 2: 50 / 3: 25 |

### Input SOC 组

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| INPUT_SOC_EN (0) | 1 | — | 0: OFF / 1: ON |
| INPUT_SOC_OPACITY (1) | 1 | — | 0: 100 / 1: 75 / 2: 50 / 3: 25 |
| INPUT_SOC_POSX (2) | 1 | — | 0~100 |
| INPUT_SOC_POSY (3) | 1 | — | 0~100 |
| INPUT_SOC_TEXT_COLOR_R/G/B (4-6) | 3 | — | 文字颜色 R/G/B，各 0~255 |
| INPUT_SOC_BG_COLOR_R/G/B (7-9) | 3 | — | 背景颜色 R/G/B，各 0~255 |

### UMD 组

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| UMD_EN (0) | 1 | — | 0: OFF / 1: ON |
| UMD_OPACITY (1) | 1 | — | 0: 100 / 1: 75 / 2: 50 / 3: 25 |
| UMD_POSX (2) | 1 | — | 0~100 |
| UMD_POSY (3) | 1 | — | 0~100 |
| UMD_TEXT_COLOR_R/G/B (4-6) | 3 | — | 文字颜色 R/G/B，各 0~255 |
| UMD_BG_COLOR_R/G/B (7-9) | 3 | — | 背景颜色 R/G/B，各 0~255 |

---

## 3.2.16 UMD 字符获取 0x0171

**说明：** 获取各输入通道及 PGM/PVW 的 UMD 字符标签，每项最长 8 个字符（20 字节）。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| UMD_STRING_IN1 (0) | 20 | — | IN1 通道标签，最长 8 个字符 |
| UMD_STRING_IN2 (1) | 20 | — | IN2 通道标签 |
| UMD_STRING_IN3 (2) | 20 | — | IN3 通道标签 |
| UMD_STRING_IN4 (3) | 20 | — | IN4 通道标签 |
| UMD_STRING_IN5 (4) | 20 | — | IN5 通道标签 |
| UMD_STRING_IN6 (5) | 20 | — | IN6 通道标签 |
| UMD_STRING_IN7 (6) | 20 | — | IN7 通道标签 |
| UMD_STRING_IN8 (7) | 20 | — | IN8 通道标签 |
| UMD_STRING_PVW (8) | 20 | — | PVW 标签 |
| UMD_STRING_PGM (9) | 20 | — | PGM 标签 |

---

## 3.2.17 Library 获取 0x0180

**说明：** 获取图案库（Pattern Library）配置参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| LIBRARY_PATTERN_1 (0) | 1 | — | 0: Black / 1: Color Bar / 2: Color 1 / 3: Color 2 / 4: Image 1 / 5: Image 2 |
| LIBRARY_PATTERN_2 (1) | 1 | — | 同上 |
| LIBRARY_IMAGE_PATH (2) | 1 | — | 0: SD Card / 1: USB Storage |
| PATTERN_COLOR1_HUE (4) | 2 | — | 0~360 |
| PATTERN_COLOR1_LUMINANCE (5) | 1 | — | 0~100 |
| PATTERN_COLOR1_SATURATION (6) | 1 | — | 0~100 |
| PATTERN_COLOR2_HUE (7) | 2 | — | 0~360 |
| PATTERN_COLOR2_LUMINANCE (8) | 1 | — | 0~100 |
| PATTERN_COLOR2_SATURATION (9) | 1 | — | 0~100 |

---

## 3.2.18 Output 获取 0x0190

**说明：** 获取输出路由、格式及画面参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| OUTPUT_SOC_HDMI_OUT_1 (0) | 1 | — | 0.IN1 / 1.IN2 / 2.IN3 / 3.IN4 / 4.IN5 / 5.IN6 / 6.PGM / 7.Clear PGM / 8.PVW / 9.Color Bar / 10.Mutiview |
| OUTPUT_SOC_SDI_OUT_2 (1) | 1 | — | 同上（0-10） |
| OUTPUT_SOC_SDI_OUT_3 (2) | 1 | — | 同上（0-10） |
| OUTPUT_SOC_STREAM_OUT (3) | 1 | — | 0.IN1 / 1.IN2 / 2.IN3 / 3.IN4 / 4.IN5 / 5.IN6 / 6.PGM / 7.Clear PGM / 8.PVW / 9.Color Bar |
| OUTPUT_SOC_LCD_OUT (4) | 1 | — | 0: MV / 1: PGM |
| OUTPUT_SOC_UVC_OUT (5) | 1 | — | 0.IN1 / 1.IN2 / 2.IN3 / 3.IN4 / 4.IN5 / 5.IN6 / 6.PGM / 7.Clear PGM / 8.PVW / 9.Color Bar |
| OUTPUT_FRAME_RATE_MODE (6) | 1 | — | 0: Integer / 1: Decimal |
| OUTPUT_FORMAT_HDMI_OUT_1 (7) | 1 | — | 0:1080i50 / 1:1080i60 / 2:1080p24 / 3:1080p25 / 4:1080p30 / 5:1080p50 / 6:1080p60 |
| OUTPUT_FORMAT_SDI_OUT_2 (8) | 1 | — | 同上（0-6） |
| OUTPUT_FORMAT_SDI_OUT_3 (9) | 1 | — | 同上（0-6） |
| OUTPUT_COLOR_SPACE (10) | 1 | — | 0: RGB FULL / 1: RGB LIMIT / 2: YUV |
| OUTPUT_BRIGHTNESS (11) | 1 | — | 0~100 |
| OUTPUT_CONTRAST (12) | 1 | — | 0~100 |
| OUTPUT_SATURATION (13) | 1 | — | 0~100 |
| FTB_MUTE_SPEED (14) | 1 | — | 0~30（显示 0.0~3.0） |
| FTB_WITH_MUTE (15) | 1 | — | 0: OFF / 1: ON |

---

## 3.2.19 Codec 获取 0x01A0

**说明：** 获取编码、码率控制及录制参数。

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| ENCOD_BITRATE (0) | 1 | — | 0:256Kbps / 1:512Kbps / 2:1Mbps / 3:2Mbps / 4:4Mbps / 5:8Mbps / 6:12Mbps / 7:16Mbps / 8:24Mbps / 9:32Mbps |
| ENCOD_RATE_CONTROL (1) | 1 | — | 0: CBR / 1: VBR |
| ENCOD_VIDEO_ENCODING (2) | 1 | — | 0: H.264 High / 1: H.264 Main / 2: H.264 Base / 3: H.265 |
| ENCOD_RES (3) | 1 | — | 0: 1920x1080 / 1: 1280x720 / 2: 720x480 |
| ENCOD_FPS (4) | 1 | — | 0: 24 / 1: 25 / 2: 30 / 3: 50 / 4: 60 |
| ENCOD_I_FRAME (5) | 2 | — | 5~300（I 帧间隔） |
| ENCOD_VOL (6) | 1 | — | 0~100 |
| ENCOD_SAMPLING_RATE (7) | 1 | — | 0: 48KHz |
| ENCOD_AUDIO_BITRATE (8) | 1 | — | 0: 64Kbps / 1: 128Kbps / 2: 256Kbps / 3: 320Kbps |
| STREAM_1_EN (9) | 1 | — | 0: OFF / 1: ON |
| STREAM_2_EN (10) | 1 | — | 0: OFF / 1: ON |
| STREAM_3_EN (11) | 1 | — | 0: OFF / 1: ON |
| RECORD_FILL_FORMAT (12) | 1 | — | 0: TS / 1: MP4 |
| RECORD_OVERWRITE (13) | 1 | — | 0: OFF / 1: ON |
| RECORD_STORAGE (14) | 1 | — | 0: SD Card / 1: USB Storage |
| RECORD_FORMAT (15) | 1 | — | 0: OFF / 1: ON |

---

## 3.2.20 SYSTEM 获取 0x01B0

**说明：** 获取系统全部配置，包含语言、风扇、温度单位、快捷键、屏幕、网络、时间、定时器等。

### 基础配置

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| SYSTEM_LANGUAGE (0) | 1 | — | 0: English / 1: 简体中文 / 2: 繁體中文 / 3: Português |
| SYSTEM_FAN (1) | 1 | — | 0: AUTO / 1: Manual / 2: OFF |
| SYSTEM_TEMA_MODE (2) | 1 | — | 0: 摄氏度 / 1: 华氏度 |
| SYSTEM_RESET (3) | 1 | — | 0: Reset Preference / 1: Factory Reset |
| SYSTEM_POWER_MODE (4) | 1 | — | 0: Power On / 1: Last state |

### 快捷键配置（F1~F6 短按/长按）

每个功能键包含 SHORT_PRESS 和 LONG_PRESS 两个参数，取值范围相同：

| 值 | 含义 |
|---|---|
| 0 | NONE |
| 1 | REC M |
| 2 | Call M |
| 3 | Key1 Mask |
| 4 | Key2 Mask |
| 5 | DSK Mask |
| 6 | Timer |
| 7 | Clr Display |

| 字段 | 字节数 |
|---|---|
| SHORTCUT_F1_SHORT_PRESS (5) | 1 |
| SHORTCUT_F1_LONG_PRESS (6) | 1 |
| SHORTCUT_F2_SHORT_PRESS (7) | 1 |
| SHORTCUT_F2_LONG_PRESS (8) | 1 |
| SHORTCUT_F3_SHORT_PRESS (9) | 1 |
| SHORTCUT_F3_LONG_PRESS (10) | 1 |
| SHORTCUT_F4_SHORT_PRESS (11) | 1 |
| SHORTCUT_F4_LONG_PRESS (12) | 1 |
| SHORTCUT_F5_SHORT_PRESS (13) | 1 |
| SHORTCUT_F5_LONG_PRESS (14) | 1 |
| SHORTCUT_F6_SHORT_PRESS (15) | 1 |
| SHORTCUT_F6_LONG_PRESS (16) | 1 |

### 屏幕参数

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| SCREEN_BRIGHTNESS (18) | 1 | — | 0~100 |
| SCREEN_CONTRAST (19) | 1 | — | 0~100 |
| SCREEN_SATURATION (20) | 1 | — | 0~100 |
| SCREEN_COLOR_CAST (21) | 1 | — | 0~100 |
| SCREEN_SHARPNESS (22) | 1 | — | 0~100 |
| SCREEN_COLOR_TEMP (26) | 1 | — | 0: 6500K / 1: 7500K / 2: 9300K / 3: USER |
| SCREEN_RED_GAIN (27) | 1 | — | 0~255 |
| SCREEN_GREEN_GAIN (28) | 1 | — | 0~255 |
| SCREEN_BLUE_GAIN (29) | 1 | — | 0~255 |
| SCREEN_RED_OFFSET (30) | 1 | — | 0~255 |
| SCREEN_GREEN_OFFSET (31) | 1 | — | 0~255 |
| SCREEN_BLUE_OFFSET (32) | 1 | — | 0~255 |

### 网络参数

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| IP_DHCP (33) | 1 | — | 0: OFF / 1: ON |
| IP_IP (34) | 4 | — | IP 地址 |
| IP_SUBNET (35) | 4 | — | 子网掩码 |
| IP_GATEWAY (36) | 4 | — | 网关 |

### 时间与定时

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| CLOCK_FORMAT (37) | 1 | — | 0: 12H / 1: 24H |
| TIME_SYNC (38) | 1 | — | 0: NTP / 1: MANUAL |
| TIME_ZONE (39) | 1 | — | 0~37，对应 UTC-12:00 ~ UTC+14:00 |
| DATE_TIME (40) | 6 | — | 日期时间 |
| TIMER_TYPE (41) | 1 | — | 0: TIMER / 1: Countdown |
| TIMER_HOUR (42) | 1 | — | 0~100 |
| TIMER_MIN (43) | 1 | — | 0~59 |
| TIMER_SEC (44) | 1 | — | 0~59 |

---

## 附：同步协议指令码总表

| 指令码 | 名称 | 方向 | 备注 |
|---|---|---|---|
| 0x0110 | 按键获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0120 | Transition 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0130 | KEY 源获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0131 | LUMA 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0132 | CHROMA 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0133 | PIP1 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0134 | PIP2 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0135 | PIP3 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0136 | PIP Border 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0140 | DSK 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0141 | LOGO 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0150 | Audio 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0160 | VIEW 选择获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0161 | VIEW 设置获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0170 | MV 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0171 | UMD 字符获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0180 | Library 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x0190 | Output 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x01A0 | Codec 获取 | 双向 | 含上位机获取 + 设备主动上报 |
| 0x01B0 | SYSTEM 获取 | 双向 | 含上位机获取 + 设备主动上报 |

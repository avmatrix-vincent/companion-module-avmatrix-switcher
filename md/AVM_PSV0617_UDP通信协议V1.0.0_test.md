---
title: AVM UDP通信协议（PSV0617）
subtitle: 版本 V1.0.0
---

# AVM UDP通信协议

**PSV0617（0x08）**

## 更新记录

| 版本 | 时间 | 更新内容 | 作者 |
|---|---|---|---|
| V1.0.0 | 20260731 | 初稿。 | YC |

## 1、协议报文结构

协议版本v1.0

表1 上位机发送的报文结构：

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Head | 2 | 0xA5  0x5A | 包头标识 |
| Protocol_Version | 2 | -- | 大端（高位在前），协议版本号，例如：01 00，标识版本为：V1.0 |
| Length | 2 | -- | 包含Head->Tail的长度：25+n+4 |
| index | 2 | -- | 大端（高位在前），数据包序号 |
| Padding | 8 | [0x00]*8 | 填充8字节的0值 |
| Pack_Type | 1 | -- | 数据包类型<br>0：上位机发送CMD给设备<br>1：设备回应CMD Response给上位机<br>2：设备主动上报Report给上位机 |
| CMD | 2 | -- | 大端（高位在前），指令码，见第2节。 |
| Session | 4 | -- | 用于确保回应与请求是一一对应的，可用随机数或按顺序产生。 |
| Data_Length | 2 |  | 大端（高位在前），数据长度 |
| Data | n | -- | 最大不超过65535字节长度的数据，针对不同设备的主控芯片，可以自行规定最大长度 |
| Sum | 2 | -- | 大端（高位在前），25+n长度的数据进行字节和校验 |
| Tail | 2 | 0xA6  0x6A | 包结尾符 |

## 2、协议指令集

### 2.1、0617指令集

| 命令值 | 说明 |
|---|---|
| 0x0001 | 获取版本信息，mcu版本，mdin640版本，keyboard版本，PCB版本 |
|  |  |
| 0x0010 | 按键控制指令 |
|  |  |
| 0x0020 | Transition 设置 |
|  |  |
| 0x0030 | KEY源设置 |
| 0x0031 | Luma设置 |
| 0x0032 | Chroma 设置 |
| 0x0033 | PIP1  设置 |
| 0x0034 | PIP2  设置 |
| 0x0035 | PIP3  设置 |
| 0x0036 | PIP Border设置 |
|  |  |
| 0x0040 | DSK设置 |
| 0x0041 | Logo设置 |
|  |  |
| 0x0050 | Audio设置 |
| 0x0060 | View 选择 |
| 0x0061 | View 设置 |
| 0x0070 | MV 设置 |
| 0x0071 | UMD Text 设置 |
|  |  |
| 0x0080 | Library设置 |
| 0x0090 | Output设置 |
| 0x00A0 | Codec设置 |
| 0x00B0 | System设置 |
|  |  |
| 0x0110 | 获取按键控制指令（此指令包括上位机主动获取数据和设备主动上报数据） |
|  |  |
| 0x0120 | Transition 获取（此指令包括上位机主动获取数据和设备主动上报数据） |
|  |  |
| 0x0130 | KEY源获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0131 | Luma获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0132 | Chroma 获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0133 | PIP1  获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0134 | PIP2  获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0135 | PIP3  获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0136 | PIP Border获取（此指令包括上位机主动获取数据和设备主动上报数据） |
|  |  |
| 0x0140 | DSK获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0141 | Logo获取（此指令包括上位机主动获取数据和设备主动上报数据） |
|  |  |
| 0x0150 | Audio获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0160 | Input获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0170 | MV获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0180 | Library获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x0190 | Output获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x01A0 | Codec获取（此指令包括上位机主动获取数据和设备主动上报数据） |
| 0x01B0 | System获取（此指令包括上位机主动获取数据和设备主动上报数据） |
|  |  |

## 3、详细指令

指令的报文结构可参考：表1 上位机发送的报文结构，此处仅针对Data部分进行详述。

## 3.1、控制协议

### 3.1.1、读取版本号指令0x0001

#### 指令0x0001回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| System版本 | 4 | -- |  |
| Image版本 | 4 | -- |  |
| Keys版本 | 4 | -- |  |
| Display版本 | 4 | -- |  |
| Hardware版本 | 2 | -- |  |

### 3.1.2、按键控制指令 0x0010

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | -- | 指示设置哪个参数（NO.0-2） |
| Key_val（NO.0） | 2 | -- | 按键对应的值（按键值对应请查看键值对应表） |
| T_Bar_val（NO.1） | 2 | -- | 推杆数据（值的范围0~4095） |
| b_bar_pos（NO.2） | 2 | -- | 推杆的位置<br>0：底部<br>1：中间<br>2：顶部 |

#### 指令0x0010回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

#### 键值对应表

| 1~8 | PGM1~6、PGM pattern1、PGM pattern2 |
|---|---|
| 9~16 | PVW1~6、PVW pattern1、PVW pattern2 |
| 17 | CUT |
| 18 | Auto |
| 19 | FTB |
| 20 | Mute |
| 21~22 | Speed1、Speed2 |
| 23 | REC |
| 24~26 | Stream1~3 |
| 27~30 | Wipe1~4 |
| 31 | MIX |
| 32 | DIP |
| 33 | FREEZE |
| 34-39 | F1~F6 |

### 3.1.3、Transition 设置  0x0020

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | -- | 指示设置哪个参数（NO.0-11） |
| Wipe 1(NO.0) | 1 | -- | 划像1 (样式0-10) |
| Wipe 2(NO.1) | 1 | -- | 划像2 (样式0-10) |
| Wipe 3(NO.2) | 1 | -- | 划像3 (样式0-10) |
| Wipe 4(NO.3) | 1 | -- | 划像4 (样式0-10) |
| Softness(NO.4) | 1 | -- | 柔化度 0-100 |
| Direction(NO.5) | 1 | -- | 方向<br>0：Normal<br>1：Invert<br>2：Flip-Flop |
| MIX(NO.6) | 1 | -- | 方向<br>0：OFF<br>1：ON |
| Dir Color R(NO.7)<br>Dir Color G<br>Dir Color B | 3 |  | 0-255<br>0-255<br>0-255 |
| Speed 1(NO.8) | 1 | -- | 速率1<br>1-80 |
| Speed 2(NO.9) | 1 | -- | 速率2<br>1-80 |
| T-Bar A/BMode(NO.10) | 1 | -- | A/B模式<br>0：OFF<br>1:ON |
| T-Bar Status(NO.11) | 1 | -- | 推杆状态<br>0：OFF<br>1:ON |

#### 指令0x0020回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.4、KEY源设置  0x0030

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | -- | 指示设置哪个参数（NO.0-5） |
| Key1 Type（0） | 1 | -- | 0：PIP<br>1：Luma key |
| Key1 Priority（1） | 1 | -- | 0：优先级1<br>1：优先级2<br>3：优先级3 |
| Key2 Type（2） | 1 | -- | 0：PIP<br>1：Chroma key |
| Key2 Priority（3） | 1 | -- | 0：优先级1<br>1：优先级2<br>3：优先级3 |
| Key3 Type（4） | 1 | -- | 0：PIP |
| Key3 Priority（5） | 1 | -- | 0：优先级1<br>1：优先级2<br>3：优先级3 |

#### 指令0x0030回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.5、LUMA设置  0x0031

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | -- | 指示设置哪个参数（NO.0-15） |
| LUMA_TIE(0) | 1 | -- | 0：Disbale<br>1：Enable |
| LUMA_STATUS(1) | 1 | -- | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| FILL_SOC(2) | 1 | -- | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7：Color Bar |
| KEY_SOC(3) | 1 | -- | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7：Color Bar |
| LUMA_SIZE(4) | 1 | -- | Zoom size ：12-100 |
| LUMA_POSX(5) | 1 | -- | Position X: 0~100 |
| LUMA_POSY(6) | 1 | -- | Position Y: 0~100 |
| LUMA_CLIP(7) | 1 | -- | 0~100 |
| LUMA_GAIN(8) | 1 | -- | 0~100 |
| LUMA_INV(9) | 1 | -- | 0:OFF<br>1:ON |
| MASK_EN(10) | 1 | -- | 0:OFF<br>1:ON |
| LUMA_MASK_LEFT(11) | 1 | -- | 0-50 |
| LUMA_MASK_TOP(12) | 1 | -- | 0-50 |
| LUMA_MASK_RIGHT(13) | 1 | -- | 50-100 |
| LUMA_MASK_BOTTOM(14) | 1 | -- | 50-100 |
| LUMA_RESET(15) | 1 | -- | 1：EN |

#### 指令0x0031回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.6、CHROMA设置  0x0032

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-21） |
| CHROMA_STATUS(0) | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| CHROMA_KEY_SOC(1) | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7：Color Bar |
| CHROMA_KEY_TYPE(2) | 1 | - | 0： Green<br>1： Blue<br>2:  Red<br>3:  Custom<br>4:  Fetch |
| CHROMA_KEY_COLOR_R(3)<br>CHROMA_KEY_COLOR_G<br>CHROMA_KEY_COLOR_B | 3 | - | 0~255<br>0~255<br>0~255 |
| CHROMA_KEY_FETCH_POS_X(4) | 2 | - | 0~1920 |
| CHROMA_KEY_FETCH_POS_Y(5) | 2 | - | 0~1080 |
| CHROMA_SIZE(6) | 1 | - | Zoom size ：12-100 |
| CHROMA_POSX(7) | 1 | - | Position X: 0~100 |
| CHROMA_POSY(8) | 1 | - | PositionY: 0~100 |
| CHROMA_SIMILARITY,(9) | 1 | - | 0~100 |
| CHROMA_SMOOTH(10) | 1 | - | 0~255 |
| CHROMA_SPILL(11) | 1 | - | 0~255 |
| CHROMA_OPACITY,(12) | 1 | - | 0~100 |
| CHROMA_BRIGHTNESS(13) | 1 | - | 0~100 |
| CHROMA_CONTRAST,(14) | 1 | - | 0~100 |
| CHROMA_SATURATION,(15) | 1 | - | 0~100 |
| CHROMA_MASK_EN,(16) | 1 | - | 0:OFF<br>1:ON |
| CHROMA_MASK_LEFT,(17) | 1 | - | 0-50 |
| CHROMA_MASK_TOP,(18) | 1 | - | 0-50 |
| CHROMA_MASK_RIGHT,(19) | 1 | - | 50-100 |
| CHROMA_MASK_BOTTOM,(20) | 1 | - | 50-100 |
| CHROMA_RESET,(21) | 1 | - | 1：EN |

#### 指令0x0032回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.7、PIP1设置  0x0033

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-5） |
| PIP1_STATUS（0） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| PIP1_SOC（1） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar<br>8:  Color 1<br>9:  Color 2<br>10:  PAT 1<br>11:  PAT2 |
| PIP1_SIZE（2） | 1 | - | Zoom size ：12-100 |
| PIP1_POSX（3） | 1 | - | 0~100 |
| PIP1_POSY（4） | 1 | - | 0~100 |
| PIP1_RESET（5） | 1 | - | En:1 |

#### 指令0x0033回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.8、PIP2设置  0x0034

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-5） |
| PIP2_STATUS（0） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| PIP2_SOC（1） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar<br>8:  Color 1<br>9:  Color 2<br>10:  PAT 1<br>11:  PAT2 |
| PIP2_SIZE（2） | 1 | - | Zoom size ：12-100 |
| PIP2_POSX（3） | 1 | - | 0~100 |
| PIP2_POSY（4） | 1 | - | 0~100 |
| PIP2_RESET（5） | 1 | - | En:1 |

#### 指令0x0034回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.9、PIP3设置  0x0035

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-5） |
| PIP3_STATUS（0） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| PIP3_SOC（1） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar<br>8:  Color 1<br>9:  Color 2<br>10:  PAT 1<br>11:  PAT2 |
| PIP3_SIZE（2） | 1 | - | Zoom size ：12-100 |
| PIP3_POSX（3） | 1 | - | 0~100 |
| PIP3_POSY（4） | 1 | - | 0~100 |
| PIP3_RESET（5） | 1 | - | En:1 |

#### 指令0x0035回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.9、PIP Border设置  0x0036

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-2） |
| PIP_BORDER_STATUS（0） | 1 | - | 0：OFF<br>1：ON |
| PIP_BORDER_COLOR（1） | 1 | - | 0:  White<br>1:  Red<br>2:  Green<br>3:  Blue<br>4:  Black |
| PIP_BORDER_WIDTH（2） | 1 | - | 0~15 |

#### 指令0x0036回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.10、DSK设置  0x0040

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-12） |
| DSK_TIE（0） | 1 | - | 0：OFF<br>1：ON |
| DSK_STATUS（1） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| DSK_FILL_SOC（2） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar |
| DSK_KEY_SOC（3） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar |
| DSK_CILP（4） | 1 |  | 0~100 |
| DSK_GAIN（5） | 1 |  | 0~100 |
| DSK_INV（6） | 1 |  | 0：OFF<br>1：ON |
| DSK_MASK_EN（7） |  |  | 0:OFF<br>1:ON |
| DSK_MASK_LEFT（8） | 1 |  | 0-50 |
| DSK_MASK_TOP（9） | 1 |  | 0-50 |
| DSK_MASK_RIGHT（10） | 1 |  | 50-100 |
| DSK_MASK_BOTTOM（11） | 1 |  | 50-100 |
| DSK_RESET（12） | 1 |  | 1：EN |

#### 指令0x0040回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.11、LOGO设置  0x0041

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-6） |
| LOGO_STATUS（0） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| LOGO_SEL（1） | 1 | - | 0~7选择LOGO样式 |
| LOGO_POSX（2） | 1 |  | 0~100 |
| LOGO_POSY（3） | 1 |  | 0~100 |
| LOGO_SIZE（4） | 1 |  | 5 ~20 |
| LOGO_OPACITY（5） | 1 |  | 20~100 |
| LOGO_RESET（6） | 1 |  | 1：EN |

#### 指令0x0041回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.12、Audio设置  0x0050

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-48） |
| AUDIO_MUTE（0） | 1 | - | 0：OFF<br>1：ON |
| AUDIO_ALL_AFV（1） | 1 | - | 0：OFF<br>1：ON |
| AUDIO_RESET（2） | 1 |  | 1：En |
| AUDIO_MASTER_EN（3） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_MASTER_VOL（4） | 1 |  | 0~72 |
| AUDIO_EAR_EN（5） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_EAR_VOL（6） | 1 |  | 0~72 |
| AUDIO_EAR_SOC（7） | 1 |  | 0:  PGM<br>1:  IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7:  MIC 1<br>8:  MIC 2<br>9:  Line In |
| AUDIO_IN1_EN（8） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN1_VOL（9） | 1 |  | 0~72 |
| AUDIO_IN1_AFV（10） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN1_DELAY（11） | 1 |  | 0~100（显示0~500） |
| AUDIO_IN2_EN（12） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN2_VOL（13） | 1 |  | 0~72 |
| AUDIO_IN2_AFV（14） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN2_DELAY（15） | 1 |  | 0~100（显示0~500） |
| AUDIO_IN3_EN（16） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN3_VOL（17） | 1 |  | 0~72 |
| AUDIO_IN3_AFV（18） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN3_DELAY（19） | 1 |  | 0~100（显示0~500） |
| AUDIO_IN4_EN（20） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN4_VOL（21） | 1 |  | 0~72 |
| AUDIO_IN4_AFV（22） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN4_DELAY（23） | 1 |  | 0~100（显示0~500） |
| AUDIO_IN5_EN（24） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN5_VOL（25） | 1 |  | 0~72 |
| AUDIO_IN5_AFV（26） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN5_DELAY（27） | 1 |  | 0~100（显示0~500） |
| AUDIO_IN6_EN（28） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN6_VOL（29） | 1 |  | 0~72 |
| AUDIO_IN6_AFV（30） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_IN6_DELAY（31） | 1 |  | 0~100（显示0~500） |
| AUDIO_MIC_XLR_MODE（32） | 1 |  | 0: MIX<br>1: XLR |
| AUDIO_MIC1_EN（33） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_MIC1_GUITAR（34） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_MIC1_PER_GAIN（35） | 1 |  | 0~14 |
| AUDIO_MIC1_VOL（36） | 1 |  | 0~72 |
| AUDIO_MIC1_DELAY（37） | 1 |  | 0~100（显示0~500） |
| AUDIO_MIC2_EN（38） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_MIC2_GUITAR（39） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_MIC2_PER_GAIN（40） | 1 |  | 0~14 |
| AUDIO_MIC2_VOL（41） | 1 |  | 0~72 |
| AUDIO_MIC2_DELAY（42） | 1 |  | 0~100（显示0~500） |
| AUDIO_XLR_EN（43） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_XLR_VOL（44） | 1 |  | 0~72 |
| AUDIO_XLR_DELAY（45） | 1 |  | 0~100（显示0~500） |
| AUDIO_LINE_IN_EN（46） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_LINE_IN_VOL（47） | 1 |  | 0~72 |
| AUDIO_LINE_IN_DELAY（48） | 1 |  | 0~100（显示0~500） |

#### 指令0x0050回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.13、VIEW选择  0x0060

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0） |
| IN_VIEW_CONTROL（0） | 1 | - | 0：VIEW1<br>1：VIEW2<br>2：VIEW3<br>3：VIEW4<br>4：VIEW5<br>5：VIEW6 |

#### 指令0x0060回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.14、VIEW设置  0x0061

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-33） |
| VIEW1_SOC（0） | 1 | - | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW1_FILP（1） | 1 |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW1_BRIGHTNESS（2） | 1 |  | 0~100 |
| VIEW1_CONTRAST（3） | 1 |  | 0~100 |
| VIEW1_SATURATION（4） | 1 |  | 0~100 |
| VIEW2_SOC（5） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW2_FILP（6） | 1 |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW2_BRIGHTNESS（7） | 1 |  | 0~100 |
| VIEW2_CONTRAST（8） | 1 |  | 0~100 |
| VIEW2_SATURATION（9） | 1 |  | 0~100 |
| VIEW3_SOC（10） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW3_FILP（11） | 1 |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW3_BRIGHTNESS（12） | 1 |  | 0~100 |
| VIEW3_CONTRAST（13） | 1 |  | 0~100 |
| VIEW3_SATURATION（14） | 1 |  | 0~100 |
| VIEW4_SOC（15） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW4_FILP（16） | 1 |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW4_BRIGHTNESS（17） | 1 |  | 0~100 |
| VIEW4_CONTRAST（18） | 1 |  | 0~100 |
| VIEW4_SATURATION（19） | 1 |  | 0~100 |
| VIEW5_SOC（20） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW5_FILP（21） | 1 |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW5_BRIGHTNESS（22） | 1 |  | 0~100 |
| VIEW5_CONTRAST（23） | 1 |  | 0~100 |
| VIEW5_SATURATION（24） | 1 |  | 0~100 |
| VIEW6_SOC（25） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW6_FILP（26） | 1 |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW6_BRIGHTNESS（27） | 1 |  | 0~100 |
| VIEW6_CONTRAST（28） | 1 |  | 0~100 |
| VIEW6_SATURATION（29） | 1 |  | 0~100 |
| VIEW_RESET（30） | 1 |  | 1：EN |
| FREEZE_CONTROL（31） | 1 |  | 0：pvw<br>1：pgm |
| INPUT_SOC_IN5（32） | 1 |  | 0：sdi<br>1：hdmi |
| INPUT_SOC_IN6（33） | 1 |  | 0：sdi<br>1：hdmi |

#### 指令0x0061回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.15、MV设置  0x0070

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-33） |
| LAYOUT_STYLE（0） | 1 | - | 0：Landscape<br>1：Portrain |
| LAYOUTPORT_POSX（1） | 1 |  | 0~100 |
| LAYOUTPORT_POSY（2） | 1 |  | 0~100 |
| AUDIO_METER_ALL_EN（3） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN1_EN（4） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN2_EN（5） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN3_EN（6） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN4_EN（7） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN5_EN（8） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN6_EN（9） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_PGM_EN（10） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_MIC_EN（11） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_LINE_IN_EN（12） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_METER_POS（13） | 1 |  | 0：Left<br>1：Right |
| AUDIO_METER_OPACITY（14） | 1 |  | 0：100<br>1：75<br>2：50<br>3：25 |
| INPUT_SOC_EN（15） | 1 |  | 0：OFF<br>1：ON |
| INPUT_SOC_OPACITY（16） | 1 |  | 0：100<br>1：75<br>2：50<br>3：25 |
| INPUT_SOC_POSX（17） | 1 |  | 0~100 |
| INPUT_SOC_POSY（18） | 1 |  | 0~100 |
| INPUT_SOC_TEXT_COLOR_R（19）<br>INPUT_SOC_TEXT_COLOR_G<br>INPUT_SOC_TEXT_COLOR_B | 3 |  | 0~255<br>0~255<br>0~255 |
| INPUT_SOC_BG_COLOR_R（20）<br>INPUT_SOC_BG_COLOR_G<br>INPUT_SOC_BG_COLOR_B | 3 |  | 0~255<br>0~255<br>0~255 |
| UMD_EN（21） | 1 |  | 0：OFF<br>1：ON |
| UMD_OPACITY（22） | 1 |  | 0：100<br>1：75<br>2：50<br>3：25 |
| UMD_POSX（23） | 1 |  | 0~100 |
| UMD_POSY（24） | 1 |  | 0~100 |
| UMD_TEXT_COLOR_R（25）<br>UMD_TEXT_COLOR_G<br>UMD_TEXT_COLOR_B | 3 |  | 0~255<br>0~255<br>0~255 |
| UMD_BG_COLOR_R（26）<br>UMD_BG_COLOR_G<br>UMD_BG_COLOR_B | 3 |  | 0~255<br>0~255<br>0~255 |

#### 指令0x0070回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.16、UMD 字符设置  0x0071

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-9） |
| UMD_STRING_IN1（0） | 20 | - | 最长8个字符 |
| UMD_STRING_IN2（1） | 20 |  |  |
| UMD_STRING_IN3（2） | 20 |  |  |
| UMD_STRING_IN4（3） | 20 |  |  |
| UMD_STRING_IN5（4） | 20 |  |  |
| UMD_STRING_IN6（5） | 20 |  |  |
| UMD_STRING_IN7（6） | 20 |  |  |
| UMD_STRING_IN8（7） | 20 |  |  |
| UMD_STRING_PVW（8） | 20 |  |  |
| UMD_STRING_PGM（9） | 20 |  |  |

#### 指令0x0071回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.17、Library设置  0x0080

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-12） |
| LIBRARY_PATTERN_1（0） | 1 | - | 0：Black<br>1：Color Bar<br>2：Color 1<br>3：Color 2<br>4：Image 1<br>5：Image 2 |
| LIBRARY_PATTERN_2（1） | 1 |  | 0：Black<br>1：Color Bar<br>2：Color 1<br>3：Color 2<br>4：Image 1<br>5：Image 2 |
| LIBRARY_IMAGE_PATH（2） | 1 |  | 0：SD Card<br>1：USB Storage |
| LIBRARY_IMAGE_CAPTURE（3） | 1 |  | 1：En |
| PATTERN_COLOR1_HUE（4） | 2 |  | 0 ~ 360 |
| PATTERN_COLOR1_LUMINANCE（5） | 1 |  | 0 ~ 100 |
| PATTERN_COLOR1_SATURATION（6） | 1 |  | 0 ~ 100 |
| PATTERN_COLOR2_HUE（7） | 1 |  | 0 ~ 360 |
| PATTERN_COLOR2_LUMINANCE（8） | 1 |  | 0 ~ 100 |
| PATTERN_COLOR2_SATURATION（9） | 1 |  | 0 ~ 100 |

#### 指令0x0080回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.18、Output设置  0x0090

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-15） |
| OUTPUT_SOC_HDMI_OUT_1（0） | 1 | - | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar<br>10：Mutiview |
| OUTPUT_SOC_SDI_OUT_2（1） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar<br>10：Mutiview |
| OUTPUT_SOC_SDI_OUT_3（2） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar<br>10：Mutiview |
| OUTPUT_SOC_STREAM_OUT（3） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar |
| OUTPU_SOC_LCD_OUT（4） | 1 |  | 0: MV<br>1: PGM |
| OUTPUT_SOC_UVC_OUT（5） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar |
| OUTPUT_FRAME_RATE_MODE（6） | 1 |  | 0：Integer<br>1：Decimal |
| OUTPUT_FORMAT_HDMI_OUT_1（7） | 1 |  | 0：1080i50<br>1：1080i60<br>2：1080p24<br>3：1080p25<br>4：1080p30<br>5：1080p50<br>6：1080p60 |
| OUTPUT_FORMAT_SDI_OUT_2（8） | 1 |  | 0：1080i50<br>1：1080i60<br>2：1080p24<br>3：1080p25<br>4：1080p30<br>5：1080p50<br>6：1080p60 |
| OUTPUT_FORMAT_SDI_OUT_3（9） | 1 |  | 0：1080i50<br>1：1080i60<br>2：1080p24<br>3：1080p25<br>4：1080p30<br>5：1080p50<br>6：1080p60 |
| OUTPUT_COLOR_SPACE（10） |  |  | 0：RGB FULL<br>1：RGB LIMIT<br>2：YUV |
| OUTPUT_BRIGHTNESS（11） |  |  | 0~100 |
| OUTPUT_CONTRAST（12） |  |  | 0~100 |
| OUTPUT_SATURATION（13） |  |  | 0~100 |
| FTB_MUTE_SPEED（14） |  |  | 0~30(显示0.0~3.0) |
| FTB_WITH_MUTE（15） |  |  | 0：OFF<br>1：ON |

#### 指令0x0090回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.19、Codec设置  0x00A0

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-15） |
| ENCOD_BITRATE（0） | 1 | - | 0：256Kbps<br>1：512Kbps<br>2：1Mbps<br>3：2Mbps<br>4：4Mbps<br>5：8Mbps<br>6：12Mbps<br>7：16Mbps<br>8：24Mbps<br>9：32Mbps |
| ENCOD_RATE_CONTROL（1） | 1 |  | 0：CBR<br>1：VBR |
| ENCOD_VIDEO_ENCODEING（2） | 1 |  | 0：H.264 High<br>1：H.264 Main<br>2：H.264 Base<br>3：H.265 |
| ENCOD_RES（3） | 1 |  | 0：1920x1080<br>1：1280x720<br>2：720x480 |
| ENCOD_FPS（4） | 1 |  | 0：24<br>1：25<br>2：30<br>3：50<br>4：60 |
| ENCOD_I_FRAME（5） | 2 |  | 5~300 |
| ENCOD_VOL（6） | 1 |  | 0~100 |
| ENCOD_SAMPLING_RATE（7） | 1 |  | 0：48Khz |
| ENCOD_AUDIO_BITRATE（8） | 1 |  | 0：64Kbps<br>1：128Kbps<br>2：256Kbps<br>3：320Kbps |
| STREAM_1_EN（9） | 1 |  | 0：OFF<br>1：ON |
| STREAM_2_EN（10） |  |  | 0：OFF<br>1：ON |
| STREAM_3_EN（11） |  |  | 0：OFF<br>1：ON |
| RECORD_FILL_FORMAT（12） |  |  | 0：TS<br>1：MP4 |
| RECORD_OVERWIRTE（13） |  |  | 0：OFF<br>1：ON |
| RECORD_STORAGE（14） |  |  | 0：SD Card<br>1：USB Storage |
| RECORD_FORMAT（15） |  |  | 0：OFF<br>1：ON |

#### 指令0x00A0回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

### 3.1.20、SYSTEM设置  0x00B0

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Param_Vaild | 4 | - | 指示设置哪个参数（NO.0-44） |
| SYSTEM_LANGUAGE（0） | 1 | - | 0：English<br>1：简体中文<br>2：繁體中文<br>3：Protugues |
| SYSTEM_FAN（1） | 1 |  | 0：AUTO<br>1：Manual<br>2：OFF |
| SYSTEM_TEMA_MODE（2） | 1 |  | 0：摄氏度<br>1：华氏度 |
| SYSTEM_RESET（3） | 1 |  | 0：Reset Preference<br>1：Factory Reset |
| SYSTEM_POWER_MODE（4） | 1 |  | 0：Power On<br>1：Last state |
| SHORTCUT_F1_SHORT_PRESS（5） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F1_LONG_PRESS（6） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F2_SHORT_PRESS（7） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F2_LONG_PRESS（8） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F3_SHORT_PRESS（9） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F3_LONG_PRESS（10） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F4_SHORT_PRESS（11） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F4_LONG_PRESS（12） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F5_SHORT_PRESS（13） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F5_LONG_PRESS（14） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F6_SHORT_PRESS（15） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F6_LONG_PRESS（16） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_RESET（17） | 1 |  | 1：EN |
| SCREEN_BRIGHTNESS（18） | 1 |  | 0~100 |
| SCREEN_CONTRAST（19） | 1 |  | 0~100 |
| SCREEN_SATURATION（20） | 1 |  | 0~100 |
| SCREEN_COLOR_CAST（21） | 1 |  | 0~100 |
| SCREEN_SHARPNESS（22） | 1 |  | 0~100 |
| SCREEN_COLOR_TEMP（26） | 1 |  | 0：6500K<br>1：7500K<br>2：9300K<br>3：USER |
| SCREEN_RED_GAIN（27） | 1 |  | 0~255 |
| SCREEN_GREEN_GAIN（28） | 1 |  | 0~255 |
| SCREEN_BLUE_GAIN（29） | 1 |  | 0~255 |
| SCREEN_RED_OFFSET（30） | 1 |  | 0~255 |
| SCREEN_GREEN_OFFSET（31） | 1 |  | 0~255 |
| SCREEN_BLUE_OFFSET（32） | 1 |  | 0~255 |
| IP_DHCP（33） | 1 |  | 0：OFF<br>1：ON |
| IP_IP（34） | 4 |  | IP addr |
| IP_SUBNET（35） | 4 |  |  |
| IP_GATEWAY（36） | 4 |  |  |
| CLOCK_FORMAT（37） | 1 |  | 0：12H<br>1：24H |
| TIME_SYNC（38） | 1 |  | 0：NTP<br>1：MANUAL |
| TIME_ZONE（39） | 1 |  | 0:"UTC-12:00"<br>1:"UTC-11:00"<br>2:"UTC-10:00"<br>3:"UTC-09:30"<br>4:"UTC-09:00"<br>5:"UTC-08:00"<br>6:"UTC-07:00"<br>7:"UTC-06:00"<br>8:"UTC-05:00"<br>9:"UTC-04:00"<br>10:"UTC-03:30"<br>11:"UTC-03:00"<br>12:"UTC-02:00"<br>13:"UTC-01:00"<br>14:"UTC-00:00"<br>15:"UTC+01:00"<br>16:"UTC+02:00"<br>17:"UTC+03:00"<br>18:"UTC+03:30"<br>19:"UTC+04:00"<br>20:"UTC+04:30"<br>21:"UTC+05:00"<br>22:"UTC+05:30"<br>23:"UTC+05:45"<br>24:"UTC+06:00"<br>25:"UTC+06:30"<br>26:"UTC+07:00"<br>27:"UTC+08:00"<br>28:"UTC+08:45"<br>29:"UTC+09:00"<br>30:"UTC+09:30"<br>31:"UTC+10:00"<br>32:"UTC+10:30"<br>33:"UTC+11:00"<br>34:"UTC+12:00"<br>35:"UTC+12:45"<br>36:"UTC+13:00"<br>37:"UTC+14:00" |
| DATE_TIME（40） | 6 |  |  |
| TIMER_TYPE（41） | 1 |  | 0:TIMER<br>1:Countdown |
| TIMER_HOUR（42） | 1 |  | 0~100 |
| TIMER_MIN（43） | 1 |  | 0~59 |
| TIMER_SEC（44） | 1 |  | 0~59 |

#### 指令0x00B0回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败。 |

## 3.2、同步协议

### 3.2.1、按键获取指令 0x0110

#### 指令0x0110回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Key_val（NO.0） | 2 | -- | 按键对应的值（按键值对应请查看键值对应表） |
| T_Bar_val（NO.1） | 2 | -- | 推杆数据（值的范围0~4095） |
| b_bar_pos（NO.2） | 2 | -- | 推杆的位置<br>0：底部<br>1：中间<br>2：顶部 |

### 3.2.2、Transition 获取  0x0120、

#### 指令0x0120回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Wipe 1(NO.0) | 1 | -- | 划像1 (样式0-10) |
| Wipe 2(NO.1) | 1 | -- | 划像2 (样式0-10) |
| Wipe 3(NO.2) | 1 | -- | 划像3 (样式0-10) |
| Wipe 4(NO.3) | 1 | -- | 划像4 (样式0-10) |
| Softness(NO.4) | 1 | -- | 柔化度 0-100 |
| Direction(NO.5) | 1 | -- | 方向<br>0：Normal<br>1：Invert<br>2：Flip-Flop |
| MIX(NO.6) | 1 | -- | 方向<br>0：OFF<br>1：ON |
| Dir Color R(NO.7)<br>Dir Color G<br>Dir Color B | 3 | -- | 0-255<br>0-255<br>0-255 |
| Speed 1(NO.10) | 1 | -- | 速率1<br>1-80 |
| Speed 2(NO.11) | 1 | -- | 速率2<br>1-80 |
| T-Bar A/BMode(NO.12) | 1 | -- | A/B模式<br>0：OFF<br>1:ON |
| T-Bar Status(NO.13) | 1 | -- | 推杆状态<br>0：OFF<br>1:ON |

### 3.2.3、KEY源获取  0x0130

#### 指令0x0130回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Key1 Type（0） | 1 | -- | 0：PIP<br>1：Luma key |
| Key1 Priority（1） | 1 | -- | 0：优先级1<br>1：优先级2<br>3：优先级3 |
| Key2 Type（2） | 1 | -- | 0：PIP<br>1：Chroma key |
| Key2 Priority（3） | 1 | -- | 0：优先级1<br>1：优先级2<br>3：优先级3 |
| Key3 Type（4） | 1 | -- | 0：PIP |
| Key3 Priority（5） | 1 | -- | 0：优先级1<br>1：优先级2<br>3：优先级3 |

### 3.2.4、LUMA设置  0x0031

#### 指令0x0131回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| LUMA_TIE(0) | 1 | -- | 0：Disbale<br>1：Enable |
| LUMA_STATUS(1) | 1 | -- | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| FILL_SOC(2) | 1 | -- | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7：Color Bar |
| KEY_SOC(3) | 1 | -- | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7：Color Bar |
| LUMA_SIZE(4) | 1 | -- | Zoom size ：12-100 |
| LUMA_POSX(5) | 1 | -- | Position X: 0~100 |
| LUMA_POSY(6) | 1 | -- | Position Y: 0~100 |
| LUMA_CLIP(7) | 1 | -- | 0~100 |
| LUMA_GAIN(8) | 1 | -- | 0~100 |
| LUMA_INV(9) | 1 | -- | 0:OFF<br>1:ON |
| MASK_EN(10) | 1 | -- | 0:OFF<br>1:ON |
| LUMA_MASK_LEFT(11) | 1 | -- | 0-50 |
| LUMA_MASK_TOP(12) | 1 | -- | 0-50 |
| LUMA_MASK_RIGHT(13) | 1 | -- | 50-100 |
| LUMA_MASK_BOTTOM(14) | 1 | -- | 50-100 |

### 3.2.5、CHROMA获取  0x0132

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| CHROMA_STATUS(0) | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| CHROMA_KEY_SOC(1) | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7：Color Bar |
| CHROMA_KEY_TYPE(2) | 1 | - | 0： Green<br>1： Blue<br>2:  Red<br>3:  Custom<br>4:  Fetch |
| CHROMA_KEY_COLOR_R(3)<br>CHROMA_KEY_COLOR_G(4)<br>CHROMA_KEY_COLOR_B(5) | 3 | - | 0~255<br>0~255<br>0~255 |
| CHROMA_KEY_FETCH_POS_X(6) | 2 | - | 0~1920 |
| CHROMA_KEY_FETCH_POS_Y(7) | 2 | - | 0~1080 |
| CHROMA_SIZE(8) | 1 | - | Zoom size ：12-100 |
| CHROMA_POSX(9) | 1 | - | Position X: 0~100 |
| CHROMA_POSY(10) | 1 | - | PositionY: 0~100 |
| CHROMA_SIMILARITY,(11) | 1 | - | 0~100 |
| CHROMA_SMOOTH(12) | 1 | - | 0~255 |
| CHROMA_SPILL(13) | 1 | - | 0~255 |
| CHROMA_OPACITY,(14) | 1 | - | 0~100 |
| CHROMA_BRIGHTNESS(15) | 1 | - | 0~100 |
| CHROMA_CONTRAST,(16) | 1 | - | 0~100 |
| CHROMA_SATURATION,(17) | 1 | - | 0~100 |
| CHROMA_MASK_EN,(18) | 1 | - | 0:OFF<br>1:ON |
| CHROMA_MASK_LEFT,(19) | 1 | - | 0-50 |
| CHROMA_MASK_TOP,(20) | 1 | - | 0-50 |
| CHROMA_MASK_RIGHT,(21) | 1 | - | 50-100 |
| CHROMA_MASK_BOTTOM,(22) | 1 | - | 50-100 |

### 3.2.5、PIP1获取  0x0133

#### 指令0x0133回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| PIP1_STATUS（0） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| PIP1_SOC（1） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar<br>8:  Color 1<br>9:  Color 2<br>10:  PAT 1<br>11:  PAT2 |
| PIP1_SIZE（2） | 1 | - | Zoom size ：12-100 |
| PIP1_POSX（3） | 1 | - | 0~100 |
| PIP1_POSY（4） | 1 | - | 0~100 |

### 3.2.7、PIP2获取  0x0134

#### 指令0x0134回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| PIP2_STATUS（0） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| PIP2_SOC（1） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar<br>8:  Color 1<br>9:  Color 2<br>10:  PAT 1<br>11:  PAT2 |
| PIP2_SIZE（2） | 1 | - | Zoom size ：12-100 |
| PIP2_POSX（3） | 1 | - | 0~100 |
| PIP2_POSY（4） | 1 | - | 0~100 |

### 3.2.8、PIP3获取  0x0135、

#### 指令0x0135回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| PIP3_STATUS（0） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| PIP3_SOC（1） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar<br>8:  Color 1<br>9:  Color 2<br>10:  PAT 1<br>11:  PAT2 |
| PIP3_SIZE（2） | 1 | - | Zoom size ：12-100 |
| PIP3_POSX（3） | 1 | - | 0~100 |
| PIP3_POSY（4） | 1 | - | 0~100 |

### 3.2.8、PIP Border获取  0x0136

#### 指令0x0136回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| PIP_BORDER_STATUS（0） | 1 | - | 0：OFF<br>1：ON |
| PIP_BORDER_COLOR（1） | 1 | - | 0:  White<br>1:  Red<br>2:  Green<br>3:  Blue<br>4:  Black |
| PIP_BORDER_WIDTH（2） | 1 | - | 0~15 |

### 3.2.9、DSK获取  0x0140

#### 指令0x0140回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| DSK_TIE（0） | 1 | - | 0：OFF<br>1：ON |
| DSK_STATUS（1） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| DSK_FILL_SOC（2） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar |
| DSK_KEY_SOC（3） | 1 | - | 0： BLACK<br>1： IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7： Color Bar |
| DSK_CILP（4） | 1 |  | 0~100 |
| DSK_GAIN（5） |  |  | 0~100 |
| DSK_INV（6） |  |  | 0：OFF<br>1：ON |
| DSK_MASK_EN（7） |  |  | 0:OFF<br>1:ON |
| DSK_MASK_LEFT（8） |  |  | 0-50 |
| DSK_MASK_TOP（9） |  |  | 0-50 |
| DSK_MASK_RIGHT（10） |  |  | 50-100 |
| DSK_MASK_BOTTOM（11） |  |  | 50-100 |

### 3.2.10、LOGO设置  0x0141

#### 指令0x0141回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| LOGO_STATUS（0） | 1 | - | 0：OFF<br>1：KEY<br>2：ONAIR<br>3：KEY&ONAIR |
| LOGO_SEL（1） | 1 | - | 0~7选择LOGO样式 |
| LOGO_POSX（2） | 1 |  | 0~100 |
| LOGO_POSY（3） |  |  | 0~100 |
| LOGO_SIZE（4） |  |  | 5 ~20 |
| LOGO_OPACITY（5） |  |  | 20~100 |

### 3.2.11、Audio设置  0x0150

#### 指令0x0150回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| AUDIO_MUTE（0） | 1 | - | 0：OFF<br>1：ON |
| AUDIO_ALL_AFV（1） | 1 | - | 0：OFF<br>1：ON |
| AUDIO_RESET（2） | 1 |  | 1：En |
| AUDIO_MASTER_EN（3） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_MASTER_VOL（4） | 1 |  | 0-72 |
| AUDIO_EAR_EN（5） | 1 |  | 0：OFF<br>1：ON |
| AUDIO_EAR_VOL（6） | 1 |  | 0-72 |
| AUDIO_EAR_SOC（7） |  |  | 0:  PGM<br>1:  IN1<br>2:  IN2<br>3:  IN3<br>4:  IN4<br>5:  IN5<br>6:  IN6<br>7:  MIC 1<br>8:  MIC 2<br>9:  Line In |
| AUDIO_IN1_EN（8） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN1_VOL（9） |  |  | 0-72 |
| AUDIO_IN1_AFV（10） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN1_DELAY（11） |  |  | 0~100（显示0~500） |
| AUDIO_IN2_EN（12） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN2_VOL（13） |  |  | 0-72 |
| AUDIO_IN2_AFV（14） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN2_DELAY（15） |  |  | 0~100（显示0~500） |
| AUDIO_IN3_EN（16） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN3_VOL（17） |  |  | 0-72 |
| AUDIO_IN3_AFV（18） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN3_DELAY（19） |  |  | 0~100（显示0~500） |
| AUDIO_IN4_EN（20） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN4_VOL（21） |  |  | 0-72 |
| AUDIO_IN4_AFV（22） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN4_DELAY（23） |  |  | 0~100（显示0~500） |
| AUDIO_IN5_EN（24） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN5_VOL（25） |  |  | 0-72 |
| AUDIO_IN5_AFV（26） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN5_DELAY（27） |  |  | 0~100（显示0~500） |
| AUDIO_IN6_EN（28） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN6_VOL（29） |  |  | 0-72 |
| AUDIO_IN6_AFV（30） |  |  | 0：OFF<br>1：ON |
| AUDIO_IN6_DELAY（31） |  |  | 0~100（显示0~500） |
| AUDIO_MIC_XLR_MODE（32） |  |  | 0: MIX<br>1: XLR |
| AUDIO_MIC1_EN（33） |  |  | 0：OFF<br>1：ON |
| AUDIO_MIC1_GUITAR（34） |  |  | 0：OFF<br>1：ON |
| AUDIO_MIC1_PER_GAIN（35） |  |  | 0~14 |
| AUDIO_MIC1_VOL（36） |  |  | 0-72 |
| AUDIO_MIC1_DELAY（37） |  |  | 0~100（显示0~500） |
| AUDIO_MIC2_EN（38） |  |  | 0：OFF<br>1：ON |
| AUDIO_MIC2_GUITAR（39） |  |  | 0：OFF<br>1：ON |
| AUDIO_MIC2_PER_GAIN（40） |  |  | 0~14 |
| AUDIO_MIC2_VOL（41） |  |  | 0-72 |
| AUDIO_MIC2_DELAY（42） |  |  | 0~100（显示0~500） |
| AUDIO_XLR_EN（43） |  |  | 0：OFF<br>1：ON |
| AUDIO_XLR_VOL（44） |  |  | 0-72 |
| AUDIO_XLR_DELAY（45） |  |  | 0~100（显示0~500） |
| AUDIO_LINE_IN_EN（46） |  |  | 0：OFF<br>1：ON |
| AUDIO_LINE_IN_VOL（47） |  |  | 0-72 |
| AUDIO_LINE_IN_DELAY（48） |  |  | 0~100（显示0~500） |

### 3.2.12、VIEW获取  0x0160

#### 指令0x0160回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| IN_VIEW_CONTROL（0） | 1 | - | 0：VIEW1<br>1：VIEW2<br>2：VIEW3<br>3：VIEW4<br>4：VIEW5<br>5：VIEW6 |

### 3.2.13、VIEW获取  0x0161

#### 指令0x0161回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| VIEW1_SOC（0） | 1 | - | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW1_FILP（1） |  |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW1_BRIGHTNESS（2） |  |  | 0~100 |
| VIEW1_CONTRAST（3） |  |  | 0~100 |
| VIEW1_SATURATION（4） |  |  | 0~100 |
| VIEW2_SOC（5） |  |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW2_FILP（6） |  |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW2_BRIGHTNESS（7） |  |  | 0~100 |
| VIEW2_CONTRAST（8） |  |  | 0~100 |
| VIEW2_SATURATION（9） |  |  | 0~100 |
| VIEW3_SOC（10） |  |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW3_FILP（11） |  |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW3_BRIGHTNESS（12） |  |  | 0~100 |
| VIEW3_CONTRAST（13） |  |  | 0~100 |
| VIEW3_SATURATION（14） |  |  | 0~100 |
| VIEW4_SOC（15） |  |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW4_FILP（16） |  |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW4_BRIGHTNESS（17） |  |  | 0~100 |
| VIEW4_CONTRAST（18） |  |  | 0~100 |
| VIEW4_SATURATION（19） |  |  | 0~100 |
| VIEW5_SOC（20） |  |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW5_FILP（21） |  |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW5_BRIGHTNESS（22） |  |  | 0~100 |
| VIEW5_CONTRAST（23） |  |  | 0~100 |
| VIEW5_SATURATION（24） |  |  | 0~100 |
| VIEW6_SOC（25） |  |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6 |
| VIEW6_FILP（26） |  |  | 0：OFF<br>1：Horizontal<br>2：Vertical<br>3：Rotate 180 |
| VIEW6_BRIGHTNESS（27） |  |  | 0~100 |
| VIEW6_CONTRAST（28） |  |  | 0~100 |
| VIEW6_SATURATION（29） |  |  | 0~100 |
| VIEW_RESET（30） |  |  | 1：EN |
| FREEZE_CONTROL（31） |  |  | 0：pvw<br>1：pgm |
| INPUT_SOC_IN5（32） |  |  | 0：sdi<br>1：hdmi |
| INPUT_SOC_IN6（33） |  |  | 0：sdi<br>1：hdmi |

### 3.2.14、MV获取  0x0170

#### 指令0x0170回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| LAYOUT_STYLE（0） | 1 | - | 0：Landscape<br>1：Portrain |
| LAYOUTPORT_POSX（1） |  |  | 0~100 |
| LAYOUTPORT_POSY（2） |  |  | 0~100 |
| AUDIO_METER_ALL_EN（3） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN1_EN（4） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN2_EN（5） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN3_EN（6） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN4_EN（7） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN5_EN（8） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_IN6_EN（9） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_PGM_EN（10） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_MIC_EN（11） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_LINE_IN_EN（12） |  |  | 0：OFF<br>1：ON |
| AUDIO_METER_POS（13） |  |  | 0：Left<br>1：Right |
| AUDIO_METER_OPACITY（14） |  |  | 0：100<br>1：75<br>2：50<br>3：25 |
| INPUT_SOC_EN（0） |  |  | 0：OFF<br>1：ON |
| INPUT_SOC_OPACITY（1） |  |  | 0：100<br>1：75<br>2：50<br>3：25 |
| INPUT_SOC_POSX（2） |  |  | 0~100 |
| INPUT_SOC_POSY（3） |  |  | 0~100 |
| INPUT_SOC_TEXT_COLOR_R（4）<br>INPUT_SOC_TEXT_COLOR_G<br>INPUT_SOC_TEXT_COLOR_B | 3 |  | 0~255<br>0~255<br>0~255 |
| INPUT_SOC_BG_COLOR_R（7）<br>INPUT_SOC_BG_COLOR_G<br>INPUT_SOC_BG_COLOR_B | 3 |  | 0~255<br>0~255<br>0~255 |
| UMD_EN（0） |  |  | 0：OFF<br>1：ON |
| UMD_OPACITY（1） |  |  | 0：100<br>1：75<br>2：50<br>3：25 |
| UMD_POSX（2） |  |  | 0~100 |
| UMD_POSY（3） |  |  | 0~100 |
| UMD_TEXT_COLOR_R（4）<br>UMD_TEXT_COLOR_G（5）<br>UMD_TEXT_COLOR_B（6） |  |  | 0~255<br>0~255<br>0~255 |
| UMD_BG_COLOR_R（7）<br>UMD_BG_COLOR_G（8）<br>UMD_BG_COLOR_B（9） |  |  | 0~255<br>0~255<br>0~255 |

### 3.2.15、UMD 字符设置  0x0171

#### 指令0x0171回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| UMD_STRING_IN1（0） | 20 | - | 最长8个字符 |
| UMD_STRING_IN2（1） | 20 |  |  |
| UMD_STRING_IN3（2） | 20 |  |  |
| UMD_STRING_IN4（3） | 20 |  |  |
| UMD_STRING_IN5（4） | 20 |  |  |
| UMD_STRING_IN6（5） | 20 |  |  |
| UMD_STRING_IN7（6） | 20 |  |  |
| UMD_STRING_IN8（7） | 20 |  |  |
| UMD_STRING_PVW（8） | 20 |  |  |
| UMD_STRING_PGM（9） | 20 |  |  |

### 3.2.16、Library获取  0x0180

#### 指令0x0180回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| LIBRARY_PATTERN_1（0） | 1 | - | 0：Black<br>1：Color Bar<br>2：Color 1<br>3：Color 2<br>4：Image 1<br>5：Image 2 |
| LIBRARY_PATTERN_2（1） | 1 |  | 0：Black<br>1：Color Bar<br>2：Color 1<br>3：Color 2<br>4：Image 1<br>5：Image 2 |
| LIBRARY_IMAGE_PATH（2） | 1 |  | 0：SD Card<br>1：USB Storage |
| PATTERN_COLOR1_HUE（4） | 2 |  | 0 ~ 360 |
| PATTERN_COLOR1_LUMINANCE（5） | 1 |  | 0 ~ 100 |
| PATTERN_COLOR1_SATURATION（6） | 1 |  | 0 ~ 100 |
| PATTERN_COLOR2_HUE（7） | 1 |  | 0 ~ 360 |
| PATTERN_COLOR2_LUMINANCE（8） | 1 |  | 0 ~ 100 |
| PATTERN_COLOR2_SATURATION（9） | 1 |  | 0 ~ 100 |

### 3.2.17、Output获取  0x0190

#### 指令0x0190回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| OUTPUT_SOC_HDMI_OUT_1（0） | 1 | - | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar<br>10：Mutiview |
| OUTPUT_SOC_SDI_OUT_2（1） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar<br>10：Mutiview |
| OUTPUT_SOC_SDI_OUT_3（2） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar<br>10：Mutiview |
| OUTPUT_SOC_STREAM_OUT（3） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar |
| OUTPU_SOC_LCD_OUT（4） | 1 |  | 0: MV<br>1: PGM |
| OUTPUT_SOC_UVC_OUT（5） | 1 |  | 0：IN1<br>1：IN2<br>2：IN3<br>3：IN4<br>4：IN5<br>5：IN6<br>6：PGM<br>7：Clear PGM<br>8：PVW<br>9：Color Bar |
| OUTPUT_FRAME_RATE_MODE（6） | 1 |  | 0：Integer<br>1：Decimal |
| OUTPUT_FORMAT_HDMI_OUT_1（7） | 1 |  | 0：1080i50<br>1：1080i60<br>2：1080p24<br>3：1080p25<br>4：1080p30<br>5：1080p50<br>6：1080p60 |
| OUTPUT_FORMAT_SDI_OUT_2（8） | 1 |  | 0：1080i50<br>1：1080i60<br>2：1080p24<br>3：1080p25<br>4：1080p30<br>5：1080p50<br>6：1080p60 |
| OUTPUT_FORMAT_SDI_OUT_3（9） | 1 |  | 0：1080i50<br>1：1080i60<br>2：1080p24<br>3：1080p25<br>4：1080p30<br>5：1080p50<br>6：1080p60 |
| OUTPUT_COLOR_SPACE（10） |  |  | 0：RGB FULL<br>1：RGB LIMIT<br>2：YUV |
| OUTPUT_BRIGHTNESS（11） |  |  | 0~100 |
| OUTPUT_CONTRAST（12） |  |  | 0~100 |
| OUTPUT_SATURATION（13） |  |  | 0~100 |
| FTB_MUTE_SPEED（14） |  |  | 0~30(显示0.0~3.0) |
| FTB_WITH_MUTE（15） |  |  | 0：OFF<br>1：ON |

### 3.2.18、Codec获取  0x01A0

#### 指令0x01A0回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| ENCOD_BITRATE（0） | 1 | - | 0：256Kbps<br>1：512Kbps<br>2：1Mbps<br>3：2Mbps<br>4：4Mbps<br>5：8Mbps<br>6：12Mbps<br>7：16Mbps<br>8：24Mbps<br>9：32Mbps |
| ENCOD_RATE_CONTROL（1） | 1 |  | 0：CBR<br>1：VBR |
| ENCOD_VIDEO_ENCODEING（2） | 1 |  | 0：H.264 High<br>1：H.264 Main<br>2：H.264 Base<br>3：H.265 |
| ENCOD_RES（3） | 1 |  | 0：1920x1080<br>1：1280x720<br>2：720x480 |
| ENCOD_FPS（4） | 1 |  | 0：24<br>1：25<br>2：30<br>3：50<br>4：60 |
| ENCOD_I_FRAME（5） | 2 |  | 5~300 |
| ENCOD_VOL（6） | 1 |  | 0~100 |
| ENCOD_SAMPLING_RATE（7） | 1 |  | 0：48Khz |
| ENCOD_AUDIO_BITRATE（8） | 1 |  | 0：64Kbps<br>1：128Kbps<br>2：256Kbps<br>3：320Kbps |
| STREAM_1_EN（9） | 1 |  | 0：OFF<br>1：ON |
| STREAM_2_EN（10） |  |  | 0：OFF<br>1：ON |
| STREAM_3_EN（11） |  |  | 0：OFF<br>1：ON |
| RECORD_FILL_FORMAT（12） |  |  | 0：TS<br>1：MP4 |
| RECORD_OVERWIRTE（13） |  |  | 0：OFF<br>1：ON |
| RECORD_STORAGE（14） |  |  | 0：SD Card<br>1：USB Storage |
| RECORD_FORMAT（15） |  |  | 0：OFF<br>1：ON |

### 3.2.19、SYSTEM获取  0x01B0

#### 指令0x01B0回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| SYSTEM_LANGUAGE（0） | 1 | - | 0：English<br>1：简体中文<br>2：繁體中文<br>3：Protugues |
| SYSTEM_FAN（1） | 1 |  | 0：AUTO<br>1：Manual<br>2：OFF |
| SYSTEM_TEMA_MODE（2） | 1 |  | 0：摄氏度<br>1：华氏度 |
| SYSTEM_RESET（3） | 1 |  | 0：Reset Preference<br>1：Factory Reset |
| SYSTEM_POWER_MODE（4） | 1 |  | 0：Power On<br>1：Last state |
| SHORTCUT_F1_SHORT_PRESS（5） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F1_LONG_PRESS（6） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F2_SHORT_PRESS（7） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F2_LONG_PRESS（8） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F3_SHORT_PRESS（9） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F3_LONG_PRESS（10） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F4_SHORT_PRESS（11） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F4_LONG_PRESS（12） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F5_SHORT_PRESS（13） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F5_LONG_PRESS（14） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F6_SHORT_PRESS（15） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SHORTCUT_F6_LONG_PRESS（16） | 1 |  | 0：NONE<br>1：REC M<br>2：Call M<br>3：Key1 Mask<br>4：Key2 Mask<br>5：DSK Mask<br>6：Timer<br>7：Clr Display |
| SCREEN_BRIGHTNESS（18） | 1 |  | 0~100 |
| SCREEN_CONTRAST（19） | 1 |  | 0~100 |
| SCREEN_SATURATION（20） | 1 |  | 0~100 |
| SCREEN_COLOR_CAST（21） | 1 |  | 0~100 |
| SCREEN_SHARPNESS（22） | 1 |  | 0~100 |
| SCREEN_COLOR_TEMP（26） | 1 |  | 0：6500K<br>1：7500K<br>2：9300K<br>3：USER |
| SCREEN_RED_GAIN（27） | 1 |  | 0~255 |
| SCREEN_GREEN_GAIN（28） | 1 |  | 0~255 |
| SCREEN_BLUE_GAIN（29） | 1 |  | 0~255 |
| SCREEN_RED_OFFSET（30） | 1 |  | 0~255 |
| SCREEN_GREEN_OFFSET（31） | 1 |  | 0~255 |
| SCREEN_BLUE_OFFSET（32） | 1 |  | 0~255 |
| IP_DHCP（33） | 1 |  | 0：OFF<br>1：ON |
| IP_IP（34） | 4 |  | IP addr |
| IP_SUBNET（35） | 4 |  |  |
| IP_GATEWAY（36） | 4 |  |  |
| CLOCK_FORMAT（37） | 1 |  | 0：12H<br>1：24H |
| TIME_SYNC（38） | 1 |  | 0：NTP<br>1：MANUAL |
| TIME_ZONE（39） | 1 |  | 0:"UTC-12:00"<br>1:"UTC-11:00"<br>2:"UTC-10:00"<br>3:"UTC-09:30"<br>4:"UTC-09:00"<br>5:"UTC-08:00"<br>6:"UTC-07:00"<br>7:"UTC-06:00"<br>8:"UTC-05:00"<br>9:"UTC-04:00"<br>10:"UTC-03:30"<br>11:"UTC-03:00"<br>12:"UTC-02:00"<br>13:"UTC-01:00"<br>14:"UTC-00:00"<br>15:"UTC+01:00"<br>16:"UTC+02:00"<br>17:"UTC+03:00"<br>18:"UTC+03:30"<br>19:"UTC+04:00"<br>20:"UTC+04:30"<br>21:"UTC+05:00"<br>22:"UTC+05:30"<br>23:"UTC+05:45"<br>24:"UTC+06:00"<br>25:"UTC+06:30"<br>26:"UTC+07:00"<br>27:"UTC+08:00"<br>28:"UTC+08:45"<br>29:"UTC+09:00"<br>30:"UTC+09:30"<br>31:"UTC+10:00"<br>32:"UTC+10:30"<br>33:"UTC+11:00"<br>34:"UTC+12:00"<br>35:"UTC+12:45"<br>36:"UTC+13:00"<br>37:"UTC+14:00" |
| DATE_TIME（40） | 6 |  |  |
| TIMER_TYPE（41） | 1 |  | 0:TIMER<br>1:Countdown |
| TIMER_HOUR（42） | 1 |  | 0~100 |
| TIMER_MIN（43） | 1 |  | 0~59 |
| TIMER_SEC（44） | 1 |  | 0~59 |

## 3.3、其他通用协议

### 3.3.1、设备重命名  0xBB00

上位机发送数据

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Dev_Name | 24 | -- | 设备名称，最大24个字节，不够补0，不支持中文字符。 |

设备发送数据

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Report Code | 1 | -- | 0：成功，<br>1：失败 |

### 3.3.2、查询设备名  0xBB01

上位机发送数据

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Dev_Type | 1 |  | 见设备类型 |
| Macaddr | 6 |  | 6位的设备mac地址 |

设备回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Dev_Name | 24 | -- | 设备名称，上位机可以自定义设备名称，若未设置，则使用默认名称。<br>默认名称由（model+MAC前两个字节）组成，eg：VS0605E_6E5A |

### 3.3.3、心跳包  0xEEEE

上位机通过设备的心跳包，来判断设备是否离线。采用上位机查询的方式，上位机5s发送一次心跳查询，若连续三次没有收到设备的回复，则表示设备离线。

上位机发送数据

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| Dev_Type | 1 |  | 见设备类型 |
| Macaddr | 6 |  | 6位的设备mac地址 |

设备回复

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| vendor | 6 | -- | 厂商英文简称：”AVM” (长度最长为6的字符串) |
| Product_name | 16 | -- | 产品信息”6CH-SWITCHER”(长度最长为16的字符串) |
| MAC | 6 | -- | 设备的mac地址 |

## 4、设备发现流程

由于设备接上路由器后，IP地址段是未知的，因此要采用广播的方式来查找设备(不采用子网段广播的方式，是因为上位机有可能有多个网口，采用子网段广播，需要指定同网段的网口才行)。

SYCONFIG UDP广播通信接口：

协议：UDP

端口：7000

目的IP地址：255.255.255.255

SYCONFIG发现设备交互过程：

![SYCONFIG发现设备交互过程](AVM_PSV0617_UDP通信协议V1.0.0_test.assets/discovery_flow.png)

*图：SYCONFIG 设备发现交互过程*

### 4.1、上位机发送（0xFFFF）

上位机发送数据

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| target | 1 | -- | 按照请求的目标设备，可以分为几类，由target字段来区分：<br>0xFF代表所有设备；<br>0x01代表使用设备类型的方式指定的被绑定的设备（Dev_Type字段)；<br>0x02代表使用MAC地址的方式指定的被绑定设备<br>（Macaddr字段）；<br>0x03代表使用二维码方式的方式指定的被绑定设备<br>（Sn字段）。<br>注：无target字段，或者不满足target字段定义的范围的报文，或者按照target的类型要求不一致，设备不能做出应答。 |
| Dev_Type | 1 | （可选，由target字段决定） | 见设备类型 |
| Macaddr | 6 | （可选，由target字段决定） | 6位的设备mac地址 |
| Sn | 8 | （可选，由target字段决定） | Sn：在使用二维码扫码绑定设备时，一般提供的是sn。APP扫描二维码时，如果没有sn字段，sn默认为“00000000”。<br>设备端检测到APP发来的sn为“00000000”，不校验sn；否则需要用设备端的sn校验。如果设备端没有sn为“00000000”，用mac地址与APP发来的sn做校验。 |

请求局域网内所有设备进行应答

A5 5A 10 00 00 1E 00 01 00 00 00 00 00 00 00 00 00 FF FF 00 00 00 01 00 01 FF SUM1 SUM2 A6 6A

请求局域网内所有的vs0605e的设备进行应答

A5 5A 10 00 00 24 00 01 00 00 00 00 00 00 00 00 00 FF FF 00 00 00 01 00 02 01 01 SUM1 SUM2 A6 6A

请求局域网内MACADDR[010203040506]的设备进行应答

A5 5A 10 00 00 24 00 01 00 00 00 00 00 00 00 00 00 FF FF 00 00 00 01 00 07 02 01 02 03 04 05 06 SUM1 SUM2 A6 6A

### 4.2、设备回复

设备厂商信息、品牌信息

产品品类、型号Model

设备ID、序列号SN、MAC地址等信息

| 字段 | 字节数 | 值 | 说明 |
|---|---|---|---|
| vendor | 6 | -- | 厂商英文简称：”AVM” (长度最长为6的字符串) |
| Product_name | 16 | -- | 产品信息”6CH-SWITCHER”(长度最长为16的字符串) |
| Product_type | 1 | -- | 见设备类型 |
| model | 10 | -- | 产品型号”VS0605E”(长度最长为10的字符串) |
| deviceId | 4 | -- | 设备id |
| SN | 8 | -- | 序列号 |
| MAC | 6 | -- | 设备的mac地址 |
| Protocol_Version | 2 | -- | 协议版本号 |
| Dev_Name | 24 | -- | 设备名称，上位机可以自定义设备名称，若未设置，则使用默认名称。<br>默认名称由（model+MAC前两个字节）组成，eg：VS0605E_6E5A |

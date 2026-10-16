

class ModelRticePreferences(object):
    _targetCSCPosList = ["RGB2YUV", "YUV2RGB"]
    _colorRangeList = ["LIMIT", "FULL", "EXPAND", "SHRINK"]
    _colorRangeModeList = ["AUTO", "LIMIT", "FULL", "EXPAND", "SHRINK"]
    _edidModeList = ["Default", "Follow TX", "Follow USB", "Undefined", "Mixed"]

    # AT_IPT_FIFO1_ADC/AT_IPT_FIFO2_I2S_IN/AT_IPT_SPDIF/AT_IPT_UAC
    _mixerSourceList = ["ADC", "I2S IN", "SPDIF", "UAC"]

    # 0: 8bit, 1:10bit, 2:12bit, 3:16bit, 4: 6bit
    _colorDepthList = [8, 10, 12, 16, 6]

    # 0: RGB, 1: YUV422, 2: YUV444, 3: YUV420, 4: YUV400(Y ONLY)
    _colorSpaceList = ["RGB", "YUV422", "YUV444", "YUV420", "YUV400"]

    #
    _hdmiTimingInfoColorRangeModeList = ["Default", "Limit", "Full", "Unknow"]
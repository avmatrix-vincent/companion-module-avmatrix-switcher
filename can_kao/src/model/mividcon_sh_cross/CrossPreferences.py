

class CrossPreferences(object):
    _pid = 5   # 5:SC2040 ,6:MIVIDCON_Cross

    _sdi_sfp_in = ["SDI In","SFP In"]
    _output_sources = ["SDI In", "HDMI In", "Scaler"]
    _scaler_sources = ["SDI In", "HDMI In"]
    _patterns = ["100% Colorbar", "16-Step Grayscale", "32-Step Grayscale"]
    _sdi_out_modes = ["Loop Out", "Output"]

    _output_formats = [
        "480i",
	    "576i",
	    "720p24",
        "720p25",
        "720p30",
        "720p50",
        "720p60",
        "ED480p59.94",
        "ED576p50",
        "1080i50",
        "1080i60",
        "1080p24",
        "1080p25",
        "1080p30",
        "1080p50",
        "1080p60",
        "720p23.98",
        "720p29.97",
        "720p59.94",
        "1080psf23.98",
        "1080psf24",
        "1080psf25",
        "1080psf29.97",
        "1080psf30",
        "1080i59.94",
        "1080p23.98",
        "1080p29.97",
        "1080p59.94"
    ]

    _color_spaces = ["DVI RGB444", "HDMI RGB444 2CH", "HDMI YCbCr444 2CH", "HDMI YCbCr422 2CH", "HDMI RGB444 8CH", "HDMI YCbCr444 8CH", "HDMI YCbCr422 8CH"]
    _sdi_out_level_modes = ["3G Level-A", "3G Level-B"]
    _sd2sd_aspects = ["Anamorphic",
                      "I=16:9 FS O=14:9/16:9 LB",
                      "I=16:9 FS O=4:3/16:9 LB",
                      "I=16:9 FS O=14:9/16:9 CC",
                      "I=16:9 FS O=4:3/16:9 CC",
                      "I=16:9/14:9 PB O=4:3/14:9 LB",
                      "I=16:9/14:9 PB O=4:3/14:9 CC",
                      "I=16:9/14:9 PB O=16:9/14:9 ZM",
                      "I=16:9/4:3 PB O=14:9/4:3 PB",
                      "I=16:9/4:3 PB O=16:9/4:3 ZM",
                      "I=16:9/4:3 PB O=14:9/4:3 ZM",
                      "I=14:9 FS O=16:9/14:9 PB",
                      "I=14:9 FS O=4:3/14:9 LB",
                      "I=14:9 FS O=4:3/14:9 CC",
                      "I=14:9 FS O=16:9/14:9 ZM",
                      "I=14:9/4:3 PB O=16:9/4:3 PB",
                      "I=14:9/4:3 PB O=16:9/4:3 ZM",
                      "I=14:9/4:3 PB O=14:9/4:3 ZM",
                      "I=14:9/16:9 LB O=4:3/16:9 LB",
                      "I=14:9/16:9 LB O=14:9/16:9 CC",
                      "I=14:9/16:9 LB O=4:3/16:9 CC",
                      "I=4:3 FS O=16:9/4:3 PB",
                      "I=4:3 FS O=14:9/4:3 PB",
                      "I=4:3 FS O=16:9/4:3 ZM",
                      "I=4:3 FS O=14:9/4:3 ZM",
                      "I=4:3/16:9 LB O=14:9/16:9 LB",
                      "I=4:3/16:9 LB O=14:9/16:9 CC",
                      "I=4:3/16:9 LB O=4:3/16:9 CC",
                      "I=4:3/14:9 LB O=16:9/14:9 PB",
                      "I=4:3/14:9 LB O=4:3/14:9 CC",
                      "I=4:3/14:9 LB O=16:9/14:9 ZM"
                      ]     #["Original", "4:3"]

    _sd2hd_aspects = ["Anamorphic",
                      "I=16:9/14:9 PB O=16:9/14:9 ZM",
                     "I=16:9/4:3 PB O=16:9/4:3 ZM",
                      "I=14:9 FS O=16:9/14:9 PB",
                     "I=14:9 FS O=16:9/14:9 ZM",
                      "I=14:9/4:3 PB O=16:9/4:3 PB",
                     "I=14:9/4:3 PB O=16:9/4:3 ZM",
                      "I=4:3 FS O=16:9/4:3 PB",
                      "I=4:3 FS O=16:9/4:3 ZM",
                      "I=4:3/14:9 LB O=16:9/14:9 PB",
                      "I=4:3/14:9 LB O=16:9/14:9 ZM"
                      ]
    _hd2sd_aspects = [ "Anamorphic",
                       "I=16:9 FS O=14:9/16:9 LB",
                       "I=16:9 FS O=4:3/16:9 LB",
                       "I=16:9 FS O=14:9/16:9 CC",
                       "I=16:9 FS O=4:3/16:9 CC",
                       "I=16:9/14:9 PB O=4:3/14:9 LB",
                       "I=16:9/14:9 PB O=4:3/14:9 CC",
                       "I=16:9/14:9 PB O=16:9/14:9 ZM",
                       "I=16:9/4:3 PB O=14:9/4:3 PB",
                       "I=16:9/4:3 PB O=16:9/4:3 ZM",
                       "I=16:9/4:3 PB O=14:9/4:3 ZM"
                    ]
    _hd2hd_aspects = ["Anamorphic","I=16:9/14:9 PB O=16:9/14:9 ZM","I=16:9/4:3 PB O=16:9/4:3 ZM"]
    _deinterlaces = ["Top and Bottom","Weave"]
    _pattens = ["Off","100% Color Bar","75% Color Bar",
                "White","Yellow","Cyan",
                "Green","Magenta","Red",
                "Blue","Black","Gray",
                "8H Gray Level","16H Gray Level","32H Gray Level",
                "64H Gray Level","White Ramp","Black Ramp",
                "Win50 White","Win50 Black","Check Filed",
                "Red Ramp","Green Ramp","Blue Ramp"]
    _tpg_ops = ["Disable","Dynamic Circle","Frame Count"]


    _image_flip_modes = ["Off", "H Flip", "V Flip", "H&V Flip"]

    _hdmi_out_audio_channels = ["HDMI CH1-2", "HDMI CH3-4", "HDMI CH5-6", "HDMI CH7-8","Audio In","Off"]
    _hdmi_out_audio_channels_sdi = ["HDMI CH1-2", "HDMI CH3-4", "HDMI CH5-6", "HDMI CH7-8","HDMI CH9-10","HDMI CH11-12","HDMI CH13-14","HDMI CH15-16","Audio In","Off"]

    _sdi_out_audio_channels = ["SDI CH1-2", "SDI CH3-4", "SDI CH5-6", "SDI CH7-8","Audio In", "Off"]
    _sdi_out_audio_channels_sdi = ["SDI CH1-2", "SDI CH3-4", "SDI CH5-6", "SDI CH7-8", "SDI CH9-10","SDI CH11-12", "SDI CH13-14", "SDI CH15-16", "Audio In", "Off"]

    _scaler_refs = ["Free-run", "SDI In", "HDMI In", "Source"]

    _Analog_Audio_Out=[
        "SDI CH1-2","SDI CH3-4","SDI CH5-6",
        "SDI CH7-8", "SDI CH9-10", "SDI CH11-12",
        "SDI CH13-14", "SDI CH15-16", "HDMI CH1-2",
        "HDMI CH3-4", "HDMI CH5-6", "HDMI CH7-8",
        "off"
    ]
    _tpg_audio_test=["Off","L 1kHz R 1kHz","L 1kHz R Mute","L Mute R 1kHz"]


    """
    未来可能需要支持:
        "Black and no signal", 
        "Blue and no signal", 
        "Green and no signal", 
        "Cyan and no signal", 
        "Red and no siganl", 
        "Magenta and no signal", 
        "Yellow and no signal", 
        "White and no signal"
    """
    _no_signal_indicators = [
        "Black", "Blue", "Green", "Cyan", "Red", "Magenta", "Yellow", "White"
    ]
    _lcd_off_times = ["5 seconds", "15 seconds", "30 seconds", "1 minute", "5 minutes", "10 minutes", "30 minutes", "Never"]
    _back_to_status_times = ["5 seconds", "15 seconds", "30 seconds", "1 minute", "5 minutes", "10 minutes", "30 minutes", "Never"]
    _languages = ["English/英文","Chinese/中文"] # "Chinese/中文"
    _languages_list=[
        ["English"],
        ["中文"],
        ["English/英文","Chinese/中文"]
    ]


    _input_formats = [
        "480i",
        "576i",
        "720p24",
        "720p25",
        "720p30",
        "720p50",
        "720p60",
        "1080i48",
        "1080i50",
        "1080i60",
        "1080p24",
        "1080p25",
        "1080p30",
        "1080p48",
        "1080p50",
        "1080p60",
        "720p23.98",
        "720p29.97",
        "720p59.94",
        "1080psf23.98",
        "1080psf24",
        "1080psf25",
        "1080psf29.97",
        "1080psf30",	
        "1080i59.94",
        "1080p23.98",
        "1080p29.97",
        "1080p59.94",
        "1080p50DL",
        "1080p59.94DL",
        "1080p60DL",	
        "No Signal"
    ]

    """
    _pid
    """
    @staticmethod
    def get_pid():
        return CrossPreferences._pid

    """
    _tpg_audio_test
    """
    @staticmethod
    def get_tpg_audio_test():
        return CrossPreferences._tpg_audio_test

    @staticmethod
    def get_tpg_audio_test_by_index(index):
        if index >= len(CrossPreferences._tpg_audio_test):
            return "ErrorSDISFP"
        return CrossPreferences._tpg_audio_test[index]

    @staticmethod
    def get_index_by_tpg_audio_test(source):
        for i in range(len(CrossPreferences._tpg_audio_test)):
            if source == CrossPreferences._tpg_audio_test[i]:
                return i
        return 0xFF


    """
    _Analog_Audio_Out
    """
    @staticmethod
    def get_analog_audio_out():
        return CrossPreferences._Analog_Audio_Out

    @staticmethod
    def get_analog_audio_out_by_index(index):
        if index >= len(CrossPreferences._Analog_Audio_Out):
            return "ErrorSDISFP"
        return CrossPreferences._Analog_Audio_Out[index]

    @staticmethod
    def get_index_by_analog_audio_out(source):
        for i in range(len(CrossPreferences._Analog_Audio_Out)):
            if source == CrossPreferences._Analog_Audio_Out[i]:
                return i
        return 0xFF

    """
    _sdi_sfp_in
    """
    @staticmethod
    def get_sdi_sfps():
        return CrossPreferences._sdi_sfp_in

    @staticmethod
    def get_sdi_sfp_by_index(index):
        if index >= len(CrossPreferences._sdi_sfp_in):
            return "ErrorSDISFP"

        return CrossPreferences._sdi_sfp_in[index]

    @staticmethod
    def get_index_by_sdi_sfp(source):
        for i in range(len(CrossPreferences._sdi_sfp_in)):
            if source == CrossPreferences._sdi_sfp_in[i]:
                return i

        return 0xFF

    """
    _output_sources
    """
    @staticmethod
    def get_output_sources():
        return CrossPreferences._output_sources

    @staticmethod
    def get_output_source_by_index(index):
        if index >= len(CrossPreferences._output_sources):
            return "ErrorOutputSource"

        return CrossPreferences._output_sources[index]

    @staticmethod
    def get_index_by_output_source(source):
        for i in range(len(CrossPreferences._output_sources)):
            if source == "SDI In" or source == "SFP In":
                return 0
            elif source == CrossPreferences._output_sources[i]:
                return i

        return 0xFF

    """
    _scaler_sources
    """
    @staticmethod
    def get_scaler_sources():
        return CrossPreferences._scaler_sources

    @staticmethod
    def get_scaler_source_by_index(index):
        if index >= len(CrossPreferences._scaler_sources):
            return "ErrorScalerSource"

        return CrossPreferences._scaler_sources[index]

    @staticmethod
    def get_index_by_scaler_source(source):
        for i in range(len(CrossPreferences._scaler_sources)):
            if source == "SDI In" or source == "SFP In":
                return 0
            if source == CrossPreferences._scaler_sources[i]:
                return i
        
        return 0xFF

    """
    _patterns
    """
    @staticmethod
    def get_patterns():
        return CrossPreferences._patterns

    @staticmethod
    def get_pattern_by_index(index):
        if index >= len(CrossPreferences._patterns):
            return "ErrorPattern"

        return CrossPreferences._patterns[index]

    @staticmethod
    def get_index_by_pattern(pattern):
        for i in range(len(CrossPreferences._patterns)):
            if pattern == CrossPreferences._patterns[i]:
                return i
        
        return 0xFF
    
    """
    _sdi_out_modes
    """
    @staticmethod
    def get_sdi_out_modes():
        return CrossPreferences._sdi_out_modes

    @staticmethod
    def get_sdi_out_mode_by_index(index):
        if index >= len(CrossPreferences._sdi_out_modes):
            return "ErrorSdiOutMode"

        return CrossPreferences._sdi_out_modes[index]

    @staticmethod
    def get_index_by_sdi_out_mode(mode):
        for i in range(len(CrossPreferences._sdi_out_modes)):
            if mode == CrossPreferences._sdi_out_modes[i]:
                return i
        
        return 0xFF

    """
    _output_formats
    """
    @staticmethod
    def get_output_formats():
        return CrossPreferences._output_formats

    @staticmethod
    def get_output_format_by_index(index):
        if index >= len(CrossPreferences._output_formats):
            return "ErrorOutputFormat"

        return CrossPreferences._output_formats[index]

    @staticmethod
    def get_index_by_output_format(output_format):
        for i in range(len(CrossPreferences._output_formats)):
            if output_format == CrossPreferences._output_formats[i]:
                return i
        
        return 0xFF

    """
    _color_spaces
    """
    @staticmethod
    def get_color_spaces():
        return CrossPreferences._color_spaces

    @staticmethod
    def get_color_space_by_index(index):
        if index >= len(CrossPreferences._color_spaces):
            return "ErrorColorSpace"

        return CrossPreferences._color_spaces[index]

    @staticmethod
    def get_index_by_color_space(color_space):
        for i in range(len(CrossPreferences._color_spaces)):
            if color_space == CrossPreferences._color_spaces[i]:
                return i
        
        return 0xFF

    """
    _sdi_out_level_modes
    """
    @staticmethod
    def get_sdi_out_level_modes():
        return CrossPreferences._sdi_out_level_modes

    @staticmethod
    def get_sdi_out_level_mode_by_index(index):
        if index >= len(CrossPreferences._sdi_out_level_modes):
            return "ErrorSdiOutLevelMode"

        return CrossPreferences._sdi_out_level_modes[index]

    @staticmethod
    def get_index_by_sdi_out_level_mode(level_mode):
        for i in range(len(CrossPreferences._sdi_out_level_modes)):
            if level_mode == CrossPreferences._sdi_out_level_modes[i]:
                return i
        
        return 0xFF

    """
    _sd2sd_aspects
    """
    @staticmethod
    def get_sd2sd_aspects():
        return CrossPreferences._sd2sd_aspects

    @staticmethod
    def get_sd2sd_aspect_by_index(index):
        if index >= len(CrossPreferences._sd2sd_aspects):
            return "ErrorSD2SDAspect"

        return CrossPreferences._sd2sd_aspects[index]

    @staticmethod
    def get_index_by_sd2sd_aspect(level_mode):
        for i in range(len(CrossPreferences._sd2sd_aspects)):
            if level_mode == CrossPreferences._sd2sd_aspects[i]:
                return i
        
        return 0xFF

    """
    _sd2hd_aspects
    """
    @staticmethod
    def get_sd2hd_aspects():
        return CrossPreferences._sd2hd_aspects

    @staticmethod
    def get_sd2hd_aspect_by_index(index):
        if index >= len(CrossPreferences._sd2hd_aspects):
            return "ErrorSD2HDAspect"

        return CrossPreferences._sd2hd_aspects[index]

    @staticmethod
    def get_index_by_sd2hd_aspect(level_mode):
        for i in range(len(CrossPreferences._sd2hd_aspects)):
            if level_mode == CrossPreferences._sd2hd_aspects[i]:
                return i
        
        return 0xFF

    """
    _hd2sd_aspects
    """
    @staticmethod
    def get_hd2sd_aspects():
        return CrossPreferences._hd2sd_aspects

    @staticmethod
    def get_hd2sd_aspect_by_index(index):
        if index >= len(CrossPreferences._hd2sd_aspects):
            return "ErrorHD2SDAspect"

        return CrossPreferences._hd2sd_aspects[index]

    @staticmethod
    def get_index_by_hd2sd_aspect(level_mode):
        for i in range(len(CrossPreferences._hd2sd_aspects)):
            if level_mode == CrossPreferences._hd2sd_aspects[i]:
                return i
        
        return 0xFF

    """
    _hd2hd_aspects
    """
    @staticmethod
    def get_hd2hd_aspects():
        return CrossPreferences._hd2hd_aspects

    @staticmethod
    def get_hd2hd_aspect_by_index(index):
        if index >= len(CrossPreferences._hd2hd_aspects):
            return "ErrorHD2HDAspect"

        return CrossPreferences._hd2hd_aspects[index]

    @staticmethod
    def get_index_by_hd2hd_aspect(level_mode):
        for i in range(len(CrossPreferences._hd2hd_aspects)):
            if level_mode == CrossPreferences._hd2hd_aspects[i]:
                return i
        
        return 0xFF


    """
    _deinterlaces
    """
    @staticmethod
    def get_deinterlaces():
        return CrossPreferences._deinterlaces

    @staticmethod
    def get_deinterlaces_by_index(index):
        if index >= len(CrossPreferences._deinterlaces):
            return "ErrorDeinterlaces"

        return CrossPreferences._deinterlaces[index]

    @staticmethod
    def get_index_by_deinterlaces(level_mode):
        for i in range(len(CrossPreferences._deinterlaces)):
            if level_mode == CrossPreferences._deinterlaces[i]:
                return i
        
        return 0xFF


    """
    _pattens
    """
    @staticmethod
    def get_pattens():
        return CrossPreferences._pattens
    @staticmethod
    def get_pattens_by_index(index):
        if index >= len(CrossPreferences._pattens):
            return "ErrorPattern"

        return CrossPreferences._pattens[index]
    @staticmethod
    def get_index_by_pattens(level_mode):
        for i in range(len(CrossPreferences._pattens)):
            if level_mode == CrossPreferences._pattens[i]:
                return i
        
        return 0xFF


    """
    _tpg_ops
    """
    @staticmethod
    def get_tpg_ops():
        return CrossPreferences._tpg_ops
    @staticmethod
    def get_tpgop_by_index(index):
        if index >= len(CrossPreferences._tpg_ops):
            return "ErrorTPGOPS"

        return CrossPreferences._tpg_ops[index]
    @staticmethod
    def get_index_by_tpg_op(level_mode):
        for i in range(len(CrossPreferences._tpg_ops)):
            if level_mode == CrossPreferences._tpg_ops[i]:
                return i
        
        return 0xFF




    """
    _image_flip_modes
    """
    @staticmethod
    def get_image_flip_modes():
        return CrossPreferences._image_flip_modes

    @staticmethod
    def get_image_flip_mode_by_index(index):
        if index >= len(CrossPreferences._image_flip_modes):
            return "ErrorImageFlipMode"

        return CrossPreferences._image_flip_modes[index]

    @staticmethod
    def get_index_by_image_flip_mode(flip_mode):
        for i in range(len(CrossPreferences._image_flip_modes)):
            if flip_mode == CrossPreferences._image_flip_modes[i]:
                return i
        
        return 0xFF

    """
    _hdmi_out_audio_channels
    """
    @staticmethod
    def get_hdmi_out_audio_channels():
        return CrossPreferences._hdmi_out_audio_channels

    @staticmethod
    def get_hdmi_out_audio_channel_by_index(index):
        if index >= len(CrossPreferences._hdmi_out_audio_channels):
            return "ErrorHDMIOutAudioChannel"

        return CrossPreferences._hdmi_out_audio_channels[index]

    @staticmethod
    def get_index_by_hdmi_out_audio_channel(audio_channel):
        for i in range(len(CrossPreferences._hdmi_out_audio_channels)):
            if audio_channel == CrossPreferences._hdmi_out_audio_channels[i]:
                return i
        
        return 0xFF

    """
    _hdmi_out_audio_channels_sdi
    """

    @staticmethod
    def get_hdmi_out_audio_channels_sdi():
        return CrossPreferences._hdmi_out_audio_channels_sdi

    @staticmethod
    def get_hdmi_out_audio_channel_sdi_by_index(index):
        if index >= len(CrossPreferences._hdmi_out_audio_channels_sdi):
            return "ErrorHDMIOutAudioChannel"

        return CrossPreferences._hdmi_out_audio_channels_sdi[index]

    @staticmethod
    def get_index_by_hdmi_out_audio_channel_sdi(audio_channel):
        for i in range(len(CrossPreferences._hdmi_out_audio_channels_sdi)):
            if audio_channel == CrossPreferences._hdmi_out_audio_channels_sdi[i]:
                return i

        return 0xFF

    """
    _sdi_out_audio_channels
    """
    @staticmethod
    def get_sdi_out_audio_channels():
        return CrossPreferences._sdi_out_audio_channels

    @staticmethod
    def get_sdi_out_audio_channel_by_index(index):
        if index >= len(CrossPreferences._sdi_out_audio_channels):
            return "ErrorSDIOutAudioChannel"

        return CrossPreferences._sdi_out_audio_channels[index]

    @staticmethod
    def get_index_by_sdi_out_audio_channel(audio_channel):
        for i in range(len(CrossPreferences._sdi_out_audio_channels)):
            if audio_channel == CrossPreferences._sdi_out_audio_channels[i]:
                return i
        
        return 0xFF

    """
    _sdi_out_audio_channels_sdi
    """
    @staticmethod
    def get_sdi_out_audio_channels_sdi():
        return CrossPreferences._sdi_out_audio_channels_sdi

    @staticmethod
    def get_sdi_out_audio_channel_sdi_by_index(index):
        if index >= len(CrossPreferences._sdi_out_audio_channels_sdi):
            return "ErrorSDIOutAudioChannel"

        return CrossPreferences._sdi_out_audio_channels_sdi[index]

    @staticmethod
    def get_index_by_sdi_out_audio_channel_sdi(audio_channel):
        for i in range(len(CrossPreferences._sdi_out_audio_channels_sdi)):
            if audio_channel == CrossPreferences._sdi_out_audio_channels_sdi[i]:
                return i

        return 0xFF

    """
    _scaler_refs
    """
    @staticmethod
    def get_scaler_refs():
        return CrossPreferences._scaler_refs

    @staticmethod
    def get_scaler_ref_by_index(index):
        if index >= len(CrossPreferences._scaler_refs):
            return "ErrorScalerRef"

        return CrossPreferences._scaler_refs[index]

    @staticmethod
    def get_index_by_scaler_ref(source):
        for i in range(len(CrossPreferences._scaler_refs)):
            if source == CrossPreferences._scaler_refs[i]:
                return i
        
        return 0xFF
    
    """
    _no_signal_indicators
    """
    @staticmethod
    def get_no_signal_indicators():
        return CrossPreferences._no_signal_indicators

    @staticmethod
    def get_no_signal_indicator_by_index(index):
        if index >= len(CrossPreferences._no_signal_indicators):
            return "ErrorNoSignalIndicator"

        return CrossPreferences._no_signal_indicators[index]

    @staticmethod
    def get_index_by_no_signal_indicator(indicator):
        for i in range(len(CrossPreferences._no_signal_indicators)):
            if indicator == CrossPreferences._no_signal_indicators[i]:
                return i
        
        return 0xFF

    """
    _lcd_off_times
    """
    @staticmethod
    def get_lcd_off_times():
        return CrossPreferences._lcd_off_times

    @staticmethod
    def get_lcd_off_time_by_index(index):
        if index >= len(CrossPreferences._lcd_off_times):
            return "ErrorLCDOffTime"

        return CrossPreferences._lcd_off_times[index]

    @staticmethod
    def get_index_by_lcd_off_time(off_time):
        for i in range(len(CrossPreferences._lcd_off_times)):
            if off_time == CrossPreferences._lcd_off_times[i]:
                return i
        
        return 0xFF

    """
    _back_to_status_times
    """
    @staticmethod
    def get_back_to_status_times():
        return CrossPreferences._back_to_status_times

    @staticmethod
    def get_back_to_status_time_by_index(index):
        if index >= len(CrossPreferences._back_to_status_times):
            return "ErrorBack2StatusTime"

        return CrossPreferences._back_to_status_times[index]

    @staticmethod
    def get_index_by_back_to_status_time(back_time):
        for i in range(len(CrossPreferences._back_to_status_times)):
            if back_time == CrossPreferences._back_to_status_times[i]:
                return i
        
        return 0xFF

    """
    _languages_list
    """
    @staticmethod
    def get_languages_by_index(index):
        if index >= len(CrossPreferences._languages_list):
            return CrossPreferences._languages_list[0]

        return CrossPreferences._languages_list[index]

    """
    _languages
    """
    @staticmethod
    def get_languages():
        return CrossPreferences._languages

    @staticmethod
    def get_language_by_index(index):
        if index >= len(CrossPreferences._languages):
            return "ErrorLanguage"

        return CrossPreferences._languages[index]

    @staticmethod
    def get_index_by_language(lan):
        for i in range(len(CrossPreferences._languages)):
            if lan == CrossPreferences._languages[i]:
                return i
        
        return 0xFF

    """
    _input_formats
    """
    @staticmethod
    def get_input_formats():
        return CrossPreferences._input_formats

    @staticmethod
    def get_input_format_by_index(index):
        if index >= len(CrossPreferences._input_formats):
            return "ErrorInputFormat"

        return CrossPreferences._input_formats[index]

    @staticmethod
    def get_index_by_input_format(input_format):
        for i in range(len(CrossPreferences._input_formats)):
            if input_format == CrossPreferences._input_formats[i]:
                return i

        return 0xFF
    

class SC7030Preferences(object):

    _output_resolutions = [
        "1080p60", "1080p59.94", "1080p50", "1080p30", "1080p29.97", "1080p25", "1080p24", "1080p23.98",
        "1080i60", "1080i59.94", "1080i50", "720p60", "720p59.94", "720p50", "576I", "480I"
    ]

    _video_inputs = ["SDI", "HDMI", "DVI", "VGA", "YPbPr", "S-video", "CVBS"]

    _m_out_radio = ["Original","4:3","5:4","16:9"]
    _m_out_radio_2 = ["16:9","4:3"]

    _audio_inputs = ["Follow Input", "Analog Audio"]
    _hdmi_out_range = ["Full Range", "Limited Range"]
    _3g_out_level = ["Level-A","Level-B"]

    @staticmethod
    def get_out_radio():
        return SC7030Preferences._m_out_radio

    @staticmethod
    def get_out_radio2():
        return SC7030Preferences._m_out_radio_2

    @staticmethod
    def get_output_resolutions():
        return SC7030Preferences._output_resolutions
    
    @staticmethod
    def get_video_inputs():
        return SC7030Preferences._video_inputs

    @staticmethod
    def get_audio_inputs():
        return SC7030Preferences._audio_inputs

    @staticmethod
    def get_hdmi_out_range():
        return SC7030Preferences._hdmi_out_range

    @staticmethod
    def get_3g_out_level():
        return SC7030Preferences._3g_out_level
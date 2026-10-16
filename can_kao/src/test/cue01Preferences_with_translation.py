from src.config.TranslationManager import TranslationManager

def dynamic_list_property(func):
    class DynamicListProperty:
        def __get__(self, instance, owner):
            return func(instance)
    return DynamicListProperty()

class Cue01Preferences(object):
    _formats = ["Auto",
            "480I60","578I50","480P60","576P50","720P60","720P50","1080I60","1080I50",
            "1080P60","1080P59.94","1080P50","1080P30","1080P29.97","1080P25","1080P24","1080P23.98",
            "2160P60","2160P59.94","2160P50","2160P30", "2160P29.97", "2160P25", "2160P24", "2160P23.98",   
            "4096P60", "4096P59.94", "4096P50", "4096P30", "4096P29.97","4096P25", "4096P24", "4096P23.98"
        ]
    
    _color_spaces = ["YUV420", "YUV422", "YUV444", "RGB"]

    _ranges = ["Full range", "Limited range"]

    _nr_modes = ["Off", "3D", "2D", "2D+3D"]

    _languages = ["English", "中文"]

    ''' ------------------------------------------------------------ 双语言的属性方法 -------------------------------------------------------------'''
    @dynamic_list_property
    def _inputs(self):
        if TranslationManager().current_language_index == 1:
            return ["前景", "背景", "辅助"]
        return ["Foreground", "Background", "AUX"]

    @dynamic_list_property
    def _color_tones(self):
        if TranslationManager().current_language_index == 1:
            return ["无", "绿色", "肤色"]
        return ["Off", "Green", "Skin Tone"]
    
    @dynamic_list_property
    def _bnr_intensities(self):
        if TranslationManager().current_language_index == 1:
            return ["高", "中", "低"]
        return ["High", "Middle", "Low"]

    @dynamic_list_property
    def _luma_video_sources(self):
        if TranslationManager().current_language_index == 1:
            return ["颜色1", "颜色2", "前景", "辅助", "黑场"]
        return ["Color1", "Color2", "Foreground", "AUX", "Black"]

    @dynamic_list_property
    def _chroma_video_sources(self):
        if TranslationManager().current_language_index == 1:
            return ["颜色1", "颜色2", "前景", "黑场"]
        return ["Color1", "Color2", "Foreground", "Black"]

    @dynamic_list_property
    def _spill_correction2_colors(self):
        if TranslationManager().current_language_index == 1:
            return ["关", "红", "绿", "蓝"]
        return ["Off", "Red", "Green", "Blue"]

    @dynamic_list_property
    def _dsk_video_sources(self):
        if TranslationManager().current_language_index == 1:
            return ["颜色1", "颜色2", "前景", "辅助", "黑场"]
        return ["Color1", "Color2", "Foreground", "AUX", "Black"]

    @dynamic_list_property
    def _fan_modes(self):
        if TranslationManager().current_language_index == 1:
            return ["关", "开", "自动"]
        return ["Off", "On", "Auto"]
    
    ''' ------------------------------------------------------------ 静态方法，用于外界对列表进行操作 ------------------------------------------------------------ '''
    @staticmethod
    def get_formats():
        return Cue01Preferences._formats

    @staticmethod
    def get_format_by_index(index):
        if index == 0xFE:
            return "Auto"
        elif index >= len(Cue01Preferences._formats):
            return "ErrorFormat"

        return Cue01Preferences._formats[index]

    @staticmethod
    def get_index_by_format(format):
        if format == "Auto":
            return 0xFF
        
        for i in range(len(Cue01Preferences._formats)):
            if format == Cue01Preferences._formats[i]:
                return i
        
        return 0xFF
    
    @staticmethod
    def get_color_spaces():
        return Cue01Preferences._color_spaces

    @staticmethod
    def get_color_space_by_index(index):
        if index >= len(Cue01Preferences._color_spaces):
            return "ErrorColorSpace"

        return Cue01Preferences._color_spaces[index]

    @staticmethod
    def get_index_by_color_space(color_space):
        for i in range(len(Cue01Preferences._color_spaces)):
            if color_space == Cue01Preferences._color_spaces[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_ranges():
        return Cue01Preferences._ranges

    @staticmethod
    def get_range_by_index(index):
        if index >= len(Cue01Preferences._ranges):
            return "ErrorRange"

        return Cue01Preferences._ranges[index]

    @staticmethod
    def get_index_by_range(rg):
        for i in range(len(Cue01Preferences._ranges)):
            if rg == Cue01Preferences._ranges[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_inputs():
        return Cue01Preferences._inputs

    @staticmethod
    def get_input_by_index(index):
        if index >= len(Cue01Preferences._inputs):
            return "ErrorInput"

        return Cue01Preferences._inputs[index]

    @staticmethod
    def get_index_by_input(_input_):
        for i in range(len(Cue01Preferences._inputs)):
            if _input_ == Cue01Preferences._inputs[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_color_tones():
        return Cue01Preferences._color_tones

    @staticmethod
    def get_color_tone_by_index(index):
        if index >= len(Cue01Preferences._color_tones):
            return "ErrorColorTone"

        return Cue01Preferences._color_tones[index]

    @staticmethod
    def get_index_by_color_tone(color_tone):
        for i in range(len(Cue01Preferences._color_tones)):
            if color_tone == Cue01Preferences._color_tones[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_nr_modes():
        return Cue01Preferences._nr_modes

    @staticmethod
    def get_nr_mode_by_index(index):
        if index >= len(Cue01Preferences._nr_modes):
            return "ErrorNRMode"

        return Cue01Preferences._nr_modes[index]

    @staticmethod
    def get_index_by_nr_mode(nr_mode):
        for i in range(len(Cue01Preferences._nr_modes)):
            if nr_mode == Cue01Preferences._nr_modes[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_bnr_intensities():
        return Cue01Preferences._bnr_intensities

    @staticmethod
    def get_bnr_intensity_by_index(index):
        if index >= len(Cue01Preferences._bnr_intensities):
            return "ErrorBNRIntensity"

        return Cue01Preferences._bnr_intensities[index]

    @staticmethod
    def get_index_by_bnr_intensity(nr_intensity):
        for i in range(len(Cue01Preferences._bnr_intensities)):
            if nr_intensity == Cue01Preferences._bnr_intensities[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_luma_video_sources():
        return Cue01Preferences._luma_video_sources

    @staticmethod
    def get_luma_video_src_by_index(index):
        if index >= len(Cue01Preferences._luma_video_sources):
            return "ErrorLumaVideoSrc"

        return Cue01Preferences._luma_video_sources[index]

    @staticmethod
    def get_index_by_luma_video_src(video_src):
        for i in range(len(Cue01Preferences._luma_video_sources)):
            if video_src == Cue01Preferences._luma_video_sources[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_chroma_video_sources():
        return Cue01Preferences._chroma_video_sources

    @staticmethod
    def get_chroma_video_src_by_index(index):
        if index >= len(Cue01Preferences._chroma_video_sources):
            return "ErrorChromaVideoSrc"

        return Cue01Preferences._chroma_video_sources[index]

    @staticmethod
    def get_index_by_chroma_video_src(video_src):
        for i in range(len(Cue01Preferences._chroma_video_sources)):
            if video_src == Cue01Preferences._chroma_video_sources[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_spill_correction2_colors():
        return Cue01Preferences._spill_correction2_colors

    @staticmethod
    def get_spill_correction2_color_by_index(index):
        if index >= len(Cue01Preferences._spill_correction2_colors):
            return "ErrorSpillCorrectionColor"

        return Cue01Preferences._spill_correction2_colors[index]

    @staticmethod
    def get_index_by_spill_correction2_color(color):
        for i in range(len(Cue01Preferences._spill_correction2_colors)):
            if color == Cue01Preferences._spill_correction2_colors[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_dsk_video_sources():
        return Cue01Preferences._dsk_video_sources

    @staticmethod
    def get_dsk_video_src_by_index(index):
        if index >= len(Cue01Preferences._dsk_video_sources):
            return "ErrorDskVideoSrc"

        return Cue01Preferences._dsk_video_sources[index]

    @staticmethod
    def get_index_by_dsk_video_src(video_src):
        for i in range(len(Cue01Preferences._dsk_video_sources)):
            if video_src == Cue01Preferences._dsk_video_sources[i]:
                return i
        
        return 0xFF
    
    @staticmethod
    def get_languages():
        return Cue01Preferences._languages

    @staticmethod
    def get_language_by_index(index):
        if index >= len(Cue01Preferences._languages):
            return "ErrorLanguage"

        return Cue01Preferences._languages[index]

    @staticmethod
    def get_index_by_language(lan):
        for i in range(len(Cue01Preferences._languages)):
            if lan == Cue01Preferences._languages[i]:
                return i
        
        return 0xFF
    
    @staticmethod
    def get_fan_modes():
        return Cue01Preferences._fan_modes

    @staticmethod
    def get_fan_mode_by_index(index):
        if index >= len(Cue01Preferences._fan_modes):
            return "ErrorFanMode"

        return Cue01Preferences._fan_modes[index]

    @staticmethod
    def get_index_by_fan_mode(fan_mode):
        for i in range(len(Cue01Preferences._fan_modes)):
            if fan_mode == Cue01Preferences._fan_modes[i]:
                return i
        
        return 0xFF

        
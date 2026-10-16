

class Cue01Preferences(object):
    _input_format = {
        0x12: "576i23.98",
        0x13: "576i24",
        0x14: "576i47.95",
        0x15: "576i25",
        0x16: "576i29.97",
        0x17: "576i30",
        0x18: "576i48",
        0x19: "576i50",
        0x1A: "576i59.94",
        0x1B: "576i60",
        0x22: "480i23.98",
        0x23: "480i24",
        0x24: "480i47.95",
        0x25: "480i25",
        0x26: "480i29.97",
        0x27: "480i30",
        0x28: "480i48",
        0x29: "480i50",
        0x2A: "480i59.94",
        0x2B: "480i60",
        0x32: "1280x720p23.98",
        0x33: "1280x720p24",
        0x34: "1280x720p47.95",
        0x35: "1280x720p25",
        0x36: "1280x720p29.97",
        0x37: "1280x720p30",
        0x38: "1280x720p48",
        0x39: "1280x720p50",
        0x3A: "1280x720p59.94",
        0x3B: "1280x720p60",
        0x42: "1920x1080i23.98",
        0x43: "1920x1080i24",
        0x44: "1920x1080i47.95",
        0x45: "1920x1080i25",
        0x46: "1920x1080i29.97",
        0x47: "1920x1080i30",
        0x48: "1920x1080i48",
        0x49: "1920x1080i50",
        0x4A: "1920x1080i59.94",
        0x4B: "1920x1080i60",
        0x52: "1920x1080p23.98",
        0x53: "1920x1080p24",
        0x54: "1920x1080p47.95",
        0x55: "1920x1080p25",
        0x56: "1920x1080p29.97",
        0x57: "1920x1080p30",
        0x58: "1920x1080p48",
        0x59: "1920x1080p50",
        0x5A: "1920x1080p59.94",
        0x5B: "1920x1080p60",
        0x62: "3840x2160p23.98",
        0x63: "3840x2160p24",
        0x64: "3840x2160p47.95",
        0x65: "3840x2160p25",
        0x66: "3840x2160p29.97",
        0x67: "3840x2160p30",
        0x68: "3840x2160p48",
        0x69: "3840x2160p50",
        0x6A: "3840x2160p59.94",
        0x6B: "3840x2160p60",
        0x72: "4096x2160p23.98",
        0x73: "4096x2160p24",
        0x74: "4096x2160p47.95",
        0x75: "4096x2160p25",
        0x76: "4096x2160p29.97",
        0x77: "4096x2160p30",
        0x78: "4096x2160p48",
        0x79: "4096x2160p50",
        0x7A: "4096x2160p59.94",
        0x7B: "4096x2160p60",
        0x82: "480p23.98",
        0x83: "480p24",
        0x84: "480p47.95",
        0x85: "480p25",
        0x86: "480p29.97",
        0x87: "480p30",
        0x88: "480p48",
        0x89: "480p50",
        0x8A: "480p59.94",
        0x8B: "480p60",
        0x92: "576p23.98",
        0x93: "576p24",
        0x94: "576p47.95",
        0x95: "576p25",
        0x96: "576p29.97",
        0x97: "576p30",
        0x98: "576p48",
        0x99: "576p50",
        0x9A: "576p59.94",
        0x9B: "576p60"
    }

    _formats = [
            "1280x720p60","1280x720p50","1920x1080i60","1920x1080i50",
            "1920x1080p60","1920x1080p59.94","1920x1080p50","1920x1080p30","1920x1080p29.97","1920x1080p25","1920x1080p24","1920x1080p23.98",
            "3840x2160p60","3840x2160p59.94","3840x2160p50","3840x2160p30", "3840x2160p29.97", "3840x2160p25", "3840x2160p24", "3840x2160p23.98",   
            "4096x2160p60", "4096x2160p59.94", "4096x2160p50", "4096x2160p30", "4096x2160p29.97","4096x2160p25", "4096x2160p24", "4096x2160p23.98"
        ]
    
    _aux_outputs = ["PGM", "PGM Clean", "DSK In", "BG In", "FG In"]
    
    _color_spaces = ["YUV420", "YUV422", "YUV444", "RGB"]

    _ranges = ["Full range", "Limited range"]

    _inputs = ["Foreground", "Background", "AUX"]

    _color_tones = ["Off", "Green", "Skin Tone"]

    _nr_modes = ["Off", "3D", "2D", "2D+3D"]

    _bnr_intensities = ["High", "Middle", "Low"]

    _luma_video_sources = ["Color1", "Color2", "Foreground", "AUX", "Black"]

    _chroma_key_colors = ["Green", "Blue", "Auto"]

    _chroma_video_sources = ["Color1", "Color2", "Foreground"]

    _spill_correction2_colors = ["Red", "Green", "Blue"]

    # _dsk_video_sources = ["Color1", "Color2", "Foreground", "AUX", "Black"]
    # _dsk_video_sources = ["AUX", "Picture"]
    _dsk_video_sources = ["DSK In"]

    _bg_sources = ["Color1", "Color2", "Background Input"]

    _languages = ["English", "中文"]

    _fan_modes = ["Off", "On", "Auto"]

    @staticmethod
    def get_input_formats():
        return Cue01Preferences._input_format
    
    @staticmethod
    def get_input_format_by_key(key):
        if key in Cue01Preferences._input_format:
            return Cue01Preferences._input_format[key]
        else:
            return "ErrorInputFormat"

    @staticmethod
    def get_key_by_input_format(input_format):
        for key in Cue01Preferences._input_format:
            if input_format == Cue01Preferences._input_format[key]:
                return key
        
        return 0xFF

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
    def get_aux_outputs():
        return Cue01Preferences._aux_outputs

    @staticmethod
    def get_aux_output_by_index(index):
        if index >= len(Cue01Preferences._aux_outputs):
            return "ErrorAuxOutput"

        return Cue01Preferences._aux_outputs[index]

    @staticmethod
    def get_index_by_aux_output(aux_output):
        for i in range(len(Cue01Preferences._aux_outputs)):
            if aux_output == Cue01Preferences._aux_outputs[i]:
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
    def get_chroma_key_colors():
        return Cue01Preferences._chroma_key_colors

    @staticmethod
    def get_chroma_key_color_by_index(index):
        if index >= len(Cue01Preferences._chroma_key_colors):
            return "ErrorChromaKeyColor"

        return Cue01Preferences._chroma_key_colors[index]

    @staticmethod
    def get_index_by_chroma_key_color(color):
        for i in range(len(Cue01Preferences._chroma_key_colors)):
            if color == Cue01Preferences._chroma_key_colors[i]:
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

    @staticmethod
    def get_dsk_video_sources():
        return Cue01Preferences._dsk_video_sources

    @staticmethod
    def get_dsk_video_src_by_index(index):
        return Cue01Preferences._dsk_video_sources[index]
    
    @staticmethod
    def get_index_by_dsk_video_src(video_src):
        for i in range(len(Cue01Preferences._dsk_video_sources)):
            if video_src == Cue01Preferences._dsk_video_sources[i]: 
                return i
        
        return 0xFF

    @staticmethod
    def get_bg_sources():
        return Cue01Preferences._bg_sources

    @staticmethod
    def get_bg_src_by_index(index):
        if index >= len(Cue01Preferences._bg_sources):
            return "ErrorBgSrc"

        return Cue01Preferences._bg_sources[index]

    @staticmethod
    def get_index_by_bg_src(bg_src):
        for i in range(len(Cue01Preferences._bg_sources)):
            if bg_src == Cue01Preferences._bg_sources[i]:
                return i
        
        return 0xFF 
    

        
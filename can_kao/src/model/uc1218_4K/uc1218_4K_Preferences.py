

class UC1218_4K_Preferences(object):
    _codec_channels = ["HeadphoneOut", "LineIn", "MicIn"]
    _codec_mic_in_volumes = ["Bypass", "20dB", "24dB", "30dB", "35dB", "40dB", "50dB", "52dB"]
    
    @staticmethod
    def get_codec_channels():
        return UC1218_4K_Preferences._codec_channels

    @staticmethod
    def get_codec_channel_by_index(index):
        if index >= len(UC1218_4K_Preferences._codec_channels):
            return "ErrorCodecChannel"

        return UC1218_4K_Preferences._codec_channels[index]

    @staticmethod
    def get_index_by_codec_channel(channel):
        for i in range(len(UC1218_4K_Preferences._codec_channels)):
            if channel == UC1218_4K_Preferences._codec_channels[i]:
                return i + 1
        
        return 0xFF
    
    @staticmethod
    def get_codec_mic_in_volumes():
        return UC1218_4K_Preferences._codec_mic_in_volumes

    @staticmethod
    def get_codec_mic_in_volume_by_index(index):
        if index >= len(UC1218_4K_Preferences._codec_mic_in_volumes):
            return "ErrorCodecMicInVolume"

        return UC1218_4K_Preferences._codec_mic_in_volumes[index]

    @staticmethod
    def get_index_by_codec_mic_in_volume(volume):
        for i in range(len(UC1218_4K_Preferences._codec_mic_in_volumes)):
            if volume == UC1218_4K_Preferences._codec_mic_in_volumes[i]:
                return i
        
        return 0xFF

    @staticmethod
    def get_index_by_channel_and_volume(channel, volume):
        index = 0x00
        if channel == UC1218_4K_Preferences._codec_channels[0]: # HP Out
            index = int((12.0 - volume)/1.5)
            index = index if 0x00 <= index <= 0x27 else 0xFF
        elif channel == UC1218_4K_Preferences._codec_channels[1]: # Line In
            index = int((12.0 - volume)/1.5)
            index = index if 0x00 <= index <= 0x1F else 0xFF
        elif channel == UC1218_4K_Preferences._codec_channels[2]: # Mic In
            if volume in UC1218_4K_Preferences._codec_mic_in_volumes:
                index = UC1218_4K_Preferences.get_index_by_codec_mic_in_volume(volume)
            else:
                index = 0xFF

        return index
    

        
import logging
from src.model.modelPreferences import ModelPreferences, ModelContinuousTask
from src.model.uc1218_4K.uc1218_4K_Preferences import UC1218_4K_Preferences
from src.model.modelRticePreferences import ModelRticePreferences

class UC1218_4K_Model(object):
    def __init__(self, app) -> None:
        self._app = app
        self._mc_task = ModelContinuousTask(self._action_handle)

    def _action_handle(self, task):
        if task["type"] == "usb":
            self._app.async_action_usb(task["dev_sn"], task["cmd"], task["data"], task["cb"])
        elif task["type"] == "rtice":
            self._app.async_action_rtice(task["dev_sn"], task["func"], task["args"], task["cb"])
        else:
            logging.error("Unknow task type: {}".format(task["type"]))

    def __get_version_info_callback(self, dev_sn, args):
        _args = ModelPreferences.sc_handle_version_info(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_version_info(self, dev_sn):
        _cmd = 0x16
        _data = []

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_version_info_callback)

    @staticmethod
    def handle_get_codec_volume_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))
        _micInVolumeList = ["Bypass", "+20dB", "+24dB", "+30dB", "+35dB", "+40dB", "+44dB", "+50dB", "+52dB"]

        _args = {
            "function": "get_codec_volume",
            "args": {
                "HeadphoneOut":{
                    "volume": 8 - args[8],
                    "db": f"{12 - (args[8]*1.5)}dB",
                    "mute": True if (args[11] & 0x01) != 0x00 else False 
                },
                "LineIn": {
                    "volume": 8 - args[9],
                    "db": f"{12 - (args[9]*1.5)}dB",
                    "mute": True if (args[11] & 0x02) != 0x00 else False 
                },
                "MicIn": {
                    "volume": args[10],
                    "db": f"{_micInVolumeList[args[10]]}" if args[10] < len(_micInVolumeList) else "Reserved",
                    "mute": True if (args[11] & 0x04) != 0x00 else False 
                },
                "I2SMixer": {
                    "MicInToI2SEnable": True if (args[12] & 0x01) == 0x00 else False,
                    "LineInToI2SEnable": True if (args[12] & 0x02) == 0x00 else False,
                    "MicInToHpEnable": True if (args[12] & 0x04) == 0x00 else False,
                    "LineInToHpEnable": True if (args[12] & 0x08) == 0x00 else False,
                    "I2SToHpEnable": True if (args[12] & 0x10) == 0x00 else False,
                }
            }
        }
        return _args

    def __get_codec_volume_callback(self, dev_sn, args):
        _args = UC1218_4K_Model.handle_get_codec_volume_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_codec_volume(self, dev_sn):
        _cmd = 0xD0
        _data = []

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_codec_volume_callback)

    """
    Volume Setting
    """
    def __set_codec_volume_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_codec_volume",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_codec_volume")
        self._app.async_callback(dev_sn, _args)

    def async_set_codec_volume(self, dev_sn, args):
        _cmd = 0xD1
        _data = []
        _valid = 0x0000
        _channel = 0x00
        _volume = 0x00

        logging.debug("args:{}".format(args))

        if "Channel" in args:
            _channel = UC1218_4K_Preferences.get_index_by_codec_channel(args["Channel"]) 

            if _channel == 0xFF:
                logging.error("Error Codec Channel: {}".format(args["Channel"]))
            else:
                _valid |= 0x0001
        
        if "Volume" in args:
            _volume = UC1218_4K_Preferences.get_index_by_channel_and_volume(args["Channel"], args["Volume"])
            if _volume == 0xFF:
                logging.error("Error Volume: {}".format(args["Volume"]))
                _valid = 0x0000
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _channel.to_bytes(1, "big")
        _data += _volume.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_codec_volume_callback)
        _task = {
            "dev_sn": dev_sn,
            "type": "usb",
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_codec_volume_callback
        }

        self._mc_task.do_current_task("set_codec_volume", _task)
    
    def __set_codec_mute_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_codec_mute",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_codec_mute(self, dev_sn, args):
        _cmd = 0xD2
        _data = []
        _valid = 0x0000
        _channel = 0x00
        _mute = 0x00

        logging.debug("args:{}".format(args))

        if "Channel" in args:
            _channel = UC1218_4K_Preferences.get_index_by_codec_channel(args["Channel"]) 

            if _channel == 0xFF:
                logging.error("Error Codec Channel: {}".format(args["Channel"]))
            else:
                _valid |= 0x0001
        
        if "Mute" in args:
            _mute = 0x01 if args["Mute"] is True else 0x00

        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _channel.to_bytes(1, "big")
        _data += _mute.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_codec_mute_callback)

    def __set_codec_mixer_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_codec_mixer",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_codec_mixer(self, dev_sn, args):
        _cmd = 0xD3
        _data = []
        _valid = 0x00
        _state = 0x00

        logging.debug("args:{}".format(args))

        if "MicInToI2SEnable" in args:
            _valid |= 0x01
            _state |= 0x00 if args["MicInToI2SEnable"] is True else 0x01 # 0: 开启， 1：关闭

        if "LineInToI2SEnable" in args:
            _valid |= 0x02
            _state |= 0x00 if args["LineInToI2SEnable"] is True else 0x02 # 0: 开启， 1：关闭

        if "MicInToHpEnable" in args:
            _valid |= 0x04
            _state |= 0x00 if args["MicInToHpEnable"] is True else 0x04 # 0: 开启， 1：关闭

        if "LineInToHpEnable" in args:
            _valid |= 0x08
            _state |= 0x00 if args["LineInToHpEnable"] is True else 0x08 # 0: 开启， 1：关闭
        
        if "I2SInToHpEnable" in args:
            _valid |= 0x10
            _state |= 0x00 if args["I2SInToHpEnable"] is True else 0x10 # 0: 开启， 1：关闭
        
        if _valid == 0x00:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(1, "big")
        _data += _state.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_codec_mixer_callback)

    def __factory_reset_codec_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "factory_reset_codec",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_factory_reset_codec(self, dev_sn):
        _cmd = 0xD4
        _data = []
        
        logging.debug("_data:{}".format(_data))
        self._app.async_action_usb(dev_sn, _cmd, _data, self.__factory_reset_codec_callback)
    
    def __init_rtice_device_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "init_rtice_device",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_init_rtice_device(self, dev_sn):
        _func = "init_device"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__init_rtice_device_callback)

    def __deinit_rtice_device_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "deinit_rtice_device",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_deinit_rtice_device(self, dev_sn):
        _func = "deinit_device"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__deinit_rtice_device_callback)

    """
    Get RTICE customer version
    """
    def __get_rtice_customer_version_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_customer_version",
            "args": {
                "Result": args["Result"],
                "Version": args["Version"] if args["Result"] else ""
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_customer_version(self, dev_sn):
        _func = "get_customer_version"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_customer_version_callback)

    """
    Get RTICE USB iProduct
    """
    def __get_rtice_USB_iProduct_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_USB_iProduct",
            "args": {
                "Result": args["Result"],
                "iProduct": args["iProduct"] if args["Result"] else ""
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_USB_iProduct(self, dev_sn):
        _func = "get_USB_iProduct"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_USB_iProduct_callback)

    """
    Get RTICE UVC Name
    """
    def __get_rtice_UVC_Name_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_UVC_Name",
            "args": {
                "Result": args["Result"],
                "UVCName": args["UVCName"] if args["Result"] else ""
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_UVC_Name(self, dev_sn):
        _func = "get_UVC_Name"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_UVC_Name_callback)

    """
    Get RTICE UAC Name
    """
    def __get_rtice_UAC_Name_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_UAC_Name",
            "args": {
                "Result": args["Result"],
                "UACName": args["UACName"] if args["Result"] else ""
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_UAC_Name(self, dev_sn):
        _func = "get_UAC_Name"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_UAC_Name_callback)

    """
    Get RTICE UAC OUT2 Name
    """
    def __get_rtice_UAC_OUT2_Name_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_UAC_OUT2_Name",
            "args": {
                "Result": args["Result"],
                "UACOut2Name": args["UACOut2Name"] if args["Result"] else ""
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_UAC_OUT2_Name(self, dev_sn):
        _func = "get_UAC_OUT2_Name"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_UAC_OUT2_Name_callback)

    """
    Get RTICE UAC IN Name
    """
    def __get_rtice_UAC_IN_Name_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_UAC_IN_Name",
            "args": {
                "Result": args["Result"],
                "UACInName": args["UACInName"] if args["Result"] else ""
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_UAC_IN_Name(self, dev_sn):
        _func = "get_UAC_IN_Name"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_UAC_IN_Name_callback)

    """
    Get RTICE UAC IN Name
    """
    def __get_rtice_HdmiRX_RawTimingInfo_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_HdmiRX_RawTimingInfo",
            "args": {
                "Result": args["Result"],
                "IsInterlace": True if args["is_interlace"] else False,
                "Resolution": "{}x{}".format(args["hActive"], args["vActive"]) if args["Result"] else "0x0",
                "FrameRate": "{}".format(round(args["vFreq"]/100, 2) if (args["vFreq"]%100 != 0) else int(args["vFreq"]/100)) if args["Result"] else "0",
                "ColorSpace": ModelRticePreferences._colorSpaceList[args["colorspace"]] if args["Result"] else "",
                "ColorRange": ModelRticePreferences._hdmiTimingInfoColorRangeModeList[args["colorrange"]] if args["Result"] else "",
                "ColorDepth": "{}bit".format(ModelRticePreferences._colorDepthList[args["colordepth"]]) if args["Result"] else ""
            }
        }
        
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_HdmiRX_RawTimingInfo(self, dev_sn):
        _func = "get_HdmiRX_RawTimingInfo"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_HdmiRX_RawTimingInfo_callback)

    """
    Get RTICE HDMI volume gain
    """
    def __get_rtice_Audio_HdmiDPRX_VolumeGain_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_Audio_HdmiDPRX_VolumeGain",
            "args": {
                "Result": args["Result"],
                "Gain": args["Gain"] if args["Result"] else 0
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_Audio_HdmiDPRX_VolumeGain(self, dev_sn):
        _func = "get_Audio_HdmiDPRX_VolumeGain"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_Audio_HdmiDPRX_VolumeGain_callback)

    def __set_rtice_Audio_HdmiDPRX_VolumeGain_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_Audio_HdmiDPRX_VolumeGain",
            "args": {
                "Result": args["Result"]
            }
        }

        self._mc_task.do_next_task("set_Audio_HdmiDPRX_VolumeGain")
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_Audio_HdmiDPRX_VolumeGain(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_Audio_HdmiDPRX_VolumeGain"

        # self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_Audio_HdmiDPRX_VolumeGain_callback)
        _task = {
            "dev_sn": dev_sn,
            "type": "rtice",
            "func": _func,
            "args": args,
            "cb": self.__set_rtice_Audio_HdmiDPRX_VolumeGain_callback
        }

        self._mc_task.do_current_task("set_Audio_HdmiDPRX_VolumeGain", _task)

    def __get_rtice_Audio_UAC_VolumeGain_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_Audio_UAC_VolumeGain",
            "args": {
                "Result": args["Result"],
                "Gain": args["Gain"] if args["Result"] else 0
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_Audio_UAC_VolumeGain(self, dev_sn):
        _func = "get_Audio_UAC_VolumeGain"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_Audio_UAC_VolumeGain_callback)

    def __set_rtice_Audio_UAC_VolumeGain_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_Audio_UAC_VolumeGain",
            "args": {
                "Result": args["Result"]
            }
        }
        self._mc_task.do_next_task("set_Audio_UAC_VolumeGain")
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_Audio_UAC_VolumeGain(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_Audio_UAC_VolumeGain"

        # self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_Audio_UAC_VolumeGain_callback)
        _task = {
            "dev_sn": dev_sn,
            "type": "rtice",
            "func": _func,
            "args": args,
            "cb": self.__set_rtice_Audio_UAC_VolumeGain_callback
        }

        self._mc_task.do_current_task("set_Audio_UAC_VolumeGain", _task)

    def __get_rtice_Audio_I2SOut_MixerSource_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_Audio_I2SOut_MixerSource",
            "args": {
                "Result": args["Result"],
                "MixerSource": args["MixerSource"] if args["Result"] else []
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_Audio_I2SOut_MixerSource(self, dev_sn):
        _func = "get_Audio_I2SOut_MixerSource"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_Audio_I2SOut_MixerSource_callback)

    def __set_rtice_Audio_I2SOut_MixerSource_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_Audio_I2SOut_MixerSource",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_Audio_I2SOut_MixerSource(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_Audio_I2SOut_MixerSource"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_Audio_I2SOut_MixerSource_callback)
    
    def __get_rtice_Audio_UACOut2_MixerSource_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_Audio_UACOut2_MixerSource",
            "args": {
                "Result": args["Result"],
                "MixerSource": args["MixerSource"] if args["Result"] else []
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_Audio_UACOut2_MixerSource(self, dev_sn):
        _func = "get_Audio_UACOut2_MixerSource"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_Audio_UACOut2_MixerSource_callback)

    def __set_rtice_Audio_UACOut2_MixerSource_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_Audio_UACOut2_MixerSource",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_Audio_UACOut2_MixerSource(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_Audio_UACOut2_MixerSource"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_Audio_UACOut2_MixerSource_callback)

    def __get_rtice_EDID_mode_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_EDID_mode",
            "args": {
                "Result": args["Result"],
                "EdidMode": args["EdidMode"] if args["Result"] else ""
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_EDID_mode(self, dev_sn):
        _func = "get_EDID_mode"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_EDID_mode_callback)

    def __set_rtice_EDID_mode_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_EDID_mode",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_EDID_mode(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_EDID_mode"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_EDID_mode_callback)
        
    def __get_rtice_ColorRange_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_ColorRange",
            "args": {
                "Result": args["Result"],
                "ColorRange": args["ColorRange"] if args["Result"] else ""
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_ColorRange(self, dev_sn, args):
        _func = "get_ColorRange"
        return self._app.async_action_rtice(dev_sn, _func, args, self.__get_rtice_ColorRange_callback)

    def __set_rtice_ColorRange_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_rtice_ColorRange",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_ColorRange(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_ColorRange"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_ColorRange_callback)

    def __get_rtice_EDID_DDC_RX_table_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_EDID_DDC_RX_table",
            "args": {
                "Result": args["Result"],
                "EDIDTable": args["EDIDTable"]  if args["Result"] else []
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_EDID_DDC_RX_table(self, dev_sn):
        _func = "get_EDID_DDC_RX_table"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_EDID_DDC_RX_table_callback)

    def __set_rtice_EDID_DDC_RX_table_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_rtice_EDID_DDC_RX_table",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_EDID_DDC_RX_table(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_EDID_DDC_RX_table"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_EDID_DDC_RX_table_callback)

    def __set_rtice_Flash_CustomerProprietary_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_rtice_Flash_CustomerProprietary",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_Flash_CustomerProprietary(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_Flash_CustomerProprietary"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_Flash_CustomerProprietary_callback)

    def __get_rtice_Flash_CustomerProprietary_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_Flash_CustomerProprietary",
            "args": {
                "Result": args["Result"],
                "CustomerProprietary": args["CustomerProprietary"]  if args["Result"] else []
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_Flash_CustomerProprietary(self, dev_sn):
        _func = "get_Flash_CustomerProprietary"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_Flash_CustomerProprietary_callback)

    def __set_rtice_ConfigData_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_rtice_ConfigData",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_ConfigData(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_ConfigData"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_ConfigData_callback)

    def __get_rtice_ConfigData_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_ConfigData",
            "args": {
                "Result": args["Result"],
                "ConfigData": args["ConfigData"]  if args["Result"] else []
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_ConfigData(self, dev_sn):
        _func = "get_ConfigData"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_ConfigData_callback)

    def __set_rtice_RestoreToDefault_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_RestoreToDefault",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_RestoreToDefault(self, dev_sn):
        _func = "set_RestoreToDefault"
        _args = ""
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__set_rtice_RestoreToDefault_callback)

    def __set_rtice_EDID_Flash_table_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_rtice_EDID_Flash_table",
            "args": {
                "Result": args["Result"]
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_EDID_Flash_table(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_EDID_Flash_table"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_EDID_Flash_table_callback)

    def __get_rtice_EDID_Flash_table_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_EDID_Flash_table",
            "args": {
                "Result": args["Result"],
                "EDIDTableIndex": args["EDIDTableIndex"]  if args["Result"] else [],
                "EDIDTable": args["EDIDTable"]  if args["Result"] else []
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_EDID_Flash_table(self, dev_sn, args):
        _func = "get_EDID_Flash_table"
        
        return self._app.async_action_rtice(dev_sn, _func, args, self.__get_rtice_EDID_Flash_table_callback)

    def __set_rtice_EDID_Flash_Table_Name_List_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_rtice_EDID_Flash_Table_Name_List",
            "args": {
                "Result": args["Result"],
                "NameList": args["NameList"]  if args["Result"] else []
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_EDID_Flash_Table_Name_List(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_EDID_Flash_Table_Name_List"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_EDID_Flash_Table_Name_List_callback)

    def __get_rtice_EDID_Flash_Table_Name_List_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_EDID_Flash_Table_Name_List",
            "args": {
                "Result": args["Result"],
                "Version": args["Version"]  if args["Result"] else [],
                "NameList": args["NameList"]  if args["Result"] else []
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_EDID_Flash_Table_Name_List(self, dev_sn):
        _func = "get_EDID_Flash_Table_Name_List"
        _args = ""
        
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_EDID_Flash_Table_Name_List_callback)

    def __set_rtice_EDID_Flash_Default_table_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_rtice_EDID_Flash_Default_table",
            "args": {
                "Result": args["Result"],
                "EDIDTableIndex": args["EDIDTableIndex"]  if args["Result"] else 0
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_rtice_EDID_Flash_Default_table(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _func = "set_EDID_Flash_Default_table"

        self._app.async_action_rtice(dev_sn, _func, args, self.__set_rtice_EDID_Flash_Default_table_callback)

    def __get_rtice_EDID_Flash_Default_table_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_rtice_EDID_Flash_Default_table",
            "args": {
                "Result": args["Result"],
                "EDIDTableIndex": args["EDIDTableIndex"]  if args["Result"] else 0,
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_get_rtice_EDID_Flash_Default_table(self, dev_sn):
        _func = "get_EDID_Flash_Default_table"
        _args = ""
        
        return self._app.async_action_rtice(dev_sn, _func, _args, self.__get_rtice_EDID_Flash_Default_table_callback)

    
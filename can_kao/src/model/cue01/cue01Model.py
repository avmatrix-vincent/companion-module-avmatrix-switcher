import logging
from src.model.cue01.cue01Preferences import Cue01Preferences
from src.model.modelPreferences import ModelPreferences, ModelContinuousTask
import threading
import queue
from _thread import *
import traceback

class Cue01Model(object):
    def __init__(self, app) -> None:
        self._app = app
        self._mc_task = ModelContinuousTask(self._action_handle)

    def _action_handle(self, task):
        self._app.async_action(task["dev_sn"], task["cmd"], task["data"], task["cb"])

    def __get_version_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        mcu_version = "V{}.{}.{}.{}".format(args[0], args[1], args[2], args[3])
        mdin640_version = "V{}.{}.{}.{}".format(args[4], args[5], args[6], args[7])
        keyboard_version = "V{}.{}.{}.{}".format(args[8], args[9], args[10], args[11])
        pcb_version = "V{}.{}".format(args[12], args[13])

        _args = {
            "function": "get_version",
            "args": {
                "McuVersion": mcu_version,
                "Mdin640Version": mdin640_version,
                "KeyboardVersion": keyboard_version,
                "PcbVersion": pcb_version
            }
        }
        self._app.async_callback(dev_sn, _args)

    # 异步获取版本信息
    def async_get_version(self, dev_sn):
        _cmd = 0x0001
        _data = []
        # _data_length = len(_data)

        self._app.async_action(dev_sn, _cmd, _data, self.__get_version_callback)

    # 获取输入状态回调
    @staticmethod
    def handle_input_status(args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        _input_formats = Cue01Preferences.get_input_formats()

        _color_spaces = ["YUV420", "YUV422", "YUV444", "RGB"]

        _ranges = ["Full range", "Limited range"]

        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_input_status",
            "args": {
                "ChannelNumber": 3,
                "Video": [
                    {
                        "Format": "None" if args[0]==0xFE else _input_formats[args[0]],
                        "ColorSpace": "None" if args[1]==0xFE else _color_spaces[args[1]],
                        "BitDepth": 0 if args[2]==0xFE else args[2],
                        "Range": "None" if args[3]==0xFE else _ranges[args[3]]
                    },
                    {
                        "Format": "None" if args[4]==0xFE else _input_formats[args[4]],
                        "ColorSpace": "None" if args[5]==0xFE else _color_spaces[args[5]],
                        "BitDepth": 0 if args[6]==0xFE else args[6],
                        "Range": "None" if args[7]==0xFE else _ranges[args[7]]
                    },
                    {
                        "Format": "None" if args[8]==0xFE else _input_formats[args[8]],
                        "ColorSpace": "None" if args[9]==0xFE else _color_spaces[args[9]],
                        "BitDepth": 0 if args[10]==0xFE else args[10],
                        "Range": "None" if args[11]==0xFE else _ranges[args[11]]
                    }
                ]
            }
        }

        return _args
    
    def __get_input_status_callback(self, dev_sn, args):
        _args = Cue01Model.handle_input_status(args)
        self._app.async_callback(dev_sn, _args)

    # 异步获取输入状态
    def async_get_input_status(self, dev_sn):
        _cmd = 0x0004
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_input_status_callback)

    @staticmethod
    def handle_ref_enhance_params(args): # 处理外同步信号和视频增强参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        _reference_inputs = ["Background", "Foreground", "AUX"]
        _video_sources = ["Background", "Foreground", "AUX"]
        _ltis = ["Off", "On"]
        _ctis = ["Off", "On"]
        _color_tones = ["Off", "Green", "Human"]
        _channel0_addr_offset = 2
        _channel1_addr_offset = 13
        _channel2_addr_offset = 24

        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_ref_enhance_params",
            "args": {
                "ReferenceInput": _reference_inputs[args[0]],
                "VideoSource": _video_sources[args[1]],
                "ChannelNumber": 3,
                "Video": [
                    {
                        "Contrast": args[_channel0_addr_offset],
                        "Brightness": args[_channel0_addr_offset + 1],
                        "Saturation": args[_channel0_addr_offset + 2],
                        "Hue": args[_channel0_addr_offset + 3],
                        "LTI": _ltis[args[_channel0_addr_offset + 4]],
                        "CTI": _ctis[args[_channel0_addr_offset + 5]],
                        "ColorTone": _color_tones[args[_channel0_addr_offset + 6]],
                        "HAntiAlias": args[_channel0_addr_offset + 7],
                        "VAntiAlias": args[_channel0_addr_offset + 8],
                        "HPeakFilter": args[_channel0_addr_offset + 9],
                        "VPeakFilter": args[_channel0_addr_offset + 10]
                    },
                    {
                        "Contrast": args[_channel1_addr_offset],
                        "Brightness": args[_channel1_addr_offset + 1],
                        "Saturation": args[_channel1_addr_offset + 2],
                        "Hue": args[_channel1_addr_offset + 3],
                        "LTI": _ltis[args[_channel1_addr_offset + 4]],
                        "CTI": _ctis[args[_channel1_addr_offset + 5]],
                        "ColorTone": _color_tones[args[_channel1_addr_offset + 6]],
                        "HAntiAlias": args[_channel1_addr_offset + 7],
                        "VAntiAlias": args[_channel1_addr_offset + 8],
                        "HPeakFilter": args[_channel1_addr_offset + 9],
                        "VPeakFilter": args[_channel1_addr_offset + 10]
                    },
                    {
                        "Contrast": args[_channel2_addr_offset],
                        "Brightness": args[_channel2_addr_offset + 1],
                        "Saturation": args[_channel2_addr_offset + 2],
                        "Hue": args[_channel2_addr_offset + 3],
                        "LTI": _ltis[args[_channel2_addr_offset + 4]],
                        "CTI": _ctis[args[_channel2_addr_offset + 5]],
                        "ColorTone": _color_tones[args[_channel2_addr_offset + 6]],
                        "HAntiAlias": args[_channel2_addr_offset + 7],
                        "VAntiAlias": args[_channel2_addr_offset + 8],
                        "HPeakFilter": args[_channel2_addr_offset + 9],
                        "VPeakFilter": args[_channel2_addr_offset + 10]
                    }
                ]
            }
        }
        return _args

    def __get_ref_enhance_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_ref_enhance_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_ref_enhance_params(self, dev_sn):
        _cmd = 0x0090
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_ref_enhance_params_callback)

    @staticmethod
    def handle_noise_reduction_params(args): # 处理视频图像降噪参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        _video_sources = ["Background", "Foreground", "AUX"]
        _nr_modes = ["Off", "3D", "2D", "2D+3D"]
        _nr_motion_displays = ["Off", "On"]
        _bnr_modes = ["Off", "On"]
        _bnr_intensity = ["High", "Middle", "Low"]
        _block_displays = ["Off", "On"]

        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_noise_reduction_params",
            "args": {
                "VideoSource": _video_sources[args[0]],
                "ChannelNumber": 3,
                "Video": [
                    {
                        "NRMode": _nr_modes[args[1]],
                        "NRMotionDisplay": _nr_motion_displays[args[2]]
                    },
                    {
                        "NRMode": _nr_modes[args[3]],
                        "NRMotionDisplay": _nr_motion_displays[args[4]]
                    },
                    {
                        "NRMode": _nr_modes[args[5]],
                        "NRMotionDisplay": _nr_motion_displays[args[6]]
                    }
                ],
                "BNRMode": _bnr_modes[args[7]],
                "BNRIntensity": _bnr_intensity[args[8]],
                "BlockCoordinateX": ((args[9]>>4) & 0x0f),
                "BlockCoordinateY": (args[9] & 0x0f),
                "BlockDisplay": _block_displays[args[10]],
                "BlockThreshold": args[11]
            }
        }
        return _args

    def __get_noise_reduction_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_noise_reduction_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_noise_reduction_params(self, dev_sn):
        _cmd = 0x0091
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_noise_reduction_params_callback)

    @staticmethod
    def handle_source_params(args): # 处理源参数
        logging.debug("args:{}".format(args))
        _args = {
            "function": "get_source_params",
            "args": {
                "BackgroundSource": Cue01Preferences.get_bg_src_by_index(args[0]),
                "MatteSource": args[1],
                "AuxOutput": Cue01Preferences.get_aux_output_by_index(args[2])
            }
        }
        return _args

    def __get_source_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_source_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_source_params(self, dev_sn):
        _cmd = 0x009B
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_source_params_callback)

    @staticmethod
    def handle_output_interface_params(args): # 处理输出接口参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        _formats = Cue01Preferences.get_formats() ######################################################

        _color_spaces = Cue01Preferences.get_color_spaces()

        _ranges = Cue01Preferences.get_ranges()

        logging.debug("args:{}".format(args))
        _args = {
            "function": "get_output_interface_params",
            "args": {
                "Number": 4,
                "Output": [
                    {
                        "Format": "Auto" if args[0]==0xFF else _formats[args[0]],
                        "ColorSpace": _color_spaces[args[1]],
                        "Range": _ranges[args[2]]
                    },
                    {
                        "Format": "Auto" if args[3]==0xFF else _formats[args[3]],
                        "ColorSpace": _color_spaces[args[4]],
                        "Range": _ranges[args[5]]
                    },
                    {
                        "Format": "Auto" if args[6]==0xFF else _formats[args[6]],
                        "ColorSpace": _color_spaces[args[7]],
                        "Range": _ranges[args[8]]
                    },
                    {
                        "Format": Cue01Preferences.get_format_by_index(args[9]),
                        "ColorSpace": _color_spaces[args[10]],
                        "Range": _ranges[args[11]]
                    }
                ]
            }
        }
        print(args[9], Cue01Preferences.get_format_by_index(args[9]))
        return _args

    def __get_output_interface_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_output_interface_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_output_interface_params(self, dev_sn):
        _cmd = 0x0092
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_output_interface_params_callback)

    @staticmethod
    def handle_color_generation_params(args): # 处理颜色生成器参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_color_generation_params",
            "args": {
                "ColorNumber": 2,
                "Color": [
                    {
                        "Red": args[0],
                        "Green": args[1],
                        "Blue": args[2]
                    },
                    {
                        "Red": args[3],
                        "Green": args[4],
                        "Blue": args[5]
                    }
                ]
            }
        }
        return _args

    def __get_color_generation_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_color_generation_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_color_generation_params(self, dev_sn):
        _cmd = 0x0093
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_color_generation_params_callback)

    @staticmethod
    def handle_luma_params(args): # 处理 luma 参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        _switch_value = ["Off", "On"]
        
        _args = {
            "function": "get_luma_params",
            "args": {
                "Status": args[0],
                "ToleranceLeft": int.from_bytes(args[1:3], byteorder='big'),
                "ToleranceRight": int.from_bytes(args[3:5], byteorder='big'),
                "ToleranceCurveSwitch": _switch_value[args[5]],
                "ToleranceInvertSwitch": _switch_value[args[6]],
                "ToleranceUnitStep": int.from_bytes(args[7:9], byteorder='big'),
                "ClipSwitch": _switch_value[args[9]],
                "ClipLeft": int.from_bytes(args[10:12], byteorder='big'),
                "ClipRight": int.from_bytes(args[12:14], byteorder='big'),
                "ClipCurveSwitch": _switch_value[args[14]]
            }
        }
        return _args

    def __get_luma_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_luma_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_luma_params(self, dev_sn):
        _cmd = 0x0094
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_luma_params_callback)

    @staticmethod
    def handle_chroma_params(args): # 处理 Chroma 参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))

        _video_sources = Cue01Preferences.get_chroma_video_sources()
        _switch_value = ["Off", "On"]
        _spill_correction_param = Cue01Preferences.get_spill_correction2_colors()
        
        _args = {
            "function": "get_chroma_params",
            "args": {
                "VideoSource": _video_sources[args[0]],
                "PosX": int.from_bytes(args[1:3], byteorder='big'),
                "PosY": int.from_bytes(args[3:5], byteorder='big'),
                "ColorKeyRed": args[5],
                "ColorKeyGreen": args[6],
                "ColorKeyBlue": args[7],
                "ColorKeyAngle": args[8],
                "ColorKeyTolerance": args[9],
                "ColorKeySoftness": args[10],
                "KeySetForeground": int.from_bytes(args[11:13], byteorder='big'),
                "KeySetBackground": int.from_bytes(args[13:15], byteorder='big'),
                "KeySetEdge": int.from_bytes(args[15:17], byteorder='big'),
                "ClipSwitch": _switch_value[args[17]],
                "ClipCurveSwitch": _switch_value[args[18]],
                "ClipLeft": int.from_bytes(args[19:21], byteorder='big'),
                "ClipRight": int.from_bytes(args[21:23], byteorder='big'),
                "SpillCorrectionSwitch": _switch_value[args[23]],
                "SpillCorrectionEdge": int.from_bytes(args[24:26], byteorder='big'),
                "SpillCorrectionBackground": int.from_bytes(args[26:28], byteorder='big'),
                "SpillCorrection2Switch": _switch_value[args[28]],
                "SpillCorrection2Param": _spill_correction_param[args[29] - 1],
                "SpillCorrection2Value": int.from_bytes(args[30:32], byteorder='big'),
                "ColorAdjBrightness": args[32],
                "ColorAdjContract": args[33],
                "ColorAdjSaturation": args[34],
                "ColorAdjRed": args[35],
                "ColorAdjGreen": args[36],
                "ColorAdjBlue": args[37],
                "Status": args[38],
                "KeyColor": args[39]
            }
        }
        return _args

    def __get_chroma_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_chroma_params(args)    
        self._app.async_callback(dev_sn, _args)

    def async_get_chroma_params(self, dev_sn):
        _cmd = 0x0095
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_chroma_params_callback)

    @staticmethod
    def handle_usk_layer_params(args): # 处理 USK 参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))

        _switch_value = ["Off", "On"]
        
        _args = {
            "function": "get_usk_layer_params",
            "args": {
                "PipSwitch": _switch_value[args[0]],
                "PipHPos": args[1],
                "PipVPos": args[2],
                "PipWidth": args[3],
                "PipHeight": args[4],
                "MaskSwitch": _switch_value[args[5]],
                "MaskTop": int.from_bytes(args[6:8], byteorder='big'),
                "MaskBottom": int.from_bytes(args[8:10], byteorder='big'),
                "MaskLeft": int.from_bytes(args[10:12], byteorder='big'),
                "MaskRight": int.from_bytes(args[12:14], byteorder='big'),
                "Stage1": args[14],
                "Stage2": args[15]
            }
        }
        return _args

    def __get_usk_layer_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_usk_layer_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_usk_layer_params(self, dev_sn):
        _cmd = 0x0096
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_usk_layer_params_callback)

    @staticmethod
    def handle_dsk_params(args): # 处理 DSK 参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))

        _video_sources = ["Color1", "Color2", "Foreground", "AUX", "Black"]
        _switch_value = ["Off", "On"]
        
        _args = {
            "function": "get_dsk_params",
            "args": {
                "VideoSource": _video_sources[args[0] if args[0] < 5 else 0],
                "ToleranceLeft": int.from_bytes(args[1:3], byteorder='big'),
                "ToleranceRight": int.from_bytes(args[3:5], byteorder='big'),
                "ToleranceInvertSwitch": _switch_value[args[5]],
                "ToleranceUnitStep": int.from_bytes(args[6:8], byteorder='big'),
                "ClipSwitch": _switch_value[args[8]],
                "ClipLeft": int.from_bytes(args[9:11], byteorder='big'),
                "ClipRight": int.from_bytes(args[11:13], byteorder='big'),
                "ClipCurveSwitch": _switch_value[args[13]],
                "ClipPGMLevel": int.from_bytes(args[14:16], byteorder='big'),
                "ClipPVWLevel": int.from_bytes(args[16:18], byteorder='big'),
                "PipSwitch": _switch_value[args[18]],
                "PipHPos": args[19],
                "PipVPos": args[20],
                "PipWidth": args[21],
                "PipHeight": args[22],
                "MaskSwitch": _switch_value[args[23]],
                "MaskTop": int.from_bytes(args[24:26], byteorder='big'),
                "MaskBottom": int.from_bytes(args[26:28], byteorder='big'),
                "MaskLeft": int.from_bytes(args[28:30], byteorder='big'),
                "MaskRight": int.from_bytes(args[30:32], byteorder='big'),
            }
        }
        return _args

    def __get_dsk_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_dsk_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_dsk_params(self, dev_sn):
        _cmd = 0x0097
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_dsk_params_callback)

    @staticmethod
    def handle_system_params(args): # 处理系统设置和网络设置参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))

        _languages = Cue01Preferences.get_languages()
        _fan_mode_value = Cue01Preferences.get_fan_modes()
        # _dhcp_value = ["Off", "On", "Auto"]
        
        _args = {
            "function": "get_system_params",
            "args": {
                "Language": _languages[args[0]],
                # "FanMode": _fan_mode_value[args[1]],
                "FanSpeed": args[1],
                # "DHCP": _dhcp_value[args[2]],
                "DHCP": False if args[2] == 0 else True,
                "IPAddress": "{}.{}.{}.{}".format(args[3], args[4], args[5], args[6]),
                "SubnetMask": "{}.{}.{}.{}".format(args[7], args[8], args[9], args[10]),
                "Gateway": "{}.{}.{}.{}".format(args[11], args[12], args[13], args[14])
            }
        }
        return _args

    def __get_system_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_system_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_system_params(self, dev_sn):
        _cmd = 0x0098
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_system_params_callback)

    @staticmethod
    def handle_audio_params(args): # 处理音频参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_audio_params",
            "args": {
                "PGM": args[0],
                "Volumn": args[1]
            }
        }
        return _args

    def __get_audio_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_audio_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_audio_params(self, dev_sn):
        _cmd = 0x009A
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_audio_params_callback)

    @staticmethod
    def handle_user_params(args): # 处理用户参数
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_user_params",
            "args": {
                "CurrentUser": args[0],
                "UserValidList": ModelPreferences.byte_to_binary_list(args[1]),
                "UsernameList": [
                    args[2:18].decode("ascii").rstrip('\x00'),
                    args[18:34].decode("ascii").rstrip('\x00'),
                    args[34:50].decode("ascii").rstrip('\x00'),
                    args[50:66].decode("ascii").rstrip('\x00'),
                    args[66:82].decode("ascii").rstrip('\x00'),
                    args[82:98].decode("ascii").rstrip('\x00'),
                    args[98:114].decode("ascii").rstrip('\x00'),
                    args[114:130].decode("ascii").rstrip('\x00'),
                ]
            }
        }
        return _args

    def __get_user_params_callback(self, dev_sn, args):
        _args = Cue01Model.handle_user_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_user_params(self, dev_sn):
        _cmd = 0x0099
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_user_params_callback)

    @staticmethod
    def handle_export_config(args): # 导出配置
        logging.debug("args:{}".format(args))
        _args = {
            "function": "export_config",
            "args": {
                "ConfigData": args[0:500]
            }
        }
        return _args

# --------------------------------------------------------------- set --------------------------------------------------------------------------------

    """
    设置输出
    """
    def __set_output_interface_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_output_interface",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_output_interface(self, dev_sn, args):
        _cmd = 0x0005
        _data = []
        _valid = 0x00
        _format = 0xFF
        _color_space = 0xFF
        _range = 0xFF

        logging.debug("args:{}".format(args))

        if "Format" in args:
            _format = Cue01Preferences.get_index_by_format(args["Format"])
            # if _format != 0xFF:
            _valid |= 0x01
        
        if "ColorSpace" in args:
            _color_space = Cue01Preferences.get_index_by_color_space(args["ColorSpace"])
            if _color_space != 0xFF:
                _valid |= 0x02

        if "Range" in args:
            _range = Cue01Preferences.get_index_by_range(args["Range"])
            logging.debug("_range:{}".format(_range))
            if _range != 0xFF:
                _valid |= 0x04
        
        if _valid == 0x00:
            logging.error("没有有效数据需要设置")
            return

        if args["Index"] > 3:
            logging.error("配置的输出端口号超出范围(0~3)，Index=", args["Index"])
            return

        _data += _valid.to_bytes(1, "big")
        _data += args["Index"].to_bytes(1, "big")
        _data += _format.to_bytes(1, "big")
        _data += _color_space.to_bytes(1, "big")
        _data += _range.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_output_interface_callback)

    """
    设置色彩发生器
    """
    def __set_color_generation_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_color_generation",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_color_generation(self, dev_sn, args):
        _cmd = 0x0007
        _data = []

        logging.debug("args:{}".format(args))

        if args["ColorValid"][0] and args["ColorValid"][1]:
            # _data += [0x03, 0x00, 0x00, 0x00]
            _data += [0x00, 0x00, 0x00, 0x03]
            _data += args["Color"][0]["Red"].to_bytes(1, "big")
            _data += args["Color"][0]["Green"].to_bytes(1, "big")
            _data += args["Color"][0]["Blue"].to_bytes(1, "big")
            _data += args["Color"][1]["Red"].to_bytes(1, "big")
            _data += args["Color"][1]["Green"].to_bytes(1, "big")
            _data += args["Color"][1]["Blue"].to_bytes(1, "big")
        elif args["ColorValid"][0]:
            # _data += [0x01, 0x00, 0x00, 0x00]
            _data += [0x00, 0x00, 0x00, 0x01]
            _data += args["Color"][0]["Red"].to_bytes(1, "big")
            _data += args["Color"][0]["Green"].to_bytes(1, "big")
            _data += args["Color"][0]["Blue"].to_bytes(1, "big")
            _data += [0x00]
            _data += [0x00]
            _data += [0x00]
        elif args["ColorValid"][1]:
            # _data += [0x02, 0x00, 0x00, 0x00]
            _data += [0x00, 0x00, 0x00, 0x02]
            _data += [0x00]
            _data += [0x00]
            _data += [0x00]
            _data += args["Color"][0]["Red"].to_bytes(1, "big")
            _data += args["Color"][0]["Green"].to_bytes(1, "big")
            _data += args["Color"][0]["Blue"].to_bytes(1, "big")
        else:
            return

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_color_generation_callback)


    """
    设置Reference Input
    """
    def __set_ref_input_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_ref_input",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_reference_input(self, dev_sn, args):
        _cmd = 0x0006
        _data = []

        logging.debug("args:{}".format(args))
        
        if "ReferenceInput" not in args:
            logging.error("没有有效数据需要设置")
            return
        
        _ref_input = Cue01Preferences.get_index_by_input(args["ReferenceInput"]) 

        if _ref_input == 0xFF:
            logging.error("配置的Reference输入有误：{}".format(args["ReferenceInput"]))
            return

        _data += _ref_input.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_ref_input_callback)

    """
    设置Input Enhancement
    """
    def __set_input_enhancement_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_input_enhancement",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_input_enhancement(self, dev_sn, args):
        _cmd = 0x0010
        _data = []
        _valid = 0x0000
        _video_src = 0xFF
        _contrast = 0
        _brightness = 0
        _saturation = 0
        _hue = 0
        _lti = 0
        _cti = 0
        _color_tone = 0
        _h_anti_alias = 0
        _v_anti_alias = 0
        _h_peak_filter = 0
        _v_peak_filter = 0

        logging.debug("args:{}".format(args))

        if "VideoSource" in args:
            _video_src = args["VideoSource"]
            _valid |= 0x0001
        
        if "Contrast" in args:
            _contrast = args["Contrast"]
            _valid |= 0x0002
        
        if "Brightness" in args:
            _brightness = args["Brightness"]
            _valid |= 0x0004
        
        if "Saturation" in args:
            _saturation = args["Saturation"]
            _valid |= 0x0008
        
        if "Hue" in args:
            _hue = args["Hue"]
            _valid |= 0x0010

        if "LTI" in args:
            _lti = 1 if args["LTI"] == "On" or args["LTI"] == "ON" else 0
            logging.debug("_lti:{}".format(_lti))
            _valid |= 0x0020

        if "CTI" in args:
            _cti = 1 if args["CTI"] == "On" or args["CTI"] == "ON" else 0
            logging.debug("_cti:{}".format(_cti))
            _valid |= 0x0040

        if "ColorTone" in args:
            _color_tone = Cue01Preferences.get_index_by_color_tone(args["ColorTone"])
            logging.debug("_color_tone:{}".format(_color_tone))
            if _color_tone != 0xFF:
                _valid |= 0x0080

        if "HAntiAlias" in args:
            _h_anti_alias = args["HAntiAlias"]
            _valid |= 0x0100

        if "VAntiAlias" in args:
            _v_anti_alias = args["VAntiAlias"]
            _valid |= 0x0200

        if "HPeakFilter" in args:
            _h_peak_filter = args["HPeakFilter"]
            _valid |= 0x0400
        
        if "VPeakFilter" in args:
            _v_peak_filter = args["VPeakFilter"]
            _valid |= 0x0800
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        if _video_src > 2:
            logging.error("配置的视频源超出范围(0~2)， _video_src=", _video_src)
            return

        _data += _valid.to_bytes(4, "big")
        _data += _video_src.to_bytes(1, "big")
        _data += _contrast.to_bytes(1, "big")
        _data += _brightness.to_bytes(1, "big")
        _data += _saturation.to_bytes(1, "big")
        _data += _hue.to_bytes(1, "big")
        _data += _lti.to_bytes(1, "big")
        _data += _cti.to_bytes(1, "big")
        _data += _color_tone.to_bytes(1, "big")
        _data += _h_anti_alias.to_bytes(1, "big")
        _data += _v_anti_alias.to_bytes(1, "big")
        _data += _h_peak_filter.to_bytes(1, "big")
        _data += _v_peak_filter.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_input_enhancement_callback)
    
    """
    设置Input Noise Reduction
    """
    def __set_input_noise_reduction_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_input_noise_reduction",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_input_noise_reduction(self, dev_sn, args):
        _cmd = 0x0011
        _data = []
        _valid = 0x0000
        _video_src = 0xFF
        _nr_mode = 0x00
        _nr_motion_display = 0x00
        _bnr_mode = 0x00
        _bnr_intensity = 0x00
        _block_coordinate = 0x00
        _block_display = 0x00
        _block_threshold = 0x00

        logging.debug("args:{}".format(args))

        if "VideoSource" in args:
            _video_src = args["VideoSource"]
            _valid |= 0x0001
        
        if "NRMode" in args and "VideoSource" in args:
            _nr_mode = Cue01Preferences.get_index_by_nr_mode(args["NRMode"])
            _valid |= 0x0002
        elif "NRMode" in args:
            logging.error("只有NRMode参数，无VideoSource参数，忽略该参数")
        
        if "NRMotionDisplay" in args and "VideoSource" in args:
            _nr_motion_display = 1 if args["NRMotionDisplay"] == "On" or args["NRMotionDisplay"] == "ON" else 0
            _valid |= 0x0004
        elif "NRMotionDisplay" in args:
            logging.error("只有NRMotionDisplay参数，无VideoSource参数，忽略该参数")

        if "BNRMode" in args:
            _bnr_mode = 1 if args["BNRMode"] == "On" or args["BNRMode"] == "ON" else 0
            logging.debug("_bnr_mode:{}".format(_bnr_mode))
            _valid |= 0x0008

        if "BNRIntensity" in args:
            _bnr_intensity = Cue01Preferences.get_index_by_bnr_intensity(args["BNRIntensity"])
            logging.debug("_bnr_intensity:{}".format(_bnr_intensity))
            if _bnr_intensity != 0xFF:
                _valid |= 0x0010

        if "BlockCoordinateX" in args and "BlockCoordinateY" in args:
            _x = args["BlockCoordinateX"]
            _y = args["BlockCoordinateY"]
            _block_coordinate = (_x << 4) | _y
            _valid |= 0x0020
        elif "BlockCoordinateX" in args:
            logging.error("只有BlockCoordinateX参数，无BlockCoordinateY参数，忽略该参数")
        elif "BlockCoordinateY" in args:
            logging.error("只有BlockCoordinateY参数，无BlockCoordinateX参数，忽略该参数")

        if "BlockDisplay" in args:
            _block_display = 1 if args["BlockDisplay"] == "On" or args["BlockDisplay"] == "ON" else 0
            logging.debug("_block_display:{}".format(_block_display))
            _valid |= 0x0040

        if "BlockThreshold" in args:
            _block_threshold = args["BlockThreshold"]
            _valid |= 0x0080
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        # if _video_src > 2:
        #     logging.error("配置的视频源超出范围(0~2)， _video_src=", _video_src)
        #     return

        _data += _valid.to_bytes(4, "big")
        _data += _video_src.to_bytes(1, "big")
        _data += _nr_mode.to_bytes(1, "big")
        _data += _nr_motion_display.to_bytes(1, "big")
        _data += _bnr_mode.to_bytes(1, "big")
        _data += _bnr_intensity.to_bytes(1, "big")
        _data += _block_coordinate.to_bytes(1, "big")
        _data += _block_display.to_bytes(1, "big")
        _data += _block_threshold.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_input_noise_reduction_callback)

    """ 
    设置源参数
    """
    def __set_source_params_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))

        _args = {
            "function": "set_source_params",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_source_params(self, dev_sn, args):
        _cmd = 0x0083
        _data = []
        _valid = 0x0000
        _bg_source = 0x00
        _matte_source = 0x00
        _aux_source = 0x00

        logging.debug("args:{}".format(args))

        if "BackgroundSource" in args:
            _bg_source = Cue01Preferences.get_index_by_bg_src(args["BackgroundSource"])
            _valid |= 0x0001
        
        if "MatteSource" in args:
            _matte_source = args["MatteSource"]
            _valid |= 0x0002

        if "AuxOutput" in args:
            _aux_source = Cue01Preferences.get_index_by_aux_output(args["AuxOutput"])
            _valid |= 0x0004
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _bg_source.to_bytes(1, "big")  
        _data += _matte_source.to_bytes(1, "big")
        _data += _aux_source.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_source_params_callback)

    """
    设置音频参数
    """
    def __set_audio_params_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))

        _args = {
            "function": "set_audio_params",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_audio_params")
        self._app.async_callback(dev_sn, _args)

    def async_set_audio_params(self, dev_sn, args):
        _cmd = 0x0084
        _data = []
        _valid = 0x0000
        _pgm = 0x00
        _volumn = 0x00

        logging.debug("args:{}".format(args))

        if "PGM" in args:
            _pgm = args["PGM"]
            _valid |= 0x0001

        if "Volumn" in args:
            _volumn = args["Volumn"]
            _valid |= 0x0002
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return
        
        _data += _valid.to_bytes(4, "big")
        _data += _pgm.to_bytes(1, "big")
        _data += _volumn.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_audio_params_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_audio_params_callback
        }

        self._mc_task.do_current_task("set_audio_params", _task)

    def __set_luma_status_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """ 
        logging.debug("args:{}".format(args))

        _args = {
            "function": "set_luma_status",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_luma_status(self, dev_sn, args):
        _cmd = 0x0020
        _data = []
        _luma_status = 0x00


        logging.debug("args:{}".format(args))

        if "Status" in args:
            _luma_status = 1 if args["Status"] == "On" or args["Status"] == "ON" else 0
            logging.debug("luma status:{}".format(_luma_status))

        _data += _luma_status.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_luma_status_callback)

    """
    设置Luma Fill Source
    """
    def __set_luma_fill_src_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_luma_fill_src",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_luma_fill_src(self, dev_sn, args):
        _cmd = 0x0020
        _data = []

        logging.debug("args:{}".format(args))
        
        if "FillSource" not in args:
            logging.error("没有有效数据需要设置")
            return
        
        _fill_src = Cue01Preferences.get_index_by_luma_video_src(args["FillSource"]) 

        if _fill_src == 0xFF:
            logging.error("配置的Luma视频源有误：{}".format(args["FillSource"]))
            return

        _data += _fill_src.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_luma_fill_src_callback)

    """
    设置Luma Tolerance
    """
    def __set_luma_tolerance_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_luma_tolerance",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_luma_tolerance")
        self._app.async_callback(dev_sn, _args)

    def async_set_luma_tolerance(self, dev_sn, args):
        _cmd = 0x0021
        _data = []
        _valid = 0x0000
        _left_value = 0x00
        _right_value = 0x00
        _curve_switch = 0x00
        _invert_switch = 0x00
        _unit_step = 0x00

        logging.debug("args:{}".format(args))

        if "ToleranceLeft" in args:
            _left_value = args["ToleranceLeft"]
            _valid |= 0x0001
        
        if "ToleranceRight" in args:
            _right_value = args["ToleranceRight"]
            _valid |= 0x0002

        if "ToleranceCurve" in args:
            _curve_switch = 1 if args["ToleranceCurve"] == "On" or args["ToleranceCurve"] == "ON" else 0
            logging.debug("_curve_switch:{}".format(_curve_switch))
            _valid |= 0x0004
        
        if "ToleranceInvert" in args:
            _invert_switch = 1 if args["ToleranceInvert"] == "On" or args["ToleranceInvert"] == "ON" else 0
            logging.debug("_invert_switch:{}".format(_invert_switch))
            _valid |= 0x0008

        if "ToleranceUnitStep" in args:
            _unit_step = args["ToleranceUnitStep"]
            _valid |= 0x0010
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        # if _video_src > 2:
        #     logging.error("配置的视频源超出范围(0~2)， _video_src=", _video_src)
        #     return

        _data += _valid.to_bytes(4, "big")
        _data += _left_value.to_bytes(2, "big")
        _data += _right_value.to_bytes(2, "big")
        _data += _curve_switch.to_bytes(1, "big")
        _data += _invert_switch.to_bytes(1, "big")
        _data += _unit_step.to_bytes(2, "big")

        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_luma_tolerance_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_luma_tolerance_callback
        }

        self._mc_task.do_current_task("set_luma_tolerance", _task)

    """
    设置Luma Key Clip
    """
    def __set_luma_key_clip_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_luma_key_clip",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_luma_key_clip")
        self._app.async_callback(dev_sn, _args)

    def async_set_luma_key_clip(self, dev_sn, args):
        _cmd = 0x0022
        _data = []
        _valid = 0x0000
        _clip_switch = 0x00
        _left_value = 0x00
        _right_value = 0x00
        _curve_switch = 0x00

        logging.debug("args:{}".format(args))

        if "KeyClip" in args:
            _clip_switch = 1 if args["KeyClip"] == "On" or args["KeyClip"] == "ON" else 0
            logging.debug("_clip_switch:{}".format(_clip_switch))
            _valid |= 0x0001

        if "ClipLeft" in args:
            _left_value = args["ClipLeft"]
            _valid |= 0x0002
        
        if "ClipRight" in args:
            _right_value = args["ClipRight"]
            _valid |= 0x0004
        
        if "KeyClipCurve" in args:
            _curve_switch = 1 if args["KeyClipCurve"] == "On" or args["KeyClipCurve"] == "ON" else 0
            logging.debug("_curve_switch:{}".format(_curve_switch))
            _valid |= 0x0008
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _clip_switch.to_bytes(1, "big")
        _data += _left_value.to_bytes(2, "big")
        _data += _right_value.to_bytes(2, "big")
        _data += _curve_switch.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_luma_key_clip_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_luma_key_clip_callback
        }

        self._mc_task.do_current_task("set_luma_key_clip", _task)

    """
    Chroma Fill Source
    """
    def __set_chroma_fill_src_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_chroma_fill_src",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_chroma_fill_src(self, dev_sn, args):
        _cmd = 0x0030
        _data = []
        _valid = 0x0000
        _status = 0x00
        _keycolor = 0x00
        _fill_src = 0x00

        logging.debug("args:{}".format(args))
        
        # if "FillSource" not in args:
        #     logging.error("没有有效数据需要设置")
        #     return

        if "Status" in args:
            _status = args["Status"]
            _valid = 0x0001

        if "KeyColor" in args:
            _keycolor = Cue01Preferences.get_index_by_chroma_key_color(args["KeyColor"])
            _valid = 0x0002
        
        if "FillSource" in args:
            _fill_src = Cue01Preferences.get_index_by_chroma_video_src(args["FillSource"]) 
            _valid = 0x0004

        if _fill_src == 0xFF:
            logging.error("配置的Chroma视频源有误：{}".format(args["FillSource"]))
            # return

        _data += _valid.to_bytes(4, "big")
        _data += _status.to_bytes(1, "big")
        _data += _keycolor.to_bytes(1, "big")
        _data += _fill_src.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_chroma_fill_src_callback)

    """
    Chroma Fetch Position
    """
    def __set_chroma_fetch_position_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_chroma_fetch_position",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_chroma_fetch_position(self, dev_sn, args):
        _cmd = 0x0031
        _data = []

        logging.debug("args:{}".format(args))
        
        if "PosX" not in args or "PosY" not in args:
            logging.error("没有有效数据需要设置")
            return
        
        _pos_x = args["PosX"]
        _pos_y = args["PosY"]

        _valid = ((0 <= _pos_x <= 3824) and (0 <= _pos_y <= 2144))

        if not _valid:
            logging.error("配置的坐标有误：({}, {})".format(_pos_x, _pos_y))
            return

        _data += _pos_x.to_bytes(2, "big")
        _data += _pos_y.to_bytes(2, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_chroma_fetch_position_callback)
    
    """
    Chroma Color Key
    """
    def __set_chroma_color_key_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_chroma_color_key",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_chroma_color_key")
        self._app.async_callback(dev_sn, _args)

    def async_set_chroma_color_key(self, dev_sn, args):
        _cmd = 0x0032
        _data = []
        _valid = 0x0000
        _red = 0x00
        _green = 0x00
        _blue = 0x00
        _angle = 0x00
        _tolerance = 0x00
        _softness = 0x00

        logging.debug("args:{}".format(args))

        if "ColorKeyRed" in args:
            _red = args["ColorKeyRed"]
            if 0 <= _red <= 255:
                _valid |= 0x0001
            else:
                logging.error("Error Color Key Red: {}".format(_red))

        if "ColorKeyGreen" in args:
            _green = args["ColorKeyGreen"]
            if 0 <= _green <= 255:
                _valid |= 0x0002
            else:
                logging.error("Error Color Key Green: {}".format(_green))
        
        if "ColorKeyBlue" in args:
            _blue = args["ColorKeyBlue"]
            if 0 <= _blue <= 255:
                _valid |= 0x0004
            else:
                logging.error("Error Color Key Blue: {}".format(_blue))
        
        if "ColorKeyAngle" in args:
            _angle = args["ColorKeyAngle"]
            if 0 <= _angle <= 180:
                _valid |= 0x0008
            else:
                logging.error("Error Color Key Angle: {}".format(_angle))

        if "ColorKeyTolerance" in args:
            _tolerance = args["ColorKeyTolerance"]
            if 0 <= _tolerance <= 100:
                _valid |= 0x0010
            else:
                logging.error("Error Color Key Tolerance: {}".format(_tolerance))

        if "ColorKeySoftness" in args:
            _softness = args["ColorKeySoftness"]
            if 0 <= _softness <= 100:
                _valid |= 0x0020
            else:
                logging.error("Error Color Key Softness: {}".format(_softness))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _red.to_bytes(1, "big")
        _data += _green.to_bytes(1, "big")
        _data += _blue.to_bytes(1, "big")
        _data += _angle.to_bytes(1, "big")
        _data += _tolerance.to_bytes(1, "big")
        _data += _softness.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_chroma_color_key_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_chroma_color_key_callback
        }

        self._mc_task.do_current_task("set_chroma_color_key", _task)

    """
    Chroma Key Setting
    """
    def __set_chroma_key_setting_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_chroma_key_setting",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_chroma_key_setting(self, dev_sn, args):
        _cmd = 0x0033
        _data = []
        _valid = 0x0000
        _foreground = 0x00
        _background = 0x00
        _key_edge = 0x00

        logging.debug("args:{}".format(args))

        if "KeySettingForeground" in args:
            _foreground = args["KeySettingForeground"]
            if 0 <= _foreground <= 1000:
                _valid |= 0x0001
            else:
                logging.error("Error Key Setting Foreground: {}".format(_foreground))

        if "KeySettingBackground" in args:
            _background = args["KeySettingBackground"]
            if 0 <= _background <= 1000:
                _valid |= 0x0002
            else:
                logging.error("Error Key Setting Background: {}".format(_background))
        
        if "KeySettingKeyEdge" in args:
            _key_edge = args["KeySettingKeyEdge"]
            if 0 <= _key_edge <= 1000:
                _valid |= 0x0004
            else:
                logging.error("Error Key Setting Key Edge: {}".format(_key_edge))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _foreground.to_bytes(2, "big")
        _data += _background.to_bytes(2, "big")
        _data += _key_edge.to_bytes(2, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_chroma_key_setting_callback)

    """
    Chroma Key Clip
    """
    def __set_chroma_key_clip_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_chroma_key_clip",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_chroma_key_clip")
        self._app.async_callback(dev_sn, _args)

    def async_set_chroma_key_clip(self, dev_sn, args):
        _cmd = 0x0034
        _data = []
        _valid = 0x0000
        _clip_switch = 0x00
        _left_value = 0x00
        _right_value = 0x00
        _curve_switch = 0x00

        logging.debug("args:{}".format(args))

        if "KeyClip" in args:
            _clip_switch = 1 if args["KeyClip"] == "On" or args["KeyClip"] == "ON" else 0
            logging.debug("_clip_switch:{}".format(_clip_switch))
            _valid |= 0x0001
        
        if "KeyClipCurve" in args:
            _curve_switch = 1 if args["KeyClipCurve"] == "On" or args["KeyClipCurve"] == "ON" else 0
            logging.debug("_curve_switch:{}".format(_curve_switch))
            _valid |= 0x0002

        if "ClipLeft" in args:
            _left_value = args["ClipLeft"]
            if 0 <= _left_value <= 1000:
                _valid |= 0x0004
            else:
                logging.error("Error Key Clip Left: {}".format(_left_value))
        
        if "ClipRight" in args:
            _right_value = args["ClipRight"]
            if 0 <= _right_value <= 1000:
                _valid |= 0x0008
            else:
                logging.error("Error Key Clip Right: {}".format(_right_value))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _clip_switch.to_bytes(1, "big")
        _data += _curve_switch.to_bytes(1, "big")
        _data += _left_value.to_bytes(2, "big")
        _data += _right_value.to_bytes(2, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_chroma_key_clip_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_chroma_key_clip_callback
        }

        self._mc_task.do_current_task("set_chroma_key_clip", _task)

    """
    Chroma Spill Correction
    """
    def __set_chroma_spill_correction_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_chroma_spill_correction",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_chroma_spill_correction")
        self._app.async_callback(dev_sn, _args)

    def async_set_chroma_spill_correction(self, dev_sn, args):
        _cmd = 0x0035
        _data = []
        _valid = 0x0000
        _spill_switch = 0x00
        _spill_edge = 0x00
        _background = 0x00

        logging.debug("args:{}".format(args))

        if "SpillCorrectionSwitch" in args:
            _spill_switch = 1 if args["SpillCorrectionSwitch"] == "On" or args["SpillCorrectionSwitch"] == "ON" else 0
            logging.debug("_spill_switch:{}".format(_spill_switch))
            _valid |= 0x0001

        if "SpillEdge" in args:
            _spill_edge = args["SpillEdge"]
            if 0 <= _spill_edge <= 1000:
                _valid |= 0x0002
            else:
                logging.error("Error Spill Edge: {}".format(_spill_edge))
        
        if "SpillBackground" in args:
            _background = args["SpillBackground"]
            if 0 <= _background <= 1000:
                _valid |= 0x0004
            else:
                logging.error("Error Spill Background: {}".format(_background))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _spill_switch.to_bytes(1, "big")
        _data += _spill_edge.to_bytes(2, "big")
        _data += _background.to_bytes(2, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_chroma_spill_correction_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_chroma_spill_correction_callback
        }

        self._mc_task.do_current_task("set_chroma_spill_correction", _task)

    """
    Chroma Spill Correction2
    """
    def __set_chroma_spill_correction2_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_chroma_spill_correction2",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_chroma_spill_correction2")
        self._app.async_callback(dev_sn, _args)

    def async_set_chroma_spill_correction2(self, dev_sn, args):
        _cmd = 0x0036
        _data = []
        _valid = 0x0000
        _spill2_reset = 0x00
        _spill2_switch = 0x00
        _spill2_color = 0x00
        _spill2_value = 0x00

        logging.debug("args:{}".format(args))

        if "SpillCorrection2Reset" in args:
            _spill2_reset = 1 if args["SpillCorrection2Reset"] == "On" or args["SpillCorrection2Reset"] == "ON" else 0
            logging.debug("_spill2_reset:{}".format(_spill2_reset))
            _valid |= 0x0001

        if "SpillCorrection2Switch" in args:
            _spill2_switch = 1 if args["SpillCorrection2Switch"] == "On" or args["SpillCorrection2Switch"] == "ON" else 0
            logging.debug("_spill_switch:{}".format(_spill2_switch))
            _valid |= 0x0002

        if "Spill2Color" in args:
            _spill2_color = Cue01Preferences.get_index_by_spill_correction2_color(args["Spill2Color"]) + 1 # 因去掉off，颜色下标不变从1开始，所以发送得+1，接收得-1 

            if _spill2_color == 0xFF:
                logging.error("配置的Spill2 Color有误：{}".format(args["Spill2Color"]))
            else:
                _valid |= 0x0004

        if "Spill2Value" in args:
            _spill2_value = args["Spill2Value"]
            if 0 <= _spill2_value <= 20000:
                _valid |= 0x0008
            else:
                logging.error("Error Spill2 Value: {}".format(_spill2_value))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _spill2_reset.to_bytes(1, "big")
        _data += _spill2_switch.to_bytes(1, "big")
        _data += _spill2_color.to_bytes(1, "big")
        _data += _spill2_value.to_bytes(2, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_chroma_spill_correction2_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_chroma_spill_correction2_callback
        }

        self._mc_task.do_current_task("set_chroma_spill_correction2", _task)

    """
    Chroma Color Adjustment
    """
    def __set_chroma_color_adjustment_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_chroma_color_adjustment",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_chroma_color_adjustment")
        self._app.async_callback(dev_sn, _args)

    def async_set_chroma_color_adjustment(self, dev_sn, args):
        _cmd = 0x0037
        _data = []
        _valid = 0x0000
        _reset = 0x00
        _brightness = 0x00
        _contract = 0x00
        _saturation = 0x00
        _red = 0x00
        _green = 0x00
        _blue = 0x00

        logging.debug("args:{}".format(args))

        if "ColorAdjReset" in args:
            _reset = 1 if args["ColorAdjReset"] == "On" or args["ColorAdjReset"] == "ON" else 0
            logging.debug("_reset:{}".format(_reset))
            _valid |= 0x0001

        if "ColorAdjBrightness" in args:
            _brightness = args["ColorAdjBrightness"]
            if 0 <= _brightness <= 200:
                _valid |= 0x0002
            else:
                logging.error("Error Color Adjustment Brightness: {}".format(_brightness))
        
        if "ColorAdjContract" in args:
            _contract = args["ColorAdjContract"]
            if 0 <= _contract <= 200:
                _valid |= 0x0004
            else:
                logging.error("Error Color Adjustment Contract: {}".format(_contract))
        
        if "ColorAdjSaturation" in args:
            _saturation = args["ColorAdjSaturation"]
            if 0 <= _saturation <= 200:
                _valid |= 0x0008
            else:
                logging.error("Error Color Adjustment Saturation: {}".format(_saturation))

        if "ColorAdjRed" in args:
            _red = args["ColorAdjRed"]
            if 0 <= _red <= 200:
                _valid |= 0x0010
            else:
                logging.error("Error Color Adjustment Red: {}".format(_red))
        
        if "ColorAdjGreen" in args:
            _green = args["ColorAdjGreen"]
            if 0 <= _green <= 200:
                _valid |= 0x0020
            else:
                logging.error("Error Color Adjustment Green: {}".format(_green))
        
        if "ColorAdjBlue" in args:
            _blue = args["ColorAdjBlue"]
            if 0 <= _blue <= 200:
                _valid |= 0x0040
            else:
                logging.error("Error Color Adjustment Blue: {}".format(_blue))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _reset.to_bytes(1, "big")
        _data += _brightness.to_bytes(1, "big")
        _data += _contract.to_bytes(1, "big")
        _data += _saturation.to_bytes(1, "big")
        _data += _red.to_bytes(1, "big")
        _data += _green.to_bytes(1, "big")
        _data += _blue.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_chroma_color_adjustment_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_chroma_color_adjustment_callback
        }

        self._mc_task.do_current_task("set_chroma_color_adjustment", _task)

    """
    USK PIP
    """
    def __set_usk_pip_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_usk_pip",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_usk_pip")
        self._app.async_callback(dev_sn, _args)

    def async_set_usk_pip(self, dev_sn, args):
        _cmd = 0x0040
        _data = []
        _valid = 0x0000
        _switch = 0x00
        _pos_h = 0x00
        _pos_v = 0x00
        _width = 0x00
        _height = 0x00

        logging.debug("args:{}".format(args))

        if "UskPipSwitch" in args:
            _switch = 1 if args["UskPipSwitch"] == "On" or args["UskPipSwitch"] == "ON" else 0
            logging.debug("_switch:{}".format(_switch))
            _valid |= 0x0001

        if "UskPipPosHor" in args:
            _pos_h = args["UskPipPosHor"]
            if 0 <= _pos_h <= 100:
                _valid |= 0x0002
            else:
                logging.error("Error USK PIP Horizontal: {}".format(_pos_h))
        
        if "UskPipPosVer" in args:
            _pos_v = args["UskPipPosVer"]
            if 0 <= _pos_v <= 100:
                _valid |= 0x0004
            else:
                logging.error("Error USK PIP Vertical: {}".format(_pos_v))
        
        if "UskPipWidth" in args:
            _width = args["UskPipWidth"]
            if 0 <= _width <= 100:
                _valid |= 0x0008
            else:
                logging.error("Error USK PIP Width: {}".format(_width))

        if "UskPipHeight" in args:
            _height = args["UskPipHeight"]
            if 0 <= _height <= 100:
                _valid |= 0x0010
            else:
                logging.error("Error USK PIP Height: {}".format(_height))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _switch.to_bytes(1, "big")
        _data += _pos_h.to_bytes(1, "big")
        _data += _pos_v.to_bytes(1, "big")
        _data += _width.to_bytes(1, "big")
        _data += _height.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_usk_pip_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_usk_pip_callback
        }

        self._mc_task.do_current_task("set_usk_pip", _task)
    
    """
    USK Mask
    """
    def __set_usk_mask_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_usk_mask",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_usk_mask")
        self._app.async_callback(dev_sn, _args)

    def async_set_usk_mask(self, dev_sn, args):
        _cmd = 0x0050
        _data = []
        _valid = 0x0000
        _switch = 0x00
        _top = 0x00
        _bottom = 0x00
        _left = 0x00
        _right = 0x00

        logging.debug("args:{}".format(args))

        if "UskMaskSwitch" in args:
            _switch = 1 if args["UskMaskSwitch"] == "On" or args["UskMaskSwitch"] == "ON" else 0
            logging.debug("_switch:{}".format(_switch))
            _valid |= 0x0001

        if "UskMaskTop" in args:
            _top = args["UskMaskTop"]
            if 0 <= _top <= 1800:
                _valid |= 0x0002
            else:
                logging.error("Error USK Mask Top: {}".format(_top))
        
        if "UskMaskBottom" in args:
            _bottom = args["UskMaskBottom"]
            if 0 <= _bottom <= 1800:
                _valid |= 0x0004
            else:
                logging.error("Error USK Mask Bottom: {}".format(_bottom))
        
        if "UskMaskLeft" in args:
            _left = args["UskMaskLeft"]
            if 0 <= _left <= 3200:
                _valid |= 0x0008
            else:
                logging.error("Error USK Mask Left: {}".format(_left))

        if "UskMaskRight" in args:
            _right = args["UskMaskRight"]
            if 0 <= _right <= 3200:
                _valid |= 0x0010
            else:
                logging.error("Error USK Mask Right: {}".format(_right))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _switch.to_bytes(1, "big")
        _data += _top.to_bytes(2, "big")
        _data += _bottom.to_bytes(2, "big")
        _data += _left.to_bytes(2, "big")
        _data += _right.to_bytes(2, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_usk_mask_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_usk_mask_callback
        }

        self._mc_task.do_current_task("set_usk_mask", _task)

    """
    USK Edge Stage
    """
    def __set_usk_edge_stage_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_usk_edge_stage",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_usk_edge_stage(self, dev_sn, args):
        _cmd = 0x0060
        _data = []
        _valid = 0x0000
        _stage1 = 0x00
        _stage2 = 0x00

        _stages = ["Off", "Erode3x3", "Erode5x5", "Dilate3x3", "Dilate5x5", "Gaussian3x3", "Gaussian5x5"]

        logging.debug("args:{}".format(args))

        if "UskEdgeStage1" in args:
            try:
                _stage1 = _stages.index(args["UskEdgeStage1"])
                _valid |= 0x0001
            except ValueError:
                logging.error("Error USK Edge Stage1: {}".format(args["UskEdgeStage1"]))
                return

        if "UskEdgeStage2" in args:
            try:
                _stage2 = _stages.index(args["UskEdgeStage2"])
                _valid |= 0x0002
            except ValueError:
                logging.error("Error USK Edge Stage2: {}".format(args["UskEdgeStage2"]))
                return
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _stage1.to_bytes(1, "big")
        _data += _stage2.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_usk_edge_stage_callback)

    """
    DSK Fill Source
    """
    def __set_dsk_fill_src_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_dsk_fill_src",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_dsk_fill_src(self, dev_sn, args):
        _cmd = 0x0070
        _data = []

        logging.debug("args:{}".format(args))
        
        if "FillSource" not in args:
            logging.error("没有有效数据需要设置")
            return
        
        _fill_src = Cue01Preferences.get_index_by_dsk_video_src(args["FillSource"]) 

        if _fill_src == 0xFF:
            logging.error("配置的DSK视频源有误：{}".format(args["FillSource"]))
            return

        _data += _fill_src.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_dsk_fill_src_callback)

    """
    设置DSK Tolerance
    """
    def __set_dsk_tolerance_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_dsk_tolerance",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_dsk_tolerance")
        self._app.async_callback(dev_sn, _args)

    def async_set_dsk_tolerance(self, dev_sn, args):
        _cmd = 0x0071
        _data = []
        _valid = 0x0000
        _left_value = 0x00
        _right_value = 0x00
        _invert_switch = 0x00
        _unit_step = 0x00

        logging.debug("args:{}".format(args))

        if "ToleranceLeft" in args:
            _left_value = args["ToleranceLeft"]
            _valid |= 0x0001
        
        if "ToleranceRight" in args:
            _right_value = args["ToleranceRight"]
            _valid |= 0x0002
        
        if "ToleranceInvert" in args:
            _invert_switch = 1 if args["ToleranceInvert"] == "On" or args["ToleranceInvert"] == "ON" else 0
            logging.debug("_invert_switch:{}".format(_invert_switch))
            _valid |= 0x0004

        if "ToleranceUnitStep" in args:
            _unit_step = args["ToleranceUnitStep"]
            _valid |= 0x0008
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        # if _video_src > 2:
        #     logging.error("配置的视频源超出范围(0~2)， _video_src=", _video_src)
        #     return

        _data += _valid.to_bytes(4, "big")
        _data += _left_value.to_bytes(2, "big")
        _data += _right_value.to_bytes(2, "big")
        _data += _invert_switch.to_bytes(1, "big")
        _data += _unit_step.to_bytes(2, "big")

        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_dsk_tolerance_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_dsk_tolerance_callback
        }

        self._mc_task.do_current_task("set_dsk_tolerance", _task)

    """
    设置DSK Clip
    """
    def __set_dsk_clip_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_dsk_clip",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_dsk_clip")
        self._app.async_callback(dev_sn, _args)

    def async_set_dsk_clip(self, dev_sn, args):
        _cmd = 0x0072
        _data = []
        _valid = 0x0000
        _clip_switch = 0x00
        _left_value = 0x00
        _right_value = 0x00
        _curve_switch = 0x00
        _pgm_level = 0x00
        _pvw_level = 0x00

        logging.debug("args:{}".format(args))

        if "DSKClip" in args:
            _clip_switch = 1 if args["DSKClip"] == "On" or args["DSKClip"] == "ON" else 0
            logging.debug("_clip_switch:{}".format(_clip_switch))
            _valid |= 0x0001

        if "ClipLeft" in args:
            _left_value = args["ClipLeft"]
            if 0 <= _left_value <= 1000:
                _valid |= 0x0002
            else:
                logging.error("Error DSK Clip Left: {}".format(_left_value))
        
        if "ClipRight" in args:
            _right_value = args["ClipRight"]
            if 0 <= _right_value <= 1000:
                _valid |= 0x0004
            else:
                logging.error("Error DSK Clip Right: {}".format(_right_value))
        
        if "DSKClipCurve" in args:
            _curve_switch = 1 if args["DSKClipCurve"] == "On" or args["DSKClipCurve"] == "ON" else 0
            logging.debug("_curve_switch:{}".format(_curve_switch))
            _valid |= 0x0008

        if "DSKClipPGM" in args:
            _pgm_level = args["DSKClipPGM"]
            if 0 <= _pgm_level <= 1000:
                _valid |= 0x0010
            else:
                logging.error("Error DSK PGM Level: {}".format(_pgm_level))
        
        if "DSKClipPVW" in args:
            _pvw_level = args["DSKClipPVW"]
            if 0 <= _pvw_level <= 1000:
                _valid |= 0x0020
            else:
                logging.error("Error DSK PVW Level: {}".format(_pvw_level))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _clip_switch.to_bytes(1, "big")
        _data += _left_value.to_bytes(2, "big")
        _data += _right_value.to_bytes(2, "big")
        _data += _curve_switch.to_bytes(1, "big")
        _data += _pgm_level.to_bytes(2, "big")
        _data += _pvw_level.to_bytes(2, "big")

        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_dsk_clip_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_dsk_clip_callback
        }

        self._mc_task.do_current_task("set_dsk_clip", _task)

    """
    DSK PIP
    """
    def __set_dsk_pip_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_dsk_pip",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_dsk_pip")
        self._app.async_callback(dev_sn, _args)

    def async_set_dsk_pip(self, dev_sn, args):
        _cmd = 0x0073
        _data = []
        _valid = 0x0000
        _switch = 0x00
        _pos_h = 0x00
        _pos_v = 0x00
        _width = 0x00
        _height = 0x00

        logging.debug("args:{}".format(args))

        if "DskPipSwitch" in args:
            _switch = 1 if args["DskPipSwitch"] == "On" or args["DskPipSwitch"] == "ON" else 0
            logging.debug("_switch:{}".format(_switch))
            _valid |= 0x0001

        if "DskPipPosHor" in args:
            _pos_h = args["DskPipPosHor"]
            if 0 <= _pos_h <= 100:
                _valid |= 0x0002
            else:
                logging.error("Error DSK PIP Horizontal: {}".format(_pos_h))
        
        if "DskPipPosVer" in args:
            _pos_v = args["DskPipPosVer"]
            if 0 <= _pos_v <= 100:
                _valid |= 0x0004
            else:
                logging.error("Error DSK PIP Vertical: {}".format(_pos_v))
        
        if "DskPipWidth" in args:
            _width = args["DskPipWidth"]
            if 0 <= _width <= 100:
                _valid |= 0x0008
            else:
                logging.error("Error DSK PIP Width: {}".format(_width))

        if "DskPipHeight" in args:
            _height = args["DskPipHeight"]
            if 0 <= _height <= 100:
                _valid |= 0x0010
            else:
                logging.error("Error DSK PIP Height: {}".format(_height))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _switch.to_bytes(1, "big")
        _data += _pos_h.to_bytes(1, "big")
        _data += _pos_v.to_bytes(1, "big")
        _data += _width.to_bytes(1, "big")
        _data += _height.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_dsk_pip_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_dsk_pip_callback
        }

        self._mc_task.do_current_task("set_dsk_pip", _task)
    
    """
    DSK Mask
    """
    def __set_dsk_mask_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_dsk_mask",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_dsk_mask")
        self._app.async_callback(dev_sn, _args)

    def async_set_dsk_mask(self, dev_sn, args):
        _cmd = 0x0074
        _data = []
        _valid = 0x0000
        _switch = 0x00
        _top = 0x00
        _bottom = 0x00
        _left = 0x00
        _right = 0x00

        logging.debug("args:{}".format(args))

        if "DskMaskSwitch" in args:
            _switch = 1 if args["DskMaskSwitch"] == "On" or args["DskMaskSwitch"] == "ON" else 0
            logging.debug("_switch:{}".format(_switch))
            _valid |= 0x0001

        if "DskMaskTop" in args:
            _top = args["DskMaskTop"]
            if 0 <= _top <= 1800:
                _valid |= 0x0002
            else:
                logging.error("Error DSK Mask Top: {}".format(_top))
        
        if "DskMaskBottom" in args:
            _bottom = args["DskMaskBottom"]
            if 0 <= _bottom <= 1800:
                _valid |= 0x0004
            else:
                logging.error("Error DSK Mask Bottom: {}".format(_bottom))
        
        if "DskMaskLeft" in args:
            _left = args["DskMaskLeft"]
            if 0 <= _left <= 3200:
                _valid |= 0x0008
            else:
                logging.error("Error DSK Mask Left: {}".format(_left))

        if "DskMaskRight" in args:
            _right = args["DskMaskRight"]
            if 0 <= _right <= 3200:
                _valid |= 0x0010
            else:
                logging.error("Error DSK Mask Right: {}".format(_right))
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _switch.to_bytes(1, "big")
        _data += _top.to_bytes(2, "big")
        _data += _bottom.to_bytes(2, "big")
        _data += _left.to_bytes(2, "big")
        _data += _right.to_bytes(2, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_dsk_mask_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_dsk_mask_callback
        }

        self._mc_task.do_current_task("set_dsk_mask", _task)

    """
    System Setting
    """
    def __set_system_setting_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_system_setting",
            "args": {
                "Result": True
            }
        }

        self._mc_task.do_next_task("set_system_setting")
        self._app.async_callback(dev_sn, _args)

    def async_set_system_setting(self, dev_sn, args):
        _cmd = 0x0080
        _data = []
        _valid = 0x0000
        _language = 0x00
        _fan_speed = 0
        _reset = 0x00

        logging.debug("args:{}".format(args))

        if "Language" in args:
            _language = Cue01Preferences.get_index_by_language(args["Language"]) 

            if _language == 0xFF:
                logging.error("Error Language: {}".format(args["Language"]))
            else:
                _valid |= 0x0001

        # if "FanMode" in args:
        #     _fan_mode = Cue01Preferences.get_index_by_fan_mode(args["FanMode"]) 

            # if _fan_mode == 0xFF:
            #     logging.error("Error Fan Mode: {}".format(args["FanMode"]))
            # else:
            #     _valid |= 0x0002
        
        if "FanSpeed" in args:
            _fan_speed = args["FanSpeed"]
            if 0 <= _fan_speed <= 100:
                _valid |= 0x0002
            else:
                logging.error("Error Fan Speed: {}".format(_fan_speed))

        if "SystemReset" in args:
            _reset = 1 if args["SystemReset"] == "On" or args["SystemReset"] == "ON" else 0
            logging.debug("_reset:{}".format(_reset))
            _valid |= 0x0004
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _language.to_bytes(1, "big")
        _data += _fan_speed.to_bytes(1, "big")
        _data += _reset.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        # self._app.async_action(dev_sn, _cmd, _data, self.__set_system_setting_callback)
        _task = {
            "dev_sn": dev_sn,
            "cmd": _cmd,
            "data": _data,
            "args": args,
            "cb": self.__set_system_setting_callback
        }

        self._mc_task.do_current_task("set_system_setting", _task)

    # def __set_dhcp_status_callback(self, dev_sn, args):
    #     pass

    # def async_set_dhcp_status(self, dev_sn, args):
    #     pass

    def __set_network_setting_callback(self, dev_sn, args):
        logging.debug("args:{}".format(args))

    def async_set_network_setting(self, dev_sn, args):
        _cmd = 0x0081
        _data = []
        _valid = 0x0000
        _checked = 0x00
        _ip_address = 0x00
        _subnet_mask = 0x00
        _gateway = 0x00

        logging.debug("args:{}".format(args))

        if "checked" in args:
            # _checked = 0x01 if args["checked"] else 0x00
            _checked = 1 if args["checked"] else 0
            _valid |= 0x0001
        if "ip_address" in args:
            one = args["ip_address"][0]
            two = args["ip_address"][1]
            three = args["ip_address"][2]
            four = args["ip_address"][3]
            _ip_address = [one, two, three, four]
            _valid |= 0x0002
        if "subnet_mask" in args:
            one = args["subnet_mask"][0]
            two = args["subnet_mask"][1]
            three = args["subnet_mask"][2]
            four = args["subnet_mask"][3]
            _subnet_mask = [one, two, three, four]
            _valid |= 0x0004
        if "gateway" in args:
            one = args["gateway"][0]
            two = args["gateway"][1]
            three = args["gateway"][2]
            four = args["gateway"][3]
            _gateway = [one, two, three, four]
            _valid |= 0x0008

        _data += _valid.to_bytes(4, "big")
        _data += _checked.to_bytes(1, "big")
        _data += _ip_address
        _data += _subnet_mask
        _data += _gateway

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_network_setting_callback)

    def async_set_user_params(self, dev_sn, args):
        _cmd = 0x0082
        _data = []
        _valid = 0x0000
        _user_option = 0x00
        _user_num = 0x00
        _config_data = [0x00]*500
        _user_name_bytes = [0x00]*16

        logging.debug("args:{}".format(args))

        if "UserOption" in args:
            _user_option = args["UserOption"]
            _valid |= 0x0001

        if "UserNum" in args:
            _user_num = args["UserNum"]
            _valid |= 0x0002

        if "UserName" in args:
            _user_name = args["UserName"].encode("ascii")
            if 0 < len(_user_name) <= 16:
                _user_name_bytes = list(_user_name) + [0x00]*(16 -  len(_user_name))
                _valid |= 0x0004
            else:
                logging.error("Username is too long(should be less than 16 chars): {}".format(args["UserName"]))
        
        if "ConfigData" in args:
            _config_data = args["ConfigData"]
            _valid |= 0x0008
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _user_option.to_bytes(1, "big")
        _data += _user_num.to_bytes(1, "big")
        _data += _user_name_bytes
        _data += _config_data

        logging.debug("_data:{}".format(_data))
        if _user_option == 4: # 导入
            self._app.async_action(dev_sn, _cmd, _data, self.__set_user_import_callback)
        # elif _user_option == 5: # 导出，不做处理，直接等配置数据主动上报
        #     self._app.async_action(dev_sn, _cmd, _data, self.__set_user_export_callback)
        else: # 其他操作
            self._app.async_action(dev_sn, _cmd, _data, self.__set_user_normal_callback)

    def __set_user_import_callback(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _args = {
                    "function": "import_config",
                    "args": {
                        "Result": args[0]
                    }
        }
        self._app.async_callback(dev_sn, _args)

    def __set_user_normal_callback(self, dev_sn, args):
        logging.debug("args:{}".format(args))
        _args = {
                    "function": "normal_operation",
                    "args": {
                        "Result": True
                    }
                }
        self._app.async_callback(dev_sn, _args)

    # 处理设备主动上报
    def handle_ccp_report(self, dev_sn, cmd, args):
        # parse args here 
        # 示例args = b'\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        stacked_index = 1
        tab_index = [1]
        _args = None
        # 根据cmd在_args中填写更新的页面编号
        # if cmd == 144: # 外同步信号，输入视频图像参数增强更新0x0090
        #     stacked_index = 1
        #     tab_index = [1, 2]
        #     # 调用对应的解析函数，需要根据cmd编写新方法，处理args得到新的适用于对应页面更新的数据
        #     _args = Cue01Model.handle_ref_enhance_params(args)
        # elif cmd == 145: # 输入视频图像降噪参数更新 0x0091
        #     stacked_index = 1
        #     tab_index = [3]
        #     _args = Cue01Model.handle_noise_reduction_params(args)
        if cmd == 146: # 输出参数更新 0x0092
            stacked_index = 2
            tab_index = [0]
            _args = Cue01Model.handle_output_interface_params(args)
        elif cmd == 147: # 色彩生成器更新 0x0093
            stacked_index = 3
            tab_index = [0]
            _args = Cue01Model.handle_color_generation_params(args)
        elif cmd == 148: # Luma参数更新 0x0094
            stacked_index = 3
            tab_index = [1]
            _args = Cue01Model.handle_luma_params(args)
        elif cmd == 149: # Chroma参数更新 0x0095
            stacked_index = 3
            tab_index = [2]
            _args = Cue01Model.handle_chroma_params(args)
        elif cmd == 150: # USK pip、mask  和 Edge 参数更新 0x0096
            stacked_index = 3
            tab_index = [3]
            _args = Cue01Model.handle_usk_layer_params(args)
        elif cmd == 151: # DSK 参数更新 0x0097
            stacked_index = 3
            tab_index = [4]
            _args = Cue01Model.handle_dsk_params(args)
        elif cmd == 152: # 系统参数更新 0x0098
            stacked_index = 4
            tab_index = [0, 1]
            _args = Cue01Model.handle_system_params(args)
        elif cmd == 153: # 用户参数更新 0x0099
            stacked_index = 4
            tab_index = [2]
            _args = Cue01Model.handle_user_params(args)
        elif cmd == 154: # 音频参数更新 0x009A
            stacked_index = 1
            tab_index = [1]
            _args = Cue01Model.handle_audio_params(args)
        elif cmd == 155: # 源参数更新 0x009B
            stacked_index = 2
            tab_index = [0]
            _args = Cue01Model.handle_source_params(args)
        elif cmd == 156: # 导出配置 0x009C
            stacked_index = 4
            tab_index = [2]
            _args = Cue01Model.handle_export_config(args)
        elif cmd == 4: # 输入视频信息更新
            stacked_index = 1
            tab_index = [0]
            _args = Cue01Model.handle_input_status(args)
        else:
            logging.error(f"设备上报cmd:{cmd}不符合规定")
            return
        
        index_dict = {
            "stacked_index": stacked_index,
            "tab_index": tab_index,
        }
        _args.update(index_dict)
        # 与设备回复不一样，设备主动上报处理好数据之后，统一在此处调用 device.{}.report 注册的方法
        self._app.handle_model_report(dev_sn, _args) 
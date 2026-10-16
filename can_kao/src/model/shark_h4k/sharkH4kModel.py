import logging
from src.model.shark_h4k.sharkH4kPreferences import SharkH4kPreferences
from src.model.modelPreferences import ModelPreferences, ModelContinuousTask
import threading
import queue
from _thread import *
import traceback

class SharkH4kModel(object):
    def __init__(self, app) -> None:
        self._app = app
        self._mc_task = ModelContinuousTask(self._action_handle)

    def _action_handle(self, task):
        self._app.async_action(task["dev_sn"], task["cmd"], task["data"], task["cb"])

    def __get_version_info_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        mcu_version = "V{}.{}.{}.{}".format(args[0], args[1], args[2], args[3])
        fe_mdin640_version = "V{}.{}.{}.{}".format(args[4], args[5], args[6], args[7])
        be_mdin640_version = "V{}.{}.{}.{}".format(args[8], args[9], args[10], args[11])
        keyboard_version = "V{}.{}.{}.{}".format(args[12], args[13], args[14], args[15])
        fpga_version = "V{}.{}.{}.{}".format(args[16], args[17], args[18], args[19])
        pcb_version = "V{}.{}".format(args[20], args[21])

        _args = {
            "function": "get_version_info",
            "args": {
                "McuVersion": mcu_version,
                "FrontEndMdin640Version": fe_mdin640_version,
                "BackEndMdin640Version": be_mdin640_version,
                "KeyboardVersion": keyboard_version,
                "FPGAVersion": fpga_version,
                "PcbVersion": pcb_version
            }
        }
        self._app.async_callback(dev_sn, _args)

    # 异步获取版本信息
    def async_get_version_info(self, dev_sn):
        _cmd = 0x0001
        _data = []
        # _data_length = len(_data)

        self._app.async_action(dev_sn, _cmd, _data, self.__get_version_info_callback)

    # 获取输入状态回调
    @staticmethod
    def handle_input_status(args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        _input_formats = SharkH4kPreferences.get_input_formats()

        _color_spaces = ["YUV420", "YUV422", "YUV444", "RGB"]

        _ranges = ["Full range", "Limited range"]

        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_input_status",
            "args": {
                "ChannelNumber": 4,
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
                    },
                    {
                        "Format": "None" if args[12]==0xFE else _input_formats[args[12]],
                        "ColorSpace": "None" if args[13]==0xFE else _color_spaces[args[13]],
                        "BitDepth": 0 if args[14]==0xFE else args[14],
                        "Range": "None" if args[15]==0xFE else _ranges[args[15]]
                    }
                ]
            }
        }

        return _args
    
    def __get_input_status_callback(self, dev_sn, args):
        _args = SharkH4kModel.handle_input_status(args)
        self._app.async_callback(dev_sn, _args)

    # 异步获取输入状态
    def async_get_input_status(self, dev_sn):
        _cmd = 0x0004
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_input_status_callback)

    @staticmethod
    def handle_switch_state(args): # 处理切换台状态
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        _pgm_sources = ["HDMI1", "HDMI2", "HDMI3", "HDMI4", "Pattern1", "Pattern2"]
        _pvw_sources = ["HDMI1", "HDMI2", "HDMI3", "HDMI4", "Pattern1", "Pattern2"]
        _mv_state = ["Off", "On"]

        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "get_switch_state",
            "args": {
                "PGMSource": _pgm_sources[args[0] - 1] if 0x01 <= args[0] <= 0x04 else _pgm_sources[args[0] - 0xF0 + 4] if 0xF0 <= args[0] <= 0xF1 else "Unknow",
                "PVWSource": _pvw_sources[args[1] - 1] if 0x01 <= args[1] <= 0x04 else _pvw_sources[args[1] - 0xF0 + 4] if 0xF0 <= args[1] <= 0xF1 else "Unknow",
                "MVState": _mv_state[args[2]] if args[2] <= 0x01 else "Unknow",
            }
        }
        return _args

    def __get_switch_state_callback(self, dev_sn, args):
        _args = SharkH4kModel.handle_switch_state(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_switch_state(self, dev_sn):
        _cmd = 0x000A
        _data = []

        self._app.async_action(dev_sn, _cmd, _data, self.__get_switch_state_callback)

# --------------------------------------------------------------- set --------------------------------------------------------------------------------

    """
    设置PGM输出
    """
    def __set_pgm_output_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_pgm_output",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_pgm_output(self, dev_sn, args):
        _cmd = 0x0005
        _data = []
        _source = 0xFF
        _valid = 0x0000

        logging.debug("args:{}".format(args))

        if "Source" in args:
            if args["Source"] == "HDMI1":
                _source = 0x01
            elif args["Source"] == "HDMI2":
                _source = 0x02
            elif args["Source"] == "HDMI3":
                _source = 0x03
            elif args["Source"] == "HDMI4":
                _source = 0x04
            elif args["Source"] == "Pattern1":
                _source = 0xF0
            elif args["Source"] == "Pattern2":
                _source = 0xF1
            else:
                logging.error("配置的PGM输出源有误：{}".format(args["Source"]))
                return
            
            _valid = 0x01  # 有效的源
        else:
            logging.error("PGM输出源未配置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _source.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_pgm_output_callback)

    """
    设置PVW输出
    """
    def __set_pvw_output_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_pvw_output",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_pvw_output(self, dev_sn, args):
        _cmd = 0x0006
        _data = []
        _source = 0xFF
        _valid = 0x0000

        logging.debug("args:{}".format(args))

        if "Source" in args:
            if args["Source"] == "HDMI1":
                _source = 0x01
            elif args["Source"] == "HDMI2":
                _source = 0x02
            elif args["Source"] == "HDMI3":
                _source = 0x03
            elif args["Source"] == "HDMI4":
                _source = 0x04
            elif args["Source"] == "Pattern1":
                _source = 0xF0
            elif args["Source"] == "Pattern2":
                _source = 0xF1
            else:
                logging.error("配置的PVW输出源有误：{}".format(args["Source"]))
                return
            
            _valid = 0x01  # 有效的源
        else:
            logging.error("PGM输出源未配置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _source.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_pvw_output_callback)

    """
    设置MV输出开关
    """
    def __set_mv_state_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_mv_state",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_mv_state(self, dev_sn, args):
        _cmd = 0x0007
        _data = []
        _state = 0xFF
        _valid = 0x0000

        logging.debug("args:{}".format(args))

        if "State" in args:
            if args["State"] == "Off":
                _state = 0x00
            elif args["State"] == "On":
                _state = 0x01
            else:
                logging.error("配置的MV开关有误：{}".format(args["State"]))
                return
            
            _valid = 0x01  # 有效的源
        else:
            logging.error("MV开关未配置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _state.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_mv_state_callback)

    """
    设置MV输出开关
    """
    def __set_clock_phase_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_clock_phase",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_clock_phase(self, dev_sn, args):
        _cmd = 0x0008
        _data = []
        _phase = 0xFF
        _valid = 0x0000

        logging.debug("args:{}".format(args))

        if "ClockPhase" in args:
            if args["ClockPhase"] in [0, 1, 2, 3, 4, 5, 6, 7]:
                _phase = args["ClockPhase"]
            else:
                logging.error("配置的时钟相位有误：{}".format(args["ClockPhase"]))
                return
            
            _valid = 0x01  # 有效的源
        else:
            logging.error("时钟相位未配置")
            return

        _data += _valid.to_bytes(4, "big")
        _data += _phase.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_clock_phase_callback)

    """
    设置PGM/PVW切换
    """
    def __set_pgm_pvw_cut_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_pgm_pvw_cut",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_pgm_pvw_cut(self, dev_sn, args):
        _cmd = 0x0009
        _data = []

        logging.debug("_data:{}".format(_data))
        self._app.async_action(dev_sn, _cmd, _data, self.__set_pgm_pvw_cut_callback)
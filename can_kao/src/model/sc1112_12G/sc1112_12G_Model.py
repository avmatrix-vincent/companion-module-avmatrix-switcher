import logging
from src.model.modelPreferences import ModelPreferences

class SC1112_12G_Model(object):
    def __init__(self, app) -> None:
        self._app = app

    def __get_version_info_callback(self, dev_sn, args):
        _args = ModelPreferences.sc_handle_version_info(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_version_info(self, dev_sn):
        _cmd = 0x16
        _data = []

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_version_info_callback)

    @staticmethod
    def handle_setting_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_setting_params",
            "args": {
                "HDMIColorRange": args[15],
                "ColorSpace": args[17],
                "ColoriMetry": args[19]
            }
        }
        return _args

    def __get_setting_params_callback(self, dev_sn, args):
        _args = SC1112_12G_Model.handle_setting_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_setting_params(self, dev_sn):
        _cmd = 0xB0
        _data = []

        dev_id = ModelPreferences._usb_model_list.index("SC1112-12G") + 1
        _data += dev_id.to_bytes(1, "little")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_setting_params_callback)

    ''' 设置参数回调 '''
    def __set_setting_params_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        result = True
        if args[8] != 0:
            result = False
            logging.error("设置SC7030参数失败！")
        
        _args = {
            "function": "set_setting_params",
            "args": {
                "Result": result
            }
        }
        self._app.async_callback(dev_sn, _args)
    
    def async_set_setting_params(self, dev_sn, args):
        _cmd = 0xB1
        _data = []
        _valid = 0x00
        _output_resolution = 0x00
        _video_inputMode = 0x00
        _audio_input = 0x00
        _aspect_ratio = 0x00
        _hdmi_color_range = 0x00
        _sdi_mode = 0x00
        _color_space = 0x00
        _colorimetry = 0x00

        logging.debug("args:{}".format(args))

        if "HDMIColorRange" in args:
            _hdmi_color_range = args["HDMIColorRange"]
            _valid |= 0x10
        if "ColorSpace" in args:
            _color_space = args["ColorSpace"]
            _valid |= 0x40
        if "HDMIoutColorimetry" in args:
            _colorimetry = args["HDMIoutColorimetry"]
            _valid |= 1<<7
        if _valid == 0x00:
            logging.error("没有有效数据需要设置")
            return

        dev_id = ModelPreferences._usb_model_list.index("SC1112-12G") + 1
        _data += dev_id.to_bytes(1, "little")
        _data += _valid.to_bytes(2, "little")
        _data += _output_resolution.to_bytes(1, "little")
        _data += _video_inputMode.to_bytes(1, "little")
        _data += _audio_input.to_bytes(1, "little")
        _data += _aspect_ratio.to_bytes(1, "little")
        _data += _hdmi_color_range.to_bytes(1, "little")
        _data += _sdi_mode.to_bytes(1, "little")
        _data += _color_space.to_bytes(1, "little")
        _data += _colorimetry.to_bytes(1, "little")

        logging.debug("_data:{}".format(_data))
        self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_setting_params_callback)
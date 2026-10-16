import logging
from src.model.modelPreferences import ModelPreferences
from src.model.sc2020_12G.sc2020_12G_Preferences import SC2020_12G_Preferences


class SC2020_12G_Model(object):
    def __init__(self, app) -> None:
        self._app = app


    def __get_version_info_callback(self, dev_sn, args):
        _args = ModelPreferences.sc_handle_version_info(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_version_info(self, dev_sn):
        _cmd = 0x16
        _data = []

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_version_info_callback)

    """
    0xB0指令
    查询设备的配置信息
    PID：7 / SC2020-12G
    """

    @staticmethod
    def handle_get_setting_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_setting_params",
            "args": {
                "SDI_SFP_Out_Src": args[11],
                "HDMI_Out_Source": args[12],
                "HDMI_Out_Range": args[13],
                "3G_SDI_Out": args[14],
                "HDMI_Out_Color": args[15],
                "SDI_SFP_Mode": args[16],
                "HDMI_In_Format": args[17],
                "SDI_SFP_In_Format": args[18],
                "HDMI_In_Range": args[19],
                "HDMI_In_Color": args[20],
                "SDI_In_Range": args[21],
                "SDI_In_Color": args[22],
                "DIP_PC_Flag": args[23],
                "Fan_Speed": args[24],
                "MCU_Temperature": int(hex(args[25])[2:] + hex(args[26])[2:], 16),   # 25 26
                "FPGA_Temperature":  int(hex(args[27])[2:] + hex(args[28])[2:], 16),  # 27 28
                "Color_Metry": args[29],
                "HDMI_IN_Color_depth": args[30],
                "HDMI_In_Colorimetry": args[31]
            }
        }
        return _args

    def __get_setting_params_callback(self, dev_sn, args):
        _args = SC2020_12G_Model.handle_get_setting_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_setting_params(self, dev_sn):
        _cmd = 0xB0
        _data = []

        dev_id = SC2020_12G_Preferences.get_pid()
        _data += dev_id.to_bytes(1, "little")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_setting_params_callback)



    '''
    0xB1
    设备配置指令
    '''
    def __set_setting_params_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        result = True
        if args[8] != 0:
            result = False
            logging.error("设置SC2020_12G参数失败！")

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
        _valid = 0x0000

        _sdi_sfp_out_src=0x00
        _hdmi_out_src=0x00
        _hdmi_out_range=0x00
        _3g_sdi_out = 0x00
        _hdmi_out_color = 0x00
        _sdi_sfp_mode = 0x00
        _color_metry = 0x00
        _fan_speed = 0x00

        logging.debug("args:{}".format(args))

        if "SDI_SFP_Out_Src" in args:
            _sdi_sfp_out_src = args["SDI_SFP_Out_Src"] # SC2020_12G_Preferences.get_index_by_sdi_sfp_out(args["SDI_SFP_Out_Src"])
            _valid |= 0x0001
        if "HDMI_Out_Source" in args:
            _hdmi_out_src = args["HDMI_Out_Source"] #SC2020_12G_Preferences.get_index_by_hdmi_out_src(args["HDMI_Out_Source"])
            _valid |= 1<<1
        if "HDMI_Out_Range" in args:
            _hdmi_out_range = SC2020_12G_Preferences.get_index_by_hdmi_out_range(args["HDMI_Out_Range"])
            _valid |= 1<<2
        if "3G_SDI_Out" in args:
            _3g_sdi_out = SC2020_12G_Preferences.get_index_by_3g_sdi_out(args["3G_SDI_Out"])
            _valid |= 1<<3
        if "HDMI_Out_Color" in args:
            _hdmi_out_color = SC2020_12G_Preferences.get_index_by_hdmi_out_color(args["HDMI_Out_Color"])
            _valid |= 1<<4
        if "SDI_SFP_Mode" in args:
            _sdi_sfp_mode = SC2020_12G_Preferences.get_index_by_sdi_sfp_in_mode(args["SDI_SFP_Mode"])
            _valid |= 1<<5
        if "Color_Metry" in args:
            _color_metry = SC2020_12G_Preferences.get_index_by_color_metry(args["Color_Metry"])
            _valid |= 1<<6
        if "Fan_Speed" in args:
            _fan_speed = SC2020_12G_Preferences.get_index_by_fan_speed(args["Fan_Speed"])
            _valid |= 1<<7
        if _valid == 0x00:
            logging.error("没有有效数据需要设置")
            return


        dev_id = SC2020_12G_Preferences.get_pid()
        _data += dev_id.to_bytes(1, "little")
        _data += _valid.to_bytes(2, "little")
        _data += _sdi_sfp_out_src.to_bytes(1, "little")
        _data += _hdmi_out_src.to_bytes(1, "little")
        _data += _hdmi_out_range.to_bytes(1, "little")
        _data += _3g_sdi_out.to_bytes(1, "little")
        _data += _hdmi_out_color.to_bytes(1, "little")
        _data += _sdi_sfp_mode.to_bytes(1, "little")
        _data += _color_metry.to_bytes(1, "little")
        _data += _fan_speed.to_bytes(1, "little")


        logging.debug("_data:{}".format(_data))
        self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_setting_params_callback)
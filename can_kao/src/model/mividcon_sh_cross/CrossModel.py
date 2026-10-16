import logging
from src.model.modelPreferences import ModelPreferences
from src.model.mividcon_sh_cross.CrossPreferences import CrossPreferences

class CrossModel(object):
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
    输出设置: 0xB0指令
    """
    def __set_output_params_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_output_params",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_output_params(self, dev_sn, args):
        _cmd = 0xB0
        _data = []
        _pid = CrossPreferences.get_pid()
        _valid = 0x0000
        _sdi_sfp_in = 0x00  # 新增
        _hdmi_out_src = 0x00
        _sdi_ourt_src = 0x00
        _scaler_src = 0x00
        _pattern = 0x00
        _sdi_out_mode = 0x00

        logging.debug("args:{}".format(args))

        if "HDMIOutSource" in args:
            _hdmi_out_src = CrossPreferences.get_index_by_output_source(args["HDMIOutSource"])

            if _hdmi_out_src == 0xFF:
                logging.error("Error HDMI Out Source: {}".format(args["HDMIOutSource"]))
            else:
                _valid |= 0x0001

        if "SDIOutSource" in args:
            _sdi_ourt_src = CrossPreferences.get_index_by_output_source(args["SDIOutSource"])
            if _sdi_ourt_src == 0xFF:
                logging.error("Error SDI Out Source: {}".format(args["SDIOutSource"]))
            else:
                _valid |= 1 << 1  # 将第2位（从0开始计数）置为1

        if "ScalerSource" in args:
            _scaler_src = CrossPreferences.get_index_by_scaler_source(args["ScalerSource"])
            if _scaler_src == 0xFF:
                logging.error("Error Scaler Source: {}".format(args["ScalerSource"]))
            else:
                _valid |= 1 << 2  # 将第3位（从0开始计数）置为1

        if "SDISFPIn" in args:
            _sdi_sfp_in = CrossPreferences.get_index_by_sdi_sfp(args["SDISFPIn"])
            # 等协议文档
            if _sdi_sfp_in == 0xFF:
                logging.error("Error SDI SFP In: {}".format(args["SDISFPIn"]))
            else:
                _valid |= 1 << 3  # 将第4位（从0开始计数）置为1

        # if "Pattern" in args:
        #     _pattern = CrossPreferences.get_index_by_pattern(args["Pattern"])
        #     if _pattern == 0xFF:
        #         logging.error("Error Pattern: {}".format(args["Pattern"]))
        #     else:
        #         _valid |= 0x0008

        # if "SDIOutMode" in args:
        #     _sdi_out_mode = CrossPreferences.get_index_by_sdi_out_mode(args["SDIOutMode"])
        #     if _sdi_out_mode == 0xFF:
        #         logging.error("Error SDI Out 1&2 Mode: {}".format(args["SDIOutMode"]))
        #     else:
        #         _valid |= 0x0010

        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _pid.to_bytes(1, "big")
        _data += _valid.to_bytes(2, "big")
        _data += _hdmi_out_src.to_bytes(1, "big")
        _data += _sdi_ourt_src.to_bytes(1, "big")
        _data += _scaler_src.to_bytes(1, "big")
        _data += _sdi_sfp_in.to_bytes(1, "big")
        # _data += _pattern.to_bytes(1, "big")
        # _data += _sdi_out_mode.to_bytes(1, "big")

        logging.debug("_data:{}".format(_data))
        self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_output_params_callback)
    
    """
    视频格式设置: 0xB1指令
    """
    def __set_video_format_params_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_video_format_params",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_video_format_params(self, dev_sn, args):
        _cmd = 0xB1
        _data = []
        _pid = CrossPreferences.get_pid()
        _valid = 0x0000
        _output_format = 0x00
        _hdmi_color_space = 0x00
        _sdi_out_level_mode = 0x00
        _sd2sd_aspect = 0x00
        _is_psf = 0x00
        _sdi_image_flip = 0x00
        _hdmi_image_flip = 0x00
        _sd2hd=0x00
        _hd2sd = 0x00
        _hd2hd = 0x00
        _dl = 0x00
        _ptn = 0x00
        _tgp_op = 0x00

        logging.debug("args:{}".format(args))

        if "OutputFormat" in args:
            _output_format = CrossPreferences.get_index_by_output_format(args["OutputFormat"]) 

            if _output_format == 0xFF:
                logging.error("Error Output Format: {}".format(args["OutputFormat"]))
            else:
                _valid |= 0x0001
        
        if "HDMIColorSpace" in args:
            _hdmi_color_space = CrossPreferences.get_index_by_color_space(args["HDMIColorSpace"])
            if _hdmi_color_space == 0xFF:
                logging.error("Error HDMI Color Space: {}".format(args["HDMIColorSpace"]))
            else:
                _valid |= 0x0002

        if "SDIOutLevelMode" in args:
            _sdi_out_level_mode = CrossPreferences.get_index_by_sdi_out_level_mode(args["SDIOutLevelMode"])
            if _sdi_out_level_mode == 0xFF:
                logging.error("Error 3G-SDI Out Level Mode: {}".format(args["SDIOutLevelMode"]))
            else:
                _valid |= 0x0004
                #logging.error("ssss:"+_sdi_out_level_mode)
        
        if "SD2SDAspect" in args:
            _sd2sd_aspect = CrossPreferences.get_index_by_sd2sd_aspect(args["SD2SDAspect"])
            if _sd2sd_aspect == 0xFF:
                logging.error("Error SD2SD Aspect: {}".format(args["SD2SDAspect"]))
            else:
                _valid |= 0x0008
        
        if "IsPsf" in args:
            _is_psf = 0x01 if args["IsPsf"] is True else 0x00
            _valid |= 0x0010
        
        if "SDIImageFlip" in args:
            _sdi_image_flip = CrossPreferences.get_index_by_image_flip_mode(args["SDIImageFlip"])
            if _sdi_image_flip == 0xFF:
                logging.error("Error SDI Image Flip: {}".format(args["SDIImageFlip"]))
            else:
                _valid |= 0x0020
        
        if "HDMIImageFlip" in args:
            _hdmi_image_flip = CrossPreferences.get_index_by_image_flip_mode(args["HDMIImageFlip"])
            if _hdmi_image_flip == 0xFF:
                logging.error("Error HDMI Image Flip: {}".format(args["HDMIImageFlip"]))
            else:
                _valid |= 0x0040

        if "SD2HDAspect" in args:
            _sd2hd = CrossPreferences.get_index_by_sd2hd_aspect(args["SD2HDAspect"])
            if _sd2hd == 0xFF:
                logging.error("Error SD2HDAspect: {}".format(args["SD2HDAspect"]))
            else:
                _valid |= 1<<7
        if "HD2SDAspect" in args:
            _hd2sd = CrossPreferences.get_index_by_hd2sd_aspect(args["HD2SDAspect"])
            if _hd2sd == 0xFF:
                logging.error("Error HD2SDAspect: {}".format(args["HD2SDAspect"]))
            else:
                _valid |= 1<<8
        if "HD2HDAspect" in args:
            _hd2hd = CrossPreferences.get_index_by_hd2hd_aspect(args["HD2HDAspect"])
            if _hd2hd == 0xFF:
                logging.error("Error HD2HDAspect: {}".format(args["HD2HDAspect"]))
            else:
                _valid |= 1<<9

        if "Deinterlace" in args:
            _dl = CrossPreferences.get_index_by_deinterlaces(args["Deinterlace"])
            if _dl == 0xFF:
                logging.error("Error Deinterlace: {}".format(args["Deinterlace"]))
            else:
                _valid |= 1<<10

        if "Pattern" in args:
            _ptn = CrossPreferences.get_index_by_pattens(args["Pattern"])
            if _ptn == 0xFF:
                logging.error("Error Pattern: {}".format(args["Pattern"]))
            else:
                _valid |= 1<<11

        if "TGP" in args:
            _tgp_op = CrossPreferences.get_index_by_tpg_op(args["TGP"])
            if _tgp_op == 0xFF:
                logging.error("Error TGP OP: {}".format(args["TGP"]))
            else:
                _valid |= 1<<12

        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _pid.to_bytes(1, "big")
        _data += _valid.to_bytes(2, "big")
        _data += _output_format.to_bytes(1, "big")
        _data += _hdmi_color_space.to_bytes(1, "big")
        _data += _sdi_out_level_mode.to_bytes(1, "big")
        _data += _sd2sd_aspect.to_bytes(1, "big")
        _data += _is_psf.to_bytes(1, "big")
        _data += _sdi_image_flip.to_bytes(1, "big")
        _data += _hdmi_image_flip.to_bytes(1, "big")
        _data += _sd2hd.to_bytes(1, "big")
        _data += _hd2sd.to_bytes(1, "big")
        _data += _hd2hd.to_bytes(1, "big")
        _data += _dl.to_bytes(1, "big")
        _data += _ptn.to_bytes(1, "big")
        _data += _tgp_op.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_video_format_params_callback)
    
    """
    音频设置: 0xB2指令
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
        self._app.async_callback(dev_sn, _args)

    def async_set_audio_params(self, dev_sn, args):
        _cmd = 0xB2
        _data = []
        _pid = CrossPreferences.get_pid()
        _valid = 0x0000
        _hdmi_out_ch_1_2 = 0x00
        _hdmi_out_ch_3_4 = 0x00
        _hdmi_out_ch_5_6 = 0x00
        _hdmi_out_ch_7_8 = 0x00
        _sdi_out_ch_1_2 = 0x00
        _sdi_out_ch_3_4 = 0x00
        _sdi_out_ch_5_6 = 0x00
        _sdi_out_ch_7_8 = 0x00
        _sdi_out_ch_9_10 = 0x00
        _sdi_out_ch_11_12 = 0x00
        _sdi_out_ch_13_14 = 0x00
        _sdi_out_ch_15_16 = 0x00
        _analog_out = 0x00
        _tpg_audio = 0x00

        logging.debug("args:{}".format(args))

        if "HDMIOutChannel_1_2" in args:
            if args["flag"]:
                _hdmi_out_ch_1_2 = CrossPreferences.get_index_by_hdmi_out_audio_channel(args["HDMIOutChannel_1_2"])
            else:
                _hdmi_out_ch_1_2 = CrossPreferences.get_index_by_hdmi_out_audio_channel_sdi(args["HDMIOutChannel_1_2"])
            if _hdmi_out_ch_1_2 == 0xFF:
                logging.error("Error HDMI Out Channel 1&2: {}".format(args["HDMIOutChannel_1_2"]))
            else:
                _valid |= 0x0001
        
        if "HDMIOutChannel_3_4" in args:
            if args["flag"]:
                _hdmi_out_ch_3_4 = CrossPreferences.get_index_by_hdmi_out_audio_channel(args["HDMIOutChannel_3_4"])
            else:
                _hdmi_out_ch_3_4 = CrossPreferences.get_index_by_hdmi_out_audio_channel_sdi(args["HDMIOutChannel_3_4"])
            if _hdmi_out_ch_3_4 == 0xFF:
                logging.error("Error HDMI Out Channel 3&4: {}".format(args["HDMIOutChannel_3_4"]))
            else:
                _valid |= 0x0002
        
        if "HDMIOutChannel_5_6" in args:
            if args["flag"]:
                _hdmi_out_ch_5_6 = CrossPreferences.get_index_by_hdmi_out_audio_channel(args["HDMIOutChannel_5_6"])
            else:
                _hdmi_out_ch_5_6 = CrossPreferences.get_index_by_hdmi_out_audio_channel_sdi(args["HDMIOutChannel_5_6"])
            if _hdmi_out_ch_5_6 == 0xFF:
                logging.error("Error HDMI Out Channel 5&6: {}".format(args["HDMIOutChannel_5_6"]))
            else:
                _valid |= 0x0004
        
        if "HDMIOutChannel_7_8" in args:
            if args["flag"]:
                _hdmi_out_ch_7_8 = CrossPreferences.get_index_by_hdmi_out_audio_channel(args["HDMIOutChannel_7_8"])
            else:
                _hdmi_out_ch_7_8 = CrossPreferences.get_index_by_hdmi_out_audio_channel_sdi(args["HDMIOutChannel_7_8"])
            if _hdmi_out_ch_7_8 == 0xFF:
                logging.error("Error HDMI Out Channel 7&8: {}".format(args["HDMIOutChannel_7_8"]))
            else:
                _valid |= 0x0008
        
        if "SDIOutChannel_1_2" in args:
            if args["flag"]:
                _sdi_out_ch_1_2 = CrossPreferences.get_index_by_sdi_out_audio_channel(args["SDIOutChannel_1_2"])
            else:
                _sdi_out_ch_1_2 = CrossPreferences.get_index_by_sdi_out_audio_channel_sdi(args["SDIOutChannel_1_2"])
            if _sdi_out_ch_1_2 == 0xFF:
                logging.error("Error SDI Out Channel 1&2: {}".format(args["SDIOutChannel_1_2"]))
            else:
                _valid |= 0x0010
        
        if "SDIOutChannel_3_4" in args:
            if args["flag"]:
                _sdi_out_ch_3_4 = CrossPreferences.get_index_by_sdi_out_audio_channel(args["SDIOutChannel_3_4"])
            else:
                _sdi_out_ch_3_4 = CrossPreferences.get_index_by_sdi_out_audio_channel_sdi(args["SDIOutChannel_3_4"])
            if _sdi_out_ch_3_4 == 0xFF:
                logging.error("Error SDI Out Channel 3&4: {}".format(args["SDIOutChannel_3_4"]))
            else:
                _valid |= 0x0020

        if "SDIOutChannel_5_6" in args:
            if args["flag"]:
                _sdi_out_ch_5_6 = CrossPreferences.get_index_by_sdi_out_audio_channel(args["SDIOutChannel_5_6"])
            else:
                _sdi_out_ch_5_6 = CrossPreferences.get_index_by_sdi_out_audio_channel_sdi(args["SDIOutChannel_5_6"])
            if _sdi_out_ch_5_6 == 0xFF:
                logging.error("Error SDI Out Channel 5&6: {}".format(args["SDIOutChannel_5_6"]))
            else:
                _valid |= 0x0040

        if "SDIOutChannel_7_8" in args:
            if args["flag"]:
                _sdi_out_ch_7_8 = CrossPreferences.get_index_by_sdi_out_audio_channel(args["SDIOutChannel_7_8"])
            else:
                _sdi_out_ch_7_8 = CrossPreferences.get_index_by_sdi_out_audio_channel_sdi(args["SDIOutChannel_7_8"])
            if _sdi_out_ch_7_8 == 0xFF:
                logging.error("Error SDI Out Channel 7&8: {}".format(args["SDIOutChannel_7_8"]))
            else:
                _valid |= 0x0080

        if "SDIOutChannel_9_10" in args:
            if args["flag"]:
                _sdi_out_ch_9_10 = CrossPreferences.get_index_by_sdi_out_audio_channel(args["SDIOutChannel_9_10"])
            else:
                _sdi_out_ch_9_10 = CrossPreferences.get_index_by_sdi_out_audio_channel_sdi(args["SDIOutChannel_9_10"])
            if _sdi_out_ch_9_10 == 0xFF:
                logging.error("Error SDI Out Channel 9&10: {}".format(args["SDIOutChannel_9_10"]))
            else:
                _valid |= 0x0100

        if "SDIOutChannel_11_12" in args:
            if args["flag"]:
                _sdi_out_ch_11_12 = CrossPreferences.get_index_by_sdi_out_audio_channel(args["SDIOutChannel_11_12"])
            else:
                _sdi_out_ch_11_12 = CrossPreferences.get_index_by_sdi_out_audio_channel_sdi(args["SDIOutChannel_11_12"])
            if _sdi_out_ch_11_12 == 0xFF:
                logging.error("Error SDI Out Channel 11&12: {}".format(args["SDIOutChannel_11_12"]))
            else:
                _valid |= 0x0200
        
        if "SDIOutChannel_13_14" in args:
            if args["flag"]:
                _sdi_out_ch_13_14 = CrossPreferences.get_index_by_sdi_out_audio_channel(args["SDIOutChannel_13_14"])
            else:
                _sdi_out_ch_13_14 = CrossPreferences.get_index_by_sdi_out_audio_channel_sdi(args["SDIOutChannel_13_14"])
            if _sdi_out_ch_13_14 == 0xFF:
                logging.error("Error SDI Out Channel 13&14: {}".format(args["SDIOutChannel_13_14"]))
            else:
                _valid |= 0x0400

        if "SDIOutChannel_15_16" in args:
            _sdi_out_ch_15_16 = CrossPreferences.get_index_by_sdi_out_audio_channel(args["SDIOutChannel_15_16"])
            if args["flag"]:
                _sdi_out_ch_15_16 = CrossPreferences.get_index_by_sdi_out_audio_channel(args["SDIOutChannel_15_16"])
            else:
                _sdi_out_ch_15_16 = CrossPreferences.get_index_by_sdi_out_audio_channel_sdi(args["SDIOutChannel_15_16"])
            if _sdi_out_ch_15_16 == 0xFF:
                logging.error("Error SDI Out Channel 15&16: {}".format(args["SDIOutChannel_15_16"]))
            else:
                _valid |= 0x0800

        if "AnalogAudio" in args:
            _analog_out = CrossPreferences.get_index_by_analog_audio_out(args["AnalogAudio"])

            if _analog_out == 0xFF:
                logging.error("Error Analog_audio_out: {}".format(args["AnalogAudio"]))
            else:
                print(_valid)
                _valid |= 1<<12

        if "TPGAudio" in args:
            _tpg_audio = CrossPreferences.get_index_by_tpg_audio_test(args["TPGAudio"])

            if _analog_out == 0xFF:
                logging.error("Error TPG_Audio_test: {}".format(args["TPGAudio"]))
            else:
                _valid |= 1<<13

        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _pid.to_bytes(1, "big")
        _data += _valid.to_bytes(2, "big")
        _data += _hdmi_out_ch_1_2.to_bytes(1, "big")
        _data += _hdmi_out_ch_3_4.to_bytes(1, "big")
        _data += _hdmi_out_ch_5_6.to_bytes(1, "big")
        _data += _hdmi_out_ch_7_8.to_bytes(1, "big")
        _data += _sdi_out_ch_1_2.to_bytes(1, "big")
        _data += _sdi_out_ch_3_4.to_bytes(1, "big")
        _data += _sdi_out_ch_5_6.to_bytes(1, "big")
        _data += _sdi_out_ch_7_8.to_bytes(1, "big")
        _data += _sdi_out_ch_9_10.to_bytes(1, "big")
        _data += _sdi_out_ch_11_12.to_bytes(1, "big")
        _data += _sdi_out_ch_13_14.to_bytes(1, "big")
        _data += _sdi_out_ch_15_16.to_bytes(1, "big")
        _data += _analog_out.to_bytes(1, "big")
        _data += _tpg_audio.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_audio_params_callback)

    """
    系统设置: 0xB3指令
    """
    def __set_system_params_callback(self, dev_sn, args):
        """
        解析args的数据为key-value对，并通过_ui_cbs
        """
        logging.debug("args:{}".format(args))
        
        _args = {
            "function": "set_system_params",
            "args": {
                "Result": True
            }
        }
        self._app.async_callback(dev_sn, _args)

    def async_set_system_params(self, dev_sn, args):
        _cmd = 0xB3
        _data = []
        _pid = CrossPreferences.get_pid()
        _valid = 0x0000
        _scaler_ref = 0x00
        _no_signal_indicator = 0x00
        _lcd_off_time = 0x00
        _back_to_status_time = 0x00
        _language = 0x00
        _factory_reset = 0x00

        logging.debug("args:{}".format(args))

        if "ScalerRef" in args:
            _scaler_ref = CrossPreferences.get_index_by_scaler_ref(args["ScalerRef"]) 

            if _scaler_ref == 0xFF:
                logging.error("Error Scaler Ref: {}".format(args["ScalerRef"]))
            else:
                _valid |= 0x0001
        
        if "NoSignalIndicator" in args:
            _no_signal_indicator = CrossPreferences.get_index_by_no_signal_indicator(args["NoSignalIndicator"])
            if _no_signal_indicator == 0xFF:
                logging.error("Error No Signal Indicator: {}".format(args["NoSignalIndicator"]))
            else:
                _valid |= 0x0002

        if "LCDOffTime" in args:
            _lcd_off_time = CrossPreferences.get_index_by_lcd_off_time(args["LCDOffTime"])
            if _lcd_off_time == 0xFF:
                logging.error("Error LCD Off Time: {}".format(args["LCDOffTime"]))
            else:
                _valid |= 0x0004
        
        if "BackToStatusTime" in args:
            _back_to_status_time = CrossPreferences.get_index_by_back_to_status_time(args["BackToStatusTime"])
            if _back_to_status_time == 0xFF:
                logging.error("Error Back To Status Time: {}".format(args["BackToStatusTime"]))
            else:
                _valid |= 0x0008
        
        if "Language" in args:
            _language = args["Language"] #CrossPreferences.get_index_by_language(args["Language"])
            if _language == 0xFF:
                logging.error("Error Language: {}".format(args["Language"]))
            else:
                _valid |= 0x0010
        
        if "FactoryReset" in args:
            _factory_reset = 0x01 if args["FactoryReset"] is True else 0x00
            _valid |= 0x0020
        
        if _valid == 0x0000:
            logging.error("没有有效数据需要设置")
            return

        _data += _pid.to_bytes(1, "big")
        _data += _valid.to_bytes(2, "big")
        _data += _scaler_ref.to_bytes(1, "big")
        _data += _no_signal_indicator.to_bytes(1, "big")
        _data += _lcd_off_time.to_bytes(1, "big")
        _data += _back_to_status_time.to_bytes(1, "big")
        _data += _language.to_bytes(1, "big")
        _data += _factory_reset.to_bytes(1, "big")
        
        logging.debug("_data:{}".format(_data))
        self._app.async_action_usb(dev_sn, _cmd, _data, self.__set_system_params_callback)

    """
    0xB8指令
    设备的输入信息查询及上报
    PID编号:
    SC2040: 5
    MIVIDCON_Cross: 6
    """
    @staticmethod
    def handle_get_input_video_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_input_video_params",
            "args": {
                "SDI":{
                    "format": args[11],
                    "formatString": f"{CrossPreferences.get_input_format_by_index(args[11])}", 
                },
                "HDMI": {
                    "format": args[12],
                    "formatString": f"{CrossPreferences.get_input_format_by_index(args[12])}", 
                }
            }
        }
        return _args

    def __get_input_video_params_callback(self, dev_sn, args):
        _args = CrossModel.handle_get_input_video_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_input_video_params(self, dev_sn):
        _cmd = 0xB8
        _data = []
        _pid = CrossPreferences.get_pid()

        _data += _pid.to_bytes(1, "big")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_input_video_params_callback)

    """
    0xB9指令
    设备的输出设置参数查询及上报
    PID编号:
    SC2040: 5
    MIVIDCON_Cross: 6
    """
    @staticmethod
    def handle_get_output_video_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_output_video_params",
            "args": {
                "HDMIOut":{
                    "source": args[11],
                    "sourceString": f"{CrossPreferences.get_output_source_by_index(args[11])}", 
                },
                "SDIOut": {
                    "source": args[12],
                    "sourceString": f"{CrossPreferences.get_output_source_by_index(args[12])}", 
                },
                "Scaler": {
                    "source": args[13],
                    "sourceString": f"{CrossPreferences.get_scaler_source_by_index(args[13])}", 
                },
                "Sdi_Sfp": {
                    "source": args[14],
                    "sourceString": f"{CrossPreferences.get_sdi_sfp_by_index(args[14])}",
                }
                # "Pattern": {
                #     "source": args[14],
                #     "sourceString": f"{CrossPreferences.get_pattern_by_index(args[14])}",
                # },
                # "SDIOut_1_2": {
                #     "mode": args[15],
                #     "modeString": f"{CrossPreferences.get_sdi_out_mode_by_index(args[15])}",
                # }
            }
        }
        return _args

    def __get_output_video_params_callback(self, dev_sn, args):
        _args = CrossModel.handle_get_output_video_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_output_video_params(self, dev_sn):
        _cmd = 0xB9
        _data = []
        _pid = CrossPreferences.get_pid()

        _data += _pid.to_bytes(1, "big")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_output_video_params_callback)

    """
    0xBA指令
    设备的视频格式参数查询及上报
    PID编号:
    SC2040: 5
    MIVIDCON_Cross: 6
    """
    @staticmethod
    def handle_get_output_video_format_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_output_video_format_params",
            "args": {
                "Output":{
                    "format": args[11],
                    "formatString": f"{CrossPreferences.get_output_format_by_index(args[11])}", 
                },
                "HDMI": {
                    "colorSpace": args[12],
                    "colorSpaceString": f"{CrossPreferences.get_color_space_by_index(args[12])}", 
                },
                "3G-SDIOut": {
                    "levelMode": args[13],
                    "levelModeString": f"{CrossPreferences.get_sdi_out_level_mode_by_index(args[13])}", 
                },
                "SD2SD ASPECT": {
                    "aspect": args[14],
                    "aspectString": f"{CrossPreferences.get_sd2sd_aspect_by_index(args[14])}", 
                },
                "1080i=1080psf": {
                    "isPsf": True if args[15] == 1 else False,
                },
                "SDIImage": {
                    "flipMode": args[16],
                    "flipModeString": f"{CrossPreferences.get_image_flip_mode_by_index(args[16])}", 
                },
                "HDMIImage": {
                    "flipMode": args[17],
                    "flipModeString": f"{CrossPreferences.get_image_flip_mode_by_index(args[17])}",
                },
                "SD2HD ASPECT": {
                    "aspect": args[18],
                    "aspectString": f"{CrossPreferences.get_sd2hd_aspect_by_index(args[18])}",
                },
                "HD2SD ASPECT": {
                    "aspect": args[19],
                    "aspectString": f"{CrossPreferences.get_hd2sd_aspect_by_index(args[19])}",
                },
                "HD2HD ASPECT": {
                    "aspect": args[20],
                    "aspectString": f"{CrossPreferences.get_hd2hd_aspect_by_index(args[20])}",
                },
                "Deinterlace Mode": {
                    "mode": args[21],
                    "modeString": f"{CrossPreferences.get_deinterlaces_by_index(args[21])}",
                },
                "Pattern": {
                    "aspect": args[22],
                    "aspectString": f"{CrossPreferences.get_pattens_by_index(args[22])}",
                },
                "TPG OP": {
                    "mode": args[23],
                    "modeString": f"{CrossPreferences.get_tpgop_by_index(args[23])}",
                },
            }
        }
        return _args

    def __get_output_video_format_params_callback(self, dev_sn, args):
        _args = CrossModel.handle_get_output_video_format_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_output_video_format_params(self, dev_sn):
        _cmd = 0xBA
        _data = []
        _pid = CrossPreferences.get_pid()

        _data += _pid.to_bytes(1, "big")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_output_video_format_params_callback)
    
    """
    0xBB指令
    设备的音频参数查询及上报
    PID编号:
    SC2040: 5
    MIVIDCON_Cross: 6
    """
    @staticmethod
    def handle_get_output_audio_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_output_audio_params",
            "args": {
                "HDMIOutChannel_1_2":{
                    "format": args[11],
                    "formatString": f"{CrossPreferences.get_hdmi_out_audio_channel_by_index(args[11])}", 
                },
                "HDMIOutChannel_3_4":{
                    "format": args[12],
                    "formatString": f"{CrossPreferences.get_hdmi_out_audio_channel_by_index(args[12])}", 
                },
                "HDMIOutChannel_5_6":{
                    "format": args[13],
                    "formatString": f"{CrossPreferences.get_hdmi_out_audio_channel_by_index(args[13])}", 
                },
                "HDMIOutChannel_7_8":{
                    "format": args[14],
                    "formatString": f"{CrossPreferences.get_hdmi_out_audio_channel_by_index(args[14])}", 
                },
                "SDIOutChannel_1_2":{
                    "format": args[15],
                    "formatString": f"{CrossPreferences.get_sdi_out_audio_channel_by_index(args[15])}", 
                },
                "SDIOutChannel_3_4":{
                    "format": args[16],
                    "formatString": f"{CrossPreferences.get_sdi_out_audio_channel_by_index(args[16])}", 
                },
                "SDIOutChannel_5_6":{
                    "format": args[17],
                    "formatString": f"{CrossPreferences.get_sdi_out_audio_channel_by_index(args[17])}", 
                },
                "SDIOutChannel_7_8":{
                    "format": args[18],
                    "formatString": f"{CrossPreferences.get_sdi_out_audio_channel_by_index(args[18])}", 
                },
                "SDIOutChannel_9_10":{
                    "format": args[19],
                    "formatString": f"{CrossPreferences.get_sdi_out_audio_channel_by_index(args[19])}", 
                },
                "SDIOutChannel_11_12":{
                    "format": args[20],
                    "formatString": f"{CrossPreferences.get_sdi_out_audio_channel_by_index(args[20])}", 
                },
                "SDIOutChannel_13_14":{
                    "format": args[21],
                    "formatString": f"{CrossPreferences.get_sdi_out_audio_channel_by_index(args[21])}", 
                },"SDIOutChannel_15_16":{
                    "format": args[22],
                    "formatString": f"{CrossPreferences.get_sdi_out_audio_channel_by_index(args[22])}", 
                },"Analog_audio_out":{
                    "format": args[23],
                    "formatString": f"{CrossPreferences.get_analog_audio_out_by_index(args[23])}",
                },"TPG_Audio_test":{
                    "format": args[24],
                    "formatString": f"{CrossPreferences.get_tpg_audio_test_by_index(args[24])}",
                }
            }
        }
        return _args

    def __get_output_audio_params_callback(self, dev_sn, args):
        _args = CrossModel.handle_get_output_audio_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_output_audio_params(self, dev_sn):
        _cmd = 0xBB
        _data = []
        _pid = CrossPreferences.get_pid()

        _data += _pid.to_bytes(1, "big")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_output_audio_params_callback)

    """
    0xBC指令
    设备的音频参数查询及上报
    PID编号:
    SC2040: 5
    MIVIDCON_Cross: 6
    """
    @staticmethod
    def handle_get_system_params(args):
        '''
        解析数据
        '''
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_system_params",
            "args": {
                "ScalerRef":{
                    "source": args[11],
                    "formatString": f"{CrossPreferences.get_scaler_ref_by_index(args[11])}", 
                },
                "NoSignalIndicator":{
                    "indicator": args[12],
                    "indicatorString": f"{CrossPreferences.get_no_signal_indicator_by_index(args[12])}", 
                },
                "LCDOffTime":{
                    "time": args[13],
                    "timeString": f"{CrossPreferences.get_lcd_off_time_by_index(args[13])}", 
                },
                "Back2StatusTime":{
                    "time": args[14],
                    "timeString": f"{CrossPreferences.get_back_to_status_time_by_index(args[14])}", 
                },
                "Language":{
                    "lan": args[15],
                    "lanString": f"{CrossPreferences.get_language_by_index(args[15])}", 
                },
                "LanguageList": {
                    "lan": args[16],
                    "lanString": f"{CrossPreferences.get_languages_by_index(args[16])}",
                }
            }
        }
        return _args

    def __get_system_params_callback(self, dev_sn, args):
        _args = CrossModel.handle_get_system_params(args)
        self._app.async_callback(dev_sn, _args)

    def async_get_system_params(self, dev_sn):
        _cmd = 0xBC
        _data = []
        _pid = CrossPreferences.get_pid()

        _data += _pid.to_bytes(1, "big")

        self._app.async_action_usb(dev_sn, _cmd, _data, self.__get_system_params_callback)
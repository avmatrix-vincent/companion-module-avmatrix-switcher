import importlib
import logging
import traceback
from globals import *
from src.config.menu_translations import UC1218_4K_MENU, UC1218_4K_MENU_CH
from src.avm_stack.avm_manager import singletonManager
from src.components.CustomTabWidget import CustomTabWidget
from PySide6.QtCore import Qt
from src.view.uc1218_4K.UC1218_4K_Audio import UC1218_4K_Audio
from src.view.uc1218_4K.UC1218_4K_EDID import UC1218_4K_EDID
from src.view.uc1218_4K.UC1218_4K_VideoSetting import UC1218_4K_VideoSetting
from src.view.uc1218_4K.UC1218_4K_DeviceInfor import UC1218_4K_DeviceInfor

class UC1218_4K_PagesController():
    """ 用于控制UC1218_4K内部界面显示相关的类 """

    def __init__(self, main_ui, args):
        self.main_ui = main_ui
        self.args = args
        self._model_name = args["model"]
        self._device_name = args["name"]
        self._serial_number = args["sn"]
        self._tabWidgetList = []

        self._create_tabs()
        self.add_page_to_stackedWidget()

        self._model = singletonManager.register_model(self._serial_number, self._model_name)

        singletonManager.register_notice(f"device.{self._serial_number}.cb", self._async_callback)
        singletonManager.register_notice(f"device.{self._serial_number}.report", self._handle_report)

        self.init_rtice_device()

    # 创建每个一级菜单(QListWidget选项)对应的右侧QTabWidget对象，及内部页面
    def _create_tabs(self):
        # _widget_class = [UC1218_4K_Audio, UC1218_4K_EDID, UC1218_4K_VideoSetting, UC1218_4K_DeviceInfor]
        _widget_class = [UC1218_4K_Audio, UC1218_4K_EDID, UC1218_4K_DeviceInfor]

        for i, text in enumerate(UC1218_4K_MENU):
            _tabWidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)
            _widget = _widget_class[i](_tabWidget)
            _widget.setAttribute(Qt.WA_StyledBackground, True)
            _widget.setProperty("type", "tab_inner_widget")
            _tabWidget.addTab(_widget, text)
            self._tabWidgetList.append(_tabWidget)

    def add_page_to_stackedWidget(self):
        for _tabWidget in self._tabWidgetList:
            self.main_ui.stackedWidget.addWidget(_tabWidget)

    def retranslateUi(self, index):
        # if current_language_index == 0: # 英文
        if index == 0: # 英文
            for i, text in enumerate(UC1218_4K_MENU):
                self._tabWidgetList[i].setTabText(0, text)
        # elif current_language_index == 1: # 中文
        if index == 1: #中文
            for i, text in enumerate(UC1218_4K_MENU_CH):
                self._tabWidgetList[i].setTabText(0, text)

    """
    由于该函数是在Notice中通过signal触发的槽函数中回调的，因此可以直接更新UI
    """
    def _async_callback(self, args):
        try:
            self.main_ui.stackedWidget.currentWidget().currentWidget().handle_async_callback(args)
        except Exception:
            logging.error(traceback.format_exc())

    def _handle_report(self, args):
        '''
        args = {
            "function": "get_color_generation_params",
            "stacked_index": 1,
            "tab_index": 1,
            "args": {}
        }
        '''
        # 可根据args中的页面编号 调用对应页面的 handle_async_callback
        logging.debug("report_listener args: {}".format(args))
        stacked_index = args['stacked_index']
        for tab_index in args['tab_index']:
            self.main_ui.stackedWidget.widget(stacked_index).widget(tab_index).handle_async_callback(args)

    def get_version_info(self):
        self._model.async_get_version_info(self._serial_number)

    def get_codec_volume(self):
        self._model.async_get_codec_volume(self._serial_number)

    def set_codec_volume(self, args):
        self._model.async_set_codec_volume(self._serial_number, args)
    
    def set_codec_mute(self, args):
        self._model.async_set_codec_mute(self._serial_number, args)
    
    def set_codec_mixer(self, args):
        self._model.async_set_codec_mixer(self._serial_number, args)

    def factory_reset_codec(self):
        self._model.async_factory_reset_codec(self._serial_number)
    
    def init_rtice_device(self):
        return self._model.async_init_rtice_device(self._serial_number)

    def deinit_rtice_device(self):
        return self._model.async_deinit_rtice_device(self._serial_number)

    def get_rtice_customer_version(self):
        return self._model.async_get_rtice_customer_version(self._serial_number)
    
    def get_rtice_USB_iProduct(self):
        return self._model.async_get_rtice_USB_iProduct(self._serial_number)

    def get_rtice_UVC_Name(self):
        return self._model.async_get_rtice_UVC_Name(self._serial_number)

    def get_rtice_UAC_Name(self):
        return self._model.async_get_rtice_UAC_Name(self._serial_number)

    def get_rtice_UAC_OUT2_Name(self):
        return self._model.async_get_rtice_UAC_OUT2_Name(self._serial_number)

    def get_rtice_UAC_IN_Name(self):
        return self._model.async_get_rtice_UAC_IN_Name(self._serial_number)

    def get_rtice_HdmiRX_RawTimingInfo(self):
        return self._model.async_get_rtice_HdmiRX_RawTimingInfo(self._serial_number)
    
    def get_rtice_Audio_HdmiDPRX_VolumeGain(self):
        return self._model.async_get_rtice_Audio_HdmiDPRX_VolumeGain(self._serial_number)

    def set_rtice_Audio_HdmiDPRX_VolumeGain(self, args):
        self._model.async_set_rtice_Audio_HdmiDPRX_VolumeGain(self._serial_number, args)
    
    def get_rtice_Audio_UAC_VolumeGain(self):
        return self._model.async_get_rtice_Audio_UAC_VolumeGain(self._serial_number)

    def set_rtice_Audio_UAC_VolumeGain(self, args):
        self._model.async_set_rtice_Audio_UAC_VolumeGain(self._serial_number, args)

    def get_rtice_Audio_I2SOut_MixerSource(self):
        return self._model.async_get_rtice_Audio_I2SOut_MixerSource(self._serial_number)

    def set_rtice_Audio_I2SOut_MixerSource(self, args):
        self._model.async_set_rtice_Audio_I2SOut_MixerSource(self._serial_number, args)

    def get_rtice_Audio_UACOut2_MixerSource(self):
        return self._model.async_get_rtice_Audio_UACOut2_MixerSource(self._serial_number)

    def set_rtice_Audio_UACOut2_MixerSource(self, args):
        self._model.async_set_rtice_Audio_UACOut2_MixerSource(self._serial_number, args)

    def get_rtice_EDID_mode(self):
        return self._model.async_get_rtice_EDID_mode(self._serial_number)

    def set_rtice_EDID_mode(self, args):
        self._model.async_set_rtice_EDID_mode(self._serial_number, args)

    def get_rtice_ColorRange(self, args):
        return self._model.async_get_rtice_ColorRange(self._serial_number, args)

    def set_rtice_ColorRange(self, args):
        self._model.async_set_rtice_ColorRange(self._serial_number, args)

    def get_rtice_EDID_DDC_RX_table(self):
        self._model.async_get_rtice_EDID_DDC_RX_table(self._serial_number)

    def set_rtice_EDID_DDC_RX_table(self, args):
        self._model.async_set_rtice_EDID_DDC_RX_table(self._serial_number, args)

    def get_rtice_ConfigData(self):
        return self._model.async_get_rtice_ConfigData(self._serial_number)

    def set_rtice_ConfigData(self, args):
        self._model.async_set_rtice_ConfigData(self._serial_number, args)

    def set_rtice_RestoreToDefault(self):
        self._model.async_set_rtice_RestoreToDefault(self._serial_number)

    def get_rtice_EDID_Flash_table(self, args):
        return self._model.async_get_rtice_EDID_Flash_table(self._serial_number, args)

    def set_rtice_EDID_Flash_table(self, args):
        self._model.async_set_rtice_EDID_Flash_table(self._serial_number, args)

    def get_rtice_EDID_Flash_Table_Name_List(self):
        return self._model.async_get_rtice_EDID_Flash_Table_Name_List(self._serial_number)

    def set_rtice_EDID_Flash_Table_Name_List(self, args):
        self._model.async_set_rtice_EDID_Flash_Table_Name_List(self._serial_number, args)
    
    def get_rtice_EDID_Flash_Default_table(self):
        return self._model.async_get_rtice_EDID_Flash_Default_table(self._serial_number)

    def set_rtice_EDID_Flash_Default_table(self, args):
        self._model.async_set_rtice_EDID_Flash_Default_table(self._serial_number, args)
        
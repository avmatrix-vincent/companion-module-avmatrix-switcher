import importlib
import logging
from globals import *
from src.config.menu_translations import MIVIDCON_SH_CROSS_MENU, MIVIDCON_SH_CROSS_MENU_CH
from src.avm_stack.avm_manager import singletonManager
from src.components.CustomTabWidget import CustomTabWidget
from PySide6.QtCore import Qt
from src.view.mividcon_sh_cross.crossOutput import CrossOutput
from src.view.mividcon_sh_cross.crossVideoFormat import CrossVideoFormat
from src.view.mividcon_sh_cross.crossAudio import CrossAudio
from src.view.mividcon_sh_cross.crossSystem import CrossSystem


class CrossPagesController():
    """ 用于控制Mividcon Sh Cross内部界面显示相关的类 """

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

    # 创建每个一级菜单(QListWidget选项)对应的右侧QTabWidget对象，及内部页面
    def _create_tabs(self):
        
        _widget_class = [CrossOutput, CrossVideoFormat, CrossAudio, CrossSystem]

        for i, text in enumerate(MIVIDCON_SH_CROSS_MENU):
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
            for i, text in enumerate(MIVIDCON_SH_CROSS_MENU):
                self._tabWidgetList[i].setTabText(0, text)
        # elif current_language_index == 1: # 中文
        if index == 1: #中文
            for i, text in enumerate(MIVIDCON_SH_CROSS_MENU_CH):
                self._tabWidgetList[i].setTabText(0, text)

    """
    由于该函数是在Notice中通过signal触发的槽函数中回调的，因此可以直接更新UI
    """
    def _async_callback(self, args):
        try:
            self.main_ui.stackedWidget.currentWidget().currentWidget().handle_async_callback(args)
        except Exception:
            import traceback
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

    def set_output_params(self, args):
        self._model.async_set_output_params(self._serial_number, args)

    def set_video_format_params(self, args):
        self._model.async_set_video_format_params(self._serial_number, args)

    def set_audio_params(self, args):
        self._model.async_set_audio_params(self._serial_number, args)

    def set_system_params(self, args):
        self._model.async_set_system_params(self._serial_number, args)
    
    def get_input_video_params(self):
        self._model.async_get_input_video_params(self._serial_number)

    def get_output_video_params(self):
        self._model.async_get_output_video_params(self._serial_number)
    
    def get_output_video_format_params(self):
        self._model.async_get_output_video_format_params(self._serial_number)

    def get_output_audio_params(self):
        self._model.async_get_output_audio_params(self._serial_number)

    def get_system_params(self):
        self._model.async_get_system_params(self._serial_number)

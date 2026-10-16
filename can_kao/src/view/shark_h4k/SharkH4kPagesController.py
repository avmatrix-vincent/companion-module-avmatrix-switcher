import importlib
import logging
import traceback
from globals import *
from src.config.menu_translations import SHARK_H4K_MENU, SHARK_H4K_MENU_CH
from src.avm_stack.avm_manager import singletonManager
from src.components.CustomTabWidget import CustomTabWidget
from PySide6.QtCore import Qt
from src.view.shark_h4k.Shark_H4K_Switch import Shark_H4K_Switch
from src.view.shark_h4k.Shark_H4K_InputStatus import SharkH4KInputStatusWidget

class SharkH4kPagesController():
    """ 用于控制Shark H4K内部界面显示相关的类 """

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
        _widget_class = [SharkH4KInputStatusWidget, Shark_H4K_Switch]

        for i, text in enumerate(SHARK_H4K_MENU):
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
            for i, text in enumerate(SHARK_H4K_MENU):
                self._tabWidgetList[i].setTabText(0, text)
        # elif current_language_index == 1: # 中文
        if index == 1: #中文
            for i, text in enumerate(SHARK_H4K_MENU_CH):
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

    def get_input_status(self):
        self._model.async_get_input_status(self._serial_number)

    def get_switch_state(self):
        self._model.async_get_switch_state(self._serial_number)

    def set_pgm_output(self, args):
        self._model.async_set_pgm_output(self._serial_number, args)

    def set_pvw_output(self, args):
        self._model.async_set_pvw_output(self._serial_number, args)

    def set_mv_state(self, args):
        self._model.async_set_mv_state(self._serial_number, args)

    def set_clock_phase(self, args):
        self._model.async_set_clock_phase(self._serial_number, args)

    def set_pgm_pvw_cut(self, args):
        self._model.async_set_pgm_pvw_cut(self._serial_number, args)
        
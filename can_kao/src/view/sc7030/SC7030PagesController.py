import importlib
import logging
import traceback
from globals import *
from src.config.menu_translations import SC7030_MENU, SC7030_MENU_CH
from src.avm_stack.avm_manager import singletonManager
from src.components.CustomTabWidget import CustomTabWidget
from PySide6.QtCore import Qt
from src.view.sc7030.SC7030Setting import SC7030Setting
from src.view.sc7030.SC7030Info import SC7030Info


class SC7030PagesController():
    """ 用于控制SC7030内部界面显示相关的类 """

    def __init__(self, main_ui, args):
        self.main_ui = main_ui
        self.args = args
        self._model_name = args["model"]
        self._device_name = args["name"]
        # self._type_name = args["type"]
        # self._interface_name = args["interface"]
        self._serial_number = args["sn"]
        self.setting_tabWidget = []
        self._create_tabs()
        self.add_page_to_stackedWidget()

        self._model = singletonManager.register_model(self._serial_number, self._model_name)

        singletonManager.register_notice(f"device.{self._serial_number}.cb", self._async_callback)
        singletonManager.register_notice(f"device.{self._serial_number}.report", self._handle_report)

    # 创建每个一级菜单(QListWidget选项)对应的右侧QTabWidget对象，及内部页面
    def _create_tabs(self):
        #self.setting_tabWidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)
        _widget_class = [SC7030Setting, SC7030Info]
        for i, text in enumerate(SC7030_MENU):
            _tabWidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)
            _widget = _widget_class[i](_tabWidget)
            _widget.setAttribute(Qt.WA_StyledBackground, True)
            _widget.setProperty("type", "tab_inner_widget")
            _tabWidget.addTab(_widget, text)
            self.setting_tabWidget.append(_tabWidget)

    def add_page_to_stackedWidget(self):
        for _tabWidget in self.setting_tabWidget:
            self.main_ui.stackedWidget.addWidget(_tabWidget)

    def retranslateUi(self, index):
        if not hasattr(self, "setting_tabWidget") or self.setting_tabWidget is None: return
        # if current_language_index == 0: # 英文
        if index == 0: # 英文
            for i, text in enumerate(SC7030_MENU):
                self.setting_tabWidget[i].setTabText(0, text)
        # elif current_language_index == 1: # 中文
        elif index == 1:
            for i, text in enumerate(SC7030_MENU_CH):
                self.setting_tabWidget[i].setTabText(0, text)

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

    def get_setting_params(self):
        self._model.async_get_setting_params(self._serial_number)

    def set_setting_params(self, args):
        self._model.async_set_setting_params(self._serial_number, args)
        
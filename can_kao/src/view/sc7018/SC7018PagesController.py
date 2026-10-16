import logging
import traceback
from globals import *
from src.config.menu_translations import SC7018_MENU, SC7018_MENU_CH
from src.avm_stack.avm_manager import singletonManager
from src.components.CustomTabWidget import CustomTabWidget
from PySide6.QtCore import Qt
from src.view.sc7018.SC7018Setting import SC7018Setting


class SC7018PagesController():
    """ 用于控制SC7018内部界面显示相关的类 """

    def __init__(self, main_ui, args):
        self.main_ui = main_ui
        self.args = args
        self._model_name = args["model"]
        self._device_name = args["name"]
        # self._type_name = args["type"]
        # self._interface_name = args["interface"]
        self._serial_number = args["sn"]
        self._create_tabs()
        self.add_page_to_stackedWidget()

        self._model = singletonManager.register_model(self._serial_number, self._model_name)

        singletonManager.register_notice(f"device.{self._serial_number}.cb", self._async_callback)
        # singletonManager.register_notice(f"device.{self._serial_number}.report", self._handle_report)

    # 创建每个一级菜单(QListWidget选项)对应的右侧QTabWidget对象，及内部页面
    def _create_tabs(self):
        self.setting_pages = []
        self.setting_tabWidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)

        for text in SC7018_MENU:
            self.sc2030_setting_widget = SC7018Setting(self.setting_tabWidget)
            self.sc2030_setting_widget.setAttribute(Qt.WA_StyledBackground, True)
            self.sc2030_setting_widget.setProperty("type", "tab_inner_widget")
            self.setting_tabWidget.addTab(self.sc2030_setting_widget, text)

    def add_page_to_stackedWidget(self):
        self.main_ui.stackedWidget.addWidget(self.setting_tabWidget)

    def retranslateUi(self, index):
        # if current_language_index == 0: # 英文
        if index == 0: # 英文
            for i, text in enumerate(SC7018_MENU):
                self.setting_tabWidget.setTabText(i, text)
        # elif current_language_index == 1: # 中文
        elif index == 1:
            for i, text in enumerate(SC7018_MENU_CH):
                self.setting_tabWidget.setTabText(i, text)

    """
    由于该函数是在Notice中通过signal触发的槽函数中回调的，因此可以直接更新UI
    """
    def _async_callback(self, args):
        try:
            self.main_ui.stackedWidget.currentWidget().currentWidget().handle_async_callback(args)
        except Exception:
            logging.error(traceback.format_exc())

    def get_version_info(self):
        self._model.async_get_version_info(self._serial_number)

    def get_setting_params(self):
        self._model.async_get_setting_params(self._serial_number)

    def set_setting_params(self, args):
        self._model.async_set_setting_params(self._serial_number, args)
 
      
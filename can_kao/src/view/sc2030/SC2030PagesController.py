import importlib
from globals import *
from src.config.menu_translations import SC2030_MENU, SC2030_MENU_CH
from src.avm_stack.avm_manager import singletonManager
from src.components.CustomTabWidget import CustomTabWidget
from PySide6.QtCore import Qt
from src.view.sc2030.SC2030Setting import SC2030Setting


class SC2030PagesController():
    """ 用于控制SC2030内部界面显示相关的类 """

    def __init__(self, main_ui, args):
        self.main_ui = main_ui
        self.args = args
        self._model_name = args["model"]
        self._device_name = args["name"]
        self._serial_number = args["sn"]
        self._create_tabs()
        self.add_page_to_stackedWidget()

        # self._model = singletonManager.register_model(self._serial_number, self._model_name)

        # singletonManager.register_notice(f"device.{self._serial_number}.cb", self._async_callback)
        # singletonManager.register_notice(f"device.{self._serial_number}.report", self._handle_report)

    # 创建每个一级菜单(QListWidget选项)对应的右侧QTabWidget对象，及内部页面
    def _create_tabs(self):
        self.setting_pages = []
        self.setting_tabWidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)

        for text in SC2030_MENU:
            self.sc2030_setting_widget = SC2030Setting(self.setting_tabWidget)
            self.sc2030_setting_widget.setAttribute(Qt.WA_StyledBackground, True)
            self.sc2030_setting_widget.setProperty("type", "tab_inner_widget")
            self.setting_tabWidget.addTab(self.sc2030_setting_widget, text)

    def add_page_to_stackedWidget(self):
        self.main_ui.stackedWidget.addWidget(self.setting_tabWidget)

    def retranslateUi(self, index):
        # if current_language_index == 0: # 英文
        if index == 0: # 英文
            for i, text in enumerate(SC2030_MENU):
                self.setting_tabWidget.setTabText(i, text)
        # elif current_language_index == 1: # 中文
        elif index == 1: # 中文
            for i, text in enumerate(SC2030_MENU_CH):
                self.setting_tabWidget.setTabText(i, text)
        
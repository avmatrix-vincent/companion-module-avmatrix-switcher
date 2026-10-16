import importlib
import logging
from globals import *
from src.config.menu_translations import SC2020_12G_MENU, SC2020_12G_MENU_CH
from src.avm_stack.avm_manager import singletonManager
from src.components.CustomTabWidget import CustomTabWidget
from PySide6.QtCore import Qt, QTimer
from src.view.sc2020_12G.SC2020_12G_Setting import SC2020_12G_Setting


class SC2020_12G_PagesController():
    """ 用于控制SC2020_12G内部界面显示相关的类 """
    def __init__(self, main_ui, args):
        self.main_ui = main_ui
        self.args = args
        self._model_name = args["model"]
        self._device_name = args["name"]
        self._serial_number = args["sn"]
        self._create_tabs()
        self.add_page_to_stackedWidget()

        self._model = singletonManager.register_model(self._serial_number, self._model_name)


        singletonManager.register_notice(f"device.{self._serial_number}.cb", self._async_callback)
        singletonManager.register_notice(f"device.{self._serial_number}.report", self._handle_report)

    def _create_tabs(self):
        self.setting_pages = []
        self.setting_tabWidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)

        # 确保变量已初始化
        # if not hasattr(self, 'sc2020_12G_setting_widget'):
        #     self.sc2020_12G_setting_widget = None

        for text in SC2020_12G_MENU:
            self.sc2020_12G_setting_widget = SC2020_12G_Setting(self.setting_tabWidget)
            self.sc2020_12G_setting_widget.setAttribute(Qt.WA_StyledBackground, True)
            self.sc2020_12G_setting_widget.setProperty("type", "tab_inner_widget")
            self.setting_tabWidget.addTab(self.sc2020_12G_setting_widget, text)

    def add_page_to_stackedWidget(self):
        self.main_ui.stackedWidget.addWidget(self.setting_tabWidget)

    def retranslateUi(self, index):
        # if current_language_index == 0: # 英文
        if index == 0: # 英文
            for i, text in enumerate(SC2020_12G_MENU):
                self.setting_tabWidget.setTabText(i, text)
        # elif current_language_index == 1: # 中文
        if index == 1: #中文
            for i, text in enumerate(SC2020_12G_MENU_CH):
                self.setting_tabWidget.setTabText(i, text)


    def get_sn(self):
        return self._serial_number


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

    def get_setting_params(self):
        self._model.async_get_setting_params(self._serial_number)

    def set_setting_params(self, args):
        self._model.async_set_setting_params(self._serial_number, args)


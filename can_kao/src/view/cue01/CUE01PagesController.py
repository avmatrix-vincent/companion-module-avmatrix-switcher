import __main__
import importlib
import traceback
from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QTabWidget, QApplication, QWidget, QLabel, QVBoxLayout, QTabBar
from PySide6.QtCore import Qt
from globals import *
from src.config.menu_translations import *
from src.view.cue01 import *
from src.avm_stack.avm_manager import singletonManager
from src.config.TranslationManager import TranslationManager
from src.components.CustomTabWidget import CustomTabWidget
from src.view.cue01.inputStatusWidget import *
from src.view.cue01.colorGenerationWidget import *
from src.view.cue01.lumaKeyWidget import *
from src.view.cue01.chromaKeyWidget import *
from src.view.cue01.chromaKeyWidgetMac import *
from src.view.cue01.dskWidget import *
from src.view.cue01.inputEnhancementWidget import *
from src.view.cue01.inputNoiseReductionWidget import *
from src.view.cue01.networkSettingWidget import *
from src.view.cue01.outputInterfaceWidget import *
from src.view.cue01.referenceInputWidget import *
from src.view.cue01.systemSettingWidget import *
from src.view.cue01.userSettingWidget import *
from src.view.cue01.uskWidget import *
from src.view.cue01.regReadWriteWidget import *
from src.view.cue01.audioWidget import *
from src.view.cue01.sourceWidget import *

class CUE01Controller():
    """ 用于控制CUE01内部界面显示相关的类 """

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

    # 创建每个一级菜单(QListWidget选项)对应的右侧QTabWidget对象，及内部页面
    def _create_tabs(self):
        self.input_pages = []
        self.output_pages = []
        self.keying_pages = []
        self.system_pages = []
        self.register_pages = []
        self.input_tabwidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)
        self.output_tabwidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)
        self.keying_tabwidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)
        self.system_tabwidget = CustomTabWidget(self.args, self, self.main_ui.stackedWidget)

        for key, value in MENUS.items():
            self.refresh_tab_item_list()
            if key in self.input_all_languages_list:
                self._create_widgets(self.input_tabwidget, value["widgets"], self.input_pages)
                for i, page in enumerate(self.input_pages):
                    self.input_tabwidget.addTab(page, self.input_items[i])
            elif key in self.output_all_languages_list:
                self._create_widgets(self.output_tabwidget, value["widgets"], self.output_pages)
                for i, page in enumerate(self.output_pages):
                    self.output_tabwidget.addTab(page, self.output_items[i])
            elif key in self.keying_all_languages_list:
                self._create_widgets(self.keying_tabwidget, value["widgets"], self.keying_pages)
                for i, page in enumerate(self.keying_pages):
                    self.keying_tabwidget.addTab(page, self.keying_items[i])
            elif key in self.system_all_languages_list:
                self._create_widgets(self.system_tabwidget, value["widgets"], self.system_pages)
                for i, page in enumerate(self.system_pages):
                    self.system_tabwidget.addTab(page, self.system_items[i])

    # 根据模块（py）文件（类）名创建对应的Tab选项页面
    def _create_widgets(self, parent, name_list, page_list):
        for name in name_list:
            # widget = globals()[name(parent)]
            # class_obj = getattr(__main__, name)  # 使用反射机制获取类对象
            module_path, class_name = name.rsplit(".", 1) # 分割字符串，提取模块路径和类名
            if module_path.rsplit(".", 1)[1] == "chromaKeyWidget" and sys.platform.startswith('darwin'):
                module_path = module_path.replace("chromaKeyWidget", "chromaKeyWidgetMac") # Mac读取另一个
            module = importlib.import_module(module_path) # 动态导入模块
            class_obj = getattr(module, class_name) # 获取模块中的类对象
            widget = class_obj(parent)
            try: widget.init_ui()
            except: widget.setupUi()
            widget.setAttribute(Qt.WA_StyledBackground, True)
            widget.setProperty("type", "tab_inner_widget")
            page_list.append(widget)

    def add_page_to_stackedWidget(self):
        self.main_ui.stackedWidget.addWidget(self.input_tabwidget)
        self.main_ui.stackedWidget.addWidget(self.output_tabwidget)
        self.main_ui.stackedWidget.addWidget(self.keying_tabwidget)
        self.main_ui.stackedWidget.addWidget(self.system_tabwidget)
        # self.main_ui.stackedWidget.addWidget(self.register_tabwidget)

    # 获取当前语言下的二级菜单列表
    def refresh_tab_item_list(self, index=None):
        if not index:
            index = TranslationManager().current_language_index
        # 获取一级菜单各语言列表
        self.input_all_languages_list = get_all_language_menus_by_key("INPUT")
        self.output_all_languages_list = get_all_language_menus_by_key("OUTPUT")
        self.keying_all_languages_list = get_all_language_menus_by_key("KEYING")
        self.system_all_languages_list = get_all_language_menus_by_key("SYSTEM")

        self.input_items = get_items_list(index, "INPUT")
        self.output_items = get_items_list(index, "OUTPUT")
        self.keying_items = get_items_list(index, "KEYING")
        self.system_items = get_items_list(index, "SYSTEM")

    def retranslateUi(self, index):
        self.refresh_tab_item_list(index)
        for i, _ in enumerate(self.input_pages):
            self.input_tabwidget.setTabText(i, self.input_items[i])
        for i, _ in enumerate(self.output_pages):
            self.output_tabwidget.setTabText(i, self.output_items[i])
        for i, _ in enumerate(self.keying_pages):
            self.keying_tabwidget.setTabText(i, self.keying_items[i])
        for i, _ in enumerate(self.system_pages):
            self.system_tabwidget.setTabText(i, self.system_items[i])
        
    def update_luma_or_chroma_status(self, type:str):
        # 只有Chroma和 luma标志都为启用，即开启状态只能二选一，但关闭状态可以两者同时存在
        if chroma_config.using_chroma and chroma_config.using_luma:
            if type == "chroma": # 当前是chroma需要启用
                with QSignalBlocker(self.keying_pages[1].checkBox_status): # 不发指令，只改变复选框状态
                    self.keying_pages[1].checkBox_status.setChecked(False) # 禁用Luma
                self.keying_pages[1].control_luma_status(False)
                chroma_config.using_luma = False
                logging.info("已开启Chroma Status并禁用Luma Status")
            elif type == "luma": # 当前是luma需要启用
                with QSignalBlocker(self.keying_pages[2]._fill_src_value["StatusCheckBox"]): # 不发指令，只改变复选框状态
                    self.keying_pages[2]._fill_src_value["StatusCheckBox"].setChecked(False) # 禁用Chroma
                self.keying_pages[2].control_chroma_status(False)
                chroma_config.using_chroma = False
                logging.info("已开启Luma Status并禁用Chroma Status")

    """
    由于该函数是在Notice中通过signal触发的槽函数中回调的，因此可以直接更新UI
    """
    def _async_callback(self, args):
        # widget = self.main_ui.stackedWidget.currentWidget()
        # widget.currentWidget().handle_async_callback(args)
        try:
            current_tab_widget = self.main_ui.stackedWidget.currentWidget()
            if isinstance(current_tab_widget, QTabWidget):
                current_tab_widget.currentWidget().handle_async_callback(args)
        except Exception:
            logging.error(traceback.format_exc())
            # print(traceback.format_exc())

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
        try:
            stacked_index = args['stacked_index']
            for tab_index in args['tab_index']:
                self.main_ui.stackedWidget.widget(stacked_index).widget(tab_index).handle_async_callback(args)
        except:
            logging.error(traceback.format_exc())

    def get_version(self):
        self._model.async_get_version(self._serial_number)

    def get_input_status(self):
        self._model.async_get_input_status(self._serial_number)

    def get_source_params(self):
        self._model.async_get_source_params(self._serial_number)

    def get_reference_enhancement(self):
        self._model.async_get_ref_enhance_params(self._serial_number)

    def get_noise_reduction(self):
        self._model.async_get_noise_reduction_params(self._serial_number)

    def get_output_interface(self):
        self._model.async_get_output_interface_params(self._serial_number)

    def get_audio_params(self):
        self._model.async_get_audio_params(self._serial_number)

    def get_color_generation(self):
        self._model.async_get_color_generation_params(self._serial_number)

    def get_luma(self):
        self._model.async_get_luma_params(self._serial_number)

    def get_chroma(self):
        self._model.async_get_chroma_params(self._serial_number)

    def get_usk_layer(self):
        self._model.async_get_usk_layer_params(self._serial_number)

    def get_dsk(self):
        self._model.async_get_dsk_params(self._serial_number)

    def get_system(self):
        self._model.async_get_system_params(self._serial_number)

    def get_user_params(self):
        self._model.async_get_user_params(self._serial_number)

    # ---------------------------------------------------- set --------------------------------------------------------------------------
    def set_color_generation(self, args):
        self._model.async_set_color_generation(self._serial_number, args)

    def set_output_interface(self, args):
        self._model.async_set_output_interface(self._serial_number, args)

    def set_reference_input(self, args):
        self._model.async_set_reference_input(self._serial_number, args)

    def set_input_enhancement(self, args):
        self._model.async_set_input_enhancement(self._serial_number, args)

    def set_input_noise_reduction(self, args):
        self._model.async_set_input_noise_reduction(self._serial_number, args)

    def set_source_params(self, args):
        self._model.async_set_source_params(self._serial_number, args)
    
    def set_audio_params(self, args):
        self._model.async_set_audio_params(self._serial_number, args)
    
    def set_luma_key(self, args):
        self._model.async_set_luma_status(self._serial_number, args)

    def set_luma_fill_src(self, args):
        self._model.async_set_luma_fill_src(self._serial_number, args)

    def set_luma_tolerance(self, args):
        self._model.async_set_luma_tolerance(self._serial_number, args)

    def set_luma_key_clip(self, args):
        self._model.async_set_luma_key_clip(self._serial_number, args)

    def set_chroma_fill_src(self, args):
        self._model.async_set_chroma_fill_src(self._serial_number, args)

    def set_chroma_fetch_position(self, args):
        self._model.async_set_chroma_fetch_position(self._serial_number, args)

    def set_chroma_color_key(self, args):
        self._model.async_set_chroma_color_key(self._serial_number, args)
    
    def set_chroma_key_setting(self, args):
        self._model.async_set_chroma_key_setting(self._serial_number, args)
        
    def set_chroma_key_clip(self, args):
        self._model.async_set_chroma_key_clip(self._serial_number, args)
        
    def set_chroma_spill_correction(self, args):
        self._model.async_set_chroma_spill_correction(self._serial_number, args)

    def set_chroma_spill_correction2(self, args):
        self._model.async_set_chroma_spill_correction2(self._serial_number, args)
        
    def set_chroma_color_adjustment(self, args):
        self._model.async_set_chroma_color_adjustment(self._serial_number, args)

    def set_usk_pip(self, args):
        self._model.async_set_usk_pip(self._serial_number, args)
    
    def set_usk_mask(self, args):
        self._model.async_set_usk_mask(self._serial_number, args)
    
    def set_usk_edge_stage(self, args):
        self._model.async_set_usk_edge_stage(self._serial_number, args)
    
    def set_dsk_fill_src(self, args):
        self._model.async_set_dsk_fill_src(self._serial_number, args)

    def set_dsk_tolerance(self, args):
        self._model.async_set_dsk_tolerance(self._serial_number, args)

    def set_dsk_clip(self, args):
        self._model.async_set_dsk_clip(self._serial_number, args)

    def set_dsk_pip(self, args):
        self._model.async_set_dsk_pip(self._serial_number, args)
    
    def set_dsk_mask(self, args):
        self._model.async_set_dsk_mask(self._serial_number, args)

    def set_system_setting(self, args):
        self._model.async_set_system_setting(self._serial_number, args)

    # def set_dhcp_status(self, args):
    #     self._model.async_set_dhcp_status(self._serial_number, args)

    def set_network_setting(self, args):
        self._model.async_set_network_setting(self._serial_number, args)

    def set_user_params(self, args):
        self._model.async_set_user_params(self._serial_number, args)

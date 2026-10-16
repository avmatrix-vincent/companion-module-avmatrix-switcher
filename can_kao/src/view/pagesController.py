from src.view.cue01.CUE01PagesController import CUE01Controller
from src.view.sc2030.SC2030PagesController import SC2030PagesController
from src.view.sc7030.SC7030PagesController import SC7030PagesController
from src.view.sc7018.SC7018PagesController import SC7018PagesController
from src.view.sc1221_12G.SC1221_12G_PagesController import SC1221_12G_PagesController
from src.view.sc1112_12G.SC1112_12G_PagesController import SC1112_12G_PagesController
from src.view.sd1242_4K.SD1242_4K_PagesController import SD1242_4K_PagesController
from src.view.uc1218_4K.UC1218_4K_PagesController import UC1218_4K_PagesController
from src.view.mividcon_sh_cross.CrossPagesController import CrossPagesController
from src.view.shark_h4k.SharkH4kPagesController import SharkH4kPagesController
from src.view.sc2020_12G.SC2020_12G_PagesController import SC2020_12G_PagesController
# from src.view.shark_h4k_pro.Shark_H4K_Pro_PagesController import Shark_H4K_Pro_PagesController
from src.config.menu_translations import *

class PagesController(object):
    # 菜单不应该放在这里，应该放在每个具体的pages controller中去实现
    # 暂时封装在这里，方便调用
    _controller_table = [
        {
            "models": ["CUE01", "KM32-4K"],
            "names": ["CUE01", "KM32-4K"],
            "class": CUE01Controller,
            "menus": [CUE01_MENU_1, CUE01_MENU_1_CH]
        },{
            "models": ["SC2030"],
            "names": ["SC2030"],
            "class": SC2030PagesController,
            "menus": [SC2030_MENU, SC2030_MENU_CH]
        },{
            "models": ["SC7030", "Multi to HDMI/SDI Converter"],
            "names": ["SC7030", "SC7030"],
            "class": SC7030PagesController,
            "menus": [SC7030_MENU, SC7030_MENU_CH]
        },{
            "models": ["UC7018", "Multi to USB3.0 Capture"],
            "names": ["UC7018", "UC7018"],
            "class": SC7018PagesController,
            "menus": [SC7018_MENU, SC7018_MENU_CH]
        },{
            "models": ["SC1221-12G", "4K HDMI to SDI Converter"],
            "names": ["SC1221-12G", "SC1221-12G"],
            "class": SC1221_12G_PagesController,
            "menus": [SC1112_1221_MENU, SC1112_1221_MENU_CH]
        },{
            "models": ["SC1112-12G", "4K SDI to HDMI Converter"],
            "names": ["SC1112-12G", "SC1112-12G"],
            "class": SC1112_12G_PagesController,
            "menus": [SC1112_1221_MENU, SC1112_1221_MENU_CH]
        },{
            "models": ["SD1242-4K", "4K HDMI 1-4 DA"],
            "names": ["SD1242-4K", "SD1242-4K"],
            "class": SD1242_4K_PagesController,
            "menus": [SD1242_4K_MENU, SD1242_4K_MENU_CH]
        },{
            "models": ["UC1218-4K", "USB_Capture", "4K HDMI USB3.0 Capture", "4K HDMI USB3.1 Capture"],
            "names": ["UC1218-4K", "USB Capture", "UC1218-4KS", "UC1218-4K PRO"],
            "class": UC1218_4K_PagesController,
            "menus": [UC1218_4K_MENU, UC1218_4K_MENU_CH]
        },{
            "models": ["SDI/HDMI Converter A","SC2040"], # "MIVIDCON",
            "names": ["Cross Converter", "Cross Converter"],
            "class": CrossPagesController,
            "menus": [MIVIDCON_SH_CROSS_MENU, MIVIDCON_SH_CROSS_MENU_CH]
        },{
            "models": ["SHARK-H4K"],
            "names": ["SHARK-H4K"],
            "class": SharkH4kPagesController,
            "menus": [SHARK_H4K_MENU, SHARK_H4K_MENU_CH]
        },{
            "models": ["SC2020-12G","12G SDI/HDMI Converter"],
            "names": ["SC2020-12G"],
            "class": SC2020_12G_PagesController,
            "menus": [SC2020_12G_MENU, SC2020_12G_MENU_CH]
        }
    ]

    _default_class = SD1242_4K_PagesController
    _default_menu = [DEFAULT_MENU, DEFAULT_MENU_CH]

    @staticmethod
    def is_supported_model(model):
        for _table in PagesController._controller_table:
            for _item in _table["models"]:
                if model.startswith(_item):
                    return True

        return False

    @staticmethod
    def get_name_by_model(model):
        for _table in PagesController._controller_table:
            for i in range(len(_table["models"])):
                if model.startswith(_table["models"][i]):
                    return _table["names"][i]

    @staticmethod
    def get_pages_controller_class(model):
        for _table in PagesController._controller_table:
            for _item in _table["models"]:
                if model.startswith(_item):
                    return _table["class"]

        return PagesController._default_class

    @staticmethod
    def get_menus_by_model(model):
        for _table in PagesController._controller_table:
            for _item in _table["models"]:
                if model.startswith(_item):
                    return _table["menus"]

        return PagesController._default_menu
from src.model.cue01.cue01Model import Cue01Model
from src.model.sc7030.sc7030Model import SC7030Model
from src.model.sc7018.sc7018Model import SC7018Model
from src.model.sc1221_12G.sc1221_12G_Model import SC1221_12G_Model
from src.model.sc1112_12G.sc1112_12G_Model import SC1112_12G_Model
from src.model.sd1242_4K.sd1242_4K_Model import SD1242_4K_Model
from src.model.uc1218_4K.uc1218_4K_Model import UC1218_4K_Model
from src.model.mividcon_sh_cross.CrossModel import CrossModel
from src.model.shark_h4k.sharkH4kModel import SharkH4kModel
from src.model.sc2020_12G.sc2020_12G_Model import SC2020_12G_Model

class ModelClassFactory(object):
    _model_class_table = [
        {
            "models": ["CUE01", "KM32-4K"],
            "class": Cue01Model
        },{
            "models": ["SC7030", "Multi to HDMI/SDI Converter"],
            "class": SC7030Model
        },{
            "models": ["UC7018", "Multi to USB3.0 Capture"],
            "class": SC7018Model
        },{
            "models": ["SC1221-12G", "4K HDMI to SDI Converter", "HDMI to SDI Converter"],
            "class": SC1221_12G_Model
        },{
            "models": ["SC1112-12G", "4K SDI to HDMI Converter", "SDI to HDMI Converter"],
            "class": SC1112_12G_Model
        },{
            "models": ["SD1242-4K", "4K HDMI 1-4 DA"],
            "class": SD1242_4K_Model
        },{
            "models": ["UC1218-4K", "USB_Capture", "4K HDMI USB3.0 Capture", "4K HDMI USB3.1 Capture"],
            "class": UC1218_4K_Model
        },{
            "models": ["SDI/HDMI Converter A","SC2040"], # "MIVIDCON",
            "class": CrossModel
        },{
            "models": ["SHARK-H4K", "SHARK H4K"],
            "class": SharkH4kModel
        },{
            "models": ["SC2020-12G", "12G SDI/HDMI Converter"],
            "class": SC2020_12G_Model
        }
    ]

    @staticmethod
    def get_model_class_table():
        return ModelClassFactory._model_class_table
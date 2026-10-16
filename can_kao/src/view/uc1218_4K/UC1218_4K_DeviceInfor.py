import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSignalBlocker, Qt, Signal, QCoreApplication
from src.ui.uc1218_4K.uc1218_4K_device_infor_ui import Ui_UC1218_4K_Device_Infor_Form
from src.model.modelPreferences import ModelPreferences
from src.model.uc1218_4K.uc1218_4K_Preferences import UC1218_4K_Preferences
from globals import relative_path, global_qss

class UC1218_4K_DeviceInfor(Ui_UC1218_4K_Device_Infor_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self._rtice_version = ""
        self._mcu_app_version = ""
        self._uac_name = ""
        self._uac2_name = ""

        self.factoryReset_pushButton.clicked.connect(self._on_factory_reset)

    def _on_factory_reset(self):
        confirm_box = QMessageBox()
        confirm_box.setText(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"Restore device to factory settings?", None)) 
        confirm_box.setWindowTitle(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"Factory Reset", None))
        confirm_box.addButton(QMessageBox.Yes)
        confirm_box.addButton(QMessageBox.No)
        response = confirm_box.exec()
    
        # 根据用户的选择进行操作
        if response == QMessageBox.No:
            return
        
        logging.debug("_on_factory_reset")
        # 复位2900
        self._parent.controller.set_rtice_RestoreToDefault()
        # 复位MCU的Codec
        self._parent.controller.factory_reset_codec()
        # 2900的自定义区域，需要自己复位

        _data = [0, 0] # RGB2YUV和YUV2RGB都设置为默认的Bypass模式
        _args = {
            "ConfigData": _data
        }
        self._parent.controller.set_rtice_ConfigData(_args)

    def showEvent(self, event):
        self._parent.controller.get_version_info()
        self._parent.controller.get_rtice_customer_version()
        self._parent.controller.get_rtice_USB_iProduct()
        self._parent.controller.get_rtice_UVC_Name()
        self._parent.controller.get_rtice_UAC_Name()
        self._parent.controller.get_rtice_UAC_OUT2_Name()
        self._parent.controller.get_rtice_HdmiRX_RawTimingInfo()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_rtice_customer_version":
            _args = obj["args"]
            _result = _args["Result"]
            _version = _args["Version"]
            if _result:
                self._rtice_version = "SYS " + _version
                self.versionValue_label.setText(self._rtice_version + "/" + self._mcu_app_version)
        elif obj["function"] == "get_version_info":
            args = obj["args"]
            logging.debug("Get version args:{}".format(args))
            if args["APPVersion"][3] != 0:
                _app_version = "V%d.%d.%d.%d" % (args["APPVersion"][0], args["APPVersion"][1],
                                                        args["APPVersion"][2], args["APPVersion"][3])
            else:
                _app_version = "V%d.%d.%d" % (args["APPVersion"][0], args["APPVersion"][1], args["APPVersion"][2])
            
            self._mcu_app_version = "MCU:" + _app_version
            self.versionValue_label.setText(self._rtice_version + "/" + self._mcu_app_version)
            # logging.debug(f"APPVersion:{_app_version}")
        elif obj["function"] == "get_rtice_USB_iProduct":
            _args = obj["args"]
            _result = _args["Result"]
            _iProduct = _args["iProduct"]
            if _result:
                self.productNameValue_label.setText(_iProduct)
        elif obj["function"] == "get_rtice_UVC_Name":
            _args = obj["args"]
            _result = _args["Result"]
            _UVCName = _args["UVCName"]
            if _result:
                self.uvcNameValue_label.setText(_UVCName)
        elif obj["function"] == "get_rtice_UAC_Name":
            _args = obj["args"]
            _result = _args["Result"]
            _UACName = _args["UACName"]
            if _result:
                self._uac_name = _UACName
                self.uacNameValue_label.setText(_UACName + "/" + self._uac2_name)
        elif obj["function"] == "get_rtice_UAC_OUT2_Name":
            _args = obj["args"]
            _result = _args["Result"]
            _UACOUT2Name = _args["UACOut2Name"]
            if _result:
                self._uac2_name = _UACOUT2Name
                self.uacNameValue_label.setText(self._uac_name + "/" + _UACOUT2Name)
        elif obj["function"] == "get_rtice_HdmiRX_RawTimingInfo":
            _args = obj["args"]
            _result = _args["Result"]
            if _result:
                _interlace_sign = "i" if _args["IsInterlace"] else "p"
                _colorInfor = "{} {} {}".format(_args["ColorSpace"], _args["ColorDepth"], _args["ColorRange"])
                self.inputVideo_infor_label.setText(_args["Resolution"] + _interlace_sign + _args["FrameRate"] + " " + _colorInfor)
        elif obj["function"] == "set_RestoreToDefault":
            _args = obj["args"]
            _result = _args["Result"]
            if _result:
                logging.debug(f"Restore device to default success!")
            else:
                logging.debug(f"Restore device to default error!")

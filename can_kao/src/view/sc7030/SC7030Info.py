import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QButtonGroup
from PySide6.QtCore import QSignalBlocker
from src.ui.sc7030.sc7030_info_ui import Ui_SC7030_Info_Form
from src.model.sc7030.sc7030Preferences import SC7030Preferences
from src.model.modelPreferences import ModelPreferences

class SC7030Info(Ui_SC7030_Info_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)


    def showEvent(self, event):
        self._parent.controller.get_version_info()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        try:
            if obj["function"] == "get_version_info":
                # _model = self._parent.args["args"]["model"]
                _manufacturer = self._parent.args["args"]["manufacturer"]
                _sn = self._parent.args["args"]["sn"]
                # self.label_model.setText(_model)
                self.label_manufacturer.setText(_manufacturer)
                self.label_sn.setText(_sn)

                args = obj["args"]
                logging.debug("args:{}".format(args))
                _mcu_mode = ModelPreferences.get_mcu_mode_by_index(args["MCUMode"])
                _protocol_version = "V%d.%d" % (args["ProtocolVersion"][0], args["ProtocolVersion"][1])
                _boot_version = ""
                _app_version = ""
                _fpga_version = ""
                _hardware_version = ""
                if args["BootVersion"][3] != 0:
                    _boot_version = "V%d.%d.%d.%d" % (args["BootVersion"][0], args["BootVersion"][1],
                                                            args["BootVersion"][2], args["BootVersion"][3])
                else:
                    _boot_version = "V%d.%d.%d" % (args["BootVersion"][0], args["BootVersion"][1], args["BootVersion"][2])
                if args["APPVersion"][3] != 0:
                    _app_version = "V%d.%d.%d.%d" % (args["APPVersion"][0], args["APPVersion"][1],
                                                            args["APPVersion"][2], args["APPVersion"][3])
                else:
                    _app_version = "V%d.%d.%d" % (args["APPVersion"][0], args["APPVersion"][1], args["APPVersion"][2])
                if args["FPGAVersion"][3] != 0:
                    _fpga_version = "V%d.%d.%d.%d" % (args["FPGAVersion"][0], args["FPGAVersion"][1],
                                                            args["FPGAVersion"][2], args["FPGAVersion"][3])
                else:
                    _fpga_version = "V%d.%d.%d" % (args["FPGAVersion"][0], args["FPGAVersion"][1], args["FPGAVersion"][2])
                if args["HardwareVersion"][3] != 0:
                    _hardware_version = "V%d.%d.%d.%d" % (args["HardwareVersion"][0], args["HardwareVersion"][1],
                                                            args["HardwareVersion"][2], args["HardwareVersion"][3])
                elif args["HardwareVersion"][2] != 0:
                    _hardware_version = "V%d.%d.%d" % (args["HardwareVersion"][0], args["HardwareVersion"][1], args["HardwareVersion"][2])
                else:
                    _hardware_version = "V%d.%d" % (args["HardwareVersion"][0], args["HardwareVersion"][1])
                self.label_mcu_mode.setText(_mcu_mode)
                self.label_protocol_ver.setText(_protocol_version)
                self.label_boot_version.setText(_boot_version)
                self.label_app_version.setText(_app_version)
                self.label_fpga_version.setText(_fpga_version)
                self.label_hardware_ver.setText(_hardware_version)

        except:
            import traceback
            print(traceback.format_exc())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = SC7030Info()
    window.show()
    sys.exit(app.exec())
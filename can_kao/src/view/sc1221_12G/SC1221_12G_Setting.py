import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QButtonGroup
from PySide6.QtCore import QSignalBlocker
from src.ui.sc1221_12G.SC1221_12G_setting_ui import Ui_SC1221_12G_Setting_Form
from src.model.modelPreferences import ModelPreferences

class SC1221_12G_Setting(Ui_SC1221_12G_Setting_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.button_group_sdi_output = QButtonGroup(self.widget_sdi_output)
        self.button_group_sdi_output.addButton(self.radioButton_3g_level_a)
        self.button_group_sdi_output.addButton(self.radioButton_3g_level_b)
        self.button_group_sdi_output.buttonClicked.connect(self._on_sdi_output_radioButton_clicked)
        
    def _on_sdi_output_radioButton_clicked(self):
        if self.radioButton_3g_level_a.isChecked():
            logging.debug("SDI 3G Level A is Checked")
            _args = {
                "SDIMode": 0
            }
            self._parent.controller.set_setting_params(_args)
        elif self.radioButton_3g_level_b.isChecked():
            logging.debug("SDI 3G Level B is Checked")
            _args = {
                "SDIMode": 1
            }
            self._parent.controller.set_setting_params(_args)

    def showEvent(self, event):
        self._parent.controller.get_version_info()
        self._parent.controller.get_setting_params()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
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
        if obj["function"] == "get_setting_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))
            _sdi_mode = args["SDIMode"]
            if _sdi_mode != 0xFF:
                with QSignalBlocker(self.button_group_sdi_output):
                    if _sdi_mode == 0:
                        self.radioButton_3g_level_a.setChecked(True)
                    elif _sdi_mode == 1:
                        self.radioButton_3g_level_b.setChecked(True)
        elif obj["function"] == "set_setting_params":
            args = obj["args"]
            logging.debug("Set setting params args args:{}".format(args))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = SC1221_12G_Setting()
    window.show()
    sys.exit(app.exec())
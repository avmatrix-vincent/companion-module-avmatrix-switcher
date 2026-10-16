import os, sys, logging

from PySide6 import QtCore
from PySide6.QtCore import QSignalBlocker

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QButtonGroup
from src.ui.sc7018.sc7018_setting_ui import Ui_SC7018_Settomg_Form
from src.model.sc7030.sc7030Preferences import SC7030Preferences
from src.model.modelPreferences import ModelPreferences

class SC7018Setting(Ui_SC7018_Settomg_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        _video_inputs = SC7030Preferences.get_video_inputs()
        self._m_radios = SC7030Preferences.get_out_radio()
        self._m_radios2 = SC7030Preferences.get_out_radio2()

        self.comboBox_video_input.addItems(_video_inputs)
        self.comboBox_out_radio.addItems(self._m_radios)
        self.comboBox_audio_input.addItems(SC7030Preferences.get_audio_inputs())

        self.comboBox_video_input.currentIndexChanged.connect(self._select_setting_params)
        self.comboBox_out_radio.currentIndexChanged.connect(self._select_setting_params)
        self.comboBox_audio_input.currentIndexChanged.connect(self._select_setting_params)

        self.a_index =0
        self.m_index = 0

    
    def _select_setting_params(self, index):
        sender = self.sender()

        if sender == self.comboBox_video_input:
            logging.debug("select video input input:{}".format(index))
            _args = {
                    "VideoInputMode": index
                }
            with QSignalBlocker(self.comboBox_out_radio):
                if 3 > index >= 0:
                    # self.comboBox_out_radio.clear()
                    # self.comboBox_out_radio.addItems(self._m_radios2)
                    # self.comboBox_out_radio.setCurrentIndex(self.a_index)
                    self.comboBox_out_radio.setEnabled(False)
                else:

                    self.comboBox_out_radio.setEnabled(True)
                    self.comboBox_out_radio.clear()
                    self.comboBox_out_radio.addItems(self._m_radios)
                    self.comboBox_out_radio.setCurrentIndex(self.m_index)
            self._parent.controller.set_setting_params(_args)
            #self._parent.controller.get_setting_params()

        if sender == self.comboBox_out_radio:
            if self.comboBox_video_input.currentIndex()<3:
                logging.debug("select out Radio:{}".format(index))
                _args = {
                    "AspectRatio": index
                }
                self._parent.controller.set_setting_params(_args)
            else:
                logging.debug("select out Radio:{}".format(index))
                _args = {
                        "Ms1824OutRatio": index
                    }
                self._parent.controller.set_setting_params(_args)


        if sender == self.comboBox_audio_input:
            logging.debug("select audio input:{}".format(index))
            _args = {
                    "AudioInput": index
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
            _video_inputMode = args["VideoInputMode"]
            _audio_input = args["AudioInput"]
            _aspect_ratio = args["AspectRatio"]
            _m_out_radio = args["Ms1824OutRatio"]

            self.a_index = _aspect_ratio
            self.m_index =  _m_out_radio
            if _video_inputMode != 0xFF:
                with QSignalBlocker(self.comboBox_video_input):
                    self.comboBox_video_input.setCurrentIndex(_video_inputMode)
            if _audio_input != 0xFF:
                with QSignalBlocker(self.comboBox_audio_input):
                    self.comboBox_audio_input.setCurrentIndex(_audio_input)
            if _m_out_radio != 0xFF or _aspect_ratio != 0xFF:
                with QSignalBlocker(self.comboBox_out_radio):
                    if  3>_video_inputMode>=0:
                        # self.comboBox_out_radio.clear()
                        # self.comboBox_out_radio.addItems(self._m_radios2)
                        # self.comboBox_out_radio.setCurrentIndex(_aspect_ratio)
                        self.comboBox_out_radio.setEnabled(False)
                    else:

                        self.comboBox_out_radio.setEnabled(True)

                        self.comboBox_out_radio.clear()
                        self.comboBox_out_radio.addItems(self._m_radios)
                        self.comboBox_out_radio.setCurrentIndex(_m_out_radio)

        elif obj["function"] == "set_setting_params":
            args = obj["args"]
            logging.debug("Set setting params args args:{}".format(args))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = SC7018Setting()
    window.show()
    sys.exit(app.exec())
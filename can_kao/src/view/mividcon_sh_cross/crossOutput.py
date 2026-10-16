import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSignalBlocker, Qt, Signal, QCoreApplication
from src.ui.mividcon_sh_cross.cross_output_ui import Ui_Cross_Output_Form
from src.model.modelPreferences import ModelPreferences
from src.model.mividcon_sh_cross.CrossPreferences import CrossPreferences
from globals import relative_path, global_qss

class CrossOutput(Ui_Cross_Output_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        # self.pattern_comboBox.addItems(CrossPreferences._patterns)


        self.sfp_radioButton.clicked.connect(lambda: self._on_sdi_sfp_buttonGroup_clicked(1))
        self.sdi_in_radioButton.clicked.connect(lambda: self._on_sdi_sfp_buttonGroup_clicked(0))

        self.hdmiOutSrc_sdiIn_radioButton.clicked.connect(lambda: self._on_hdmiOutSrc_buttonGroup_clicked(0))
        self.hdmiOutSrc_hdmiIn_radioButton.clicked.connect(lambda: self._on_hdmiOutSrc_buttonGroup_clicked(1))
        self.hdmiOutSrc_scaler_radioButton.clicked.connect(lambda: self._on_hdmiOutSrc_buttonGroup_clicked(2))
       # self.hdmiOutSrc_pattern_radioButton.clicked.connect(lambda: self._on_hdmiOutSrc_buttonGroup_clicked(3))

        self.sdiOutSrc_sdiIn_radioButton.clicked.connect(lambda: self._on_sdiOutSrc_buttonGroup_clicked(0))
        self.sdiOutSrc_hdmiIn_radioButton.clicked.connect(lambda: self._on_sdiOutSrc_buttonGroup_clicked(1))
        self.sdiOutSrc_scaler_radioButton.clicked.connect(lambda: self._on_sdiOutSrc_buttonGroup_clicked(2))
        #self.sdiOutSrc_pattern_radioButton.clicked.connect(lambda: self._on_sdiOutSrc_buttonGroup_clicked(3))

        self.scalerSrc_sdiIn_radioButton.clicked.connect(lambda: self._on_scalerSrc_buttonGroup_clicked(0))
        self.scalerSrc_hdmiIn_radioButton.clicked.connect(lambda: self._on_scalerSrc_buttonGroup_clicked(1))
        #self.scalerSrc_pattern_radioButton.clicked.connect(lambda: self._on_scalerSrc_buttonGroup_clicked(2))

        # self.pattern_comboBox.currentIndexChanged.connect(self._on_pattern_index_changed)

        # self.sdiOutMode_loopOut_radioButton.clicked.connect(lambda: self._on_sdiOutMode_buttonGroup_clicked(0))
        # self.sdiOutMode_output_radioButton.clicked.connect(lambda: self._on_sdiOutMode_buttonGroup_clicked(1))

    def _on_sdi_sfp_buttonGroup_clicked(self, index):
        logging.debug(f"SDI/SFP in: index={index}")
        currentCheck = CrossPreferences.get_sdi_sfp_by_index(index)
        _args = {
            "SDISFPIn": currentCheck
        }
        self.hdmiOutSrc_sdiIn_radioButton.setText(currentCheck) # HDMI 同步
        self.sdiOutSrc_sdiIn_radioButton.setText(currentCheck)  # SDI 同步
        self.scalerSrc_sdiIn_radioButton.setText(currentCheck)  # scaler 同步

        self._parent.controller.set_output_params(_args)
    def _on_hdmiOutSrc_buttonGroup_clicked(self, index):
        logging.debug(f"_on_hdmiOutSrc_buttonGroup_clicked: index={index}")
        _args = {
            "HDMIOutSource": CrossPreferences.get_output_source_by_index(index)
        }
        self._parent.controller.set_output_params(_args)

    def _on_sdiOutSrc_buttonGroup_clicked(self, index):
        logging.debug(f"_on_sdiOutSrc_buttonGroup_clicked: index={index}")
        _args = {
            "SDIOutSource": CrossPreferences.get_output_source_by_index(index)
        }
        self._parent.controller.set_output_params(_args)

    def _on_scalerSrc_buttonGroup_clicked(self, index):
        logging.debug(f"_on_scalerSrc_buttonGroup_clicked: index={index}")
        _args = {
            "ScalerSource": CrossPreferences.get_scaler_source_by_index(index)
        }
        self._parent.controller.set_output_params(_args)

    def _on_pattern_index_changed(self, index):
        logging.debug(f"_on_pattern_index_changed: index={index}")
        _args = {
            "Pattern": CrossPreferences.get_pattern_by_index(index)
        }
        self._parent.controller.set_output_params(_args)

    def _on_sdiOutMode_buttonGroup_clicked(self, index):
        logging.debug(f"_on_sdiOutMode_buttonGroup_clicked: index={index}")
        _args = {
            "SDIOutMode": CrossPreferences.get_sdi_out_mode_by_index(index)
        }
        self._parent.controller.set_output_params(_args)

    def showEvent(self, event):
        self._parent.controller.get_output_video_params()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_output_video_params":
            args = obj["args"]
            logging.debug("Get output video params args:{}".format(args))

            try:
                if args["HDMIOut"]["sourceString"] == "SDI In":
                    self.hdmiOutSrc_sdiIn_radioButton.setChecked(True)
                elif args["HDMIOut"]["sourceString"] == "HDMI In":
                    self.hdmiOutSrc_hdmiIn_radioButton.setChecked(True)
                elif args["HDMIOut"]["sourceString"] == "Scaler":
                    self.hdmiOutSrc_scaler_radioButton.setChecked(True)
                # else:
                #     self.hdmiOutSrc_pattern_radioButton.setChecked(True)

                if args["SDIOut"]["sourceString"] == "SDI In":
                    self.sdiOutSrc_sdiIn_radioButton.setChecked(True)
                elif args["SDIOut"]["sourceString"] == "HDMI In":
                    self.sdiOutSrc_hdmiIn_radioButton.setChecked(True)
                elif args["SDIOut"]["sourceString"] == "Scaler":
                    self.sdiOutSrc_scaler_radioButton.setChecked(True)
                # else:
                #     self.sdiOutSrc_pattern_radioButton.setChecked(True)

                if args["Scaler"]["sourceString"] == "SDI In":
                    self.scalerSrc_sdiIn_radioButton.setChecked(True)
                elif args["Scaler"]["sourceString"] == "HDMI In":
                    self.scalerSrc_hdmiIn_radioButton.setChecked(True)
                # else:
                #     self.scalerSrc_pattern_radioButton.setChecked(True)

                if args["Sdi_Sfp"]["sourceString"] == "SDI In":
                    self.sdi_in_radioButton.setChecked(True)
                elif args["Sdi_Sfp"]["sourceString"] == "SFP In":
                    self.sfp_radioButton.setChecked(True)

                # self.pattern_comboBox.setCurrentIndex(args["Pattern"]["source"])

                # if args["SDIOut_1_2"]["modeString"] == "Loop Out":
                #     self.sdiOutMode_loopOut_radioButton.setChecked(True)
                # else:
                #     self.sdiOutMode_output_radioButton.setChecked(True)
            except Exception as e:
                logging.error("Update output video error!")
        elif obj["function"] == "set_output_params":
            args = obj["args"]
            logging.debug("Set output params args:{}".format(args))
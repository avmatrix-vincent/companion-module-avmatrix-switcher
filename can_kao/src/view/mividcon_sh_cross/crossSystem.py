import os, sys, logging

from src.config.TranslationManager import TranslationManager

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSignalBlocker, Qt, Signal, QCoreApplication
from src.ui.mividcon_sh_cross.cross_system_ui import Ui_Cross_System_Form
from src.model.modelPreferences import ModelPreferences
from src.model.mividcon_sh_cross.CrossPreferences import CrossPreferences
from globals import relative_path, global_qss

class CrossSystem(Ui_Cross_System_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.scalerRef_comboBox.addItems(CrossPreferences._scaler_refs)
        self.noSignalIndicator_comboBox.addItems(CrossPreferences._no_signal_indicators)
        self.lcdOffTime_comboBox.addItems(CrossPreferences._lcd_off_times)
        self.back2StatusTime_comboBox.addItems(CrossPreferences._back_to_status_times)
        self.language_comboBox.addItems(CrossPreferences._languages)
        self.factoryReset_pushButton.setProperty("type", "device_btn")
        self.versionValue_label.setText("")

        self.scalerRef_comboBox.currentIndexChanged.connect(self._on_scaler_ref_index_changed)
        self.noSignalIndicator_comboBox.currentIndexChanged.connect(self._on_no_signal_indicator_index_changed)
        self.lcdOffTime_comboBox.currentIndexChanged.connect(self._on_lcd_off_time_index_changed)
        self.back2StatusTime_comboBox.currentIndexChanged.connect(self._on_back_to_status_time_index_changed)
        self.language_comboBox.currentIndexChanged.connect(self._on_language_index_changed)

        self.factoryReset_pushButton.clicked.connect(self._on_factory_reset_clicked)

    def _on_scaler_ref_index_changed(self, index):
        _args = {
            "ScalerRef":  CrossPreferences.get_scaler_ref_by_index(index)
        }
        logging.debug(f"_on_scaler_ref_index_changed: _args={_args}")
        self._parent.controller.set_system_params(_args)

    def _on_no_signal_indicator_index_changed(self, index):
        _args = {
            "NoSignalIndicator":  CrossPreferences.get_no_signal_indicator_by_index(index)
        }
        logging.debug(f"_on_scaler_ref_index_changed: _args={_args}")
        self._parent.controller.set_system_params(_args)

    def _on_lcd_off_time_index_changed(self, index):
        _args = {
            "LCDOffTime":  CrossPreferences.get_lcd_off_time_by_index(index)
        }
        logging.debug(f"_on_lcd_off_time_index_changed: _args={_args}")
        self._parent.controller.set_system_params(_args)

    def _on_back_to_status_time_index_changed(self, index):
        _args = {
            "BackToStatusTime":  CrossPreferences.get_back_to_status_time_by_index(index)
        }
        logging.debug(f"_on_back_to_status_time_index_changed: _args={_args}")
        self._parent.controller.set_system_params(_args)

    def _on_language_index_changed(self, index):
        _args = {
            "Language":  index
        }
        logging.debug(f"_on_language_index_changed: _args={_args}")
        lan_text = self.language_comboBox.currentText()
        if "中文" in lan_text:
            TranslationManager().set_language(1)  # 1  为中文
        else:
            TranslationManager().set_language(0)  # 0 为英文

        self._parent.controller.set_system_params(_args)

    def _on_factory_reset_clicked(self):
        logging.debug("_on_factory_reset_clicked")
        confirm_box = QMessageBox()
        confirm_box.setText(QCoreApplication.translate("Cross_System_Form","Confirm reset and restart?",None))  # QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"Restore device to factory settings?", None)
        confirm_box.setWindowTitle(QCoreApplication.translate("Cross_System_Form","Factory Reset",None))
        yes_btn = confirm_box.addButton(QMessageBox.Yes)
        no_btn = confirm_box.addButton(QMessageBox.No)
        yes_btn.setText(QCoreApplication.translate("Cross_System_Form","Yes",None))
        no_btn.setText(QCoreApplication.translate("Cross_System_Form","No",None))
        response = confirm_box.exec()
    
        # 根据用户的选择进行操作
        if response == QMessageBox.No:
            return
        
        _args = {
            "FactoryReset":  True
        }
        logging.debug(f"_on_language_index_changed: _args={_args}")
        self._parent.controller.set_system_params(_args)

    def showEvent(self, event):
        self._parent.controller.get_system_params()
        self._parent.controller.get_version_info()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_system_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))
            try:
                self.scalerRef_comboBox.blockSignals(True)
                self.scalerRef_comboBox.setCurrentIndex(args["ScalerRef"]["source"])
                self.scalerRef_comboBox.blockSignals(False)

                self.noSignalIndicator_comboBox.blockSignals(True)
                self.noSignalIndicator_comboBox.clear()
                self.noSignalIndicator_comboBox.addItems(QCoreApplication.translate("Cross_System_Form", item, None)
                for item in CrossPreferences._no_signal_indicators)
                self.noSignalIndicator_comboBox.setCurrentIndex(args["NoSignalIndicator"]["indicator"])
                self.noSignalIndicator_comboBox.blockSignals(False)

                self.lcdOffTime_comboBox.blockSignals(True)
                self.lcdOffTime_comboBox.clear()
                self.lcdOffTime_comboBox.addItems(QCoreApplication.translate("Cross_System_Form", item, None)
                                                         for item in CrossPreferences._lcd_off_times)
                self.lcdOffTime_comboBox.setCurrentIndex(args["LCDOffTime"]["time"])
                self.lcdOffTime_comboBox.blockSignals(False)

                self.back2StatusTime_comboBox.blockSignals(True)
                self.back2StatusTime_comboBox.clear()
                self.back2StatusTime_comboBox.addItems(QCoreApplication.translate("Cross_System_Form", item, None)
                                                  for item in CrossPreferences._back_to_status_times)
                self.back2StatusTime_comboBox.setCurrentIndex(args["Back2StatusTime"]["time"])
                self.back2StatusTime_comboBox.blockSignals(False)

                self.language_comboBox.blockSignals(True)
                self.language_comboBox.clear()
                self.language_comboBox.addItems(CrossPreferences.get_languages_by_index(args["LanguageList"]["lan"]))
                if args["Language"]["lan"]<len(CrossPreferences.get_languages_by_index(args["LanguageList"]["lan"])):
                    self.language_comboBox.setCurrentIndex(args["Language"]["lan"])
                else:
                    self.language_comboBox.setCurrentIndex(0)

                # lan_text = self.language_comboBox.currentText()
                # if "中文" in lan_text:
                #     TranslationManager().set_language(1)  # 1  为中文
                # else:
                #     TranslationManager().set_language(0)  # 0 为英文

                self.language_comboBox.blockSignals(False)


            except Exception as e:
                logging.error("Update system information error!")


        elif obj["function"] == "get_version_info":
            args = obj["args"]
            logging.debug("Get version args:{}".format(args))
            if args["APPVersion"][3] != 0:
                _app_version = "MCU V%d.%d.%d.%d" % (args["APPVersion"][0], args["APPVersion"][1],
                                                        args["APPVersion"][2], args["APPVersion"][3])
            else:
                _app_version = "MCU V%d.%d.%d" % (args["APPVersion"][0], args["APPVersion"][1], args["APPVersion"][2])
            self.versionValue_label.setText(_app_version)
            if args["FPGAVersion"][3] != 0:
                _fpga_version = "FPGA V%d.%d.%d.%d" % (args["FPGAVersion"][0], args["FPGAVersion"][1],
                                                        args["FPGAVersion"][2], args["FPGAVersion"][3])
            else:
                _fpga_version = "FPGA V%d.%d.%d" % (args["FPGAVersion"][0], args["FPGAVersion"][1], args["FPGAVersion"][2])
            self.versionValue_label2.setText(_fpga_version)
            
        elif obj["function"] == "set_system_params":
            args = obj["args"]
            logging.debug("Set system args:{}".format(args))
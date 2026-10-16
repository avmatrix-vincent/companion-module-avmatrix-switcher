import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSignalBlocker, Qt, Signal
from src.ui.uc1218_4K.uc1218_4K_audio_ui import Ui_UC1218_4K_Audio_Form
from src.model.modelPreferences import ModelPreferences
from src.model.uc1218_4K.uc1218_4K_Preferences import UC1218_4K_Preferences
from globals import relative_path, global_qss

class UC1218_4K_Audio(Ui_UC1218_4K_Audio_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.hdmi_volume_slider.setRange(-72, 30)
        self.hdmi_volume_slider.valueChanged.connect(self._on_hdmi_volume_slider_value_changed)

        self.pc_volume_slider.setRange(-72, 30)
        self.pc_volume_slider.valueChanged.connect(self._on_pc_volume_slider_value_changed)

        self.line_in_volume_slider.setRange(-23, 8)
        self.line_in_volume_slider.valueChanged.connect(self._on_line_in_volume_slider_value_changed)

        self.mic_in_volume_slider.setRange(0, 7)
        self.mic_in_volume_slider.valueChanged.connect(self._on_mic_in_volume_slider_value_changed)

        self.hp_out_volume_slider.setRange(-31, 8)
        self.hp_out_volume_slider.valueChanged.connect(self._on_hp_out_volume_slider_value_changed)

        self.mixer_submit_pushButton.clicked.connect(self._on_submit_mixer_config)

        self.mixer_uac_out_pc_in_checkBox.setDisabled(True) # UAC本身就是PC输出，因此不能选择PC IN，增加此控件，只是为了UI对齐
        self.hdmi_volume_value_lineEdit.setReadOnly(True)
        self.line_in_volume_value_lineEdit.setReadOnly(True)
        self.pc_volume_value_lineEdit.setReadOnly(True)
        self.mic_in_volume_value_lineEdit.setReadOnly(True)
        self.hp_out_volume_value_lineEdit.setReadOnly(True)

    def _set_rtice_i2sout_mixer_source(self):
        mixer_sources = []

        if self.mixer_hp_out_pc_checkBox.isChecked(): mixer_sources.append("UAC")
        if self.mixer_hp_out_hdmi_checkBox.isChecked(): mixer_sources.append("SPDIF")

        _args = {
            "MixerSource": mixer_sources
        }
        self._parent.controller.set_rtice_Audio_I2SOut_MixerSource(_args)
    
    def _set_rtice_uacout2_mixer_source(self):
        mixer_sources = ["I2S IN"] #I2S IN是必须的，用于接入MIC IN和Line IN

        if self.mixer_uac_out_hmdi_checkBox.isChecked(): mixer_sources.append("SPDIF")

        _args = {
            "MixerSource": mixer_sources
        }
        self._parent.controller.set_rtice_Audio_UACOut2_MixerSource(_args)

    def _set_codec_mixer_source(self):
        _args = {
            "MicInToI2SEnable": self.mixer_uac_out_mic_in_checkBox.isChecked(),
            "LineInToI2SEnable": self.mixer_uac_out_line_in_checkBox.isChecked(),
            "MicInToHpEnable": self.mixer_hp_out_mic_in_checkBox.isChecked(),
            "LineInToHpEnable": self.mixer_hp_out_line_in_checkBox.isChecked(),
            "I2SInToHpEnable": self.mixer_hp_out_hdmi_checkBox.isChecked() or self.mixer_hp_out_pc_checkBox.isChecked()
        }
        self._parent.controller.set_codec_mixer(_args)

    def _on_submit_mixer_config(self):
        logging.debug("_on_submit_mixer_config")
        self._set_codec_mixer_source()
        self._set_rtice_i2sout_mixer_source()
        self._set_rtice_uacout2_mixer_source()

    def _on_hdmi_volume_slider_value_changed(self, value):
        self.hdmi_volume_value_lineEdit.setText(f"{value}dB")
        _args = {
            "Gain": value
        }
        self._parent.controller.set_rtice_Audio_HdmiDPRX_VolumeGain(_args)

    def _on_pc_volume_slider_value_changed(self, value):
        self.pc_volume_value_lineEdit.setText(f"{value}dB")
        _args = {
            "Gain": value
        }
        self._parent.controller.set_rtice_Audio_UAC_VolumeGain(_args)

    def _on_line_in_volume_slider_value_changed(self, value):
        self.line_in_volume_value_lineEdit.setText(f"{value*1.5}dB")
        _args = {
            "Channel": "LineIn",
            "Volume": value*1.5
        }
        self._parent.controller.set_codec_volume(_args)
    
    def _on_mic_in_volume_slider_value_changed(self, index):
        _mic_in_db_list = UC1218_4K_Preferences.get_codec_mic_in_volumes()
        self.mic_in_volume_value_lineEdit.setText(f"{_mic_in_db_list[index]}")
        _args = {
            "Channel": "MicIn",
            "Volume": _mic_in_db_list[index]
        }
        self._parent.controller.set_codec_volume(_args)

    def _on_hp_out_volume_slider_value_changed(self, value):
        self.hp_out_volume_value_lineEdit.setText(f"{value*1.5}dB")
        _args = {
            "Channel": "HeadphoneOut",
            "Volume": value*1.5
        }
        self._parent.controller.set_codec_volume(_args)

    def showEvent(self, event):
        # self._parent.controller.get_version_info()
        self._parent.controller.get_codec_volume()
        self._parent.controller.get_rtice_Audio_HdmiDPRX_VolumeGain()
        self._parent.controller.get_rtice_Audio_UAC_VolumeGain()
        self._parent.controller.get_rtice_Audio_I2SOut_MixerSource()
        self._parent.controller.get_rtice_Audio_UACOut2_MixerSource()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_version_info":
            # _model = self._parent.args["args"]["model"]
            _manufacturer = self._parent.args["args"]["manufacturer"]
            _sn = self._parent.args["args"]["sn"]
        elif obj["function"] == "get_codec_volume":
            args = obj["args"]
            logging.debug("Get volume args:{}".format(args))
            # print("Get device's edid args:{}".format(args))
            with QSignalBlocker(self.hp_out_volume_slider):
                self.hp_out_volume_slider.setValue(args["HeadphoneOut"]["volume"])
                volume_db = args["HeadphoneOut"]["db"]
                self.hp_out_volume_value_lineEdit.setText(f"{volume_db}")

            with QSignalBlocker(self.line_in_volume_slider):
                self.line_in_volume_slider.setValue(args["LineIn"]["volume"])
                volume_db = args["LineIn"]["db"]
                self.line_in_volume_value_lineEdit.setText(f"{volume_db}")

            with QSignalBlocker(self.mic_in_volume_slider):
                self.mic_in_volume_slider.setValue(args["MicIn"]["volume"])
                volume_db = args["MicIn"]["db"]
                self.mic_in_volume_value_lineEdit.setText(f"{volume_db}")

            self.mixer_uac_out_line_in_checkBox.setChecked(args["I2SMixer"]["LineInToI2SEnable"])
            self.mixer_uac_out_mic_in_checkBox.setChecked(args["I2SMixer"]["MicInToI2SEnable"])

            self.mixer_hp_out_line_in_checkBox.setChecked(args["I2SMixer"]["LineInToHpEnable"])
            self.mixer_hp_out_mic_in_checkBox.setChecked(args["I2SMixer"]["MicInToHpEnable"])
        elif obj["function"] == "get_Audio_I2SOut_MixerSource":
            args = obj["args"]
            if "UAC" in args["MixerSource"]:
                self.mixer_hp_out_pc_checkBox.setChecked(True)
            else:
                self.mixer_hp_out_pc_checkBox.setChecked(False)

            if "SPDIF" in args["MixerSource"]:
                self.mixer_hp_out_hdmi_checkBox.setChecked(True)
            else:
                self.mixer_hp_out_hdmi_checkBox.setChecked(False)

        elif obj["function"] == "get_Audio_UACOut2_MixerSource":
            args = obj["args"]

            if "SPDIF" in args["MixerSource"]:
                self.mixer_uac_out_hmdi_checkBox.setChecked(True)
            else:
                self.mixer_uac_out_hmdi_checkBox.setChecked(False)

        elif obj["function"] == "get_Audio_HdmiDPRX_VolumeGain":
            args = obj["args"]
            gain = args["Gain"]

            with QSignalBlocker(self.hdmi_volume_slider):
                self.hdmi_volume_slider.setValue(gain)
                self.hdmi_volume_value_lineEdit.setText(f"{gain}dB")
        elif obj["function"] == "get_Audio_UAC_VolumeGain":
            args = obj["args"]
            gain = args["Gain"]

            with QSignalBlocker(self.pc_volume_slider):
                self.pc_volume_slider.setValue(gain)
                self.pc_volume_value_lineEdit.setText(f"{gain}dB")

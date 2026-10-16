import logging

from PySide6.QtWidgets import QWidget, QButtonGroup
from PySide6.QtCore import Qt, QSignalBlocker
from src.model.cue01.cue01Preferences import Cue01Preferences
from src.ui.cue01.audioWidget_ui import Ui_CUE01_Audio_Form

class AudioWidget(Ui_CUE01_Audio_Form, QWidget):
    def __init__(self, parent):
        super(AudioWidget, self).__init__(parent)
        self._parent = parent
        self.setupUi(self)

    def init_ui(self):
        _radio_button_group = QButtonGroup(self.radio_widget)
        _radio_button_group.addButton(self.radioButton_mute)
        _radio_button_group.addButton(self.radioButton_fg_in)
        _radio_button_group.addButton(self.radioButton_bg_in)
        _radio_button_group.addButton(self.radioButton_dsk_in)
        _radio_button_group.addButton(self.radioButton_line_in)
        _radio_button_group.buttonClicked.connect(self.on_radio_button_clicked)

        self.widget_volumn.slider.setRange(0, 14)
        self.widget_volumn.spinbox.setRange(0, 14)
        self.widget_volumn.slider.setValue(7)
        self.widget_volumn.spinbox.setValue(7)
        self.widget_volumn.slider.valueChanged.connect(self.on_volumn_value_changed)
        self.widget_volumn.spinbox.valueChanged.connect(self.on_volumn_value_changed)

        self.check_volumn_status()

    def check_volumn_status(self):
        if self.radioButton_line_in.isChecked():
            self.widget_volumn.setDisabled(False)
        else:
            self.widget_volumn.setDisabled(True)

    def on_radio_button_clicked(self, button):
        logging.debug("select PGM type:{}".format(button.text()))
        pgm_type = 0
        if button == self.radioButton_mute:
            pgm_type = 0
            self.widget_volumn.setDisabled(True)
        elif button == self.radioButton_fg_in:
            pgm_type = 1
            self.widget_volumn.setDisabled(True)
        elif button == self.radioButton_bg_in:
            pgm_type = 2
            self.widget_volumn.setDisabled(True)
        elif button == self.radioButton_dsk_in:
            pgm_type = 3
            self.widget_volumn.setDisabled(True)
        elif button == self.radioButton_line_in:
            pgm_type = 4
            self.widget_volumn.setDisabled(False)
        args = {
            "PGM": pgm_type,
        }
        self._parent.controller.set_audio_params(args)

    def on_volumn_value_changed(self, value):
        sender = self.sender()
        if sender == self.widget_volumn.slider:
            with QSignalBlocker(self.widget_volumn.spinbox):
                self.widget_volumn.spinbox.setValue(value)
        if sender == self.widget_volumn.spinbox:
            with QSignalBlocker(self.widget_volumn.slider):
                self.widget_volumn.slider.setValue(value)   
        logging.debug("volumn value changed:{}".format(value))
        args = {
            "Volumn": value
        }

        self._parent.controller.set_audio_params(args)

    def showEvent(self, event):
        self._parent.controller.get_audio_params()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_audio_params":
            args = obj["args"]
            logging.debug("audio params args:{}".format(args))
            _pgm_type = args["PGM"]
            _vomun_value = args["Volumn"]
            if not 0 <= _vomun_value <= 14:
                _vomun_value = 7
                
            with QSignalBlocker(self.widget_volumn.slider):
                if _pgm_type == 0:
                    self.radioButton_mute.setChecked(True)
                elif _pgm_type == 1:
                    self.radioButton_fg_in.setChecked(True)
                elif _pgm_type == 2:
                    self.radioButton_bg_in.setChecked(True)
                elif _pgm_type == 3:
                    self.radioButton_dsk_in.setChecked(True)
                elif _pgm_type == 4:
                    self.radioButton_line_in.setChecked(True)
            with QSignalBlocker(self.widget_volumn.spinbox):
                self.widget_volumn.spinbox.setValue(_vomun_value)
            with QSignalBlocker(self.widget_volumn.slider):
                self.widget_volumn.slider.setValue(_vomun_value)
            self.check_volumn_status()

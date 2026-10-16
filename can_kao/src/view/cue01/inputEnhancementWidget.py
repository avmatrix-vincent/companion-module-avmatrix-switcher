import os, sys, logging
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QObject, QSignalBlocker
from src.ui.cue01.inputEnhancementWidget_ui import Ui_CUE01_Input_Enhancement_Widget_Form
from src.model.cue01.cue01Preferences import Cue01Preferences
from globals import block_signal

class InputEnhancementWidget(Ui_CUE01_Input_Enhancement_Widget_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self._input_values = []
        self.setupUi(self)

    def init_ui(self):
        self.line.setProperty("type", "title_line")
        self.line_2.setProperty("type", "title_line")
        self.line_3.setProperty("type", "title_line")
        self.line_4.setProperty("type", "title_line")
        self.line_5.setProperty("type", "title_line")
        self.line_6.setProperty("type", "title_line")

        self.label.setProperty("type", "title")
        self.label_2.setProperty("type", "title")
        self.label_3.setProperty("type", "title")

        self.comboBox_fore_color.setMaximumHeight(20)
        self.comboBox_back_color.setMaximumHeight(20)
        self.comboBox_aux_color.setMaximumHeight(20)

        self.widget_fore_contrast.slider.setRange(0, 255)
        self.widget_fore_contrast.spinbox.setRange(0, 255)
        self.widget_back_contrast.slider.setRange(0, 255)
        self.widget_back_contrast.spinbox.setRange(0, 255)
        self.widget_aux_contrast.slider.setRange(0, 255)
        self.widget_aux_contrast.spinbox.setRange(0, 255)
        self.widget_fore_brightness.slider.setRange(0, 255)
        self.widget_fore_brightness.spinbox.setRange(0, 255)
        self.widget_back_brightness.slider.setRange(0, 255)
        self.widget_back_brightness.spinbox.setRange(0, 255)
        self.widget_aux_brightness.slider.setRange(0, 255)
        self.widget_aux_brightness.spinbox.setRange(0, 255)
        self.widget_fore_saturation.slider.setRange(0, 255)
        self.widget_fore_saturation.spinbox.setRange(0, 255)
        self.widget_back_saturation.slider.setRange(0, 255)
        self.widget_back_saturation.spinbox.setRange(0, 255)
        self.widget_aux_saturation.slider.setRange(0, 255)
        self.widget_aux_saturation.spinbox.setRange(0, 255)
        self.widget_fore_hue.slider.setRange(0, 255)
        self.widget_fore_hue.spinbox.setRange(0, 255)
        self.widget_back_hue.slider.setRange(0, 255)
        self.widget_back_hue.spinbox.setRange(0, 255)
        self.widget_aux_hue.slider.setRange(0, 255)
        self.widget_aux_hue.spinbox.setRange(0, 255)

        self.widget_fore_anti_hori.slider.setRange(0, 19)
        self.widget_fore_anti_verti.slider.setRange(0, 19)
        self.widget_fore_peak_hori.slider.setRange(0, 10)
        self.widget_fore_peak_verti.slider.setRange(0, 10)
        self.widget_back_anti_hori.slider.setRange(0, 19)
        self.widget_back_anti_verti.slider.setRange(0, 19)
        self.widget_back_peak_hori.slider.setRange(0, 10)
        self.widget_back_peak_verti.slider.setRange(0, 10)
        self.widget_aux_anti_hori.slider.setRange(0, 19)
        self.widget_aux_anti_verti.slider.setRange(0, 19)
        self.widget_aux_peak_hori.slider.setRange(0, 10)
        self.widget_aux_peak_verti.slider.setRange(0, 10)

        self.widget_fore_anti_hori.spinbox.setRange(0, 19)
        self.widget_fore_anti_verti.spinbox.setRange(0, 19)
        self.widget_fore_peak_hori.spinbox.setRange(0, 10)
        self.widget_fore_peak_verti.spinbox.setRange(0, 10)
        self.widget_back_anti_hori.spinbox.setRange(0, 19)
        self.widget_back_anti_verti.spinbox.setRange(0, 19)
        self.widget_back_peak_hori.spinbox.setRange(0, 10)
        self.widget_back_peak_verti.spinbox.setRange(0, 10)
        self.widget_aux_anti_hori.spinbox.setRange(0, 19)
        self.widget_aux_anti_verti.spinbox.setRange(0, 19)
        self.widget_aux_peak_hori.spinbox.setRange(0, 10)
        self.widget_aux_peak_verti.spinbox.setRange(0, 10)

        _color_tones = Cue01Preferences.get_color_tones()
        self.comboBox_fore_color.addItems(_color_tones)
        self.comboBox_back_color.addItems(_color_tones)
        self.comboBox_aux_color.addItems(_color_tones)
        self.comboBox_fore_color.currentIndexChanged[int].connect(self._select_color_tone)
        self.comboBox_back_color.currentIndexChanged[int].connect(self._select_color_tone)
        self.comboBox_aux_color.currentIndexChanged[int].connect(self._select_color_tone)

        self.widget_fore_lti_switch_btn.checkedChanged.connect(self._on_lti_rbtn_clicked)
        self.widget_fore_cti_switch_btn.checkedChanged.connect(self._on_cti_rbtn_clicked)
        self.widget_back_lti_switch_btn.checkedChanged.connect(self._on_lti_rbtn_clicked)
        self.widget_back_cti_switch_btn.checkedChanged.connect(self._on_cti_rbtn_clicked)
        self.widget_aux_lti_switch_btn.checkedChanged.connect(self._on_lti_rbtn_clicked)
        self.widget_aux_cti_switch_btn.checkedChanged.connect(self._on_cti_rbtn_clicked)

        self.widget_fore_anti_hori.slider.valueChanged.connect(self._anti_alias_horizontal_slider_value_changed)
        self.widget_fore_anti_hori.spinbox.valueChanged.connect(self._anti_alias_horizontal_spin_box_value_changed)
        self.widget_fore_anti_verti.slider.valueChanged.connect(self._anti_alias_vertical_slider_value_changed)
        self.widget_fore_anti_verti.spinbox.valueChanged.connect(self._anti_alias_vertical_spin_box_value_changed)
        self.widget_fore_peak_hori.slider.valueChanged.connect(self._peak_filter_horizontal_slider_value_changed)
        self.widget_fore_peak_hori.spinbox.valueChanged.connect(self._peak_filter_horizontal_spin_box_value_changed)
        self.widget_fore_peak_verti.slider.valueChanged.connect(self._peak_filter_vertical_slider_value_changed)
        self.widget_fore_peak_verti.spinbox.valueChanged.connect(self._peak_filter_vertical_spin_box_value_changed)
        self.widget_fore_contrast.slider.valueChanged.connect(self._contrast_slider_value_changed)
        self.widget_fore_contrast.spinbox.valueChanged.connect(self._contrast_spin_box_value_changed)
        self.widget_fore_brightness.slider.valueChanged.connect(self._brightness_slider_value_changed)
        self.widget_fore_brightness.spinbox.valueChanged.connect(self._brightness_spin_box_value_changed)
        self.widget_fore_saturation.slider.valueChanged.connect(self._saturation_slider_value_changed)
        self.widget_fore_saturation.spinbox.valueChanged.connect(self._saturation_spin_box_value_changed)
        self.widget_fore_hue.slider.valueChanged.connect(self._hue_slider_value_changed)
        self.widget_fore_hue.spinbox.valueChanged.connect(self._hue_spin_box_value_changed)

        self.widget_back_anti_hori.slider.valueChanged.connect(self._anti_alias_horizontal_slider_value_changed)
        self.widget_back_anti_hori.spinbox.valueChanged.connect(self._anti_alias_horizontal_spin_box_value_changed)
        self.widget_back_anti_verti.slider.valueChanged.connect(self._anti_alias_vertical_slider_value_changed)
        self.widget_back_anti_verti.spinbox.valueChanged.connect(self._anti_alias_vertical_spin_box_value_changed)
        self.widget_back_peak_hori.slider.valueChanged.connect(self._peak_filter_horizontal_slider_value_changed)
        self.widget_back_peak_hori.spinbox.valueChanged.connect(self._peak_filter_horizontal_spin_box_value_changed)
        self.widget_back_peak_verti.slider.valueChanged.connect(self._peak_filter_vertical_slider_value_changed)
        self.widget_back_peak_verti.spinbox.valueChanged.connect(self._peak_filter_vertical_spin_box_value_changed)
        self.widget_back_contrast.slider.valueChanged.connect(self._contrast_slider_value_changed)
        self.widget_back_contrast.spinbox.valueChanged.connect(self._contrast_spin_box_value_changed)
        self.widget_back_brightness.slider.valueChanged.connect(self._brightness_slider_value_changed)
        self.widget_back_brightness.spinbox.valueChanged.connect(self._brightness_spin_box_value_changed)
        self.widget_back_saturation.slider.valueChanged.connect(self._saturation_slider_value_changed)
        self.widget_back_saturation.spinbox.valueChanged.connect(self._saturation_spin_box_value_changed)
        self.widget_back_hue.slider.valueChanged.connect(self._hue_slider_value_changed)
        self.widget_back_hue.spinbox.valueChanged.connect(self._hue_spin_box_value_changed)

        self.widget_aux_anti_hori.slider.valueChanged.connect(self._anti_alias_horizontal_slider_value_changed)
        self.widget_aux_anti_hori.spinbox.valueChanged.connect(self._anti_alias_horizontal_spin_box_value_changed)
        self.widget_aux_anti_verti.slider.valueChanged.connect(self._anti_alias_vertical_slider_value_changed)
        self.widget_aux_anti_verti.spinbox.valueChanged.connect(self._anti_alias_vertical_spin_box_value_changed)
        self.widget_aux_peak_hori.slider.valueChanged.connect(self._peak_filter_horizontal_slider_value_changed)
        self.widget_aux_peak_hori.spinbox.valueChanged.connect(self._peak_filter_horizontal_spin_box_value_changed)
        self.widget_aux_peak_verti.slider.valueChanged.connect(self._peak_filter_vertical_slider_value_changed)
        self.widget_aux_peak_verti.spinbox.valueChanged.connect(self._peak_filter_vertical_spin_box_value_changed)
        self.widget_aux_contrast.slider.valueChanged.connect(self._contrast_slider_value_changed)
        self.widget_aux_contrast.spinbox.valueChanged.connect(self._contrast_spin_box_value_changed)
        self.widget_aux_brightness.slider.valueChanged.connect(self._brightness_slider_value_changed)
        self.widget_aux_brightness.spinbox.valueChanged.connect(self._brightness_spin_box_value_changed)
        self.widget_aux_saturation.slider.valueChanged.connect(self._saturation_slider_value_changed)
        self.widget_aux_saturation.spinbox.valueChanged.connect(self._saturation_spin_box_value_changed)
        self.widget_aux_hue.slider.valueChanged.connect(self._hue_slider_value_changed)
        self.widget_aux_hue.spinbox.valueChanged.connect(self._hue_spin_box_value_changed)


        self._input_values = [
            {
                "ContrastSlider": self.widget_back_contrast.slider,
                "ContrastSpinBox": self.widget_back_contrast.spinbox,
                "BrightnessSlider": self.widget_back_brightness.slider,
                "BrightnessSpinBox": self.widget_back_brightness.spinbox,
                "SaturationSlider": self.widget_back_saturation.slider,
                "SaturationSpinBox": self.widget_back_saturation.spinbox,
                "HueSlider": self.widget_back_hue.slider,
                "HueSpinBox": self.widget_back_hue.spinbox,
                "LTISwitchButton": self.widget_back_lti_switch_btn,
                "CTISwitchButton": self.widget_back_cti_switch_btn,
                "ColorToneComboBox": self.comboBox_back_color,
                "ColorToneIndex": 0,
                "AntiAliasHSlider": self.widget_back_anti_hori.slider,
                "AntiAliasHSpinBox": self.widget_back_anti_hori.spinbox,
                "AntiAliasVSlider": self.widget_back_anti_verti.slider,
                "AntiAliasVSpinBox": self.widget_back_anti_verti.spinbox,
                "PeakFilterHSlider": self.widget_back_peak_hori.slider,
                "PeakFilterHSpinBox": self.widget_back_peak_hori.spinbox,
                "PeakFilterVSlider": self.widget_back_peak_verti.slider,
                "PeakFilterVSpinBox": self.widget_back_peak_verti.spinbox
            },
            {
                "ContrastSlider": self.widget_fore_contrast.slider,
                "ContrastSpinBox": self.widget_fore_contrast.spinbox,
                "BrightnessSlider": self.widget_fore_brightness.slider,
                "BrightnessSpinBox": self.widget_fore_brightness.spinbox,
                "SaturationSlider": self.widget_fore_saturation.slider,
                "SaturationSpinBox": self.widget_fore_saturation.spinbox,
                "HueSlider": self.widget_fore_hue.slider,
                "HueSpinBox": self.widget_fore_hue.spinbox,
                "LTISwitchButton": self.widget_fore_lti_switch_btn,
                "CTISwitchButton": self.widget_fore_cti_switch_btn,
                "ColorToneComboBox": self.comboBox_fore_color,
                "ColorToneIndex": 0,
                "AntiAliasHSlider": self.widget_fore_anti_hori.slider,
                "AntiAliasHSpinBox": self.widget_fore_anti_hori.spinbox,
                "AntiAliasVSlider": self.widget_fore_anti_verti.slider,
                "AntiAliasVSpinBox": self.widget_fore_anti_verti.spinbox,
                "PeakFilterHSlider": self.widget_fore_peak_hori.slider,
                "PeakFilterHSpinBox": self.widget_fore_peak_hori.spinbox,
                "PeakFilterVSlider": self.widget_fore_peak_verti.slider,
                "PeakFilterVSpinBox": self.widget_fore_peak_verti.spinbox
            },
            {
                "ContrastSlider": self.widget_aux_contrast.slider,
                "ContrastSpinBox": self.widget_aux_contrast.spinbox,
                "BrightnessSlider": self.widget_aux_brightness.slider,
                "BrightnessSpinBox": self.widget_aux_brightness.spinbox,
                "SaturationSlider": self.widget_aux_saturation.slider,
                "SaturationSpinBox": self.widget_aux_saturation.spinbox,
                "HueSlider": self.widget_aux_hue.slider,
                "HueSpinBox": self.widget_aux_hue.spinbox,
                "LTISwitchButton": self.widget_aux_lti_switch_btn,
                "CTISwitchButton": self.widget_aux_cti_switch_btn,
                "ColorToneComboBox": self.comboBox_aux_color,
                "ColorToneIndex": 0,
                "AntiAliasHSlider": self.widget_aux_anti_hori.slider,
                "AntiAliasHSpinBox": self.widget_aux_anti_hori.spinbox,
                "AntiAliasVSlider": self.widget_aux_anti_verti.slider,
                "AntiAliasVSpinBox": self.widget_aux_anti_verti.spinbox,
                "PeakFilterHSlider": self.widget_aux_peak_hori.slider,
                "PeakFilterHSpinBox": self.widget_aux_peak_hori.spinbox,
                "PeakFilterVSlider": self.widget_aux_peak_verti.slider,
                "PeakFilterVSpinBox": self.widget_aux_peak_verti.spinbox
            }
        ]


    def showEvent(self, event):
        self._parent.controller.get_reference_enhancement()
        super().showEvent(event)  # 调用基类的 showEvent 方法
        self.update()

    def handle_async_callback(self, obj):
        if obj["function"] == "get_ref_enhance_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))

            _channel_number = min(args["ChannelNumber"], len(self._input_values))

            for i in range(_channel_number):
                _input = args["Video"][i]

                _contrast = _input["Contrast"]
                _brightness = _input["Brightness"]
                _saturation = _input["Saturation"]
                _hue = _input["Hue"]
                _lti = _input["LTI"]
                _cti = _input["CTI"]
                _color_tone = _input["ColorTone"]
                _h_anti_alias = _input["HAntiAlias"]
                _v_anti_alias = _input["VAntiAlias"]
                _h_peak_filter = _input["HPeakFilter"]
                _v_peak_filter = _input["VPeakFilter"]

                self._input_values[i]["ContrastSlider"].setValue(_contrast)
                self._input_values[i]["ContrastSpinBox"].setValue(_contrast)
                self._input_values[i]["BrightnessSlider"].setValue(_brightness)
                self._input_values[i]["BrightnessSpinBox"].setValue(_brightness)
                self._input_values[i]["SaturationSlider"].setValue(_saturation)
                self._input_values[i]["SaturationSpinBox"].setValue(_saturation)
                self._input_values[i]["HueSlider"].setValue(_hue)
                self._input_values[i]["HueSpinBox"].setValue(_hue)

                if _lti == "On" or _lti == "ON":
                    self._input_values[i]["LTISwitchButton"].set_checked(True)
                else:
                    self._input_values[i]["LTISwitchButton"].set_checked(False)

                if _cti == "On" or _cti == "ON":
                    self._input_values[i]["CTISwitchButton"].set_checked(True)
                else:
                    self._input_values[i]["CTISwitchButton"].set_checked(False)

                _color_tone_index = Cue01Preferences.get_index_by_color_tone(_color_tone)
                if _color_tone_index != 0xFF:
                    self._input_values[i]["ColorToneIndex"] = _color_tone_index
                    self._input_values[i]["ColorToneComboBox"].setCurrentIndex(_color_tone_index)

                self._input_values[i]["AntiAliasHSpinBox"].setValue(_h_anti_alias)
                self._input_values[i]["AntiAliasHSlider"].setValue(_h_anti_alias)
                self._input_values[i]["AntiAliasVSpinBox"].setValue(_v_anti_alias)
                self._input_values[i]["AntiAliasVSlider"].setValue(_v_anti_alias)
                self._input_values[i]["PeakFilterHSpinBox"].setValue(_h_peak_filter)
                self._input_values[i]["PeakFilterHSlider"].setValue(_h_peak_filter)
                self._input_values[i]["PeakFilterVSpinBox"].setValue(_v_peak_filter)
                self._input_values[i]["PeakFilterVSlider"].setValue(_v_peak_filter)
            # self.update()
        elif obj["function"] == "set_input_enhancement":
            args = obj["args"]
            logging.debug("Set input enhancement args:{}".format(args))

    # 通过 key 获取对应控件
    def get_target_widget(self, sender_key, target_key, *args, **kwargs):
        sender = self.sender()
        for controls in self._input_values:
            if controls[sender_key] == sender:
                return controls[target_key]
        return None

    @block_signal(lambda self, value: self.get_target_widget("AntiAliasHSlider", "AntiAliasHSpinBox"))
    def _anti_alias_horizontal_slider_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["AntiAliasHSlider"] == sender:
                if self._input_values[i]["AntiAliasHSpinBox"].value() != value:
                    self._input_values[i]["AntiAliasHSpinBox"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "HAntiAlias": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("AntiAliasHSpinBox", "AntiAliasHSlider"))
    def _anti_alias_horizontal_spin_box_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["AntiAliasHSpinBox"] == sender:
                if self._input_values[i]["AntiAliasHSlider"].value() != value:
                    self._input_values[i]["AntiAliasHSlider"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "HAntiAlias": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("AntiAliasVSlider", "AntiAliasVSpinBox"))
    def _anti_alias_vertical_slider_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["AntiAliasVSlider"] == sender:
                if self._input_values[i]["AntiAliasVSpinBox"].value() != value:
                    self._input_values[i]["AntiAliasVSpinBox"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "VAntiAlias": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("AntiAliasVSpinBox", "AntiAliasVSlider"))
    def _anti_alias_vertical_spin_box_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["AntiAliasVSpinBox"] == sender:
                if self._input_values[i]["AntiAliasVSlider"].value() != value:
                    self._input_values[i]["AntiAliasVSlider"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "VAntiAlias": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("PeakFilterHSlider", "PeakFilterHSpinBox"))
    def _peak_filter_horizontal_slider_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["PeakFilterHSlider"] == sender:
                if self._input_values[i]["PeakFilterHSpinBox"].value() != value:
                    self._input_values[i]["PeakFilterHSpinBox"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "HPeakFilter": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("PeakFilterHSpinBox", "PeakFilterHSlider"))
    def _peak_filter_horizontal_spin_box_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["PeakFilterHSpinBox"] == sender:
                if self._input_values[i]["PeakFilterHSlider"].value() != value:
                    self._input_values[i]["PeakFilterHSlider"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "HPeakFilter": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("PeakFilterVSlider", "PeakFilterVSpinBox"))
    def _peak_filter_vertical_slider_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["PeakFilterVSlider"] == sender:
                if self._input_values[i]["PeakFilterVSpinBox"].value() != value:
                    self._input_values[i]["PeakFilterVSpinBox"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "VPeakFilter": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("PeakFilterVSpinBox", "PeakFilterVSlider"))
    def _peak_filter_vertical_spin_box_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["PeakFilterVSpinBox"] == sender:
                if self._input_values[i]["PeakFilterVSlider"].value() != value:
                    self._input_values[i]["PeakFilterVSlider"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "VPeakFilter": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("ContrastSlider", "ContrastSpinBox"))
    def _contrast_slider_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["ContrastSlider"] == sender:
                if self._input_values[i]["ContrastSpinBox"].value() != value:
                    self._input_values[i]["ContrastSpinBox"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "Contrast": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("ContrastSpinBox", "ContrastSlider"))
    def _contrast_spin_box_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["ContrastSpinBox"] == sender:
                if self._input_values[i]["ContrastSlider"].value() != value:
                    self._input_values[i]["ContrastSlider"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "Contrast": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("BrightnessSlider", "BrightnessSpinBox"))
    def _brightness_slider_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["BrightnessSlider"] == sender:
                if self._input_values[i]["BrightnessSpinBox"].value() != value:
                    self._input_values[i]["BrightnessSpinBox"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "Brightness": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("BrightnessSpinBox", "BrightnessSlider"))
    def _brightness_spin_box_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["BrightnessSpinBox"] == sender:
                if self._input_values[i]["BrightnessSlider"].value() != value:
                    self._input_values[i]["BrightnessSlider"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "Brightness": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("SaturationSlider", "SaturationSpinBox"))
    def _saturation_slider_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["SaturationSlider"] == sender:
                if self._input_values[i]["SaturationSpinBox"].value() != value:
                    self._input_values[i]["SaturationSpinBox"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "Saturation": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("SaturationSpinBox", "SaturationSlider"))
    def _saturation_spin_box_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["SaturationSpinBox"] == sender:
                if self._input_values[i]["SaturationSlider"].value() != value:
                    self._input_values[i]["SaturationSlider"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "Saturation": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("HueSlider", "HueSpinBox"))
    def _hue_slider_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["HueSlider"] == sender:
                if self._input_values[i]["HueSpinBox"].value() != value:
                    self._input_values[i]["HueSpinBox"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "Hue": value
                }
                self._parent.controller.set_input_enhancement(_args)

    @block_signal(lambda self, value: self.get_target_widget("HueSpinBox", "HueSlider"))
    def _hue_spin_box_value_changed(self, value):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["HueSpinBox"] == sender:
                if self._input_values[i]["HueSlider"].value() != value:
                    self._input_values[i]["HueSlider"].setValue(value)
                _args = {
                    "VideoSource": i,
                    "Hue": value
                }
                self._parent.controller.set_input_enhancement(_args)

    def _on_lti_rbtn_clicked(self, button):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["LTISwitchButton"] == sender:
                if sender.checked:
                    logging.debug("LTI ON")
                    _args = {
                        "VideoSource": i,
                        "LTI": "On"
                    }
                    self._parent.controller.set_input_enhancement(_args)
                else:
                    logging.debug("CTI OFF")
                    _args = {
                        "VideoSource": i,
                        "LTI": "Off"
                    }
                    self._parent.controller.set_input_enhancement(_args)
    
    def _on_cti_rbtn_clicked(self, button):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["CTISwitchButton"] == sender:
                if sender.checked:
                    logging.debug("CTI ON")
                    _args = {
                        "VideoSource": i,
                        "CTI": "On"
                    }
                    self._parent.controller.set_input_enhancement(_args)
                else:
                    logging.debug("CTI OFF")
                    _args = {
                        "VideoSource": i,
                        "CTI": "Off"
                    }
                    self._parent.controller.set_input_enhancement(_args)

    def _select_color_tone(self, index):
        sender = self.sender()

        for i in range(len(self._input_values)):
            if self._input_values[i]["ColorToneComboBox"] == sender:
                if self._input_values[i]["ColorToneIndex"] != index:
                    logging.debug("select ColorToneIndex {}:{}".format(i, index))
                    self._input_values[i]["ColorToneIndex"] = index
                    _args = {
                        "VideoSource": i,
                        "ColorTone": Cue01Preferences.get_color_tone_by_index(index)
                    }
                    self._parent.controller.set_input_enhancement(_args)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = InputEnhancementWidget()
    window.show()
    sys.exit(app.exec())

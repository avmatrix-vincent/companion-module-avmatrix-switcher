
import logging
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QSignalBlocker
from src.ui.cue01.inputNoiseReductionWidget_ui import Ui_CUE01_Input_Noise_Reduction_Widget_Form
from src.model.cue01.cue01Preferences import Cue01Preferences

class InputNoiseReductionWidget(Ui_CUE01_Input_Noise_Reduction_Widget_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self._nr_values = []
        self._bnr_values = []
        self.setupUi(self)

    def init_ui(self):
        self.line.setProperty("type", "title_line")
        self.line_2.setProperty("type", "title_line")
        self.line_3.setProperty("type", "title_line")
        self.line_4.setProperty("type", "title_line")
        self.line_5.setProperty("type", "title_line")
        self.line_6.setProperty("type", "title_line")
        self.line_7.setProperty("type", "title_line")
        self.line_8.setProperty("type", "title_line")

        self.label.setProperty("type", "title")
        self.label_2.setProperty("type", "title")
        self.label_3.setProperty("type", "title")
        self.label_4.setProperty("type", "title")

        _nr_modes = Cue01Preferences.get_nr_modes()
        _bnr_intensities = Cue01Preferences.get_bnr_intensities()

        self.spinBox.setRange(0, 7)
        self.spinBox_2.setRange(0, 7)
        self.widget_block_threshold.slider.setRange(0, 255)
        self.widget_block_threshold.spinbox.setRange(0, 255)

        self.comboBox_fore_nr.addItems(_nr_modes)
        self.comboBox_back_nr.addItems(_nr_modes)
        self.comboBox_aux_nr.addItems(_nr_modes)
        self.comboBox_bnr.addItems(_bnr_intensities)
        self.comboBox_fore_nr.currentIndexChanged[int].connect(self._select_nr_mode)
        self.comboBox_back_nr.currentIndexChanged[int].connect(self._select_nr_mode)
        self.comboBox_aux_nr.currentIndexChanged[int].connect(self._select_nr_mode)
        self.comboBox_bnr.currentIndexChanged[int].connect(self._select_bnr_intensity)

        self.checkBox_fore_nr_display.stateChanged.connect(self._nr_motion_display_state_changed)
        self.checkBox_back_nr_display.stateChanged.connect(self._nr_motion_display_state_changed)
        self.checkBox_aux_nr_display.stateChanged.connect(self._nr_motion_display_state_changed)

        self.spinBox.valueChanged.connect(self._block_coordinate_x_spin_box_value_changed)
        self.spinBox_2.valueChanged.connect(self._block_coordinate_y_spin_box_value_changed)
        self.widget_block_threshold.spinbox.valueChanged.connect(self._block_threshold_spin_box_value_changed)
        self.widget_block_threshold.slider.valueChanged.connect(self._block_threshold_slider_value_changed)

        self.widget_bnr_mode_switch_btn.checkedChanged.connect(self._on_bnr_mode_rbtn_clicked)
        self.widget_block_switchbtn.checkedChanged.connect(self._on_block_display_rbtn_clicked)

        self._nr_values = [
            {
                "NRModeComboBox": self.comboBox_fore_nr,
                "NRModeIndex": 0,
                "NRMotionDisplayCheckBox": self.checkBox_fore_nr_display,
                "NRMotionDisplayIsChecked": False
            },
            {
                "NRModeComboBox": self.comboBox_back_nr,
                "NRModeIndex": 0,
                "NRMotionDisplayCheckBox": self.checkBox_back_nr_display,
                "NRMotionDisplayIsChecked": False
            },
            {
                "NRModeComboBox": self.comboBox_aux_nr,
                "NRModeIndex": 0,
                "NRMotionDisplayCheckBox": self.checkBox_aux_nr_display,
                "NRMotionDisplayIsChecked": False
            }
        ]

        self._bnr_values = [
            {
                "BNRModeSwitchButton": self.widget_bnr_mode_switch_btn,
                "BNRIntensityCamboBox": self.comboBox_bnr,
                "BNRIntensityIndex": 0,
                "BlockCoordinateXSpinBox": self.spinBox,
                "BlockCoordinateYSpinBox": self.spinBox_2,
                "BlockCoordinateSwitchButton": self.widget_block_switchbtn,
                "BlockThresholdSlider": self.widget_block_threshold.slider,
                "BlockThresholdSpinBox": self.widget_block_threshold.spinbox
            }
        ]


    def _select_nr_mode(self, index):
        sender = self.sender()

        for i in range(len(self._nr_values)):
            if self._nr_values[i]["NRModeComboBox"] == sender:
                if self._nr_values[i]["NRModeIndex"] != index:
                    logging.debug("select NRModeIndex {}:{}".format(i, index))
                    self._nr_values[i]["NRModeIndex"] = index
                    _args = {
                        "VideoSource": i,
                        "NRMode": Cue01Preferences.get_nr_mode_by_index(index)
                    }
                    self._parent.controller.set_input_noise_reduction(_args)

    def _nr_motion_display_state_changed(self, state):
        sender = self.sender()

        for i in range(len(self._nr_values)):
            if self._nr_values[i]["NRMotionDisplayCheckBox"] == sender:
                if self._nr_values[i]["NRMotionDisplayCheckBox"].isChecked() and not self._nr_values[i]["NRMotionDisplayIsChecked"]:
                    logging.debug("NRMotionDisplay {} ON".format(i))
                    self._nr_values[i]["NRMotionDisplayIsChecked"] = True
                    _args = {
                        "VideoSource": i,
                        "NRMotionDisplay": "On"
                    }
                    self._parent.controller.set_input_noise_reduction(_args)
                elif not self._nr_values[i]["NRMotionDisplayCheckBox"].isChecked() and self._nr_values[i]["NRMotionDisplayIsChecked"]:
                    logging.debug("NRMotionDisplay {} OFF".format(i))
                    self._nr_values[i]["NRMotionDisplayIsChecked"] = False
                    _args = {
                        "VideoSource": i,
                        "NRMotionDisplay": "Off"
                    }
                    self._parent.controller.set_input_noise_reduction(_args)

    def _on_bnr_mode_rbtn_clicked(self, checked: bool):
        _bnr_value = self._bnr_values[0]

        if checked:
            logging.debug("BNR Mode ON")
            _args = {
                "BNRMode": "On"
            }
            self._parent.controller.set_input_noise_reduction(_args)
        else:
            logging.debug("BNR Mode OFF")
            _args = {
                "BNRMode": "Off"
            }
            self._parent.controller.set_input_noise_reduction(_args)

    def _select_bnr_intensity(self, index):
        _bnr_value = self._bnr_values[0]

        if _bnr_value["BNRIntensityIndex"] != index:
            logging.debug("select BNRIntensityIndex:{}".format(index))
            _bnr_value["BNRIntensityIndex"] = index
            _args = {
                "BNRIntensity": Cue01Preferences.get_bnr_intensity_by_index(index)
            }
            self._parent.controller.set_input_noise_reduction(_args)

    def _block_coordinate_x_spin_box_value_changed(self, value):
        _bnr_value = self._bnr_values[0]

        logging.debug("Block Coordinate X:{}".format(value))
        _args = {
            "BlockCoordinateX": value,
            "BlockCoordinateY": _bnr_value["BlockCoordinateYSpinBox"].value()
        }
        self._parent.controller.set_input_noise_reduction(_args)

    def _block_coordinate_y_spin_box_value_changed(self, value):
        _bnr_value = self._bnr_values[0]

        logging.debug("Block Coordinate Y:{}".format(value))
        _args = {
            "BlockCoordinateX": _bnr_value["BlockCoordinateXSpinBox"].value(),
            "BlockCoordinateY": value
        }
        self._parent.controller.set_input_noise_reduction(_args)

    def _on_block_display_rbtn_clicked(self, checked:bool):
        _bnr_value = self._bnr_values[0]

        if checked:
            logging.debug("Block Display ON")
            _args = {
                "BlockDisplay": "On"
            }
            self._parent.controller.set_input_noise_reduction(_args)
        else:
            logging.debug("Block Display OFF")
            _args = {
                "BlockDisplay": "Off"
            }
            self._parent.controller.set_input_noise_reduction(_args)

    def _block_threshold_slider_value_changed(self, value):
        _bnr_value = self._bnr_values[0]

        if _bnr_value["BlockThresholdSpinBox"].value() != value:
            with QSignalBlocker(_bnr_value["BlockThresholdSpinBox"]):
                _bnr_value["BlockThresholdSpinBox"].setValue(value)
        _args = {
            "BlockThreshold": value
        }
        self._parent.controller.set_input_noise_reduction(_args)

    def _block_threshold_spin_box_value_changed(self, value):
        _bnr_value = self._bnr_values[0]

        if _bnr_value["BlockThresholdSlider"].value() != value:
            with QSignalBlocker(_bnr_value["BlockThresholdSlider"]):
                _bnr_value["BlockThresholdSlider"].setValue(value)
        _args = {
            "BlockThreshold": value
        }
        self._parent.controller.set_input_noise_reduction(_args)
    
    def showEvent(self, event):
        self._parent.controller.get_noise_reduction()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_noise_reduction_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))

            _channel_number = min(args["ChannelNumber"], len(self._nr_values))

            for i in range(_channel_number):
                _input = args["Video"]

                _nr_mode = _input[i]["NRMode"]
                _nr_motion_display = _input[i]["NRMotionDisplay"]

                _nr_mode_index = Cue01Preferences.get_index_by_nr_mode(_nr_mode)
                if _nr_mode_index != 0xFF:
                    self._nr_values[i]["NRModeIndex"] = _nr_mode_index
                    self._nr_values[i]["NRModeComboBox"].setCurrentIndex(_nr_mode_index)

                if _nr_motion_display == "On" or _nr_motion_display == "ON":
                    self._nr_values[i]["NRMotionDisplayIsChecked"] = True
                    self._nr_values[i]["NRMotionDisplayCheckBox"].setChecked(True)
                else:
                    self._nr_values[i]["NRMotionDisplayIsChecked"] = False
                    self._nr_values[i]["NRMotionDisplayCheckBox"].setChecked(False)

            _bnr_mode = args["BNRMode"]
            _bnr_intensity = args["BNRIntensity"]
            _block_coordinate_x = args["BlockCoordinateX"]
            _block_coordinate_y = args["BlockCoordinateY"]
            _block_display = args["BlockDisplay"]
            _block_threshold = args["BlockThreshold"]

            if _bnr_mode == "On" or _bnr_mode == "ON":
                self._bnr_values[0]["BNRModeSwitchButton"].set_checked(True)
            else:
                self._bnr_values[0]["BNRModeSwitchButton"].set_checked(False)

            _bnr_intensity_index = Cue01Preferences.get_index_by_bnr_intensity(_bnr_intensity)
            if _bnr_intensity_index != 0xFF:
                self._bnr_values[0]["BNRIntensityIndex"] = _bnr_intensity_index
                self._bnr_values[0]["BNRIntensityCamboBox"].setCurrentIndex(_bnr_intensity_index)
            
            self._bnr_values[0]["BlockCoordinateXSpinBox"].setValue(_block_coordinate_x)
            self._bnr_values[0]["BlockCoordinateYSpinBox"].setValue(_block_coordinate_y)

            if _block_display == "On" or _block_display == "ON":
                self._bnr_values[0]["BlockCoordinateSwitchButton"].set_checked(True)
            else:
                self._bnr_values[0]["BlockCoordinateSwitchButton"].set_checked(False)

            self._bnr_values[0]["BlockThresholdSpinBox"].setValue(_block_threshold)
            self._bnr_values[0]["BlockThresholdSlider"].setValue(_block_threshold)
        elif obj["function"] == "set_input_noise_reduction":
            args = obj["args"]
            logging.debug("Set input noise reduction args:{}".format(args))


import logging
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QSignalBlocker, QCoreApplication
from src.ui.cue01.lumaKeyWidget_ui import Ui_CUE01_Luma_Key_Widget_Form
from src.model.cue01.cue01Preferences import Cue01Preferences
from src.config.ChromaConfig import chroma_config
from globals import toggle_layout_enable_or_disable, global_qss, enalbed_range_slider_qss, disabled_range_slider_qss

class LumaKeyWidget(Ui_CUE01_Luma_Key_Widget_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._parent = parent

    def init_ui(self):
        # _fill_srcs = Cue01Preferences.get_luma_video_sources()

        self._luma_key_values = {
            # "FillSourceComboBox": self.comboBox_fill_source,
            "FillSourceIndex": 0,
            "ToleranceCurveSwitchButton": self.widget_tolerance_curve,
            "ToleranceInvertSwitchButton": self.widget_tolerance_invert,
            "ToleranceLeftLabel": self.spinBox_tolerance_min,
            "ToleranceRightLabel": self.spinBox_tolerance_max,
            "ToleranceRangeSlider": self.rangeSlider_tolerance,
            "ToleranceLeftValue": 0,
            "ToleranceRightValue": 1000,
            # "ToleranceUnitStepSpinBox": self.spinBox_unit_step,
            "KeyClipSwitchButton": self.widget_keyClip_switchbtn,
            "KeyClipCurveSwitchButton": self.widget_keyClip_curve_switchbtn,
            "KeyClipLeftLabel": self.spinBox_keyClip_min,
            "KeyClipRightLabel": self.spinBox_keyClip_max,
            "KeyClipRangeSlider": self.rangeSlider_keyClip,
            "KeyClipLeftValue": 0,
            "KeyClipRightValue": 1000,
        }

        # self.comboBox_fill_source.addItems(_fill_srcs)
        # self.comboBox_fill_source.currentIndexChanged[int].connect(self._select_fill_source)

        # self.spinBox_unit_step.valueChanged.connect(self._on_tolerance_unit_step_spin_box_value_changed)

        self.widget_tolerance_curve.checkedChanged.connect(self._on_tolerance_curve_rbtn_clicked)
        self.widget_tolerance_invert.checkedChanged.connect(self._on_tolerance_invert_rbtn_clicked)
        self.widget_keyClip_switchbtn.checkedChanged.connect(self._on_key_clip_switch_rbtn_clicked)
        self.widget_keyClip_curve_switchbtn.checkedChanged.connect(self._on_key_clip_curve_rbtn_clicked)

        self.spinBox_tolerance_min.setSuffix("%")
        self.spinBox_tolerance_max.setSuffix("%")
        self.spinBox_keyClip_min.setSuffix("%")
        self.spinBox_keyClip_max.setSuffix("%")
        self.spinBox_tolerance_min.setRange(0, 100)
        self.spinBox_tolerance_max.setRange(0, 100)
        self.spinBox_keyClip_min.setRange(0, 100)
        self.spinBox_keyClip_max.setRange(0, 100)

        self.rangeSlider_tolerance.setRange(0, 1000)
        self.rangeSlider_tolerance.setBarMovesAllHandles(False)
        # self.rangeSlider_tolerance.setValue([0, 1000])
        self.rangeSlider_tolerance.valueChanged.connect(self._on_tolerance_range_slider_value_changed)
        self.rangeSlider_keyClip.setRange(0, 1000)
        self.rangeSlider_keyClip.setBarMovesAllHandles(False)
        # self.rangeSlider_keyClip.setValue((200, 800))
        self.rangeSlider_keyClip.valueChanged.connect(self._on_key_clip_range_slider_value_changed)

        self.spinBox_tolerance_min.valueChanged.connect(lambda value : self.rangeSlider_tolerance.setValue((value*10, self.rangeSlider_tolerance.value()[1])))
        self.spinBox_tolerance_max.valueChanged.connect(lambda value : self.rangeSlider_tolerance.setValue((self.rangeSlider_tolerance.value()[0], value*10)))
        self.spinBox_keyClip_min.valueChanged.connect(lambda value : self.rangeSlider_keyClip.setValue((value*10, self.rangeSlider_keyClip.value()[1])))
        self.spinBox_keyClip_max.valueChanged.connect(lambda value : self.rangeSlider_keyClip.setValue((self.rangeSlider_keyClip.value()[0], value*10)))

        self.rangeSlider_tolerance.setProperty("type", "rangeslider")
        self.rangeSlider_keyClip.setProperty("type", "rangeslider")

        self.checkBox_status.stateChanged.connect(self._on_status_checkbox_clicked)
        # 设置默认不可用状态
        self.control_luma_status(False)

    def _on_status_checkbox_clicked(self, status):
        sender = self.sender()
        checked = sender.isChecked()
        if checked:
            logging.debug("Luma Status ON")
            self.checkBox_status.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Active", None))
            _args = {
                "Status": "On"
            }
            self.control_luma_status(True)
            self.check_tolerance_widget_status()
            self._parent.controller.set_luma_key(_args)
        else:
            logging.debug("Luma Status OFF")
            self.checkBox_status.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Inactive", None))
            _args = {
                "Status": "Off"
            }
            self.control_luma_status(False)
            self._parent.controller.set_luma_key(_args)

    def _select_fill_source(self, index):
        sender = self.sender()

        if self._luma_key_values["FillSourceComboBox"] == sender:
            if self._luma_key_values["FillSourceIndex"] != index:
                logging.debug("select FillSourceIndex:{}".format(index))
                self._luma_key_values["FillSourceIndex"] = index
                _args = {
                    "FillSource": Cue01Preferences.get_luma_video_src_by_index(index)
                }
                self._parent.controller.set_luma_fill_src(_args)

    def _on_tolerance_curve_rbtn_clicked(self, checked:bool):
        self.check_tolerance_widget_status()
        if checked:
            logging.debug("Tolerance Curve ON")
            _args = {
                "ToleranceCurve": "On"
            }
            self._parent.controller.set_luma_tolerance(_args)
        else:
            logging.debug("Tolerance Curve OFF")
            _args = {
                "ToleranceCurve": "Off"
            }
            self._parent.controller.set_luma_tolerance(_args)

    def _on_tolerance_invert_rbtn_clicked(self, checked:bool):
        self.check_tolerance_widget_status()
        if checked:
            logging.debug("Tolerance Invert ON")
            _args = {
                "ToleranceInvert": "On"
            }
            self._parent.controller.set_luma_tolerance(_args)
        else:
            logging.debug("Tolerance Invert OFF")
            _args = {
                "ToleranceInvert": "Off"
            }
            self._parent.controller.set_luma_tolerance(_args)

    def _on_tolerance_range_slider_value_changed(self, value):
        _tolerance_left = value[0]
        _tolerance_right = value[1]

        # self._luma_key_values["ToleranceLeftLabel"].setText("{}%".format(_tolerance_left/10.0))
        # self._luma_key_values["ToleranceRightLabel"].setText("{}%".format(_tolerance_right/10.0))
        self._luma_key_values["ToleranceLeftLabel"].setValue(_tolerance_left/10.0)
        self._luma_key_values["ToleranceRightLabel"].setValue(_tolerance_right/10.0)

        if self._luma_key_values["ToleranceLeftValue"] != _tolerance_left or self._luma_key_values["ToleranceRightValue"] != _tolerance_right:
            logging.debug("Tolerance Range:{}".format(value))

            self._luma_key_values["ToleranceLeftValue"] = _tolerance_left
            self._luma_key_values["ToleranceRightValue"] = _tolerance_right
            _args = {
                "ToleranceLeft": _tolerance_left,
                "ToleranceRight": _tolerance_right
            }
            self._parent.controller.set_luma_tolerance(_args)

    # def _on_tolerance_unit_step_spin_box_value_changed(self, value):
    #     logging.debug("Tolerance Unit Step:{}".format(value))
    #     _args = {
    #         "ToleranceUnitStep": value
    #     }
    #     self._parent.controller.set_luma_tolerance(_args)

    def _on_key_clip_switch_rbtn_clicked(self, checked:bool):
        if checked:
            logging.debug("Key Clip ON")
            _args = {
                "KeyClip": "On"
            }
            self.update_clip_widget_status(True)
            self._parent.controller.set_luma_key_clip(_args)
        else:
            logging.debug("Key Clip OFF")
            _args = {
                "KeyClip": "Off"
            }
            self.update_clip_widget_status(False)
            self._parent.controller.set_luma_key_clip(_args)

    def _on_key_clip_curve_rbtn_clicked(self, checked:bool):
        if checked:
            logging.debug("Key Clip Curve ON")
            _args = {
                "KeyClipCurve": "On"
            }
            self._parent.controller.set_luma_key_clip(_args)
        else:
            logging.debug("Key Clip Curve OFF")
            _args = {
                "KeyClipCurve": "Off"
            }
            self._parent.controller.set_luma_key_clip(_args)

    def _on_key_clip_range_slider_value_changed(self, value):
        _key_clip_left = value[0]
        _key_clip_right = value[1]

        # self._luma_key_values["KeyClipLeftLabel"].setText("{}%".format(_key_clip_left/10.0))
        # self._luma_key_values["KeyClipRightLabel"].setText("{}%".format(_key_clip_right/10.0))
        self._luma_key_values["KeyClipLeftLabel"].setValue(_key_clip_left/10.0)
        self._luma_key_values["KeyClipRightLabel"].setValue(_key_clip_right/10.0)

        if self._luma_key_values["KeyClipLeftValue"] != _key_clip_left or self._luma_key_values["KeyClipRightValue"] != _key_clip_right:
            logging.debug("Key Clip Range:{}".format(value))

            self._luma_key_values["KeyClipLeftValue"] = _key_clip_left
            self._luma_key_values["KeyClipRightValue"] = _key_clip_right
            _args = {
                "ClipLeft": _key_clip_left,
                "ClipRight": _key_clip_right
            }
            self._parent.controller.set_luma_key_clip(_args)
    
    def control_luma_status(self, status):
        toggle_layout_enable_or_disable(self.verticalLayout, status)
        if status: # 总体状态为Active，但还要检查子布局中的可能不可用的部分
            chroma_config.using_luma = True
            # self._parent.controller.update_luma_or_chroma_status("luma")
            self.check_tolerance_widget_status()
            if not self.widget_keyClip_switchbtn.checked:
                self.update_clip_widget_status(False)
            else:
                self.rangeSlider_keyClip.setStyleSheet(enalbed_range_slider_qss)
        else:
            chroma_config.using_luma = False
            # self.check_tolerance_widget_status() # 总开关导致全部关，不要检查子控件
            self.rangeSlider_tolerance.setStyleSheet(disabled_range_slider_qss)
            self.rangeSlider_keyClip.setStyleSheet(disabled_range_slider_qss)

    def check_tolerance_widget_status(self): # 检查并更新Tolerance相关控件是否可用，只有两个开关都是关闭状态才不可用
        if not self.widget_tolerance_curve.checked and not self.widget_tolerance_invert.checked:
            toggle_layout_enable_or_disable(self.horizontalLayout_4, False)
            # toggle_layout_enable_or_disable(self.horizontalLayout_5, False)
            self.rangeSlider_tolerance.setStyleSheet(disabled_range_slider_qss)
        else:
            toggle_layout_enable_or_disable(self.horizontalLayout_4, True)
            # toggle_layout_enable_or_disable(self.horizontalLayout_5, True)
            self.rangeSlider_tolerance.setStyleSheet(enalbed_range_slider_qss)

    def update_clip_widget_status(self, status): # 控制KeyClip相关控件是否可用
        if status:
            self.widget_keyClip_curve_switchbtn.setEnabled(True)
            toggle_layout_enable_or_disable(self.horizontalLayout_6, True)
            self.rangeSlider_keyClip.setStyleSheet(enalbed_range_slider_qss)
        else:
            self.widget_keyClip_curve_switchbtn.setEnabled(False)
            toggle_layout_enable_or_disable(self.horizontalLayout_6, False)
            self.rangeSlider_keyClip.setStyleSheet(disabled_range_slider_qss)

    def showEvent(self, event):
        self._parent.controller.get_luma()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_luma_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))

            _status = args["Status"]
            # _luma_video_src = args["VideoSource"]
            _tolerance_curve_switch = args["ToleranceCurveSwitch"]
            _tolerance_invert_switch = args["ToleranceInvertSwitch"]
            _tolerance_left = args["ToleranceLeft"]
            _tolerance_right = args["ToleranceRight"]
            _tolerance_unit_step = args["ToleranceUnitStep"]

            with QSignalBlocker(self.checkBox_status):
                if _status == 0: # 未使用
                    self.checkBox_status.setChecked(False)
                    self.checkBox_status.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Inactive", None))
                    self.control_luma_status(False)
                elif _status == 1: # 使用中
                    self.checkBox_status.setChecked(True)
                    self.checkBox_status.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Active", None))
                    self.control_luma_status(True)

            # _luma_video_src_index = Cue01Preferences.get_index_by_luma_video_src(_luma_video_src)
            # if _luma_video_src_index != 0xFF:
            #     self._luma_key_values["FillSourceIndex"] = _luma_video_src_index
            #     self._luma_key_values["FillSourceComboBox"].setCurrentIndex(_luma_video_src_index)

            if _tolerance_curve_switch == "On" or _tolerance_curve_switch == "ON":
                self._luma_key_values["ToleranceCurveSwitchButton"].set_checked(True)
            else:
                self._luma_key_values["ToleranceCurveSwitchButton"].set_checked(False)

            if _tolerance_invert_switch == "On" or _tolerance_invert_switch == "ON":
                self._luma_key_values["ToleranceInvertSwitchButton"].set_checked(True)
            else:
                self._luma_key_values["ToleranceInvertSwitchButton"].set_checked(False)
            
            self.check_tolerance_widget_status()

            if 0 <= _tolerance_left <= _tolerance_right and  _tolerance_right <= 1000:
                # 先同步变量的值，确保此处更新的值，不会触发设置
                self._luma_key_values["ToleranceLeftValue"] = _tolerance_left
                self._luma_key_values["ToleranceRightValue"] = _tolerance_right
                # 更新UI，其中setValue会触发回调，因此要确保先同步变量的值
                with QSignalBlocker(self._luma_key_values["ToleranceLeftLabel"]):
                    self._luma_key_values["ToleranceLeftLabel"].setValue(_tolerance_left/10.0)
                with QSignalBlocker(self._luma_key_values["ToleranceRightLabel"]):
                    self._luma_key_values["ToleranceRightLabel"].setValue(_tolerance_right/10.0)
                with QSignalBlocker(self._luma_key_values["ToleranceRangeSlider"]):
                    self._luma_key_values["ToleranceRangeSlider"].setValue((_tolerance_left, _tolerance_right))

            # if 0 <= _tolerance_unit_step <= 999:
            #     with QSignalBlocker(self._luma_key_values["ToleranceUnitStepSpinBox"]):
            #         self._luma_key_values["ToleranceUnitStepSpinBox"].setValue(_tolerance_unit_step)

            _key_clip_switch = args["ClipSwitch"]
            _key_clip_curve_switch = args["ClipCurveSwitch"]
            _key_clip_left = args["ClipLeft"]
            _key_clip_right = args["ClipRight"]

            if _key_clip_switch == "On" or _key_clip_switch == "ON":
                self._luma_key_values["KeyClipSwitchButton"].set_checked(True)
                self.update_clip_widget_status(True)
            else:
                self._luma_key_values["KeyClipSwitchButton"].set_checked(False)
                self.update_clip_widget_status(False)

            if _key_clip_curve_switch == "On" or _key_clip_curve_switch == "ON":
                self._luma_key_values["KeyClipCurveSwitchButton"].set_checked(True)
            else:
                self._luma_key_values["KeyClipCurveSwitchButton"].set_checked(False)

            if 0 <= _key_clip_left <= _key_clip_right and  _key_clip_right <= 1000:
                # 先同步变量的值，确保此处更新的值，不会触发设置
                self._luma_key_values["KeyClipLeftValue"] = _key_clip_left
                self._luma_key_values["KeyClipRightValue"] = _key_clip_right
                # 更新UI，其中setValue会触发回调，因此要确保先同步变量的值
                with QSignalBlocker(self._luma_key_values["KeyClipLeftLabel"]):
                    self._luma_key_values["KeyClipLeftLabel"].setValue(_key_clip_left/10.0)
                with QSignalBlocker(self._luma_key_values["KeyClipRightLabel"]):
                    self._luma_key_values["KeyClipRightLabel"].setValue(_key_clip_right/10.0)
                with QSignalBlocker(self._luma_key_values["KeyClipRangeSlider"]):
                    self._luma_key_values["KeyClipRangeSlider"].setValue((_key_clip_left, _key_clip_right))
        elif obj["function"] == "set_luma_fill_src":
            args = obj["args"]
            logging.debug("Set luma fill source args:{}".format(args))
        elif obj["function"] == "set_luma_tolerance":
            args = obj["args"]
            logging.debug("Set luma tolerance args:{}".format(args))
        elif obj["function"] == "set_luma_key_clip":
            args = obj["args"]
            logging.debug("Set luma key clip args:{}".format(args))


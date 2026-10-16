import logging

from PySide6.QtWidgets import QWidget, QAbstractSpinBox
from PySide6.QtCore import QSignalBlocker, Qt, QCoreApplication
from src.model.cue01.cue01Preferences import Cue01Preferences
from src.ui.cue01.dskWidget_ui import Ui_CUE01_DSK_Widget_Form
from globals import toggle_layout_enable_or_disable, enalbed_range_slider_qss, disabled_range_slider_qss

class DSKWidget(Ui_CUE01_DSK_Widget_Form, QWidget):
    def __init__(self, parent):
        super(DSKWidget, self).__init__(parent)
        self._parent = parent
        self.setupUi(self)

    def init_ui(self):
        _fill_srcs = Cue01Preferences.get_dsk_video_sources()

        self.comboBox_video_source.addItems(_fill_srcs)
        self.comboBox_video_source.currentIndexChanged[int].connect(self._select_fill_source)

        self.widget_invert_switchBtn.checkedChanged.connect(self._on_tolerance_invert_rbtn_clicked)

        self.rangeSlider_tolerance.setRange(0, 1000)
        self.rangeSlider_tolerance.setValue((0, 1000))
        self.rangeSlider_tolerance.setBarMovesAllHandles(False)
        self.rangeSlider_tolerance.valueChanged.connect(self._on_tolerance_range_slider_value_changed)

        # self.spinBox_unit_step.setRange(0, 999)
        # self.spinBox_unit_step.setValue(0)
        # self.spinBox_unit_step.setStepType(QAbstractSpinBox.DefaultStepType)
        # self.spinBox_unit_step.valueChanged.connect(self._on_tolerance_unit_step_spin_box_value_changed)

        self.widget_clip_switchBtn.checkedChanged.connect(self._on_dsk_clip_switch_rbtn_clicked)

        self.widget_curve_switchBtn.checkedChanged.connect(self._on_dsk_clip_curve_rbtn_clicked)

        self.rangeSlider_clip.setRange(0, 1000)
        self.rangeSlider_clip.setValue((200, 800))
        self.rangeSlider_clip.setBarMovesAllHandles(False)
        self.rangeSlider_clip.valueChanged.connect(self._on_dsk_clip_range_slider_value_changed)

        self.widget_pgm_level.slider.setRange(0, 1000)
        self.widget_pgm_level.spinbox.setRange(0, 100)
        self.widget_pgm_level.spinbox.setFixedWidth(60)
        # self.widget_pgm_level.slider.setSingleStep()
        self.widget_pgm_level.spinbox.setSingleStep(0.1)
        self.widget_pgm_level.slider.setValue(0)
        self.widget_pgm_level.slider.valueChanged.connect(self._on_dsk_clip_pgm_level_slider_value_changed)

        # self.widget_pvw_level.slider.setRange(0, 1000)
        # self.widget_pvw_level.spinbox.setRange(0, 100)
        # self.widget_pvw_level.spinbox.setSingleStep(0.1)
        # self.widget_pvw_level.slider.setValue(0)
        # self.widget_pvw_level.slider.valueChanged.connect(self._on_dsk_clip_pvw_level_slider_value_changed)

        self.widget_pip_switchBtn.checkedChanged.connect(self._on_dsk_pip_switch_rbtn_clicked)

        self.widget_pip_horizontal.slider.setRange(0, 100)
        self.widget_pip_horizontal.spinbox.setRange(0, 100)
        self.widget_pip_horizontal.slider.setValue(0)
        self.widget_pip_horizontal.slider.valueChanged.connect(self._on_dsk_pip_pos_hor_slider_value_changed)

        self.widget_pip_vertical.slider.setRange(0, 100)
        self.widget_pip_vertical.spinbox.setRange(0, 100)
        self.widget_pip_vertical.slider.setValue(0)
        self.widget_pip_vertical.slider.valueChanged.connect(self._on_dsk_pip_pos_ver_slider_value_changed)

        self.widget_pip_width.slider.setRange(0, 100)
        self.widget_pip_width.spinbox.setRange(0, 100)
        self.widget_pip_width.slider.setSingleStep(5)
        self.widget_pip_width.spinbox.setSingleStep(5)
        self.widget_pip_width.slider.setValue(0)
        self.widget_pip_width.slider.setSingleStep(5)
        self.widget_pip_width.slider.setPageStep(5)
        self.widget_pip_width.slider.valueChanged.connect(self._on_dsk_pip_width_slider_value_changed)

        self.widget_pip_height.slider.setRange(0, 100)
        self.widget_pip_height.spinbox.setRange(0, 100)
        self.widget_pip_height.slider.setSingleStep(5)
        self.widget_pip_height.spinbox.setSingleStep(5)
        self.widget_pip_height.slider.setValue(0)
        self.widget_pip_height.slider.setSingleStep(5)
        self.widget_pip_height.slider.setPageStep(5)
        self.widget_pip_height.slider.valueChanged.connect(self._on_dsk_pip_height_slider_value_changed)

        self.widget_mask_switchBtn.checkedChanged.connect(self._on_dsk_mask_switch_rbtn_clicked)

        self.widget_mask_top.slider.setRange(0, 360)
        self.widget_mask_top.spinbox.setRange(-9, 9)
        self.widget_mask_top.spinbox.setSingleStep(0.05)
        self.widget_mask_top.slider.setValue(0)
        self.widget_mask_top.slider.valueChanged.connect(self._on_dsk_mask_top_slider_value_changed)

        self.widget_mask_bottom.slider.setRange(0, 360)
        self.widget_mask_bottom.spinbox.setRange(-9, 9)
        self.widget_mask_bottom.spinbox.setSingleStep(0.05)
        self.widget_mask_bottom.slider.setValue(0)
        self.widget_mask_bottom.slider.valueChanged.connect(self._on_dsk_mask_bottom_slider_value_changed)

        self.widget_mask_left.slider.setRange(0, 640)
        self.widget_mask_left.spinbox.setRange(-16, 16)
        self.widget_mask_left.spinbox.setSingleStep(0.05)
        self.widget_mask_left.slider.setValue(0)
        self.widget_mask_left.slider.setSingleStep(5)
        self.widget_mask_left.slider.setPageStep(5)
        self.widget_mask_left.slider.valueChanged.connect(self._on_dsk_mask_left_slider_value_changed)

        self.widget_mask_right.slider.setRange(0, 640)
        self.widget_mask_right.spinbox.setRange(-16, 16)
        self.widget_mask_right.spinbox.setSingleStep(0.05)
        self.widget_mask_right.slider.setValue(0)
        self.widget_mask_right.slider.setSingleStep(5)
        self.widget_mask_right.slider.setPageStep(5)
        self.widget_mask_right.slider.valueChanged.connect(self._on_dsk_mask_right_slider_value_changed)

        self.spinBox_tolerance__min.setSuffix("%")
        self.spinBox_tolerance_max.setSuffix("%")
        self.spinBox_clip__min.setSuffix("%")
        self.spinBox_clip_max.setSuffix("%")
        # self.widget_pgm_level.spinbox.setSuffix("%")
        # self.widget_pvw_level.spinbox.setSuffix("%")
        self.widget_pip_horizontal.spinbox.setSuffix("%")
        self.widget_pip_vertical.spinbox.setSuffix("%")
        self.widget_pip_width.spinbox.setSuffix("%")
        self.widget_pip_height.spinbox.setSuffix("%")

        self.spinBox_tolerance__min.valueChanged.connect(lambda value : self.rangeSlider_tolerance.setValue((value*10, self.rangeSlider_tolerance.value()[1])))
        self.spinBox_tolerance_max.valueChanged.connect(lambda value : self.rangeSlider_tolerance.setValue((self.rangeSlider_tolerance.value()[0], value*10)))
        self.spinBox_clip__min.valueChanged.connect(lambda value : self.rangeSlider_clip.setValue((value*10, self.rangeSlider_clip.value()[1])))
        self.spinBox_clip_max.valueChanged.connect(lambda value : self.rangeSlider_clip.setValue((self.rangeSlider_clip.value()[0], value*10)))
        self.widget_pgm_level.spinbox.valueChanged.connect(lambda value : self.widget_pgm_level.slider.setValue(value*10))
        # self.widget_pvw_level.spinbox.valueChanged.connect(lambda value : self.widget_pvw_level.slider.setValue(value*10))
        self.widget_pip_horizontal.spinbox.valueChanged.connect(lambda value : self.widget_pip_horizontal.slider.setValue(int(value)))
        self.widget_pip_vertical.spinbox.valueChanged.connect(lambda value : self.widget_pip_vertical.slider.setValue(int(value)))
        self.widget_pip_width.spinbox.valueChanged.connect(lambda value : self.widget_pip_width.slider.setValue(int(value)))
        self.widget_pip_height.spinbox.valueChanged.connect(lambda value : self.widget_pip_height.slider.setValue(int(value)))
        self.widget_mask_top.spinbox.valueChanged.connect(lambda value : self.widget_mask_top.slider.setValue(int((value*100 + 900) / 5)))
        self.widget_mask_bottom.spinbox.valueChanged.connect(lambda value : self.widget_mask_bottom.slider.setValue(int((value*100 + 900) / 5)))
        self.widget_mask_left.spinbox.valueChanged.connect(lambda value : self.widget_mask_left.slider.setValue(int((value*100 + 1600) / 5)))
        self.widget_mask_right.spinbox.valueChanged.connect(lambda value : self.widget_mask_right.slider.setValue(int((value*100 + 1600) / 5)))

        """
        记录控件，以备更新UI
        """
        self._fill_src_value= {
            "FillSourceComboBox": self.comboBox_video_source,
            "FillSourceIndex": 0
        }
        self._dsk_tolerance_value = {
            "ToleranceInvertSwitchButton": self.widget_invert_switchBtn,
            "ToleranceLeftLabel": self.spinBox_tolerance__min,
            "ToleranceRightLabel": self.spinBox_tolerance_max,
            "ToleranceRangeSlider": self.rangeSlider_tolerance,
            "ToleranceLeftValue": 0,
            "ToleranceRightValue": 1000,
            # "ToleranceUnitStepSpinBox": self.spinBox_unit_step,
        }
        self._dsk_clip_value= {
            "DSKClipSwitchSwitchButton": self.widget_clip_switchBtn,
            "DSKClipCurveSwitchButton": self.widget_curve_switchBtn,
            "DSKClipLeftLabel": self.spinBox_clip__min,
            "DSKClipRightLabel": self.spinBox_clip_max,
            "DSKClipRangeSlider": self.rangeSlider_clip,
            "DSKClipLeftValue": 0,
            "DSKClipRightValue": 1000,
            "DSKClipPGMLevelSlider": self.widget_pgm_level.slider,
            "DSKClipPGMLevelLineEdit": self.widget_pgm_level.spinbox,
            "DSKClipPGMLevelValue": 0,
            # "DSKClipPVWLevelSlider": self.widget_pvw_level.slider,
            # "DSKClipPVWLevelLineEdit": self.widget_pvw_level.spinbox,
            "DSKClipPVWLevelValue": 0,
        }
        self._dsk_pip_value= {
            "DskPipSwitchSwitchButton": self.widget_pip_switchBtn,
            "DskPipPosHorSlider": self.widget_pip_horizontal.slider,
            "DskPipPosHorLineEdit": self.widget_pip_horizontal.spinbox,
            "DskPipPosHorValue": 0,
            "DskPipPosVerSlider": self.widget_pip_vertical.slider,
            "DskPipPosVerLineEdit": self.widget_pip_vertical.spinbox,
            "DskPipPosVerValue": 0,
            "DskPipWidthSlider": self.widget_pip_width.slider,
            "DskPipWidthLineEdit": self.widget_pip_width.spinbox,
            "DskPipWidthValue": 0,
            "DskPipHeightSlider": self.widget_pip_height.slider,
            "DskPipHeightLineEdit": self.widget_pip_height.spinbox,
            "DskPipHeightValue": 0,
        }
        self._dsk_mask_value= {
            "DskMaskSwitchSwitchButton": self.widget_mask_switchBtn,
            "DskMaskTopSlider": self.widget_mask_top.slider,
            "DskMaskTopLineEdit": self.widget_mask_top.spinbox,
            "DskMaskTopValue": 0,
            "DskMaskBottomSlider": self.widget_mask_bottom.slider,
            "DskMaskBottomLineEdit": self.widget_mask_bottom.spinbox,
            "DskMaskBottomValue": 0,
            "DskMaskLeftSlider": self.widget_mask_left.slider,
            "DskMaskLeftLineEdit": self.widget_mask_left.spinbox,
            "DskMaskLeftValue": 0,
            "DskMaskRightSlider": self.widget_mask_right.slider,
            "DskMaskRightLineEdit": self.widget_mask_right.spinbox,
            "DskMaskRightValue": 0,
        }
    
        # self.change_dsk_tolerance_status(False)
        self.change_dsk_clip_status(False)
        self.change_dsk_pip_status(False)
        self.change_dsk_mask_status(False)

    def retranslateUi(self, form):
        super().retranslateUi(form)

        _fill_srcs = Cue01Preferences.get_dsk_video_sources()

        _fill_src_cb = self.comboBox_video_source

        for i in range(len(_fill_srcs)):
            _item_text = QCoreApplication.translate("CUE01_DSK_Widget_Form", _fill_srcs[i], None)
            _fill_src_cb.setItemText(i, _item_text)

    # def change_dsk_tolerance_status(self, status:bool):
        # toggle_layout_enable_or_disable(self.horizontalLayout_4, status)
        # toggle_layout_enable_or_disable(self.horizontalLayout_5, status)
        # if status:
        #     self.rangeSlider_tolerance.setStyleSheet(enalbed_range_slider_qss)
        # else:
        #     self.rangeSlider_tolerance.setStyleSheet(disabled_range_slider_qss)

    def change_dsk_clip_status(self, status:bool):
        if not status:
            self.widget_curve_switchBtn.set_checked(False)
        toggle_layout_enable_or_disable(self.horizontalLayout_6, status)
        toggle_layout_enable_or_disable(self.horizontalLayout_7, status)
        # toggle_layout_enable_or_disable(self.horizontalLayout_8, status)
        toggle_layout_enable_or_disable(self.horizontalLayout_10, status)
        if status:
            self.rangeSlider_clip.setStyleSheet(enalbed_range_slider_qss)
        else:
            self.rangeSlider_clip.setStyleSheet(disabled_range_slider_qss)

    def change_dsk_pip_status(self, status:bool):
        toggle_layout_enable_or_disable(self.horizontalLayout_12, status)
        toggle_layout_enable_or_disable(self.horizontalLayout_13, status)
        toggle_layout_enable_or_disable(self.horizontalLayout_14, status)
        toggle_layout_enable_or_disable(self.horizontalLayout_15, status)

    def change_dsk_mask_status(self, status:bool):
        toggle_layout_enable_or_disable(self.horizontalLayout_17, status)
        toggle_layout_enable_or_disable(self.horizontalLayout_18, status)
        toggle_layout_enable_or_disable(self.horizontalLayout_19, status)
        toggle_layout_enable_or_disable(self.horizontalLayout_20, status)

    def _select_fill_source(self, index):
        sender = self.sender()

        if self._fill_src_value["FillSourceComboBox"] == sender:
            if self._fill_src_value["FillSourceIndex"] != index:
                logging.debug("select FillSourceIndex:{}".format(index))
                self._fill_src_value["FillSourceIndex"] = index
                _args = {
                    "FillSource": Cue01Preferences.get_dsk_video_src_by_index(index)
                }
                self._parent.controller.set_dsk_fill_src(_args)
    
    def _on_tolerance_invert_rbtn_clicked(self, checked: bool):
        if checked:
            logging.debug("Tolerance Invert ON")
            _args = {
                "ToleranceInvert": "On"
            }
            # self.change_dsk_tolerance_status(True)
            self._parent.controller.set_dsk_tolerance(_args)
        else:
            logging.debug("Tolerance Invert OFF")
            _args = {
                "ToleranceInvert": "Off"
            }
            # self.change_dsk_tolerance_status(False)
            self._parent.controller.set_dsk_tolerance(_args)

    def _on_tolerance_range_slider_value_changed(self, value):
        _tolerance_left = value[0]
        _tolerance_right = value[1]

        # self._dsk_tolerance_value["ToleranceLeftLabel"].setText("{}%".format(_tolerance_left/10.0))
        self._dsk_tolerance_value["ToleranceLeftLabel"].setValue(_tolerance_left/10.0)
        # self._dsk_tolerance_value["ToleranceRightLabel"].setText("{}%".format(_tolerance_right/10.0))
        self._dsk_tolerance_value["ToleranceRightLabel"].setValue(_tolerance_right/10.0)

        if self._dsk_tolerance_value["ToleranceLeftValue"] != _tolerance_left or self._dsk_tolerance_value["ToleranceRightValue"] != _tolerance_right:
            logging.debug("Tolerance Range:{}".format(value))

            self._dsk_tolerance_value["ToleranceLeftValue"] = _tolerance_left
            self._dsk_tolerance_value["ToleranceRightValue"] = _tolerance_right
            _args = {
                "ToleranceLeft": _tolerance_left,
                "ToleranceRight": _tolerance_right
            }
            self._parent.controller.set_dsk_tolerance(_args)

    def _on_tolerance_unit_step_spin_box_value_changed(self, value):
        logging.debug("Tolerance Unit Step:{}".format(value))
        _args = {
            "ToleranceUnitStep": value
        }
        self._parent.controller.set_dsk_tolerance(_args)
    
    def _on_dsk_clip_switch_rbtn_clicked(self, checked: bool):
        if checked:
            logging.debug("DSK Clip ON")
            _args = {
                "DSKClip": "On"
            }
            self.change_dsk_clip_status(True)
            self._parent.controller.set_dsk_clip(_args)
        else:
            logging.debug("DSK Clip OFF")
            _args = {
                "DSKClip": "Off"
            }
            self.change_dsk_clip_status(False)
            self._parent.controller.set_dsk_clip(_args)

    def _on_dsk_clip_curve_rbtn_clicked(self, checked: bool):
        if checked:
            logging.debug("DSK Clip Curve ON")
            _args = {
                "DSKClipCurve": "On"
            }
            self._parent.controller.set_dsk_clip(_args)
        else:
            logging.debug("DSK Clip Curve OFF")
            _args = {
                "DSKClipCurve": "Off"
            }
            self._parent.controller.set_dsk_clip(_args)

    def _on_dsk_clip_range_slider_value_changed(self, value):
        _dsk_clip_left = value[0]
        _dsk_clip_right = value[1]

        # self._dsk_clip_value["DSKClipLeftLabel"].setText("{}%".format(_dsk_clip_left/10.0))
        # self._dsk_clip_value["DSKClipRightLabel"].setText("{}%".format(_dsk_clip_right/10.0))
        with QSignalBlocker(self._dsk_clip_value["DSKClipLeftLabel"]):
            self._dsk_clip_value["DSKClipLeftLabel"].setValue(_dsk_clip_left/10.0)
        
        with QSignalBlocker(self._dsk_clip_value["DSKClipRightLabel"]):
            self._dsk_clip_value["DSKClipRightLabel"].setValue(_dsk_clip_right/10.0)

        if self._dsk_clip_value["DSKClipLeftValue"] != _dsk_clip_left or self._dsk_clip_value["DSKClipRightValue"] != _dsk_clip_right:
            logging.debug("DSK Clip Range:{}".format(value))

            self._dsk_clip_value["DSKClipLeftValue"] = _dsk_clip_left
            self._dsk_clip_value["DSKClipRightValue"] = _dsk_clip_right
            _args = {
                "ClipLeft": _dsk_clip_left,
                "ClipRight": _dsk_clip_right
            }
            self._parent.controller.set_dsk_clip(_args)
    
    def _on_dsk_clip_pgm_level_slider_value_changed(self, value):
        if self._dsk_clip_value["DSKClipPGMLevelValue"] != value:
            # self._dsk_clip_value["DSKClipPGMLevelLineEdit"].setText("{}%".format(value/10.0))
            self._dsk_clip_value["DSKClipPGMLevelLineEdit"].setValue(value/10.0)
            self._dsk_clip_value["DSKClipPGMLevelValue"] = value
            _args = {
                "DSKClipPGM": value
            }
            self._parent.controller.set_dsk_clip(_args)
    
    # def _on_dsk_clip_pvw_level_slider_value_changed(self, value):
    #     if self._dsk_clip_value["DSKClipPVWLevelValue"] != value:
    #         # self._dsk_clip_value["DSKClipPVWLevelLineEdit"].setText("{}%".format(value/10.0))
    #         self._dsk_clip_value["DSKClipPVWLevelLineEdit"].setValue(value/10.0)
    #         self._dsk_clip_value["DSKClipPVWLevelValue"] = value
    #         _args = {
    #             "DSKClipPVW": value
    #         }
    #         self._parent.controller.set_dsk_clip(_args)
    
    def _on_dsk_pip_switch_rbtn_clicked(self, checked:bool):
        if checked:
            logging.debug("DSK PIP ON")
            _args = {
                "DskPipSwitch": "On"
            }
            self.change_dsk_pip_status(True)
            self._parent.controller.set_dsk_pip(_args)
        else:
            logging.debug("DSK PIP OFF")
            _args = {
                "DskPipSwitch": "Off"
            }
            self.change_dsk_pip_status(False)
            self._parent.controller.set_dsk_pip(_args)   
        
    def _on_dsk_pip_pos_hor_slider_value_changed(self, value):
        if self._dsk_pip_value["DskPipPosHorValue"] != value:
            # self._dsk_pip_value["DskPipPosHorLineEdit"].setText("{}%".format(value*1.0))
            self._dsk_pip_value["DskPipPosHorLineEdit"].setValue(value*1.0)
            self._dsk_pip_value["DskPipPosHorValue"] = value
            _args = {
                "DskPipPosHor": value
            }
            self._parent.controller.set_dsk_pip(_args)
    
    def _on_dsk_pip_pos_ver_slider_value_changed(self, value):
        if self._dsk_pip_value["DskPipPosVerValue"] != value:
            # self._dsk_pip_value["DskPipPosVerLineEdit"].setText("{}%".format(value*1.0))
            self._dsk_pip_value["DskPipPosVerLineEdit"].setValue(value*1.0)
            self._dsk_pip_value["DskPipPosVerValue"] = value
            _args = {
                "DskPipPosVer": value
            }
            self._parent.controller.set_dsk_pip(_args)
    
    def _on_dsk_pip_width_slider_value_changed(self, value):
        if self._dsk_pip_value["DskPipWidthValue"] != value:
            # self._dsk_pip_value["DskPipWidthLineEdit"].setText("{}%".format(value*1.0))
            self._dsk_pip_value["DskPipWidthLineEdit"].setValue(value*1.0)
            self._dsk_pip_value["DskPipWidthValue"] = value
            _args = {
                "DskPipWidth": value
            }
            self._parent.controller.set_dsk_pip(_args)
    
    def _on_dsk_pip_height_slider_value_changed(self, value):
        if self._dsk_pip_value["DskPipHeightValue"] != value:
            # self._dsk_pip_value["DskPipHeightLineEdit"].setText("{}%".format(value*1.0))
            self._dsk_pip_value["DskPipHeightLineEdit"].setValue(value*1.0)
            self._dsk_pip_value["DskPipHeightValue"] = value
            _args = {
                "DskPipHeight": value
            }
            self._parent.controller.set_dsk_pip(_args)

    def _on_dsk_mask_switch_rbtn_clicked(self, checked:bool):
        if checked:
            logging.debug("DSK Mask ON")
            _args = {
                "DskMaskSwitch": "On"
            }
            self.change_dsk_mask_status(True)
            self._parent.controller.set_dsk_mask(_args)
        else:
            logging.debug("DSK Mask OFF")
            _args = {
                "DskMaskSwitch": "Off"
            }
            self.change_dsk_mask_status(False)
            self._parent.controller.set_dsk_mask(_args)   
        
    def _on_dsk_mask_top_slider_value_changed(self, value):
        if self._dsk_mask_value["DskMaskTopValue"] != value:
            # self._dsk_mask_value["DskMaskTopLineEdit"].setText("{}".format((value*5 - 900)/100.0))
            self._dsk_mask_value["DskMaskTopLineEdit"].setValue((value*5 - 900)/100.0)
            self._dsk_mask_value["DskMaskTopValue"] = value
            _args = {
                "DskMaskTop": (value*5)
            }
            self._parent.controller.set_dsk_mask(_args)
    
    def _on_dsk_mask_bottom_slider_value_changed(self, value):
        if self._dsk_mask_value["DskMaskBottomValue"] != value:
            # self._dsk_mask_value["DskMaskBottomLineEdit"].setText("{}".format((value*5 - 900)/100.0))
            self._dsk_mask_value["DskMaskBottomLineEdit"].setValue((value*5 - 900)/100.0)
            self._dsk_mask_value["DskMaskBottomValue"] = value
            _args = {
                "DskMaskBottom": (value*5)
            }
            self._parent.controller.set_dsk_mask(_args)
    
    def _on_dsk_mask_left_slider_value_changed(self, value):
        if self._dsk_mask_value["DskMaskLeftValue"] != value:
            # self._dsk_mask_value["DskMaskLeftLineEdit"].setText("{}".format((value*5 - 1600)/100.0))
            self._dsk_mask_value["DskMaskLeftLineEdit"].setValue((value*5 - 1600)/100.0)
            self._dsk_mask_value["DskMaskLeftValue"] = value
            _args = {
                "DskMaskLeft": (value*5)
            }
            self._parent.controller.set_dsk_mask(_args)
    
    def _on_dsk_mask_right_slider_value_changed(self, value):
        if self._dsk_mask_value["DskMaskRightValue"] != value:
            # self._dsk_mask_value["DskMaskRightLineEdit"].setText("{}".format((value*5 - 1600)/100.0))
            self._dsk_mask_value["DskMaskRightLineEdit"].setValue((value*5 - 1600)/100.0)
            self._dsk_mask_value["DskMaskRightValue"] = value
            _args = {
                "DskMaskRight": (value*5)
            }
            self._parent.controller.set_dsk_mask(_args)
    
    def showEvent(self, event):
        self._parent.controller.get_dsk()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_dsk_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))

            _dsk_video_src = args["VideoSource"]

            _dsk_video_src_index = Cue01Preferences.get_index_by_dsk_video_src(_dsk_video_src)
            if _dsk_video_src_index != 0xFF:
                self._fill_src_value["FillSourceIndex"] = _dsk_video_src_index
                self._fill_src_value["FillSourceComboBox"].setCurrentIndex(_dsk_video_src_index)

            # DSK Tolerance
            _tolerance_invert_switch = args["ToleranceInvertSwitch"]
            _tolerance_left = args["ToleranceLeft"]
            _tolerance_right = args["ToleranceRight"]
            _tolerance_unit_step = args["ToleranceUnitStep"]

            if _tolerance_invert_switch == "On" or _tolerance_invert_switch == "ON":
                # self.change_dsk_tolerance_status(True)
                self._dsk_tolerance_value["ToleranceInvertSwitchButton"].set_checked(True)
            else:
                # self.change_dsk_tolerance_status(False)
                self._dsk_tolerance_value["ToleranceInvertSwitchButton"].set_checked(False)

            if 0 <= _tolerance_left <= _tolerance_right and  _tolerance_right <= 1000:
                # 先同步变量的值，确保此处更新的值，不会触发设置
                self._dsk_tolerance_value["ToleranceLeftValue"] = _tolerance_left
                self._dsk_tolerance_value["ToleranceRightValue"] = _tolerance_right
                # 更新UI，其中setValue会触发回调，因此要确保先同步变量的值
                # self._dsk_tolerance_value["ToleranceLeftLabel"].setText("{}%".format(_tolerance_left/10.0))
                self._dsk_tolerance_value["ToleranceLeftLabel"].setValue(_tolerance_left/10.0)
                # self._dsk_tolerance_value["ToleranceRightLabel"].setText("{}%".format(_tolerance_right/10.0))
                self._dsk_tolerance_value["ToleranceRightLabel"].setValue(_tolerance_right/10.0)
                self._dsk_tolerance_value["ToleranceRangeSlider"].setValue((_tolerance_left, _tolerance_right))

            # if 0 <= _tolerance_unit_step <= 999:
            #     self._dsk_tolerance_value["ToleranceUnitStepSpinBox"].setValue(_tolerance_unit_step)

            _dsk_clip_switch = args["ClipSwitch"]
            _dsk_clip_curve_switch = args["ClipCurveSwitch"]
            _dsk_clip_left = args["ClipLeft"]
            _dsk_clip_right = args["ClipRight"]
            _dsk_clip_pgm_level = args["ClipPGMLevel"]
            # _dsk_clip_pvw_level = args["ClipPVWLevel"]

            if _dsk_clip_curve_switch == "On" or _dsk_clip_curve_switch == "ON":
                self._dsk_clip_value["DSKClipCurveSwitchButton"].set_checked(True)
            else:
                self._dsk_clip_value["DSKClipCurveSwitchButton"].set_checked(False)

            if _dsk_clip_switch == "On" or _dsk_clip_switch == "ON":
                self.change_dsk_clip_status(True)
                self._dsk_clip_value["DSKClipSwitchSwitchButton"].set_checked(True)
            else:
                self.change_dsk_clip_status(False)
                self._dsk_clip_value["DSKClipSwitchSwitchButton"].set_checked(False)

            if 0 <= _dsk_clip_left <= _dsk_clip_right and  _dsk_clip_right <= 1000:
                # 先同步变量的值，确保此处更新的值，不会触发设置
                self._dsk_clip_value["DSKClipLeftValue"] = _dsk_clip_left
                self._dsk_clip_value["DSKClipRightValue"] = _dsk_clip_right
                # 更新UI，其中setValue会触发回调，因此要确保先同步变量的值
                # self._dsk_clip_value["DSKClipLeftLabel"].setText("{}%".format(_dsk_clip_left/10.0))
                # self._dsk_clip_value["DSKClipRightLabel"].setText("{}%".format(_dsk_clip_right/10.0))
                self._dsk_clip_value["DSKClipLeftLabel"].setValue(_dsk_clip_left/10.0)
                self._dsk_clip_value["DSKClipRightLabel"].setValue(_dsk_clip_right/10.0)
                self._dsk_clip_value["DSKClipRangeSlider"].setValue((_dsk_clip_left, _dsk_clip_right))
            
            if 0 <= _dsk_clip_pgm_level <= 1000:
                self._dsk_clip_value["DSKClipPGMLevelValue"] = _dsk_clip_pgm_level
                # self._dsk_clip_value["DSKClipPGMLevelLineEdit"].setText("{}%".format(_dsk_clip_pgm_level/10.0))
                self._dsk_clip_value["DSKClipPGMLevelLineEdit"].setValue(_dsk_clip_pgm_level/10.0)
                self._dsk_clip_value["DSKClipPGMLevelSlider"].setValue(_dsk_clip_pgm_level)
            
            # if 0 <= _dsk_clip_pvw_level <= 1000:
            #     self._dsk_clip_value["DSKClipPVWLevelValue"] = _dsk_clip_pvw_level
            #     # self._dsk_clip_value["DSKClipPVWLevelLineEdit"].setText("{}%".format(_dsk_clip_pvw_level/10.0))
            #     self._dsk_clip_value["DSKClipPVWLevelLineEdit"].setValue(_dsk_clip_pvw_level/10.0)
            #     self._dsk_clip_value["DSKClipPVWLevelSlider"].setValue(_dsk_clip_pvw_level)
            
            # DSK PIP
            _pip_switch = args["PipSwitch"]
            _pip_pos_h = args["PipHPos"]
            _pip_pos_v = args["PipVPos"]
            _pip_width = args["PipWidth"]
            _pip_height = args["PipHeight"]

            if _pip_switch == "On" or _pip_switch == "ON":
                self.change_dsk_pip_status(True)
                self._dsk_pip_value["DskPipSwitchSwitchButton"].set_checked(True)
            else:
                self.change_dsk_pip_status(False)
                self._dsk_pip_value["DskPipSwitchSwitchButton"].set_checked(False)
            
            if 0 <= _pip_pos_h <= 100:
                self._dsk_pip_value["DskPipPosHorValue"] = _pip_pos_h
                # self._dsk_pip_value["DskPipPosHorLineEdit"].setText("{}%".format(_pip_pos_h*1.0))
                self._dsk_pip_value["DskPipPosHorLineEdit"].setValue(_pip_pos_h*1.0)
                self._dsk_pip_value["DskPipPosHorSlider"].setValue(_pip_pos_h*1.0)
            
            if 0 <= _pip_pos_v <= 100:
                self._dsk_pip_value["DskPipPosVerValue"] = _pip_pos_v
                # self._dsk_pip_value["DskPipPosVerLineEdit"].setText("{}%".format(_pip_pos_v*1.0))
                self._dsk_pip_value["DskPipPosVerLineEdit"].setValue(_pip_pos_v*1.0)
                self._dsk_pip_value["DskPipPosVerSlider"].setValue(_pip_pos_v*1.0)
            
            if 0 <= _pip_width <= 100:
                self._dsk_pip_value["DskPipWidthValue"] = _pip_width
                # self._dsk_pip_value["DskPipWidthLineEdit"].setText("{}%".format(_pip_width*1.0))
                self._dsk_pip_value["DskPipWidthLineEdit"].setValue(_pip_width*1.0)
                self._dsk_pip_value["DskPipWidthSlider"].setValue(_pip_width*1.0)

            if 0 <= _pip_height <= 100:
                self._dsk_pip_value["DskPipHeightValue"] = _pip_height
                # self._dsk_pip_value["DskPipHeightLineEdit"].setText("{}%".format(_pip_height*1.0))
                self._dsk_pip_value["DskPipHeightLineEdit"].setValue(_pip_height*1.0)
                self._dsk_pip_value["DskPipHeightSlider"].setValue(_pip_height*1.0)

            _mask_switch = args["MaskSwitch"]
            _mask_top = args["MaskTop"]
            _mask_bottom = args["MaskBottom"]
            _mask_left = args["MaskLeft"]
            _mask_right = args["MaskRight"]

            if _mask_switch == "On" or _mask_switch == "ON":
                self.change_dsk_mask_status(True)
                self._dsk_mask_value["DskMaskSwitchSwitchButton"].set_checked(True)
            else:
                self.change_dsk_mask_status(False)
                self._dsk_mask_value["DskMaskSwitchSwitchButton"].set_checked(False)
            
            if 0 <= _mask_top <= 1800:
                self._dsk_mask_value["DskMaskTopValue"] = int(_mask_top/5)
                # self._dsk_mask_value["DskMaskTopLineEdit"].setText("{}".format((_mask_top - 900)/100.0))
                self._dsk_mask_value["DskMaskTopLineEdit"].setValue((_mask_top - 900)/100.0)
                self._dsk_mask_value["DskMaskTopSlider"].setValue(int(_mask_top/5))
            
            if 0 <= _mask_bottom <= 1800:
                self._dsk_mask_value["DskMaskBottomValue"] = int(_mask_bottom/5)
                # self._dsk_mask_value["DskMaskBottomLineEdit"].setText("{}".format((_mask_bottom - 900)/100.0))
                self._dsk_mask_value["DskMaskBottomLineEdit"].setValue((_mask_bottom - 900)/100.0)
                self._dsk_mask_value["DskMaskBottomSlider"].setValue(int(_mask_bottom/5))
            
            if 0 <= _mask_left <= 3200:
                self._dsk_mask_value["DskMaskLeftValue"] = int(_mask_left/5)
                # self._dsk_mask_value["DskMaskLeftLineEdit"].setText("{}".format((_mask_left - 1600)/100.0))
                self._dsk_mask_value["DskMaskLeftLineEdit"].setValue((_mask_left - 1600)/100.0)
                self._dsk_mask_value["DskMaskLeftSlider"].setValue(int(_mask_left/5))

            if 0 <= _mask_right <= 3200:
                self._dsk_mask_value["DskMaskRightValue"] = int(_mask_right/5)
                # self._dsk_mask_value["DskMaskRightLineEdit"].setText("{}".format((_mask_right - 1600)/100.0))
                self._dsk_mask_value["DskMaskRightLineEdit"].setValue((_mask_right - 1600)/100.0)
                self._dsk_mask_value["DskMaskRightSlider"].setValue(int(_mask_right/5))

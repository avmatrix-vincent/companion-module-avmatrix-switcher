import os, sys, logging
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtWidgets import QWidget, QApplication, QButtonGroup, QSizePolicy, QSpacerItem
from src.ui.cue01.uskWidget_ui import Ui_CUE01_USK_Widget_Form
from globals import toggle_layout_visibility, toggle_layout_enable_or_disable

class USKWidget(Ui_CUE01_USK_Widget_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.setupUi(self)

    def init_ui(self):

        # 隐藏USK Edge
        self.radio_main_widget.hide()
        toggle_layout_visibility(self.horizontalLayout_5, False)
        # toggle_layout_visibility(self.verticalLayout_3, False)

        # 添加弹簧使各滑块之间垂直间隔减小
        self.verticalLayout_4.insertItem(0, QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum))
        self.verticalLayout_4.insertItem(4, QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum))
        self.verticalLayout_4.addSpacerItem(QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Maximum))

        self.widget_pip_hori.slider.setRange(0, 100)
        self.widget_pip_hori.spinbox.setRange(0, 100)
        self.widget_pip_verti.slider.setRange(0, 100)
        self.widget_pip_verti.spinbox.setRange(0, 100)
        self.widget_pip_width.slider.setRange(1, 100)
        self.widget_pip_width.spinbox.setRange(1, 100)
        self.widget_pip_height.slider.setRange(1, 100)
        self.widget_pip_height.spinbox.setRange(1, 100)
        self.widget_mask_top.slider.setRange(0, 360)
        self.widget_mask_top.spinbox.setRange(-9, 9)
        self.widget_mask_bottom.slider.setRange(0, 360)
        self.widget_mask_bottom.spinbox.setRange(-9, 9)
        self.widget_mask_left.slider.setRange(0, 640)
        self.widget_mask_left.spinbox.setRange(-16, 16)
        self.widget_mask_right.slider.setRange(0, 640)
        self.widget_mask_right.spinbox.setRange(-16, 16)

        self.widget_pip_width.slider.setSingleStep(5)
        self.widget_pip_width.spinbox.setSingleStep(5)
        self.widget_pip_height.slider.setSingleStep(5)
        self.widget_pip_height.spinbox.setSingleStep(5)
        self.widget_mask_top.slider.setSingleStep(0.05)
        self.widget_mask_top.spinbox.setSingleStep(0.05)
        self.widget_mask_bottom.slider.setSingleStep(0.05)
        self.widget_mask_bottom.spinbox.setSingleStep(0.05)
        self.widget_mask_left.slider.setSingleStep(0.05)
        self.widget_mask_left.spinbox.setSingleStep(0.05)
        self.widget_mask_right.slider.setSingleStep(0.05)
        self.widget_mask_right.spinbox.setSingleStep(0.05)

        _usk_edge_stage1_rbtn_group = QButtonGroup(self.widget_radios_goup_1)
        _usk_edge_stage1_rbtn_group.addButton(self.radioButton_stage_1_off)
        _usk_edge_stage1_rbtn_group.addButton(self.radioButton_stage_1_erode_3)
        _usk_edge_stage1_rbtn_group.addButton(self.radioButton_stage_1_erode_5)
        _usk_edge_stage1_rbtn_group.addButton(self.radioButton_stage_1_dilate_3)
        _usk_edge_stage1_rbtn_group.addButton(self.radioButton_stage_1_dilate_5)
        _usk_edge_stage1_rbtn_group.addButton(self.radioButton_stage1_gaussian3)
        _usk_edge_stage1_rbtn_group.addButton(self.radioButton_stage1_gaussian5)
        _usk_edge_stage1_rbtn_group.buttonClicked.connect(self._on_usk_edge_stage1_rbtn_clicked)
        _usk_edge_stage2_rbtn_group = QButtonGroup(self.widget_radios_group_2)
        _usk_edge_stage2_rbtn_group.addButton(self.radioButton_stage_2_off)
        _usk_edge_stage2_rbtn_group.addButton(self.radioButton_stage2_erode3)
        _usk_edge_stage2_rbtn_group.addButton(self.radioButton_stage2_erode5)
        _usk_edge_stage2_rbtn_group.addButton(self.radioButton_stage2_dilate3)
        _usk_edge_stage2_rbtn_group.addButton(self.radioButton_stage2_dilate5)
        _usk_edge_stage2_rbtn_group.addButton(self.radioButton_stage2_gaussian3)
        _usk_edge_stage2_rbtn_group.addButton(self.radioButton_stage2_gaussian5)
        _usk_edge_stage2_rbtn_group.buttonClicked.connect(self._on_usk_edge_stage2_rbtn_clicked)
        self._usk_pip_value= {
            "UskPipSwitchButton": self.widget_pip_switchbtn,
            "UskPipPosHorSlider": self.widget_pip_hori.slider,
            "UskPipPosHorLineEdit": self.widget_pip_hori.spinbox,
            "UskPipPosHorValue": 0,
            "UskPipPosVerSlider": self.widget_pip_verti.slider,
            "UskPipPosVerLineEdit": self.widget_pip_verti.spinbox,
            "UskPipPosVerValue": 0,
            "UskPipWidthSlider": self.widget_pip_width.slider,
            "UskPipWidthLineEdit": self.widget_pip_width.spinbox,
            "UskPipWidthValue": 0,
            "UskPipHeightSlider": self.widget_pip_height.slider,
            "UskPipHeightLineEdit": self.widget_pip_height.spinbox,
            "UskPipHeightValue": 0,
        }
        self._usk_mask_value= {
            "UskMaskSwitchButton": self.widget_mask_switchbtn,
            "UskMaskTopSlider": self.widget_mask_top.slider,
            "UskMaskTopLineEdit": self.widget_mask_top.spinbox,
            "UskMaskTopValue": 0,
            "UskMaskBottomSlider": self.widget_mask_bottom.slider,
            "UskMaskBottomLineEdit": self.widget_mask_bottom.spinbox,
            "UskMaskBottomValue": 0,
            "UskMaskLeftSlider": self.widget_mask_left.slider,
            "UskMaskLeftLineEdit": self.widget_mask_left.spinbox,
            "UskMaskLeftValue": 0,
            "UskMaskRightSlider": self.widget_mask_right.slider,
            "UskMaskRightLineEdit": self.widget_mask_right.spinbox,
            "UskMaskRightValue": 0,
        }
        self._usk_edge_value = {
            "UskEdgeStage1OffRadio": self.radioButton_stage_1_off,
            "UskEdgeStage1Erode3x3Radio": self.radioButton_stage_1_erode_3,
            "UskEdgeStage1Erode5x5Radio": self.radioButton_stage_1_erode_5,
            "UskEdgeStage1Dilate3x3Radio": self.radioButton_stage_1_dilate_3,
            "UskEdgeStage1Dilate5x5Radio": self.radioButton_stage_1_dilate_5,
            "UskEdgeStage1Gaussian3x3Radio": self.radioButton_stage1_gaussian3,
            "UskEdgeStage1Gaussian5x5Radio": self.radioButton_stage1_gaussian5,
            "UskEdgeStage2OffRadio": self.radioButton_stage_2_off,
            "UskEdgeStage2Erode3x3Radio": self.radioButton_stage2_erode3,
            "UskEdgeStage2Erode5x5Radio": self.radioButton_stage2_erode5,
            "UskEdgeStage2Dilate3x3Radio": self.radioButton_stage2_dilate3,
            "UskEdgeStage2Dilate5x5Radio": self.radioButton_stage2_dilate5,
            "UskEdgeStage2Gaussian3x3Radio": self.radioButton_stage2_gaussian3,
            "UskEdgeStage2Gaussian5x5Radio": self.radioButton_stage2_gaussian5,
        }

        self.widget_pip_switchbtn.checkedChanged.connect(self._on_usk_pip_switch_rbtn_clicked)
        self.widget_pip_hori.slider.valueChanged.connect(self._on_usk_pip_pos_hor_slider_value_changed)
        self.widget_pip_verti.slider.valueChanged.connect(self._on_usk_pip_pos_ver_slider_value_changed)
        self.widget_pip_width.slider.valueChanged.connect(self._on_usk_pip_width_slider_value_changed)
        self.widget_pip_height.slider.valueChanged.connect(self._on_usk_pip_height_slider_value_changed)
        self.widget_pip_hori.spinbox.valueChanged.connect(lambda value : self.widget_pip_hori.slider.setValue(int(value)))
        self.widget_pip_verti.spinbox.valueChanged.connect(lambda value : self.widget_pip_verti.slider.setValue(int(value)))
        self.widget_pip_width.spinbox.valueChanged.connect(lambda value : self.widget_pip_width.slider.setValue(int(value)))
        self.widget_pip_height.spinbox.valueChanged.connect(lambda value : self.widget_pip_height.slider.setValue(int(value)))
        self.widget_mask_top.spinbox.valueChanged.connect(lambda value : self.widget_mask_top.slider.setValue(int((value*100 + 900) / 5)))
        self.widget_mask_bottom.spinbox.valueChanged.connect(lambda value : self.widget_mask_bottom.slider.setValue(int((value*100 + 900) / 5)))
        self.widget_mask_left.spinbox.valueChanged.connect(lambda value : self.widget_mask_left.slider.setValue(int((value*100 + 1600) / 5)))
        self.widget_mask_right.spinbox.valueChanged.connect(lambda value : self.widget_mask_right.slider.setValue(int((value*100 + 1600) / 5)))

        self.widget_mask_switchbtn.checkedChanged.connect(self._on_usk_mask_switch_rbtn_clicked)
        self.widget_mask_top.slider.valueChanged.connect(self._on_usk_mask_top_slider_value_changed)
        self.widget_mask_bottom.slider.valueChanged.connect(self._on_usk_mask_bottom_slider_value_changed)
        self.widget_mask_left.slider.valueChanged.connect(self._on_usk_mask_left_slider_value_changed)
        self.widget_mask_right.slider.valueChanged.connect(self._on_usk_mask_right_slider_value_changed)

        self.line.setProperty("type", "title_line")
        self.line_2.setProperty("type", "title_line")
        self.line_3.setProperty("type", "title_line")
        self.line_4.setProperty("type", "title_line")
        self.line_5.setProperty("type", "title_line")
        self.line_6.setProperty("type", "title_line")

        self.label.setProperty("type", "title")
        self.label_2.setProperty("type", "title")
        self.label_5.setProperty("type", "title")

        self.widget_pip_hori.spinbox.setSuffix("%")
        self.widget_pip_verti.spinbox.setSuffix("%")
        self.widget_pip_width.spinbox.setSuffix("%")
        self.widget_pip_height.spinbox.setSuffix("%")

        if self.widget_pip_switchbtn.checked:
            toggle_layout_enable_or_disable(self.gridLayout_3, True)
        else:
            toggle_layout_enable_or_disable(self.gridLayout_3, False)
        if self.widget_mask_switchbtn.checked:
            toggle_layout_enable_or_disable(self.gridLayout_4, True)
        else:
            toggle_layout_enable_or_disable(self.gridLayout_4, False)

    
    def _on_usk_pip_switch_rbtn_clicked(self, checked: bool):
        if checked:
            logging.debug("USK PIP ON")
            _args = {
                "UskPipSwitch": "On"
            }
            toggle_layout_enable_or_disable(self.gridLayout_3, True)
            self._parent.controller.set_usk_pip(_args)
        else:
            logging.debug("USK PIP OFF")
            _args = {
                "UskPipSwitch": "Off"
            }
            toggle_layout_enable_or_disable(self.gridLayout_3, False)
            self._parent.controller.set_usk_pip(_args)   
        
    def _on_usk_pip_pos_hor_slider_value_changed(self, value):
        if self._usk_pip_value["UskPipPosHorValue"] != value:
            # self._usk_pip_value["UskPipPosHorLineEdit"].setText("{}%".format(value*1.0))
            self._usk_pip_value["UskPipPosHorLineEdit"].setValue(value*1.0)
            self._usk_pip_value["UskPipPosHorValue"] = value
            _args = {
                "UskPipPosHor": value
            }
            self._parent.controller.set_usk_pip(_args)
    
    def _on_usk_pip_pos_ver_slider_value_changed(self, value):
        if self._usk_pip_value["UskPipPosVerValue"] != value:
            # self._usk_pip_value["UskPipPosVerLineEdit"].setText("{}%".format(value*1.0))
            self._usk_pip_value["UskPipPosVerLineEdit"].setValue(value*1.0)
            self._usk_pip_value["UskPipPosVerValue"] = value
            _args = {
                "UskPipPosVer": value
            }
            self._parent.controller.set_usk_pip(_args)
    
    def _on_usk_pip_width_slider_value_changed(self, value):
        if self._usk_pip_value["UskPipWidthValue"] != value:
            # self._usk_pip_value["UskPipWidthLineEdit"].setText("{}%".format(value*1.0))
            self._usk_pip_value["UskPipWidthLineEdit"].setValue(value*1.0)
            self._usk_pip_value["UskPipWidthValue"] = value
            _args = {
                "UskPipWidth": value
            }
            self._parent.controller.set_usk_pip(_args)
    
    def _on_usk_pip_height_slider_value_changed(self, value):
        if self._usk_pip_value["UskPipHeightValue"] != value:
            # self._usk_pip_value["UskPipHeightLineEdit"].setText("{}%".format(value*1.0))
            self._usk_pip_value["UskPipHeightLineEdit"].setValue(value*1.0)
            self._usk_pip_value["UskPipHeightValue"] = value
            _args = {
                "UskPipHeight": value
            }
            self._parent.controller.set_usk_pip(_args)

    def _on_usk_mask_switch_rbtn_clicked(self, checked: bool):
        if checked:
            logging.debug("USK Mask ON")
            _args = {
                "UskMaskSwitch": "On"
            }
            toggle_layout_enable_or_disable(self.gridLayout_4, True)
            self._parent.controller.set_usk_mask(_args)
        else:
            logging.debug("USK Mask OFF")
            _args = {
                "UskMaskSwitch": "Off"
            }
            toggle_layout_enable_or_disable(self.gridLayout_4, False)
            self._parent.controller.set_usk_mask(_args)   
        
    def _on_usk_mask_top_slider_value_changed(self, value):
        if self._usk_mask_value["UskMaskTopValue"] != value:
            # self._usk_mask_value["UskMaskTopLineEdit"].setText("{}".format((value*5 - 900)/100.0))
            self._usk_mask_value["UskMaskTopLineEdit"].setValue((value*5 - 900)/100.0)
            self._usk_mask_value["UskMaskTopValue"] = value
            _args = {
                "UskMaskTop": (value*5)
            }
            self._parent.controller.set_usk_mask(_args)
    
    def _on_usk_mask_bottom_slider_value_changed(self, value):
        if self._usk_mask_value["UskMaskBottomValue"] != value:
            # self._usk_mask_value["UskMaskBottomLineEdit"].setText("{}".format((value*5 - 900)/100.0))
            self._usk_mask_value["UskMaskBottomLineEdit"].setValue((value*5 - 900)/100.0)
            self._usk_mask_value["UskMaskBottomValue"] = value
            _args = {
                "UskMaskBottom": (value*5)
            }
            self._parent.controller.set_usk_mask(_args)
    
    def _on_usk_mask_left_slider_value_changed(self, value):
        if self._usk_mask_value["UskMaskLeftValue"] != value:
            # self._usk_mask_value["UskMaskLeftLineEdit"].setText("{}".format((value*5 - 1600)/100.0))
            self._usk_mask_value["UskMaskLeftLineEdit"].setValue((value*5 - 1600)/100.0)
            self._usk_mask_value["UskMaskLeftValue"] = value
            _args = {
                "UskMaskLeft": (value*5)
            }
            self._parent.controller.set_usk_mask(_args)
    
    def _on_usk_mask_right_slider_value_changed(self, value):
        if self._usk_mask_value["UskMaskRightValue"] != value:
            # self._usk_mask_value["UskMaskRightLineEdit"].setText("{}".format((value*5 - 1600)/100.0))
            self._usk_mask_value["UskMaskRightLineEdit"].setValue((value*5 - 1600)/100.0)
            self._usk_mask_value["UskMaskRightValue"] = value
            _args = {
                "UskMaskRight": (value*5)
            }
            self._parent.controller.set_usk_mask(_args)

    def _on_usk_edge_stage1_rbtn_clicked(self, button):
        if self._usk_edge_value["UskEdgeStage1OffRadio"].isChecked():
            logging.debug("USK Edge Stage1 Off")
            _args = {
                "UskEdgeStage1": "Off"
            }
            self._parent.controller.set_usk_edge_stage(_args)
        elif self._usk_edge_value["UskEdgeStage1Erode3x3Radio"].isChecked():
            logging.debug("USK Edge Stage1 Erode 3x3")
            _args = {
                "UskEdgeStage1": "Erode3x3"
            }
            self._parent.controller.set_usk_edge_stage(_args)   
        elif self._usk_edge_value["UskEdgeStage1Erode5x5Radio"].isChecked():
            logging.debug("USK Edge Stage1 Erode 5x5")
            _args = {
                "UskEdgeStage1": "Erode5x5"
            }
            self._parent.controller.set_usk_edge_stage(_args) 
        elif self._usk_edge_value["UskEdgeStage1Dilate3x3Radio"].isChecked():
            logging.debug("USK Edge Stage1 Dilate 3x3")
            _args = {
                "UskEdgeStage1": "Dilate3x3"
            }
            self._parent.controller.set_usk_edge_stage(_args) 
        elif self._usk_edge_value["UskEdgeStage1Dilate5x5Radio"].isChecked():
            logging.debug("USK Edge Stage1 Dilate 5x5")
            _args = {
                "UskEdgeStage1": "Dilate5x5"
            }
            self._parent.controller.set_usk_edge_stage(_args) 
        elif self._usk_edge_value["UskEdgeStage1Gaussian3x3Radio"].isChecked():
            logging.debug("USK Edge Stage1 Gaussian 3x3")
            _args = {
                "UskEdgeStage1": "Gaussian3x3"
            }
            self._parent.controller.set_usk_edge_stage(_args) 
        elif self._usk_edge_value["UskEdgeStage1Gaussian5x5Radio"].isChecked():
            logging.debug("USK Edge Stage1 Gaussian 5x5")
            _args = {
                "UskEdgeStage1": "Gaussian5x5"
            }
            self._parent.controller.set_usk_edge_stage(_args) 
    
    def _on_usk_edge_stage2_rbtn_clicked(self, button):
        if self._usk_edge_value["UskEdgeStage2OffRadio"].isChecked():
            logging.debug("USK Edge Stage2 Off")
            _args = {
                "UskEdgeStage2": "Off"
            }
            self._parent.controller.set_usk_edge_stage(_args)
        elif self._usk_edge_value["UskEdgeStage2Erode3x3Radio"].isChecked():
            logging.debug("USK Edge Stage2 Erode 3x3")
            _args = {
                "UskEdgeStage2": "Erode3x3"
            }
            self._parent.controller.set_usk_edge_stage(_args)   
        elif self._usk_edge_value["UskEdgeStage2Erode5x5Radio"].isChecked():
            logging.debug("USK Edge Stage2 Erode 5x5")
            _args = {
                "UskEdgeStage2": "Erode5x5"
            }
            self._parent.controller.set_usk_edge_stage(_args) 
        elif self._usk_edge_value["UskEdgeStage2Dilate3x3Radio"].isChecked():
            logging.debug("USK Edge Stage2 Dilate 3x3")
            _args = {
                "UskEdgeStage2": "Dilate3x3"
            }
            self._parent.controller.set_usk_edge_stage(_args) 
        elif self._usk_edge_value["UskEdgeStage2Dilate5x5Radio"].isChecked():
            logging.debug("USK Edge Stage2 Dilate 5x5")
            _args = {
                "UskEdgeStage2": "Dilate5x5"
            }
            self._parent.controller.set_usk_edge_stage(_args) 
        elif self._usk_edge_value["UskEdgeStage2Gaussian3x3Radio"].isChecked():
            logging.debug("USK Edge Stage2 Gaussian 3x3")
            _args = {
                "UskEdgeStage2": "Gaussian3x3"
            }
            self._parent.controller.set_usk_edge_stage(_args) 
        elif self._usk_edge_value["UskEdgeStage2Gaussian5x5Radio"].isChecked():
            logging.debug("USK Edge Stage2 Gaussian 5x5")
            _args = {
                "UskEdgeStage2": "Gaussian5x5"
            }
            self._parent.controller.set_usk_edge_stage(_args) 

    def showEvent(self, event):
        # self._parent.controller.get_luma()
        # self._parent.controller.get_chroma()
        self._parent.controller.get_usk_layer()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        # if obj["function"] == "get_luma_params":
        #     args = obj["args"]
        #     logging.debug("luma args:{}".format(args))
        # elif obj["function"] == "get_chroma_params":
        #     args = obj["args"]
        #     logging.debug("chroma args:{}".format(args))
        if obj["function"] == "get_usk_layer_params":
            args = obj["args"]
            logging.debug("USK layer args:{}".format(args))

            _pip_switch = args["PipSwitch"]
            _pip_pos_h = args["PipHPos"]
            _pip_pos_v = args["PipVPos"]
            _pip_width = args["PipWidth"]
            _pip_height = args["PipHeight"]

            if _pip_switch == "On" or _pip_switch == "ON":
                toggle_layout_enable_or_disable(self.gridLayout_3, True)
                self._usk_pip_value["UskPipSwitchButton"].set_checked(True)
            else:
                toggle_layout_enable_or_disable(self.gridLayout_3, False)
                self._usk_pip_value["UskPipSwitchButton"].set_checked(False)
            
            if 0 <= _pip_pos_h <= 100:
                self._usk_pip_value["UskPipPosHorValue"] = _pip_pos_h
                # self._usk_pip_value["UskPipPosHorLineEdit"].setText("{}%".format(_pip_pos_h*1.0))
                self._usk_pip_value["UskPipPosHorLineEdit"].setValue(_pip_pos_h*1.0)
                self._usk_pip_value["UskPipPosHorSlider"].setValue(_pip_pos_h)
            
            if 0 <= _pip_pos_v <= 100:
                self._usk_pip_value["UskPipPosVerValue"] = _pip_pos_v
                # self._usk_pip_value["UskPipPosVerLineEdit"].setText("{}%".format(_pip_pos_v*1.0))
                self._usk_pip_value["UskPipPosVerLineEdit"].setValue(_pip_pos_v*1.0)
                self._usk_pip_value["UskPipPosVerSlider"].setValue(_pip_pos_v)
            
            if 0 <= _pip_width <= 100:
                self._usk_pip_value["UskPipWidthValue"] = _pip_width
                # self._usk_pip_value["UskPipWidthLineEdit"].setText("{}%".format(_pip_width*1.0))
                self._usk_pip_value["UskPipWidthLineEdit"].setValue(_pip_width*1.0)
                self._usk_pip_value["UskPipWidthSlider"].setValue(_pip_width)

            if 0 <= _pip_height <= 100:
                self._usk_pip_value["UskPipHeightValue"] = _pip_height
                # self._usk_pip_value["UskPipHeightLineEdit"].setText("{}%".format(_pip_height*1.0))
                self._usk_pip_value["UskPipHeightLineEdit"].setValue(_pip_height*1.0)
                self._usk_pip_value["UskPipHeightSlider"].setValue(_pip_height)

            _mask_switch = args["MaskSwitch"]
            _mask_top = args["MaskTop"]
            _mask_bottom = args["MaskBottom"]
            _mask_left = args["MaskLeft"]
            _mask_right = args["MaskRight"]

            if _mask_switch == "On" or _mask_switch == "ON":
                toggle_layout_enable_or_disable(self.gridLayout_4, True)
                self._usk_mask_value["UskMaskSwitchButton"].set_checked(True)
            else:
                toggle_layout_enable_or_disable(self.gridLayout_4, False)
                self._usk_mask_value["UskMaskSwitchButton"].set_checked(False)
            
            if 0 <= _mask_top <= 1800:
                self._usk_mask_value["UskMaskTopValue"] = int(_mask_top/5)
                # self._usk_mask_value["UskMaskTopLineEdit"].setText("{}".format((_mask_top - 900)/100.0))
                self._usk_mask_value["UskMaskTopLineEdit"].setValue((_mask_top - 900)/100.0)
                self._usk_mask_value["UskMaskTopSlider"].setValue(int(_mask_top/5))
            
            if 0 <= _mask_bottom <= 1800:
                self._usk_mask_value["UskMaskBottomValue"] = int(_mask_bottom/5)
                # self._usk_mask_value["UskMaskBottomLineEdit"].setText("{}".format((_mask_bottom - 900)/100.0))
                self._usk_mask_value["UskMaskBottomLineEdit"].setValue((_mask_bottom - 900)/100.0)
                self._usk_mask_value["UskMaskBottomSlider"].setValue(int(_mask_bottom/5))
            
            if 0 <= _mask_left <= 3200:
                self._usk_mask_value["UskMaskLeftValue"] = int(_mask_left/5)
                # self._usk_mask_value["UskMaskLeftLineEdit"].setText("{}".format((_mask_left - 1600)/100.0))
                self._usk_mask_value["UskMaskLeftLineEdit"].setValue((_mask_left - 1600)/100.0)
                self._usk_mask_value["UskMaskLeftSlider"].setValue(int(_mask_left/5))

            if 0 <= _mask_right <= 3200:
                self._usk_mask_value["UskMaskRightValue"] = int(_mask_right/5)
                # self._usk_mask_value["UskMaskRightLineEdit"].setText("{}".format((_mask_right - 1600)/100.0))
                self._usk_mask_value["UskMaskRightLineEdit"].setValue((_mask_right - 1600)/100.0)
                self._usk_mask_value["UskMaskRightSlider"].setValue(int(_mask_right/5))

            _stage1 = args["Stage1"]
            _stage2 = args["Stage2"]

            if _stage1 == 0:
                self._usk_edge_value["UskEdgeStage1OffRadio"].setChecked(True)
            elif _stage1 == 1:
                self._usk_edge_value["UskEdgeStage1Erode3x3Radio"].setChecked(True)
            elif _stage1 == 2:
                self._usk_edge_value["UskEdgeStage1Erode5x5Radio"].setChecked(True)
            elif _stage1 == 3:
                self._usk_edge_value["UskEdgeStage1Dilate3x3Radio"].setChecked(True)
            elif _stage1 == 4:
                self._usk_edge_value["UskEdgeStage1Dilate5x5Radio"].setChecked(True)
            elif _stage1 == 5:
                self._usk_edge_value["UskEdgeStage1Gaussian3x3Radio"].setChecked(True)
            elif _stage1 == 6:
                self._usk_edge_value["UskEdgeStage1Gaussian5x5Radio"].setChecked(True)
            
            if _stage2 == 0:
                self._usk_edge_value["UskEdgeStage2OffRadio"].setChecked(True)
            elif _stage2 == 1:
                self._usk_edge_value["UskEdgeStage2Erode3x3Radio"].setChecked(True)
            elif _stage2 == 2:
                self._usk_edge_value["UskEdgeStage2Erode5x5Radio"].setChecked(True)
            elif _stage2 == 3:
                self._usk_edge_value["UskEdgeStage2Dilate3x3Radio"].setChecked(True)
            elif _stage2 == 4:
                self._usk_edge_value["UskEdgeStage2Dilate5x5Radio"].setChecked(True)
            elif _stage2 == 5:
                self._usk_edge_value["UskEdgeStage2Gaussian3x3Radio"].setChecked(True)
            elif _stage2 == 6:
                self._usk_edge_value["UskEdgeStage2Gaussian5x5Radio"].setChecked(True)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = USKWidget()
    window.show()
    sys.exit(app.exec())
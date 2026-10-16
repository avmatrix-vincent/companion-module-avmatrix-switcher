import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSignalBlocker, Qt, Signal
from src.ui.uc1218_4K.uc1218_4K_video_setting_ui import Ui_UC1218_4K_Video_Setting_Form
from src.model.modelPreferences import ModelPreferences
from src.model.uc1218_4K.uc1218_4K_Preferences import UC1218_4K_Preferences
from src.model.modelRticePreferences import ModelRticePreferences
from globals import relative_path, global_qss

class UC1218_4K_VideoSetting(Ui_UC1218_4K_Video_Setting_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)
        self.input_colorSpace = ""

        self.set_colorRange_bypass_radioButton.clicked.connect(lambda: self._on_colorRange_buttonGroup_clicked(ModelRticePreferences._targetCSCPosList[0], ModelRticePreferences._colorRangeModeList[0]))
        self.set_colorRange_limitedRange_radioButton.clicked.connect(lambda: self._on_colorRange_buttonGroup_clicked(ModelRticePreferences._targetCSCPosList[0], ModelRticePreferences._colorRangeModeList[1]))
        self.set_colorRange_fullRange_radioButton.clicked.connect(lambda: self._on_colorRange_buttonGroup_clicked(ModelRticePreferences._targetCSCPosList[0], ModelRticePreferences._colorRangeModeList[2]))
    
    def _on_colorRange_buttonGroup_clicked(self, targetCSCPos, colorRange):
        try:
            _args = {
                "TargetCSCPos": targetCSCPos,
                "ColorRange": colorRange
            }
            self._parent.controller.set_rtice_ColorRange(_args)
            self._set_rtice_ConfigData()
        except Exception as e:
            logging.error(f"e:{e}")

    def _set_rtice_ConfigData(self):
        try:
            _data = [0, 0] # 第一个为RGB2YUV的转换模式，第二个为YUV2RGB的转换模式

            # 此处只采用第一个RGB2YUV的转换模式，实际设置后，YUV2RGB也同样有效
            if self.set_colorRange_bypass_radioButton.isChecked():
                _data[0] = 0
            elif self.set_colorRange_limitedRange_radioButton.isChecked():
                _data[0] = 1
            elif self.set_colorRange_fullRange_radioButton.isChecked():
                _data[0] = 2

            _args = {
                "ConfigData": _data
            }
            self._parent.controller.set_rtice_ConfigData(_args)
        except Exception as e:
            logging.error(f"e:{e}")

    def showEvent(self, event):
        self._parent.controller.get_rtice_ConfigData()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_rtice_HdmiRX_RawTimingInfo":
            _args = obj["args"]
            _result = _args["Result"]
            if _result:
                _colorSpace = _args["ColorSpace"]
                # 在获取到输入端的ColorSpace之后，才知道是RGB2YUV还是YUV2RGB，然后再去获取生效的输出color range
                # logging.debug(f"input_colorSpace: {self.input_colorSpace}")
                _args = {
                    "TargetCSCPos": ModelRticePreferences._targetCSCPosList[0] if _colorSpace.startswith("RGB") else ModelRticePreferences._targetCSCPosList[1]
                }
                self._parent.controller.get_rtice_ColorRange(_args)
        elif obj["function"] == "get_rtice_ColorRange":
            _args = obj["args"]
            if _args["ColorRange"] in ModelRticePreferences._colorRangeList:
                if _args["ColorRange"] == ModelRticePreferences._colorRangeList[0]:
                    self.colorRange_value_label.setText("Limited Range")
                elif _args["ColorRange"] == ModelRticePreferences._colorRangeList[1]:
                    self.colorRange_value_label.setText("Full Range")
        elif obj["function"] == "get_rtice_ConfigData":
            _args = obj["args"]
            _data = _args["ConfigData"]

            if _args["Result"] and len(_data) >= 2:
                if _data[0] == 0:
                    with QSignalBlocker(self.set_colorRange_bypass_radioButton):
                        self.set_colorRange_bypass_radioButton.setChecked(True)
                elif _data[0] == 1:
                    with QSignalBlocker(self.set_colorRange_limitedRange_radioButton):
                        self.set_colorRange_limitedRange_radioButton.setChecked(True)
                elif _data[0] == 2:
                    with QSignalBlocker(self.set_colorRange_fullRange_radioButton):
                        self.set_colorRange_fullRange_radioButton.setChecked(True)
                else:
                    _data[0] = 0
                    with QSignalBlocker(self.set_colorRange_bypass_radioButton):
                        self.set_colorRange_bypass_radioButton.setChecked(True)
                
                # 设置RGB2YUV的ColorRange与配置同步
                _args = {
                    "TargetCSCPos": ModelRticePreferences._targetCSCPosList[0],
                    "ColorRange": ModelRticePreferences._colorRangeModeList[_data[0]]
                }
                self._parent.controller.set_rtice_ColorRange(_args)
            else:
                logging.error("Error to get config data!")
                # 一般是没有初始化自定义区数据，这里初始化一下
                with QSignalBlocker(self.set_colorRange_bypass_radioButton):
                    self.set_colorRange_bypass_radioButton.setChecked(True)

                # 设置RGB2YUV的ColorRange与配置同步
                _args = {
                    "TargetCSCPos": ModelRticePreferences._targetCSCPosList[0],
                    "ColorRange": ModelRticePreferences._colorRangeModeList[0]
                }
                self._parent.controller.set_rtice_ColorRange(_args)

                # 设置YUV2RGB的ColorRange与配置同步
                # _args = {
                #     "TargetCSCPos": ModelRticePreferences._targetCSCPosList[1],
                #     "ColorRange": ModelRticePreferences._colorRangeModeList[0]
                # }
                # self._parent.controller.set_rtice_ColorRange(_args)

                # self._set_rtice_ConfigData()

            # 同步配置后，再获取HDMI RX Timing信息，然后在回包处理中再去获取生效的ColorRange
            self._parent.controller.get_rtice_HdmiRX_RawTimingInfo()
        elif obj["function"] == "set_rtice_ConfigData":
            _args = obj["args"]
            logging.debug("Set config data success!")
            # 配置后，也要再获取HDMI RX Timing信息，然后在回包处理中再去获取生效的ColorRange
            self._parent.controller.get_rtice_HdmiRX_RawTimingInfo()

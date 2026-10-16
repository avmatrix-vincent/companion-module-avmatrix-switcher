import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QButtonGroup
from PySide6.QtCore import QSignalBlocker
from src.ui.sc7030.sc7030_setting_ui import Ui_SC7030_Setting_Form
from src.model.sc7030.sc7030Preferences import SC7030Preferences
from src.model.modelPreferences import ModelPreferences

class SC7030Setting(Ui_SC7030_Setting_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        _output_resolutions = SC7030Preferences.get_output_resolutions()
        _video_inputs = SC7030Preferences.get_video_inputs()
        _m_out_radio = SC7030Preferences.get_out_radio()
        _audio_input = SC7030Preferences.get_audio_inputs()
        _hdmi_out_range = SC7030Preferences.get_hdmi_out_range()
        _3g_out_level = SC7030Preferences.get_3g_out_level()

        self.comboBox_output_resolution.addItems(_output_resolutions)
        self.comboBox_video_input_mode.addItems(_video_inputs)
        self.comboBox_out_radio.addItems(_m_out_radio)
        self.comboBox_audio_input.addItems(_audio_input)
        self.comboBox_hdmi_out_range.addItems(_hdmi_out_range)
        self.comboBox_3g_level.addItems(_3g_out_level)

        # self.comboBox_output_resolution.setCurrentIndex(-1)
        # self.comboBox_video_input_mode.setCurrentIndex(-1)

        self.comboBox_output_resolution.currentIndexChanged.connect(self._select_setting_params)
        self.comboBox_video_input_mode.currentIndexChanged.connect(self._select_setting_params)
        self.comboBox_out_radio.currentIndexChanged.connect(self._select_setting_params)
        self.comboBox_audio_input.currentIndexChanged.connect(self._select_setting_params)
        self.comboBox_hdmi_out_range.currentIndexChanged.connect(self._select_setting_params)
        self.comboBox_3g_level.currentIndexChanged.connect(self._select_setting_params)


    def _select_setting_params(self, index):
        sender = self.sender()

        if sender == self.comboBox_output_resolution:
            logging.debug("select output resolution input:{}".format(index))
            _args = {
                    "OutputResolution": index
                }
            self._parent.controller.set_setting_params(_args)

        elif sender == self.comboBox_video_input_mode:
            logging.debug("select video input input:{}".format(index))
            _args = {
                    "VideoInputMode": index
                }
            with QSignalBlocker(self.comboBox_out_radio):
                if 3 > index >= 0:
                    self.comboBox_out_radio.clear()
                    self.comboBox_out_radio.addItems(SC7030Preferences.get_out_radio2())
                else:
                    self.comboBox_out_radio.clear()
                    self.comboBox_out_radio.addItems(SC7030Preferences.get_out_radio())

            self._parent.controller.set_setting_params(_args)
            self._parent.controller.get_setting_params()

        elif sender == self.comboBox_out_radio:
            if self.comboBox_video_input_mode.currentIndex()<3:
                logging.debug("select out Radio:{}".format(index))
                _args = {
                    "AspectRatio": index
                }
                self._parent.controller.set_setting_params(_args)
            else:
                logging.debug("select out radio input:{}".format(index))
                _args = {
                        "MS1824OutRatio": index
                    }
                self._parent.controller.set_setting_params(_args)

        elif sender == self.comboBox_audio_input:
            logging.debug("select audio input:{}".format(index))
            _args = {
                "AudioInput": index
            }
            self._parent.controller.set_setting_params(_args)

        elif sender == self.comboBox_hdmi_out_range:
            logging.debug("select hdmi out range:{}".format(index))
            _args = {
                "HDMIColorRange": index
            }
            self._parent.controller.set_setting_params(_args)

        elif sender == self.comboBox_3g_level:
            logging.debug("select 3g out level:{}".format(index))
            _args = {
                "SDIMode": index
            }
            self._parent.controller.set_setting_params(_args)

    def showEvent(self, event):
        #self._parent.controller.get_version_info()
        self._parent.controller.get_setting_params()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        try:
            if obj["function"] == "get_setting_params":
                args = obj["args"]
                logging.debug("args:{}".format(args))
                _output_resolution = args["OutputResolution"]
                _video_inputMode = args["VideoInputMode"]
                _audio_input = args["AudioInput"]
                _aspect_ratio = args["AspectRatio"]
                _hdmi_color_range = args["HDMIColorRange"]
                _sdi_mode = args["SDIMode"]
                _m_out_radio = args["MS1824OutRatio"]
                if _output_resolution != 0xFF:
                    with QSignalBlocker(self.comboBox_output_resolution):
                        self.comboBox_output_resolution.setCurrentIndex(_output_resolution)
                if _video_inputMode != 0xFF and _video_inputMode < 7:
                    with QSignalBlocker(self.comboBox_video_input_mode):
                        self.comboBox_video_input_mode.setCurrentIndex(_video_inputMode)
                if _audio_input != 0xFF:
                    with QSignalBlocker(self.comboBox_audio_input):
                        self.comboBox_audio_input.setCurrentIndex(_audio_input)
                if _hdmi_color_range != 0xFF:
                    with QSignalBlocker(self.comboBox_hdmi_out_range):
                        self.comboBox_hdmi_out_range.setCurrentIndex(_hdmi_color_range)
                if _sdi_mode != 0xFF:
                    with QSignalBlocker(self.comboBox_3g_level):
                        self.comboBox_3g_level.setCurrentIndex(_sdi_mode)
                if _m_out_radio != 0xFF and  _m_out_radio < 4:
                    with QSignalBlocker(self.comboBox_out_radio):
                        if 3 > _video_inputMode >= 0:
                            self.comboBox_out_radio.clear()
                            self.comboBox_out_radio.addItems(SC7030Preferences.get_out_radio2())
                            self.comboBox_out_radio.setCurrentIndex(_aspect_ratio)
                        else:
                            self.comboBox_out_radio.clear()
                            self.comboBox_out_radio.addItems(SC7030Preferences.get_out_radio())
                            self.comboBox_out_radio.setCurrentIndex(_m_out_radio)



            elif obj["function"] == "set_setting_params":
                args = obj["args"]
                logging.debug("Set setting params args args:{}".format(args))

        except:
            import traceback
            print(traceback.format_exc())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = SC7030Setting()
    window.show()
    sys.exit(app.exec())
import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSignalBlocker, Qt, Signal
from src.ui.shark_h4k.SharkH4kSwitch_ui import Ui_SharkH4kSwitch_Form
from src.model.modelPreferences import ModelPreferences
from globals import relative_path, global_qss

class Shark_H4K_Switch(Ui_SharkH4kSwitch_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.clock_phase_comboBox.addItems(["Phase 0", "Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5", "Phase 6", "Phase 7"])
        self.clock_phase_comboBox.currentIndexChanged.connect(self.on_clock_phase_changed)

        self.mv_onoff_checkBox.stateChanged.connect(self.on_mv_state_changed)

        self.pvw_ch1_pushButton.clicked.connect(lambda: self.on_pvw_source_changed("HDMI1")) # lambda: self._on_hdmiOutSrc_buttonGroup_clicked(0)
        self.pvw_ch2_pushButton.clicked.connect(lambda: self.on_pvw_source_changed("HDMI2"))
        self.pvw_ch3_pushButton.clicked.connect(lambda: self.on_pvw_source_changed("HDMI3"))
        self.pvw_ch4_pushButton.clicked.connect(lambda: self.on_pvw_source_changed("HDMI4"))
        self.pvw_pattern1_pushButton.clicked.connect(lambda: self.on_pvw_source_changed("Pattern1"))
        self.pvw_pattern2_pushButton.clicked.connect(lambda: self.on_pvw_source_changed("Pattern2"))

        self.pvw_ch1_pushButton.setProperty("type", "pvw_button")
        self.pvw_ch2_pushButton.setProperty("type", "pvw_button")
        self.pvw_ch3_pushButton.setProperty("type", "pvw_button")
        self.pvw_ch4_pushButton.setProperty("type", "pvw_button")
        self.pvw_pattern1_pushButton.setProperty("type", "pvw_button")
        self.pvw_pattern2_pushButton.setProperty("type", "pvw_button")

        self.pgm_ch1_pushButton.clicked.connect(lambda: self.on_pgm_source_changed("HDMI1"))
        self.pgm_ch2_pushButton.clicked.connect(lambda: self.on_pgm_source_changed("HDMI2"))
        self.pgm_ch3_pushButton.clicked.connect(lambda: self.on_pgm_source_changed("HDMI3"))
        self.pgm_ch4_pushButton.clicked.connect(lambda: self.on_pgm_source_changed("HDMI4"))
        self.pgm_pattern1_pushButton.clicked.connect(lambda: self.on_pgm_source_changed("Pattern1"))
        self.pgm_pattern2_pushButton.clicked.connect(lambda: self.on_pgm_source_changed("Pattern2"))

        self.pgm_ch1_pushButton.setProperty("type", "pgm_button")
        self.pgm_ch2_pushButton.setProperty("type", "pgm_button")
        self.pgm_ch3_pushButton.setProperty("type", "pgm_button")
        self.pgm_ch4_pushButton.setProperty("type", "pgm_button")
        self.pgm_pattern1_pushButton.setProperty("type", "pgm_button")
        self.pgm_pattern2_pushButton.setProperty("type", "pgm_button")

        self.pgm_pvw_cut_pushButton.clicked.connect(self.on_pgm_pvw_cut_button_clicked)
        self.pgm_pvw_cut_pushButton.setProperty("type", "cut_button")

    def on_mv_state_changed(self, state):
        logging.debug("MV state changed, state: {}".format(state))
        """ 处理MV开关状态变化 """
        args = {
            "State": "On" if self.mv_onoff_checkBox.isChecked() else "Off"
        }
        self._parent.controller.set_mv_state(args)

    def on_clock_phase_changed(self, index):
        """ 处理时钟相位变化 """
        args = {
            "ClockPhase": index
        }
        self._parent.controller.set_clock_phase(args)

    def on_pvw_source_changed(self, source):
        logging.debug("PVW source changed, source: {}".format(source))
        """ 处理PVW源变化 """
        args = {
            "Source": source
        }
        self._parent.controller.set_pvw_output(args)

    def on_pgm_source_changed(self, source):
        logging.debug("PGM source changed, source: {}".format(source))
        """ 处理PGM源变化 """
        args = {
            "Source": source
        }
        self._parent.controller.set_pgm_output(args)

    def on_pgm_pvw_cut_button_clicked(self):
        """ 处理PGM和PVW切换按钮点击 """
        args = {
        }
        self._parent.controller.set_pgm_pvw_cut(args)

    def showEvent(self, event):
        self._parent.controller.get_version_info()
        self._parent.controller.get_switch_state()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_version_info":
            args = obj["args"]
            logging.debug("Get version args:{}".format(args))
        elif obj["function"] == "get_switch_state":
            args = obj["args"]
            logging.debug("Get switch state args:{}".format(args))

            if "PGMSource" in args:
                _pgm_source = args["PGMSource"]
                _pgm_buttons_map = {
                    "HDMI1": self.pgm_ch1_pushButton,
                    "HDMI2": self.pgm_ch2_pushButton,
                    "HDMI3": self.pgm_ch3_pushButton,
                    "HDMI4": self.pgm_ch4_pushButton,
                    "Pattern1": self.pgm_pattern1_pushButton,
                    "Pattern2": self.pgm_pattern2_pushButton
                }
                
                for button in _pgm_buttons_map.values():
                    button.setDisabled(False)

                if _pgm_source in _pgm_buttons_map:
                    # _pgm_buttons_map[pgm_source].setChecked(True)
                    _pgm_buttons_map[_pgm_source].setDisabled(True)
                else:
                    logging.warning("Unknown PGM source: {}".format(_pgm_source))
            
            if "PVWSource" in args:
                _pvw_source = args["PVWSource"]
                _pvw_buttons_map = {
                    "HDMI1": self.pvw_ch1_pushButton,
                    "HDMI2": self.pvw_ch2_pushButton,
                    "HDMI3": self.pvw_ch3_pushButton,
                    "HDMI4": self.pvw_ch4_pushButton,
                    "Pattern1": self.pvw_pattern1_pushButton,
                    "Pattern2": self.pvw_pattern2_pushButton
                }
                
                for button in _pvw_buttons_map.values():
                    button.setDisabled(False)

                if _pvw_source in _pvw_buttons_map:
                    # _pvw_buttons_map[pvw_source].setChecked(True)
                    _pvw_buttons_map[_pvw_source].setDisabled(True)
                else:
                    logging.warning("Unknown PVW source: {}".format(_pvw_source))

            if "MVState" in args:
                mv_state = args["MVState"]
                with QSignalBlocker(self.mv_onoff_checkBox):
                    if mv_state == "On":
                        self.mv_onoff_checkBox.setChecked(True)
                    else:
                        self.mv_onoff_checkBox.setChecked(False)
        elif obj["function"] in ["set_pgm_output", "set_pvw_output", "set_pgm_pvw_cut"]:
            args = obj["args"]
            logging.debug("Setter's callback args:{}".format(args))

            # 执行set之后，在这里再获取一次切换台状态
            self._parent.controller.get_switch_state()

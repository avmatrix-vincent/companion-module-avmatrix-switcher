import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication
from src.ui.sc2030.sc2030_setting_ui import Ui_SC2030_Setting_Form

class SC2030Setting(Ui_SC2030_Setting_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.pushButton_save.setProperty("type", "device_btn")
        self.comboBox_scaling.addItems(['123', 'abc', '31r243352462362', "99999999999999999999", "gaiewegawe"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = SC2030Setting()
    window.show()
    sys.exit(app.exec())
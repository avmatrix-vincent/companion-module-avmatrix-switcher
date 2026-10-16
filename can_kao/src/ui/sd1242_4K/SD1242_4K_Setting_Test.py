import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QButtonGroup
from PySide6.QtCore import QSignalBlocker
from src.ui.sd1242_4K.SD1242_4K_Setting_ui import Ui_Form
from src.model.modelPreferences import ModelPreferences

class SC1112_12G_Setting_Test(Ui_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.device_edid_plainTextEdit.setReadOnly(True)

    def showEvent(self, event):
        super().showEvent(event)  # 调用基类的 showEvent 方法

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = SC1112_12G_Setting_Test()
    window.show()
    sys.exit(app.exec())
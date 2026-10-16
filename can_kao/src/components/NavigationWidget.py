import sys, os
# sys.path.append("../")
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QApplication, QWidget, QPushButton, QSpacerItem, QSizePolicy
from src.components.DeviceWidget import DeviceMiniWidget
from globals import relative_path

class NavigationWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(QSize(60, 586))
        self.main_layout = QVBoxLayout(self)

        self.scan_btn = QPushButton()
        self.scan_btn.setFixedSize(QSize(50, 50))
        self.main_layout.addWidget(self.scan_btn)
        # 添加垂直弹簧到布局中
        spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout.addItem(spacer)
        page_btn_layout = QHBoxLayout()
        self.page_up_btn = QPushButton()
        self.page_down_btn = QPushButton()
        page_btn_layout.addWidget(self.page_up_btn)
        page_btn_layout.addWidget(self.page_down_btn)
        self.main_layout.addLayout(page_btn_layout)

        self.main_layout.setSpacing(10)
        page_btn_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.scan_btn.setIcon(QIcon(relative_path("res/images/scan.png")))
        self.scan_btn.setIconSize(QSize(32, 32))
        self.page_up_btn.setIcon(QIcon(relative_path("res/images/pageUp.png")))
        self.page_down_btn.setIcon(QIcon(relative_path("res/images/pageDown.png")))
        self.scan_btn.setProperty("type", "scan_mini_btn")
        self.page_up_btn.setObjectName("page_up_btn")
        self.page_down_btn.setObjectName("page_down_btn")

    def test_insert(self):
        device_1 = DeviceMiniWidget("124132", self)
        self.main_layout.insertWidget(1, device_1)
        device_2 = DeviceMiniWidget("124132", self)
        self.main_layout.insertWidget(2, device_2)
        device_3 = DeviceMiniWidget("124132", self)
        self.main_layout.insertWidget(3, device_3)
        device_4 = DeviceMiniWidget("124132", self)
        self.main_layout.insertWidget(4, device_4)
        device_5 = DeviceMiniWidget("124132", self)
        self.main_layout.insertWidget(5, device_5)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NavigationWidget()
    window.test_insert()
    window.show()
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    sys.exit(app.exec())

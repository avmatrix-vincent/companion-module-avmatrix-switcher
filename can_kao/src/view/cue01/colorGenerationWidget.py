import os
import sys
import logging
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QApplication, QLabel
from PySide6.QtGui import QColor
from src.components.ColorSelector import ColorSelector
from PySide6.QtCore import QCoreApplication

class ColorGenerationWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        # self._colors = ["#000000", "#000000"]
        self._colors = ['#00aa7f', '#aaffff']
        
        # self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        
        sub_layout = QHBoxLayout()
        # sub_layout.setSpacing(0)
        self.color_selector_1 = ColorSelector(self, self._colors[0])
        self.color_selector_2 = ColorSelector(self, self._colors[1])
        sub_layout.addStretch(2)
        self.label_color_1 = QLabel()
        sub_layout.addWidget(self.label_color_1, 1)
        sub_layout.addWidget(self.color_selector_1, 2)
        sub_layout.addStretch(1)
        self.label_color_2 = QLabel()
        sub_layout.addWidget(self.label_color_2, 1)
        sub_layout.addWidget(self.color_selector_2, 2)
        sub_layout.addStretch(2)

        main_layout.addStretch(1)
        main_layout.addLayout(sub_layout, 2)
        main_layout.addStretch(6)

        self.color_selector_1.color_selected_signal.connect(self.set_color)
        self.color_selector_2.color_selected_signal.connect(self.set_color)

        self.retranslateUi()
        
    def set_color(self, color):
        if self.sender() == self.color_selector_1:
            self._colors[0] = color
            self.save_color("Color1", self._colors[0])
        elif self.sender() == self.color_selector_2:
            self._colors[1] = color
            self.save_color("Color2", self._colors[1])

    def save_color(self, flag, color):
        _color_rgb = QColor.fromString(color)

        args = {
            "ColorValid": [True, False] if flag == "Color1" else [False, True],
            "Color": [
                {
                    "Red": _color_rgb.red(),
                    "Green": _color_rgb.green(),
                    "Blue": _color_rgb.blue()
                }
            ]
        }

        self._parent.controller.set_color_generation(args)

    def retranslateUi(self):
        self.label_color_1.setText(QCoreApplication.translate("CUE01_Color_Generation_Widget_Form", u"Color1", None))
        self.label_color_2.setText(QCoreApplication.translate("CUE01_Color_Generation_Widget_Form", u"Color2", None))

    def showEvent(self, event):
        self._parent.controller.get_color_generation()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_color_generation_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))

            if args["ColorNumber"] == 2:
                colors = args["Color"]
                self._colors[0] = QColor.fromRgb(colors[0]["Red"], colors[0]["Green"], colors[0]["Blue"]).name()
                self._colors[1] = QColor.fromRgb(colors[1]["Red"], colors[1]["Green"], colors[1]["Blue"]).name()
                self.color_selector_1.setColor(self._colors[0])
                self.color_selector_2.setColor(self._colors[1])
        elif obj["function"] == "set_color_generation":
            args = obj["args"]
            logging.debug("Set color generation args:{}".format(args))


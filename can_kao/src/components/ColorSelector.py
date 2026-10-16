import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QColorDialog, QPushButton
from PySide6.QtCore import Qt, QSettings, Signal
from PySide6.QtGui import QIcon, QBrush, QPixmap, QPainter, QPen, QMouseEvent, QPalette
from src.ui.cue01.color_selector_widget_ui import Ui_Form as ColorWidget
from globals import relative_path
from src.config.TranslationManager import TranslationManager

def modify_colorDialog_str(widget):
    index = TranslationManager().current_language_index
    if isinstance(widget, QPushButton):
        text = widget.text()
        # print(text)
        if "Pick Screen Color" in text: #  or "选取屏幕颜色" in text
            widget.setText("选取屏幕颜色" if index == 1 else "Pick Screen Color")
    if isinstance(widget, QLabel):
        text = widget.text()
        # print(text)
        if "HTML" in text:
            widget.setText("Hex:")
    elif isinstance(widget, QWidget):
        for child in widget.children():
            modify_colorDialog_str(child)

class ColorSelector(ColorWidget, QWidget):

    color_selected_signal = Signal(str)

    def __init__(self, parent=None, color="#f39801"):  
        super().__init__(parent)  
        self.setupUi(self)
        self.current_color = color
        self.setColor(color)

        # 绑定鼠标点击事件  
        self.mousePressEvent = self.on_color_label_mouse_press 
  
    def setColor(self, color):
        # print(color)
        self.current_color = color
        self.color_display_widget.setStyleSheet("#color_display_widget { background-color: %s; border-radius: 8px; }"%color)
  
    def on_color_label_mouse_press(self, event: QMouseEvent):  
        if event.button() == Qt.LeftButton:  
            # 弹出颜色对话框  
            color_dialog = QColorDialog()
            # 强制使用QT颜色选择器，不使用系统本地颜色选择器
            color_dialog.setOptions(QColorDialog.DontUseNativeDialog) # 创建窗口之后马上设置，解决翻译和设置当前颜色的问题
            color_dialog.setCurrentColor(self.current_color)
            color_dialog.setWindowTitle("选择颜色" if TranslationManager().current_language_index == 1 else "Select Color")
            modify_colorDialog_str(color_dialog)
            # color_dialog.setOptions(QColorDialog.ShowAlphaChannel | QColorDialog.DontUseNativeDialog)
            color_dialog.setProperty("type", "color_dialog")
            color_dialog.setWindowIcon(QIcon(relative_path("res/images/color_selector.png")))

            # 加载自定义颜色
            self.load_custom_colors(color_dialog)

            if color_dialog.exec():  
                selected_color = color_dialog.selectedColor().name()
                self.color_selected_signal.emit(selected_color)
                self.setColor(selected_color)

                # 保存自定义颜色
                self.save_custom_colors(color_dialog)

    def load_custom_colors(self, color_dialog):
        settings = QSettings("AvMatrix", "UpperComputer")
        custom_colors = settings.value("customColors", [])
        if custom_colors:
            color_dialog.setCustomColor(0, custom_colors[0])
            for i, color in enumerate(custom_colors):
                color_dialog.setCustomColor(i, int(color, 16))

    def save_custom_colors(self, color_dialog):
        settings = QSettings("MyCompany", "MyApp")
        custom_colors = []
        for i in range(16):
            color = color_dialog.customColor(i)
            if color.isValid():
                custom_colors.append(hex(color.rgb()))
        settings.setValue("customColors", custom_colors)


# 示例使用  
if __name__ == '__main__':  
    app = QApplication([])  
    picker = ColorSelector()    
    picker.show()  
    app.exec()
import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from src.components.CustomSingleSlider import CustomSingleSlider
from src.components.CustomSpinBox import CustomDoubleSpinBox
  
class SingleSliderWithDoubleSpinbox(QWidget):  
    def __init__(self, parent=None, max_value=999, default_value=0):  
        super().__init__(parent)
        self.max_value = max_value
        self.init_ui()

        self.slider.setMaximum(max_value)
        self.slider.setValue(default_value)
        self.spinbox.setValue(default_value)
        # self.slider.valueChanged.connect(lambda value : self.spinbox.setValue(value))
        # self.spinbox.valueChanged.connect(lambda value : self.slider.setValue(value))

    def init_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.slider = CustomSingleSlider(self)
        self.slider.setOrientation(Qt.Horizontal)
        self.spinbox = CustomDoubleSpinBox(self)
        main_layout.addWidget(self.slider)
        main_layout.addWidget(self.spinbox)

        # self.slider.setMaximumHeight(16)
        # self.spinbox.setMaximumHeight(16)

    def get_value(self): # 用于外界直接获取当前值
        return self.slider.value()



  
# 主程序  
if __name__ == "__main__":  
    app = QApplication(sys.argv)   
    widget = SingleSliderWithDoubleSpinbox()    
    widget.show()  
    sys.exit(app.exec())
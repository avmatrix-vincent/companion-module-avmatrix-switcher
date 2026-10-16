import sys  
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QSizePolicy, QDoubleSpinBox
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
  
class CustomSpinBox(QSpinBox):  
    def __init__(self, parent=None, max_num=1000):  
        super().__init__(parent)
        self.setMaximum(max_num)
        self.setAlignment(Qt.AlignCenter)
        self.setMinimumSize(QSize(60, 20)) 
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)  

class CustomDoubleSpinBox(QDoubleSpinBox):  
    def __init__(self, parent=None, max_num=1000):  
        super().__init__(parent)
        self.setMaximum(max_num)
        self.setAlignment(Qt.AlignCenter)
        self.setMinimumSize(QSize(60, 20)) 
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum) 
  
# 主程序  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
  
    widget = QWidget()  
    layout = QVBoxLayout(widget)  
  
    # 创建自定义下拉框  
    custom_combo_box = CustomSpinBox()  
    layout.addWidget(custom_combo_box)  
  
    widget.show()  
    sys.exit(app.exec())
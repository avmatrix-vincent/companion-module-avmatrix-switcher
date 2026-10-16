import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QToolButton, QHBoxLayout  
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon  
from globals import relative_path
  
class ClearableLineEdit(QWidget):  
    def __init__(self, parent=None):  
        super().__init__(parent)  
  
        # 创建布局  
        layout = QHBoxLayout(self)  
        layout.setContentsMargins(1, 1, 1, 1)  
        layout.setSpacing(0)  
  
        # 创建输入框  
        self.line_edit = QLineEdit(self)  
        layout.addWidget(self.line_edit, 1)  # 1 表示给 QLineEdit 更多的拉伸因子  
  
        # 创建清空按钮  
        self.clear_button = QToolButton(self)  
        self.clear_button.setIcon(QIcon(relative_path(r"res\images\clear.png")))  # 替换为你的图标路径  
        # self.clear_button.setIconSize(QSize(16, 16))  # 设置按钮图标大小  
        self.clear_button.setAutoRaise(True)  
        self.clear_button.clicked.connect(self.clear_text)  
        layout.addWidget(self.clear_button)   
  
        # 设置对象名称以便在QSS中引用  
        self.clear_button.setProperty("type", "clearButton") 

        self.setAttribute(Qt.WA_StyledBackground, True) 
        self.setFixedHeight(27) 
  
    def clear_text(self):  
        """清空输入框内容"""  
        self.line_edit.clear()  
  
# 主程序  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
  
    widget = QWidget()
    layout = QVBoxLayout(widget)  
  
    # 创建自定义输入框  
    clearable_line_edit = ClearableLineEdit()
    clearable_line_edit.setProperty("type", "clearableLineEdit")  
    layout.addWidget(clearable_line_edit)
    clearable_line_edit.setAttribute(Qt.WA_StyledBackground, True) 
    clearable_line_edit.setStyleSheet("""
        QWidget[type='clearableLineEdit'] {
            background-color: #252525;
            border-radius: 3px;
        }    
        QWidget[type='clearableLineEdit'] QLineEdit {
            background-color: #252525;
            outline: none;
            border: none;
            color: #9c9c9c;
            margin: 3px 1px 3px 8px;
        }
        QToolButton[type='clearButton'] {
        background-color: #252525;  
        border: none;   
        padding: 0;
        margin: 3px 8px 3px 1px; 
    }  
        QToolButton[type='clearButton']:pressed {  
            padding-left: 1px;
            padding-bottom: 1px;
        }  
        """)
    widget.show()  
    sys.exit(app.exec())
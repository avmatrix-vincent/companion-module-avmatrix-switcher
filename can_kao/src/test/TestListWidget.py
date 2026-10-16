import sys
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QScrollBar
from PySide6.QtCore import Qt

class ListWidgetItem(QWidget):
    def __init__(self, text):
        super().__init__()
        layout = QHBoxLayout()
        
        self.label = QLabel(text)
        self.button = QPushButton("按钮")
        
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

class CustomListWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 主布局
        layout = QVBoxLayout()
        
        # 顶部标题
        self.title = QLabel("列表标题")
        self.title.setAlignment(Qt.AlignCenter)
        
        # 列表部件
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet("""
            QListWidget::item {
                border-bottom: 1px solid gray;
            }
        """)
        self.list_widget.setSpacing(2)
        self.list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        layout.addWidget(self.title)
        layout.addWidget(self.list_widget)
        self.setLayout(layout)
    
    def add_items(self, items):
        for item_text in items:
            item_widget = ListWidgetItem(item_text)
            list_widget_item = QListWidgetItem(self.list_widget)
            list_widget_item.setSizeHint(item_widget.sizeHint())
            self.list_widget.addItem(list_widget_item)
            self.list_widget.setItemWidget(list_widget_item, item_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CustomListWidget()
    window.add_items(["选项1", "选项2", "选项3", "选项4"])
    window.resize(300, 400)
    window.show()
    sys.exit(app.exec())

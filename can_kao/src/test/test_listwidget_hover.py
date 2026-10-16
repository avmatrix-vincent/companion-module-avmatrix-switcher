import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PySide6.QtCore import QEvent, QPoint
from globals import global_qss

class CustomListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setProperty("type", "default_listWidget")
        self.setStyleSheet(global_qss)
        self.addItems([f"Item {i + 1}" for i in range(10)])
        self.itemEntered.connect(self.on_item_entered)
        # self.viewport().installEventFilter(self)

    def on_item_entered(self, item):
        if self.row(item) == 0:
            self.setProperty("type", "first_item_hover")
            self.setStyleSheet(global_qss)
        else:
            self.setProperty("type", "default_listWidget")
            self.setStyleSheet(global_qss)

    # def eventFilter(self, source, event):
    #     if event.type() == QEvent.Leave:
    #         self.setProperty("type", "default_listWidget")
    #         self.setStyleSheet(global_qss)
    #     return super().eventFilter(source, event)

if __name__ == "__main__":
    from PySide6.QtGui import QCursor
    app = QApplication(sys.argv)
    listWidget = CustomListWidget()
    listWidget.show()
    sys.exit(app.exec())

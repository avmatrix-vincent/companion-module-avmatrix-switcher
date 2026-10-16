from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject

def my_slot():
    print("Button clicked")

app = QApplication([])

button = QPushButton("Click me")

# 将槽函数连接到按钮的 clicked 信号
button.clicked.connect(my_slot)

# 检查按钮是否连接到槽函数
if button.clicked.isConnected(my_slot):
    print("Button is connected to a slot")
else:
    print("Button is not connected to any slot")

app.exec()

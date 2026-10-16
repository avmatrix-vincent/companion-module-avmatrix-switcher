from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

def show_message_box():
    msg_box = QMessageBox()
    msg_box.setWindowFlags(Qt.FramelessWindowHint)  # 去掉窗口边框
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setText("Are you sure you want to proceed?")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    ret = msg_box.exec()

    if ret == QMessageBox.Yes:
        print("Yes clicked")
    else:
        print("No clicked")

if __name__ == "__main__":
    app = QApplication([])

    main_widget = QWidget()
    layout = QVBoxLayout(main_widget)

    button = QPushButton("Show Message Box")
    button.clicked.connect(show_message_box)
    layout.addWidget(button)

    main_widget.setLayout(layout)
    main_widget.show()

    app.exec()

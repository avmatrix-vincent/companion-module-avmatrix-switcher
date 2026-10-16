from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Qt, Signal, QTimer, QRect, QSize
from PySide6.QtGui import QPainter, QPixmap
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from globals import relative_path

class SwitchBtn(QWidget):
    checkedChanged = Signal(bool)

    def __init__(self, parent=None):
        super(SwitchBtn, self).__init__(parent)

        self.checked = False
        self.space = 2  # Margin space
        self.rectRadius = 5  # Rounded rectangle radius
        self.sliderWidth = 20  # Adjusted slider width for smaller size
        self.sliderPosition = 0
        self.setFixedSize(QSize(40, 24))  # Adjusted size to maintain aspect ratio

        # Load the original pixmap without scaling first
        self.originalSliderPixmap = QPixmap(relative_path("res/images/switch_btn_handle.png"))
        self.originalBackgroundOn = QPixmap(relative_path("res/images/switch_bg_open.png"))
        self.originalBackgroundOff = QPixmap(relative_path("res/images/switch_bg_close.png"))

        self.update_pixmaps()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateValue)

    def update_pixmaps(self):
        self.sliderPixmap = self.originalSliderPixmap.scaled(
            self.sliderWidth, self.height() - self.space * 2, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.backgroundOn = self.originalBackgroundOn.scaled(
            self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.backgroundOff = self.originalBackgroundOff.scaled(
            self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def resizeEvent(self, event):
        self.update_pixmaps()
        super().resizeEvent(event)

    def set_checked(self, checked):
        self.checked = checked
        if self.timer.isActive():
            self.timer.stop()
        self.update_slider_position()
        self.timer.start()

    def updateValue(self):
        if self.checked:
            if self.sliderPosition < self.width() - self.sliderWidth:
                self.sliderPosition += 1
            else:
                self.sliderPosition = self.width() - self.sliderWidth
                self.timer.stop()
        else:
            if self.sliderPosition > 0:
                self.sliderPosition -= 1
            else:
                self.sliderPosition = 0
                self.timer.stop()

        self.update()

    def update_slider_position(self):
        if self.checked:
            self.sliderPosition = self.width() - self.sliderWidth if self.timer.isActive() else self.width() - self.sliderWidth
        else:
            self.sliderPosition = 0 if self.timer.isActive() else 0

    def mousePressEvent(self, event):
        self.checked = not self.checked
        self.checkedChanged.emit(self.checked)
        self.timer.start(5)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # Draw background
        if self.checked:
            painter.drawPixmap(self.rect(), self.backgroundOn)
        else:
            painter.drawPixmap(self.rect(), self.backgroundOff)
        # Draw slider
        sliderRect = QRect(self.sliderPosition, self.space+1, self.sliderWidth, self.height() - 2 * self.space)
        painter.drawPixmap(sliderRect, self.sliderPixmap)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400, 200)
        self.switchBtn = SwitchBtn(self)
        self.switchBtn.set_checked(True)
        self.switchBtn.setGeometry(10, 10, 40, 24)  # Adjusted size to match SwitchBtn
        self.switchBtn.checkedChanged.connect(self.getState)

    def getState(self, checked):
        print("checked=", checked)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

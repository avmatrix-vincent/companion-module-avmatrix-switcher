from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal, QPropertyAnimation, QTimer, QRect

class AnimatedSplashScreen(QWidget):
    animation_finished = Signal()

    def __init__(self, top_image_path, bottom_image_path):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 获取屏幕几何尺寸
        screen_geometry = QApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Load images
        top_pixmap = QPixmap(top_image_path)
        bottom_pixmap = QPixmap(bottom_image_path)

        # Calculate initial and final positions
        pixmap_height = top_pixmap.height()
        pixmap_width = top_pixmap.width()
        center_x = (screen_width - pixmap_width) // 2
        center_y = screen_height // 2

        # Create labels
        self.top_label = QLabel(self)
        self.top_label.setPixmap(top_pixmap)
        self.top_label.setGeometry(center_x, center_y - pixmap_height, top_pixmap.width(), top_pixmap.height())

        self.bottom_label = QLabel(self)
        self.bottom_label.setPixmap(bottom_pixmap)
        self.bottom_label.setGeometry(center_x, center_y, bottom_pixmap.width(), bottom_pixmap.height())

        self.setGeometry(0, 0, screen_width, screen_height)

        # Create animations
        self.top_animation = QPropertyAnimation(self.top_label, b"geometry")
        self.top_animation.setDuration(500)
        self.top_animation.setStartValue(QRect(center_x, center_y - pixmap_height, top_pixmap.width(), top_pixmap.height()))
        self.top_animation.setEndValue(QRect(center_x, -pixmap_height, top_pixmap.width(), top_pixmap.height()))

        self.bottom_animation = QPropertyAnimation(self.bottom_label, b"geometry")
        self.bottom_animation.setDuration(500)
        self.bottom_animation.setStartValue(QRect(center_x, center_y, bottom_pixmap.width(), bottom_pixmap.height()))
        self.bottom_animation.setEndValue(QRect(center_x, screen_height, bottom_pixmap.width(), bottom_pixmap.height()))

        self.top_animation.finished.connect(self.on_animation_finished)
        
    def start_animation(self):
        # 添加一个计时器来延迟动画的启动
        QTimer.singleShot(1000, self.top_animation.start)  # 1秒延迟
        QTimer.singleShot(1000, self.bottom_animation.start)  # 1秒延迟

    def on_animation_finished(self):
        self.animation_finished.emit()
        self.close()

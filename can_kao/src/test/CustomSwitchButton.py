import sys  
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout  
from PySide6.QtCore import Qt, Signal, QTimer, QRect, QRectF, QSize
from PySide6.QtGui import QColor, QFont, QPainter, QPainterPath, QPixmap, QLinearGradient, QRadialGradient, QBrush, QPen
  
class SwitchBtn(QWidget):
    
    checkedChanged = Signal(bool)

    def __init__(self, parent=None):
        super(SwitchBtn, self).__init__(parent)

        self.checked = False
        self.bgColorOn_top = QColor("#a9761d")
        self.bgColorOn_bottom = QColor("#e5d2b1")
        self.bgColorOff_top = QColor("#4a4a4a")
        self.bgColorOff_bottom = QColor("#ababab")

        self.sliderColorOff = QColor("#8b9596")
        self.sliderColorOn = QColor("#beb8bc")

        self.space = 2
        self.rectRadius = 5

        self.step = self.width() / 50
        self.startX = 0
        self.endX = 0

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.updateValue)

        self.sliderPixmap = QPixmap(r"res\images\slider.png")  # 替换为你的图标路径  
        self.sliderPixmap = self.sliderPixmap.scaled(self.sliderPixmap.width() - self.space * 2,  
                                                        self.sliderPixmap.height() - self.space * 2,  
                                                       Qt.KeepAspectRatio,  
                                                       Qt.SmoothTransformation)
        
        self.setFixedSize(QSize(40, 20))

    def set_checked(self, checked):
        self.checked = checked
        if self.timer.isActive():
            self.timer.stop()
        self.update_slider_position()
        self.timer.start()

    def updateValue(self):
        if self.checked:
            if self.startX < self.endX:
                self.startX = self.startX + self.step
            else:
                self.startX = self.endX
                self.timer.stop()
        else:
            if self.startX  > self.endX:
                self.startX = self.startX - self.step
            else:
                self.startX = self.endX
                self.timer.stop()

        self.update()

    def update_slider_position(self):
        # 状态切换改变后自动计算终点坐标
        if self.checked:
            self.endX = self.width() - self.height()
            self.startX = self.endX if self.timer.isActive() else self.width() - self.height()
        else:
            self.endX = 0
            self.startX = self.endX if self.timer.isActive() else 0

    def mousePressEvent(self, event):
        self.checked = not self.checked
        # 发射信号
        self.checkedChanged.emit(self.checked)

        # 每次移动的步长为宽度的50分之一
        self.step = self.width() / 50
        # 状态切换改变后自动计算终点坐标
        if self.checked:
            self.endX = self.width() - self.height()
        else:
            self.endX = 0
        self.timer.start(5)

    def paintEvent(self, evt):
        # 绘制准备工作, 启用反锯齿
            painter = QPainter()
            painter.begin(self)
            painter.setRenderHint(QPainter.Antialiasing)
            # 绘制背景
            self.drawBg(evt, painter)
            # 绘制滑块
            self.drawSlider(evt, painter)
            painter.end()

    def drawBg(self, event, painter):  
        painter.save()  
        painter.setPen(Qt.NoPen)  

        # 创建线性渐变
        gradient = QLinearGradient(0, 0, 0, self.height())
        if self.checked:
            gradient.setColorAt(0, self.bgColorOn_top)
            gradient.setColorAt(1, self.bgColorOn_bottom)
        else:
            gradient.setColorAt(0, self.bgColorOff_top)
            gradient.setColorAt(1, self.bgColorOff_bottom)

        painter.setBrush(QBrush(gradient))

        # 设置小圆与水平条的高度差距
        gap = 3  # 根据需要调整这个值  
        available_height = self.height() - 2 * gap  # 减去顶部和底部的空隙  
        
        # 调整矩形的位置和大小以创建空隙  
        rect = QRect(0, gap, self.width(), available_height)  
        
        # 半径为可用高度的一半  
        radius = available_height / 2
        # 圆的宽度仍然为可用高度  
        circleWidth = available_height-1

        path = QPainterPath()  
        path.moveTo(radius, rect.top())  
        path.arcTo(QRectF(rect.left()+3, rect.top(), circleWidth, circleWidth), 90, 180)  
        path.lineTo(rect.width() - radius, rect.bottom())  
        path.arcTo(QRectF(rect.width() - circleWidth, rect.top(), circleWidth-3, circleWidth), 270, 180)  
        path.lineTo(radius, rect.top())  
        
        painter.drawPath(path)  

        # # 绘制黑色边框
        # border_color = QColor("#1e1915")
        # border_width = 1
        # painter.setPen(QPen(border_color, border_width))
        # painter.drawRoundedRect(rect.adjusted(border_width / 2, border_width / 2, -border_width / 2, -border_width / 2), radius, radius)

        painter.restore()

    # def drawBg(self, event, painter):  
    #     painter.save()  
    #     painter.setPen(Qt.NoPen)  

    #     # 创建线性渐变
    #     gradient = QLinearGradient(0, 0, 0, self.height())
    #     gradient.setColorAt(0, QColor("#a9761d"))
    #     gradient.setColorAt(1, QColor("#e5d2b1"))

    #     painter.setBrush(QBrush(gradient))

    #     # 假设你想要在顶部和底部各保留gap个像素的空间  
    #     gap = 3  # 你可以根据需要调整这个值  
    #     available_height = self.height() - 2 * gap  # 减去顶部和底部的空隙  
        
    #     # 调整矩形的位置和大小以创建空隙  
    #     rect = QRect(0, gap, self.width(), available_height)  
        
    #     # 半径为可用高度的一半  
    #     radius = available_height / 2
    #     # 圆的宽度仍然为可用高度  
    #     circleWidth = available_height-1

    #     path = QPainterPath()  
    #     path.moveTo(radius, rect.top())  
    #     path.arcTo(QRectF(rect.left()+3, rect.top(), circleWidth, circleWidth), 90, 180)  
    #     path.lineTo(rect.width() - radius, rect.bottom())  
    #     path.arcTo(QRectF(rect.width() - circleWidth, rect.top(), circleWidth-3, circleWidth), 270, 180)  
    #     path.lineTo(radius, rect.top())  
        
    #     painter.drawPath(path)  
    #     painter.restore()

    def drawSlider(self, event, painter):
        painter.save()

        if self.checked:
            painter.setBrush(self.sliderColorOn)
        else:
            painter.setBrush(self.sliderColorOff)

        rect = QRect(0, 0, self.width(), self.height())
        sliderWidth = rect.height() - self.space * 2
        sliderRect = QRect(self.startX + self.space, self.space, sliderWidth, sliderWidth)
        painter.drawEllipse(sliderRect)

        painter.restore() 


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400,200)
        self.switchBtn = SwitchBtn(self)
        self.switchBtn.set_checked(True)
        self.switchBtn.setGeometry(10,10,60,30)
        self.switchBtn.checkedChanged.connect(self.getState)

    def getState(self,checked):
        print("checked=", checked)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    #form = SwitchBtn()
    form.show()
    sys.exit(app.exec())
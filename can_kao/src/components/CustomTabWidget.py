from PySide6.QtWidgets import QTabWidget, QLabel, QVBoxLayout, QHBoxLayout, QTabBar, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from globals import global_qss


class CustomTabWidget(QTabWidget):
    """ 
        每个设备的一级菜单对应的QTabWidget
        包含二级菜单和内部的页面
    """

    def __init__(self, args, controller, parent=None):
        super().__init__(parent)
        self.args = args
        self.controller = controller
        self.currentChanged.connect(self.tab_change)

    def resizeEvent(self, event): # 使Tab选项卡宽度自动均匀分配
        self.resize_tab_width()
        self.single_tab_repaint_radius()

    def resize_tab_width(self):
        # 获取当前窗口宽度和选项卡数量
        tab_count = self.count()
        total_width = self.width()
        if tab_count > 0:
            # 计算每个选项卡的宽度
            tab_width = total_width // tab_count
            # 如果存在余数，将剩余的像素分配给最后一个选项卡
            remainder = total_width % tab_count
            qss = "QTabBar::tab { height: 40px; width: %spx; }" % str(tab_width)
            if remainder > 0:
                last_tab_width = tab_width + remainder
                qss += "QTabBar::tab:last { width: %spx; }" % str(last_tab_width)
            self.tabBar().setStyleSheet(qss)  

    def single_tab_repaint_radius(self):
        if self.count() == 1: # 改变单tab的页面圆角样式
            self.tabBar().setProperty("type", "single_tab")
            self.currentWidget().setProperty("type", "single_tabwidget")
            self.setStyleSheet(global_qss)

    def showEvent(self, event):
        index = self.currentIndex()
        self.tab_change(index) # 防止点击一级菜单并未触发QTabWidget切换选项卡，而内部页面左上角还是圆角的问题
        self.single_tab_repaint_radius()
        super().showEvent(event)

    def tab_change(self, index): # 切换tab页时控制圆角
        ''' Tab页的第一页和最后一页顶部圆角取消 '''
        if index == 0:
            self.tabBar().setProperty("type", "center")
            self.currentWidget().setProperty("type", "left_tab_inner_widget")
            self.setStyleSheet(global_qss)
        elif index == self.count() - 1:
            self.tabBar().setProperty("type", "right")
            self.currentWidget().setProperty("type", "right_tab_inner_widget")
            self.setStyleSheet(global_qss)
        else:
            self.tabBar().setProperty("type", "center")
            self.currentWidget().setProperty("type", "center_tab_inner_widget")
            self.setStyleSheet(global_qss)
        self.resize_tab_width() 

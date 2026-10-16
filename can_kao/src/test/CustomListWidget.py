from PySide6.QtWidgets import QApplication, QListWidget, QStyledItemDelegate, QListWidgetItem, QStyleOptionViewItem, QStyle
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QPainterPath, QLinearGradient
from PySide6.QtCore import Qt, QRect, QSize, QModelIndex
  
class CustomDelegate(QStyledItemDelegate):  
    def __init__(self, parent=None):  
        super().__init__(parent)  
        self.selected_color = QColor("#888888")  # 选中项的背景色  
        self.shadow_color = QColor("#444444")  # 阴影颜色  
  
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):  
        painter.save()  
  
        # 检查项是否被选中  
        if option.state & QStyle.State_Selected:
            print("选中")  
            # 绘制立体凹陷效果  
            rect = option.rect  
              
            # 绘制阴影  
            shadow_rect = QRect(rect.x(), rect.y() + 5, rect.width() - 5, rect.height() - 5)  
            painter.setPen(QPen(Qt.NoPen))  
            painter.setBrush(QBrush(self.shadow_color))  
            painter.drawRect(shadow_rect)  
  
            # 绘制背景  
            painter.setBrush(QBrush(self.selected_color))  
            if index.row() == 0:  
                print("第一项")
                # 对于第一项，绘制带有上圆角的矩形  
                path = QPainterPath()  
                path.addRoundedRect(rect.x(), rect.y(), rect.width(), rect.height(), 0, 10)  
                painter.drawPath(path)  
            else:  
                # 其他项绘制矩形  
                painter.drawRect(rect)  
  
            # 绘制文本（如果需要）  
            # ...  
  
        # 绘制未选中的项（如果需要）  
        # ...  
  
        painter.restore()  
  
# 其余代码与之前的示例相同  
app = QApplication([])  
list_widget = QListWidget()  
list_widget.setItemDelegate(CustomDelegate())  
list_widget.setSpacing(0)  
  
# 添加项到QListWidget  
for i in range(5):  
    item = QListWidgetItem(f"Item {i+1}")  
    list_widget.addItem(item)  
  
list_widget.show()  
app.exec()
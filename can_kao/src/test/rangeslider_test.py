from PySide6.QtWidgets import QApplication, QComboBox, QStyledItemDelegate, QStyle, QStyleOptionViewItem, QStyleOptionButton
from PySide6.QtCore import Qt, QRect, QEvent, QModelIndex
from PySide6.QtGui import QPainter, QPalette, QColor

class CheckBoxDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        option = QStyleOptionViewItem(option)
        self.initStyleOption(option, index)
        option.features &= ~QStyleOptionViewItem.HasCheckIndicator  # 隐藏左侧默认复选框
        style = option.widget.style() if option.widget else QApplication.style()
        style.drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)

        # 绘制右侧复选框
        check_state = index.data(Qt.CheckStateRole)
        opt = QStyleOptionButton()
        opt.rect = QRect(option.rect.right() - 20, option.rect.top(), 20, option.rect.height())
        opt.state = QStyle.State_Enabled | QStyle.State_Active
        opt.state |= QStyle.State_On if check_state == Qt.Checked else QStyle.State_Off

        # 绘制右侧复选框
        check_state = index.data(Qt.CheckStateRole)
        opt = QStyleOptionButton()
        opt.rect = QRect(option.rect.right() - 20, option.rect.top(), 20, option.rect.height())
        opt.state = QStyle.State_Enabled | QStyle.State_Active
        if check_state == Qt.Checked:
            opt.state |= QStyle.State_On
            color = QColor(Qt.red)  # 选中时为红色
        else:
            opt.state |= QStyle.State_Off
            color = QColor(Qt.blue)  # 未选中时为蓝色

        # 继承原始调色板并设置颜色
        opt.palette = option.palette
        opt.palette.setColor(QPalette.ButtonText, color)
        opt.palette.setColor(QPalette.WindowText, color)
        
        style.drawControl(QStyle.CE_CheckBox, opt, painter)

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.MouseButtonRelease:
            checkbox_rect = QRect(option.rect.right() - 20, option.rect.top(), 20, option.rect.height())
            if checkbox_rect.contains(event.pos()):
                current_state = index.data(Qt.CheckStateRole)
                if current_state != Qt.Checked:
                    for row in range(model.rowCount()):
                        other_index = model.index(row, 0)
                        if other_index.data(Qt.CheckStateRole) == Qt.Checked:
                            model.setData(other_index, Qt.Unchecked, Qt.CheckStateRole)
                    model.setData(index, Qt.Checked, Qt.CheckStateRole)
                return True
        return super().editorEvent(event, model, option, index)

class SingleCheckComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setItemDelegate(CheckBoxDelegate())
        self.model().dataChanged.connect(self._on_data_changed)
        self.setStyleSheet("")

    def setCheckedItem(self, index):
        model = self.model()
        for row in range(model.rowCount()):
            other_index = model.index(row, 0)
            if other_index.data(Qt.CheckStateRole) == Qt.Checked:
                model.setData(other_index, Qt.Unchecked, Qt.CheckStateRole)
        model.setData(model.index(index, 0), Qt.Checked, Qt.CheckStateRole)

    def _on_data_changed(self, top_left, bottom_right, roles):
        if Qt.CheckStateRole in roles:
            for row in range(top_left.row(), bottom_right.row() + 1):
                idx = self.model().index(row, 0)
                if idx.data(Qt.CheckStateRole) == Qt.Checked:
                    self.setCurrentIndex(row)
                    break

    def event(self, event):
        if event.type() == QEvent.StyleChange:
            self.view().setStyleSheet(self.styleSheet())
        return super().event(event)

# 示例用法
if __name__ == "__main__":
    app = QApplication([])
    combo = SingleCheckComboBox()
    combo.addItems(["选项1", "选项2", "选项3", "选项4"])
    combo.setCheckedItem(2)
    combo.setStyleSheet("""
        /* 主控件样式 */
        SingleCheckComboBox {   
            border-radius: 5px;  
            padding: 5px 5px 5px 8px;
            margin-right: 0;
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4b4b4b, stop:0.55 #2e2e2e, stop:1 #242424);
            color: #959595; 
        }

        /* 下拉按钮样式 */
        SingleCheckComboBox::drop-down { 
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4b4b4b, stop:0.55 #2e2e2e, stop:1 #242424);
            subcontrol-origin: padding;   
            border-top-right-radius: 5px;  
            border-bottom-right-radius: 5px;  
        }  

        /* 下拉箭头图标 */
        SingleCheckComboBox::down-arrow {  
            image: url(:/icons/images/drop_arrow.png);
            background-color: transparent;
            padding-right: 8px;
        }  

        /* 下拉列表样式 */
        SingleCheckComboBox QAbstractItemView {
            outline: none;
            border: none;
            background-color: #1c1c1c;
            padding: 5px 5px 5px 5px;
            color: #959595;
        }

        /* 选中项样式（控制勾号颜色） */
        SingleCheckComboBox QAbstractItemView::item:selected {
            background-color: #f39801;  /* 选中背景色 */
            color: white;               /* 选中文本色（勾号颜色继承此值） */
            border-radius: 3px;
            margin-right: 5px;
        }

        /* 其他滚动条样式 */
        SingleCheckComboBox QAbstractItemView QScrollBar::handle:vertical {
            border-radius: 5px;
            background-color: #2f2f2f;
        }
        /* ... 其他滚动条样式省略 ... */
    """)
    combo.show()
    app.exec()
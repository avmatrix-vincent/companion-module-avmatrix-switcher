from PySide6.QtWidgets import QApplication, QComboBox, QStyledItemDelegate, QStyle, QStyleOptionViewItem, QStyleOptionButton
from PySide6.QtCore import Qt, QRect, QEvent, QPoint, QModelIndex
from PySide6.QtGui import QPainter, QPalette, QColor

class CheckBoxDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        # 确保样式表生效：使用 QStyle 绘制默认背景和文本
        option = QStyleOptionViewItem(option)
        self.initStyleOption(option, index)
        option.features &= ~QStyleOptionViewItem.HasCheckIndicator  # 禁止左侧默认复选框
        style = option.widget.style() if option.widget else QApplication.style()
        style.drawControl(QStyle.CE_ItemViewItem, option, painter, option.widget)

        # 绘制右侧复选框
        check_state = index.data(Qt.CheckStateRole)
        opt = QStyleOptionButton()
        opt.rect = QRect(option.rect.right() - 20, option.rect.top(), 20, option.rect.height())
        opt.state = QStyle.State_Enabled | QStyle.State_Active
        if check_state == Qt.Checked:
            opt.state |= QStyle.State_On
        else:
            opt.state |= QStyle.State_Off

        # 继承原始调色板并设置颜色
        opt.palette = option.palette
        # opt.palette.setColor(QPalette.ButtonText, color)
        # opt.palette.setColor(QPalette.WindowText, color)
        
        style.drawControl(QStyle.CE_CheckBox, opt, painter)

class SingleCheckComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setItemDelegate(CheckBoxDelegate())
        self.model().dataChanged.connect(self._on_data_changed)
        self.setStyleSheet("")  # 初始化空样式表以启用子控件样式

    def setCheckedItem(self, index):
        """Select an item by index and uncheck all other items"""
        model = self.model()
        # Uncheck all items first
        for row in range(model.rowCount()):
            other_index = model.index(row, 0)
            if other_index.data(Qt.CheckStateRole) == Qt.Checked:
                model.setData(other_index, Qt.Unchecked, Qt.CheckStateRole)
        # Check the specified item
        model.setData(model.index(index, 0), Qt.Checked, Qt.CheckStateRole)
        # self.setCurrentIndex(index)

    def _on_data_changed(self, top_left, bottom_right, roles):
        if Qt.CheckStateRole in roles:
            for row in range(top_left.row(), bottom_right.row() + 1):
                idx = self.model().index(row, 0)
                if idx.data(Qt.CheckStateRole) == Qt.Checked:
                    self.setCurrentIndex(row)
                    break

    # 启用 QSS 样式继承
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
    combo.setCheckedItem(3)
    # 应用用户提供的 QSS 样式表
    combo.setStyleSheet("""
        SingleCheckComboBox {   
            border-radius: 5px;  
            padding: 5px 5px 5px 8px;
            margin-right: 0;
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4b4b4b, stop:0.55 #2e2e2e, stop:1 #242424);
            color: #959595; 
        }

        SingleCheckComboBox::drop-down { 
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4b4b4b, stop:0.55 #2e2e2e, stop:1 #242424);
            subcontrol-origin: padding;   
            border-top-right-radius: 5px;  
            border-bottom-right-radius: 5px;  
        }  

        SingleCheckComboBox::down-arrow {  
            image: url(:/icons/images/drop_arrow.png);
            background-color: transparent;
            padding-right: 8px;
        }  

        SingleCheckComboBox QAbstractItemView {
            outline: none;
            border: none;
            background-color: #1c1c1c;
            padding: 5px 5px 5px 5px;
            color: #959595;
        }

        SingleCheckComboBox QAbstractItemView::item:selected {
            background-color: #f39801;
            color: black;
            border-radius: 3px;
            margin-right: 5px;
        } 

        SingleCheckComboBox QAbstractItemView QScrollBar::handle:vertical {
            border-radius: 5px;
            background-color: #2f2f2f;
        }

        SingleCheckComboBox QAbstractItemView QScrollBar:vertical {
            padding-top: 20px;
            padding-bottom: 20px;
            background-color: #1c1c1c;
            border-radius: 2px;
        }

        SingleCheckComboBox QAbstractItemView QScrollBar::add-page:vertical,
        SingleCheckComboBox QAbstractItemView QScrollBar::sub-page:vertical {
            background-color: #1c1c1c;
        }

        SingleCheckComboBox QAbstractItemView QScrollBar::add-line:vertical {
            background-color: #1c1c1c;
            border-bottom-left-radius: 5px;
            border-bottom-right-radius: 5px;
            image: url(:/icons/images/down.png);
        }

        SingleCheckComboBox QAbstractItemView QScrollBar::sub-line:vertical {
            background-color: #1c1c1c;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
            image: url(:/icons/images/up.png);
        }

        SingleCheckComboBox QAbstractItemView QCheckBox::indicator:checked {
            /* image: url(:/icons/images/checked.png); */
            border-image: url(:/icons/images/checked.png);
            border-radius: 2px;
        }
    """)
    combo.show()
    app.exec()
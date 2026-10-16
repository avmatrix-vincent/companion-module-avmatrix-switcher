import os
import sys, logging
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDialog, QSpacerItem, QSizePolicy, QComboBox
from PySide6.QtCore import QObject, QSize, Signal, Qt, QAbstractListModel, QCoreApplication, QPoint
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtTest import QTest
from globals import relative_path, global_qss
from src.avm_stack.avm_manager import singletonManager
from src.config.TranslationManager import TranslationManager
from src.avm_stack.heartbeat import HeartbeatManager
from src.view.cue01.CUE01PagesController import CUE01Controller
from src.components.ClearableLineEdit import ClearableLineEdit
from src.config.TranslationManager import TranslationManager

class DeviceWidget(QWidget):
    """ 可点击的设备控件 """

    clicked = Signal()
    delete_signal = Signal()
    # setting_signal = Signal() 
    rename_signal = Signal()

    def __init__(self, parent, args, send_heartbeat_callback=None):
        self.mainui = parent
        super().__init__(self.mainui.left_left_widget)
        # super().__init__()
        self.original_size = None  
        self.original_pos = None 
        self.origin_btn_size = None 
        self.is_pressed = False
        self.allow_show_panel = True
        # self.name = args["name"] # 模拟
        self.__model = args["model"]
        self.__device_name = args["name"]
        self.__address = args["addr"][0] if "addr" in args else args["sn"]
        self.__is_activate = False
        # self.__interface_name = args["interface"]
        self.__serial_number = args["sn"]
        self._parent = parent
        self._args = args
        self.init_ui()
        self.setMaximumSize(QSize(170, 97))
        self.setObjectName(self.__device_name)
        self.setProperty("type", "device_widget")

        self.setAttribute(Qt.WA_StyledBackground, True) # 这句不加，背景颜色不生效

        self.hearbeatManager = HeartbeatManager(args, send_heartbeat_callback)

        self.retranslateUi()
    
    def init_ui(self):
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(5, 7, 5, 7)
        widget_vertical_layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        self.device_name_label = QLabel(self)
        self.device_name_label.setText(self.__device_name)
        self.device_name_label.setProperty("type", "device_name")
        self.device_name_label.setAlignment(Qt.AlignCenter)  # 文本居中
        self.little_button = QPushButton()
        self.little_button.setObjectName("little_x_btn")
        self.little_button.setFixedSize(QSize(15, 15))
        self.little_button.setIcon(QIcon(relative_path("res/images/delete.png")))
        # self.little_button.clicked.connect(self.delete_signal.emit)

        top_layout.addSpacing(5)
        top_layout.addWidget(self.device_name_label)
        top_layout.addStretch()
        top_layout.addWidget(self.little_button)
        # top_layout.addSpacing(5)
        self.hori_spacer_1 = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        top_layout.addSpacerItem(self.hori_spacer_1)
        self.hori_spacer_1.changeSize(5, 0)

        hbox = QHBoxLayout()
        self.tip_light_label = QLabel()
        self.tip_light_label.setProperty("tip_bar", "dark")
        # self.tip_light_label.setPixmap(QPixmap("res/images/设备未选中.png"))
        self.tip_light_label.setFixedSize(QSize(60, 12))
        address_hbox = QHBoxLayout()
        address_label = QLabel(self.__address)
        address_label.setProperty("type", "address")
        address_hbox.addSpacing(5)
        address_hbox.addWidget(address_label)
        hbox.addWidget(self.tip_light_label)
        hbox.addStretch()

        button_layout = QHBoxLayout()
        self.delete_button = QPushButton(self.tr("Delete"))
        self.rename_button = QPushButton(self.tr("Rename"))
        self.delete_button.setProperty("type", "device_btn")
        self.rename_button.setProperty("type", "device_btn")
        button_layout.addSpacing(5)
        button_layout.addWidget(self.rename_button)
        button_layout.addSpacing(5)
        button_layout.addWidget(self.delete_button)
        button_layout.addSpacing(5)
        self.rename_button.clicked.connect(self.rename_signal.emit)
        self.delete_button.clicked.connect(self.delete_signal.emit)

        self.clicked.connect(self._notify_device_activate)

        widget_vertical_layout.setSpacing(3)
        widget_vertical_layout.addLayout(top_layout)
        widget_vertical_layout.addLayout(hbox)
        widget_vertical_layout.addLayout(address_hbox)
        widget_vertical_layout.addLayout(button_layout)

        self.main_layout.addLayout(widget_vertical_layout)
        self.hori_spacer_2 = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        self.main_layout.addSpacerItem(self.hori_spacer_2)

    def trigger_click(widget):
        QTest.mouseClick(widget, Qt.LeftButton)

    def mousePressEvent(self, event):
        # print("Widget Clicked")
        if event.button() == Qt.LeftButton:  
            self.is_pressed = True  
            self.original_size = self.size()
            self.origin_btn_size = self.delete_button.size()
            self.original_pos = self.pos() 
            new_pos = self.original_pos + QPoint(3, 3)
            # 缩小、移动
            self.setMaximumSize(self.original_size.width()-6, self.original_size.height()-6)
            self.delete_button.resize(self.origin_btn_size.width()-2, self.origin_btn_size.height()) # 目前必须时宽度-2，其他值会导致出问题
            self.rename_button.resize(self.origin_btn_size.width()-2, self.origin_btn_size.height())
            self.move(new_pos)
            # 缩小设备名称
            self.device_name_label.setProperty("type", "device_name_reduce")
            self.device_name_label.setStyleSheet(global_qss)
  
    def mouseReleaseEvent(self, event):  
        if event.button() == Qt.LeftButton and self.is_pressed:  
            self.is_pressed = False
            self._notify_device_activate()
            # 恢复原始大小  
            self.resize(self.original_size)
            self.delete_button.resize(self.origin_btn_size)
            self.rename_button.resize(self.origin_btn_size)
            self.move(self.original_pos)
            # 恢复设备名称字体大小
            self.device_name_label.setProperty("type", "device_name")
            self.device_name_label.setStyleSheet(global_qss)

    def _notify_device_activate(self):
        if not self.allow_show_panel:
            logging.warning(f"Device {self.__device_name} is disconnected, can't be activated!")
            return
        self.__is_activate = True
        args = {
            "message_type": "activate",
            "message": {
                "type": "activate",
                "device_type": "normal",
                "sn": self.__serial_number,
                "name": self.__device_name,
                "model": self.__model,
                "args": self._args
                # "interface": self.__interface_name,
            }
        }
        singletonManager.dispatch(args)
        self.hearbeatManager.start() # 开始发送心跳包

    def get_device_name(self):
        return self.__device_name

    def set_serial_number(self, sn):
        self.__serial_number = sn

    def get_serial_number(self):
        return self.__serial_number

    def get_model(self):
        return self.__model

    def show_activate(self):
        self.__is_activate = True
        self.setMaximumSize(QSize(177, 97))
        self.setProperty("status", "selected")
        self.tip_light_label.setProperty("tip_bar", "light")
        self.setStyleSheet(global_qss)
        self.hori_spacer_2.changeSize(5, 0) 

    def clear_activate(self):
        self.__is_activate = False
        self.setMaximumSize(QSize(170, 97))
        self.setProperty("status", "unselected")
        self.tip_light_label.setProperty("tip_bar", "dark")
        self.setStyleSheet(global_qss)
        self.hori_spacer_2.changeSize(0, 0)

    def get_activate(self):
        return self.__is_activate

    def create_control_pannel(self):
        # 此处应该依据model名称来产生对应的对象
        return CUE01Controller(self.mainui, self._args)

    def retranslateUi(self):
        self.rename_button.setText(self.tr("Rename"))
        if self.delete_button.text() in ["删除", "Delete"]:
            self.delete_button.setText(self.tr("Delete"))
        else:
            self.delete_button.setText(self.tr("Setting"))


class DeviceMiniWidget(QWidget):
    """ 折叠后的可点击的设备控件 """

    # clicked = Signal(QObject)

    def __init__(self, main_ui, parent, args):
        self.mainui = main_ui
        super().__init__(parent)
        self.original_size = None  
        self.original_pos = None 
        self.origin_btn_size = None 
        self.is_pressed = False
        # self.name = args["name"] # 模拟
        self.__model = args["model"]
        self.__device_name = args["name"]
        # self.__address = args["addr"][0]
        self.__is_activate = False
        # self.__interface_name = args["interface"]
        self.__serial_number = args["sn"]
        self._parent = parent
        self._args = args
        self.init_ui()

        # self.setMaximumSize(QSize(50, 90))
        # self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)  
        self.setFixedSize(QSize(50, 90))
        self.setProperty("type", "mini")
        self.setAttribute(Qt.WA_StyledBackground, True) # 这句不加，背景颜色不生效

    def init_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.device_name_label = QLabel(self.__device_name[0:2] + ".." + self.__device_name[-2:])
        self.device_name_label.setProperty("type", "mini_device_name")
        self.device_logo_label = QLabel()
        self.device_logo_label.setPixmap(QPixmap(relative_path("res/images/device_icon.png")))
        self.tip_light_label = QLabel()
        self.tip_light_label.setProperty("tip_bar", "light")
        self.tip_light_label.setMaximumSize(QSize(30, 4))
        self.main_layout.addWidget(self.device_name_label)
        self.main_layout.addWidget(self.device_logo_label)
        self.main_layout.addWidget(self.tip_light_label)

    def _notify_device_activate(self):
        self.__is_activate = True
        args = {
            "message_type": "activate",
            "message": {
                "type": "activate",
                "device_type": "mini",
                "sn": self.__serial_number,
                "name": self.__device_name,
                "model": self.__model,
                "args": self._args
                # "interface": self.__interface_name,
            }
        }

        singletonManager.dispatch(args)

    def set_serial_number(self, sn):
        self.__serial_number = sn

    def get_serial_number(self):
        return self.__serial_number

    def show_activate(self):
        self.__is_activate = True
        self.setProperty("status", "mini_active")
        self.tip_light_label.setProperty("tip_bar", "light")
        self.setStyleSheet(global_qss)

    def clear_activate(self):
        self.__is_activate = False
        self.setProperty("status", "mini")
        self.tip_light_label.setProperty("tip_bar", "dark")
        self.setStyleSheet(global_qss)

    def get_activate(self):
        return self.__is_activate

    def create_control_pannel(self):
        # 此处应该依据model名称来产生对应的对象
        return CUE01Controller(self.mainui, self._args)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: 
            self.is_pressed = True
            self.setStyleSheet("margin: 3px;")

    def mouseReleaseEvent(self, event):
        self.is_pressed = False
        self.setStyleSheet("margin: 0;")
        self._notify_device_activate()
        # self.setProperty("mini_status", "active")
        # self.setStyleSheet(global_qss)
        # self.clicked.emit(self)

class RenameDialog(QDialog):

    rename_text_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.setFixedSize(180, 100)
        self.setProperty("type", "rename")
        self.setWindowIcon(QIcon(relative_path("res/images/rename.png")))

    def initUI(self):
        self.setWindowTitle(self.tr('Rename'))
        layout = QVBoxLayout()
        self.input_edit = ClearableLineEdit(self)
        layout.addWidget(self.input_edit)
        hbox = QHBoxLayout()
        button = QPushButton(self.tr('OK'), self)
        button.clicked.connect(self.submitClicked)
        hbox.addStretch()
        hbox.addWidget(button)
        hbox.addStretch()
        layout.addLayout(hbox)

        self.setLayout(layout)

        button.setFixedWidth(70)
        button.setProperty("type", "device_btn")

    def submitClicked(self):
        input_text = self.input_edit.line_edit.text()
        if input_text.strip() == "": return
        self.rename_text_signal.emit(input_text)
        self.close()

class SettingDialog(QDialog):

    retranslate_signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        # self.setFixedSize(400, 80)
        self.setProperty("type", "rename")
        self.setWindowIcon(QIcon(relative_path("res/images/setting.png")))
        self.setWindowTitle(self.tr("Setting"))

        self.apply_button.clicked.connect(self.apply_setting)
        self.cancel_button.clicked.connect(self.close)
        self.language_combo.currentIndexChanged.connect(self.change_index)

        self.language_combo.setCurrentIndex(TranslationManager().current_language_index)
        
    def initUI(self):
        self.language_combo = QComboBox()
        self.apply_button = QPushButton(self.tr("Apply"))
        self.cancel_button = QPushButton(self.tr("Cancel"))

        items = [self.tr(item) for item in TranslationManager._language_items]
        self.language_combo.addItems(items)

        # 水平布局：标签和下拉框
        h_layout = QHBoxLayout()
        h_layout.addWidget(QLabel(self.tr("Software Language:")))
        h_layout.addSpacing(18)
        h_layout.addWidget(self.language_combo)

        # 水平布局：按钮
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.apply_button)
        button_layout.addStretch()
        button_layout.addWidget(self.cancel_button)
        button_layout.addStretch()

        # 垂直布局：上面的水平布局和按钮布局
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(button_layout)

        # 设置主布局
        self.setLayout(v_layout)

        self.language_combo.setFixedWidth(150)

    def change_index(self, index):
        # global current_language_index
        # current_language_index = index
        pass

    def apply_setting(self):
        index = self.language_combo.currentIndex()
        TranslationManager().current_language_index = index
        logging.info(f"改变全局语言下标：{index}")
        TranslationManager().set_language(index)
        self.retranslate_signal.emit(index)
        logging.info("Apply Settings")
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    args = {
                        "addr": ["192.168.2.111", 1],
                        "interface": "Ethernet",
                        "vendor": "avmatrix",
                        "productName": "HVS0402E",
                        "type": "Switcher",
                        "model": "CUE01",
                        "deviceId": 123456,
                        "sn": 'qaehnerh2452',
                        "mac": "11:22:33:44:55:66",
                        "protocolVer": "V1.2",
                        "name": "CUE01"
                    }
    window = DeviceWidget(QWidget(), args, None)
    # window = DeviceMiniWidget("SC1205")
    window.show()
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    sys.exit(app.exec())

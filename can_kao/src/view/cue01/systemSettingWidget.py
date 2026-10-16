import logging

from PySide6 import QtWidgets, QtCore
from src.model.cue01.cue01Preferences import Cue01Preferences
from src.components.CustomComboBox import CustomComboBox
from src.components.SingleSliderWithSpinbox import SingleSliderWithSpinbox
# from globals import update_translations
from PySide6.QtCore import QSignalBlocker, Qt, QCoreApplication


class SystemSettingWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SystemSettingWidget, self).__init__(parent)
        self._parent = parent

    def setupUi(self):
        # self.setStyleSheet("QObject{color:white; font-size: 18px;}")
        _layout = QtWidgets.QGridLayout()
        # _layout.setSpacing(0)
        _layout.setSpacing(10)
        # _layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        # _layout.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        _layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)

        _layout.setContentsMargins(0, 70, 250, 80)

        _languages = Cue01Preferences.get_languages()
        _fan_modes = Cue01Preferences.get_fan_modes()

        # 语言选择
        # _language_label = QtWidgets.QLabel(self.tr("语言："))
        self._language_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Language：", None))
        self._language_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _language_label.setFixedSize(150, 40)

        self._language_list_cb = CustomComboBox(self)
        for i in range(len(_languages)):
            self._language_list_cb.addItem(_languages[i])
        self._language_list_cb.currentIndexChanged[int].connect(self.__select_language)

        # 风扇设置
        # _fan_mode_label = QtWidgets.QLabel(self.tr("风扇："))
        self._fan_mode_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Fan Setting：", None))
        self._fan_mode_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _fan_mode_label.setFixedSize(150, 40)

        # _fan_mode_cb = CustomComboBox(self)
        # for i in range(len(_fan_modes)):
        #     _fan_mode_cb.addItem(_fan_modes[i])
        # _fan_mode_cb.currentIndexChanged[int].connect(self.__select_fan_mode)
        self._fan_mode_widget = SingleSliderWithSpinbox(self)
        self._fan_mode_widget.setFixedWidth(250)
        self._fan_mode_widget.set_range(0, 100)
        self._fan_mode_widget.slider.valueChanged.connect(self.__set_fan_speed)
        self._fan_mode_widget.spinbox.valueChanged.connect(self.__set_fan_speed)

        # 系统复位
        # reset_label = QtWidgets.QLabel(self.tr("系统复位："))
        self.reset_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"System Reset：", None))
        self.reset_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # reset_label.setFixedSize(150, 40)

        self.reset_btn = QtWidgets.QPushButton()
        # reset_btn.setText(self.tr("复位"))
        self.reset_btn.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Reset", None))
        # reset_btn.setStyleSheet("QPushButton{color:yellow; font-size: 18px;}")
        self.reset_btn.setMaximumWidth(70)
        self.reset_btn.clicked.connect(self.__system_reset)

        # MCU固件版本
        # mcu_version_label = QtWidgets.QLabel(self.tr("MCU版本："))
        self.mcu_version_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"MCU Version：", None))
        # mcu_version_label.setFixedSize(150, 40)
        self.mcu_version_label.setFixedHeight(24)
        self.mcu_version_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

        self.mcu_version_value = QtWidgets.QLabel("")
        self.mcu_version_value.setFixedWidth(200)

        # MDIN640固件版本
        # mdin_version_label = QtWidgets.QLabel(self.tr("系统版本："))
        self.mdin_version_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"System Version：", None))
        # mdin_version_label.setFixedSize(150, 40)
        self.mdin_version_label.setFixedHeight(24)
        self.mdin_version_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

        self.mdin_version_value = QtWidgets.QLabel("")
        # mdin_version_value.setFixedSize(200, 40)

        # keyboard固件版本
        # kb_version_label = QtWidgets.QLabel(self.tr("Keyboard版本："))
        self.kb_version_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Keyboard Version：", None))
        # kb_version_label.setFixedSize(150, 40)
        self.kb_version_label.setFixedHeight(24)
        self.kb_version_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

        self.kb_version_value = QtWidgets.QLabel("")
        # kb_version_value.setFixedSize(200, 40)

        # 硬件版本
        # hw_version_label = QtWidgets.QLabel(self.tr("硬件版本："))
        # hw_version_label = QtWidgets.QLabel(self.tr("Hardware Version："))
        # hw_version_label.setFixedHeight(24)
        # hw_version_label.setFixedSize(150, 40)
        # hw_version_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

        # hw_version_value = QtWidgets.QLabel("")
        # hw_version_value.setFixedSize(200, 40)

        row = 0
        _layout.addWidget(self._language_label, row, 0, 1, 1)
        _layout.addWidget(self._language_list_cb, row, 1, 1, 1)

        row += 1
        _layout.addWidget(self._fan_mode_label, row, 0, 1, 1)
        _layout.addWidget(self._fan_mode_widget, row, 1, 1, 1)

        row += 1
        _layout.addWidget(self.reset_label, row, 0, 1, 1)
        _layout.addWidget(self.reset_btn, row, 1, 1, 1)

        row += 1
        _layout.addWidget(self.mcu_version_label, row, 0, 1, 1)
        _layout.addWidget(self.mcu_version_value, row, 1, 1, 1)

        row += 1
        _layout.addWidget(self.mdin_version_label, row, 0, 1, 1)
        _layout.addWidget(self.mdin_version_value, row, 1, 1, 1)

        row += 1
        _layout.addWidget(self.kb_version_label, row, 0, 1, 1)
        _layout.addWidget(self.kb_version_value, row, 1, 1, 1)

        # row += 1
        # _layout.addWidget(hw_version_label, row, 0, 1, 1)
        # _layout.addWidget(hw_version_value, row, 1, 1, 1)

        # self._mcu_version_value = mcu_version_value
        # self._mdin_version_value = mdin_version_value
        # self._kb_version_value = kb_version_value
        # self._hw_version_value = hw_version_value

        self._system_value = {
            "LanguageListComboBox": self._language_list_cb,
            "LanguageListIndex": 0,
            "FanModeComboBox": self._fan_mode_widget,
            "FanModeIndex": 0,
            "McuVersionLabel": self.mcu_version_value,
            "MdinVersionLabel": self.mdin_version_value,
            "KbVersionLabel": self.kb_version_value,
            # "HwVersionLabel": hw_version_value,
        }

        self.setLayout(_layout)
        # self.retranslateUi()

    def retranslateUi(self):
        self._language_label.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Language：", None))
        self._fan_mode_label.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Fan Setting：", None))
        self.reset_label.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"System Reset：", None))
        self.reset_btn.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Reset", None))
        self.mcu_version_label.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"MCU Version：", None))
        self.mdin_version_label.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"System Version：", None))
        self.kb_version_label.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Keyboard Version：", None))

    def showEvent(self, event):
        self._parent.controller.get_version()
        self._parent.controller.get_system()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def __select_language(self, index):
        sender = self.sender()

        if self._system_value["LanguageListComboBox"] == sender:
            if self._system_value["LanguageListIndex"] != index:
                logging.debug("select LanguageListIndex:{}".format(index))
                self._system_value["LanguageListIndex"] = index
                _args = {
                    "Language": Cue01Preferences.get_language_by_index(index)
                }
                self._parent.controller.set_system_setting(_args)

    def __select_fan_mode(self, index):
        sender = self.sender()

        if self._system_value["FanModeComboBox"] == sender:
            if self._system_value["FanModeIndex"] != index:
                logging.debug("select FanModeIndex:{}".format(index))
                self._system_value["FanModeIndex"] = index
                _args = {
                    "FanMode": Cue01Preferences.get_fan_mode_by_index(index)
                }
                self._parent.controller.set_system_setting(_args)

    def __set_fan_speed(self, value):
        logging.debug("select FanSpeed:{}".format(value))
        sender = self.sender()
        if self._system_value["FanModeComboBox"].slider == sender:
            with QSignalBlocker(self._system_value["FanModeComboBox"].spinbox):
                self._system_value["FanModeComboBox"].spinbox.setValue(value)
        elif self._system_value["FanModeComboBox"].spinbox == sender:
            with QSignalBlocker(self._system_value["FanModeComboBox"].slider):
                self._system_value["FanModeComboBox"].slider.setValue(value)
        _args = {
            "FanSpeed": value
        }
        self._parent.controller.set_system_setting(_args)

    def __system_reset(self):
        """
        提醒用户是否确认要复位
        """
        message = QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Are you sure reset the device?", None)
        # 使用字符串替换方法来插入变量值
        title = QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Factory Reset", None)
        # 弹出对话框进行确认
        confirm_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, title, message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        yes_button = confirm_box.button(QtWidgets.QMessageBox.StandardButton.Yes)
        yes_button.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"Yes", None))
        no_button = confirm_box.button(QtWidgets.QMessageBox.StandardButton.No)
        no_button.setText(QCoreApplication.translate("CUE01_System_Setting_Widget_Form", u"No", None))

        response = confirm_box.exec()
    
        # 根据用户的选择进行操作
        if response == QtWidgets.QMessageBox.StandardButton.No:
            return

        _args = {
            "SystemReset": "On"
        }
        self._parent.controller.set_system_setting(_args)

    def __update_versions(self, args):
        self._system_value["McuVersionLabel"].setText(args["McuVersion"])
        self._system_value["MdinVersionLabel"].setText(args["Mdin640Version"])
        self._system_value["KbVersionLabel"].setText(args["KeyboardVersion"])
        # self._system_value["HwVersionLabel"].setText(args["PcbVersion"])
    
    def handle_async_callback(self, obj):
        if obj["function"] == "get_version":
            args = obj["args"]
            logging.debug("version args:{}".format(args))
            self.__update_versions(args)
        elif obj["function"] == "get_system_params":
            args = obj["args"]
            logging.debug("system args:{}".format(args))

            _language = args["Language"]
            # _fan_mode = args["FanMode"]
            _fan_speed = args["FanSpeed"]

            _language_index = Cue01Preferences.get_index_by_language(_language)
            if _language_index != 0xFF:
                self._system_value["LanguageListIndex"] = _language_index
                self._system_value["LanguageListComboBox"].setCurrentIndex(_language_index)
            
            # _fan_mode_index = Cue01Preferences.get_index_by_fan_mode(_fan_mode)
            # if _fan_mode_index != 0xFF:
            #     self._system_value["FanModeIndex"] = _fan_mode_index
            #     self._system_value["FanModeComboBox"].setCurrentIndex(_fan_mode_index)

            if _fan_speed < 0 or _fan_speed > 100:
                logging.error("fan speed error:{}".format(_fan_speed))
                return
            with QSignalBlocker(self._system_value["FanModeComboBox"].spinbox):
                self._system_value["FanModeComboBox"].spinbox.setValue(_fan_speed)
            with QSignalBlocker(self._system_value["FanModeComboBox"].slider):
                self._system_value["FanModeComboBox"].slider.setValue(_fan_speed)

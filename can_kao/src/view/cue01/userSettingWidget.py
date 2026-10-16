import os, sys, logging, traceback
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QSettings, QStandardPaths, Qt, QTimer, QCoreApplication
from PySide6.QtGui import QFont
from src.ui.cue01.userSetting_ui import Ui_CUE01_User_Setting_Form


class UserSettingWidget(Ui_CUE01_User_Setting_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.__settings = QSettings("AvMatrix", "Upper_Computer")
        self.timer = QTimer()
        self.device_response_exported = False # 设备是否回复导出 标志
        self.device_response_import = False # 设备是否回复导入 标志
        # 用户配置字典（True表示已配置，False表示未配置）
        self.__user_config_dict = [
            {
                "name": "Default",
                "isValid": True
            },{
                "name": "",
                "isValid": False
            },{
                "name": "",
                "isValid": False
            },{
                "name": "",
                "isValid": False
            },{
                "name": "",
                "isValid": False
            },{
                "name": "",
                "isValid": False
            },{
                "name": "",
                "isValid": False
            },{
                "name": "",
                "isValid": False
            }
        ]
        self.setupUi(self)

    def init_ui(self):
        self.__update_combobox_status()
        # self.pushButton_delete_user.setEnabled(False)
        self.lineEdit_current_user.line_edit.setReadOnly(True)
        self.lineEdit_current_user.line_edit.setAlignment(Qt.AlignCenter)
        self.lineEdit_current_user.clear_button.hide()

        self.pushButton_switch_user.clicked.connect(self.switch_user)
        self.pushButton_import.clicked.connect(self._handle_import_config)
        self.pushButton_export.clicked.connect(self._handle_export_config)
        self.pushButton_add_user.clicked.connect(self._handle_add_user)
        self.pushButton_delete_user.clicked.connect(self._handle_delete_user)

    # 更新combobox，显示当前用户列表，并选中当前用户
    def __update_combobox_status(self, user_name="Default"):
        user_list = []
        for user in self.__user_config_dict:
            if user["isValid"]:
                user_list.append(user["name"])

        self.comboBox_current_user.clear()
        self.comboBox_current_user.addItems(user_list)
        # self.comboBox_current_user.setCurrentText(user_name)

        self.lineEdit_current_user.line_edit.setText(user_name)
        # if user_name == "Default":
        #     # self.pushButton_import.setEnabled(False) # 禁用导入按钮
        #     self.pushButton_delete_user.setEnabled(False) # 禁用删除按钮
        # else:
        #     self.pushButton_delete_user.setEnabled(True)
            # self.pushButton_import.setEnabled(True)

    def _get_user_id_by_username(self, username):
        for i in range(len(self.__user_config_dict)):
            user = self.__user_config_dict[i]
            if user["isValid"] and user["name"] == username:
                return i

        return 0xff
    
    def _get_user_id_not_used(self):
        for i in range(len(self.__user_config_dict)):
            user = self.__user_config_dict[i]
            if not user["isValid"]:
                return i

        return 0xff

    # 切换用户
    def switch_user(self):
        # 切换用户时，更新配置信息，并发送指令到设备，更新配置信息
        if self.comboBox_current_user.currentText() == self.lineEdit_current_user.line_edit.text():
            return
        user_name = self.comboBox_current_user.currentText()
        user_id = self._get_user_id_by_username(user_name)

        if user_id == 0xff:
            logging.error("错误的用户，不应该会发生的")
            return
        # 切换用户
        choice = QMessageBox.question(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"tip", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"Swithing user will reboot the device, continue?", None))
        if choice == QMessageBox.Yes:
            ''' 发送指令到设备，切换用户 '''
            logging.info(f"准备发送指令到设备，切换为用户：{user_name}")
            _args = {
                "UserOption": 1,
                "UserNum": user_id,
                "UserName": user_name
            }
            self._parent.controller.set_user_params(_args)

    # 导入配置
    def _handle_import_config(self):
        _user_id = self._get_user_id_not_used()
        if _user_id == 0xff:
            QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"The user list is full!", None))
            return

        # 获取上次打开的路径，如果没有，则选择桌面位置
        import_dir = self.__settings.value("import_Dir", QStandardPaths.writableLocation(QStandardPaths.DesktopLocation))
        filename_path, result = QFileDialog.getOpenFileName(self,
                                                            QCoreApplication.translate("CUE01_User_Setting_Widget", u"choose config file(.config)", None),
                                                            import_dir,
                                                            "AvMatrix Files (*.config);;All Files (*)")
        if result:
            logging.info(f"Import config file path: {filename_path}")
            _file_dir = os.path.dirname(filename_path)
            _filename = os.path.basename(filename_path)
            _filename_no_ext = os.path.splitext(_filename)[0]
            self.__settings.setValue("import_Dir", _file_dir) # 保存本次打开的路径

            if self._get_user_id_by_username(_filename_no_ext) != 0xff:
                QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"The user name is duplicated, please modify the configuration filename!", None))
                return

            try:
                _filename_bytes = _filename_no_ext.encode("ascii")
                if len(_filename_bytes) > 16:
                    QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"The configuration filename should be no more than 16 characters!", None))
                    return
            except:
                QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"The configuration file name only supports ASCII characters!", None))
                return

            logging.info("准备发送指令到设备获取配置信息")
            # 解析配置文件
            config_data = ""
            with open(filename_path, "rb") as f:
                config_data = f.read()
            if not 200 <= len(config_data) <= 500 :
                QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"The configuration file is error!", None))
                return
            # 发送配置到设备
            self.device_response_import = False # 先把回应标识设置为False
            _args = {
                "UserOption": 4,
                "UserNum": _user_id,
                "UserName": _filename_no_ext,
                "ConfigData": list(config_data),
            }
            self._parent.controller.set_user_params(_args)

    # 导出配置
    def _handle_export_config(self):
        user_name = self.comboBox_current_user.currentText()
        user_id = self._get_user_id_by_username(user_name)

        # 获取上次打开的路径，如果没有，则选择桌面位置
        export_dir = self.__settings.value("export_dir", QStandardPaths.writableLocation(QStandardPaths.DesktopLocation))
        export_path = QFileDialog.getExistingDirectory(self,
                                                            QCoreApplication.translate("CUE01_User_Setting_Widget", u"choose export directory", None),
                                                            export_dir)
        if len(export_path) > 0:
            logging.info(f"Export directory path: {export_path}")
            self.__settings.setValue("export_dir", export_path) # 保存本次打开的路径
            # 发送指令到设备，获取配置信息
            logging.info("准备发送指令到设备，获取当前用户的配置信息")
            self.device_response_exported = False # 重新初始化 设备是否回复导出标志
            _args = {
                "UserOption": 5,
                "UserNum": user_id,
            }
            self._parent.controller.set_user_params(_args)
            self.timer.singleShot(10000, self.export_failed) # 等待10秒未导出成功则超时

    def export_failed(self):
        if not self.device_response_exported:
            logging.error("导出配置文件超时，可能设备未回复！")
            self.device_response_exported = True # 超时后，此处标识为已经回复过了
            QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"Export of user configuration failed! Please check if the device is connected.", None))

    # 异步导出配置回调
    def handle_async_export_callback(self, args):
        try:
            # 封装配置信息，保存到文件
            user_name = self.comboBox_current_user.currentText()
            data = args["ConfigData"]
            export_dir = self.__settings.value("export_dir", QStandardPaths.writableLocation(QStandardPaths.DesktopLocation))
            export_path = os.path.join(export_dir, f"{user_name}.config")
            with open(export_path, "wb") as f:
                f.write(data)
            logging.info(f"导出配置文件成功! 路径:{export_path}")
            QMessageBox.information(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Info", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"Export of user configuration successufully!", None))
        except:
            logging.error(f"导出配置文件失败! 错误：{traceback.format_exc()}")
            QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"Export of user configuration failed! Please check if the device is connected.", None))

    # 新增用户
    def _handle_add_user(self):
        _user_id = self._get_user_id_not_used()
        if _user_id == 0xff:
            QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"The number of users has reached the limit! Please delete one user and try again.", None))
            return

        ''' 发送指令到设备，保存当前用户的配置信息 '''
        logging.info(f"准备发送指令到设备，新建用户id:{_user_id}")
        _args = {
            "UserOption": 3,
            "UserNum": _user_id,
        }
        self._parent.controller.set_user_params(_args)

    # 删除用户
    def _handle_delete_user(self):
        current_user_name = self.lineEdit_current_user.line_edit.text()
        user_name = self.comboBox_current_user.currentText()
        user_id = self._get_user_id_by_username(user_name)

        if user_name == current_user_name:
            QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"Not allowed to delete the current user's configuration.", None))
            return

        if user_name == "Default":
            QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"Not allowed to delete the default user's configuration.", None))
            return
        
        # 在代码中定义需要翻译的字符串，使用占位符
        message_template = QCoreApplication.translate("CUE01_User_Setting_Widget", u"Please ensure that the configuration file has been saved, Otherwise, the {}'s configuration will not be retrievable! The Device will reboot, Continue?", None)
        message = message_template.format(user_name)

        choice = QMessageBox.question(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"warning", None), message)
        if choice == QMessageBox.Yes:
            ''' 发送指令到设备，删除当前用户的配置信息 '''
            logging.info(f"准备发送指令到设备，删除{user_name}用户")
            _args = {
                "UserOption": 2,
                "UserNum": user_id,
            }
            self._parent.controller.set_user_params(_args)

    def showEvent(self, event):
        self._parent.controller.get_user_params()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_user_params":
            args = obj["args"]
            logging.debug("user args:{}".format(args))
            _current_user = "Default"
            _current_user_index = args["CurrentUser"]
            _user_valid_list = args["UserValidList"]
            _username_list = args["UsernameList"]

            for i in range(len(_user_valid_list)):
                if _user_valid_list[i] == 0:
                    if i > 0: # 确保第一个用户是有效的
                        self.__user_config_dict[i]["isValid"] = False
                else:
                    self.__user_config_dict[i]["isValid"] = True
                    self.__user_config_dict[i]["name"] = _username_list[i]

            logging.debug("__user_config_dict:{}".format(self.__user_config_dict))

            # 当前用户的id超出列表，为无效用户，设置为默认的Default用户
            if _current_user_index >= len(_user_valid_list):
                _current_user_index = 0

            # 当前用户为非有效用户，设置为默认的Default用户
            if not self.__user_config_dict[_current_user_index]["isValid"]:
                _current_user_index = 0

            _current_user = self.__user_config_dict[_current_user_index]["name"]
            self.__update_combobox_status(_current_user)
        elif obj["function"] == "normal_operation": # 一般操作回复处理
            if obj["args"]["Result"] == 0:
                logging.info("Operation successufully!")
                self._parent.controller.get_user_params()
            else:
                logging.warning("Operation failed!")
        elif obj["function"] == "import_config": # 导入操作回复处理
            logging.info("Import config callback")
            if not self.device_response_import:
                self.device_response_import = True
                if obj["args"]["Result"] == 0:
                    QMessageBox.information(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Info", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"Import of user configuration successufully!", None))
                    self._parent.controller.get_user_params()
                else:
                    QMessageBox.warning(self, QCoreApplication.translate("CUE01_User_Setting_Widget", u"Warning", None), QCoreApplication.translate("CUE01_User_Setting_Widget", u"Import of user configuration failed! Please check if the device is connected.", None))
        elif obj["function"] == "export_config": # 导出操作处理，由主动上报触发
            logging.info("Export config callback")
            if not self.device_response_exported:
                self.device_response_exported = True
                self.handle_async_export_callback(obj["args"])
        else:
            logging.info("obj:{}".format(obj))

import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSignalBlocker, Qt, Signal, QCoreApplication
from src.ui.uc1218_4K.uc1218_4K_edid_ui import Ui_UC1218_4K_Edid_Form
from src.model.modelPreferences import ModelPreferences
from src.model.modelRticePreferences import ModelRticePreferences
from src.model.uc1218_4K.uc1218_4K_Preferences import UC1218_4K_Preferences
from globals import relative_path, global_qss
import time

class UC1218_4K_EDID(Ui_UC1218_4K_Edid_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.export_edid_data_filename = ""
        self.edid_flash_table_name_list = []
        self.edid_flash_table_index = 0

        self.edidMode_comboBox.addItems(["Auto", "Bypass", "Pre-Saved"])

        self.edidMode_comboBox.currentIndexChanged.connect(self._on_edidMode_comboBox_index_changed)
        self.edidContent_delete_pushButton.clicked.connect(self._on_delete_edidContent)
        self.edidContent_save_pushButton.clicked.connect(self._on_save_edidContent)

        # self.edidContent_delete_pushButton.setProperty("type", "edid_delete")
        # self.edidContent_save_pushButton.setProperty("type", "edid_save")

        self.edidContent_comboBox.currentIndexChanged.connect(self._on_edidContent_comboBox_index_changed)

        self.exportEdid_pushButton.clicked.connect(self._on_export_edid)
        self.importEdid_pushButton.clicked.connect(self._on_import_edid)

        self.wait_action_finished_msg_box = None
        self.wait_action = {
            "action": None,
            "events": []
        }
    
    def _set_control_permission_by_mode(self, mode):
        if mode == ModelRticePreferences._edidModeList[0]: # 对应Default from flash
            self.edidContent_comboBox.setDisabled(False)
            self.edidContent_save_pushButton.setDisabled(False)
            self.exportEdid_pushButton.setDisabled(False)
            self.importEdid_pushButton.setDisabled(False)

            if self.edidContent_comboBox.currentIndex() == 0: # 默认选项，不能删除
                self.edidContent_delete_pushButton.setDisabled(True)
            else:
                self.edidContent_delete_pushButton.setDisabled(False)
        else:
            self.edidContent_comboBox.setDisabled(True)
            self.edidContent_delete_pushButton.setDisabled(True)
            self.edidContent_save_pushButton.setDisabled(True)
            self.exportEdid_pushButton.setDisabled(True)
            self.importEdid_pushButton.setDisabled(True)

    def _on_edidMode_comboBox_index_changed(self, index):
        try:
            mode = ""
            if index == 0: # Auto Mode
                mode = ModelRticePreferences._edidModeList[4] # 对应Mixed
            elif index == 1: # Bypass Mode
                mode = ModelRticePreferences._edidModeList[1] # 对应Follow TX
            else:
                mode = ModelRticePreferences._edidModeList[0] # 对应Default from flash

            self._set_control_permission_by_mode(mode)

            _args = {
                "EdidMode": mode
            }
            self._parent.controller.set_rtice_EDID_mode(_args)
        except Exception as e:
            logging.error(f"e:{e}")

    def _start_wait_action_finished_msg_box(self, action, events_list):
        # self.wait_action_finished_msg_box = 
        msg_box = QMessageBox()
        msg_title = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID Management", None)
        

        if action == "ImportEDID":
            message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"Importing EDID, please wait...", None)
        elif action == "DeleteEDID":
            message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"Deleting EDID, please wait...", None)
        elif action == "SaveEDID":
            message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID is being enabled.", None)

        msg_box.setWindowTitle(msg_title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.NoButton)  # 不显示按钮，仅用于显示信息
        msg_box.show()
        # msg_box.setWindowModality(Qt.ApplicationModal)
        self.wait_action_finished_msg_box = msg_box

        self.wait_action["action"] = action
        self.wait_action["events"].clear()
        for item in events_list:
            self.wait_action["events"].append(item)

        logging.debug(f"wait_action:{self.wait_action}")

    def _reply_wait_action_finished_msg_box(self, event):
        logging.debug(f"_reply_wait_action_finished_msg_box event:{event}")
        logging.debug(f"wait_action:{self.wait_action}")
        if event in self.wait_action["events"]:
            self.wait_action["events"].remove(event)

        if self.wait_action["action"] == None: # 直接关闭
            self._close_wait_action_finished_msg_box()
        else:
            if len(self.wait_action["events"]) == 0:
                if self.wait_action["action"] == "ImportEDID": # 导入EDID
                    self.wait_action["action"] = None
                    self._close_wait_action_finished_msg_box()
                    msg_title = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID Management", None)
                    message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID imported successfully!", None)
                    QMessageBox.information(self, msg_title, message)
                elif self.wait_action["action"] == "DeleteEDID": # 删除EDID
                    self.wait_action["action"] = None
                    self._close_wait_action_finished_msg_box()
                    msg_title = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID Management", None)
                    message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID deleted successfully!", None)
                    QMessageBox.information(self, msg_title, message)
                elif self.wait_action["action"] == "SaveEDID": # 设置EDID
                    self.wait_action["action"] = None
                    self._close_wait_action_finished_msg_box()
                    msg_title = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID Management", None)
                    message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID enabled successfully.", None)
                    QMessageBox.information(self, msg_title, message)

    def _close_wait_action_finished_msg_box(self):
        if self.wait_action_finished_msg_box:
            self.wait_action_finished_msg_box.close()
            self.wait_action_finished_msg_box = None

    def _on_delete_edidContent(self):
        table_index = self.__get_edid_flash_table_index()
        if table_index != 0:
            if self.edid_flash_table_index == table_index:
                self._start_wait_action_finished_msg_box("DeleteEDID", ["set_rtice_EDID_Flash_Table_Name_List", "set_rtice_EDID_Flash_Default_table"])
            else:
                self._start_wait_action_finished_msg_box("DeleteEDID", ["set_rtice_EDID_Flash_Table_Name_List"])

            self.edid_flash_table_name_list[table_index] = ""
            _args = {
                "NameList": self.edid_flash_table_name_list
            }
            self._parent.controller.set_rtice_EDID_Flash_Table_Name_List(_args)

            # 选中的表是设备端正在使用的表，则需要将设备端的default表切换到index0
            if self.edid_flash_table_index == table_index:
                _args = {
                    "EDIDTableIndex": 0
                }
                self._parent.controller.set_rtice_EDID_Flash_Default_table(_args)
        else:
            logging.error("Not allow to delete default EDID table!!!")

    def _on_save_edidContent(self):
        self._start_wait_action_finished_msg_box("SaveEDID", ["set_rtice_EDID_Flash_Default_table"])
        table_index = self.__get_edid_flash_table_index()
        _args = {
            "EDIDTableIndex": table_index
        }
        self._parent.controller.set_rtice_EDID_Flash_Default_table(_args)

    def _on_edidContent_comboBox_index_changed(self, index):
        if index == 0: # Default表，不允许删除
            self.edidContent_delete_pushButton.setDisabled(True)
        else:
            self.edidContent_delete_pushButton.setDisabled(False)

    def _on_import_edid(self):
        msg_title = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID Management", None)

        if not self.__is_allow_import_edid_flash_table():
            message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID import failed: EDID table is full.", None)
            QMessageBox.information(self, msg_title, f"{message}")
            return

        open_file_caption = QCoreApplication.translate("UC1218_4K_Edid_Form", u"Open EDID File", None)
        open_file_filter = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID Bin Files (*.bin);;EDID XML Files (*.xml);;All Files (*)", None)
        filename, _ = QFileDialog.getOpenFileName(self, open_file_caption, '', open_file_filter)
        if filename:
            logging.debug(f'Selected file: {filename}')
            file_extension = os.path.splitext(filename)
            edid_table_name = os.path.basename(file_extension[0])

            if self.__is_duplicate_edid_flash_table_name(edid_table_name):
                message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID import failed: Name already exists.", None)
                QMessageBox.information(self, msg_title, f"{message}")
                return
            elif len(edid_table_name.encode('utf-8')) > 32:
                message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID import failed: Name exceeds 32 characters.", None)
                QMessageBox.information(self, msg_title, f"{message}")
                return
            elif file_extension[1] == ".bin":
                if os.stat(filename).st_size not in [128, 256, 384, 512]:
                    message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"Failed to import EDID!", None)
                    QMessageBox.information(self, msg_title, message)
                else:
                    logging.debug(f"edid_table_name: {edid_table_name}")

                    result, table_index = self.__insert_edid_flash_table_name(edid_table_name)
                    if result:
                        self._start_wait_action_finished_msg_box("ImportEDID", ["set_rtice_EDID_Flash_table", "set_rtice_EDID_Flash_Table_Name_List"])
                        time.sleep(0.1) # 确保先弹出等待提示框
                        with open(filename, 'rb') as file:
                            data = file.read()
                            _args = {
                                "EDIDTableIndex": table_index,
                                "EDIDTable": data
                            }
                            self._parent.controller.set_rtice_EDID_Flash_table(_args)
                        
                        _args = {
                            "NameList": self.edid_flash_table_name_list
                        }
                        self._parent.controller.set_rtice_EDID_Flash_Table_Name_List(_args)
                    else:
                        message = QCoreApplication.translate("UC1218_4K_Edid_Form", f"EDID import failed: Get table index error.", None)
                        QMessageBox.information(self, msg_title, f"{message}")

            elif file_extension[1] == ".xml":
                message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"XML file will been support later.", None)
                QMessageBox.information(self, msg_title, message)
            else:
                message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"This file type is unsupported.", None)
                QMessageBox.information(self, msg_title, message)

        return 

    def __is_duplicate_edid_flash_table_name(self, table_name):
        if table_name != "":
            for i in range(len(self.edid_flash_table_name_list)):
                if table_name == self.edid_flash_table_name_list[i]:
                    return True
        
        return False

    def __is_allow_import_edid_flash_table(self):
        for i in range(len(self.edid_flash_table_name_list)):
            if self.edid_flash_table_name_list[i] == "":
                return True
        
        return False
    
    def __insert_edid_flash_table_name(self, table_name):
        if table_name != "":
            for i in range(len(self.edid_flash_table_name_list)):
                if self.edid_flash_table_name_list[i] == "":
                    self.edid_flash_table_name_list[i] = table_name
                    return True, i
        
        return False, 0

    def __get_edid_flash_table_index(self):
        current_text = self.edidContent_comboBox.currentText()
        table_index = 0 # 默认获取的是index0的EDID

        for i in range(len(self.edid_flash_table_name_list)):
            if current_text == self.edid_flash_table_name_list[i]:
                table_index = i
                break

        return table_index

    """
    根据从flash中读取到index来设置下拉列表中的index。
    由于有空位的存在，flash中读取到的index是不考虑空位的，而下拉列表只会显示非空的项，
    因此下拉列表中的index，需要排除掉空位
    """
    def __set_edidContent_comboBox_current_index(self, flash_table_index):
        cb_index = flash_table_index

        for i in range(flash_table_index):
            if self.edid_flash_table_name_list[i] == "": # edid_flash_table_name_list中的名称列表，是包含空位的，因此每遇到一个空位，就减掉1即可
                cb_index -= 1

        if cb_index < self.edidContent_comboBox.count(): # 设置为计算得到的table index
            self.edidContent_comboBox.setCheckedItem(cb_index)
        
        return

    def _on_export_edid(self):
        save_file_caption = QCoreApplication.translate("UC1218_4K_Edid_Form", u"Save EDID File", None)
        save_file_filter = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID Bin Files (*.bin);;All Files (*)", None)
        filename, _ = QFileDialog.getSaveFileName(self, save_file_caption, self.edidContent_comboBox.currentText(), save_file_filter)
        if filename:
            logging.debug(f'Selected file: {filename}')
            self.export_edid_data_filename = filename
            
            _args = {
                "EDIDTableIndex": self.__get_edid_flash_table_index()
            }
            self._parent.controller.get_rtice_EDID_Flash_table(_args)
        else:
            logging.debug("No selected file.")

    def retranslateUi(self, form):
        super().retranslateUi(form)

        _modes = ["Auto", "Bypass", "Pre-saved"]

        for i in range(len(_modes)):
            _item_text = QCoreApplication.translate("UC1218_4K_Edid_Form", _modes[i], None)
            self.edidMode_comboBox.setItemText(i, _item_text)

    def showEvent(self, event):
        self._parent.controller.get_rtice_EDID_mode()
        self._parent.controller.get_rtice_EDID_Flash_Default_table()
        self._parent.controller.get_rtice_EDID_Flash_Table_Name_List()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_EDID_mode":
            args = obj["args"]
            # mode_list = ["Default", "Follow TX", "Follow USB", "Undefined", "Mixed"]
            if args["EdidMode"] in ModelRticePreferences._edidModeList:
                if args["EdidMode"] == ModelRticePreferences._edidModeList[0]:
                    with QSignalBlocker(self.edidMode_comboBox):
                        self.edidMode_comboBox.setCurrentIndex(2)
                elif args["EdidMode"] == ModelRticePreferences._edidModeList[1]:
                    with QSignalBlocker(self.edidMode_comboBox):
                        self.edidMode_comboBox.setCurrentIndex(1)
                elif args["EdidMode"] == ModelRticePreferences._edidModeList[4]:
                    with QSignalBlocker(self.edidMode_comboBox):
                        self.edidMode_comboBox.setCurrentIndex(0)
        elif obj["function"] == "get_rtice_EDID_Flash_table":
            args = obj["args"]
            logging.debug("Get device's edid args:{}".format(args))
            # print("Get device's edid args:{}".format(args))
            
            if self.export_edid_data_filename == "":
                lines = int(len(args["EDIDTable"])/16)
                edid_data_str = ""
                for line in range(lines):
                    line_data_str="{:02X}:".format(line)

                    for i in range(16):
                        line_data_str += " {:02X}".format(args["EDIDTable"][line*16 + i])
                
                    if 0 <= line < lines - 1:
                        line_data_str += "\n"

                    edid_data_str += line_data_str
                
                # self.plainTextEdid.setPlainText(edid_data_str)
            else:
                with open(self.export_edid_data_filename, 'wb') as file:
                    file.write(args["EDIDTable"])
                
                msg_title = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID Management", None)
                message = QCoreApplication.translate("UC1218_4K_Edid_Form", u"EDID exported successfully!", None)
                QMessageBox.information(self, msg_title, message)
                self.export_edid_data_filename = ""
        # elif obj["function"] == "get_rtice_EDID_Flash_table":
        #     args = obj["args"]
        #     logging.debug("Get device's edid flash table args:{}".format(args))

        #     lines = int(len(args["EDIDTable"])/16)
        #     edid_data_str = ""
        #     for line in range(lines):
        #         line_data_str="{:02X}:".format(line)

        #         for i in range(16):
        #             line_data_str += " {:02X}".format(args["EDIDTable"][line*16 + i])
                
        #         if 0 <= line < lines - 1:
        #             line_data_str += "\n"

        #         edid_data_str += line_data_str

        #     logging.debug("edid_data_str:", edid_data_str)
        elif obj["function"] in ["get_rtice_EDID_Flash_Table_Name_List", "set_rtice_EDID_Flash_Table_Name_List"]:
            args = obj["args"]
            logging.debug("Get/Set device's edid flash table name list args:{}".format(args))

            # with QSignalBlocker(self.edidContent_comboBox):
            self.edidContent_comboBox.clear()
            self.edid_flash_table_name_list.clear()

            _default_text = QCoreApplication.translate("UC1218_4K_Edid_Form", "Default", None)
            if args["Result"] and "NameList" in args:
                name_list = args["NameList"]
                if all(name == "" for name in name_list) or len(name_list) == 0:
                    self.edid_flash_table_name_list = [_default_text] + [""] * 5
                    self.edidContent_comboBox.addItem(_default_text)
                else:
                    self.edid_flash_table_name_list = name_list[:6]
                    for name in name_list[:6]:
                        if name != "":
                            self.edidContent_comboBox.addItem(name)

            if self.edidContent_comboBox.count() == 0:
                self.edidContent_comboBox.addItem(_default_text)
                
            # if self.edid_flash_table_index < self.edidContent_comboBox.count(): # 设置为Flash中读取到table index
            #     # self.edidContent_comboBox.setCurrentIndex(self.edid_flash_table_index)
            #     self.edidContent_comboBox.setCheckedItem(self.edid_flash_table_index)
            self.__set_edidContent_comboBox_current_index(self.edid_flash_table_index)
            
            if obj["function"] == "set_rtice_EDID_Flash_Table_Name_List":
                self._reply_wait_action_finished_msg_box(obj["function"])

        elif obj["function"] in ["get_rtice_EDID_Flash_Default_table", "set_rtice_EDID_Flash_Default_table"]:
            args = obj["args"]
            logging.debug("Get/Set device's edid flash default table args:{}".format(args))

            # with QSignalBlocker(self.edidContent_comboBox):
            if args["Result"] and "EDIDTableIndex" in args:
                table_index = args["EDIDTableIndex"]
                if 0 <= table_index < 6:
                    self.edid_flash_table_index = table_index
                else:
                    self.edid_flash_table_index = 0
                
                # if self.edid_flash_table_index < self.edidContent_comboBox.count(): # 设置为Flash中读取到table index
                #     # self.edidContent_comboBox.setCurrentIndex(self.edid_flash_table_index)
                #     self.edidContent_comboBox.setCheckedItem(self.edid_flash_table_index)
                self.__set_edidContent_comboBox_current_index(self.edid_flash_table_index)
            
            if obj["function"] == "set_rtice_EDID_Flash_Default_table":
                self._reply_wait_action_finished_msg_box(obj["function"])
        elif obj["function"] == "set_rtice_EDID_Flash_table":
            args = obj["args"]
            logging.debug("Set device's edid flash table args:{}".format(args))

            self._reply_wait_action_finished_msg_box(obj["function"])
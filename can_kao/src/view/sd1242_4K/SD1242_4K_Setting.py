import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QCoreApplication, QSignalBlocker, Qt, Signal
from src.ui.sd1242_4K.SD1242_4K_Setting_ui import Ui_SD1242_4K_Setting_Form
from src.model.modelPreferences import ModelPreferences
from globals import relative_path, global_qss

class SD1242_4K_Setting(Ui_SD1242_4K_Setting_Form, QWidget):
    LEARNING_EDID_SELECT_TYPE = "LEARNING"
    PRESAVE_EDID_SELECT_TYPE = "PRESAVE"
    NONE_EDID_SELECT_TYPE = "NONE"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.delete_pushButton.clicked.connect(self._on_delete_edid)
        self.import_pushButton.clicked.connect(self._on_import_edid)
        self.export_pushButton.clicked.connect(self._on_export_edid)

        self.learning_edid_listWidget.itemClicked.connect(self._on_learning_edid_item_clicked)
        self.presaved_edid_listWidget.itemClicked.connect(self._on_presaved_edid_item_clicked)
        self._select_edid_item_type = SD1242_4K_Setting.NONE_EDID_SELECT_TYPE
        self.delete_pushButton.setDisabled(True)
        self.export_pushButton.setDisabled(True)

        self.learning_edid_list = []
        self.presaved_edid_list = []

        self.export_edid_data_filename = ""

    def retranslateUi(self, parent_Form):
        super().retranslateUi(parent_Form)
        self.device_edid_label.setText(u"<html><head/><body><p align=\"center\">" + QCoreApplication.translate("SD1242_4K_Setting_Form", u"Device EDID", None) + "</p></body></html>")
        self.learning_edid_label.setText(u"<html><head/><body><p align=\"center\">" + QCoreApplication.translate("SD1242_4K_Setting_Form", u"Learning EDID", None) + "</p></body></html>")
        self.presaved_edid_label.setText(u"<html><head/><body><p align=\"center\">" + QCoreApplication.translate("SD1242_4K_Setting_Form", u"Pre-Saved EDID", None) + "</p></body></html>")
    
    def _on_select_edid_item(self, type):
        """
        当选择一个item时, 使能delete按键和export按键, 并清空另外一个的选项, 同时记录该type
        """
        self.delete_pushButton.setDisabled(False)
        self.export_pushButton.setDisabled(False)
        self._select_edid_item_type = type

        if type == SD1242_4K_Setting.LEARNING_EDID_SELECT_TYPE:
            self.presaved_edid_listWidget.clearSelection()
        elif type == SD1242_4K_Setting.PRESAVE_EDID_SELECT_TYPE:
            self.learning_edid_listWidget.clearSelection()
    
    def _do_clear_selection_edid_item(self, type):
        self.delete_pushButton.setDisabled(True)
        self.export_pushButton.setDisabled(True)
        self._select_edid_item_type = SD1242_4K_Setting.NONE_EDID_SELECT_TYPE

        if type == SD1242_4K_Setting.LEARNING_EDID_SELECT_TYPE:
            self.learning_edid_listWidget.clearSelection()
        elif type == SD1242_4K_Setting.PRESAVE_EDID_SELECT_TYPE:
            self.presaved_edid_listWidget.clearSelection()

    def _on_learning_edid_item_clicked(self, item):
        self._on_select_edid_item(SD1242_4K_Setting.LEARNING_EDID_SELECT_TYPE)

    def _on_presaved_edid_item_clicked(self, item):
        self._on_select_edid_item(SD1242_4K_Setting.PRESAVE_EDID_SELECT_TYPE)

    def _on_delete_edid(self):
        message = QCoreApplication.translate("SD1242_4K_Setting_Form", u"Are you sure delete the EDID?", None)
        # 使用字符串替换方法来插入变量值
        title = QCoreApplication.translate("SD1242_4K_Setting_Form", u"Delete EDID", None)
        # 弹出对话框进行确认
        confirm_box = QMessageBox(QMessageBox.Question, title, message, QMessageBox.Yes | QMessageBox.No)

        yes_button = confirm_box.button(QMessageBox.StandardButton.Yes)
        yes_button.setText(QCoreApplication.translate("SD1242_4K_Setting_Form", u"Yes", None))
        no_button = confirm_box.button(QMessageBox.StandardButton.No)
        no_button.setText(QCoreApplication.translate("SD1242_4K_Setting_Form", u"No", None))

        response = confirm_box.exec()
    
        # 根据用户的选择进行操作
        if response == QMessageBox.StandardButton.No:
            return
        
        if self._select_edid_item_type == SD1242_4K_Setting.LEARNING_EDID_SELECT_TYPE:
            selected_item = self.learning_edid_listWidget.currentItem()
            if selected_item:
                # 移除选中的项目
                row = self.learning_edid_listWidget.row(selected_item)
                # self.learning_edid_listWidget.takeItem(row)
                self._do_clear_selection_edid_item(SD1242_4K_Setting.LEARNING_EDID_SELECT_TYPE)

                args = {
                    "EdidMode": 1,
                    "Position": row
                }
                self._parent.controller.delete_selected_edid(args)

                # 删除后再获取一下learning edid列表
                args = {
                    "EdidMode": 1
                }
                self._parent.controller.get_edid_list(args)

        elif self._select_edid_item_type == SD1242_4K_Setting.PRESAVE_EDID_SELECT_TYPE:
            selected_item = self.presaved_edid_listWidget.currentItem()
            if selected_item:
                # 移除选中的项目
                row = self.presaved_edid_listWidget.row(selected_item)
                # self.presaved_edid_listWidget.takeItem(row)
                self._do_clear_selection_edid_item(SD1242_4K_Setting.PRESAVE_EDID_SELECT_TYPE)

                args = {
                    "EdidMode": 2,
                    "Position": row
                }
                self._parent.controller.delete_selected_edid(args)

                # 删除后再获取一下presaved edid列表
                args = {
                    "EdidMode": 2
                }
                self._parent.controller.get_edid_list(args)

    def _import_edid_data(self, data, name):
        args = {
            "PresavedName": name,
            "EdidData": data
        }

        self._parent.controller.set_presaved_edid_data(args)
        # 导入后再获取一下Presaved edid列表
        args = {
            "EdidMode": 2
        }
        self._parent.controller.get_edid_list(args)
        
    def _on_import_edid(self):
        open_file_caption = QCoreApplication.translate("SD1242_4K_Setting_Form", u"Open EDID File", None)
        open_file_filter = QCoreApplication.translate("SD1242_4K_Setting_Form", u"EDID Bin Files (*.bin);;EDID XML Files (*.xml);;All Files (*)", None)
        filename, _ = QFileDialog.getOpenFileName(self, open_file_caption, '', open_file_filter)
        if filename:
            logging.debug(f'Selected file: {filename}')
            file_extension = os.path.splitext(filename)
            msg_title = QCoreApplication.translate("SD1242_4K_Setting_Form", u"Import EDID file", None)
            
            if file_extension[1] == ".bin":
                if os.stat(filename).st_size != 256:
                    message = QCoreApplication.translate("SD1242_4K_Setting_Form", u"Error EDID file", None)
                    QMessageBox.information(self, msg_title, f"{message} {os.path.basename(filename)}")
                else:
                    edid_name = os.path.basename(file_extension[0])
                    if len(edid_name) >= 15:
                        edid_name = edid_name[0:14]
                    
                    logging.debug(f"edid_name: {edid_name}")

                    with open(filename, 'rb') as file:
                        data = file.read()
                        self._import_edid_data(list(data), edid_name)

            elif file_extension[1] == ".xml":
                message = QCoreApplication.translate("SD1242_4K_Setting_Form", u"XML file will been support later.", None)
                QMessageBox.information(self, msg_title, message)
            else:
                message = QCoreApplication.translate("SD1242_4K_Setting_Form", u"This file type is unsupported.", None)
                QMessageBox.information(self, msg_title, message)

        return 

        # block0 = "00FFFFFFFFFFFF004489D40311000000001B0103808048780ADAFFA3584AA22917494B2108003140454061408180010101010101010108E80030F2705A80B0588A00BA882100001E023A801871382D40582C4500BA882100001E000000FC0051443938302048444D49205258000000FD0017F10FFFF0000A202020202020015C"
        # block1 = "020359F0591005202204030207065D5E5F606162646566C2C4C376757E7D230F7F0778030C001000F8442FC88A010203048141001606080056580067D85DC401788867E2004B837F0000E10FE40EC7C6C5E3060F01E305FF01565E00A0A0A0295030203500BA882100001A662156AA51001E30468F3300BA882100001E0000DD"

        # edid_block0 = bytearray(bytes.fromhex(block0))
        # edid_block1 = bytearray(bytes.fromhex(block1))
        # edid_data = edid_block0 + edid_block1

        # args = {
        #     "PresavedName": "test001",
        #     "EdidData": edid_data
        # }

        # self._parent.controller.set_presaved_edid_data(args)
        # # 导入后再获取一下Presaved edid列表
        # args = {
        #     "EdidMode": 2
        # }
        # self._parent.controller.get_edid_list(args)

    def _on_export_edid(self):
        save_file_caption = QCoreApplication.translate("SD1242_4K_Setting_Form", u"Save EDID File", None)
        save_file_filter = QCoreApplication.translate("SD1242_4K_Setting_Form", u"EDID Bin Files (*.bin);;All Files (*)", None)
        filename, _ = QFileDialog.getSaveFileName(self, save_file_caption, '', save_file_filter)
        if filename:
            logging.debug(f'Selected file: {filename}')
            self.export_edid_data_filename = filename

            if self._select_edid_item_type == SD1242_4K_Setting.LEARNING_EDID_SELECT_TYPE:
                selected_item = self.learning_edid_listWidget.currentItem()
                if selected_item:
                    # learning edid list选中项的数据
                    row = self.learning_edid_listWidget.row(selected_item)
                    # self.learning_edid_listWidget.takeItem(row)
                    self._do_clear_selection_edid_item(SD1242_4K_Setting.LEARNING_EDID_SELECT_TYPE)

                    args = {
                        "EdidMode": 1,
                        "Position": row
                    }
                    self._parent.controller.get_selected_edid_data(args)

            elif self._select_edid_item_type == SD1242_4K_Setting.PRESAVE_EDID_SELECT_TYPE:
                selected_item = self.presaved_edid_listWidget.currentItem()
                if selected_item:
                    # 读取presaved edid list选中项的数据
                    row = self.presaved_edid_listWidget.row(selected_item)
                    self._do_clear_selection_edid_item(SD1242_4K_Setting.PRESAVE_EDID_SELECT_TYPE)
                    
                    args = {
                        "EdidMode": 2,
                        "Position": row
                    }
                    self._parent.controller.get_selected_edid_data(args)
        else:
            logging.debug("No selected file.")

    def showEvent(self, event):
        # self._parent.controller.get_version_info()
        # self._parent.controller.get_setting_params()
        self._parent.controller.get_device_edid()
        args = {
            "EdidMode": 1
        }
        self._parent.controller.get_edid_list(args)

        args = {
            "EdidMode": 2
        }
        self._parent.controller.get_edid_list(args)
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_device_edid":
            args = obj["args"]
            logging.debug("Get device's edid args:{}".format(args))
            # print("Get device's edid args:{}".format(args))
            
            lines = int(len(args["edidData"])/16)
            edid_data_str = ""
            for line in range(lines):
                line_data_str="{:02X}:".format(line)

                for i in range(16):
                    line_data_str += " {:02X}".format(args["edidData"][line*16 + i])
            
                if 0 <= line < lines - 1:
                    line_data_str += "\n"

                edid_data_str += line_data_str
            
            # print("edid_data_str:", edid_data_str)
            self.device_edid_plainTextEdit.setPlainText(edid_data_str)

        elif obj["function"] == "get_edid_list":
            args = obj["args"]
            if args["EdidMode"] == 1: # learning edid list
                self.learning_edid_listWidget.clear()
                self.learning_edid_listWidget.setSortingEnabled(False)
                for i in range(len(args["EdidList"])):
                    _qlistwidgetitem = QListWidgetItem(args["EdidList"][i]["ListName"])
                    # _qlistwidgetitem.setText(args["EdidList"][i]["ListName"])
                    _qlistwidgetitem.setTextAlignment(Qt.AlignCenter)
                    self.learning_edid_listWidget.addItem(_qlistwidgetitem)
                
                self.learning_edid_list = args["EdidList"]
            elif args["EdidMode"] == 2: # pre-saved edid list
                self.presaved_edid_listWidget.clear()
                self.presaved_edid_listWidget.setSortingEnabled(False)
                for i in range(len(args["EdidList"])):
                    _qlistwidgetitem = QListWidgetItem(args["EdidList"][i]["ListName"])
                    # _qlistwidgetitem.setText(args["EdidList"][i]["ListName"])
                    _qlistwidgetitem.setTextAlignment(Qt.AlignCenter)
                    self.presaved_edid_listWidget.addItem(_qlistwidgetitem)
                
                self.presaved_edid_list = args["EdidList"]
            else:
                logging.error("Error edid mode: {}".format(args["EdidMode"]))

        elif obj["function"] == "get_selected_edid_data":
            args = obj["args"]
            print("Get selected edid data args:{}".format(args))
            
            with open(self.export_edid_data_filename, 'wb') as file:
                file.write(args["EdidData"])
            
            msg_title = QCoreApplication.translate("SD1242_4K_Setting_Form", u"Export EDID Data", None)
            message_template = QCoreApplication.translate("SD1242_4K_Setting_Form", u"Export EDID data to {} success!", None)
            message = message_template.format(os.path.basename(self.export_edid_data_filename))
            QMessageBox.information(self, msg_title, message)
            self.export_edid_data_filename = ""

        elif obj["function"] == "delete_selected_edid":
            args = obj["args"]

from PySide6.QtGui import QIcon
from src.components.ClearableLineEdit import ClearableLineEdit

class SetImportEdidNameDialog(QDialog):

    name_text_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.setFixedSize(150, 80)
        self.setProperty("type", "rename")
        self.setWindowIcon(QIcon(relative_path("res/images/rename.png")))

    def initUI(self):
        self.setWindowTitle(QCoreApplication.translate("SD1242_4K_Setting_Form", u"Rename", None))
        layout = QVBoxLayout()
        self.input_edit = ClearableLineEdit(self)
        layout.addWidget(self.input_edit)
        hbox = QHBoxLayout()
        button = QPushButton(QCoreApplication.translate("SD1242_4K_Setting_Form", u"OK", None), self)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = SD1242_4K_Setting()
    window.show()
    sys.exit(app.exec())
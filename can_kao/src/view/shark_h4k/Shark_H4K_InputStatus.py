import re
import os, sys, logging
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QCoreApplication
from src.ui.shark_h4k.SharkH4kInputStatus_ui import Ui_SharkH4k_Input_Status_Widget_Form
from src.config.ChromaConfig import chroma_config

class SharkH4KInputStatusWidget(Ui_SharkH4k_Input_Status_Widget_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent

        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 4)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 4)
        self.gridLayout.setColumnStretch(6, 2)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 4)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 2)
        self.gridLayout_2.setColumnStretch(5, 4)
        self.gridLayout_2.setColumnStretch(6, 2)

        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(2, 4)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout_3.setColumnStretch(4, 2)
        self.gridLayout_3.setColumnStretch(5, 4)
        self.gridLayout_3.setColumnStretch(6, 2)

        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 2)
        self.gridLayout_4.setColumnStretch(2, 4)
        self.gridLayout_4.setColumnStretch(3, 1)
        self.gridLayout_4.setColumnStretch(4, 2)
        self.gridLayout_4.setColumnStretch(5, 4)
        self.gridLayout_4.setColumnStretch(6, 2)

        self.line.setProperty("type", "title_line")
        self.line_2.setProperty("type", "title_line")
        self.line_3.setProperty("type", "title_line")
        self.line_4.setProperty("type", "title_line")
        self.line_5.setProperty("type", "title_line")
        self.line_6.setProperty("type", "title_line")
        self.line_7.setProperty("type", "title_line")
        self.line_8.setProperty("type", "title_line")

        self.label.setProperty("type", "title")
        self.label_2.setProperty("type", "title")
        self.label_3.setProperty("type", "title")

        for list_group in self.lineedit_list:
            for lineedit in list_group:
                lineedit.line_edit.setReadOnly(True)
                lineedit.line_edit.setAlignment(Qt.AlignCenter)
                # lineedit.clear_button.setEnabled(False)
                lineedit.clear_button.hide()
    
    def retranslateUi(self, form):
        super().retranslateUi(form)

        self.lineedit_list = [
            [
            self.lineEdit_hdmi1_format, 
            self.lineEdit_hdmi1_space, 
            self.lineEdit_hdmi1_depth, 
            self.lineEdit_hdmi1_range
        ],
        [
            self.lineEdit_hdmi2_format, 
            self.lineEdit_hdmi2_space, 
            self.lineEdit_hdmi2_depth, 
            self.lineEdit_hdmi2_range
        ],
        [
            self.lineEdit_hdmi3_format, 
            self.lineEdit_hdmi3_space, 
            self.lineEdit_hdmi3_depth, 
            self.lineEdit_hdmi3_range
        ],
        [
            self.lineEdit_hdmi4_format, 
            self.lineEdit_hdmi4_space, 
            self.lineEdit_hdmi4_depth, 
            self.lineEdit_hdmi4_range
        ]]
        
        for list_group in self.lineedit_list:
            _none_text = QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", "None", None)

            if list_group[2].line_edit.text() == "0":
                list_group[0].line_edit.setText(_none_text)
                list_group[1].line_edit.setText(_none_text)
                list_group[3].line_edit.setText(_none_text) 

    def showEvent(self, event):
        self._parent.controller.get_input_status()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_input_status":
            args = obj["args"]
            logging.debug("args:{}".format(args))
            _channel_number = 4 # min(args["ChannelNumber"], 4)

            for i in range(_channel_number):
                _input = args["Video"][i]

                _format = _input["Format"]
                _none_text = QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", "None", None)
                self.lineedit_list[i][0].line_edit.setText(_format if _format != "None" else _none_text)
                self.lineedit_list[i][1].line_edit.setText(_input["ColorSpace"] if _format != "None" else _none_text)
                self.lineedit_list[i][2].line_edit.setText("{}".format(_input["BitDepth"] if _format != "None" else 0))
                self.lineedit_list[i][3].line_edit.setText(_input["Range"] if _format != "None" else _none_text) 

    
import re
import os, sys, logging
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QCoreApplication
from src.ui.cue01.input_status_widget_ui import Ui_CUE01_Input_Status_Widget_Form
from src.config.ChromaConfig import chroma_config

class InputStatusWidget(Ui_CUE01_Input_Status_Widget_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.setupUi(self)
        # self.init_ui()

    def init_ui(self):
        self.lineedit_list = [
            [
            self.lineEdit_fore_format, 
            self.lineEdit_fore_space, 
            self.lineEdit_fore_depth, 
            self.lineEdit_fore_range
        ],
        [
            self.lineEdit_back_format, 
            self.lineEdit_back_space, 
            self.lineEdit_back_depth, 
            self.lineEdit_back_range
        ],
        [
            self.lineEdit_aux_format, 
            self.lineEdit_aux_space, 
            self.lineEdit_aux_depth, 
            self.lineEdit_aux_range
        ]]
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

        self.line.setProperty("type", "title_line")
        self.line_2.setProperty("type", "title_line")
        self.line_3.setProperty("type", "title_line")
        self.line_4.setProperty("type", "title_line")
        self.line_5.setProperty("type", "title_line")
        self.line_6.setProperty("type", "title_line")

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

        _lineedit_list = [
            [
            self.lineEdit_fore_format, 
            self.lineEdit_fore_space, 
            self.lineEdit_fore_depth, 
            self.lineEdit_fore_range
        ],
        [
            self.lineEdit_back_format, 
            self.lineEdit_back_space, 
            self.lineEdit_back_depth, 
            self.lineEdit_back_range
        ],
        [
            self.lineEdit_aux_format, 
            self.lineEdit_aux_space, 
            self.lineEdit_aux_depth, 
            self.lineEdit_aux_range
        ]]
        
        for list_group in _lineedit_list:
            _none_text = QCoreApplication.translate("CUE01_Input_Status_Widget_Form", "None", None)

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
            _channel_number = min(args["ChannelNumber"], 3)

            for i in range(_channel_number):
                _input = args["Video"][i]
                # self._input_values["Format"][i].setText(_input["Format"])
                # self._input_values["SpaceColor"][i].setText(_input["ColorSpace"])
                # self._input_values["BitDepth"][i].setText("{}".format(_input["BitDepth"]))
                # self._input_values["Range"][i].setText(_input["Range"])

                _format = _input["Format"]
                _none_text = QCoreApplication.translate("CUE01_Input_Status_Widget_Form", "None", None)
                self.lineedit_list[i][0].line_edit.setText(_format if _format != "None" else _none_text)
                self.lineedit_list[i][1].line_edit.setText(_input["ColorSpace"] if _format != "None" else _none_text)
                self.lineedit_list[i][2].line_edit.setText("{}".format(_input["BitDepth"] if _format != "None" else 0))
                self.lineedit_list[i][3].line_edit.setText(_input["Range"] if _format != "None" else _none_text) 

                # if i == 3: # 设置当前采样分辨率
                #     chroma_config.set_ratio_by_format(_format)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = InputStatusWidget()
    window.show()
    sys.exit(app.exec())
    
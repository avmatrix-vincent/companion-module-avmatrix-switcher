import logging
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QSignalBlocker
from src.ui.cue01.outputInterfaceWidget_ui import Ui_CUE01_Output_Interface_Widget_Form
from src.model.cue01.cue01Preferences import Cue01Preferences
from globals import global_qss, toggle_layout_visibility

class OutputInterfaceWidget(Ui_CUE01_Output_Interface_Widget_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.setupUi(self)
        self._outputs = [
                {
                    "Format": 0,
                    "ColorSpace": 0,
                    "Range": 0
                },
                {
                    "Format": 0,
                    "ColorSpace": 0,
                    "Range": 0
                },
                {
                    "Format": 0,
                    "ColorSpace": 0,
                    "Range": 0
                },
                {
                    "Format": 0,
                    "ColorSpace": 0,
                    "Range": 0,
                    "AuxOutput": 0
                }
            ]
        
    def init_ui(self):
        _formats = Cue01Preferences.get_formats()
        _color_spaces = Cue01Preferences.get_color_spaces()
        _ranges = Cue01Preferences.get_ranges()
        _aux_outputs = Cue01Preferences.get_aux_outputs()

        self.comboBox_pvw_format.addItems(_formats)
        self.comboBox_matte_format.addItems(_formats)
        self.comboBox_full_format.addItems(_formats)
        self.comboBox_pgm_format.addItems(_formats)
        self.comboBox_output_format.addItems(_formats)
        self.comboBox_pvw_color.addItems(_color_spaces)
        self.comboBox_matte_color.addItems(_color_spaces)
        self.comboBox_pgm_color.addItems(_color_spaces)
        self.comboBox_full_color.addItems(_color_spaces)
        self.comboBox_pvw_range.addItems(_ranges)
        self.comboBox_matte_range.addItems(_ranges)
        self.comboBox_full_range.addItems(_ranges)
        self.comboBox_pgm_range.addItems(_ranges)
        self.comboBox_aux_ouput.addItems(_aux_outputs)

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
        self.label_4.setProperty("type", "title")

        # self._format_cbs = [self.comboBox_pvw_format, self.comboBox_matte_format, self.comboBox_full_format, self.comboBox_pgm_format, self.comboBox_output_format]
        self._format_cbs = [self.comboBox_pvw_format, self.comboBox_matte_format, self.comboBox_full_format, self.comboBox_output_format]
        self._space_color_cbs = [self.comboBox_pvw_color, self.comboBox_matte_color, self.comboBox_full_color, self.comboBox_pgm_color]
        self._range_cbs = [self.comboBox_pvw_range, self.comboBox_matte_range, self.comboBox_full_range, self.comboBox_pgm_range]

        self.comboBox_pvw_format.currentIndexChanged[int].connect(self._select_format)
        self.comboBox_matte_format.currentIndexChanged[int].connect(self._select_format)
        self.comboBox_full_format.currentIndexChanged[int].connect(self._select_format)
        # self.comboBox_pgm_format.currentIndexChanged[int].connect(self._select_format)
        self.comboBox_output_format.currentIndexChanged[int].connect(self._select_format)
        self.comboBox_pvw_color.currentIndexChanged[int].connect(self._select_color_space)
        self.comboBox_matte_color.currentIndexChanged[int].connect(self._select_color_space)
        self.comboBox_full_color.currentIndexChanged[int].connect(self._select_color_space)
        self.comboBox_pgm_color.currentIndexChanged[int].connect(self._select_color_space)
        self.comboBox_pvw_range.currentIndexChanged[int].connect(self._select_range)
        self.comboBox_matte_range.currentIndexChanged[int].connect(self._select_range)
        self.comboBox_full_range.currentIndexChanged[int].connect(self._select_range)
        self.comboBox_pgm_range.currentIndexChanged[int].connect(self._select_range)
        self.comboBox_aux_ouput.currentIndexChanged[int].connect(self._select_aux_output)

        # 只显示Output format和Aux output控件，隐藏其他控件
        toggle_layout_visibility(self.horizontalLayout, False)
        toggle_layout_visibility(self.horizontalLayout_2, False)
        toggle_layout_visibility(self.horizontalLayout_3, False)
        toggle_layout_visibility(self.horizontalLayout_4, False)
        toggle_layout_visibility(self.horizontalLayout_5, False)
        toggle_layout_visibility(self.horizontalLayout_6, False)
        toggle_layout_visibility(self.horizontalLayout_7, False)
        toggle_layout_visibility(self.horizontalLayout_8, False)

    def _select_format(self, index):
        try:
            sender = self.sender()

            for i in range(len(self._format_cbs)):
                if sender == self._format_cbs[i]:
                    if self._outputs[i]["Format"] != index:
                        logging.debug("select format {}:{}".format(i, index))
                        self._outputs[i]["Format"] = index
                        _args = {
                            "Index": i,
                            "Format": Cue01Preferences.get_format_by_index(0xFE if index==0 else index)
                            # "Format": Cue01Preferences.get_format_by_index(0xFE if index==0 else index - 1)
                        }
                        self._parent.controller.set_output_interface(_args)
        except:
            import traceback
            print(traceback.format_exc())

    def _select_color_space(self, index):
        return
        sender = self.sender()

        for i in range(len(self._space_color_cbs)):
            if sender == self._space_color_cbs[i]:
                if self._outputs[i]["ColorSpace"] != index:
                    logging.debug("select color space {}:{}".format(i, index))
                    self._outputs[i]["ColorSpace"] = index
                    _args = {
                        "Index": i,
                        "ColorSpace": Cue01Preferences.get_color_space_by_index(index)
                    }
                    self._parent.controller.set_output_interface(_args)

    def _select_range(self, index):
        return
        sender = self.sender()

        for i in range(len(self._range_cbs)):
            if sender == self._range_cbs[i]:
                if self._outputs[i]["Range"] != index:
                    logging.debug("select range {}:{}".format(i, index))
                    self._outputs[i]["Range"] = index
                    _args = {
                        "Index": i,
                        "Range": Cue01Preferences.get_range_by_index(index)
                    }
                    self._parent.controller.set_output_interface(_args)

    def _select_aux_output(self, index):
        if self._outputs[3]["AuxOutput"] != index:
            logging.debug("select aux output:{}".format(index))
            self._outputs[3]["AuxOutput"] = index
            _args = {
                "Index": 3,
                "AuxOutput": Cue01Preferences.get_aux_output_by_index(index)
            }
            self._parent.controller.set_output_interface(_args)

    def showEvent(self, event):
        self._parent.controller.get_output_interface()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_output_interface_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))
            _output = args["Output"]
            _output_num = min(args["Number"], len(self._format_cbs))

            for i in range(_output_num):
                _format_index = Cue01Preferences.get_index_by_format(_output[i]["Format"])
                if _format_index == 0xFF:
                    self._outputs[i]["Format"] = 0
                    with QSignalBlocker(self._format_cbs[i]):
                        self._format_cbs[i].setCurrentIndex(0)
                else:
                    self._outputs[i]["Format"] = _format_index
                    with QSignalBlocker(self._format_cbs[i]):
                        self._format_cbs[i].setCurrentIndex(_format_index)

                _color_space_index = Cue01Preferences.get_index_by_color_space(_output[i]["ColorSpace"])
                if _color_space_index != 0xFF:
                    self._outputs[i]["ColorSpace"] = _color_space_index
                    with QSignalBlocker(self._space_color_cbs[i]):
                        self._space_color_cbs[i].setCurrentIndex(_color_space_index)

                _range_index = Cue01Preferences.get_index_by_range(_output[i]["Range"])
                if _range_index != 0xFF:
                    self._outputs[i]["Range"] = _range_index
                    with QSignalBlocker(self._range_cbs[i]):
                        self._range_cbs[i].setCurrentIndex(_range_index)

            _aux_output_index = Cue01Preferences.get_index_by_aux_output(_output[3]["AuxOutput"])
            if _aux_output_index != 0xFF:
                self._outputs[3]["AuxOutput"] = _aux_output_index
                with QSignalBlocker(self.comboBox_aux_ouput):
                    self.comboBox_aux_ouput.setCurrentIndex(_aux_output_index)

        elif obj["function"] == "set_output_interface":
            args = obj["args"]
            logging.debug("Set output interface args:{}".format(args))
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OutputInterfaceWidget()
    window.init_ui()
    window.show()
    window.setStyleSheet(global_qss)
    sys.exit(app.exec())

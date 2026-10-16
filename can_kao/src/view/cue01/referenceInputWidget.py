
import logging

from PySide6.QtWidgets import QWidget
from src.ui.cue01.referenceInputWidget_ui import Ui_CUE01_Reference_Input_Widget_Form
from src.model.cue01.cue01Preferences import Cue01Preferences

class ReferenceInputWidget(Ui_CUE01_Reference_Input_Widget_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.setupUi(self)

    def init_ui(self):
        _inputs = Cue01Preferences.get_inputs()
        for i in range(len(_inputs)):
            self.comboBox_ref.addItem(_inputs[i])
        self.comboBox_ref.currentIndexChanged[int].connect(self._select_reference_input)

        self.label_2.hide()
        self.comboBox_format.hide()

    def _select_reference_input(self, index):
        sender = self.sender()

        if sender == self.comboBox_ref:
            if self._ref_input != index:
                logging.debug("select reference input:{}".format(index))
                self._ref_input = index
                _args = {
                        "ReferenceInput": Cue01Preferences.get_input_by_index(index)
                    }
                self._parent.controller.set_reference_input(_args)

    def showEvent(self, event):
        self._parent.controller.get_reference_enhancement()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_ref_enhance_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))
            _ref_input = Cue01Preferences.get_index_by_input(args["ReferenceInput"]) 
            if _ref_input != 0xFF:
                self._ref_input = _ref_input
                self.comboBox_ref.setCurrentIndex(_ref_input)
        elif obj["function"] == "set_ref_input":
            args = obj["args"]
            logging.debug("Set reference input args:{}".format(args))
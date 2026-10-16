import logging

from PySide6.QtWidgets import QWidget, QButtonGroup
from PySide6.QtCore import Qt, QSignalBlocker, QCoreApplication
from src.model.cue01.cue01Preferences import Cue01Preferences
from src.ui.cue01.sourceWidget_ui import Ui_CUE01_Source_Form

class SourceWidget(Ui_CUE01_Source_Form, QWidget):
    def __init__(self, parent):
        super(SourceWidget, self).__init__(parent)
        self._parent = parent
        self.setupUi(self)

    def init_ui(self):
        _formats = Cue01Preferences.get_formats()
        _bg_sources = Cue01Preferences.get_bg_sources()
        _aux_sources = Cue01Preferences.get_aux_outputs()
        self.comboBox_output_format.addItems(_formats)

        # self.comboBox_bg_source.addItems(_bg_sources)
        # self.comboBox_aux_source.addItems(_aux_sources)

        for i in range(len(_bg_sources)):
            self.comboBox_bg_source.addItem(QCoreApplication.translate("CUE01_Source_Form", _bg_sources[i], None))

        for i in range(len(_aux_sources)):
            self.comboBox_aux_source.addItem(QCoreApplication.translate("CUE01_Source_Form", _aux_sources[i], None))

        _usk_edge_stage2_rbtn_group = QButtonGroup(self.radio_widget)
        _usk_edge_stage2_rbtn_group.addButton(self.radioButton_usk)
        _usk_edge_stage2_rbtn_group.addButton(self.radioButton_dsk)
        _usk_edge_stage2_rbtn_group.buttonClicked.connect(self.on_usk_edge_stage2_changed)
        self.comboBox_output_format.currentIndexChanged.connect(self._select_format)
        self.comboBox_bg_source.currentIndexChanged.connect(self.on_bg_source_changed)
        self.comboBox_aux_source.currentIndexChanged.connect(self.on_aux_source_changed)

    def _select_format(self, index):
        try:
            logging.debug("select output format3 :{}".format(index))
            _args = {
                "Index": 3,
                # "Format": Cue01Preferences.get_format_by_index(0xFE if index==0 else index)
                "Format": Cue01Preferences.get_format_by_index(index)
                # "Format": Cue01Preferences.get_format_by_index(0xFE if index==0 else index - 1)
            }
            self._parent.controller.set_output_interface(_args)
        except:
            import traceback
            print(traceback.format_exc())

    def on_usk_edge_stage2_changed(self, button):
        logging.debug("select matte source:{}".format(button.text()))
        matte_source = 0
        if self.radioButton_usk.isChecked():
            matte_source = 0
        elif self.radioButton_dsk.isChecked():
            matte_source = 1
        _args = {
            "MatteSource": matte_source
        }
        self._parent.controller.set_source_params(_args)

    def on_bg_source_changed(self, index):
        logging.debug("select bg source:{}".format(index))
        _args = {
                "BackgroundSource": Cue01Preferences.get_bg_src_by_index(index)
            }
        self._parent.controller.set_source_params(_args)

    def on_aux_source_changed(self, index):
        logging.debug("select aux output:{}".format(index))
        _args = {
                "AuxOutput": Cue01Preferences.get_aux_output_by_index(index)
            }
        self._parent.controller.set_source_params(_args)

    def retranslateUi(self, form):
        super().retranslateUi(form)

        _bg_sources = Cue01Preferences.get_bg_sources()
        _aux_sources = Cue01Preferences.get_aux_outputs()

        for i in range(len(_bg_sources)):
            _item_text = QCoreApplication.translate("CUE01_Source_Form", _bg_sources[i], None)
            self.comboBox_bg_source.setItemText(i, _item_text)

        for i in range(len(_aux_sources)):
            _item_text = QCoreApplication.translate("CUE01_Source_Form", _aux_sources[i], None)
            self.comboBox_aux_source.setItemText(i, _item_text)

    def showEvent(self, event):
        self._parent.controller.get_output_interface()
        self._parent.controller.get_source_params()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_output_interface_params":
            args = obj["args"]
            logging.debug("output format3 args:{}".format(args))
            _output = args["Output"]
            _format_index = Cue01Preferences.get_index_by_format(_output[3]["Format"])
            if _format_index != 0xFF:
                with QSignalBlocker(self.comboBox_output_format):
                    print(_format_index)
                    self.comboBox_output_format.setCurrentIndex(_format_index)
        if obj["function"] == "get_source_params":
            args = obj["args"]
            logging.debug("source params args:{}".format(args))
            _matte_source = args["MatteSource"]
            _bg_source = args["BackgroundSource"]
            _aux_output = args["AuxOutput"]
            if _matte_source == 0:
                self.radioButton_usk.setChecked(True)
            elif _matte_source == 1:    
                self.radioButton_dsk.setChecked(True)

            bg_index = Cue01Preferences.get_index_by_bg_src(_bg_source)
            if bg_index == 0xFF:
                bg_index = 0
            with QSignalBlocker(self.comboBox_bg_source):
                self.comboBox_bg_source.setCurrentIndex(bg_index)
                
            aux_index = Cue01Preferences.get_index_by_aux_output(_aux_output)
            if aux_index == 0xFF:
                aux_index = 0
            with QSignalBlocker(self.comboBox_aux_source):
                self.comboBox_aux_source.setCurrentIndex(aux_index)


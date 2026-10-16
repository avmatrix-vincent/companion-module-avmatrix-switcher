import logging

from PySide6 import QtWidgets, QtCore

class RegReadWriteWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(RegReadWriteWidget, self).__init__(parent)

    def setupUi(self):
        _layout = QtWidgets.QVBoxLayout(self)
        _layout.setSpacing(0)
        _layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        _layout.setContentsMargins(0, 0, 0, 0)

        _label = QtWidgets.QLabel("RegReadWrite")
        _label.setStyleSheet("QLabel {background: gray; border-top: 1px solid red; border-bottom: none; border-left: none; border-right: none;}")
        _label.setFixedSize(200, 200)

        _layout.addWidget(_label)
        self.setLayout(_layout)
    
    def handle_async_callback(self, obj):
        print("RegReadWriteWidget handle_async_callback obj:", obj)
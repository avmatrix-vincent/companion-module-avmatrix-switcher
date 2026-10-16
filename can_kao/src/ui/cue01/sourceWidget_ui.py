# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sourceWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.components.CustomComboBox import CustomComboBox

class Ui_CUE01_Source_Form(object):
    def setupUi(self, CUE01_Source_Form):
        if not CUE01_Source_Form.objectName():
            CUE01_Source_Form.setObjectName(u"CUE01_Source_Form")
        CUE01_Source_Form.resize(800, 500)
        self.verticalLayout = QVBoxLayout(CUE01_Source_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(18)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(CUE01_Source_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.comboBox_bg_source = CustomComboBox(CUE01_Source_Form)
        self.comboBox_bg_source.setObjectName(u"comboBox_bg_source")

        self.gridLayout.addWidget(self.comboBox_bg_source, 1, 1, 1, 1)

        self.radio_widget = QWidget(CUE01_Source_Form)
        self.radio_widget.setObjectName(u"radio_widget")
        self.horizontalLayout = QHBoxLayout(self.radio_widget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_usk = QRadioButton(self.radio_widget)
        self.radioButton_usk.setObjectName(u"radioButton_usk")
        self.radioButton_usk.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_usk)

        self.radioButton_dsk = QRadioButton(self.radio_widget)
        self.radioButton_dsk.setObjectName(u"radioButton_dsk")

        self.horizontalLayout.addWidget(self.radioButton_dsk)


        self.gridLayout.addWidget(self.radio_widget, 2, 1, 1, 1)

        self.label = QLabel(CUE01_Source_Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(CUE01_Source_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.comboBox_aux_source = CustomComboBox(CUE01_Source_Form)
        self.comboBox_aux_source.setObjectName(u"comboBox_aux_source")

        self.gridLayout.addWidget(self.comboBox_aux_source, 3, 1, 1, 1)

        self.comboBox_output_format = CustomComboBox(CUE01_Source_Form)
        self.comboBox_output_format.setObjectName(u"comboBox_output_format")

        self.gridLayout.addWidget(self.comboBox_output_format, 0, 1, 1, 1)

        self.label_4 = QLabel(CUE01_Source_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 254, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(CUE01_Source_Form)

        QMetaObject.connectSlotsByName(CUE01_Source_Form)
    # setupUi

    def retranslateUi(self, CUE01_Source_Form):
        CUE01_Source_Form.setWindowTitle(QCoreApplication.translate("CUE01_Source_Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_Source_Form", u"AUX Source", None))
        self.radioButton_usk.setText(QCoreApplication.translate("CUE01_Source_Form", u"USK Matte", None))
        self.radioButton_dsk.setText(QCoreApplication.translate("CUE01_Source_Form", u"DSK Matte", None))
        self.label.setText(QCoreApplication.translate("CUE01_Source_Form", u"BG Source", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_Source_Form", u"Matte Source", None))
        self.label_4.setText(QCoreApplication.translate("CUE01_Source_Form", u"Output Format", None))
    # retranslateUi


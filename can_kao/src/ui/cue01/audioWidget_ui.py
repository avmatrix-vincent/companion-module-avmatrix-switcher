# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audioWidget.ui'
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

from src.components.SingleSliderWithSpinbox import SingleSliderWithSpinbox

class Ui_CUE01_Audio_Form(object):
    def setupUi(self, CUE01_Audio_Form):
        if not CUE01_Audio_Form.objectName():
            CUE01_Audio_Form.setObjectName(u"CUE01_Audio_Form")
        CUE01_Audio_Form.resize(800, 500)
        self.verticalLayout = QVBoxLayout(CUE01_Audio_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(18)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(CUE01_Audio_Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(CUE01_Audio_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.widget_volumn = SingleSliderWithSpinbox(CUE01_Audio_Form)
        self.widget_volumn.setObjectName(u"widget_volumn")

        self.gridLayout.addWidget(self.widget_volumn, 1, 1, 1, 1)

        self.radio_widget = QWidget(CUE01_Audio_Form)
        self.radio_widget.setObjectName(u"radio_widget")
        self.horizontalLayout = QHBoxLayout(self.radio_widget)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_mute = QRadioButton(self.radio_widget)
        self.radioButton_mute.setObjectName(u"radioButton_mute")
        self.radioButton_mute.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_mute)

        self.radioButton_fg_in = QRadioButton(self.radio_widget)
        self.radioButton_fg_in.setObjectName(u"radioButton_fg_in")

        self.horizontalLayout.addWidget(self.radioButton_fg_in)

        self.radioButton_bg_in = QRadioButton(self.radio_widget)
        self.radioButton_bg_in.setObjectName(u"radioButton_bg_in")

        self.horizontalLayout.addWidget(self.radioButton_bg_in)

        self.radioButton_dsk_in = QRadioButton(self.radio_widget)
        self.radioButton_dsk_in.setObjectName(u"radioButton_dsk_in")

        self.horizontalLayout.addWidget(self.radioButton_dsk_in)

        self.radioButton_line_in = QRadioButton(self.radio_widget)
        self.radioButton_line_in.setObjectName(u"radioButton_line_in")

        self.horizontalLayout.addWidget(self.radioButton_line_in)


        self.gridLayout.addWidget(self.radio_widget, 0, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 338, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(CUE01_Audio_Form)

        QMetaObject.connectSlotsByName(CUE01_Audio_Form)
    # setupUi

    def retranslateUi(self, CUE01_Audio_Form):
        CUE01_Audio_Form.setWindowTitle(QCoreApplication.translate("CUE01_Audio_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("CUE01_Audio_Form", u"PGM", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_Audio_Form", u"Volume", None))
        self.radioButton_mute.setText(QCoreApplication.translate("CUE01_Audio_Form", u"Mute", None))
        self.radioButton_fg_in.setText(QCoreApplication.translate("CUE01_Audio_Form", u"FG In", None))
        self.radioButton_bg_in.setText(QCoreApplication.translate("CUE01_Audio_Form", u"BG In", None))
        self.radioButton_dsk_in.setText(QCoreApplication.translate("CUE01_Audio_Form", u"DSK In", None))
        self.radioButton_line_in.setText(QCoreApplication.translate("CUE01_Audio_Form", u"Line-In", None))
    # retranslateUi


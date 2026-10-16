# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'referenceInputWidget.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from src.components.CustomComboBox import CustomComboBox

class Ui_CUE01_Reference_Input_Widget_Form(object):
    def setupUi(self, CUE01_Reference_Input_Widget_Form):
        if not CUE01_Reference_Input_Widget_Form.objectName():
            CUE01_Reference_Input_Widget_Form.setObjectName(u"CUE01_Reference_Input_Widget_Form")
        CUE01_Reference_Input_Widget_Form.resize(800, 500)
        self.verticalLayout_2 = QVBoxLayout(CUE01_Reference_Input_Widget_Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(18)
        self.gridLayout.setVerticalSpacing(20)
        self.label = QLabel(CUE01_Reference_Input_Widget_Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_ref = CustomComboBox(CUE01_Reference_Input_Widget_Form)
        self.comboBox_ref.setObjectName(u"comboBox_ref")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ref.sizePolicy().hasHeightForWidth())
        self.comboBox_ref.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.comboBox_ref, 0, 1, 1, 1)

        self.label_2 = QLabel(CUE01_Reference_Input_Widget_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBox_format = CustomComboBox(CUE01_Reference_Input_Widget_Form)
        self.comboBox_format.setObjectName(u"comboBox_format")
        sizePolicy.setHeightForWidth(self.comboBox_format.sizePolicy().hasHeightForWidth())
        self.comboBox_format.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.comboBox_format, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 350, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(CUE01_Reference_Input_Widget_Form)

        QMetaObject.connectSlotsByName(CUE01_Reference_Input_Widget_Form)
    # setupUi

    def retranslateUi(self, CUE01_Reference_Input_Widget_Form):
        CUE01_Reference_Input_Widget_Form.setWindowTitle(QCoreApplication.translate("CUE01_Reference_Input_Widget_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("CUE01_Reference_Input_Widget_Form", u"Reference", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_Reference_Input_Widget_Form", u"Format", None))
    # retranslateUi


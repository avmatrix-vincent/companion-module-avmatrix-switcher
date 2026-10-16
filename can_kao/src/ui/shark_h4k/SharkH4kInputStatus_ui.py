# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SharkH4kInputStatus.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.components.ClearableLineEdit import ClearableLineEdit

class Ui_SharkH4k_Input_Status_Widget_Form(object):
    def setupUi(self, SharkH4k_Input_Status_Widget_Form):
        if not SharkH4k_Input_Status_Widget_Form.objectName():
            SharkH4k_Input_Status_Widget_Form.setObjectName(u"SharkH4k_Input_Status_Widget_Form")
        SharkH4k_Input_Status_Widget_Form.resize(800, 500)
        self.layoutWidget = QWidget(SharkH4k_Input_Status_Widget_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 761, 451))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(130, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_20)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.lineEdit_hdmi1_depth = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi1_depth.setObjectName(u"lineEdit_hdmi1_depth")

        self.gridLayout.addWidget(self.lineEdit_hdmi1_depth, 0, 5, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 6, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)

        self.lineEdit_hdmi1_format = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi1_format.setObjectName(u"lineEdit_hdmi1_format")

        self.gridLayout.addWidget(self.lineEdit_hdmi1_format, 0, 2, 1, 1)

        self.lineEdit_hdmi1_space = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi1_space.setObjectName(u"lineEdit_hdmi1_space")

        self.gridLayout.addWidget(self.lineEdit_hdmi1_space, 1, 2, 1, 1)

        self.lineEdit_hdmi1_range = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi1_range.setObjectName(u"lineEdit_hdmi1_range")

        self.gridLayout.addWidget(self.lineEdit_hdmi1_range, 1, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_21)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(130, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_4 = QFrame(self.layoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_22)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.lineEdit_hdmi2_depth = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi2_depth.setObjectName(u"lineEdit_hdmi2_depth")

        self.gridLayout_2.addWidget(self.lineEdit_hdmi2_depth, 0, 5, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_10, 1, 1, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 4, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 1, 6, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 1, 3, 1, 1)

        self.lineEdit_hdmi2_space = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi2_space.setObjectName(u"lineEdit_hdmi2_space")

        self.gridLayout_2.addWidget(self.lineEdit_hdmi2_space, 1, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 0, 6, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 3, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.lineEdit_hdmi2_format = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi2_format.setObjectName(u"lineEdit_hdmi2_format")

        self.gridLayout_2.addWidget(self.lineEdit_hdmi2_format, 0, 2, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_11, 1, 4, 1, 1)

        self.lineEdit_hdmi2_range = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi2_range.setObjectName(u"lineEdit_hdmi2_range")

        self.gridLayout_2.addWidget(self.lineEdit_hdmi2_range, 1, 5, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_23)

        self.line_5 = QFrame(self.layoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(130, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_24)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(15)
        self.horizontalSpacer_15 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_15, 0, 3, 1, 1)

        self.lineEdit_hdmi3_space = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi3_space.setObjectName(u"lineEdit_hdmi3_space")

        self.gridLayout_3.addWidget(self.lineEdit_hdmi3_space, 1, 2, 1, 1)

        self.lineEdit_hdmi3_depth = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi3_depth.setObjectName(u"lineEdit_hdmi3_depth")

        self.gridLayout_3.addWidget(self.lineEdit_hdmi3_depth, 0, 5, 1, 1)

        self.lineEdit_hdmi3_format = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi3_format.setObjectName(u"lineEdit_hdmi3_format")

        self.gridLayout_3.addWidget(self.lineEdit_hdmi3_format, 0, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 0, 0, 1, 1)

        self.lineEdit_hdmi3_range = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi3_range.setObjectName(u"lineEdit_hdmi3_range")

        self.gridLayout_3.addWidget(self.lineEdit_hdmi3_range, 1, 5, 1, 1)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_15, 1, 4, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_14, 1, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_13, 0, 4, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_14, 1, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 1, 3, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_17, 0, 6, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_18, 1, 6, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_25)

        self.line_7 = QFrame(self.layoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_7)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(130, 16777215))
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_16)

        self.line_8 = QFrame(self.layoutWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_8)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_26)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(15)
        self.lineEdit_hdmi4_space = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi4_space.setObjectName(u"lineEdit_hdmi4_space")

        self.gridLayout_4.addWidget(self.lineEdit_hdmi4_space, 1, 2, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_31, 0, 6, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_30, 1, 3, 1, 1)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_20, 0, 4, 1, 1)

        self.lineEdit_hdmi4_range = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi4_range.setObjectName(u"lineEdit_hdmi4_range")

        self.gridLayout_4.addWidget(self.lineEdit_hdmi4_range, 1, 5, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_27, 0, 3, 1, 1)

        self.lineEdit_hdmi4_depth = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi4_depth.setObjectName(u"lineEdit_hdmi4_depth")

        self.gridLayout_4.addWidget(self.lineEdit_hdmi4_depth, 0, 5, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_32, 1, 6, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_29, 1, 0, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_28, 0, 0, 1, 1)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_17, 1, 4, 1, 1)

        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_19, 0, 1, 1, 1)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_18, 1, 1, 1, 1)

        self.lineEdit_hdmi4_format = ClearableLineEdit(self.layoutWidget)
        self.lineEdit_hdmi4_format.setObjectName(u"lineEdit_hdmi4_format")

        self.gridLayout_4.addWidget(self.lineEdit_hdmi4_format, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.retranslateUi(SharkH4k_Input_Status_Widget_Form)

        QMetaObject.connectSlotsByName(SharkH4k_Input_Status_Widget_Form)
    # setupUi

    def retranslateUi(self, SharkH4k_Input_Status_Widget_Form):
        SharkH4k_Input_Status_Widget_Form.setWindowTitle(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"HDMI 1", None))
        self.label_7.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Range   ", None))
        self.label_4.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Format   ", None))
        self.label_6.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Bit Depth   ", None))
        self.label_5.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Color Space   ", None))
        self.label_2.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"HDMI 2", None))
        self.label_10.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Color Space   ", None))
        self.label_9.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Bit Depth   ", None))
        self.label_8.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Format   ", None))
        self.label_11.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Range   ", None))
        self.label_3.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"HDMI 3", None))
        self.label_15.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Range   ", None))
        self.label_14.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Color Space   ", None))
        self.label_12.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Format   ", None))
        self.label_13.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Bit Depth   ", None))
        self.label_16.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"HDMI 4", None))
        self.label_20.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Bit Depth   ", None))
        self.label_17.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Range   ", None))
        self.label_19.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Format   ", None))
        self.label_18.setText(QCoreApplication.translate("SharkH4k_Input_Status_Widget_Form", u"Color Space   ", None))
    # retranslateUi


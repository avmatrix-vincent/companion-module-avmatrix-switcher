# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_status_widget.ui'
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

class Ui_CUE01_Input_Status_Widget_Form(object):
    def setupUi(self, CUE01_Input_Status_Widget_Form):
        if not CUE01_Input_Status_Widget_Form.objectName():
            CUE01_Input_Status_Widget_Form.setObjectName(u"CUE01_Input_Status_Widget_Form")
        CUE01_Input_Status_Widget_Form.resize(800, 500)
        self.verticalLayout = QVBoxLayout(CUE01_Input_Status_Widget_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)

        self.line = QFrame(CUE01_Input_Status_Widget_Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(CUE01_Input_Status_Widget_Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(130, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.line_2 = QFrame(CUE01_Input_Status_Widget_Form)
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
        self.label_4 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.label_6 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)

        self.lineEdit_fore_space = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_fore_space.setObjectName(u"lineEdit_fore_space")

        self.gridLayout.addWidget(self.lineEdit_fore_space, 1, 2, 1, 1)

        self.label_5 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.lineEdit_fore_format = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_fore_format.setObjectName(u"lineEdit_fore_format")

        self.gridLayout.addWidget(self.lineEdit_fore_format, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.lineEdit_fore_depth = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_fore_depth.setObjectName(u"lineEdit_fore_depth")

        self.gridLayout.addWidget(self.lineEdit_fore_depth, 0, 5, 1, 1)

        self.label_7 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)

        self.lineEdit_fore_range = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_fore_range.setObjectName(u"lineEdit_fore_range")

        self.gridLayout.addWidget(self.lineEdit_fore_range, 1, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 6, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 6, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_21)

        self.line_3 = QFrame(CUE01_Input_Status_Widget_Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.label_2 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(130, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_4 = QFrame(CUE01_Input_Status_Widget_Form)
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
        self.lineEdit_back_range = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_back_range.setObjectName(u"lineEdit_back_range")

        self.gridLayout_2.addWidget(self.lineEdit_back_range, 1, 5, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 1, 3, 1, 1)

        self.lineEdit_back_depth = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_back_depth.setObjectName(u"lineEdit_back_depth")

        self.gridLayout_2.addWidget(self.lineEdit_back_depth, 0, 5, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.lineEdit_back_space = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_back_space.setObjectName(u"lineEdit_back_space")

        self.gridLayout_2.addWidget(self.lineEdit_back_space, 1, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 3, 1, 1)

        self.label_8 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)

        self.lineEdit_back_format = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_back_format.setObjectName(u"lineEdit_back_format")

        self.gridLayout_2.addWidget(self.lineEdit_back_format, 0, 2, 1, 1)

        self.label_10 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_10, 1, 1, 1, 1)

        self.label_11 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_11, 1, 4, 1, 1)

        self.label_9 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 4, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 0, 6, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 1, 6, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_23)

        self.line_5 = QFrame(CUE01_Input_Status_Widget_Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.label_3 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(130, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.line_6 = QFrame(CUE01_Input_Status_Widget_Form)
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

        self.lineEdit_aux_space = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_aux_space.setObjectName(u"lineEdit_aux_space")

        self.gridLayout_3.addWidget(self.lineEdit_aux_space, 1, 2, 1, 1)

        self.lineEdit_aux_depth = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_aux_depth.setObjectName(u"lineEdit_aux_depth")

        self.gridLayout_3.addWidget(self.lineEdit_aux_depth, 0, 5, 1, 1)

        self.lineEdit_aux_format = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_aux_format.setObjectName(u"lineEdit_aux_format")

        self.gridLayout_3.addWidget(self.lineEdit_aux_format, 0, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 0, 0, 1, 1)

        self.lineEdit_aux_range = ClearableLineEdit(CUE01_Input_Status_Widget_Form)
        self.lineEdit_aux_range.setObjectName(u"lineEdit_aux_range")

        self.gridLayout_3.addWidget(self.lineEdit_aux_range, 1, 5, 1, 1)

        self.label_15 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_15, 1, 4, 1, 1)

        self.label_14 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_14, 1, 1, 1, 1)

        self.label_12 = QLabel(CUE01_Input_Status_Widget_Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_13 = QLabel(CUE01_Input_Status_Widget_Form)
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

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(CUE01_Input_Status_Widget_Form)

        QMetaObject.connectSlotsByName(CUE01_Input_Status_Widget_Form)
    # setupUi

    def retranslateUi(self, CUE01_Input_Status_Widget_Form):
        CUE01_Input_Status_Widget_Form.setWindowTitle(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Foreground", None))
        self.label_4.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Format   ", None))
        self.label_6.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Bit Depth   ", None))
        self.label_5.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Color Space   ", None))
        self.label_7.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Range   ", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Background", None))
        self.label_8.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Format   ", None))
        self.label_10.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Color Space   ", None))
        self.label_11.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Range   ", None))
        self.label_9.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Bit Depth   ", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"AUX", None))
        self.label_15.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Range   ", None))
        self.label_14.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Color Space   ", None))
        self.label_12.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Format   ", None))
        self.label_13.setText(QCoreApplication.translate("CUE01_Input_Status_Widget_Form", u"Bit Depth   ", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lumaKeyWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from src.components.CustomSpinBox import CustomDoubleSpinBox
from src.components.SwitchButton import SwitchBtn
from superqt import QRangeSlider

class Ui_CUE01_Luma_Key_Widget_Form(object):
    def setupUi(self, CUE01_Luma_Key_Widget_Form):
        if not CUE01_Luma_Key_Widget_Form.objectName():
            CUE01_Luma_Key_Widget_Form.setObjectName(u"CUE01_Luma_Key_Widget_Form")
        CUE01_Luma_Key_Widget_Form.resize(800, 500)
        self.horizontalLayout_7 = QHBoxLayout(CUE01_Luma_Key_Widget_Form)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(200, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(CUE01_Luma_Key_Widget_Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.label_9)

        self.checkBox_status = QCheckBox(CUE01_Luma_Key_Widget_Form)
        self.checkBox_status.setObjectName(u"checkBox_status")

        self.horizontalLayout_8.addWidget(self.checkBox_status)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(CUE01_Luma_Key_Widget_Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.widget_tolerance_curve = SwitchBtn(CUE01_Luma_Key_Widget_Form)
        self.widget_tolerance_curve.setObjectName(u"widget_tolerance_curve")

        self.horizontalLayout_2.addWidget(self.widget_tolerance_curve)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(CUE01_Luma_Key_Widget_Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.widget_tolerance_invert = SwitchBtn(CUE01_Luma_Key_Widget_Form)
        self.widget_tolerance_invert.setObjectName(u"widget_tolerance_invert")

        self.horizontalLayout_2.addWidget(self.widget_tolerance_invert)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(CUE01_Luma_Key_Widget_Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.spinBox_tolerance_min = CustomDoubleSpinBox(CUE01_Luma_Key_Widget_Form)
        self.spinBox_tolerance_min.setObjectName(u"spinBox_tolerance_min")

        self.horizontalLayout_4.addWidget(self.spinBox_tolerance_min)

        self.rangeSlider_tolerance = QRangeSlider(CUE01_Luma_Key_Widget_Form)
        self.rangeSlider_tolerance.setObjectName(u"rangeSlider_tolerance")
        self.rangeSlider_tolerance.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.rangeSlider_tolerance)

        self.spinBox_tolerance_max = CustomDoubleSpinBox(CUE01_Luma_Key_Widget_Form)
        self.spinBox_tolerance_max.setObjectName(u"spinBox_tolerance_max")

        self.horizontalLayout_4.addWidget(self.spinBox_tolerance_max)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(CUE01_Luma_Key_Widget_Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.widget_keyClip_switchbtn = SwitchBtn(CUE01_Luma_Key_Widget_Form)
        self.widget_keyClip_switchbtn.setObjectName(u"widget_keyClip_switchbtn")

        self.horizontalLayout_3.addWidget(self.widget_keyClip_switchbtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(CUE01_Luma_Key_Widget_Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.widget_keyClip_curve_switchbtn = SwitchBtn(CUE01_Luma_Key_Widget_Form)
        self.widget_keyClip_curve_switchbtn.setObjectName(u"widget_keyClip_curve_switchbtn")

        self.horizontalLayout_3.addWidget(self.widget_keyClip_curve_switchbtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(CUE01_Luma_Key_Widget_Form)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.spinBox_keyClip_min = CustomDoubleSpinBox(CUE01_Luma_Key_Widget_Form)
        self.spinBox_keyClip_min.setObjectName(u"spinBox_keyClip_min")

        self.horizontalLayout_6.addWidget(self.spinBox_keyClip_min)

        self.rangeSlider_keyClip = QRangeSlider(CUE01_Luma_Key_Widget_Form)
        self.rangeSlider_keyClip.setObjectName(u"rangeSlider_keyClip")
        self.rangeSlider_keyClip.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.rangeSlider_keyClip)

        self.spinBox_keyClip_max = CustomDoubleSpinBox(CUE01_Luma_Key_Widget_Form)
        self.spinBox_keyClip_max.setObjectName(u"spinBox_keyClip_max")

        self.horizontalLayout_6.addWidget(self.spinBox_keyClip_max)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 170, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 3)

        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(200, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.retranslateUi(CUE01_Luma_Key_Widget_Form)

        QMetaObject.connectSlotsByName(CUE01_Luma_Key_Widget_Form)
    # setupUi

    def retranslateUi(self, CUE01_Luma_Key_Widget_Form):
        CUE01_Luma_Key_Widget_Form.setWindowTitle(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Luma Status", None))
        self.checkBox_status.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Inactive", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Tolerance Curve", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Tolerance Invert", None))
        self.label_6.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Tolerance", None))
        self.label_5.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Key Clip On/Off", None))
        self.label_4.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Key Clip Curve", None))
        self.label_8.setText(QCoreApplication.translate("CUE01_Luma_Key_Widget_Form", u"Key Clip", None))
    # retranslateUi


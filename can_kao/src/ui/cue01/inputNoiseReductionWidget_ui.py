# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputNoiseReductionWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.components.CustomComboBox import CustomComboBox
from src.components.CustomSpinBox import CustomSpinBox
from src.components.SingleSliderWithSpinbox import SingleSliderWithSpinbox
from src.components.SwitchButton import SwitchBtn

class Ui_CUE01_Input_Noise_Reduction_Widget_Form(object):
    def setupUi(self, CUE01_Input_Noise_Reduction_Widget_Form):
        if not CUE01_Input_Noise_Reduction_Widget_Form.objectName():
            CUE01_Input_Noise_Reduction_Widget_Form.setObjectName(u"CUE01_Input_Noise_Reduction_Widget_Form")
        CUE01_Input_Noise_Reduction_Widget_Form.resize(800, 500)
        self.horizontalLayout_11 = QHBoxLayout(CUE01_Input_Noise_Reduction_Widget_Form)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_8 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line = QFrame(CUE01_Input_Noise_Reduction_Widget_Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.line_2 = QFrame(CUE01_Input_Noise_Reduction_Widget_Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.comboBox_fore_nr = CustomComboBox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.comboBox_fore_nr.setObjectName(u"comboBox_fore_nr")

        self.horizontalLayout_5.addWidget(self.comboBox_fore_nr)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.checkBox_fore_nr_display = QCheckBox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.checkBox_fore_nr_display.setObjectName(u"checkBox_fore_nr_display")

        self.horizontalLayout_5.addWidget(self.checkBox_fore_nr_display)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_3 = QFrame(CUE01_Input_Noise_Reduction_Widget_Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.label_2 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_4 = QFrame(CUE01_Input_Noise_Reduction_Widget_Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_6.addWidget(self.label_8)

        self.comboBox_back_nr = CustomComboBox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.comboBox_back_nr.setObjectName(u"comboBox_back_nr")

        self.horizontalLayout_6.addWidget(self.comboBox_back_nr)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.checkBox_back_nr_display = QCheckBox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.checkBox_back_nr_display.setObjectName(u"checkBox_back_nr_display")

        self.horizontalLayout_6.addWidget(self.checkBox_back_nr_display)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_5 = QFrame(CUE01_Input_Noise_Reduction_Widget_Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.label_3 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.line_6 = QFrame(CUE01_Input_Noise_Reduction_Widget_Form)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_7.addWidget(self.label_9)

        self.comboBox_aux_nr = CustomComboBox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.comboBox_aux_nr.setObjectName(u"comboBox_aux_nr")

        self.horizontalLayout_7.addWidget(self.comboBox_aux_nr)

        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.checkBox_aux_nr_display = QCheckBox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.checkBox_aux_nr_display.setObjectName(u"checkBox_aux_nr_display")

        self.horizontalLayout_7.addWidget(self.checkBox_aux_nr_display)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_7 = QFrame(CUE01_Input_Noise_Reduction_Widget_Form)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_7)

        self.label_4 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_8 = QFrame(CUE01_Input_Noise_Reduction_Widget_Form)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_8.addWidget(self.label_6)

        self.widget_bnr_mode_switch_btn = SwitchBtn(CUE01_Input_Noise_Reduction_Widget_Form)
        self.widget_bnr_mode_switch_btn.setObjectName(u"widget_bnr_mode_switch_btn")

        self.horizontalLayout_8.addWidget(self.widget_bnr_mode_switch_btn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.label_11 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_8.addWidget(self.label_11)

        self.comboBox_bnr = CustomComboBox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.comboBox_bnr.setObjectName(u"comboBox_bnr")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_bnr.sizePolicy().hasHeightForWidth())
        self.comboBox_bnr.setSizePolicy(sizePolicy1)
        self.comboBox_bnr.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_8.addWidget(self.comboBox_bnr)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.label_12 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.spinBox = CustomSpinBox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_9.addWidget(self.spinBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.label_13 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_9.addWidget(self.label_13)

        self.spinBox_2 = CustomSpinBox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_9.addWidget(self.spinBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.widget_block_switchbtn = SwitchBtn(CUE01_Input_Noise_Reduction_Widget_Form)
        self.widget_block_switchbtn.setObjectName(u"widget_block_switchbtn")

        self.horizontalLayout_10.addWidget(self.widget_block_switchbtn)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.label_14 = QLabel(CUE01_Input_Noise_Reduction_Widget_Form)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_10.addWidget(self.label_14)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.widget_block_threshold = SingleSliderWithSpinbox(CUE01_Input_Noise_Reduction_Widget_Form)
        self.widget_block_threshold.setObjectName(u"widget_block_threshold")
        self.widget_block_threshold.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_10.addWidget(self.widget_block_threshold)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.horizontalSpacer_9 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)


        self.retranslateUi(CUE01_Input_Noise_Reduction_Widget_Form)

        QMetaObject.connectSlotsByName(CUE01_Input_Noise_Reduction_Widget_Form)
    # setupUi

    def retranslateUi(self, CUE01_Input_Noise_Reduction_Widget_Form):
        CUE01_Input_Noise_Reduction_Widget_Form.setWindowTitle(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"Foreground NR", None))
        self.label_5.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"NR Mode", None))
        self.checkBox_fore_nr_display.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"NR Motion Display On", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"Background NR", None))
        self.label_8.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"NR Mode", None))
        self.checkBox_back_nr_display.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"NR Motion Display On", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"AUX NR", None))
        self.label_9.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"NR Mode", None))
        self.checkBox_aux_nr_display.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"NR Motion Display On", None))
        self.label_4.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"BNR", None))
        self.label_6.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"BNR Mode", None))
        self.label_11.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"BNR Intensity", None))
        self.label_10.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"Block Coordinate", None))
        self.label_12.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"X(0-7)", None))
        self.label_13.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"Y(0-7)", None))
        self.label_7.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"Block Display", None))
        self.label_14.setText(QCoreApplication.translate("CUE01_Input_Noise_Reduction_Widget_Form", u"Block Threshold", None))
    # retranslateUi


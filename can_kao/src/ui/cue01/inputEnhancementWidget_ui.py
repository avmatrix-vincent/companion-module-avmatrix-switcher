# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputEnhancementWidget.ui'
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

from src.components.CustomComboBox import CustomComboBox
from src.components.SingleSliderWithSpinbox import SingleSliderWithSpinbox
from src.components.SwitchButton import SwitchBtn
import images_rc

class Ui_CUE01_Input_Enhancement_Widget_Form(object):
    def setupUi(self, CUE01_Input_Enhancement_Widget_Form):
        if not CUE01_Input_Enhancement_Widget_Form.objectName():
            CUE01_Input_Enhancement_Widget_Form.setObjectName(u"CUE01_Input_Enhancement_Widget_Form")
        CUE01_Input_Enhancement_Widget_Form.resize(800, 500)
        self.horizontalLayout_13 = QHBoxLayout(CUE01_Input_Enhancement_Widget_Form)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_34 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_34)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.line_2 = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(18)
        self.gridLayout.setVerticalSpacing(0)
        self.label_5 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_4 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_6 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_7 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.widget_fore_contrast = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_fore_contrast.setObjectName(u"widget_fore_contrast")

        self.gridLayout.addWidget(self.widget_fore_contrast, 0, 1, 1, 1)

        self.widget_fore_brightness = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_fore_brightness.setObjectName(u"widget_fore_brightness")

        self.gridLayout.addWidget(self.widget_fore_brightness, 1, 1, 1, 1)

        self.widget_fore_saturation = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_fore_saturation.setObjectName(u"widget_fore_saturation")

        self.gridLayout.addWidget(self.widget_fore_saturation, 2, 1, 1, 1)

        self.widget_fore_hue = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_fore_hue.setObjectName(u"widget_fore_hue")

        self.gridLayout.addWidget(self.widget_fore_hue, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.label_8 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.widget_fore_lti_switch_btn = SwitchBtn(CUE01_Input_Enhancement_Widget_Form)
        self.widget_fore_lti_switch_btn.setObjectName(u"widget_fore_lti_switch_btn")

        self.horizontalLayout_5.addWidget(self.widget_fore_lti_switch_btn)

        self.horizontalSpacer_5 = QSpacerItem(52, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_10 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.widget_fore_cti_switch_btn = SwitchBtn(CUE01_Input_Enhancement_Widget_Form)
        self.widget_fore_cti_switch_btn.setObjectName(u"widget_fore_cti_switch_btn")

        self.horizontalLayout_5.addWidget(self.widget_fore_cti_switch_btn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer_16 = QSpacerItem(14, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)

        self.comboBox_fore_color = CustomComboBox(CUE01_Input_Enhancement_Widget_Form)
        self.comboBox_fore_color.setObjectName(u"comboBox_fore_color")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_fore_color.sizePolicy().hasHeightForWidth())
        self.comboBox_fore_color.setSizePolicy(sizePolicy)
        self.comboBox_fore_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_4.addWidget(self.comboBox_fore_color)

        self.horizontalSpacer_8 = QSpacerItem(70, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fore_anti_alias_frame = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.fore_anti_alias_frame.setObjectName(u"fore_anti_alias_frame")
        self.fore_anti_alias_frame.setStyleSheet(u"#fore_anti_alias_frame{\n"
"	border-image: url(:/icons/images/alias_background.png);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.fore_anti_alias_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(18)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 10, 5)
        self.label_11 = QLabel(self.fore_anti_alias_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_15 = QLabel(self.fore_anti_alias_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_15, 0, 1, 1, 1)

        self.label_12 = QLabel(self.fore_anti_alias_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.widget_fore_anti_hori = SingleSliderWithSpinbox(self.fore_anti_alias_frame)
        self.widget_fore_anti_hori.setObjectName(u"widget_fore_anti_hori")

        self.gridLayout_2.addWidget(self.widget_fore_anti_hori, 1, 1, 1, 1)

        self.widget_fore_anti_verti = SingleSliderWithSpinbox(self.fore_anti_alias_frame)
        self.widget_fore_anti_verti.setObjectName(u"widget_fore_anti_verti")

        self.gridLayout_2.addWidget(self.widget_fore_anti_verti, 2, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 4)

        self.verticalLayout.addWidget(self.fore_anti_alias_frame)

        self.fore_peak_filter_frame = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.fore_peak_filter_frame.setObjectName(u"fore_peak_filter_frame")
        self.fore_peak_filter_frame.setStyleSheet(u"#fore_peak_filter_frame{\n"
"	border-image: url(:/icons/images/alias_background.png);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.fore_peak_filter_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(18)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 7, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.label_16 = QLabel(self.fore_peak_filter_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_16, 0, 1, 1, 1)

        self.label_13 = QLabel(self.fore_peak_filter_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.fore_peak_filter_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)

        self.widget_fore_peak_hori = SingleSliderWithSpinbox(self.fore_peak_filter_frame)
        self.widget_fore_peak_hori.setObjectName(u"widget_fore_peak_hori")

        self.gridLayout_3.addWidget(self.widget_fore_peak_hori, 1, 1, 1, 1)

        self.widget_fore_peak_verti = SingleSliderWithSpinbox(self.fore_peak_filter_frame)
        self.widget_fore_peak_verti.setObjectName(u"widget_fore_peak_verti")

        self.gridLayout_3.addWidget(self.widget_fore_peak_verti, 2, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 4)

        self.verticalLayout.addWidget(self.fore_peak_filter_frame)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(2, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_3 = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.label_2 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_4 = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(18)
        self.gridLayout_7.setVerticalSpacing(0)
        self.label_31 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_31, 1, 0, 1, 1)

        self.label_32 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_32, 2, 0, 1, 1)

        self.label_30 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_30, 0, 0, 1, 1)

        self.label_33 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_33, 3, 0, 1, 1)

        self.widget_back_contrast = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_back_contrast.setObjectName(u"widget_back_contrast")

        self.gridLayout_7.addWidget(self.widget_back_contrast, 0, 1, 1, 1)

        self.widget_back_brightness = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_back_brightness.setObjectName(u"widget_back_brightness")

        self.gridLayout_7.addWidget(self.widget_back_brightness, 1, 1, 1, 1)

        self.widget_back_saturation = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_back_saturation.setObjectName(u"widget_back_saturation")

        self.gridLayout_7.addWidget(self.widget_back_saturation, 2, 1, 1, 1)

        self.widget_back_hue = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_back_hue.setObjectName(u"widget_back_hue")

        self.gridLayout_7.addWidget(self.widget_back_hue, 3, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_25)

        self.label_34 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_34)

        self.widget_back_lti_switch_btn = SwitchBtn(CUE01_Input_Enhancement_Widget_Form)
        self.widget_back_lti_switch_btn.setObjectName(u"widget_back_lti_switch_btn")

        self.horizontalLayout_11.addWidget(self.widget_back_lti_switch_btn)

        self.horizontalSpacer_26 = QSpacerItem(52, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_26)

        self.label_35 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_35)

        self.widget_back_cti_switch_btn = SwitchBtn(CUE01_Input_Enhancement_Widget_Form)
        self.widget_back_cti_switch_btn.setObjectName(u"widget_back_cti_switch_btn")

        self.horizontalLayout_11.addWidget(self.widget_back_cti_switch_btn)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_27)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_36 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_36)

        self.horizontalSpacer = QSpacerItem(14, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.comboBox_back_color = CustomComboBox(CUE01_Input_Enhancement_Widget_Form)
        self.comboBox_back_color.setObjectName(u"comboBox_back_color")
        sizePolicy.setHeightForWidth(self.comboBox_back_color.sizePolicy().hasHeightForWidth())
        self.comboBox_back_color.setSizePolicy(sizePolicy)
        self.comboBox_back_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_12.addWidget(self.comboBox_back_color)

        self.horizontalSpacer_28 = QSpacerItem(70, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_28)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_10.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_29 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_29)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.back_alias_frame = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.back_alias_frame.setObjectName(u"back_alias_frame")
        self.back_alias_frame.setStyleSheet(u"#back_alias_frame{\n"
"	border-image: url(:/icons/images/alias_background.png);\n"
"}")
        self.gridLayout_8 = QGridLayout(self.back_alias_frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(18)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 10, 5)
        self.label_38 = QLabel(self.back_alias_frame)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_38, 1, 0, 1, 1)

        self.label_39 = QLabel(self.back_alias_frame)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_39, 2, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_30, 0, 0, 1, 1)

        self.label_37 = QLabel(self.back_alias_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_37, 0, 1, 1, 1)

        self.widget_back_anti_hori = SingleSliderWithSpinbox(self.back_alias_frame)
        self.widget_back_anti_hori.setObjectName(u"widget_back_anti_hori")

        self.gridLayout_8.addWidget(self.widget_back_anti_hori, 1, 1, 1, 1)

        self.widget_back_anti_verti = SingleSliderWithSpinbox(self.back_alias_frame)
        self.widget_back_anti_verti.setObjectName(u"widget_back_anti_verti")

        self.gridLayout_8.addWidget(self.widget_back_anti_verti, 2, 1, 1, 1)

        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(1, 4)

        self.verticalLayout_6.addWidget(self.back_alias_frame)

        self.back_filter_frame = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.back_filter_frame.setObjectName(u"back_filter_frame")
        self.back_filter_frame.setStyleSheet(u"#back_filter_frame{\n"
"	border-image: url(:/icons/images/alias_background.png);\n"
"}")
        self.gridLayout_9 = QGridLayout(self.back_filter_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(18)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 7, 5)
        self.label_40 = QLabel(self.back_filter_frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_40, 0, 1, 1, 1)

        self.label_42 = QLabel(self.back_filter_frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_42, 2, 0, 1, 1)

        self.label_41 = QLabel(self.back_filter_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_41, 1, 0, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_32, 0, 0, 1, 1)

        self.widget_back_peak_hori = SingleSliderWithSpinbox(self.back_filter_frame)
        self.widget_back_peak_hori.setObjectName(u"widget_back_peak_hori")

        self.gridLayout_9.addWidget(self.widget_back_peak_hori, 1, 1, 1, 1)

        self.widget_back_peak_verti = SingleSliderWithSpinbox(self.back_filter_frame)
        self.widget_back_peak_verti.setObjectName(u"widget_back_peak_verti")

        self.gridLayout_9.addWidget(self.widget_back_peak_verti, 2, 1, 1, 1)

        self.gridLayout_9.setColumnStretch(0, 1)
        self.gridLayout_9.setColumnStretch(1, 4)

        self.verticalLayout_6.addWidget(self.back_filter_frame)


        self.horizontalLayout_10.addLayout(self.verticalLayout_6)

        self.horizontalLayout_10.setStretch(0, 2)
        self.horizontalLayout_10.setStretch(2, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_5 = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.label_3 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.line_6 = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(18)
        self.gridLayout_4.setVerticalSpacing(0)
        self.label_17 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_20 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_19 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_18 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_18, 1, 0, 1, 1)

        self.widget_aux_contrast = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_aux_contrast.setObjectName(u"widget_aux_contrast")

        self.gridLayout_4.addWidget(self.widget_aux_contrast, 0, 1, 1, 1)

        self.widget_aux_brightness = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_aux_brightness.setObjectName(u"widget_aux_brightness")

        self.gridLayout_4.addWidget(self.widget_aux_brightness, 1, 1, 1, 1)

        self.widget_aux_saturation = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_aux_saturation.setObjectName(u"widget_aux_saturation")

        self.gridLayout_4.addWidget(self.widget_aux_saturation, 2, 1, 1, 1)

        self.widget_aux_hue = SingleSliderWithSpinbox(CUE01_Input_Enhancement_Widget_Form)
        self.widget_aux_hue.setObjectName(u"widget_aux_hue")

        self.gridLayout_4.addWidget(self.widget_aux_hue, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(18)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.label_21 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_21)

        self.widget_aux_lti_switch_btn = SwitchBtn(CUE01_Input_Enhancement_Widget_Form)
        self.widget_aux_lti_switch_btn.setObjectName(u"widget_aux_lti_switch_btn")

        self.horizontalLayout_8.addWidget(self.widget_aux_lti_switch_btn)

        self.horizontalSpacer_11 = QSpacerItem(52, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.label_22 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_22)

        self.widget_aux_cti_switch_btn = SwitchBtn(CUE01_Input_Enhancement_Widget_Form)
        self.widget_aux_cti_switch_btn.setObjectName(u"widget_aux_cti_switch_btn")

        self.horizontalLayout_8.addWidget(self.widget_aux_cti_switch_btn)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_23 = QLabel(CUE01_Input_Enhancement_Widget_Form)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_23)

        self.horizontalSpacer_4 = QSpacerItem(14, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.comboBox_aux_color = CustomComboBox(CUE01_Input_Enhancement_Widget_Form)
        self.comboBox_aux_color.setObjectName(u"comboBox_aux_color")
        sizePolicy.setHeightForWidth(self.comboBox_aux_color.sizePolicy().hasHeightForWidth())
        self.comboBox_aux_color.setSizePolicy(sizePolicy)
        self.comboBox_aux_color.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_9.addWidget(self.comboBox_aux_color)

        self.horizontalSpacer_13 = QSpacerItem(70, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.aux_alias_frame = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.aux_alias_frame.setObjectName(u"aux_alias_frame")
        self.aux_alias_frame.setStyleSheet(u"#aux_alias_frame{\n"
"	border-image: url(:/icons/images/alias_background.png);\n"
"}")
        self.gridLayout_5 = QGridLayout(self.aux_alias_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(18)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 10, 10)
        self.label_24 = QLabel(self.aux_alias_frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_24, 0, 1, 1, 1)

        self.label_26 = QLabel(self.aux_alias_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_25 = QLabel(self.aux_alias_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_15, 0, 0, 1, 1)

        self.widget_aux_anti_hori = SingleSliderWithSpinbox(self.aux_alias_frame)
        self.widget_aux_anti_hori.setObjectName(u"widget_aux_anti_hori")

        self.gridLayout_5.addWidget(self.widget_aux_anti_hori, 1, 1, 1, 1)

        self.widget_aux_anti_verti = SingleSliderWithSpinbox(self.aux_alias_frame)
        self.widget_aux_anti_verti.setObjectName(u"widget_aux_anti_verti")

        self.gridLayout_5.addWidget(self.widget_aux_anti_verti, 2, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 4)

        self.verticalLayout_4.addWidget(self.aux_alias_frame)

        self.aux_filter_frame = QFrame(CUE01_Input_Enhancement_Widget_Form)
        self.aux_filter_frame.setObjectName(u"aux_filter_frame")
        self.aux_filter_frame.setStyleSheet(u"#aux_filter_frame{\n"
"	border-image: url(:/icons/images/alias_background.png);\n"
"}")
        self.gridLayout_6 = QGridLayout(self.aux_filter_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(18)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 7, 5)
        self.label_29 = QLabel(self.aux_filter_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_28 = QLabel(self.aux_filter_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_28, 1, 0, 1, 1)

        self.label_27 = QLabel(self.aux_filter_frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_27, 0, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_17, 0, 0, 1, 1)

        self.widget_aux_peak_hori = SingleSliderWithSpinbox(self.aux_filter_frame)
        self.widget_aux_peak_hori.setObjectName(u"widget_aux_peak_hori")

        self.gridLayout_6.addWidget(self.widget_aux_peak_hori, 1, 1, 1, 1)

        self.widget_aux_peak_verti = SingleSliderWithSpinbox(self.aux_filter_frame)
        self.widget_aux_peak_verti.setObjectName(u"widget_aux_peak_verti")

        self.gridLayout_6.addWidget(self.widget_aux_peak_verti, 2, 1, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 4)

        self.verticalLayout_4.addWidget(self.aux_filter_frame)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(2, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 5)
        self.verticalLayout_7.setStretch(2, 1)
        self.verticalLayout_7.setStretch(3, 5)
        self.verticalLayout_7.setStretch(4, 1)
        self.verticalLayout_7.setStretch(5, 5)

        self.horizontalLayout_13.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_35 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_35)


        self.retranslateUi(CUE01_Input_Enhancement_Widget_Form)

        QMetaObject.connectSlotsByName(CUE01_Input_Enhancement_Widget_Form)
    # setupUi

    def retranslateUi(self, CUE01_Input_Enhancement_Widget_Form):
        CUE01_Input_Enhancement_Widget_Form.setWindowTitle(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Foreground", None))
        self.label_5.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Brightness", None))
        self.label_4.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Contrast", None))
        self.label_6.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Saturation", None))
        self.label_7.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Hue", None))
        self.label_8.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"LTI", None))
        self.label_10.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"CTI", None))
        self.label_9.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Color Tone", None))
        self.label_11.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Horizontal", None))
        self.label_15.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Anti Alias", None))
        self.label_12.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Vertical", None))
        self.label_16.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Peak Filter", None))
        self.label_13.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Horizontal", None))
        self.label_14.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Vertical", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Background", None))
        self.label_31.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Brightness", None))
        self.label_32.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Saturation", None))
        self.label_30.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Contrast", None))
        self.label_33.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Hue", None))
        self.label_34.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"LTI", None))
        self.label_35.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"CTI", None))
        self.label_36.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Color Tone", None))
        self.label_38.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Horizontal", None))
        self.label_39.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Vertical", None))
        self.label_37.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Anti Alias", None))
        self.label_40.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Peak Filter", None))
        self.label_42.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Vertical", None))
        self.label_41.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Horizontal", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"AUX", None))
        self.label_17.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Contrast", None))
        self.label_20.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Hue", None))
        self.label_19.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Saturation", None))
        self.label_18.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Brightness", None))
        self.label_21.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"LTI", None))
        self.label_22.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"CTI", None))
        self.label_23.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Color Tone", None))
        self.label_24.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Anti Alias", None))
        self.label_26.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Vertical", None))
        self.label_25.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Horizontal", None))
        self.label_29.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Vertical", None))
        self.label_28.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Horizontal", None))
        self.label_27.setText(QCoreApplication.translate("CUE01_Input_Enhancement_Widget_Form", u"Peak Filter", None))
    # retranslateUi


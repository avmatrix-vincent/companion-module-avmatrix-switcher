# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uskWidget.ui'
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
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from src.components.SingleSliderWithDoubleSpinbox import SingleSliderWithDoubleSpinbox
from src.components.SwitchButton import SwitchBtn

class Ui_CUE01_USK_Widget_Form(object):
    def setupUi(self, CUE01_USK_Widget_Form):
        if not CUE01_USK_Widget_Form.objectName():
            CUE01_USK_Widget_Form.setObjectName(u"CUE01_USK_Widget_Form")
        CUE01_USK_Widget_Form.resize(800, 500)
        self.horizontalLayout_9 = QHBoxLayout(CUE01_USK_Widget_Form)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_13 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line = QFrame(CUE01_USK_Widget_Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(CUE01_USK_Widget_Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.line_2 = QFrame(CUE01_USK_Widget_Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(CUE01_USK_Widget_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.widget_pip_switchbtn = SwitchBtn(CUE01_USK_Widget_Form)
        self.widget_pip_switchbtn.setObjectName(u"widget_pip_switchbtn")

        self.horizontalLayout_3.addWidget(self.widget_pip_switchbtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(18)
        self.gridLayout_3.setVerticalSpacing(0)
        self.widget_pip_hori = SingleSliderWithDoubleSpinbox(CUE01_USK_Widget_Form)
        self.widget_pip_hori.setObjectName(u"widget_pip_hori")

        self.gridLayout_3.addWidget(self.widget_pip_hori, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.label_9 = QLabel(CUE01_USK_Widget_Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setMaximumSize(QSize(100, 16777215))
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_8 = QLabel(CUE01_USK_Widget_Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setMaximumSize(QSize(100, 16777215))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.widget_pip_width = SingleSliderWithDoubleSpinbox(CUE01_USK_Widget_Form)
        self.widget_pip_width.setObjectName(u"widget_pip_width")

        self.gridLayout_3.addWidget(self.widget_pip_width, 0, 4, 1, 1)

        self.widget_pip_height = SingleSliderWithDoubleSpinbox(CUE01_USK_Widget_Form)
        self.widget_pip_height.setObjectName(u"widget_pip_height")

        self.gridLayout_3.addWidget(self.widget_pip_height, 1, 4, 1, 1)

        self.widget_pip_verti = SingleSliderWithDoubleSpinbox(CUE01_USK_Widget_Form)
        self.widget_pip_verti.setObjectName(u"widget_pip_verti")

        self.gridLayout_3.addWidget(self.widget_pip_verti, 1, 1, 1, 1)

        self.label_10 = QLabel(CUE01_USK_Widget_Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(60, 0))
        self.label_10.setMaximumSize(QSize(60, 16777215))
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 0, 3, 1, 1)

        self.label_11 = QLabel(CUE01_USK_Widget_Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(60, 0))
        self.label_11.setMaximumSize(QSize(60, 16777215))
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_11, 1, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_3 = QFrame(CUE01_USK_Widget_Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.label_2 = QLabel(CUE01_USK_Widget_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_4 = QFrame(CUE01_USK_Widget_Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(CUE01_USK_Widget_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.widget_mask_switchbtn = SwitchBtn(CUE01_USK_Widget_Form)
        self.widget_mask_switchbtn.setObjectName(u"widget_mask_switchbtn")

        self.horizontalLayout_4.addWidget(self.widget_mask_switchbtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(18)
        self.gridLayout_4.setVerticalSpacing(0)
        self.label_12 = QLabel(CUE01_USK_Widget_Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 0))
        self.label_12.setMaximumSize(QSize(100, 16777215))
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.widget_mask_bottom = SingleSliderWithDoubleSpinbox(CUE01_USK_Widget_Form)
        self.widget_mask_bottom.setObjectName(u"widget_mask_bottom")

        self.gridLayout_4.addWidget(self.widget_mask_bottom, 0, 4, 1, 1)

        self.label_13 = QLabel(CUE01_USK_Widget_Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 0))
        self.label_13.setMaximumSize(QSize(100, 16777215))
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 1, 2, 1, 1)

        self.widget_mask_left = SingleSliderWithDoubleSpinbox(CUE01_USK_Widget_Form)
        self.widget_mask_left.setObjectName(u"widget_mask_left")

        self.gridLayout_4.addWidget(self.widget_mask_left, 1, 1, 1, 1)

        self.widget_mask_top = SingleSliderWithDoubleSpinbox(CUE01_USK_Widget_Form)
        self.widget_mask_top.setObjectName(u"widget_mask_top")

        self.gridLayout_4.addWidget(self.widget_mask_top, 0, 1, 1, 1)

        self.widget_mask_right = SingleSliderWithDoubleSpinbox(CUE01_USK_Widget_Form)
        self.widget_mask_right.setObjectName(u"widget_mask_right")

        self.gridLayout_4.addWidget(self.widget_mask_right, 1, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)

        self.label_14 = QLabel(CUE01_USK_Widget_Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(60, 0))
        self.label_14.setMaximumSize(QSize(60, 16777215))
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_14, 0, 3, 1, 1)

        self.label_15 = QLabel(CUE01_USK_Widget_Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(60, 0))
        self.label_15.setMaximumSize(QSize(60, 16777215))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_15, 1, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line_5 = QFrame(CUE01_USK_Widget_Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_5)

        self.label_5 = QLabel(CUE01_USK_Widget_Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.line_6 = QFrame(CUE01_USK_Widget_Form)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.radio_main_widget = QWidget(CUE01_USK_Widget_Form)
        self.radio_main_widget.setObjectName(u"radio_main_widget")
        self.radio_main_widget.setMinimumSize(QSize(0, 220))
        self.horizontalLayout_8 = QHBoxLayout(self.radio_main_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.radio_main_widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(52, 0))
        self.label_6.setMaximumSize(QSize(52, 16777215))

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.widget_radios_goup_1 = QWidget(self.radio_main_widget)
        self.widget_radios_goup_1.setObjectName(u"widget_radios_goup_1")
        self.gridLayout = QGridLayout(self.widget_radios_goup_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(36)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(-1, 5, -1, 5)
        self.radioButton_stage_1_off = QRadioButton(self.widget_radios_goup_1)
        self.radioButton_stage_1_off.setObjectName(u"radioButton_stage_1_off")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radioButton_stage_1_off.sizePolicy().hasHeightForWidth())
        self.radioButton_stage_1_off.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.radioButton_stage_1_off, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(92, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(92, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.radioButton_stage_1_erode_3 = QRadioButton(self.widget_radios_goup_1)
        self.radioButton_stage_1_erode_3.setObjectName(u"radioButton_stage_1_erode_3")
        sizePolicy1.setHeightForWidth(self.radioButton_stage_1_erode_3.sizePolicy().hasHeightForWidth())
        self.radioButton_stage_1_erode_3.setSizePolicy(sizePolicy1)
        self.radioButton_stage_1_erode_3.setMinimumSize(QSize(100, 0))
        self.radioButton_stage_1_erode_3.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_stage_1_erode_3, 1, 0, 1, 1)

        self.radioButton_stage1_gaussian3 = QRadioButton(self.widget_radios_goup_1)
        self.radioButton_stage1_gaussian3.setObjectName(u"radioButton_stage1_gaussian3")
        sizePolicy1.setHeightForWidth(self.radioButton_stage1_gaussian3.sizePolicy().hasHeightForWidth())
        self.radioButton_stage1_gaussian3.setSizePolicy(sizePolicy1)
        self.radioButton_stage1_gaussian3.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.radioButton_stage1_gaussian3, 1, 2, 1, 1)

        self.radioButton_stage_1_erode_5 = QRadioButton(self.widget_radios_goup_1)
        self.radioButton_stage_1_erode_5.setObjectName(u"radioButton_stage_1_erode_5")
        sizePolicy1.setHeightForWidth(self.radioButton_stage_1_erode_5.sizePolicy().hasHeightForWidth())
        self.radioButton_stage_1_erode_5.setSizePolicy(sizePolicy1)
        self.radioButton_stage_1_erode_5.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.radioButton_stage_1_erode_5, 2, 0, 1, 1)

        self.radioButton_stage_1_dilate_5 = QRadioButton(self.widget_radios_goup_1)
        self.radioButton_stage_1_dilate_5.setObjectName(u"radioButton_stage_1_dilate_5")
        sizePolicy1.setHeightForWidth(self.radioButton_stage_1_dilate_5.sizePolicy().hasHeightForWidth())
        self.radioButton_stage_1_dilate_5.setSizePolicy(sizePolicy1)
        self.radioButton_stage_1_dilate_5.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.radioButton_stage_1_dilate_5, 2, 1, 1, 1)

        self.radioButton_stage1_gaussian5 = QRadioButton(self.widget_radios_goup_1)
        self.radioButton_stage1_gaussian5.setObjectName(u"radioButton_stage1_gaussian5")
        sizePolicy1.setHeightForWidth(self.radioButton_stage1_gaussian5.sizePolicy().hasHeightForWidth())
        self.radioButton_stage1_gaussian5.setSizePolicy(sizePolicy1)
        self.radioButton_stage1_gaussian5.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.radioButton_stage1_gaussian5, 2, 2, 1, 1)

        self.radioButton_stage_1_dilate_3 = QRadioButton(self.widget_radios_goup_1)
        self.radioButton_stage_1_dilate_3.setObjectName(u"radioButton_stage_1_dilate_3")
        sizePolicy1.setHeightForWidth(self.radioButton_stage_1_dilate_3.sizePolicy().hasHeightForWidth())
        self.radioButton_stage_1_dilate_3.setSizePolicy(sizePolicy1)
        self.radioButton_stage_1_dilate_3.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.radioButton_stage_1_dilate_3, 1, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.widget_radios_goup_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.radio_main_widget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(52, 0))
        self.label_7.setMaximumSize(QSize(52, 16777215))

        self.verticalLayout_2.addWidget(self.label_7)

        self.verticalSpacer_2 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.widget_radios_group_2 = QWidget(self.radio_main_widget)
        self.widget_radios_group_2.setObjectName(u"widget_radios_group_2")
        self.gridLayout_2 = QGridLayout(self.widget_radios_group_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(36)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.radioButton_stage_2_off = QRadioButton(self.widget_radios_group_2)
        self.radioButton_stage_2_off.setObjectName(u"radioButton_stage_2_off")
        sizePolicy1.setHeightForWidth(self.radioButton_stage_2_off.sizePolicy().hasHeightForWidth())
        self.radioButton_stage_2_off.setSizePolicy(sizePolicy1)
        self.radioButton_stage_2_off.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_stage_2_off, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(92, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(92, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.radioButton_stage2_erode3 = QRadioButton(self.widget_radios_group_2)
        self.radioButton_stage2_erode3.setObjectName(u"radioButton_stage2_erode3")
        sizePolicy1.setHeightForWidth(self.radioButton_stage2_erode3.sizePolicy().hasHeightForWidth())
        self.radioButton_stage2_erode3.setSizePolicy(sizePolicy1)
        self.radioButton_stage2_erode3.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.radioButton_stage2_erode3, 1, 0, 1, 1)

        self.radioButton_stage2_dilate3 = QRadioButton(self.widget_radios_group_2)
        self.radioButton_stage2_dilate3.setObjectName(u"radioButton_stage2_dilate3")
        sizePolicy1.setHeightForWidth(self.radioButton_stage2_dilate3.sizePolicy().hasHeightForWidth())
        self.radioButton_stage2_dilate3.setSizePolicy(sizePolicy1)
        self.radioButton_stage2_dilate3.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.radioButton_stage2_dilate3, 1, 1, 1, 1)

        self.radioButton_stage2_gaussian3 = QRadioButton(self.widget_radios_group_2)
        self.radioButton_stage2_gaussian3.setObjectName(u"radioButton_stage2_gaussian3")
        sizePolicy1.setHeightForWidth(self.radioButton_stage2_gaussian3.sizePolicy().hasHeightForWidth())
        self.radioButton_stage2_gaussian3.setSizePolicy(sizePolicy1)
        self.radioButton_stage2_gaussian3.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.radioButton_stage2_gaussian3, 1, 2, 1, 1)

        self.radioButton_stage2_erode5 = QRadioButton(self.widget_radios_group_2)
        self.radioButton_stage2_erode5.setObjectName(u"radioButton_stage2_erode5")
        sizePolicy1.setHeightForWidth(self.radioButton_stage2_erode5.sizePolicy().hasHeightForWidth())
        self.radioButton_stage2_erode5.setSizePolicy(sizePolicy1)
        self.radioButton_stage2_erode5.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.radioButton_stage2_erode5, 2, 0, 1, 1)

        self.radioButton_stage2_dilate5 = QRadioButton(self.widget_radios_group_2)
        self.radioButton_stage2_dilate5.setObjectName(u"radioButton_stage2_dilate5")
        sizePolicy1.setHeightForWidth(self.radioButton_stage2_dilate5.sizePolicy().hasHeightForWidth())
        self.radioButton_stage2_dilate5.setSizePolicy(sizePolicy1)
        self.radioButton_stage2_dilate5.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.radioButton_stage2_dilate5, 2, 1, 1, 1)

        self.radioButton_stage2_gaussian5 = QRadioButton(self.widget_radios_group_2)
        self.radioButton_stage2_gaussian5.setObjectName(u"radioButton_stage2_gaussian5")
        sizePolicy1.setHeightForWidth(self.radioButton_stage2_gaussian5.sizePolicy().hasHeightForWidth())
        self.radioButton_stage2_gaussian5.setSizePolicy(sizePolicy1)
        self.radioButton_stage2_gaussian5.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.radioButton_stage2_gaussian5, 2, 2, 1, 1)


        self.horizontalLayout_7.addWidget(self.widget_radios_group_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_12 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_4.addWidget(self.radio_main_widget)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_14 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)


        self.retranslateUi(CUE01_USK_Widget_Form)

        QMetaObject.connectSlotsByName(CUE01_USK_Widget_Form)
    # setupUi

    def retranslateUi(self, CUE01_USK_Widget_Form):
        CUE01_USK_Widget_Form.setWindowTitle(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"USK PIP", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"PIP ON/OFF", None))
        self.label_9.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Vertical", None))
        self.label_8.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Horizontal", None))
        self.label_10.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Width", None))
        self.label_11.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Height", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"USK Mask", None))
        self.label_4.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"ON/OFF", None))
        self.label_12.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Top", None))
        self.label_13.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Left", None))
        self.label_14.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Bottom", None))
        self.label_15.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Right", None))
        self.label_5.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"USK Edge", None))
        self.label_6.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Stage 1", None))
        self.radioButton_stage_1_off.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"OFF", None))
        self.radioButton_stage_1_erode_3.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Erode 3x3", None))
        self.radioButton_stage1_gaussian3.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Gaussian 3x3", None))
        self.radioButton_stage_1_erode_5.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Erode 5x5", None))
        self.radioButton_stage_1_dilate_5.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Dilate 5x5", None))
        self.radioButton_stage1_gaussian5.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Gaussian 5x5", None))
        self.radioButton_stage_1_dilate_3.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Dilate 3x3", None))
        self.label_7.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Stage 2", None))
        self.radioButton_stage_2_off.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"OFF", None))
        self.radioButton_stage2_erode3.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Erode 3x3", None))
        self.radioButton_stage2_dilate3.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Dilate 3x3", None))
        self.radioButton_stage2_gaussian3.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Gaussian 3x3", None))
        self.radioButton_stage2_erode5.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Erode 5x5", None))
        self.radioButton_stage2_dilate5.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Dilate 5x5", None))
        self.radioButton_stage2_gaussian5.setText(QCoreApplication.translate("CUE01_USK_Widget_Form", u"Gaussian 5x5", None))
    # retranslateUi


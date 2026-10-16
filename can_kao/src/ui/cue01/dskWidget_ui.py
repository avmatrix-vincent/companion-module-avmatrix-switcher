# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dskWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from src.components.CustomComboBox import CustomComboBox
from src.components.CustomSpinBox import CustomDoubleSpinBox
from src.components.SingleSliderWithDoubleSpinbox import SingleSliderWithDoubleSpinbox
from src.components.SwitchButton import SwitchBtn
from superqt import QRangeSlider
import images_rc

class Ui_CUE01_DSK_Widget_Form(object):
    def setupUi(self, CUE01_DSK_Widget_Form):
        if not CUE01_DSK_Widget_Form.objectName():
            CUE01_DSK_Widget_Form.setObjectName(u"CUE01_DSK_Widget_Form")
        CUE01_DSK_Widget_Form.resize(800, 500)
        self.verticalLayout_6 = QVBoxLayout(CUE01_DSK_Widget_Form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_fill_source = QGroupBox(CUE01_DSK_Widget_Form)
        self.groupBox_fill_source.setObjectName(u"groupBox_fill_source")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_fill_source.sizePolicy().hasHeightForWidth())
        self.groupBox_fill_source.setSizePolicy(sizePolicy)
        self.groupBox_fill_source.setStyleSheet(u"#groupBox_fill_source\n"
"{\n"
"	border-image: url(:/icons/images/groupbox_background.png);\n"
"}")
        self.groupBox_fill_source.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_fill_source)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 15, -1, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_11 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)

        self.label = QLabel(self.groupBox_fill_source)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(80, 16777215))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_video_source = CustomComboBox(self.groupBox_fill_source)
        self.comboBox_video_source.setObjectName(u"comboBox_video_source")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_video_source.sizePolicy().hasHeightForWidth())
        self.comboBox_video_source.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.comboBox_video_source)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.groupBox_fill_source)

        self.groupBox_dsk_tolerance = QGroupBox(CUE01_DSK_Widget_Form)
        self.groupBox_dsk_tolerance.setObjectName(u"groupBox_dsk_tolerance")
        self.groupBox_dsk_tolerance.setMaximumSize(QSize(16777215, 180))
        self.groupBox_dsk_tolerance.setStyleSheet(u"#groupBox_dsk_tolerance{\n"
"	\n"
"	border-image: url(:/icons/images/group_back_dsk_tolerance.png);\n"
"}")
        self.groupBox_dsk_tolerance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox_dsk_tolerance)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_dsk_tolerance)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(70, 0))
        self.label_2.setMaximumSize(QSize(70, 16777215))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.widget_invert_switchBtn = SwitchBtn(self.groupBox_dsk_tolerance)
        self.widget_invert_switchBtn.setObjectName(u"widget_invert_switchBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_invert_switchBtn.sizePolicy().hasHeightForWidth())
        self.widget_invert_switchBtn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.widget_invert_switchBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox_dsk_tolerance)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMinimumSize(QSize(60, 0))
        self.label_3.setMaximumSize(QSize(60, 16777215))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.spinBox_tolerance__min = CustomDoubleSpinBox(self.groupBox_dsk_tolerance)
        self.spinBox_tolerance__min.setObjectName(u"spinBox_tolerance__min")

        self.horizontalLayout_4.addWidget(self.spinBox_tolerance__min)

        self.rangeSlider_tolerance = QRangeSlider(self.groupBox_dsk_tolerance)
        self.rangeSlider_tolerance.setObjectName(u"rangeSlider_tolerance")
        self.rangeSlider_tolerance.setMaximumSize(QSize(150, 16777215))
        self.rangeSlider_tolerance.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.rangeSlider_tolerance)

        self.spinBox_tolerance_max = CustomDoubleSpinBox(self.groupBox_dsk_tolerance)
        self.spinBox_tolerance_max.setObjectName(u"spinBox_tolerance_max")

        self.horizontalLayout_4.addWidget(self.spinBox_tolerance_max)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.groupBox_dsk_tolerance)


        self.horizontalLayout_22.addLayout(self.verticalLayout_5)

        self.groupBox_dsk_clip = QGroupBox(CUE01_DSK_Widget_Form)
        self.groupBox_dsk_clip.setObjectName(u"groupBox_dsk_clip")
        self.groupBox_dsk_clip.setStyleSheet(u"#groupBox_dsk_clip{\n"
"	border-image: url(:/icons/images/group_back_dsk_clip.png);\n"
"}")
        self.groupBox_dsk_clip.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_dsk_clip)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.groupBox_dsk_clip)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(85, 0))
        self.label_5.setMaximumSize(QSize(85, 16777215))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.widget_clip_switchBtn = SwitchBtn(self.groupBox_dsk_clip)
        self.widget_clip_switchBtn.setObjectName(u"widget_clip_switchBtn")

        self.horizontalLayout_9.addWidget(self.widget_clip_switchBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.groupBox_dsk_clip)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setMinimumSize(QSize(85, 0))
        self.label_6.setMaximumSize(QSize(85, 16777215))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.widget_curve_switchBtn = SwitchBtn(self.groupBox_dsk_clip)
        self.widget_curve_switchBtn.setObjectName(u"widget_curve_switchBtn")

        self.horizontalLayout_10.addWidget(self.widget_curve_switchBtn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.groupBox_dsk_clip)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(85, 0))
        self.label_8.setMaximumSize(QSize(85, 16777215))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.horizontalSpacer_8 = QSpacerItem(12, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.spinBox_clip__min = CustomDoubleSpinBox(self.groupBox_dsk_clip)
        self.spinBox_clip__min.setObjectName(u"spinBox_clip__min")

        self.horizontalLayout_6.addWidget(self.spinBox_clip__min)

        self.rangeSlider_clip = QRangeSlider(self.groupBox_dsk_clip)
        self.rangeSlider_clip.setObjectName(u"rangeSlider_clip")
        self.rangeSlider_clip.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.rangeSlider_clip)

        self.spinBox_clip_max = CustomDoubleSpinBox(self.groupBox_dsk_clip)
        self.spinBox_clip_max.setObjectName(u"spinBox_clip_max")

        self.horizontalLayout_6.addWidget(self.spinBox_clip_max)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(18)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_dsk_clip)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(85, 0))
        self.label_7.setMaximumSize(QSize(85, 16777215))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.widget_pgm_level = SingleSliderWithDoubleSpinbox(self.groupBox_dsk_clip)
        self.widget_pgm_level.setObjectName(u"widget_pgm_level")

        self.horizontalLayout_7.addWidget(self.widget_pgm_level)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.horizontalLayout_22.addWidget(self.groupBox_dsk_clip)


        self.verticalLayout_6.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.groupBox_dsk_pip = QGroupBox(CUE01_DSK_Widget_Form)
        self.groupBox_dsk_pip.setObjectName(u"groupBox_dsk_pip")
        self.groupBox_dsk_pip.setStyleSheet(u"#groupBox_dsk_pip{\n"
"	\n"
"	border-image: url(:/icons/images/group_back_dsk_pip.png);\n"
"}")
        self.groupBox_dsk_pip.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_dsk_pip)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.groupBox_dsk_pip)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setMinimumSize(QSize(70, 0))
        self.label_10.setMaximumSize(QSize(70, 16777215))
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.widget_pip_switchBtn = SwitchBtn(self.groupBox_dsk_pip)
        self.widget_pip_switchBtn.setObjectName(u"widget_pip_switchBtn")

        self.horizontalLayout_11.addWidget(self.widget_pip_switchBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(18)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.groupBox_dsk_pip)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setMinimumSize(QSize(70, 0))
        self.label_11.setMaximumSize(QSize(70, 16777215))
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.widget_pip_horizontal = SingleSliderWithDoubleSpinbox(self.groupBox_dsk_pip)
        self.widget_pip_horizontal.setObjectName(u"widget_pip_horizontal")

        self.horizontalLayout_12.addWidget(self.widget_pip_horizontal)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.groupBox_dsk_pip)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setMinimumSize(QSize(70, 0))
        self.label_12.setMaximumSize(QSize(70, 16777215))
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.widget_pip_vertical = SingleSliderWithDoubleSpinbox(self.groupBox_dsk_pip)
        self.widget_pip_vertical.setObjectName(u"widget_pip_vertical")

        self.horizontalLayout_13.addWidget(self.widget_pip_vertical)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.groupBox_dsk_pip)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)
        self.label_13.setMinimumSize(QSize(70, 0))
        self.label_13.setMaximumSize(QSize(70, 16777215))
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_13)

        self.widget_pip_width = SingleSliderWithDoubleSpinbox(self.groupBox_dsk_pip)
        self.widget_pip_width.setObjectName(u"widget_pip_width")

        self.horizontalLayout_14.addWidget(self.widget_pip_width)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(self.groupBox_dsk_pip)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setMinimumSize(QSize(70, 0))
        self.label_14.setMaximumSize(QSize(70, 16777215))
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_14)

        self.widget_pip_height = SingleSliderWithDoubleSpinbox(self.groupBox_dsk_pip)
        self.widget_pip_height.setObjectName(u"widget_pip_height")

        self.horizontalLayout_15.addWidget(self.widget_pip_height)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)


        self.horizontalLayout_21.addWidget(self.groupBox_dsk_pip)

        self.groupBox_dsk_mask = QGroupBox(CUE01_DSK_Widget_Form)
        self.groupBox_dsk_mask.setObjectName(u"groupBox_dsk_mask")
        self.groupBox_dsk_mask.setStyleSheet(u"#groupBox_dsk_mask{\n"
"	border-image: url(:/icons/images/group_back_dsk_mask.png);\n"
"}")
        self.groupBox_dsk_mask.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_dsk_mask)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(self.groupBox_dsk_mask)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setMinimumSize(QSize(85, 0))
        self.label_15.setMaximumSize(QSize(85, 16777215))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_15)

        self.widget_mask_switchBtn = SwitchBtn(self.groupBox_dsk_mask)
        self.widget_mask_switchBtn.setObjectName(u"widget_mask_switchBtn")

        self.horizontalLayout_16.addWidget(self.widget_mask_switchBtn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_16 = QLabel(self.groupBox_dsk_mask)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setMinimumSize(QSize(85, 0))
        self.label_16.setMaximumSize(QSize(85, 16777215))
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_16)

        self.widget_mask_top = SingleSliderWithDoubleSpinbox(self.groupBox_dsk_mask)
        self.widget_mask_top.setObjectName(u"widget_mask_top")

        self.horizontalLayout_17.addWidget(self.widget_mask_top)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(18)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_17 = QLabel(self.groupBox_dsk_mask)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setMinimumSize(QSize(85, 0))
        self.label_17.setMaximumSize(QSize(85, 16777215))
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_17)

        self.widget_mask_bottom = SingleSliderWithDoubleSpinbox(self.groupBox_dsk_mask)
        self.widget_mask_bottom.setObjectName(u"widget_mask_bottom")

        self.horizontalLayout_18.addWidget(self.widget_mask_bottom)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_18 = QLabel(self.groupBox_dsk_mask)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setMinimumSize(QSize(85, 0))
        self.label_18.setMaximumSize(QSize(85, 16777215))
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_18)

        self.widget_mask_left = SingleSliderWithDoubleSpinbox(self.groupBox_dsk_mask)
        self.widget_mask_left.setObjectName(u"widget_mask_left")

        self.horizontalLayout_19.addWidget(self.widget_mask_left)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(18)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_19 = QLabel(self.groupBox_dsk_mask)
        self.label_19.setObjectName(u"label_19")
        sizePolicy4.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy4)
        self.label_19.setMinimumSize(QSize(85, 0))
        self.label_19.setMaximumSize(QSize(85, 16777215))
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_19)

        self.widget_mask_right = SingleSliderWithDoubleSpinbox(self.groupBox_dsk_mask)
        self.widget_mask_right.setObjectName(u"widget_mask_right")

        self.horizontalLayout_20.addWidget(self.widget_mask_right)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_21.addWidget(self.groupBox_dsk_mask)


        self.verticalLayout_6.addLayout(self.horizontalLayout_21)


        self.retranslateUi(CUE01_DSK_Widget_Form)

        QMetaObject.connectSlotsByName(CUE01_DSK_Widget_Form)
    # setupUi

    def retranslateUi(self, CUE01_DSK_Widget_Form):
        CUE01_DSK_Widget_Form.setWindowTitle(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Form", None))
        self.groupBox_fill_source.setTitle(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Fill Source", None))
        self.label.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Video Source", None))
        self.groupBox_dsk_tolerance.setTitle(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"DSK Tolerance", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Invert", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Tolerance", None))
        self.groupBox_dsk_clip.setTitle(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"DSK Clip", None))
        self.label_5.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Clip ON/OFF", None))
        self.label_6.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Curve ON/OFF", None))
        self.label_8.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Clip", None))
        self.label_7.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"PGM Level", None))
        self.groupBox_dsk_pip.setTitle(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"DSK PIP", None))
        self.label_10.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"PIP ON/OFF", None))
        self.label_11.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Horizontal", None))
        self.label_12.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Vertical", None))
        self.label_13.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Width", None))
        self.label_14.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Height", None))
        self.groupBox_dsk_mask.setTitle(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"DSK Mask", None))
        self.label_15.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Mask ON/OFF", None))
        self.label_16.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Top", None))
        self.label_17.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Bottom", None))
        self.label_18.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Left", None))
        self.label_19.setText(QCoreApplication.translate("CUE01_DSK_Widget_Form", u"Right", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sc7030_setting.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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

class Ui_SC7030_Setting_Form(object):
    def setupUi(self, SC7030_Setting_Form):
        if not SC7030_Setting_Form.objectName():
            SC7030_Setting_Form.setObjectName(u"SC7030_Setting_Form")
        SC7030_Setting_Form.resize(800, 500)
        self.verticalLayout = QVBoxLayout(SC7030_Setting_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.comboBox_output_resolution = CustomComboBox(SC7030_Setting_Form)
        self.comboBox_output_resolution.setObjectName(u"comboBox_output_resolution")
        self.comboBox_output_resolution.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_10.addWidget(self.comboBox_output_resolution)

        self.horizontalSpacer_10 = QSpacerItem(198, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.comboBox_video_input_mode = CustomComboBox(SC7030_Setting_Form)
        self.comboBox_video_input_mode.setObjectName(u"comboBox_video_input_mode")
        self.comboBox_video_input_mode.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_8.addWidget(self.comboBox_video_input_mode)

        self.horizontalSpacer_8 = QSpacerItem(198, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, -1, -1, -1)
        self.comboBox_out_radio = CustomComboBox(SC7030_Setting_Form)
        self.comboBox_out_radio.setObjectName(u"comboBox_out_radio")
        self.comboBox_out_radio.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_12.addWidget(self.comboBox_out_radio)

        self.horizontalSpacer_22 = QSpacerItem(198, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_22)


        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 1, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, -1, -1, -1)
        self.comboBox_audio_input = CustomComboBox(SC7030_Setting_Form)
        self.comboBox_audio_input.setObjectName(u"comboBox_audio_input")
        self.comboBox_audio_input.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_14.addWidget(self.comboBox_audio_input)

        self.horizontalSpacer_15 = QSpacerItem(198, 28, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)


        self.gridLayout.addLayout(self.horizontalLayout_14, 3, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_26 = QSpacerItem(198, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_26)

        self.label_3 = QLabel(SC7030_Setting_Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(130, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_13, 3, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_24 = QSpacerItem(198, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_24)

        self.label = QLabel(SC7030_Setting_Form)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(130, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_23 = QSpacerItem(198, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_23)

        self.label_2 = QLabel(SC7030_Setting_Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setMaximumSize(QSize(130, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(20, -1, -1, -1)
        self.comboBox_hdmi_out_range = CustomComboBox(SC7030_Setting_Form)
        self.comboBox_hdmi_out_range.setObjectName(u"comboBox_hdmi_out_range")
        self.comboBox_hdmi_out_range.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_16.addWidget(self.comboBox_hdmi_out_range)

        self.horizontalSpacer_17 = QSpacerItem(198, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_17)


        self.gridLayout.addLayout(self.horizontalLayout_16, 4, 1, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_28 = QSpacerItem(198, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_28)

        self.label_5 = QLabel(SC7030_Setting_Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(150, 0))
        self.label_5.setMaximumSize(QSize(130, 16777215))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_5)


        self.gridLayout.addLayout(self.horizontalLayout_15, 4, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_27 = QSpacerItem(198, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_27)

        self.label_6 = QLabel(SC7030_Setting_Form)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(150, 0))
        self.label_6.setMaximumSize(QSize(130, 16777215))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_6)


        self.gridLayout.addLayout(self.horizontalLayout_17, 5, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(20, -1, -1, -1)
        self.comboBox_3g_level = CustomComboBox(SC7030_Setting_Form)
        self.comboBox_3g_level.setObjectName(u"comboBox_3g_level")
        self.comboBox_3g_level.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_18.addWidget(self.comboBox_3g_level)

        self.horizontalSpacer_18 = QSpacerItem(198, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)


        self.gridLayout.addLayout(self.horizontalLayout_18, 5, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_25 = QSpacerItem(198, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_25)

        self.label_8 = QLabel(SC7030_Setting_Form)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(150, 0))
        self.label_8.setMaximumSize(QSize(130, 16777215))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_8)


        self.gridLayout.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(SC7030_Setting_Form)

        QMetaObject.connectSlotsByName(SC7030_Setting_Form)
    # setupUi

    def retranslateUi(self, SC7030_Setting_Form):
        SC7030_Setting_Form.setWindowTitle(QCoreApplication.translate("SC7030_Setting_Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("SC7030_Setting_Form", u"Audio Input:", None))
        self.label.setText(QCoreApplication.translate("SC7030_Setting_Form", u"SDI/HDMI Output:", None))
        self.label_2.setText(QCoreApplication.translate("SC7030_Setting_Form", u"Video Input:", None))
        self.label_5.setText(QCoreApplication.translate("SC7030_Setting_Form", u"HDMI Out Range:", None))
        self.label_6.setText(QCoreApplication.translate("SC7030_Setting_Form", u"3G-SDI Output:", None))
        self.label_8.setText(QCoreApplication.translate("SC7030_Setting_Form", u"Aspect Ratio:", None))
    # retranslateUi


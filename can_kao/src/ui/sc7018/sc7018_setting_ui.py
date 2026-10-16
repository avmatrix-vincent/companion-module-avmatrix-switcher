# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sc7018_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from src.components.CustomComboBox import CustomComboBox

class Ui_SC7018_Settomg_Form(object):
    def setupUi(self, SC7018_Settomg_Form):
        if not SC7018_Settomg_Form.objectName():
            SC7018_Settomg_Form.setObjectName(u"SC7018_Settomg_Form")
        SC7018_Settomg_Form.resize(800, 500)
        self.horizontalLayout_2 = QHBoxLayout(SC7018_Settomg_Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(18)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(SC7018_Settomg_Form)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(120, 0))
        self.label_9.setMaximumSize(QSize(120, 16777215))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.label_manufacturer = QLabel(SC7018_Settomg_Form)
        self.label_manufacturer.setObjectName(u"label_manufacturer")
        sizePolicy.setHeightForWidth(self.label_manufacturer.sizePolicy().hasHeightForWidth())
        self.label_manufacturer.setSizePolicy(sizePolicy)
        self.label_manufacturer.setMinimumSize(QSize(75, 0))
        self.label_manufacturer.setMaximumSize(QSize(75, 16777215))
        self.label_manufacturer.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.label_manufacturer)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_10 = QLabel(SC7018_Settomg_Form)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(120, 0))
        self.label_10.setMaximumSize(QSize(125, 16777215))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label_sn = QLabel(SC7018_Settomg_Form)
        self.label_sn.setObjectName(u"label_sn")
        self.label_sn.setMinimumSize(QSize(100, 0))
        self.label_sn.setMaximumSize(QSize(100, 16777215))
        self.label_sn.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.label_sn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(18)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(SC7018_Settomg_Form)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(120, 0))
        self.label_7.setMaximumSize(QSize(120, 16777215))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.label_mcu_mode = QLabel(SC7018_Settomg_Form)
        self.label_mcu_mode.setObjectName(u"label_mcu_mode")
        sizePolicy.setHeightForWidth(self.label_mcu_mode.sizePolicy().hasHeightForWidth())
        self.label_mcu_mode.setSizePolicy(sizePolicy)
        self.label_mcu_mode.setMinimumSize(QSize(75, 0))
        self.label_mcu_mode.setMaximumSize(QSize(75, 16777215))
        self.label_mcu_mode.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.label_mcu_mode)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_8 = QLabel(SC7018_Settomg_Form)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(120, 0))
        self.label_8.setMaximumSize(QSize(125, 16777215))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.label_protocol_ver = QLabel(SC7018_Settomg_Form)
        self.label_protocol_ver.setObjectName(u"label_protocol_ver")
        sizePolicy.setHeightForWidth(self.label_protocol_ver.sizePolicy().hasHeightForWidth())
        self.label_protocol_ver.setSizePolicy(sizePolicy)
        self.label_protocol_ver.setMinimumSize(QSize(100, 0))
        self.label_protocol_ver.setMaximumSize(QSize(100, 16777215))
        self.label_protocol_ver.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.label_protocol_ver)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(SC7018_Settomg_Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setMaximumSize(QSize(120, 16777215))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.label_boot_version = QLabel(SC7018_Settomg_Form)
        self.label_boot_version.setObjectName(u"label_boot_version")
        sizePolicy.setHeightForWidth(self.label_boot_version.sizePolicy().hasHeightForWidth())
        self.label_boot_version.setSizePolicy(sizePolicy)
        self.label_boot_version.setMinimumSize(QSize(75, 0))
        self.label_boot_version.setMaximumSize(QSize(75, 16777215))
        self.label_boot_version.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_5.addWidget(self.label_boot_version)

        self.horizontalSpacer_5 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_6 = QLabel(SC7018_Settomg_Form)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(120, 0))
        self.label_6.setMaximumSize(QSize(125, 16777215))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.label_app_version = QLabel(SC7018_Settomg_Form)
        self.label_app_version.setObjectName(u"label_app_version")
        sizePolicy.setHeightForWidth(self.label_app_version.sizePolicy().hasHeightForWidth())
        self.label_app_version.setSizePolicy(sizePolicy)
        self.label_app_version.setMinimumSize(QSize(100, 0))
        self.label_app_version.setMaximumSize(QSize(100, 16777215))
        self.label_app_version.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_5.addWidget(self.label_app_version)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(18)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(SC7018_Settomg_Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_fpga_version = QLabel(SC7018_Settomg_Form)
        self.label_fpga_version.setObjectName(u"label_fpga_version")
        sizePolicy.setHeightForWidth(self.label_fpga_version.sizePolicy().hasHeightForWidth())
        self.label_fpga_version.setSizePolicy(sizePolicy)
        self.label_fpga_version.setMinimumSize(QSize(75, 0))
        self.label_fpga_version.setMaximumSize(QSize(75, 16777215))
        self.label_fpga_version.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_fpga_version)

        self.horizontalSpacer_6 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.label_4 = QLabel(SC7018_Settomg_Form)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(120, 0))
        self.label_4.setMaximumSize(QSize(125, 16777215))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_hardware_ver = QLabel(SC7018_Settomg_Form)
        self.label_hardware_ver.setObjectName(u"label_hardware_ver")
        sizePolicy.setHeightForWidth(self.label_hardware_ver.sizePolicy().hasHeightForWidth())
        self.label_hardware_ver.setSizePolicy(sizePolicy)
        self.label_hardware_ver.setMinimumSize(QSize(100, 0))
        self.label_hardware_ver.setMaximumSize(QSize(100, 16777215))
        self.label_hardware_ver.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_hardware_ver)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.set_widget = QWidget(SC7018_Settomg_Form)
        self.set_widget.setObjectName(u"set_widget")
        self.set_widget.setMinimumSize(QSize(0, 80))
        self.verticalLayout = QVBoxLayout(self.set_widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.set_widget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_video_input = CustomComboBox(self.set_widget)
        self.comboBox_video_input.setObjectName(u"comboBox_video_input")

        self.horizontalLayout.addWidget(self.comboBox_video_input)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(18)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.set_widget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMaximumSize(QSize(120, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.comboBox_out_radio = CustomComboBox(self.set_widget)
        self.comboBox_out_radio.setObjectName(u"comboBox_out_radio")

        self.horizontalLayout_3.addWidget(self.comboBox_out_radio)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(18)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.set_widget)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(120, 0))
        self.label_12.setMaximumSize(QSize(120, 16777215))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.comboBox_audio_input = CustomComboBox(self.set_widget)
        self.comboBox_audio_input.setObjectName(u"comboBox_audio_input")

        self.horizontalLayout_8.addWidget(self.comboBox_audio_input)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addWidget(self.set_widget)

        self.verticalSpacer = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.retranslateUi(SC7018_Settomg_Form)

        QMetaObject.connectSlotsByName(SC7018_Settomg_Form)
    # setupUi

    def retranslateUi(self, SC7018_Settomg_Form):
        SC7018_Settomg_Form.setWindowTitle(QCoreApplication.translate("SC7018_Settomg_Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"Manufacturer:", None))
        self.label_manufacturer.setText("")
        self.label_10.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"SN:", None))
        self.label_sn.setText("")
        self.label_7.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"MCU Mode:", None))
        self.label_mcu_mode.setText("")
        self.label_8.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"Protocol Version:", None))
        self.label_protocol_ver.setText("")
        self.label_5.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"Boot Version:", None))
        self.label_boot_version.setText("")
        self.label_6.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"APP Version:", None))
        self.label_app_version.setText("")
        self.label_3.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"FPGA Version:", None))
        self.label_fpga_version.setText("")
        self.label_4.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"Hardware Version:", None))
        self.label_hardware_ver.setText("")
        self.label.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"Video Input:", None))
        self.label_11.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"Aspect Ratio:", None))
        self.label_12.setText(QCoreApplication.translate("SC7018_Settomg_Form", u"Audio Input:", None))
    # retranslateUi


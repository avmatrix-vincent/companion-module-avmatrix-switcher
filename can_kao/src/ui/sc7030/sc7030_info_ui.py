# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sc7030_info.ui'
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

class Ui_SC7030_Info_Form(object):
    def setupUi(self, SC7030_Info_Form):
        if not SC7030_Info_Form.objectName():
            SC7030_Info_Form.setObjectName(u"SC7030_Info_Form")
        SC7030_Info_Form.resize(800, 500)
        self.verticalLayout_2 = QVBoxLayout(SC7030_Info_Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 98, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(38, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(30, -1, 12, -1)
        self.label_15 = QLabel(SC7030_Info_Form)
        self.label_15.setObjectName(u"label_15")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(120, 0))
        self.label_15.setMaximumSize(QSize(125, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_15)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_15)

        self.label_protocol_ver = QLabel(SC7030_Info_Form)
        self.label_protocol_ver.setObjectName(u"label_protocol_ver")
        sizePolicy.setHeightForWidth(self.label_protocol_ver.sizePolicy().hasHeightForWidth())
        self.label_protocol_ver.setSizePolicy(sizePolicy)
        self.label_protocol_ver.setMinimumSize(QSize(100, 0))
        self.label_protocol_ver.setMaximumSize(QSize(100, 16777215))
        self.label_protocol_ver.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_protocol_ver.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_5.addWidget(self.label_protocol_ver)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 12, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.label_21 = QLabel(SC7030_Info_Form)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(100, 0))
        self.label_21.setMaximumSize(QSize(130, 16777215))
        self.label_21.setTextFormat(Qt.TextFormat.AutoText)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_21)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_9)

        self.label_manufacturer = QLabel(SC7030_Info_Form)
        self.label_manufacturer.setObjectName(u"label_manufacturer")
        sizePolicy.setHeightForWidth(self.label_manufacturer.sizePolicy().hasHeightForWidth())
        self.label_manufacturer.setSizePolicy(sizePolicy)
        self.label_manufacturer.setMinimumSize(QSize(100, 0))
        self.label_manufacturer.setMaximumSize(QSize(100, 16777215))
        self.label_manufacturer.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_manufacturer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(30, -1, 12, -1)
        self.label_11 = QLabel(SC7030_Info_Form)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(120, 0))
        self.label_11.setMaximumSize(QSize(125, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_11)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_16)

        self.label_app_version = QLabel(SC7030_Info_Form)
        self.label_app_version.setObjectName(u"label_app_version")
        sizePolicy.setHeightForWidth(self.label_app_version.sizePolicy().hasHeightForWidth())
        self.label_app_version.setSizePolicy(sizePolicy)
        self.label_app_version.setMinimumSize(QSize(100, 0))
        self.label_app_version.setMaximumSize(QSize(100, 16777215))
        self.label_app_version.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_app_version.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_7.addWidget(self.label_app_version)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(30, -1, 12, -1)
        self.label_19 = QLabel(SC7030_Info_Form)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(120, 0))
        self.label_19.setMaximumSize(QSize(125, 16777215))
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_19)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_14)

        self.label_sn = QLabel(SC7030_Info_Form)
        self.label_sn.setObjectName(u"label_sn")
        sizePolicy.setHeightForWidth(self.label_sn.sizePolicy().hasHeightForWidth())
        self.label_sn.setSizePolicy(sizePolicy)
        self.label_sn.setMinimumSize(QSize(100, 0))
        self.label_sn.setMaximumSize(QSize(100, 16777215))
        self.label_sn.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_sn.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_sn)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, 12, -1)
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)

        self.label_13 = QLabel(SC7030_Info_Form)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(100, 0))
        self.label_13.setMaximumSize(QSize(130, 16777215))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_13)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_12)

        self.label_boot_version = QLabel(SC7030_Info_Form)
        self.label_boot_version.setObjectName(u"label_boot_version")
        sizePolicy.setHeightForWidth(self.label_boot_version.sizePolicy().hasHeightForWidth())
        self.label_boot_version.setSizePolicy(sizePolicy)
        self.label_boot_version.setMinimumSize(QSize(100, 0))
        self.label_boot_version.setMaximumSize(QSize(100, 16777215))
        self.label_boot_version.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.label_boot_version)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 12, -1)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.label_17 = QLabel(SC7030_Info_Form)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(100, 0))
        self.label_17.setMaximumSize(QSize(130, 16777215))
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_17)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_11)

        self.label_mcu_mode = QLabel(SC7030_Info_Form)
        self.label_mcu_mode.setObjectName(u"label_mcu_mode")
        sizePolicy.setHeightForWidth(self.label_mcu_mode.sizePolicy().hasHeightForWidth())
        self.label_mcu_mode.setSizePolicy(sizePolicy)
        self.label_mcu_mode.setMinimumSize(QSize(100, 0))
        self.label_mcu_mode.setMaximumSize(QSize(100, 16777215))
        self.label_mcu_mode.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_mcu_mode)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, 12, -1)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_19)

        self.label_9 = QLabel(SC7030_Info_Form)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setMaximumSize(QSize(130, 16777215))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_9)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_13)

        self.label_fpga_version = QLabel(SC7030_Info_Form)
        self.label_fpga_version.setObjectName(u"label_fpga_version")
        sizePolicy.setHeightForWidth(self.label_fpga_version.sizePolicy().hasHeightForWidth())
        self.label_fpga_version.setSizePolicy(sizePolicy)
        self.label_fpga_version.setMinimumSize(QSize(100, 0))
        self.label_fpga_version.setMaximumSize(QSize(100, 16777215))
        self.label_fpga_version.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_8.addWidget(self.label_fpga_version)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(30, -1, 12, -1)
        self.label_7 = QLabel(SC7030_Info_Form)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(120, 0))
        self.label_7.setMaximumSize(QSize(125, 16777215))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_7)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_17)

        self.label_hardware_ver = QLabel(SC7030_Info_Form)
        self.label_hardware_ver.setObjectName(u"label_hardware_ver")
        sizePolicy.setHeightForWidth(self.label_hardware_ver.sizePolicy().hasHeightForWidth())
        self.label_hardware_ver.setSizePolicy(sizePolicy)
        self.label_hardware_ver.setMinimumSize(QSize(100, 0))
        self.label_hardware_ver.setMaximumSize(QSize(100, 16777215))
        self.label_hardware_ver.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_hardware_ver.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_10.addWidget(self.label_hardware_ver)


        self.gridLayout.addLayout(self.horizontalLayout_10, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_3 = QSpacerItem(140, 17, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.retranslateUi(SC7030_Info_Form)

        QMetaObject.connectSlotsByName(SC7030_Info_Form)
    # setupUi

    def retranslateUi(self, SC7030_Info_Form):
        SC7030_Info_Form.setWindowTitle(QCoreApplication.translate("SC7030_Info_Form", u"Form", None))
        self.label_15.setText(QCoreApplication.translate("SC7030_Info_Form", u"Protocol Version:", None))
        self.label_protocol_ver.setText("")
        self.label_21.setText(QCoreApplication.translate("SC7030_Info_Form", u"Manufacturer:", None))
        self.label_manufacturer.setText("")
        self.label_11.setText(QCoreApplication.translate("SC7030_Info_Form", u"APP Version:", None))
        self.label_app_version.setText("")
        self.label_19.setText(QCoreApplication.translate("SC7030_Info_Form", u"SN:", None))
        self.label_sn.setText("")
        self.label_13.setText(QCoreApplication.translate("SC7030_Info_Form", u"Boot Version:", None))
        self.label_boot_version.setText("")
        self.label_17.setText(QCoreApplication.translate("SC7030_Info_Form", u"MCU Mode:", None))
        self.label_mcu_mode.setText("")
        self.label_9.setText(QCoreApplication.translate("SC7030_Info_Form", u"FPGA Version:", None))
        self.label_fpga_version.setText("")
        self.label_7.setText(QCoreApplication.translate("SC7030_Info_Form", u"Hardware Version:", None))
        self.label_hardware_ver.setText("")
    # retranslateUi


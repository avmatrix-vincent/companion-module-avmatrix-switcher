# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SC1221_12G_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SC1221_12G_Setting_Form(object):
    def setupUi(self, SC1221_12G_Setting_Form):
        if not SC1221_12G_Setting_Form.objectName():
            SC1221_12G_Setting_Form.setObjectName(u"SC1221_12G_Setting_Form")
        SC1221_12G_Setting_Form.resize(800, 500)
        self.horizontalLayout = QHBoxLayout(SC1221_12G_Setting_Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(SC1221_12G_Setting_Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.label_manufacturer = QLabel(SC1221_12G_Setting_Form)
        self.label_manufacturer.setObjectName(u"label_manufacturer")
        sizePolicy.setHeightForWidth(self.label_manufacturer.sizePolicy().hasHeightForWidth())
        self.label_manufacturer.setSizePolicy(sizePolicy)
        self.label_manufacturer.setMinimumSize(QSize(75, 0))
        self.label_manufacturer.setMaximumSize(QSize(75, 16777215))
        self.label_manufacturer.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_5.addWidget(self.label_manufacturer)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(SC1221_12G_Setting_Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setMaximumSize(QSize(125, 16777215))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.label_sn = QLabel(SC1221_12G_Setting_Form)
        self.label_sn.setObjectName(u"label_sn")
        sizePolicy.setHeightForWidth(self.label_sn.sizePolicy().hasHeightForWidth())
        self.label_sn.setSizePolicy(sizePolicy)
        self.label_sn.setMinimumSize(QSize(100, 0))
        self.label_sn.setMaximumSize(QSize(100, 16777215))
        self.label_sn.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_5.addWidget(self.label_sn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(18)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(SC1221_12G_Setting_Form)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(120, 0))
        self.label_7.setMaximumSize(QSize(120, 16777215))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_mcu_mode = QLabel(SC1221_12G_Setting_Form)
        self.label_mcu_mode.setObjectName(u"label_mcu_mode")
        sizePolicy.setHeightForWidth(self.label_mcu_mode.sizePolicy().hasHeightForWidth())
        self.label_mcu_mode.setSizePolicy(sizePolicy)
        self.label_mcu_mode.setMinimumSize(QSize(75, 0))
        self.label_mcu_mode.setMaximumSize(QSize(75, 16777215))
        self.label_mcu_mode.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_mcu_mode)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_8 = QLabel(SC1221_12G_Setting_Form)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(120, 0))
        self.label_8.setMaximumSize(QSize(125, 16777215))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_protocol_ver = QLabel(SC1221_12G_Setting_Form)
        self.label_protocol_ver.setObjectName(u"label_protocol_ver")
        sizePolicy.setHeightForWidth(self.label_protocol_ver.sizePolicy().hasHeightForWidth())
        self.label_protocol_ver.setSizePolicy(sizePolicy)
        self.label_protocol_ver.setMinimumSize(QSize(100, 0))
        self.label_protocol_ver.setMaximumSize(QSize(100, 16777215))
        self.label_protocol_ver.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_protocol_ver)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(18)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(SC1221_12G_Setting_Form)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(120, 0))
        self.label_13.setMaximumSize(QSize(120, 16777215))
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_13)

        self.label_boot_version = QLabel(SC1221_12G_Setting_Form)
        self.label_boot_version.setObjectName(u"label_boot_version")
        sizePolicy.setHeightForWidth(self.label_boot_version.sizePolicy().hasHeightForWidth())
        self.label_boot_version.setSizePolicy(sizePolicy)
        self.label_boot_version.setMinimumSize(QSize(75, 0))
        self.label_boot_version.setMaximumSize(QSize(75, 16777215))
        self.label_boot_version.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_boot_version)

        self.horizontalSpacer_5 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_11 = QLabel(SC1221_12G_Setting_Form)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(120, 0))
        self.label_11.setMaximumSize(QSize(125, 16777215))
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.label_app_version = QLabel(SC1221_12G_Setting_Form)
        self.label_app_version.setObjectName(u"label_app_version")
        sizePolicy.setHeightForWidth(self.label_app_version.sizePolicy().hasHeightForWidth())
        self.label_app_version.setSizePolicy(sizePolicy)
        self.label_app_version.setMinimumSize(QSize(100, 0))
        self.label_app_version.setMaximumSize(QSize(100, 16777215))
        self.label_app_version.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_app_version)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_17 = QLabel(SC1221_12G_Setting_Form)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(120, 0))
        self.label_17.setMaximumSize(QSize(120, 16777215))
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_17)

        self.label_fpga_version = QLabel(SC1221_12G_Setting_Form)
        self.label_fpga_version.setObjectName(u"label_fpga_version")
        sizePolicy.setHeightForWidth(self.label_fpga_version.sizePolicy().hasHeightForWidth())
        self.label_fpga_version.setSizePolicy(sizePolicy)
        self.label_fpga_version.setMinimumSize(QSize(75, 0))
        self.label_fpga_version.setMaximumSize(QSize(75, 16777215))
        self.label_fpga_version.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_fpga_version)

        self.horizontalSpacer_6 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label_15 = QLabel(SC1221_12G_Setting_Form)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(120, 0))
        self.label_15.setMaximumSize(QSize(125, 16777215))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_15)

        self.label_hardware_ver = QLabel(SC1221_12G_Setting_Form)
        self.label_hardware_ver.setObjectName(u"label_hardware_ver")
        sizePolicy.setHeightForWidth(self.label_hardware_ver.sizePolicy().hasHeightForWidth())
        self.label_hardware_ver.setSizePolicy(sizePolicy)
        self.label_hardware_ver.setMinimumSize(QSize(100, 0))
        self.label_hardware_ver.setMaximumSize(QSize(100, 16777215))
        self.label_hardware_ver.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_hardware_ver)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.widget_sdi_output = QWidget(SC1221_12G_Setting_Form)
        self.widget_sdi_output.setObjectName(u"widget_sdi_output")
        self.widget_sdi_output.setMaximumSize(QSize(16777215, 34))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_sdi_output)
        self.horizontalLayout_6.setSpacing(18)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_sdi_output)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(120, 0))
        self.label_6.setMaximumSize(QSize(120, 16777215))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.radioButton_3g_level_a = QRadioButton(self.widget_sdi_output)
        self.radioButton_3g_level_a.setObjectName(u"radioButton_3g_level_a")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radioButton_3g_level_a.sizePolicy().hasHeightForWidth())
        self.radioButton_3g_level_a.setSizePolicy(sizePolicy1)
        self.radioButton_3g_level_a.setMinimumSize(QSize(120, 0))
        self.radioButton_3g_level_a.setMaximumSize(QSize(120, 16777215))
        self.radioButton_3g_level_a.setChecked(True)

        self.horizontalLayout_6.addWidget(self.radioButton_3g_level_a)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.radioButton_3g_level_b = QRadioButton(self.widget_sdi_output)
        self.radioButton_3g_level_b.setObjectName(u"radioButton_3g_level_b")
        sizePolicy1.setHeightForWidth(self.radioButton_3g_level_b.sizePolicy().hasHeightForWidth())
        self.radioButton_3g_level_b.setSizePolicy(sizePolicy1)
        self.radioButton_3g_level_b.setMinimumSize(QSize(125, 0))
        self.radioButton_3g_level_b.setMaximumSize(QSize(125, 16777215))

        self.horizontalLayout_6.addWidget(self.radioButton_3g_level_b)


        self.verticalLayout.addWidget(self.widget_sdi_output)

        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(SC1221_12G_Setting_Form)

        QMetaObject.connectSlotsByName(SC1221_12G_Setting_Form)
    # setupUi

    def retranslateUi(self, SC1221_12G_Setting_Form):
        SC1221_12G_Setting_Form.setWindowTitle(QCoreApplication.translate("SC1221_12G_Setting_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"Manufacturer:", None))
        self.label_manufacturer.setText("")
        self.label_3.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"SN:", None))
        self.label_sn.setText("")
        self.label_7.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"MCU Mode:", None))
        self.label_mcu_mode.setText("")
        self.label_8.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"Protocol Version:", None))
        self.label_protocol_ver.setText("")
        self.label_13.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"Boot Version:", None))
        self.label_boot_version.setText("")
        self.label_11.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"APP Version:", None))
        self.label_app_version.setText("")
        self.label_17.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"FPGA Version:", None))
        self.label_fpga_version.setText("")
        self.label_15.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"Hardware Version:", None))
        self.label_hardware_ver.setText("")
        self.label_6.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"SDI Output:", None))
        self.radioButton_3g_level_a.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"3G Level-A", None))
        self.radioButton_3g_level_b.setText(QCoreApplication.translate("SC1221_12G_Setting_Form", u"3G Level-B", None))
    # retranslateUi


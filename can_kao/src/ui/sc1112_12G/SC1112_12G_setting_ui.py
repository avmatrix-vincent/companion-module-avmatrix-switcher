# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SC1112_12G_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.components.CustomComboBox import CustomComboBox

class Ui_SC1112_12G_Setting_Form(object):
    def setupUi(self, SC1112_12G_Setting_Form):
        if not SC1112_12G_Setting_Form.objectName():
            SC1112_12G_Setting_Form.setObjectName(u"SC1112_12G_Setting_Form")
        SC1112_12G_Setting_Form.resize(800, 500)
        self.horizontalLayout = QHBoxLayout(SC1112_12G_Setting_Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(120, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 140, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(18)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(SC1112_12G_Setting_Form)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(120, 0))
        self.label_4.setMaximumSize(QSize(120, 16777215))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.label_manufacturer = QLabel(SC1112_12G_Setting_Form)
        self.label_manufacturer.setObjectName(u"label_manufacturer")
        sizePolicy.setHeightForWidth(self.label_manufacturer.sizePolicy().hasHeightForWidth())
        self.label_manufacturer.setSizePolicy(sizePolicy)
        self.label_manufacturer.setMinimumSize(QSize(75, 0))
        self.label_manufacturer.setMaximumSize(QSize(75, 16777215))
        self.label_manufacturer.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.label_manufacturer)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(SC1112_12G_Setting_Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setMaximumSize(QSize(125, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.label_sn = QLabel(SC1112_12G_Setting_Form)
        self.label_sn.setObjectName(u"label_sn")
        sizePolicy.setHeightForWidth(self.label_sn.sizePolicy().hasHeightForWidth())
        self.label_sn.setSizePolicy(sizePolicy)
        self.label_sn.setMinimumSize(QSize(115, 0))
        self.label_sn.setMaximumSize(QSize(115, 16777215))
        self.label_sn.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.label_sn)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(18)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(SC1112_12G_Setting_Form)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(120, 0))
        self.label_11.setMaximumSize(QSize(120, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.label_mcu_mode = QLabel(SC1112_12G_Setting_Form)
        self.label_mcu_mode.setObjectName(u"label_mcu_mode")
        sizePolicy.setHeightForWidth(self.label_mcu_mode.sizePolicy().hasHeightForWidth())
        self.label_mcu_mode.setSizePolicy(sizePolicy)
        self.label_mcu_mode.setMinimumSize(QSize(75, 0))
        self.label_mcu_mode.setMaximumSize(QSize(75, 16777215))
        self.label_mcu_mode.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_mcu_mode)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_7 = QLabel(SC1112_12G_Setting_Form)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(120, 0))
        self.label_7.setMaximumSize(QSize(125, 16777215))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_protocol_ver = QLabel(SC1112_12G_Setting_Form)
        self.label_protocol_ver.setObjectName(u"label_protocol_ver")
        sizePolicy.setHeightForWidth(self.label_protocol_ver.sizePolicy().hasHeightForWidth())
        self.label_protocol_ver.setSizePolicy(sizePolicy)
        self.label_protocol_ver.setMinimumSize(QSize(115, 0))
        self.label_protocol_ver.setMaximumSize(QSize(115, 16777215))
        self.label_protocol_ver.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_protocol_ver)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(18)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(SC1112_12G_Setting_Form)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(120, 0))
        self.label_13.setMaximumSize(QSize(120, 16777215))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_13)

        self.label_boot_version = QLabel(SC1112_12G_Setting_Form)
        self.label_boot_version.setObjectName(u"label_boot_version")
        sizePolicy.setHeightForWidth(self.label_boot_version.sizePolicy().hasHeightForWidth())
        self.label_boot_version.setSizePolicy(sizePolicy)
        self.label_boot_version.setMinimumSize(QSize(75, 0))
        self.label_boot_version.setMaximumSize(QSize(75, 16777215))
        self.label_boot_version.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_boot_version)

        self.horizontalSpacer_5 = QSpacerItem(0, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_10 = QLabel(SC1112_12G_Setting_Form)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(120, 0))
        self.label_10.setMaximumSize(QSize(125, 16777215))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_app_version = QLabel(SC1112_12G_Setting_Form)
        self.label_app_version.setObjectName(u"label_app_version")
        sizePolicy.setHeightForWidth(self.label_app_version.sizePolicy().hasHeightForWidth())
        self.label_app_version.setSizePolicy(sizePolicy)
        self.label_app_version.setMinimumSize(QSize(115, 0))
        self.label_app_version.setMaximumSize(QSize(115, 16777215))
        self.label_app_version.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_app_version)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_17 = QLabel(SC1112_12G_Setting_Form)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(120, 0))
        self.label_17.setMaximumSize(QSize(120, 16777215))
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_17)

        self.label_fpga_version = QLabel(SC1112_12G_Setting_Form)
        self.label_fpga_version.setObjectName(u"label_fpga_version")
        sizePolicy.setHeightForWidth(self.label_fpga_version.sizePolicy().hasHeightForWidth())
        self.label_fpga_version.setSizePolicy(sizePolicy)
        self.label_fpga_version.setMinimumSize(QSize(75, 0))
        self.label_fpga_version.setMaximumSize(QSize(75, 16777215))
        self.label_fpga_version.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_fpga_version)

        self.horizontalSpacer_6 = QSpacerItem(0, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label_15 = QLabel(SC1112_12G_Setting_Form)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(120, 0))
        self.label_15.setMaximumSize(QSize(125, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_15)

        self.label_hardware_ver = QLabel(SC1112_12G_Setting_Form)
        self.label_hardware_ver.setObjectName(u"label_hardware_ver")
        sizePolicy.setHeightForWidth(self.label_hardware_ver.sizePolicy().hasHeightForWidth())
        self.label_hardware_ver.setSizePolicy(sizePolicy)
        self.label_hardware_ver.setMinimumSize(QSize(115, 0))
        self.label_hardware_ver.setMaximumSize(QSize(115, 16777215))
        self.label_hardware_ver.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_hardware_ver)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.widget_hdmi_output = QWidget(SC1112_12G_Setting_Form)
        self.widget_hdmi_output.setObjectName(u"widget_hdmi_output")
        self.widget_hdmi_output.setMaximumSize(QSize(16777215, 34))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_hdmi_output)
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_hdmi_output)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setMaximumSize(QSize(120, 16777215))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.radioButton_full_hdmi = QRadioButton(self.widget_hdmi_output)
        self.radioButton_full_hdmi.setObjectName(u"radioButton_full_hdmi")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radioButton_full_hdmi.sizePolicy().hasHeightForWidth())
        self.radioButton_full_hdmi.setSizePolicy(sizePolicy1)
        self.radioButton_full_hdmi.setMinimumSize(QSize(120, 0))
        self.radioButton_full_hdmi.setMaximumSize(QSize(120, 16777215))
        self.radioButton_full_hdmi.setChecked(True)

        self.horizontalLayout_5.addWidget(self.radioButton_full_hdmi)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.radioButton_limited_hdmi = QRadioButton(self.widget_hdmi_output)
        self.radioButton_limited_hdmi.setObjectName(u"radioButton_limited_hdmi")
        sizePolicy1.setHeightForWidth(self.radioButton_limited_hdmi.sizePolicy().hasHeightForWidth())
        self.radioButton_limited_hdmi.setSizePolicy(sizePolicy1)
        self.radioButton_limited_hdmi.setMinimumSize(QSize(135, 0))
        self.radioButton_limited_hdmi.setMaximumSize(QSize(135, 16777215))
        self.radioButton_limited_hdmi.setChecked(False)

        self.horizontalLayout_5.addWidget(self.radioButton_limited_hdmi)

        self.horizontalSpacer_8 = QSpacerItem(15, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addWidget(self.widget_hdmi_output)

        self.widget_hdmi_output_2 = QWidget(SC1112_12G_Setting_Form)
        self.widget_hdmi_output_2.setObjectName(u"widget_hdmi_output_2")
        self.widget_hdmi_output_2.setMaximumSize(QSize(16777215, 34))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_hdmi_output_2)
        self.horizontalLayout_8.setSpacing(18)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_hdmi_output_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(120, 0))
        self.label_6.setMaximumSize(QSize(120, 16777215))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.radioButton_709 = QRadioButton(self.widget_hdmi_output_2)
        self.buttonGroup = QButtonGroup(SC1112_12G_Setting_Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_709)
        self.radioButton_709.setObjectName(u"radioButton_709")
        sizePolicy1.setHeightForWidth(self.radioButton_709.sizePolicy().hasHeightForWidth())
        self.radioButton_709.setSizePolicy(sizePolicy1)
        self.radioButton_709.setMinimumSize(QSize(120, 0))
        self.radioButton_709.setMaximumSize(QSize(120, 16777215))
        self.radioButton_709.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radioButton_709)

        self.horizontalSpacer_9 = QSpacerItem(0, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.radioButton_2020 = QRadioButton(self.widget_hdmi_output_2)
        self.buttonGroup.addButton(self.radioButton_2020)
        self.radioButton_2020.setObjectName(u"radioButton_2020")
        sizePolicy1.setHeightForWidth(self.radioButton_2020.sizePolicy().hasHeightForWidth())
        self.radioButton_2020.setSizePolicy(sizePolicy1)
        self.radioButton_2020.setMinimumSize(QSize(135, 0))
        self.radioButton_2020.setMaximumSize(QSize(135, 16777215))
        self.radioButton_2020.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_2020)

        self.horizontalSpacer_10 = QSpacerItem(15, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addWidget(self.widget_hdmi_output_2)

        self.widget_color_space = QWidget(SC1112_12G_Setting_Form)
        self.widget_color_space.setObjectName(u"widget_color_space")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_color_space)
        self.horizontalLayout_7.setSpacing(18)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_color_space)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label)

        self.comboBox__color_space = CustomComboBox(self.widget_color_space)
        self.comboBox__color_space.setObjectName(u"comboBox__color_space")

        self.horizontalLayout_7.addWidget(self.comboBox__color_space)


        self.verticalLayout.addWidget(self.widget_color_space)

        self.verticalSpacer_2 = QSpacerItem(20, 140, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(120, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(SC1112_12G_Setting_Form)

        QMetaObject.connectSlotsByName(SC1112_12G_Setting_Form)
    # setupUi

    def retranslateUi(self, SC1112_12G_Setting_Form):
        SC1112_12G_Setting_Form.setWindowTitle(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Manufacturer:", None))
        self.label_manufacturer.setText("")
        self.label_2.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"SN:", None))
        self.label_sn.setText("")
        self.label_11.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"MCU Mode:", None))
        self.label_mcu_mode.setText("")
        self.label_7.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Protocol Version:", None))
        self.label_protocol_ver.setText("")
        self.label_13.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Boot Version:", None))
        self.label_boot_version.setText("")
        self.label_10.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"APP Version:", None))
        self.label_app_version.setText("")
        self.label_17.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"FPGA Version:", None))
        self.label_fpga_version.setText("")
        self.label_15.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Hardware Version:", None))
        self.label_hardware_ver.setText("")
        self.label_5.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Color Range:", None))
        self.radioButton_full_hdmi.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Full Range", None))
        self.radioButton_limited_hdmi.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Limited Range", None))
        self.label_6.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Colorimetry:", None))
        self.radioButton_709.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Rec.709", None))
        self.radioButton_2020.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Rec.BT2020", None))
        self.label.setText(QCoreApplication.translate("SC1112_12G_Setting_Form", u"Color Space:", None))
    # retranslateUi


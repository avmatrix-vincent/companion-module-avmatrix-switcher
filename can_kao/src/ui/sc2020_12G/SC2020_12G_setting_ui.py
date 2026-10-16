# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SC2020_12G_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SC2020_12G_Setting_Form(object):
    def setupUi(self, SC2020_12G_Setting_Form):
        if not SC2020_12G_Setting_Form.objectName():
            SC2020_12G_Setting_Form.setObjectName(u"SC2020_12G_Setting_Form")
        SC2020_12G_Setting_Form.resize(800, 514)
        SC2020_12G_Setting_Form.setStyleSheet(u"\n"
"#SC2020_12G_Setting_Form{\n"
"	background-color: rgba(60, 60, 60, 1);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_25 = QHBoxLayout(SC2020_12G_Setting_Form)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_36 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_36)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_10 = QSpacerItem(17, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_10)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.msg_widget = QWidget(SC2020_12G_Setting_Form)
        self.msg_widget.setObjectName(u"msg_widget")
        self.msg_widget.setMinimumSize(QSize(387, 217))
        self.msg_widget.setMaximumSize(QSize(387, 217))
        self.msg_widget.setStyleSheet(u"#msg_widget{\n"
"	border-radius: 18px;\n"
"	background-color:rgba(89, 89, 89,1);\n"
"}\n"
"\n"
"#msg_widget QLabel {\n"
"    color: rgba(255, 255, 255, 0.4);\n"
"	font-size: 10px;\n"
"	font-weight: 400;\n"
"	line-height: 12px;\n"
"	letter-spacing: 0px;\n"
"	text-align: left;\n"
"	\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.msg_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, -1, -1, 12)
        self.name1 = QLabel(self.msg_widget)
        self.name1.setObjectName(u"name1")
        self.name1.setMinimumSize(QSize(5, 16))
        self.name1.setMaximumSize(QSize(5, 16))
        self.name1.setStyleSheet(u"#name1{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 rgba(219, 124, 51, 1), \n"
"    stop:1 rgba(137, 131, 127, 0.73));\n"
"border-radius: 2px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.name1)

        self.label_11 = QLabel(self.msg_widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 18))
        self.label_11.setMaximumSize(QSize(16777215, 18))
        font = QFont()
        font.setFamilies([u"DingTalk JinBuTi"])
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgba(219, 124, 51, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 13px;\n"
"font-weight: 400;\n"
"line-height: 14px;\n"
"letter-spacing: 0px;\n"
"text-align: left;")

        self.horizontalLayout_16.addWidget(self.label_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(12)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.msg_widget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.horizontalSpacer_9 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_9)

        self.sn_msg = QLabel(self.msg_widget)
        self.sn_msg.setObjectName(u"sn_msg")
        self.sn_msg.setMinimumSize(QSize(75, 32))
        self.sn_msg.setMaximumSize(QSize(75, 32))
        self.sn_msg.setStyleSheet(u"#sn_msg{\n"
"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;\n"
"}")

        self.horizontalLayout_19.addWidget(self.sn_msg)


        self.verticalLayout_2.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, 5, -1)
        self.label_17 = QLabel(self.msg_widget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_20.addWidget(self.label_17)

        self.horizontalSpacer_10 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)

        self.system_msg = QLabel(self.msg_widget)
        self.system_msg.setObjectName(u"system_msg")
        self.system_msg.setMinimumSize(QSize(50, 32))
        self.system_msg.setMaximumSize(QSize(100, 32))
        self.system_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.system_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.system_msg)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, 5, -1)
        self.label_19 = QLabel(self.msg_widget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_21.addWidget(self.label_19)

        self.horizontalSpacer_17 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_17)

        self.yingjian_msg = QLabel(self.msg_widget)
        self.yingjian_msg.setObjectName(u"yingjian_msg")
        self.yingjian_msg.setMinimumSize(QSize(50, 32))
        self.yingjian_msg.setMaximumSize(QSize(100, 32))
        self.yingjian_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.yingjian_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.yingjian_msg)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, -1, 5, -1)
        self.label_18 = QLabel(self.msg_widget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_22.addWidget(self.label_18)

        self.horizontalSpacer_18 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_18)

        self.image_msg = QLabel(self.msg_widget)
        self.image_msg.setObjectName(u"image_msg")
        self.image_msg.setMinimumSize(QSize(50, 32))
        self.image_msg.setMaximumSize(QSize(100, 32))
        self.image_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.image_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.image_msg)


        self.verticalLayout_2.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_34.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_23 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_23)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 2, 5, -1)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, -1, 5, -1)
        self.sn_msg_8 = QLabel(self.msg_widget)
        self.sn_msg_8.setObjectName(u"sn_msg_8")

        self.horizontalLayout_31.addWidget(self.sn_msg_8)

        self.horizontalSpacer_19 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_19)

        self.control_msg = QLabel(self.msg_widget)
        self.control_msg.setObjectName(u"control_msg")
        self.control_msg.setMinimumSize(QSize(75, 32))
        self.control_msg.setMaximumSize(QSize(75, 32))
        self.control_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.control_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.control_msg)


        self.verticalLayout_3.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, -1, 5, -1)
        self.sn_msg_9 = QLabel(self.msg_widget)
        self.sn_msg_9.setObjectName(u"sn_msg_9")

        self.horizontalLayout_32.addWidget(self.sn_msg_9)

        self.horizontalSpacer_20 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_20)

        self.temp_msg = QLabel(self.msg_widget)
        self.temp_msg.setObjectName(u"temp_msg")
        self.temp_msg.setMinimumSize(QSize(70, 32))
        self.temp_msg.setMaximumSize(QSize(16777215, 32))
        self.temp_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.temp_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.temp_msg)


        self.verticalLayout_3.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, -1, 5, -1)
        self.sn_msg_11 = QLabel(self.msg_widget)
        self.sn_msg_11.setObjectName(u"sn_msg_11")
        self.sn_msg_11.setMinimumSize(QSize(0, 32))
        self.sn_msg_11.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_33.addWidget(self.sn_msg_11)

        self.horizontalSpacer_21 = QSpacerItem(28, 28, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_21)

        self.fan_speed_comBox = QComboBox(self.msg_widget)
        self.fan_speed_comBox.setObjectName(u"fan_speed_comBox")
        self.fan_speed_comBox.setMinimumSize(QSize(68, 20))
        self.fan_speed_comBox.setMaximumSize(QSize(68, 20))
        self.fan_speed_comBox.setStyleSheet(u"color:white;\n"
"font-weight: 400;")

        self.horizontalLayout_33.addWidget(self.fan_speed_comBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_33)

        self.verticalSpacer_2 = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_34.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_34)


        self.verticalLayout_9.addWidget(self.msg_widget)

        self.verticalSpacer_7 = QSpacerItem(17, 33, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.input_widget = QWidget(SC2020_12G_Setting_Form)
        self.input_widget.setObjectName(u"input_widget")
        self.input_widget.setMinimumSize(QSize(387, 217))
        self.input_widget.setMaximumSize(QSize(387, 217))
        self.input_widget.setStyleSheet(u"#input_widget{\n"
"	border-radius: 18px;\n"
"	background-color:rgba(89, 89, 89,1);\n"
"}\n"
"\n"
"#input_widget QLabel {\n"
"    color: rgba(255, 255, 255, 0.4);\n"
"	font-size: 10px;\n"
"	font-weight: 400;\n"
"	line-height: 12px;\n"
"	letter-spacing: 0px;\n"
"	text-align: left;\n"
"	\n"
"}\n"
"")
        self.horizontalLayout_42 = QHBoxLayout(self.input_widget)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, -1, -1, 0)
        self.name2 = QLabel(self.input_widget)
        self.name2.setObjectName(u"name2")
        self.name2.setMinimumSize(QSize(5, 16))
        self.name2.setMaximumSize(QSize(5, 16))
        self.name2.setStyleSheet(u"#name2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 rgba(219, 124, 51, 1), \n"
"    stop:1 rgba(137, 131, 127, 0.73));\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.name2)

        self.label_13 = QLabel(self.input_widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 18))
        self.label_13.setMaximumSize(QSize(16777215, 18))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgba(219, 124, 51, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 13px;\n"
"font-weight: 400;\n"
"line-height: 14px;\n"
"letter-spacing: 0px;\n"
"text-align: left;")

        self.horizontalLayout_17.addWidget(self.label_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_3 = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_20 = QLabel(self.input_widget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_28.addWidget(self.label_20)

        self.horizontalSpacer_24 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_24)

        self.fenbianlv_hdmi_msg = QLabel(self.input_widget)
        self.fenbianlv_hdmi_msg.setObjectName(u"fenbianlv_hdmi_msg")
        self.fenbianlv_hdmi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.fenbianlv_hdmi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.fenbianlv_hdmi_msg)


        self.verticalLayout_5.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_28 = QLabel(self.input_widget)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_29.addWidget(self.label_28)

        self.horizontalSpacer_25 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_25)

        self.rate_hdmi_msg = QLabel(self.input_widget)
        self.rate_hdmi_msg.setObjectName(u"rate_hdmi_msg")
        self.rate_hdmi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.rate_hdmi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.rate_hdmi_msg)


        self.verticalLayout_5.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_29 = QLabel(self.input_widget)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_30.addWidget(self.label_29)

        self.horizontalSpacer_26 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_26)

        self.color_space_hdmi_msg = QLabel(self.input_widget)
        self.color_space_hdmi_msg.setObjectName(u"color_space_hdmi_msg")
        self.color_space_hdmi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.color_space_hdmi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.color_space_hdmi_msg)


        self.verticalLayout_5.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_30 = QLabel(self.input_widget)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_35.addWidget(self.label_30)

        self.horizontalSpacer_27 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_27)

        self.bit_hdmi_msg = QLabel(self.input_widget)
        self.bit_hdmi_msg.setObjectName(u"bit_hdmi_msg")
        self.bit_hdmi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.bit_hdmi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.bit_hdmi_msg)


        self.verticalLayout_5.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_31 = QLabel(self.input_widget)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_36.addWidget(self.label_31)

        self.horizontalSpacer_28 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_28)

        self.seyu_hdmi_msg = QLabel(self.input_widget)
        self.seyu_hdmi_msg.setObjectName(u"seyu_hdmi_msg")
        self.seyu_hdmi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.seyu_hdmi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.seyu_hdmi_msg)


        self.verticalLayout_5.addLayout(self.horizontalLayout_36)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)


        self.horizontalLayout_42.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_34 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_34)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(10, -1, -1, 0)
        self.name3 = QLabel(self.input_widget)
        self.name3.setObjectName(u"name3")
        self.name3.setMinimumSize(QSize(5, 16))
        self.name3.setMaximumSize(QSize(5, 16))
        self.name3.setStyleSheet(u"#name3{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 rgba(219, 124, 51, 1), \n"
"    stop:1 rgba(137, 131, 127, 0.73));\n"
"	border-radius: 2px;\n"
"}")

        self.horizontalLayout_18.addWidget(self.name3)

        self.label_15 = QLabel(self.input_widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 18))
        self.label_15.setMaximumSize(QSize(16777215, 18))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgba(219, 124, 51, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 13px;\n"
"font-weight: 400;\n"
"line-height: 14px;\n"
"letter-spacing: 0px;\n"
"text-align: left;")

        self.horizontalLayout_18.addWidget(self.label_15)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_4 = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_32 = QLabel(self.input_widget)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_37.addWidget(self.label_32)

        self.horizontalSpacer_29 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_29)

        self.fenbianlv_sdi_msg = QLabel(self.input_widget)
        self.fenbianlv_sdi_msg.setObjectName(u"fenbianlv_sdi_msg")
        self.fenbianlv_sdi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.fenbianlv_sdi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.fenbianlv_sdi_msg)


        self.verticalLayout_7.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_33 = QLabel(self.input_widget)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_38.addWidget(self.label_33)

        self.horizontalSpacer_30 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_30)

        self.rate_sdi_msg = QLabel(self.input_widget)
        self.rate_sdi_msg.setObjectName(u"rate_sdi_msg")
        self.rate_sdi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.rate_sdi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.rate_sdi_msg)


        self.verticalLayout_7.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_34 = QLabel(self.input_widget)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_39.addWidget(self.label_34)

        self.horizontalSpacer_31 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_31)

        self.color_space_sdi_msg = QLabel(self.input_widget)
        self.color_space_sdi_msg.setObjectName(u"color_space_sdi_msg")
        self.color_space_sdi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.color_space_sdi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.color_space_sdi_msg)


        self.verticalLayout_7.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_35 = QLabel(self.input_widget)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_40.addWidget(self.label_35)

        self.horizontalSpacer_32 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_32)

        self.bit_sdi_msg = QLabel(self.input_widget)
        self.bit_sdi_msg.setObjectName(u"bit_sdi_msg")
        self.bit_sdi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.bit_sdi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.bit_sdi_msg)


        self.verticalLayout_7.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_36 = QLabel(self.input_widget)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_41.addWidget(self.label_36)

        self.horizontalSpacer_33 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_33)

        self.seyu_sdi_msg = QLabel(self.input_widget)
        self.seyu_sdi_msg.setObjectName(u"seyu_sdi_msg")
        self.seyu_sdi_msg.setStyleSheet(u"color: rgba(255, 255, 255, 1);\n"
"font-family: DingTalk JinBuTi;\n"
"font-size: 10px;\n"
"font-weight: 600;\n"
"line-height: 12px;\n"
"letter-spacing: 0px;\n"
"text-align: right;")
        self.seyu_sdi_msg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.seyu_sdi_msg)


        self.verticalLayout_7.addLayout(self.horizontalLayout_41)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer_6 = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)


        self.horizontalLayout_42.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addWidget(self.input_widget)


        self.horizontalLayout_23.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_35 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_35)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.signal_widget = QWidget(SC2020_12G_Setting_Form)
        self.signal_widget.setObjectName(u"signal_widget")
        self.signal_widget.setMinimumSize(QSize(347, 472))
        self.signal_widget.setMaximumSize(QSize(347, 472))
        self.signal_widget.setStyleSheet(u"#signal_widget{\n"
"	border-radius: 18px;\n"
"	background-color:rgba(89, 89, 89,1);\n"
"}\n"
"#signal_widget QLabel{\n"
"	color: rgba(255, 255, 255, 0.4);\n"
"	font-family: DingTalk JinBuTi;\n"
"	font-size: 12px;\n"
"	font-weight: 400;\n"
"	line-height: 12px;\n"
"	letter-spacing: 0px;\n"
"	text-align: left;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.signal_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, -1, -1, 25)
        self.label_9 = QLabel(self.signal_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(5, 16))
        self.label_9.setMaximumSize(QSize(5, 16))
        self.label_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 rgba(219, 124, 51, 1), \n"
"    stop:1 rgba(137, 131, 127, 0.73));\n"
"border-radius: 2px;")

        self.horizontalLayout_15.addWidget(self.label_9)

        self.label_8 = QLabel(self.signal_widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 18))
        self.label_8.setMaximumSize(QSize(16777215, 18))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color:rgba(219, 124, 51, 1)")

        self.horizontalLayout_15.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(self.signal_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_4)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.sdi_3g_out_comBox_2 = QComboBox(self.signal_widget)
        self.sdi_3g_out_comBox_2.setObjectName(u"sdi_3g_out_comBox_2")
        self.sdi_3g_out_comBox_2.setMinimumSize(QSize(128, 20))
        self.sdi_3g_out_comBox_2.setMaximumSize(QSize(128, 20))
        self.sdi_3g_out_comBox_2.setStyleSheet(u"color:white;\n"
"font-weight: 400;")

        self.horizontalLayout_12.addWidget(self.sdi_3g_out_comBox_2)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)


        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.label_6 = QLabel(self.signal_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, -1, -1)
        self.sdi_sfp_mode_comBox_2 = QComboBox(self.signal_widget)
        self.sdi_sfp_mode_comBox_2.setObjectName(u"sdi_sfp_mode_comBox_2")
        self.sdi_sfp_mode_comBox_2.setMinimumSize(QSize(128, 20))
        self.sdi_sfp_mode_comBox_2.setMaximumSize(QSize(128, 20))
        self.sdi_sfp_mode_comBox_2.setStyleSheet(u"color:white;\n"
"font-weight: 400;")

        self.horizontalLayout_13.addWidget(self.sdi_sfp_mode_comBox_2)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)


        self.gridLayout.addLayout(self.horizontalLayout_13, 1, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.signal_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.hdmi_out_src_comBox_2 = QComboBox(self.signal_widget)
        self.hdmi_out_src_comBox_2.setObjectName(u"hdmi_out_src_comBox_2")
        self.hdmi_out_src_comBox_2.setMinimumSize(QSize(128, 20))
        self.hdmi_out_src_comBox_2.setMaximumSize(QSize(128, 20))
        self.hdmi_out_src_comBox_2.setStyleSheet(u"color:white;\n"
"font-weight: 400;")

        self.horizontalLayout_10.addWidget(self.hdmi_out_src_comBox_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)


        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.signal_widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.sdi_out_src_comBox_2 = QComboBox(self.signal_widget)
        self.sdi_out_src_comBox_2.setObjectName(u"sdi_out_src_comBox_2")
        self.sdi_out_src_comBox_2.setMinimumSize(QSize(128, 20))
        self.sdi_out_src_comBox_2.setMaximumSize(QSize(128, 20))
        self.sdi_out_src_comBox_2.setStyleSheet(u"color:white;\n"
"font-weight: 400;")

        self.horizontalLayout_9.addWidget(self.sdi_out_src_comBox_2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)


        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.signal_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.hdmi_out_range_comBox_2 = QComboBox(self.signal_widget)
        self.hdmi_out_range_comBox_2.setObjectName(u"hdmi_out_range_comBox_2")
        self.hdmi_out_range_comBox_2.setMinimumSize(QSize(128, 20))
        self.hdmi_out_range_comBox_2.setMaximumSize(QSize(128, 20))
        self.hdmi_out_range_comBox_2.setStyleSheet(u"color:white;\n"
"font-weight: 400;")

        self.horizontalLayout_11.addWidget(self.hdmi_out_range_comBox_2)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.gridLayout.addLayout(self.horizontalLayout_11, 4, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.label_5 = QLabel(self.signal_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.hdmi_out_color_comBox = QComboBox(self.signal_widget)
        self.hdmi_out_color_comBox.setObjectName(u"hdmi_out_color_comBox")
        self.hdmi_out_color_comBox.setMinimumSize(QSize(128, 20))
        self.hdmi_out_color_comBox.setMaximumSize(QSize(128, 20))
        self.hdmi_out_color_comBox.setStyleSheet(u"color:white;\n"
"font-weight: 400;")

        self.horizontalLayout_2.addWidget(self.hdmi_out_color_comBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_7 = QLabel(self.signal_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_7)


        self.gridLayout.addLayout(self.horizontalLayout_8, 6, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, -1, -1)
        self.color_metry_comBox_2 = QComboBox(self.signal_widget)
        self.color_metry_comBox_2.setObjectName(u"color_metry_comBox_2")
        self.color_metry_comBox_2.setMinimumSize(QSize(128, 20))
        self.color_metry_comBox_2.setMaximumSize(QSize(128, 20))
        self.color_metry_comBox_2.setStyleSheet(u"color:white;\n"
"font-weight: 400;")

        self.horizontalLayout_14.addWidget(self.color_metry_comBox_2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_16)


        self.gridLayout.addLayout(self.horizontalLayout_14, 6, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 114, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_10.addWidget(self.signal_widget)

        self.verticalSpacer_8 = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)


        self.horizontalLayout_23.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_9 = QSpacerItem(17, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_9)


        self.horizontalLayout_25.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_37 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_37)


        self.retranslateUi(SC2020_12G_Setting_Form)

        QMetaObject.connectSlotsByName(SC2020_12G_Setting_Form)
    # setupUi

    def retranslateUi(self, SC2020_12G_Setting_Form):
        SC2020_12G_Setting_Form.setWindowTitle(QCoreApplication.translate("SC2020_12G_Setting_Form", u"Form", None))
        self.name1.setText("")
        self.label_11.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"<html><head/><body><p><span style=\" font-weight:700;\">\u57fa\u672c\u4fe1\u606f</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u5e8f\u5217\u53f7", None))
        self.sn_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"4E9758615400", None))
        self.label_17.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u7cfb\u7edf\u7248\u672c", None))
        self.system_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"V2.0.2.1", None))
        self.label_19.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u786c\u4ef6\u7248\u672c", None))
        self.yingjian_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"V2.0.2.1", None))
        self.label_18.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u56fe\u50cf\u7248\u672c", None))
        self.image_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"V2.0.2.1", None))
        self.sn_msg_8.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u63a7\u5236\u6807\u5fd7", None))
        self.control_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"PC", None))
        self.sn_msg_9.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u8bbe\u5907\u6e29\u5ea6", None))
        self.temp_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"40\u2103", None))
        self.sn_msg_11.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u98ce\u6247\u8f6c\u901f", None))
        self.name2.setText("")
        self.label_13.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"<html><head/><body><p><span style=\" font-weight:700;\">HDMI\u8f93\u5165\u4fe1\u606f</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u5206\u8fa8\u7387", None))
        self.fenbianlv_hdmi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"3840x2160", None))
        self.label_28.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u5e27\u7387", None))
        self.rate_hdmi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"p60", None))
        self.label_29.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u8272\u5f69\u7a7a\u95f4", None))
        self.color_space_hdmi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"RGB 4:4:4", None))
        self.label_30.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u4f4d\u6df1", None))
        self.bit_hdmi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"8bits", None))
        self.label_31.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u8272\u57df", None))
        self.seyu_hdmi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"Rec.709", None))
        self.name3.setText("")
        self.label_15.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"<html><head/><body><p><span style=\" font-weight:700;\">SDI\u8f93\u5165\u4fe1\u606f</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u5206\u8fa8\u7387", None))
        self.fenbianlv_sdi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"3840x2160", None))
        self.label_33.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u5e27\u7387", None))
        self.rate_sdi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"p60", None))
        self.label_34.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u8272\u5f69\u7a7a\u95f4", None))
        self.color_space_sdi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"RGB 4:4:4", None))
        self.label_35.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u4f4d\u6df1", None))
        self.bit_sdi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"8bits", None))
        self.label_36.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"\u8272\u57df", None))
        self.seyu_sdi_msg.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"Rec.709", None))
        self.label_9.setText("")
        self.label_8.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\u4fe1\u53f7\u914d\u7f6e</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"3G-SDI Out", None))
        self.label_6.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"SDI/SFP In Mode", None))
        self.label_2.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"HDMI Out Source", None))
        self.label.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"SDI/SFP Out Source", None))
        self.label_3.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"HDMI Out Range", None))
        self.label_5.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"HDMI Out Color", None))
        self.label_7.setText(QCoreApplication.translate("SC2020_12G_Setting_Form", u"HDMI Out Colorimetry", None))
    # retranslateUi


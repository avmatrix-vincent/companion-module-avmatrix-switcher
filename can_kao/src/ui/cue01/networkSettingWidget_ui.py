# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'networkSettingWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.components.ClearableLineEdit import ClearableLineEdit
from src.components.SwitchButton import SwitchBtn

class Ui_CUE01_Network_Setting_Widget_Form(object):
    def setupUi(self, CUE01_Network_Setting_Widget_Form):
        if not CUE01_Network_Setting_Widget_Form.objectName():
            CUE01_Network_Setting_Widget_Form.setObjectName(u"CUE01_Network_Setting_Widget_Form")
        CUE01_Network_Setting_Widget_Form.resize(800, 500)
        self.horizontalLayout = QHBoxLayout(CUE01_Network_Setting_Widget_Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(254, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(18)
        self.gridLayout.setVerticalSpacing(10)
        self.widget_hcp_switchbtn = SwitchBtn(CUE01_Network_Setting_Widget_Form)
        self.widget_hcp_switchbtn.setObjectName(u"widget_hcp_switchbtn")

        self.gridLayout.addWidget(self.widget_hcp_switchbtn, 0, 1, 1, 1)

        self.clearableLineEdit_mask = ClearableLineEdit(CUE01_Network_Setting_Widget_Form)
        self.clearableLineEdit_mask.setObjectName(u"clearableLineEdit_mask")
        self.clearableLineEdit_mask.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.clearableLineEdit_mask, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.label_3 = QLabel(CUE01_Network_Setting_Widget_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(CUE01_Network_Setting_Widget_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.clearableLineEdit_gateway = ClearableLineEdit(CUE01_Network_Setting_Widget_Form)
        self.clearableLineEdit_gateway.setObjectName(u"clearableLineEdit_gateway")
        self.clearableLineEdit_gateway.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.clearableLineEdit_gateway, 3, 1, 1, 1)

        self.pushButton_save = QPushButton(CUE01_Network_Setting_Widget_Form)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.pushButton_save, 4, 1, 1, 1)

        self.label_2 = QLabel(CUE01_Network_Setting_Widget_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.clearableLineEdit_ip = ClearableLineEdit(CUE01_Network_Setting_Widget_Form)
        self.clearableLineEdit_ip.setObjectName(u"clearableLineEdit_ip")
        self.clearableLineEdit_ip.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.clearableLineEdit_ip, 1, 1, 1, 1)

        self.label = QLabel(CUE01_Network_Setting_Widget_Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 5)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 5)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(254, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.retranslateUi(CUE01_Network_Setting_Widget_Form)

        QMetaObject.connectSlotsByName(CUE01_Network_Setting_Widget_Form)
    # setupUi

    def retranslateUi(self, CUE01_Network_Setting_Widget_Form):
        CUE01_Network_Setting_Widget_Form.setWindowTitle(QCoreApplication.translate("CUE01_Network_Setting_Widget_Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_Network_Setting_Widget_Form", u"Subnet Mask", None))
        self.label_4.setText(QCoreApplication.translate("CUE01_Network_Setting_Widget_Form", u"Gateway", None))
        self.pushButton_save.setText(QCoreApplication.translate("CUE01_Network_Setting_Widget_Form", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_Network_Setting_Widget_Form", u"IP", None))
        self.label.setText(QCoreApplication.translate("CUE01_Network_Setting_Widget_Form", u"DHCP ON/OFF", None))
    # retranslateUi


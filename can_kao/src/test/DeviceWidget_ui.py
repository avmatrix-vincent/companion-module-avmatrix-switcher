# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeviceWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(180, 100)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.device_name_label = QLabel(Form)
        self.device_name_label.setObjectName(u"device_name_label")

        self.horizontalLayout.addWidget(self.device_name_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_close = QPushButton(Form)
        self.pushButton_close.setObjectName(u"pushButton_close")

        self.horizontalLayout.addWidget(self.pushButton_close)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tip_light_label = QLabel(Form)
        self.tip_light_label.setObjectName(u"tip_light_label")
        self.tip_light_label.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout.addWidget(self.tip_light_label)

        self.address_label = QLabel(Form)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.address_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.setting_button = QPushButton(Form)
        self.setting_button.setObjectName(u"setting_button")
        self.setting_button.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_2.addWidget(self.setting_button)

        self.delete_button = QPushButton(Form)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_2.addWidget(self.delete_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.device_name_label.setText(QCoreApplication.translate("Form", u"new device", None))
        self.pushButton_close.setText("")
        self.tip_light_label.setText("")
        self.address_label.setText("")
        self.setting_button.setText(QCoreApplication.translate("Form", u"Setting", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi


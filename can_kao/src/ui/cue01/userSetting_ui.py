# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userSetting.ui'
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

from src.components.ClearableLineEdit import ClearableLineEdit
from src.components.CustomComboBox import CustomComboBox

class Ui_CUE01_User_Setting_Form(object):
    def setupUi(self, CUE01_User_Setting_Form):
        if not CUE01_User_Setting_Form.objectName():
            CUE01_User_Setting_Form.setObjectName(u"CUE01_User_Setting_Form")
        CUE01_User_Setting_Form.resize(800, 500)
        self.verticalLayout_2 = QVBoxLayout(CUE01_User_Setting_Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(CUE01_User_Setting_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit_current_user = ClearableLineEdit(CUE01_User_Setting_Form)
        self.lineEdit_current_user.setObjectName(u"lineEdit_current_user")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_current_user.sizePolicy().hasHeightForWidth())
        self.lineEdit_current_user.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.lineEdit_current_user)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(18)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(CUE01_User_Setting_Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.comboBox_current_user = CustomComboBox(CUE01_User_Setting_Form)
        self.comboBox_current_user.setObjectName(u"comboBox_current_user")

        self.horizontalLayout_4.addWidget(self.comboBox_current_user)

        self.pushButton_switch_user = QPushButton(CUE01_User_Setting_Form)
        self.pushButton_switch_user.setObjectName(u"pushButton_switch_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_switch_user.sizePolicy().hasHeightForWidth())
        self.pushButton_switch_user.setSizePolicy(sizePolicy1)
        self.pushButton_switch_user.setMinimumSize(QSize(60, 0))
        self.pushButton_switch_user.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_switch_user)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(CUE01_User_Setting_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.pushButton_import = QPushButton(CUE01_User_Setting_Form)
        self.pushButton_import.setObjectName(u"pushButton_import")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_import.sizePolicy().hasHeightForWidth())
        self.pushButton_import.setSizePolicy(sizePolicy2)
        self.pushButton_import.setMinimumSize(QSize(120, 0))
        self.pushButton_import.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_import)

        self.pushButton_export = QPushButton(CUE01_User_Setting_Form)
        self.pushButton_export.setObjectName(u"pushButton_export")
        sizePolicy2.setHeightForWidth(self.pushButton_export.sizePolicy().hasHeightForWidth())
        self.pushButton_export.setSizePolicy(sizePolicy2)
        self.pushButton_export.setMinimumSize(QSize(120, 0))
        self.pushButton_export.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_export)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(18)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(CUE01_User_Setting_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))
        self.label_4.setMaximumSize(QSize(120, 16777215))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.pushButton_delete_user = QPushButton(CUE01_User_Setting_Form)
        self.pushButton_delete_user.setObjectName(u"pushButton_delete_user")
        sizePolicy2.setHeightForWidth(self.pushButton_delete_user.sizePolicy().hasHeightForWidth())
        self.pushButton_delete_user.setSizePolicy(sizePolicy2)
        self.pushButton_delete_user.setMinimumSize(QSize(120, 0))
        self.pushButton_delete_user.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_delete_user)

        self.pushButton_add_user = QPushButton(CUE01_User_Setting_Form)
        self.pushButton_add_user.setObjectName(u"pushButton_add_user")
        sizePolicy2.setHeightForWidth(self.pushButton_add_user.sizePolicy().hasHeightForWidth())
        self.pushButton_add_user.setSizePolicy(sizePolicy2)
        self.pushButton_add_user.setMinimumSize(QSize(120, 0))
        self.pushButton_add_user.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_add_user)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.retranslateUi(CUE01_User_Setting_Form)

        QMetaObject.connectSlotsByName(CUE01_User_Setting_Form)
    # setupUi

    def retranslateUi(self, CUE01_User_Setting_Form):
        CUE01_User_Setting_Form.setWindowTitle(QCoreApplication.translate("CUE01_User_Setting_Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_User_Setting_Form", u"Current User:", None))
        self.label.setText(QCoreApplication.translate("CUE01_User_Setting_Form", u"User List:", None))
        self.pushButton_switch_user.setText(QCoreApplication.translate("CUE01_User_Setting_Form", u"Switch", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_User_Setting_Form", u"Conf Operation:", None))
        self.pushButton_import.setText(QCoreApplication.translate("CUE01_User_Setting_Form", u"Import Configuration", None))
        self.pushButton_export.setText(QCoreApplication.translate("CUE01_User_Setting_Form", u"Export Configuration", None))
        self.label_4.setText(QCoreApplication.translate("CUE01_User_Setting_Form", u"User Operatioin:", None))
        self.pushButton_delete_user.setText(QCoreApplication.translate("CUE01_User_Setting_Form", u"Delete Selected User", None))
        self.pushButton_add_user.setText(QCoreApplication.translate("CUE01_User_Setting_Form", u"Create New User", None))
    # retranslateUi


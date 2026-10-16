# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SD1242_4K_Setting.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SD1242_4K_Setting_Form(object):
    def setupUi(self, SD1242_4K_Setting_Form):
        if not SD1242_4K_Setting_Form.objectName():
            SD1242_4K_Setting_Form.setObjectName(u"SD1242_4K_Setting_Form")
        SD1242_4K_Setting_Form.resize(800, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SD1242_4K_Setting_Form.sizePolicy().hasHeightForWidth())
        SD1242_4K_Setting_Form.setSizePolicy(sizePolicy)
        self.layoutWidget = QWidget(SD1242_4K_Setting_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 10, 620, 471))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.device_edid_label = QLabel(self.layoutWidget)
        self.device_edid_label.setObjectName(u"device_edid_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.device_edid_label.setFont(font)

        self.verticalLayout_3.addWidget(self.device_edid_label)

        self.device_edid_plainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.device_edid_plainTextEdit.setObjectName(u"device_edid_plainTextEdit")
        self.device_edid_plainTextEdit.setMinimumSize(QSize(260, 204))
        self.device_edid_plainTextEdit.setMaximumSize(QSize(260, 16777215))
        font1 = QFont()
        font1.setPointSize(7)
        self.device_edid_plainTextEdit.setFont(font1)

        self.verticalLayout_3.addWidget(self.device_edid_plainTextEdit)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.learning_edid_label = QLabel(self.layoutWidget)
        self.learning_edid_label.setObjectName(u"learning_edid_label")
        self.learning_edid_label.setFont(font)
        self.learning_edid_label.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.learning_edid_label)

        self.learning_edid_listWidget = QListWidget(self.layoutWidget)
        self.learning_edid_listWidget.setObjectName(u"learning_edid_listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(120)
        sizePolicy1.setHeightForWidth(self.learning_edid_listWidget.sizePolicy().hasHeightForWidth())
        self.learning_edid_listWidget.setSizePolicy(sizePolicy1)
        self.learning_edid_listWidget.setMaximumSize(QSize(260, 120))
        font2 = QFont()
        font2.setPointSize(14)
        self.learning_edid_listWidget.setFont(font2)
        self.learning_edid_listWidget.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.learning_edid_listWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.presaved_edid_label = QLabel(self.layoutWidget)
        self.presaved_edid_label.setObjectName(u"presaved_edid_label")
        self.presaved_edid_label.setFont(font)
        self.presaved_edid_label.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.presaved_edid_label)

        self.presaved_edid_listWidget = QListWidget(self.layoutWidget)
        self.presaved_edid_listWidget.setObjectName(u"presaved_edid_listWidget")
        sizePolicy1.setHeightForWidth(self.presaved_edid_listWidget.sizePolicy().hasHeightForWidth())
        self.presaved_edid_listWidget.setSizePolicy(sizePolicy1)
        self.presaved_edid_listWidget.setMaximumSize(QSize(260, 120))
        self.presaved_edid_listWidget.setFont(font2)
        self.presaved_edid_listWidget.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.presaved_edid_listWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.delete_pushButton = QPushButton(self.layoutWidget)
        self.delete_pushButton.setObjectName(u"delete_pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.delete_pushButton.sizePolicy().hasHeightForWidth())
        self.delete_pushButton.setSizePolicy(sizePolicy2)
        self.delete_pushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.delete_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.export_pushButton = QPushButton(self.layoutWidget)
        self.export_pushButton.setObjectName(u"export_pushButton")
        self.export_pushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.export_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.import_pushButton = QPushButton(self.layoutWidget)
        self.import_pushButton.setObjectName(u"import_pushButton")
        self.import_pushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.import_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SD1242_4K_Setting_Form)

        QMetaObject.connectSlotsByName(SD1242_4K_Setting_Form)
    # setupUi

    def retranslateUi(self, SD1242_4K_Setting_Form):
        SD1242_4K_Setting_Form.setWindowTitle(QCoreApplication.translate("SD1242_4K_Setting_Form", u"Form", None))
        self.device_edid_label.setText(QCoreApplication.translate("SD1242_4K_Setting_Form", u"<html><head/><body><p align=\"center\">Device EDID</p></body></html>", None))
        self.device_edid_plainTextEdit.setPlainText("")
        self.learning_edid_label.setText(QCoreApplication.translate("SD1242_4K_Setting_Form", u"<html><head/><body><p align=\"center\">Learning EDID</p></body></html>", None))
        self.presaved_edid_label.setText(QCoreApplication.translate("SD1242_4K_Setting_Form", u"<html><head/><body><p align=\"center\">Pre-Saved EDID</p></body></html>", None))
        self.delete_pushButton.setText(QCoreApplication.translate("SD1242_4K_Setting_Form", u"Delete", None))
        self.export_pushButton.setText(QCoreApplication.translate("SD1242_4K_Setting_Form", u"Export", None))
        self.import_pushButton.setText(QCoreApplication.translate("SD1242_4K_Setting_Form", u"Import", None))
    # retranslateUi


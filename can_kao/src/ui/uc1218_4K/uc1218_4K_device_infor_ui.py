# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uc1218_4K_device_infor.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_UC1218_4K_Device_Infor_Form(object):
    def setupUi(self, UC1218_4K_Device_Infor_Form):
        if not UC1218_4K_Device_Infor_Form.objectName():
            UC1218_4K_Device_Infor_Form.setObjectName(u"UC1218_4K_Device_Infor_Form")
        UC1218_4K_Device_Infor_Form.resize(800, 500)
        self.layoutWidget = QWidget(UC1218_4K_Device_Infor_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(190, 60, 411, 261))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.productNameValue_label = QLabel(self.layoutWidget)
        self.productNameValue_label.setObjectName(u"productNameValue_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productNameValue_label.sizePolicy().hasHeightForWidth())
        self.productNameValue_label.setSizePolicy(sizePolicy)
        self.productNameValue_label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_9.addWidget(self.productNameValue_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.productName_label = QLabel(self.layoutWidget)
        self.productName_label.setObjectName(u"productName_label")

        self.horizontalLayout_5.addWidget(self.productName_label)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, -1, -1, -1)
        self.uacNameValue_label = QLabel(self.layoutWidget)
        self.uacNameValue_label.setObjectName(u"uacNameValue_label")
        sizePolicy.setHeightForWidth(self.uacNameValue_label.sizePolicy().hasHeightForWidth())
        self.uacNameValue_label.setSizePolicy(sizePolicy)
        self.uacNameValue_label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_7.addWidget(self.uacNameValue_label)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.uvcNameValue_label = QLabel(self.layoutWidget)
        self.uvcNameValue_label.setObjectName(u"uvcNameValue_label")
        sizePolicy.setHeightForWidth(self.uvcNameValue_label.sizePolicy().hasHeightForWidth())
        self.uvcNameValue_label.setSizePolicy(sizePolicy)
        self.uvcNameValue_label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_8.addWidget(self.uvcNameValue_label)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.version_label = QLabel(self.layoutWidget)
        self.version_label.setObjectName(u"version_label")

        self.horizontalLayout.addWidget(self.version_label)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.inputVideo_infor_label = QLabel(self.layoutWidget)
        self.inputVideo_infor_label.setObjectName(u"inputVideo_infor_label")
        sizePolicy.setHeightForWidth(self.inputVideo_infor_label.sizePolicy().hasHeightForWidth())
        self.inputVideo_infor_label.setSizePolicy(sizePolicy)
        self.inputVideo_infor_label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_10.addWidget(self.inputVideo_infor_label)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)


        self.gridLayout.addLayout(self.horizontalLayout_10, 3, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.uvcName_label = QLabel(self.layoutWidget)
        self.uvcName_label.setObjectName(u"uvcName_label")

        self.horizontalLayout_4.addWidget(self.uvcName_label)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.uacName_label = QLabel(self.layoutWidget)
        self.uacName_label.setObjectName(u"uacName_label")

        self.horizontalLayout_3.addWidget(self.uacName_label)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, -1, -1)
        self.versionValue_label = QLabel(self.layoutWidget)
        self.versionValue_label.setObjectName(u"versionValue_label")
        sizePolicy.setHeightForWidth(self.versionValue_label.sizePolicy().hasHeightForWidth())
        self.versionValue_label.setSizePolicy(sizePolicy)
        self.versionValue_label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.versionValue_label)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.inputVideo_label = QLabel(self.layoutWidget)
        self.inputVideo_label.setObjectName(u"inputVideo_label")

        self.horizontalLayout_2.addWidget(self.inputVideo_label)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.reset_label = QLabel(self.layoutWidget)
        self.reset_label.setObjectName(u"reset_label")

        self.horizontalLayout_11.addWidget(self.reset_label)


        self.gridLayout.addLayout(self.horizontalLayout_11, 5, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, -1, -1, -1)
        self.factoryReset_pushButton = QPushButton(self.layoutWidget)
        self.factoryReset_pushButton.setObjectName(u"factoryReset_pushButton")
        self.factoryReset_pushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_12.addWidget(self.factoryReset_pushButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.gridLayout.addLayout(self.horizontalLayout_12, 5, 1, 1, 1)


        self.retranslateUi(UC1218_4K_Device_Infor_Form)

        QMetaObject.connectSlotsByName(UC1218_4K_Device_Infor_Form)
    # setupUi

    def retranslateUi(self, UC1218_4K_Device_Infor_Form):
        UC1218_4K_Device_Infor_Form.setWindowTitle(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"Form", None))
        self.productNameValue_label.setText("")
        self.productName_label.setText(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"Product Name", None))
        self.uacNameValue_label.setText("")
        self.uvcNameValue_label.setText("")
        self.version_label.setText(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"Version", None))
        self.inputVideo_infor_label.setText("")
        self.uvcName_label.setText(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"UVC Name", None))
        self.uacName_label.setText(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"UAC Name", None))
        self.versionValue_label.setText("")
        self.inputVideo_label.setText(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"Input Video", None))
        self.reset_label.setText(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"Factory Reset", None))
        self.factoryReset_pushButton.setText(QCoreApplication.translate("UC1218_4K_Device_Infor_Form", u"Reset", None))
    # retranslateUi


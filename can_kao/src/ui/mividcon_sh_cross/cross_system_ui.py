# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cross_system.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Cross_System_Form(object):
    def setupUi(self, Cross_System_Form):
        if not Cross_System_Form.objectName():
            Cross_System_Form.setObjectName(u"Cross_System_Form")
        Cross_System_Form.resize(800, 500)
        self.layoutWidget = QWidget(Cross_System_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 80, 551, 228))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.lcdOffTime_comboBox = QComboBox(self.layoutWidget)
        self.lcdOffTime_comboBox.setObjectName(u"lcdOffTime_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdOffTime_comboBox.sizePolicy().hasHeightForWidth())
        self.lcdOffTime_comboBox.setSizePolicy(sizePolicy)
        self.lcdOffTime_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_10.addWidget(self.lcdOffTime_comboBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.back2StatusTime_label = QLabel(self.layoutWidget)
        self.back2StatusTime_label.setObjectName(u"back2StatusTime_label")

        self.horizontalLayout_4.addWidget(self.back2StatusTime_label)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, -1, -1, -1)
        self.factoryReset_pushButton = QPushButton(self.layoutWidget)
        self.factoryReset_pushButton.setObjectName(u"factoryReset_pushButton")
        self.factoryReset_pushButton.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_13.addWidget(self.factoryReset_pushButton)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.gridLayout.addLayout(self.horizontalLayout_13, 5, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.language_label = QLabel(self.layoutWidget)
        self.language_label.setObjectName(u"language_label")

        self.horizontalLayout_5.addWidget(self.language_label)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.noSignalIndicator_label = QLabel(self.layoutWidget)
        self.noSignalIndicator_label.setObjectName(u"noSignalIndicator_label")

        self.horizontalLayout_2.addWidget(self.noSignalIndicator_label)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, -1, -1, -1)
        self.language_comboBox = QComboBox(self.layoutWidget)
        self.language_comboBox.setObjectName(u"language_comboBox")
        sizePolicy.setHeightForWidth(self.language_comboBox.sizePolicy().hasHeightForWidth())
        self.language_comboBox.setSizePolicy(sizePolicy)
        self.language_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_12.addWidget(self.language_comboBox)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.gridLayout.addLayout(self.horizontalLayout_12, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.scalerRef_label = QLabel(self.layoutWidget)
        self.scalerRef_label.setObjectName(u"scalerRef_label")

        self.horizontalLayout.addWidget(self.scalerRef_label)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.version_label = QLabel(self.layoutWidget)
        self.version_label.setObjectName(u"version_label")

        self.horizontalLayout_7.addWidget(self.version_label)


        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.factoryReset_label = QLabel(self.layoutWidget)
        self.factoryReset_label.setObjectName(u"factoryReset_label")

        self.horizontalLayout_6.addWidget(self.factoryReset_label)


        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, -1, -1, -1)
        self.back2StatusTime_comboBox = QComboBox(self.layoutWidget)
        self.back2StatusTime_comboBox.setObjectName(u"back2StatusTime_comboBox")
        sizePolicy.setHeightForWidth(self.back2StatusTime_comboBox.sizePolicy().hasHeightForWidth())
        self.back2StatusTime_comboBox.setSizePolicy(sizePolicy)
        self.back2StatusTime_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_11.addWidget(self.back2StatusTime_comboBox)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.gridLayout.addLayout(self.horizontalLayout_11, 3, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.noSignalIndicator_comboBox = QComboBox(self.layoutWidget)
        self.noSignalIndicator_comboBox.setObjectName(u"noSignalIndicator_comboBox")
        sizePolicy.setHeightForWidth(self.noSignalIndicator_comboBox.sizePolicy().hasHeightForWidth())
        self.noSignalIndicator_comboBox.setSizePolicy(sizePolicy)
        self.noSignalIndicator_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_9.addWidget(self.noSignalIndicator_comboBox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.lcdOffTime_label = QLabel(self.layoutWidget)
        self.lcdOffTime_label.setObjectName(u"lcdOffTime_label")

        self.horizontalLayout_3.addWidget(self.lcdOffTime_label)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, -1, -1, -1)
        self.versionValue_label = QLabel(self.layoutWidget)
        self.versionValue_label.setObjectName(u"versionValue_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.versionValue_label.sizePolicy().hasHeightForWidth())
        self.versionValue_label.setSizePolicy(sizePolicy1)
        self.versionValue_label.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_14.addWidget(self.versionValue_label)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)


        self.gridLayout.addLayout(self.horizontalLayout_14, 6, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.scalerRef_comboBox = QComboBox(self.layoutWidget)
        self.scalerRef_comboBox.setObjectName(u"scalerRef_comboBox")
        sizePolicy.setHeightForWidth(self.scalerRef_comboBox.sizePolicy().hasHeightForWidth())
        self.scalerRef_comboBox.setSizePolicy(sizePolicy)
        self.scalerRef_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_8.addWidget(self.scalerRef_comboBox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)


        self.gridLayout.addLayout(self.horizontalLayout_15, 7, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(20, -1, -1, -1)
        self.versionValue_label2 = QLabel(self.layoutWidget)
        self.versionValue_label2.setObjectName(u"versionValue_label2")
        sizePolicy1.setHeightForWidth(self.versionValue_label2.sizePolicy().hasHeightForWidth())
        self.versionValue_label2.setSizePolicy(sizePolicy1)
        self.versionValue_label2.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_16.addWidget(self.versionValue_label2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)


        self.gridLayout.addLayout(self.horizontalLayout_16, 7, 1, 1, 1)


        self.retranslateUi(Cross_System_Form)

        QMetaObject.connectSlotsByName(Cross_System_Form)
    # setupUi

    def retranslateUi(self, Cross_System_Form):
        Cross_System_Form.setWindowTitle(QCoreApplication.translate("Cross_System_Form", u"Form", None))
        self.back2StatusTime_label.setText(QCoreApplication.translate("Cross_System_Form", u"Back2Status", None))
        self.factoryReset_pushButton.setText(QCoreApplication.translate("Cross_System_Form", u"Reset", None))
        self.language_label.setText(QCoreApplication.translate("Cross_System_Form", u"Language", None))
        self.noSignalIndicator_label.setText(QCoreApplication.translate("Cross_System_Form", u"No Signal Indicator", None))
        self.scalerRef_label.setText(QCoreApplication.translate("Cross_System_Form", u"Scaler REF", None))
        self.version_label.setText(QCoreApplication.translate("Cross_System_Form", u"Version", None))
        self.factoryReset_label.setText(QCoreApplication.translate("Cross_System_Form", u"Factory Reset", None))
        self.lcdOffTime_label.setText(QCoreApplication.translate("Cross_System_Form", u"LCD Off", None))
        self.versionValue_label.setText(QCoreApplication.translate("Cross_System_Form", u"Version", None))
        self.versionValue_label2.setText(QCoreApplication.translate("Cross_System_Form", u"Version", None))
    # retranslateUi


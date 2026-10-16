# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cross_output.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Cross_Output_Form(object):
    def setupUi(self, Cross_Output_Form):
        if not Cross_Output_Form.objectName():
            Cross_Output_Form.setObjectName(u"Cross_Output_Form")
        Cross_Output_Form.resize(800, 500)
        self.layoutWidget = QWidget(Cross_Output_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 100, 711, 271))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.hdmiOutSrc_label_2 = QLabel(self.layoutWidget)
        self.hdmiOutSrc_label_2.setObjectName(u"hdmiOutSrc_label_2")

        self.horizontalLayout_11.addWidget(self.hdmiOutSrc_label_2)


        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, -1, -1, -1)
        self.sfp_radioButton = QRadioButton(self.layoutWidget)
        self.sdi_sfp_buttonGroup = QButtonGroup(Cross_Output_Form)
        self.sdi_sfp_buttonGroup.setObjectName(u"sdi_sfp_buttonGroup")
        self.sdi_sfp_buttonGroup.addButton(self.sfp_radioButton)
        self.sfp_radioButton.setObjectName(u"sfp_radioButton")
        self.sfp_radioButton.setEnabled(True)
        self.sfp_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_12.addWidget(self.sfp_radioButton)

        self.sdi_in_radioButton = QRadioButton(self.layoutWidget)
        self.sdi_sfp_buttonGroup.addButton(self.sdi_in_radioButton)
        self.sdi_in_radioButton.setObjectName(u"sdi_in_radioButton")
        self.sdi_in_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_12.addWidget(self.sdi_in_radioButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.hdmiOutSrc_label = QLabel(self.layoutWidget)
        self.hdmiOutSrc_label.setObjectName(u"hdmiOutSrc_label")

        self.horizontalLayout_6.addWidget(self.hdmiOutSrc_label)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.hdmiOutSrc_sdiIn_radioButton = QRadioButton(self.layoutWidget)
        self.hdmiOutSrc_buttonGroup = QButtonGroup(Cross_Output_Form)
        self.hdmiOutSrc_buttonGroup.setObjectName(u"hdmiOutSrc_buttonGroup")
        self.hdmiOutSrc_buttonGroup.addButton(self.hdmiOutSrc_sdiIn_radioButton)
        self.hdmiOutSrc_sdiIn_radioButton.setObjectName(u"hdmiOutSrc_sdiIn_radioButton")
        self.hdmiOutSrc_sdiIn_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.hdmiOutSrc_sdiIn_radioButton)

        self.hdmiOutSrc_hdmiIn_radioButton = QRadioButton(self.layoutWidget)
        self.hdmiOutSrc_buttonGroup.addButton(self.hdmiOutSrc_hdmiIn_radioButton)
        self.hdmiOutSrc_hdmiIn_radioButton.setObjectName(u"hdmiOutSrc_hdmiIn_radioButton")
        self.hdmiOutSrc_hdmiIn_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.hdmiOutSrc_hdmiIn_radioButton)

        self.hdmiOutSrc_scaler_radioButton = QRadioButton(self.layoutWidget)
        self.hdmiOutSrc_buttonGroup.addButton(self.hdmiOutSrc_scaler_radioButton)
        self.hdmiOutSrc_scaler_radioButton.setObjectName(u"hdmiOutSrc_scaler_radioButton")
        self.hdmiOutSrc_scaler_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.hdmiOutSrc_scaler_radioButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.scalerSrc_label = QLabel(self.layoutWidget)
        self.scalerSrc_label.setObjectName(u"scalerSrc_label")

        self.horizontalLayout_8.addWidget(self.scalerSrc_label)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.sdiOutSrc_label = QLabel(self.layoutWidget)
        self.sdiOutSrc_label.setObjectName(u"sdiOutSrc_label")

        self.horizontalLayout_7.addWidget(self.sdiOutSrc_label)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.sdiOutSrc_sdiIn_radioButton = QRadioButton(self.layoutWidget)
        self.sdiOutSrc_buttonGroup = QButtonGroup(Cross_Output_Form)
        self.sdiOutSrc_buttonGroup.setObjectName(u"sdiOutSrc_buttonGroup")
        self.sdiOutSrc_buttonGroup.addButton(self.sdiOutSrc_sdiIn_radioButton)
        self.sdiOutSrc_sdiIn_radioButton.setObjectName(u"sdiOutSrc_sdiIn_radioButton")
        self.sdiOutSrc_sdiIn_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.sdiOutSrc_sdiIn_radioButton)

        self.sdiOutSrc_hdmiIn_radioButton = QRadioButton(self.layoutWidget)
        self.sdiOutSrc_buttonGroup.addButton(self.sdiOutSrc_hdmiIn_radioButton)
        self.sdiOutSrc_hdmiIn_radioButton.setObjectName(u"sdiOutSrc_hdmiIn_radioButton")
        self.sdiOutSrc_hdmiIn_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.sdiOutSrc_hdmiIn_radioButton)

        self.sdiOutSrc_scaler_radioButton = QRadioButton(self.layoutWidget)
        self.sdiOutSrc_buttonGroup.addButton(self.sdiOutSrc_scaler_radioButton)
        self.sdiOutSrc_scaler_radioButton.setObjectName(u"sdiOutSrc_scaler_radioButton")
        self.sdiOutSrc_scaler_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.sdiOutSrc_scaler_radioButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.scalerSrc_sdiIn_radioButton = QRadioButton(self.layoutWidget)
        self.scalerSrc_buttonGroup = QButtonGroup(Cross_Output_Form)
        self.scalerSrc_buttonGroup.setObjectName(u"scalerSrc_buttonGroup")
        self.scalerSrc_buttonGroup.addButton(self.scalerSrc_sdiIn_radioButton)
        self.scalerSrc_sdiIn_radioButton.setObjectName(u"scalerSrc_sdiIn_radioButton")
        self.scalerSrc_sdiIn_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.scalerSrc_sdiIn_radioButton)

        self.scalerSrc_hdmiIn_radioButton = QRadioButton(self.layoutWidget)
        self.scalerSrc_buttonGroup.addButton(self.scalerSrc_hdmiIn_radioButton)
        self.scalerSrc_hdmiIn_radioButton.setObjectName(u"scalerSrc_hdmiIn_radioButton")
        self.scalerSrc_hdmiIn_radioButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.scalerSrc_hdmiIn_radioButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)


        self.retranslateUi(Cross_Output_Form)

        QMetaObject.connectSlotsByName(Cross_Output_Form)
    # setupUi

    def retranslateUi(self, Cross_Output_Form):
        Cross_Output_Form.setWindowTitle(QCoreApplication.translate("Cross_Output_Form", u"Form", None))
        self.hdmiOutSrc_label_2.setText(QCoreApplication.translate("Cross_Output_Form", u"SDI/SFP In", None))
        self.sfp_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"SFP In", None))
        self.sdi_in_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"SDI In", None))
        self.hdmiOutSrc_label.setText(QCoreApplication.translate("Cross_Output_Form", u"HDMI Out Source", None))
        self.hdmiOutSrc_sdiIn_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"SDI In", None))
        self.hdmiOutSrc_hdmiIn_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"HDMI In", None))
        self.hdmiOutSrc_scaler_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"Scaler", None))
        self.scalerSrc_label.setText(QCoreApplication.translate("Cross_Output_Form", u"Scaler Source", None))
        self.sdiOutSrc_label.setText(QCoreApplication.translate("Cross_Output_Form", u"SDI Out Source", None))
        self.sdiOutSrc_sdiIn_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"SDI In", None))
        self.sdiOutSrc_hdmiIn_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"HDMI In", None))
        self.sdiOutSrc_scaler_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"Scaler", None))
        self.scalerSrc_sdiIn_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"SDI In", None))
        self.scalerSrc_hdmiIn_radioButton.setText(QCoreApplication.translate("Cross_Output_Form", u"HDMI In", None))
    # retranslateUi


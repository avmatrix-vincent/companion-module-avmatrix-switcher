# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uc1218_4K_video_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_UC1218_4K_Video_Setting_Form(object):
    def setupUi(self, UC1218_4K_Video_Setting_Form):
        if not UC1218_4K_Video_Setting_Form.objectName():
            UC1218_4K_Video_Setting_Form.setObjectName(u"UC1218_4K_Video_Setting_Form")
        UC1218_4K_Video_Setting_Form.resize(800, 500)
        self.layoutWidget = QWidget(UC1218_4K_Video_Setting_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 60, 651, 91))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.set_colorRange_label = QLabel(self.layoutWidget)
        self.set_colorRange_label.setObjectName(u"set_colorRange_label")

        self.horizontalLayout_12.addWidget(self.set_colorRange_label)


        self.gridLayout_2.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 20, -1)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.colorRange_label = QLabel(self.layoutWidget)
        self.colorRange_label.setObjectName(u"colorRange_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorRange_label.sizePolicy().hasHeightForWidth())
        self.colorRange_label.setSizePolicy(sizePolicy)
        self.colorRange_label.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_15.addWidget(self.colorRange_label)


        self.gridLayout_2.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, -1, -1, -1)
        self.set_colorRange_bypass_radioButton = QRadioButton(self.layoutWidget)
        self.rgb2yuv_colorRange_buttonGroup = QButtonGroup(UC1218_4K_Video_Setting_Form)
        self.rgb2yuv_colorRange_buttonGroup.setObjectName(u"rgb2yuv_colorRange_buttonGroup")
        self.rgb2yuv_colorRange_buttonGroup.addButton(self.set_colorRange_bypass_radioButton)
        self.set_colorRange_bypass_radioButton.setObjectName(u"set_colorRange_bypass_radioButton")

        self.horizontalLayout_14.addWidget(self.set_colorRange_bypass_radioButton)

        self.set_colorRange_limitedRange_radioButton = QRadioButton(self.layoutWidget)
        self.rgb2yuv_colorRange_buttonGroup.addButton(self.set_colorRange_limitedRange_radioButton)
        self.set_colorRange_limitedRange_radioButton.setObjectName(u"set_colorRange_limitedRange_radioButton")

        self.horizontalLayout_14.addWidget(self.set_colorRange_limitedRange_radioButton)

        self.set_colorRange_fullRange_radioButton = QRadioButton(self.layoutWidget)
        self.rgb2yuv_colorRange_buttonGroup.addButton(self.set_colorRange_fullRange_radioButton)
        self.set_colorRange_fullRange_radioButton.setObjectName(u"set_colorRange_fullRange_radioButton")

        self.horizontalLayout_14.addWidget(self.set_colorRange_fullRange_radioButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)


        self.gridLayout_2.addLayout(self.horizontalLayout_14, 1, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(20, -1, -1, -1)
        self.colorRange_value_label = QLabel(self.layoutWidget)
        self.colorRange_value_label.setObjectName(u"colorRange_value_label")
        sizePolicy.setHeightForWidth(self.colorRange_value_label.sizePolicy().hasHeightForWidth())
        self.colorRange_value_label.setSizePolicy(sizePolicy)
        self.colorRange_value_label.setMinimumSize(QSize(130, 30))

        self.horizontalLayout_16.addWidget(self.colorRange_value_label)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)


        self.gridLayout_2.addLayout(self.horizontalLayout_16, 0, 1, 1, 1)


        self.retranslateUi(UC1218_4K_Video_Setting_Form)

        QMetaObject.connectSlotsByName(UC1218_4K_Video_Setting_Form)
    # setupUi

    def retranslateUi(self, UC1218_4K_Video_Setting_Form):
        UC1218_4K_Video_Setting_Form.setWindowTitle(QCoreApplication.translate("UC1218_4K_Video_Setting_Form", u"Form", None))
        self.set_colorRange_label.setText(QCoreApplication.translate("UC1218_4K_Video_Setting_Form", u"Set Color Range", None))
        self.colorRange_label.setText(QCoreApplication.translate("UC1218_4K_Video_Setting_Form", u"Color Range Status", None))
        self.set_colorRange_bypass_radioButton.setText(QCoreApplication.translate("UC1218_4K_Video_Setting_Form", u"Bypass", None))
        self.set_colorRange_limitedRange_radioButton.setText(QCoreApplication.translate("UC1218_4K_Video_Setting_Form", u"Limited Range", None))
        self.set_colorRange_fullRange_radioButton.setText(QCoreApplication.translate("UC1218_4K_Video_Setting_Form", u"Full Range", None))
        self.colorRange_value_label.setText(QCoreApplication.translate("UC1218_4K_Video_Setting_Form", u"Limited Range", None))
    # retranslateUi


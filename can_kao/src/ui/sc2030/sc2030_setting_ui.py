# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sc2030_setting.ui'
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
from src.components.CustomComboBox import CustomComboBox

class Ui_SC2030_Setting_Form(object):
    def setupUi(self, SC2030_Setting_Form):
        if not SC2030_Setting_Form.objectName():
            SC2030_Setting_Form.setObjectName(u"SC2030_Setting_Form")
        SC2030_Setting_Form.resize(800, 500)
        self.verticalLayout = QVBoxLayout(SC2030_Setting_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(18)
        self.gridLayout.setVerticalSpacing(20)
        self.lineEdit_custom = ClearableLineEdit(SC2030_Setting_Form)
        self.lineEdit_custom.setObjectName(u"lineEdit_custom")

        self.gridLayout.addWidget(self.lineEdit_custom, 0, 1, 1, 1)

        self.label_6 = QLabel(SC2030_Setting_Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.comboBox_scaling = CustomComboBox(SC2030_Setting_Form)
        self.comboBox_scaling.setObjectName(u"comboBox_scaling")

        self.gridLayout.addWidget(self.comboBox_scaling, 3, 1, 1, 1)

        self.label_4 = QLabel(SC2030_Setting_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_fw_ver = ClearableLineEdit(SC2030_Setting_Form)
        self.lineEdit_fw_ver.setObjectName(u"lineEdit_fw_ver")

        self.gridLayout.addWidget(self.lineEdit_fw_ver, 1, 1, 1, 1)

        self.comboBox_aspect_ratio = CustomComboBox(SC2030_Setting_Form)
        self.comboBox_aspect_ratio.setObjectName(u"comboBox_aspect_ratio")

        self.gridLayout.addWidget(self.comboBox_aspect_ratio, 6, 1, 1, 1)

        self.label_2 = QLabel(SC2030_Setting_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(SC2030_Setting_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.pushButton_save = QPushButton(SC2030_Setting_Form)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.gridLayout.addWidget(self.pushButton_save, 0, 2, 1, 1)

        self.label_7 = QLabel(SC2030_Setting_Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.comboBox_audio = CustomComboBox(SC2030_Setting_Form)
        self.comboBox_audio.setObjectName(u"comboBox_audio")

        self.gridLayout.addWidget(self.comboBox_audio, 5, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 6, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.comboBox_source = CustomComboBox(SC2030_Setting_Form)
        self.comboBox_source.setObjectName(u"comboBox_source")

        self.gridLayout.addWidget(self.comboBox_source, 4, 1, 1, 1)

        self.lineEdit_input_status = ClearableLineEdit(SC2030_Setting_Form)
        self.lineEdit_input_status.setObjectName(u"lineEdit_input_status")

        self.gridLayout.addWidget(self.lineEdit_input_status, 2, 1, 1, 1)

        self.label_5 = QLabel(SC2030_Setting_Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label = QLabel(SC2030_Setting_Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 131, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(SC2030_Setting_Form)

        QMetaObject.connectSlotsByName(SC2030_Setting_Form)
    # setupUi

    def retranslateUi(self, SC2030_Setting_Form):
        SC2030_Setting_Form.setWindowTitle(QCoreApplication.translate("SC2030_Setting_Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("SC2030_Setting_Form", u"Audio", None))
        self.label_4.setText(QCoreApplication.translate("SC2030_Setting_Form", u"Scaling", None))
        self.label_2.setText(QCoreApplication.translate("SC2030_Setting_Form", u"Firmware Version", None))
        self.label_3.setText(QCoreApplication.translate("SC2030_Setting_Form", u"Input Status", None))
        self.pushButton_save.setText(QCoreApplication.translate("SC2030_Setting_Form", u"Save", None))
        self.label_7.setText(QCoreApplication.translate("SC2030_Setting_Form", u"Aspect Ratio", None))
        self.label_5.setText(QCoreApplication.translate("SC2030_Setting_Form", u"Source", None))
        self.label.setText(QCoreApplication.translate("SC2030_Setting_Form", u"Custom", None))
    # retranslateUi


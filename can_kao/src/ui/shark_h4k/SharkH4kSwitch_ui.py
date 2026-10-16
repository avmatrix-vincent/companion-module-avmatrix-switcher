# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SharkH4kSwitch.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_SharkH4kSwitch_Form(object):
    def setupUi(self, SharkH4kSwitch_Form):
        if not SharkH4kSwitch_Form.objectName():
            SharkH4kSwitch_Form.setObjectName(u"SharkH4kSwitch_Form")
        SharkH4kSwitch_Form.resize(800, 500)
        self.pgm_pvw_cut_pushButton = QPushButton(SharkH4kSwitch_Form)
        self.pgm_pvw_cut_pushButton.setObjectName(u"pgm_pvw_cut_pushButton")
        self.pgm_pvw_cut_pushButton.setGeometry(QRect(650, 340, 80, 80))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pgm_pvw_cut_pushButton.sizePolicy().hasHeightForWidth())
        self.pgm_pvw_cut_pushButton.setSizePolicy(sizePolicy)
        self.pgm_pvw_cut_pushButton.setMinimumSize(QSize(80, 80))
        self.pgm_pvw_cut_pushButton.setMaximumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pgm_pvw_cut_pushButton.setFont(font)
        self.mv_onoff_checkBox = QCheckBox(SharkH4kSwitch_Form)
        self.mv_onoff_checkBox.setObjectName(u"mv_onoff_checkBox")
        self.mv_onoff_checkBox.setGeometry(QRect(140, 60, 150, 30))
        sizePolicy.setHeightForWidth(self.mv_onoff_checkBox.sizePolicy().hasHeightForWidth())
        self.mv_onoff_checkBox.setSizePolicy(sizePolicy)
        self.mv_onoff_checkBox.setMinimumSize(QSize(150, 30))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.mv_onoff_checkBox.setFont(font1)
        self.clock_phase_comboBox = QComboBox(SharkH4kSwitch_Form)
        self.clock_phase_comboBox.setObjectName(u"clock_phase_comboBox")
        self.clock_phase_comboBox.setGeometry(QRect(140, 110, 120, 22))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clock_phase_comboBox.sizePolicy().hasHeightForWidth())
        self.clock_phase_comboBox.setSizePolicy(sizePolicy1)
        self.clock_phase_comboBox.setMinimumSize(QSize(120, 0))
        self.mv_onoff_label = QLabel(SharkH4kSwitch_Form)
        self.mv_onoff_label.setObjectName(u"mv_onoff_label")
        self.mv_onoff_label.setGeometry(QRect(0, 60, 120, 30))
        sizePolicy.setHeightForWidth(self.mv_onoff_label.sizePolicy().hasHeightForWidth())
        self.mv_onoff_label.setSizePolicy(sizePolicy)
        self.mv_onoff_label.setMinimumSize(QSize(120, 30))
        self.mv_onoff_label.setMaximumSize(QSize(120, 30))
        self.mv_onoff_label.setFont(font1)
        self.mv_onoff_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(SharkH4kSwitch_Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 110, 120, 30))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(120, 30))
        self.label.setMaximumSize(QSize(120, 30))
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.layoutWidget = QWidget(SharkH4kSwitch_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 390, 577, 81))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pvw_btn_label = QLabel(self.layoutWidget)
        self.pvw_btn_label.setObjectName(u"pvw_btn_label")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.pvw_btn_label.setFont(font2)

        self.horizontalLayout.addWidget(self.pvw_btn_label)

        self.pvw_ch1_pushButton = QPushButton(self.layoutWidget)
        self.pvw_ch1_pushButton.setObjectName(u"pvw_ch1_pushButton")
        sizePolicy.setHeightForWidth(self.pvw_ch1_pushButton.sizePolicy().hasHeightForWidth())
        self.pvw_ch1_pushButton.setSizePolicy(sizePolicy)
        self.pvw_ch1_pushButton.setMinimumSize(QSize(60, 60))
        self.pvw_ch1_pushButton.setMaximumSize(QSize(60, 60))
        self.pvw_ch1_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pvw_ch1_pushButton)

        self.pvw_ch2_pushButton = QPushButton(self.layoutWidget)
        self.pvw_ch2_pushButton.setObjectName(u"pvw_ch2_pushButton")
        sizePolicy.setHeightForWidth(self.pvw_ch2_pushButton.sizePolicy().hasHeightForWidth())
        self.pvw_ch2_pushButton.setSizePolicy(sizePolicy)
        self.pvw_ch2_pushButton.setMaximumSize(QSize(60, 60))
        self.pvw_ch2_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pvw_ch2_pushButton)

        self.pvw_ch3_pushButton = QPushButton(self.layoutWidget)
        self.pvw_ch3_pushButton.setObjectName(u"pvw_ch3_pushButton")
        sizePolicy.setHeightForWidth(self.pvw_ch3_pushButton.sizePolicy().hasHeightForWidth())
        self.pvw_ch3_pushButton.setSizePolicy(sizePolicy)
        self.pvw_ch3_pushButton.setMaximumSize(QSize(60, 60))
        self.pvw_ch3_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pvw_ch3_pushButton)

        self.pvw_ch4_pushButton = QPushButton(self.layoutWidget)
        self.pvw_ch4_pushButton.setObjectName(u"pvw_ch4_pushButton")
        sizePolicy.setHeightForWidth(self.pvw_ch4_pushButton.sizePolicy().hasHeightForWidth())
        self.pvw_ch4_pushButton.setSizePolicy(sizePolicy)
        self.pvw_ch4_pushButton.setMaximumSize(QSize(60, 60))
        self.pvw_ch4_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pvw_ch4_pushButton)

        self.pvw_pattern1_pushButton = QPushButton(self.layoutWidget)
        self.pvw_pattern1_pushButton.setObjectName(u"pvw_pattern1_pushButton")
        sizePolicy.setHeightForWidth(self.pvw_pattern1_pushButton.sizePolicy().hasHeightForWidth())
        self.pvw_pattern1_pushButton.setSizePolicy(sizePolicy)
        self.pvw_pattern1_pushButton.setMaximumSize(QSize(120, 60))
        self.pvw_pattern1_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pvw_pattern1_pushButton)

        self.pvw_pattern2_pushButton = QPushButton(self.layoutWidget)
        self.pvw_pattern2_pushButton.setObjectName(u"pvw_pattern2_pushButton")
        sizePolicy.setHeightForWidth(self.pvw_pattern2_pushButton.sizePolicy().hasHeightForWidth())
        self.pvw_pattern2_pushButton.setSizePolicy(sizePolicy)
        self.pvw_pattern2_pushButton.setMaximumSize(QSize(120, 60))
        self.pvw_pattern2_pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pvw_pattern2_pushButton)

        self.layoutWidget1 = QWidget(SharkH4kSwitch_Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 300, 577, 71))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pgm_btn_label = QLabel(self.layoutWidget1)
        self.pgm_btn_label.setObjectName(u"pgm_btn_label")
        self.pgm_btn_label.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pgm_btn_label)

        self.pgm_ch1_pushButton = QPushButton(self.layoutWidget1)
        self.pgm_ch1_pushButton.setObjectName(u"pgm_ch1_pushButton")
        sizePolicy.setHeightForWidth(self.pgm_ch1_pushButton.sizePolicy().hasHeightForWidth())
        self.pgm_ch1_pushButton.setSizePolicy(sizePolicy)
        self.pgm_ch1_pushButton.setMaximumSize(QSize(60, 60))
        self.pgm_ch1_pushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pgm_ch1_pushButton)

        self.pgm_ch2_pushButton = QPushButton(self.layoutWidget1)
        self.pgm_ch2_pushButton.setObjectName(u"pgm_ch2_pushButton")
        sizePolicy.setHeightForWidth(self.pgm_ch2_pushButton.sizePolicy().hasHeightForWidth())
        self.pgm_ch2_pushButton.setSizePolicy(sizePolicy)
        self.pgm_ch2_pushButton.setMaximumSize(QSize(60, 60))
        self.pgm_ch2_pushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pgm_ch2_pushButton)

        self.pgm_ch3_pushButton = QPushButton(self.layoutWidget1)
        self.pgm_ch3_pushButton.setObjectName(u"pgm_ch3_pushButton")
        sizePolicy.setHeightForWidth(self.pgm_ch3_pushButton.sizePolicy().hasHeightForWidth())
        self.pgm_ch3_pushButton.setSizePolicy(sizePolicy)
        self.pgm_ch3_pushButton.setMaximumSize(QSize(60, 60))
        self.pgm_ch3_pushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pgm_ch3_pushButton)

        self.pgm_ch4_pushButton = QPushButton(self.layoutWidget1)
        self.pgm_ch4_pushButton.setObjectName(u"pgm_ch4_pushButton")
        sizePolicy.setHeightForWidth(self.pgm_ch4_pushButton.sizePolicy().hasHeightForWidth())
        self.pgm_ch4_pushButton.setSizePolicy(sizePolicy)
        self.pgm_ch4_pushButton.setMaximumSize(QSize(60, 60))
        self.pgm_ch4_pushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pgm_ch4_pushButton)

        self.pgm_pattern1_pushButton = QPushButton(self.layoutWidget1)
        self.pgm_pattern1_pushButton.setObjectName(u"pgm_pattern1_pushButton")
        sizePolicy.setHeightForWidth(self.pgm_pattern1_pushButton.sizePolicy().hasHeightForWidth())
        self.pgm_pattern1_pushButton.setSizePolicy(sizePolicy)
        self.pgm_pattern1_pushButton.setMaximumSize(QSize(120, 60))
        self.pgm_pattern1_pushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pgm_pattern1_pushButton)

        self.pgm_pattern2_pushButton = QPushButton(self.layoutWidget1)
        self.pgm_pattern2_pushButton.setObjectName(u"pgm_pattern2_pushButton")
        sizePolicy.setHeightForWidth(self.pgm_pattern2_pushButton.sizePolicy().hasHeightForWidth())
        self.pgm_pattern2_pushButton.setSizePolicy(sizePolicy)
        self.pgm_pattern2_pushButton.setMaximumSize(QSize(120, 60))
        self.pgm_pattern2_pushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pgm_pattern2_pushButton)


        self.retranslateUi(SharkH4kSwitch_Form)

        QMetaObject.connectSlotsByName(SharkH4kSwitch_Form)
    # setupUi

    def retranslateUi(self, SharkH4kSwitch_Form):
        SharkH4kSwitch_Form.setWindowTitle(QCoreApplication.translate("SharkH4kSwitch_Form", u"Form", None))
        self.pgm_pvw_cut_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"Cut", None))
        self.mv_onoff_checkBox.setText("")
        self.mv_onoff_label.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"MV\u5f00\u5173", None))
        self.label.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"\u65f6\u949f\u76f8\u4f4d", None))
        self.pvw_btn_label.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"PVW", None))
        self.pvw_ch1_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"1", None))
        self.pvw_ch2_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"2", None))
        self.pvw_ch3_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"3", None))
        self.pvw_ch4_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"4", None))
        self.pvw_pattern1_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"Pattern1", None))
        self.pvw_pattern2_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"Pattern2", None))
        self.pgm_btn_label.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"PGM", None))
        self.pgm_ch1_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"1", None))
        self.pgm_ch2_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"2", None))
        self.pgm_ch3_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"3", None))
        self.pgm_ch4_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"4", None))
        self.pgm_pattern1_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"Pattern1", None))
        self.pgm_pattern2_pushButton.setText(QCoreApplication.translate("SharkH4kSwitch_Form", u"Pattern2", None))
    # retranslateUi


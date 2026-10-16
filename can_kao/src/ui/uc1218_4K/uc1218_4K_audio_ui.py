# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uc1218_4K_audio.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QWidget)

class Ui_UC1218_4K_Audio_Form(object):
    def setupUi(self, UC1218_4K_Audio_Form):
        if not UC1218_4K_Audio_Form.objectName():
            UC1218_4K_Audio_Form.setObjectName(u"UC1218_4K_Audio_Form")
        UC1218_4K_Audio_Form.resize(800, 500)
        self.widget = QWidget(UC1218_4K_Audio_Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 90, 712, 283))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mic_in_volume_label = QLabel(self.widget)
        self.mic_in_volume_label.setObjectName(u"mic_in_volume_label")
        self.mic_in_volume_label.setMinimumSize(QSize(50, 0))
        font = QFont()
        font.setPointSize(10)
        self.mic_in_volume_label.setFont(font)
        self.mic_in_volume_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.mic_in_volume_label, 4, 0, 1, 1)

        self.mixer_hp_out_hdmi_checkBox = QCheckBox(self.widget)
        self.mixer_hp_out_hdmi_checkBox.setObjectName(u"mixer_hp_out_hdmi_checkBox")
        self.mixer_hp_out_hdmi_checkBox.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.mixer_hp_out_hdmi_checkBox, 1, 4, 1, 1, Qt.AlignHCenter)

        self.mixer_hp_out_pc_checkBox = QCheckBox(self.widget)
        self.mixer_hp_out_pc_checkBox.setObjectName(u"mixer_hp_out_pc_checkBox")
        self.mixer_hp_out_pc_checkBox.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.mixer_hp_out_pc_checkBox, 3, 4, 1, 1, Qt.AlignHCenter)

        self.hdmi_volume_label = QLabel(self.widget)
        self.hdmi_volume_label.setObjectName(u"hdmi_volume_label")
        self.hdmi_volume_label.setMinimumSize(QSize(40, 0))
        self.hdmi_volume_label.setFont(font)
        self.hdmi_volume_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.hdmi_volume_label, 1, 0, 1, 1)

        self.pc_volume_label = QLabel(self.widget)
        self.pc_volume_label.setObjectName(u"pc_volume_label")
        self.pc_volume_label.setMinimumSize(QSize(20, 0))
        self.pc_volume_label.setFont(font)
        self.pc_volume_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.pc_volume_label, 3, 0, 1, 1)

        self.mixer_uac_out_label = QLabel(self.widget)
        self.mixer_uac_out_label.setObjectName(u"mixer_uac_out_label")
        self.mixer_uac_out_label.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.mixer_uac_out_label.setFont(font1)
        self.mixer_uac_out_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mixer_uac_out_label, 0, 3, 1, 1)

        self.mixer_uac_out_pc_in_checkBox = QCheckBox(self.widget)
        self.mixer_uac_out_pc_in_checkBox.setObjectName(u"mixer_uac_out_pc_in_checkBox")
        self.mixer_uac_out_pc_in_checkBox.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.mixer_uac_out_pc_in_checkBox, 3, 3, 1, 1, Qt.AlignHCenter)

        self.hp_out_volume_value_lineEdit = QLineEdit(self.widget)
        self.hp_out_volume_value_lineEdit.setObjectName(u"hp_out_volume_value_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hp_out_volume_value_lineEdit.sizePolicy().hasHeightForWidth())
        self.hp_out_volume_value_lineEdit.setSizePolicy(sizePolicy)
        self.hp_out_volume_value_lineEdit.setMinimumSize(QSize(50, 0))
        self.hp_out_volume_value_lineEdit.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.hp_out_volume_value_lineEdit, 5, 2, 1, 1)

        self.hdmi_volume_value_lineEdit = QLineEdit(self.widget)
        self.hdmi_volume_value_lineEdit.setObjectName(u"hdmi_volume_value_lineEdit")
        sizePolicy.setHeightForWidth(self.hdmi_volume_value_lineEdit.sizePolicy().hasHeightForWidth())
        self.hdmi_volume_value_lineEdit.setSizePolicy(sizePolicy)
        self.hdmi_volume_value_lineEdit.setMinimumSize(QSize(50, 0))
        self.hdmi_volume_value_lineEdit.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.hdmi_volume_value_lineEdit, 1, 2, 1, 1)

        self.mic_in_volume_value_lineEdit = QLineEdit(self.widget)
        self.mic_in_volume_value_lineEdit.setObjectName(u"mic_in_volume_value_lineEdit")
        sizePolicy.setHeightForWidth(self.mic_in_volume_value_lineEdit.sizePolicy().hasHeightForWidth())
        self.mic_in_volume_value_lineEdit.setSizePolicy(sizePolicy)
        self.mic_in_volume_value_lineEdit.setMinimumSize(QSize(50, 0))
        self.mic_in_volume_value_lineEdit.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.mic_in_volume_value_lineEdit, 4, 2, 1, 1)

        self.mixer_uac_out_hmdi_checkBox = QCheckBox(self.widget)
        self.mixer_uac_out_hmdi_checkBox.setObjectName(u"mixer_uac_out_hmdi_checkBox")
        self.mixer_uac_out_hmdi_checkBox.setMinimumSize(QSize(20, 0))
        self.mixer_uac_out_hmdi_checkBox.setMaximumSize(QSize(30, 16777215))
        self.mixer_uac_out_hmdi_checkBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.mixer_uac_out_hmdi_checkBox, 1, 3, 1, 1, Qt.AlignHCenter)

        self.line_in_volume_value_lineEdit = QLineEdit(self.widget)
        self.line_in_volume_value_lineEdit.setObjectName(u"line_in_volume_value_lineEdit")
        sizePolicy.setHeightForWidth(self.line_in_volume_value_lineEdit.sizePolicy().hasHeightForWidth())
        self.line_in_volume_value_lineEdit.setSizePolicy(sizePolicy)
        self.line_in_volume_value_lineEdit.setMinimumSize(QSize(50, 0))
        self.line_in_volume_value_lineEdit.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.line_in_volume_value_lineEdit, 2, 2, 1, 1)

        self.hp_out_volume_label = QLabel(self.widget)
        self.hp_out_volume_label.setObjectName(u"hp_out_volume_label")
        self.hp_out_volume_label.setMinimumSize(QSize(80, 0))
        self.hp_out_volume_label.setFont(font)
        self.hp_out_volume_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.hp_out_volume_label, 5, 0, 1, 1)

        self.hp_out_volume_slider = QSlider(self.widget)
        self.hp_out_volume_slider.setObjectName(u"hp_out_volume_slider")
        sizePolicy.setHeightForWidth(self.hp_out_volume_slider.sizePolicy().hasHeightForWidth())
        self.hp_out_volume_slider.setSizePolicy(sizePolicy)
        self.hp_out_volume_slider.setMinimumSize(QSize(300, 0))
        self.hp_out_volume_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.hp_out_volume_slider, 5, 1, 1, 1)

        self.line_in_volume_label = QLabel(self.widget)
        self.line_in_volume_label.setObjectName(u"line_in_volume_label")
        self.line_in_volume_label.setMinimumSize(QSize(50, 0))
        self.line_in_volume_label.setFont(font)
        self.line_in_volume_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.line_in_volume_label, 2, 0, 1, 1)

        self.pc_volume_slider = QSlider(self.widget)
        self.pc_volume_slider.setObjectName(u"pc_volume_slider")
        sizePolicy.setHeightForWidth(self.pc_volume_slider.sizePolicy().hasHeightForWidth())
        self.pc_volume_slider.setSizePolicy(sizePolicy)
        self.pc_volume_slider.setMinimumSize(QSize(300, 0))
        self.pc_volume_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.pc_volume_slider, 3, 1, 1, 1)

        self.mic_in_volume_slider = QSlider(self.widget)
        self.mic_in_volume_slider.setObjectName(u"mic_in_volume_slider")
        sizePolicy.setHeightForWidth(self.mic_in_volume_slider.sizePolicy().hasHeightForWidth())
        self.mic_in_volume_slider.setSizePolicy(sizePolicy)
        self.mic_in_volume_slider.setMinimumSize(QSize(300, 0))
        self.mic_in_volume_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.mic_in_volume_slider, 4, 1, 1, 1)

        self.volume_label = QLabel(self.widget)
        self.volume_label.setObjectName(u"volume_label")
        self.volume_label.setFont(font1)
        self.volume_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.volume_label, 0, 1, 1, 1)

        self.mixer_hp_out_label = QLabel(self.widget)
        self.mixer_hp_out_label.setObjectName(u"mixer_hp_out_label")
        self.mixer_hp_out_label.setMinimumSize(QSize(100, 0))
        self.mixer_hp_out_label.setFont(font1)
        self.mixer_hp_out_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mixer_hp_out_label, 0, 4, 1, 1)

        self.line_in_volume_slider = QSlider(self.widget)
        self.line_in_volume_slider.setObjectName(u"line_in_volume_slider")
        sizePolicy.setHeightForWidth(self.line_in_volume_slider.sizePolicy().hasHeightForWidth())
        self.line_in_volume_slider.setSizePolicy(sizePolicy)
        self.line_in_volume_slider.setMinimumSize(QSize(300, 0))
        self.line_in_volume_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.line_in_volume_slider, 2, 1, 1, 1)

        self.mixer_hp_out_line_in_checkBox = QCheckBox(self.widget)
        self.mixer_hp_out_line_in_checkBox.setObjectName(u"mixer_hp_out_line_in_checkBox")
        self.mixer_hp_out_line_in_checkBox.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.mixer_hp_out_line_in_checkBox, 2, 4, 1, 1, Qt.AlignHCenter)

        self.mixer_hp_out_mic_in_checkBox = QCheckBox(self.widget)
        self.mixer_hp_out_mic_in_checkBox.setObjectName(u"mixer_hp_out_mic_in_checkBox")
        self.mixer_hp_out_mic_in_checkBox.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.mixer_hp_out_mic_in_checkBox, 4, 4, 1, 1, Qt.AlignHCenter)

        self.pc_volume_value_lineEdit = QLineEdit(self.widget)
        self.pc_volume_value_lineEdit.setObjectName(u"pc_volume_value_lineEdit")
        sizePolicy.setHeightForWidth(self.pc_volume_value_lineEdit.sizePolicy().hasHeightForWidth())
        self.pc_volume_value_lineEdit.setSizePolicy(sizePolicy)
        self.pc_volume_value_lineEdit.setMinimumSize(QSize(50, 0))
        self.pc_volume_value_lineEdit.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.pc_volume_value_lineEdit, 3, 2, 1, 1)

        self.mixer_uac_out_mic_in_checkBox = QCheckBox(self.widget)
        self.mixer_uac_out_mic_in_checkBox.setObjectName(u"mixer_uac_out_mic_in_checkBox")
        self.mixer_uac_out_mic_in_checkBox.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.mixer_uac_out_mic_in_checkBox, 4, 3, 1, 1, Qt.AlignHCenter)

        self.hdmi_volume_slider = QSlider(self.widget)
        self.hdmi_volume_slider.setObjectName(u"hdmi_volume_slider")
        sizePolicy.setHeightForWidth(self.hdmi_volume_slider.sizePolicy().hasHeightForWidth())
        self.hdmi_volume_slider.setSizePolicy(sizePolicy)
        self.hdmi_volume_slider.setMinimumSize(QSize(300, 0))
        self.hdmi_volume_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.hdmi_volume_slider, 1, 1, 1, 1)

        self.mixer_uac_out_line_in_checkBox = QCheckBox(self.widget)
        self.mixer_uac_out_line_in_checkBox.setObjectName(u"mixer_uac_out_line_in_checkBox")
        self.mixer_uac_out_line_in_checkBox.setMinimumSize(QSize(20, 0))

        self.gridLayout.addWidget(self.mixer_uac_out_line_in_checkBox, 2, 3, 1, 1, Qt.AlignHCenter)

        self.mixer_submit_pushButton = QPushButton(self.widget)
        self.mixer_submit_pushButton.setObjectName(u"mixer_submit_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mixer_submit_pushButton.sizePolicy().hasHeightForWidth())
        self.mixer_submit_pushButton.setSizePolicy(sizePolicy1)
        self.mixer_submit_pushButton.setMinimumSize(QSize(120, 0))
        self.mixer_submit_pushButton.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.mixer_submit_pushButton, 5, 3, 1, 2, Qt.AlignHCenter)


        self.retranslateUi(UC1218_4K_Audio_Form)

        QMetaObject.connectSlotsByName(UC1218_4K_Audio_Form)
    # setupUi

    def retranslateUi(self, UC1218_4K_Audio_Form):
        UC1218_4K_Audio_Form.setWindowTitle(QCoreApplication.translate("UC1218_4K_Audio_Form", u"Form", None))
        self.mic_in_volume_label.setText(QCoreApplication.translate("UC1218_4K_Audio_Form", u"Mic IN", None))
        self.mixer_hp_out_hdmi_checkBox.setText("")
        self.mixer_hp_out_pc_checkBox.setText("")
        self.hdmi_volume_label.setText(QCoreApplication.translate("UC1218_4K_Audio_Form", u"HDMI", None))
        self.pc_volume_label.setText(QCoreApplication.translate("UC1218_4K_Audio_Form", u"PC", None))
        self.mixer_uac_out_label.setText(QCoreApplication.translate("UC1218_4K_Audio_Form", u"USB Audio", None))
        self.mixer_uac_out_pc_in_checkBox.setText("")
        self.mixer_uac_out_hmdi_checkBox.setText("")
        self.hp_out_volume_label.setText(QCoreApplication.translate("UC1218_4K_Audio_Form", u"Headphone", None))
        self.line_in_volume_label.setText(QCoreApplication.translate("UC1218_4K_Audio_Form", u"Line IN", None))
        self.volume_label.setText(QCoreApplication.translate("UC1218_4K_Audio_Form", u"Volume", None))
        self.mixer_hp_out_label.setText(QCoreApplication.translate("UC1218_4K_Audio_Form", u"Headphone", None))
        self.mixer_hp_out_line_in_checkBox.setText("")
        self.mixer_hp_out_mic_in_checkBox.setText("")
        self.mixer_uac_out_mic_in_checkBox.setText("")
        self.mixer_uac_out_line_in_checkBox.setText("")
        self.mixer_submit_pushButton.setText(QCoreApplication.translate("UC1218_4K_Audio_Form", u"Apply", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cross_audio.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QWidget)

class Ui_Cross_Audio_Form(object):
    def setupUi(self, Cross_Audio_Form):
        if not Cross_Audio_Form.objectName():
            Cross_Audio_Form.setObjectName(u"Cross_Audio_Form")
        Cross_Audio_Form.resize(800, 500)
        self.layoutWidget = QWidget(Cross_Audio_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 70, 711, 391))
        self.horizontalLayout_25 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, -1, -1, -1)
        self.hdmiOutCh_3_4_comboBox = QComboBox(self.layoutWidget)
        self.hdmiOutCh_3_4_comboBox.setObjectName(u"hdmiOutCh_3_4_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hdmiOutCh_3_4_comboBox.sizePolicy().hasHeightForWidth())
        self.hdmiOutCh_3_4_comboBox.setSizePolicy(sizePolicy)
        self.hdmiOutCh_3_4_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_14.addWidget(self.hdmiOutCh_3_4_comboBox)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)


        self.gridLayout_2.addLayout(self.horizontalLayout_14, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.hdmiOutCh_1_2_label = QLabel(self.layoutWidget)
        self.hdmiOutCh_1_2_label.setObjectName(u"hdmiOutCh_1_2_label")

        self.horizontalLayout.addWidget(self.hdmiOutCh_1_2_label)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.hdmiOutCh_3_4_label = QLabel(self.layoutWidget)
        self.hdmiOutCh_3_4_label.setObjectName(u"hdmiOutCh_3_4_label")

        self.horizontalLayout_2.addWidget(self.hdmiOutCh_3_4_label)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, -1, -1, -1)
        self.hdmiOutCh_1_2_comboBox = QComboBox(self.layoutWidget)
        self.hdmiOutCh_1_2_comboBox.setObjectName(u"hdmiOutCh_1_2_comboBox")
        sizePolicy.setHeightForWidth(self.hdmiOutCh_1_2_comboBox.sizePolicy().hasHeightForWidth())
        self.hdmiOutCh_1_2_comboBox.setSizePolicy(sizePolicy)
        self.hdmiOutCh_1_2_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_13.addWidget(self.hdmiOutCh_1_2_comboBox)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.gridLayout_2.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.hdmiOutCh_5_6_label = QLabel(self.layoutWidget)
        self.hdmiOutCh_5_6_label.setObjectName(u"hdmiOutCh_5_6_label")

        self.horizontalLayout_3.addWidget(self.hdmiOutCh_5_6_label)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.hdmiOutCh_7_8_label = QLabel(self.layoutWidget)
        self.hdmiOutCh_7_8_label.setObjectName(u"hdmiOutCh_7_8_label")

        self.horizontalLayout_4.addWidget(self.hdmiOutCh_7_8_label)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_26)

        self.sdiOutCh_1_2_label_3 = QLabel(self.layoutWidget)
        self.sdiOutCh_1_2_label_3.setObjectName(u"sdiOutCh_1_2_label_3")

        self.horizontalLayout_27.addWidget(self.sdiOutCh_1_2_label_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_27, 5, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, -1, -1, -1)
        self.hdmiOutCh_5_6_comboBox = QComboBox(self.layoutWidget)
        self.hdmiOutCh_5_6_comboBox.setObjectName(u"hdmiOutCh_5_6_comboBox")
        sizePolicy.setHeightForWidth(self.hdmiOutCh_5_6_comboBox.sizePolicy().hasHeightForWidth())
        self.hdmiOutCh_5_6_comboBox.setSizePolicy(sizePolicy)
        self.hdmiOutCh_5_6_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_15.addWidget(self.hdmiOutCh_5_6_comboBox)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)


        self.gridLayout_2.addLayout(self.horizontalLayout_15, 2, 1, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_25)

        self.sdiOutCh_1_2_label_2 = QLabel(self.layoutWidget)
        self.sdiOutCh_1_2_label_2.setObjectName(u"sdiOutCh_1_2_label_2")

        self.horizontalLayout_26.addWidget(self.sdiOutCh_1_2_label_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_26, 4, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(20, -1, -1, -1)
        self.hdmiOutCh_7_8_comboBox = QComboBox(self.layoutWidget)
        self.hdmiOutCh_7_8_comboBox.setObjectName(u"hdmiOutCh_7_8_comboBox")
        sizePolicy.setHeightForWidth(self.hdmiOutCh_7_8_comboBox.sizePolicy().hasHeightForWidth())
        self.hdmiOutCh_7_8_comboBox.setSizePolicy(sizePolicy)
        self.hdmiOutCh_7_8_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_16.addWidget(self.hdmiOutCh_7_8_comboBox)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)


        self.gridLayout_2.addLayout(self.horizontalLayout_16, 3, 1, 1, 1)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(20, -1, -1, -1)
        self.analog_audio_comboBox = QComboBox(self.layoutWidget)
        self.analog_audio_comboBox.setObjectName(u"analog_audio_comboBox")
        sizePolicy.setHeightForWidth(self.analog_audio_comboBox.sizePolicy().hasHeightForWidth())
        self.analog_audio_comboBox.setSizePolicy(sizePolicy)
        self.analog_audio_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_28.addWidget(self.analog_audio_comboBox)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_27)


        self.gridLayout_2.addLayout(self.horizontalLayout_28, 4, 1, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(20, -1, -1, -1)
        self.tpg_audio_comboBox = QComboBox(self.layoutWidget)
        self.tpg_audio_comboBox.setObjectName(u"tpg_audio_comboBox")
        sizePolicy.setHeightForWidth(self.tpg_audio_comboBox.sizePolicy().hasHeightForWidth())
        self.tpg_audio_comboBox.setSizePolicy(sizePolicy)
        self.tpg_audio_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_29.addWidget(self.tpg_audio_comboBox)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_28)


        self.gridLayout_2.addLayout(self.horizontalLayout_29, 5, 1, 1, 1)


        self.horizontalLayout_25.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.sdiOutCh_3_4_label = QLabel(self.layoutWidget)
        self.sdiOutCh_3_4_label.setObjectName(u"sdiOutCh_3_4_label")

        self.horizontalLayout_6.addWidget(self.sdiOutCh_3_4_label)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(20, -1, -1, -1)
        self.sdiOutCh_7_8_comboBox = QComboBox(self.layoutWidget)
        self.sdiOutCh_7_8_comboBox.setObjectName(u"sdiOutCh_7_8_comboBox")
        sizePolicy.setHeightForWidth(self.sdiOutCh_7_8_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiOutCh_7_8_comboBox.setSizePolicy(sizePolicy)
        self.sdiOutCh_7_8_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_20.addWidget(self.sdiOutCh_7_8_comboBox)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)


        self.gridLayout.addLayout(self.horizontalLayout_20, 3, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.sdiOutCh_5_6_label = QLabel(self.layoutWidget)
        self.sdiOutCh_5_6_label.setObjectName(u"sdiOutCh_5_6_label")

        self.horizontalLayout_7.addWidget(self.sdiOutCh_5_6_label)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(20, -1, -1, -1)
        self.sdiOutCh_11_12_comboBox = QComboBox(self.layoutWidget)
        self.sdiOutCh_11_12_comboBox.setObjectName(u"sdiOutCh_11_12_comboBox")
        sizePolicy.setHeightForWidth(self.sdiOutCh_11_12_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiOutCh_11_12_comboBox.setSizePolicy(sizePolicy)
        self.sdiOutCh_11_12_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_22.addWidget(self.sdiOutCh_11_12_comboBox)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_22)


        self.gridLayout.addLayout(self.horizontalLayout_22, 5, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.sdiOutCh_11_12_label = QLabel(self.layoutWidget)
        self.sdiOutCh_11_12_label.setObjectName(u"sdiOutCh_11_12_label")

        self.horizontalLayout_10.addWidget(self.sdiOutCh_11_12_label)


        self.gridLayout.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(20, -1, -1, -1)
        self.sdiOutCh_15_16_comboBox = QComboBox(self.layoutWidget)
        self.sdiOutCh_15_16_comboBox.setObjectName(u"sdiOutCh_15_16_comboBox")
        sizePolicy.setHeightForWidth(self.sdiOutCh_15_16_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiOutCh_15_16_comboBox.setSizePolicy(sizePolicy)
        self.sdiOutCh_15_16_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_24.addWidget(self.sdiOutCh_15_16_comboBox)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_24)


        self.gridLayout.addLayout(self.horizontalLayout_24, 7, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.sdiOutCh_7_8_label = QLabel(self.layoutWidget)
        self.sdiOutCh_7_8_label.setObjectName(u"sdiOutCh_7_8_label")

        self.horizontalLayout_8.addWidget(self.sdiOutCh_7_8_label)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(20, -1, -1, -1)
        self.sdiOutCh_13_14_comboBox = QComboBox(self.layoutWidget)
        self.sdiOutCh_13_14_comboBox.setObjectName(u"sdiOutCh_13_14_comboBox")
        sizePolicy.setHeightForWidth(self.sdiOutCh_13_14_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiOutCh_13_14_comboBox.setSizePolicy(sizePolicy)
        self.sdiOutCh_13_14_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_23.addWidget(self.sdiOutCh_13_14_comboBox)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_23)


        self.gridLayout.addLayout(self.horizontalLayout_23, 6, 1, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(20, -1, -1, -1)
        self.sdiOutCh_5_6_comboBox = QComboBox(self.layoutWidget)
        self.sdiOutCh_5_6_comboBox.setObjectName(u"sdiOutCh_5_6_comboBox")
        sizePolicy.setHeightForWidth(self.sdiOutCh_5_6_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiOutCh_5_6_comboBox.setSizePolicy(sizePolicy)
        self.sdiOutCh_5_6_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_19.addWidget(self.sdiOutCh_5_6_comboBox)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)


        self.gridLayout.addLayout(self.horizontalLayout_19, 2, 1, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(20, -1, -1, -1)
        self.sdiOutCh_9_10_comboBox = QComboBox(self.layoutWidget)
        self.sdiOutCh_9_10_comboBox.setObjectName(u"sdiOutCh_9_10_comboBox")
        sizePolicy.setHeightForWidth(self.sdiOutCh_9_10_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiOutCh_9_10_comboBox.setSizePolicy(sizePolicy)
        self.sdiOutCh_9_10_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_21.addWidget(self.sdiOutCh_9_10_comboBox)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)


        self.gridLayout.addLayout(self.horizontalLayout_21, 4, 1, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(20, -1, -1, -1)
        self.sdiOutCh_3_4_comboBox = QComboBox(self.layoutWidget)
        self.sdiOutCh_3_4_comboBox.setObjectName(u"sdiOutCh_3_4_comboBox")
        sizePolicy.setHeightForWidth(self.sdiOutCh_3_4_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiOutCh_3_4_comboBox.setSizePolicy(sizePolicy)
        self.sdiOutCh_3_4_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_18.addWidget(self.sdiOutCh_3_4_comboBox)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)


        self.gridLayout.addLayout(self.horizontalLayout_18, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.sdiOutCh_13_14_label = QLabel(self.layoutWidget)
        self.sdiOutCh_13_14_label.setObjectName(u"sdiOutCh_13_14_label")

        self.horizontalLayout_11.addWidget(self.sdiOutCh_13_14_label)


        self.gridLayout.addLayout(self.horizontalLayout_11, 6, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.sdiOutCh_15_16_label = QLabel(self.layoutWidget)
        self.sdiOutCh_15_16_label.setObjectName(u"sdiOutCh_15_16_label")

        self.horizontalLayout_12.addWidget(self.sdiOutCh_15_16_label)


        self.gridLayout.addLayout(self.horizontalLayout_12, 7, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, -1, -1, -1)
        self.sdiOutCh_1_2_comboBox = QComboBox(self.layoutWidget)
        self.sdiOutCh_1_2_comboBox.setObjectName(u"sdiOutCh_1_2_comboBox")
        sizePolicy.setHeightForWidth(self.sdiOutCh_1_2_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiOutCh_1_2_comboBox.setSizePolicy(sizePolicy)
        self.sdiOutCh_1_2_comboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_17.addWidget(self.sdiOutCh_1_2_comboBox)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)


        self.gridLayout.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.sdiOutCh_1_2_label = QLabel(self.layoutWidget)
        self.sdiOutCh_1_2_label.setObjectName(u"sdiOutCh_1_2_label")

        self.horizontalLayout_5.addWidget(self.sdiOutCh_1_2_label)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.sdiOutCh_9_10_label = QLabel(self.layoutWidget)
        self.sdiOutCh_9_10_label.setObjectName(u"sdiOutCh_9_10_label")

        self.horizontalLayout_9.addWidget(self.sdiOutCh_9_10_label)


        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)


        self.horizontalLayout_25.addLayout(self.gridLayout)


        self.retranslateUi(Cross_Audio_Form)

        QMetaObject.connectSlotsByName(Cross_Audio_Form)
    # setupUi

    def retranslateUi(self, Cross_Audio_Form):
        Cross_Audio_Form.setWindowTitle(QCoreApplication.translate("Cross_Audio_Form", u"Form", None))
        self.hdmiOutCh_1_2_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"HDMI CH1-2", None))
        self.hdmiOutCh_3_4_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"HDMI CH3-4", None))
        self.hdmiOutCh_5_6_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"HDMI CH5-6", None))
        self.hdmiOutCh_7_8_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"HDMI CH7-8", None))
        self.sdiOutCh_1_2_label_3.setText(QCoreApplication.translate("Cross_Audio_Form", u"TPG Audio", None))
        self.sdiOutCh_1_2_label_2.setText(QCoreApplication.translate("Cross_Audio_Form", u"Audio Out", None))
        self.sdiOutCh_3_4_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"SDI CH3-4", None))
        self.sdiOutCh_5_6_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"SDI CH5-6", None))
        self.sdiOutCh_11_12_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"SDI CH11-12", None))
        self.sdiOutCh_7_8_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"SDI CH7-8", None))
        self.sdiOutCh_13_14_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"SDI CH13-14", None))
        self.sdiOutCh_15_16_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"SDI CH15-16", None))
        self.sdiOutCh_1_2_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"SDI CH1-2", None))
        self.sdiOutCh_9_10_label.setText(QCoreApplication.translate("Cross_Audio_Form", u"SDI CH9-10", None))
    # retranslateUi


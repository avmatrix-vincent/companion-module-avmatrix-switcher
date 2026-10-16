# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cross_videoFormat.ui'
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

class Ui_Cross_Video_Format_Form(object):
    def setupUi(self, Cross_Video_Format_Form):
        if not Cross_Video_Format_Form.objectName():
            Cross_Video_Format_Form.setObjectName(u"Cross_Video_Format_Form")
        Cross_Video_Format_Form.resize(800, 500)
        self.layoutWidget = QWidget(Cross_Video_Format_Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 70, 591, 373))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.SD2SD_aspect_comboBox = QComboBox(self.layoutWidget)
        self.SD2SD_aspect_comboBox.setObjectName(u"SD2SD_aspect_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SD2SD_aspect_comboBox.sizePolicy().hasHeightForWidth())
        self.SD2SD_aspect_comboBox.setSizePolicy(sizePolicy)
        self.SD2SD_aspect_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_10.addWidget(self.SD2SD_aspect_comboBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.gridLayout.addLayout(self.horizontalLayout_10, 3, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.hdmiColorSpace_comboBox = QComboBox(self.layoutWidget)
        self.hdmiColorSpace_comboBox.setObjectName(u"hdmiColorSpace_comboBox")
        sizePolicy.setHeightForWidth(self.hdmiColorSpace_comboBox.sizePolicy().hasHeightForWidth())
        self.hdmiColorSpace_comboBox.setSizePolicy(sizePolicy)
        self.hdmiColorSpace_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_3.addWidget(self.hdmiColorSpace_comboBox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)

        self.HD2HD_aspect_label = QLabel(self.layoutWidget)
        self.HD2HD_aspect_label.setObjectName(u"HD2HD_aspect_label")

        self.horizontalLayout_19.addWidget(self.HD2HD_aspect_label)


        self.gridLayout.addLayout(self.horizontalLayout_19, 6, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)

        self.HD2SD_aspect_label = QLabel(self.layoutWidget)
        self.HD2SD_aspect_label.setObjectName(u"HD2SD_aspect_label")

        self.horizontalLayout_17.addWidget(self.HD2SD_aspect_label)


        self.gridLayout.addLayout(self.horizontalLayout_17, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.hdmiColorSpace_label = QLabel(self.layoutWidget)
        self.hdmiColorSpace_label.setObjectName(u"hdmiColorSpace_label")

        self.horizontalLayout_4.addWidget(self.hdmiColorSpace_label)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, -1, -1, -1)
        self.i2psfMode_comboBox = QComboBox(self.layoutWidget)
        self.i2psfMode_comboBox.setObjectName(u"i2psfMode_comboBox")
        sizePolicy.setHeightForWidth(self.i2psfMode_comboBox.sizePolicy().hasHeightForWidth())
        self.i2psfMode_comboBox.setSizePolicy(sizePolicy)
        self.i2psfMode_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_11.addWidget(self.i2psfMode_comboBox)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.gridLayout.addLayout(self.horizontalLayout_11, 7, 1, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(20, -1, -1, -1)
        self.pattern_combox = QComboBox(self.layoutWidget)
        self.pattern_combox.setObjectName(u"pattern_combox")
        sizePolicy.setHeightForWidth(self.pattern_combox.sizePolicy().hasHeightForWidth())
        self.pattern_combox.setSizePolicy(sizePolicy)
        self.pattern_combox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_24.addWidget(self.pattern_combox)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_23)


        self.gridLayout.addLayout(self.horizontalLayout_24, 11, 1, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(20, -1, -1, -1)
        self.deinterlace__comboBox = QComboBox(self.layoutWidget)
        self.deinterlace__comboBox.setObjectName(u"deinterlace__comboBox")
        sizePolicy.setHeightForWidth(self.deinterlace__comboBox.sizePolicy().hasHeightForWidth())
        self.deinterlace__comboBox.setSizePolicy(sizePolicy)
        self.deinterlace__comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_22.addWidget(self.deinterlace__comboBox)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_25)


        self.gridLayout.addLayout(self.horizontalLayout_22, 8, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.SD2SD_aspect_label = QLabel(self.layoutWidget)
        self.SD2SD_aspect_label.setObjectName(u"SD2SD_aspect_label")

        self.horizontalLayout_6.addWidget(self.SD2SD_aspect_label)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(20, -1, -1, -1)
        self.HD2SD_aspect_comboBox = QComboBox(self.layoutWidget)
        self.HD2SD_aspect_comboBox.setObjectName(u"HD2SD_aspect_comboBox")
        sizePolicy.setHeightForWidth(self.HD2SD_aspect_comboBox.sizePolicy().hasHeightForWidth())
        self.HD2SD_aspect_comboBox.setSizePolicy(sizePolicy)
        self.HD2SD_aspect_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_18.addWidget(self.HD2SD_aspect_comboBox)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)


        self.gridLayout.addLayout(self.horizontalLayout_18, 5, 1, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_22)

        self.sdiImageFlip_label_2 = QLabel(self.layoutWidget)
        self.sdiImageFlip_label_2.setObjectName(u"sdiImageFlip_label_2")

        self.horizontalLayout_23.addWidget(self.sdiImageFlip_label_2)


        self.gridLayout.addLayout(self.horizontalLayout_23, 11, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, -1, -1, -1)
        self.sdiImageFlip_comboBox = QComboBox(self.layoutWidget)
        self.sdiImageFlip_comboBox.setObjectName(u"sdiImageFlip_comboBox")
        sizePolicy.setHeightForWidth(self.sdiImageFlip_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiImageFlip_comboBox.setSizePolicy(sizePolicy)
        self.sdiImageFlip_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_12.addWidget(self.sdiImageFlip_comboBox)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.gridLayout.addLayout(self.horizontalLayout_12, 9, 1, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(20, -1, -1, -1)
        self.HD2HD_aspect_comboBox = QComboBox(self.layoutWidget)
        self.HD2HD_aspect_comboBox.setObjectName(u"HD2HD_aspect_comboBox")
        sizePolicy.setHeightForWidth(self.HD2HD_aspect_comboBox.sizePolicy().hasHeightForWidth())
        self.HD2HD_aspect_comboBox.setSizePolicy(sizePolicy)
        self.HD2HD_aspect_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_20.addWidget(self.HD2HD_aspect_comboBox)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)


        self.gridLayout.addLayout(self.horizontalLayout_20, 6, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.outputFormat_comboBox = QComboBox(self.layoutWidget)
        self.outputFormat_comboBox.setObjectName(u"outputFormat_comboBox")
        sizePolicy.setHeightForWidth(self.outputFormat_comboBox.sizePolicy().hasHeightForWidth())
        self.outputFormat_comboBox.setSizePolicy(sizePolicy)
        self.outputFormat_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout.addWidget(self.outputFormat_comboBox)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.hdmiImageFlip_label = QLabel(self.layoutWidget)
        self.hdmiImageFlip_label.setObjectName(u"hdmiImageFlip_label")

        self.horizontalLayout_13.addWidget(self.hdmiImageFlip_label)


        self.gridLayout.addLayout(self.horizontalLayout_13, 10, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.sdiOutputFormat_comboBox = QComboBox(self.layoutWidget)
        self.sdiOutputFormat_comboBox.setObjectName(u"sdiOutputFormat_comboBox")
        sizePolicy.setHeightForWidth(self.sdiOutputFormat_comboBox.sizePolicy().hasHeightForWidth())
        self.sdiOutputFormat_comboBox.setSizePolicy(sizePolicy)
        self.sdiOutputFormat_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_9.addWidget(self.sdiOutputFormat_comboBox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.outputFormat_label = QLabel(self.layoutWidget)
        self.outputFormat_label.setObjectName(u"outputFormat_label")

        self.horizontalLayout_2.addWidget(self.outputFormat_label)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(20, -1, -1, -1)
        self.SD2HD_aspect_comboBox = QComboBox(self.layoutWidget)
        self.SD2HD_aspect_comboBox.setObjectName(u"SD2HD_aspect_comboBox")
        sizePolicy.setHeightForWidth(self.SD2HD_aspect_comboBox.sizePolicy().hasHeightForWidth())
        self.SD2HD_aspect_comboBox.setSizePolicy(sizePolicy)
        self.SD2HD_aspect_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_16.addWidget(self.SD2HD_aspect_comboBox)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)


        self.gridLayout.addLayout(self.horizontalLayout_16, 4, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.sdiImageFlip_label = QLabel(self.layoutWidget)
        self.sdiImageFlip_label.setObjectName(u"sdiImageFlip_label")

        self.horizontalLayout_8.addWidget(self.sdiImageFlip_label)


        self.gridLayout.addLayout(self.horizontalLayout_8, 9, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, -1, -1, -1)
        self.hdmiImageFlip_comboBox = QComboBox(self.layoutWidget)
        self.hdmiImageFlip_comboBox.setObjectName(u"hdmiImageFlip_comboBox")
        sizePolicy.setHeightForWidth(self.hdmiImageFlip_comboBox.sizePolicy().hasHeightForWidth())
        self.hdmiImageFlip_comboBox.setSizePolicy(sizePolicy)
        self.hdmiImageFlip_comboBox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_14.addWidget(self.hdmiImageFlip_comboBox)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)


        self.gridLayout.addLayout(self.horizontalLayout_14, 10, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.i2psfMode_label = QLabel(self.layoutWidget)
        self.i2psfMode_label.setObjectName(u"i2psfMode_label")

        self.horizontalLayout_7.addWidget(self.i2psfMode_label)


        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.sdiOutputFormat_label = QLabel(self.layoutWidget)
        self.sdiOutputFormat_label.setObjectName(u"sdiOutputFormat_label")

        self.horizontalLayout_5.addWidget(self.sdiOutputFormat_label)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)

        self.i2psfMode_label_2 = QLabel(self.layoutWidget)
        self.i2psfMode_label_2.setObjectName(u"i2psfMode_label_2")

        self.horizontalLayout_21.addWidget(self.i2psfMode_label_2)


        self.gridLayout.addLayout(self.horizontalLayout_21, 8, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.SD2HD_aspect_label = QLabel(self.layoutWidget)
        self.SD2HD_aspect_label.setObjectName(u"SD2HD_aspect_label")

        self.horizontalLayout_15.addWidget(self.SD2HD_aspect_label)


        self.gridLayout.addLayout(self.horizontalLayout_15, 4, 0, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_24)

        self.sdiImageFlip_label_3 = QLabel(self.layoutWidget)
        self.sdiImageFlip_label_3.setObjectName(u"sdiImageFlip_label_3")

        self.horizontalLayout_25.addWidget(self.sdiImageFlip_label_3)


        self.gridLayout.addLayout(self.horizontalLayout_25, 12, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(20, -1, -1, -1)
        self.sdiImageFlip_combox = QComboBox(self.layoutWidget)
        self.sdiImageFlip_combox.setObjectName(u"sdiImageFlip_combox")
        sizePolicy.setHeightForWidth(self.sdiImageFlip_combox.sizePolicy().hasHeightForWidth())
        self.sdiImageFlip_combox.setSizePolicy(sizePolicy)
        self.sdiImageFlip_combox.setMinimumSize(QSize(280, 0))

        self.horizontalLayout_26.addWidget(self.sdiImageFlip_combox)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_26)


        self.gridLayout.addLayout(self.horizontalLayout_26, 12, 1, 1, 1)


        self.retranslateUi(Cross_Video_Format_Form)

        QMetaObject.connectSlotsByName(Cross_Video_Format_Form)
    # setupUi

    def retranslateUi(self, Cross_Video_Format_Form):
        Cross_Video_Format_Form.setWindowTitle(QCoreApplication.translate("Cross_Video_Format_Form", u"Form", None))
        self.HD2HD_aspect_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"HD2HD Aspect", None))
        self.HD2SD_aspect_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"HD2SD Aspect", None))
        self.hdmiColorSpace_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"HDMI Color Space", None))
        self.SD2SD_aspect_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"SD2SD Aspect", None))
        self.sdiImageFlip_label_2.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"TPG", None))
        self.hdmiImageFlip_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"HDMI Out Flip", None))
        self.outputFormat_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"Output Format", None))
        self.sdiImageFlip_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"SDI Out Flip", None))
        self.i2psfMode_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"1080i=1080psf", None))
        self.sdiOutputFormat_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"3G-SDI Out", None))
        self.i2psfMode_label_2.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"Deinterlace", None))
        self.SD2HD_aspect_label.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"SD2HD Aspect", None))
        self.sdiImageFlip_label_3.setText(QCoreApplication.translate("Cross_Video_Format_Form", u"TPG Overlay", None))
    # retranslateUi


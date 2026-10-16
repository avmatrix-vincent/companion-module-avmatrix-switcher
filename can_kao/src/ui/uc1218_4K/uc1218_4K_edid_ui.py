# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uc1218_4K_edid.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.components.SingleCheckComboBox import SingleCheckComboBox

class Ui_UC1218_4K_Edid_Form(object):
    def setupUi(self, UC1218_4K_Edid_Form):
        if not UC1218_4K_Edid_Form.objectName():
            UC1218_4K_Edid_Form.setObjectName(u"UC1218_4K_Edid_Form")
        UC1218_4K_Edid_Form.resize(800, 500)
        self.widget = QWidget(UC1218_4K_Edid_Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 180, 573, 91))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.edidMode_label = QLabel(self.widget)
        self.edidMode_label.setObjectName(u"edidMode_label")

        self.horizontalLayout.addWidget(self.edidMode_label)

        self.edidMode_comboBox = QComboBox(self.widget)
        self.edidMode_comboBox.setObjectName(u"edidMode_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edidMode_comboBox.sizePolicy().hasHeightForWidth())
        self.edidMode_comboBox.setSizePolicy(sizePolicy)
        self.edidMode_comboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.edidMode_comboBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.edidContent_label = QLabel(self.widget)
        self.edidContent_label.setObjectName(u"edidContent_label")

        self.horizontalLayout_2.addWidget(self.edidContent_label)

        self.edidContent_comboBox = SingleCheckComboBox(self.widget)
        self.edidContent_comboBox.setObjectName(u"edidContent_comboBox")
        sizePolicy.setHeightForWidth(self.edidContent_comboBox.sizePolicy().hasHeightForWidth())
        self.edidContent_comboBox.setSizePolicy(sizePolicy)
        self.edidContent_comboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.edidContent_comboBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.importEdid_pushButton = QPushButton(self.widget)
        self.importEdid_pushButton.setObjectName(u"importEdid_pushButton")
        self.importEdid_pushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.importEdid_pushButton)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.exportEdid_pushButton = QPushButton(self.widget)
        self.exportEdid_pushButton.setObjectName(u"exportEdid_pushButton")
        self.exportEdid_pushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.exportEdid_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.edidContent_delete_pushButton = QPushButton(self.widget)
        self.edidContent_delete_pushButton.setObjectName(u"edidContent_delete_pushButton")
        self.edidContent_delete_pushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.edidContent_delete_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.edidContent_save_pushButton = QPushButton(self.widget)
        self.edidContent_save_pushButton.setObjectName(u"edidContent_save_pushButton")
        self.edidContent_save_pushButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.edidContent_save_pushButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(UC1218_4K_Edid_Form)

        QMetaObject.connectSlotsByName(UC1218_4K_Edid_Form)
    # setupUi

    def retranslateUi(self, UC1218_4K_Edid_Form):
        UC1218_4K_Edid_Form.setWindowTitle(QCoreApplication.translate("UC1218_4K_Edid_Form", u"Form", None))
        self.edidMode_label.setText(QCoreApplication.translate("UC1218_4K_Edid_Form", u"Mode", None))
        self.edidContent_label.setText(QCoreApplication.translate("UC1218_4K_Edid_Form", u"Content", None))
        self.importEdid_pushButton.setText(QCoreApplication.translate("UC1218_4K_Edid_Form", u"Import", None))
        self.exportEdid_pushButton.setText(QCoreApplication.translate("UC1218_4K_Edid_Form", u"Export", None))
        self.edidContent_delete_pushButton.setText(QCoreApplication.translate("UC1218_4K_Edid_Form", u"Delete", None))
        self.edidContent_save_pushButton.setText(QCoreApplication.translate("UC1218_4K_Edid_Form", u"Apply", None))
    # retranslateUi


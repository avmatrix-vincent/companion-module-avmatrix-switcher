# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_selector_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(128, 128)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bottom_widget = QWidget(Form)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.bottom_widget.setMinimumSize(QSize(110, 110))
        self.pushButton_select_color = QPushButton(self.bottom_widget)
        self.pushButton_select_color.setObjectName(u"pushButton_select_color")
        self.pushButton_select_color.setGeometry(QRect(70, 70, 32, 32))
        self.pushButton_select_color.setStyleSheet(u"border-image: url(:/icons/images/color_setting.png);")
        self.color_display_widget = QWidget(self.bottom_widget)
        self.color_display_widget.setObjectName(u"color_display_widget")
        self.color_display_widget.setGeometry(QRect(29, 29, 50, 50))
        self.color_display_widget.setStyleSheet(u"background-color: rgb(243, 152, 1);\n"
"border-radius: 8px;")
        self.color_black_label = QLabel(self.bottom_widget)
        self.color_black_label.setObjectName(u"color_black_label")
        self.color_black_label.setGeometry(QRect(14, 14, 80, 80))
        self.color_black_label.setStyleSheet(u"#color_black_label{\n"
"	background-color: #2b2b2b;\n"
"	border-radius: 8px;\n"
"	border: 2px solid #363636;\n"
"}")
        self.color_black_label.raise_()
        self.pushButton_select_color.raise_()
        self.color_display_widget.raise_()

        self.verticalLayout.addWidget(self.bottom_widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_select_color.setText("")
        self.color_black_label.setText("")
    # retranslateUi


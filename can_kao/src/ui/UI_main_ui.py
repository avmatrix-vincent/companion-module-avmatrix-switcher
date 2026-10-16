# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_main.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import images_rc

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(MainWidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainwindow_layout = QVBoxLayout()
        self.mainwindow_layout.setSpacing(0)
        self.mainwindow_layout.setObjectName(u"mainwindow_layout")
        self.top_blank_widget = QWidget(MainWidget)
        self.top_blank_widget.setObjectName(u"top_blank_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_blank_widget.sizePolicy().hasHeightForWidth())
        self.top_blank_widget.setSizePolicy(sizePolicy1)
        self.top_blank_widget.setMaximumSize(QSize(16777215, 50))
        self.top_blank_widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.top_blank_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_label = QLabel(self.top_blank_widget)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy1.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy1)
        self.logo_label.setMinimumSize(QSize(550, 0))
        self.logo_label.setStyleSheet(u"")
        self.logo_label.setScaledContents(False)

        self.horizontalLayout.addWidget(self.logo_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_setting = QPushButton(self.top_blank_widget)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        self.pushButton_setting.setMinimumSize(QSize(50, 37))
        self.pushButton_setting.setMaximumSize(QSize(50, 37))
        icon = QIcon()
        icon.addFile(u":/icons/images/top_setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_setting.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton_setting)

        self.pushButton_min = QPushButton(self.top_blank_widget)
        self.pushButton_min.setObjectName(u"pushButton_min")
        self.pushButton_min.setMinimumSize(QSize(50, 37))
        self.pushButton_min.setMaximumSize(QSize(50, 37))
        self.pushButton_min.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_min.setIcon(icon1)
        self.pushButton_min.setIconSize(QSize(14, 50))

        self.horizontalLayout.addWidget(self.pushButton_min)

        self.pushButton_close = QPushButton(self.top_blank_widget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(50, 37))
        self.pushButton_close.setMaximumSize(QSize(50, 37))
        self.pushButton_close.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setIconSize(QSize(12, 12))

        self.horizontalLayout.addWidget(self.pushButton_close)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.mainwindow_layout.addWidget(self.top_blank_widget)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainwindow_layout.addItem(self.verticalSpacer_4)

        self.main_backgroud = QWidget(MainWidget)
        self.main_backgroud.setObjectName(u"main_backgroud")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_backgroud.sizePolicy().hasHeightForWidth())
        self.main_backgroud.setSizePolicy(sizePolicy2)
        self.main_backgroud.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.main_backgroud)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.main_hori_layout = QHBoxLayout()
        self.main_hori_layout.setSpacing(0)
        self.main_hori_layout.setObjectName(u"main_hori_layout")
        self.main_hori_layout.setContentsMargins(20, -1, 20, -1)
        self.left_widget = QWidget(self.main_backgroud)
        self.left_widget.setObjectName(u"left_widget")
        sizePolicy.setHeightForWidth(self.left_widget.sizePolicy().hasHeightForWidth())
        self.left_widget.setSizePolicy(sizePolicy)
        self.left_widget.setMaximumSize(QSize(16777215, 592))
        self.left_widget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.left_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.left_left_widget = QWidget(self.left_widget)
        self.left_left_widget.setObjectName(u"left_left_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.left_left_widget.sizePolicy().hasHeightForWidth())
        self.left_left_widget.setSizePolicy(sizePolicy3)
        self.left_left_widget.setMinimumSize(QSize(184, 580))
        self.left_left_widget.setMaximumSize(QSize(16777215, 580))
        self.verticalLayout_3 = QVBoxLayout(self.left_left_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.device_list_v_layout = QVBoxLayout()
        self.device_list_v_layout.setSpacing(6)
        self.device_list_v_layout.setObjectName(u"device_list_v_layout")
        self.pushButton_scan = QPushButton(self.left_left_widget)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_scan.sizePolicy().hasHeightForWidth())
        self.pushButton_scan.setSizePolicy(sizePolicy4)
        self.pushButton_scan.setMinimumSize(QSize(0, 55))
        self.pushButton_scan.setMaximumSize(QSize(170, 55))
        self.pushButton_scan.setAutoFillBackground(False)
        self.pushButton_scan.setStyleSheet(u"border-image: url(:/icons/images/scan_new.png);\n"
"padding-left: 40px;")
        self.pushButton_scan.setIconSize(QSize(40, 40))

        self.device_list_v_layout.addWidget(self.pushButton_scan)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.device_list_v_layout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_pageUp = QPushButton(self.left_left_widget)
        self.pushButton_pageUp.setObjectName(u"pushButton_pageUp")
        sizePolicy.setHeightForWidth(self.pushButton_pageUp.sizePolicy().hasHeightForWidth())
        self.pushButton_pageUp.setSizePolicy(sizePolicy)
        self.pushButton_pageUp.setMinimumSize(QSize(85, 20))
        self.pushButton_pageUp.setMaximumSize(QSize(85, 20))
        self.pushButton_pageUp.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/pageUp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_pageUp.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.pushButton_pageUp)

        self.pushButton_pageDown = QPushButton(self.left_left_widget)
        self.pushButton_pageDown.setObjectName(u"pushButton_pageDown")
        sizePolicy.setHeightForWidth(self.pushButton_pageDown.sizePolicy().hasHeightForWidth())
        self.pushButton_pageDown.setSizePolicy(sizePolicy)
        self.pushButton_pageDown.setMinimumSize(QSize(85, 20))
        self.pushButton_pageDown.setMaximumSize(QSize(85, 20))
        self.pushButton_pageDown.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/pageDown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_pageDown.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.pushButton_pageDown)

        self.horizontalSpacer_7 = QSpacerItem(4, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.device_list_v_layout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.device_list_v_layout)


        self.horizontalLayout_4.addWidget(self.left_left_widget)

        self.listWidget = QListWidget(self.left_widget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy3.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy3)
        self.listWidget.setMinimumSize(QSize(0, 580))
        self.listWidget.setMaximumSize(QSize(160, 580))
        self.listWidget.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_4.addWidget(self.listWidget)


        self.main_hori_layout.addWidget(self.left_widget)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.main_hori_layout.addItem(self.horizontalSpacer_9)

        self.stackedWidget = QStackedWidget(self.main_backgroud)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy5)
        self.stackedWidget.setMinimumSize(QSize(0, 592))
        self.stackedWidget.setMaximumSize(QSize(16777215, 592))
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_7 = QHBoxLayout(self.page)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_left = QSpacerItem(19, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_left)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"font: 700 30pt \"Microsoft YaHei UI\";\n"
"color: rgb(71, 72, 74);")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(64, 64))
        self.label_2.setStyleSheet(u"border-image: url(:/icons/images/hook.png);")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.horizontalSpacer_right = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_right)

        self.stackedWidget.addWidget(self.page)

        self.main_hori_layout.addWidget(self.stackedWidget)


        self.verticalLayout_4.addLayout(self.main_hori_layout)


        self.mainwindow_layout.addWidget(self.main_backgroud)

        self.verticalSpacer_5 = QSpacerItem(20, 11, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.mainwindow_layout.addItem(self.verticalSpacer_5)

        self.bottom_blank_widget = QWidget(MainWidget)
        self.bottom_blank_widget.setObjectName(u"bottom_blank_widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.bottom_blank_widget.sizePolicy().hasHeightForWidth())
        self.bottom_blank_widget.setSizePolicy(sizePolicy6)
        self.bottom_blank_widget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.bottom_blank_widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_8 = QSpacerItem(956, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.bottom_info_widget = QWidget(self.bottom_blank_widget)
        self.bottom_info_widget.setObjectName(u"bottom_info_widget")
        self.bottom_info_widget.setMinimumSize(QSize(320, 0))
        self.bottom_info_widget.setMaximumSize(QSize(320, 16777215))
        self.bottom_info_widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.bottom_info_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_connected_image = QLabel(self.bottom_info_widget)
        self.label_connected_image.setObjectName(u"label_connected_image")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_connected_image.sizePolicy().hasHeightForWidth())
        self.label_connected_image.setSizePolicy(sizePolicy7)
        self.label_connected_image.setMinimumSize(QSize(14, 14))
        self.label_connected_image.setMaximumSize(QSize(14, 14))
        self.label_connected_image.setPixmap(QPixmap(u":/icons/images/connected.png"))
        self.label_connected_image.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_connected_image)

        self.label_connected = QLabel(self.bottom_info_widget)
        self.label_connected.setObjectName(u"label_connected")
        sizePolicy.setHeightForWidth(self.label_connected.sizePolicy().hasHeightForWidth())
        self.label_connected.setSizePolicy(sizePolicy)
        self.label_connected.setMinimumSize(QSize(130, 14))
        self.label_connected.setMaximumSize(QSize(130, 14))
        self.label_connected.setStyleSheet(u"color: #a0a0a0;\n"
"font-size: 14px;")
        self.label_connected.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_connected)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_version_image = QLabel(self.bottom_info_widget)
        self.label_version_image.setObjectName(u"label_version_image")
        sizePolicy7.setHeightForWidth(self.label_version_image.sizePolicy().hasHeightForWidth())
        self.label_version_image.setSizePolicy(sizePolicy7)
        self.label_version_image.setMinimumSize(QSize(14, 14))
        self.label_version_image.setMaximumSize(QSize(14, 14))
        self.label_version_image.setPixmap(QPixmap(u":/icons/images/version.png"))
        self.label_version_image.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_version_image)

        self.label_version = QLabel(self.bottom_info_widget)
        self.label_version.setObjectName(u"label_version")
        sizePolicy.setHeightForWidth(self.label_version.sizePolicy().hasHeightForWidth())
        self.label_version.setSizePolicy(sizePolicy)
        self.label_version.setMinimumSize(QSize(60, 14))
        self.label_version.setMaximumSize(QSize(60, 14))
        self.label_version.setStyleSheet(u"color: #a0a0a0;\n"
"font-size: 14px;")
        self.label_version.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_version)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addWidget(self.bottom_info_widget)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.mainwindow_layout.addWidget(self.bottom_blank_widget)


        self.verticalLayout_6.addLayout(self.mainwindow_layout)


        self.retranslateUi(MainWidget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Form", None))
        self.logo_label.setText("")
        self.pushButton_setting.setText("")
        self.pushButton_min.setText("")
        self.pushButton_close.setText("")
        self.pushButton_scan.setText(QCoreApplication.translate("MainWidget", u"SCAN", None))
        self.pushButton_pageUp.setText("")
        self.pushButton_pageDown.setText("")
        self.label.setText(QCoreApplication.translate("MainWidget", u"SCAN APPS CONCEPT", None))
        self.label_2.setText("")
        self.label_connected_image.setText("")
        self.label_connected.setText(QCoreApplication.translate("MainWidget", u"Found Devices - {}", None))
        self.label_version_image.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWidget", u"V1.0.0.1", None))
    # retranslateUi


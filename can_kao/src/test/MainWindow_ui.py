# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import images_rc
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMaximumSize(QSize(16777215, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 720))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 720))
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.top_blank_widget = QWidget(self.widget)
        self.top_blank_widget.setObjectName(u"top_blank_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_blank_widget.sizePolicy().hasHeightForWidth())
        self.top_blank_widget.setSizePolicy(sizePolicy)
        self.top_blank_widget.setMaximumSize(QSize(16777215, 50))
        self.top_blank_widget.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.top_blank_widget)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.logo_label_2 = QLabel(self.top_blank_widget)
        self.logo_label_2.setObjectName(u"logo_label_2")
        sizePolicy.setHeightForWidth(self.logo_label_2.sizePolicy().hasHeightForWidth())
        self.logo_label_2.setSizePolicy(sizePolicy)
        self.logo_label_2.setMinimumSize(QSize(550, 0))
        self.logo_label_2.setStyleSheet(u"")
        self.logo_label_2.setScaledContents(False)

        self.horizontalLayout_9.addWidget(self.logo_label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.pushButton_min_2 = QPushButton(self.top_blank_widget)
        self.pushButton_min_2.setObjectName(u"pushButton_min_2")
        self.pushButton_min_2.setMinimumSize(QSize(50, 0))
        self.pushButton_min_2.setMaximumSize(QSize(50, 37))
        self.pushButton_min_2.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/images/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_min_2.setIcon(icon)
        self.pushButton_min_2.setIconSize(QSize(14, 50))

        self.horizontalLayout_9.addWidget(self.pushButton_min_2)

        self.pushButton_close_2 = QPushButton(self.top_blank_widget)
        self.pushButton_close_2.setObjectName(u"pushButton_close_2")
        self.pushButton_close_2.setMinimumSize(QSize(50, 0))
        self.pushButton_close_2.setMaximumSize(QSize(50, 37))
        self.pushButton_close_2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close_2.setIcon(icon1)
        self.pushButton_close_2.setIconSize(QSize(12, 12))

        self.horizontalLayout_9.addWidget(self.pushButton_close_2)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)


        self.verticalLayout_10.addWidget(self.top_blank_widget)

        self.verticalSpacer_4 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.main_backgroud = QWidget(self.widget)
        self.main_backgroud.setObjectName(u"main_backgroud")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_backgroud.sizePolicy().hasHeightForWidth())
        self.main_backgroud.setSizePolicy(sizePolicy1)
        self.main_backgroud.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.main_backgroud)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.main_hori_layout_2 = QHBoxLayout()
        self.main_hori_layout_2.setSpacing(0)
        self.main_hori_layout_2.setObjectName(u"main_hori_layout_2")
        self.main_hori_layout_2.setContentsMargins(20, -1, 20, -1)
        self.left_widget_2 = QWidget(self.main_backgroud)
        self.left_widget_2.setObjectName(u"left_widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_widget_2.sizePolicy().hasHeightForWidth())
        self.left_widget_2.setSizePolicy(sizePolicy2)
        self.left_widget_2.setMaximumSize(QSize(16777215, 606))
        self.left_widget_2.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.left_widget_2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(6, 6, 6, 6)
        self.left_left_widget_2 = QWidget(self.left_widget_2)
        self.left_left_widget_2.setObjectName(u"left_left_widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.left_left_widget_2.sizePolicy().hasHeightForWidth())
        self.left_left_widget_2.setSizePolicy(sizePolicy3)
        self.left_left_widget_2.setMinimumSize(QSize(184, 586))
        self.verticalLayout_9 = QVBoxLayout(self.left_left_widget_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.device_list_v_layout_2 = QVBoxLayout()
        self.device_list_v_layout_2.setSpacing(6)
        self.device_list_v_layout_2.setObjectName(u"device_list_v_layout_2")
        self.pushButton_scan_2 = QPushButton(self.left_left_widget_2)
        self.pushButton_scan_2.setObjectName(u"pushButton_scan_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_scan_2.sizePolicy().hasHeightForWidth())
        self.pushButton_scan_2.setSizePolicy(sizePolicy4)
        self.pushButton_scan_2.setMinimumSize(QSize(0, 55))
        self.pushButton_scan_2.setMaximumSize(QSize(170, 55))
        self.pushButton_scan_2.setAutoFillBackground(False)
        self.pushButton_scan_2.setStyleSheet(u"border-image: url(:/icons/images/scan_new.png);\n"
"padding-left: 40px;")
        self.pushButton_scan_2.setIconSize(QSize(40, 40))

        self.device_list_v_layout_2.addWidget(self.pushButton_scan_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.device_list_v_layout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_pageUp_2 = QPushButton(self.left_left_widget_2)
        self.pushButton_pageUp_2.setObjectName(u"pushButton_pageUp_2")
        sizePolicy2.setHeightForWidth(self.pushButton_pageUp_2.sizePolicy().hasHeightForWidth())
        self.pushButton_pageUp_2.setSizePolicy(sizePolicy2)
        self.pushButton_pageUp_2.setMinimumSize(QSize(85, 20))
        self.pushButton_pageUp_2.setMaximumSize(QSize(85, 20))
        self.pushButton_pageUp_2.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/pageUp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_pageUp_2.setIcon(icon2)

        self.horizontalLayout_13.addWidget(self.pushButton_pageUp_2)

        self.pushButton_pageDown_2 = QPushButton(self.left_left_widget_2)
        self.pushButton_pageDown_2.setObjectName(u"pushButton_pageDown_2")
        sizePolicy2.setHeightForWidth(self.pushButton_pageDown_2.sizePolicy().hasHeightForWidth())
        self.pushButton_pageDown_2.setSizePolicy(sizePolicy2)
        self.pushButton_pageDown_2.setMinimumSize(QSize(85, 20))
        self.pushButton_pageDown_2.setMaximumSize(QSize(85, 20))
        self.pushButton_pageDown_2.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/pageDown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_pageDown_2.setIcon(icon3)

        self.horizontalLayout_13.addWidget(self.pushButton_pageDown_2)

        self.horizontalSpacer_11 = QSpacerItem(4, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)


        self.device_list_v_layout_2.addLayout(self.horizontalLayout_13)


        self.verticalLayout_9.addLayout(self.device_list_v_layout_2)


        self.horizontalLayout_12.addWidget(self.left_left_widget_2)

        self.listWidget_2 = QListWidget(self.left_widget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy3.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy3)
        self.listWidget_2.setMinimumSize(QSize(0, 594))
        self.listWidget_2.setMaximumSize(QSize(160, 594))
        self.listWidget_2.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_12.addWidget(self.listWidget_2)


        self.main_hori_layout_2.addWidget(self.left_widget_2)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.main_hori_layout_2.addItem(self.horizontalSpacer_12)

        self.stackedWidget_2 = QStackedWidget(self.main_backgroud)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy5)
        self.stackedWidget_2.setMinimumSize(QSize(0, 606))
        self.stackedWidget_2.setMaximumSize(QSize(16777215, 606))
        self.stackedWidget_2.setStyleSheet(u"")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_14 = QHBoxLayout(self.page_2)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_left_2 = QSpacerItem(19, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_left_2)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"font: 700 30pt \"Microsoft YaHei UI\";\n"
"color: rgb(71, 72, 74);")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_3)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(64, 64))
        self.label_4.setStyleSheet(u"border-image: url(:/icons/images/hook.png);")

        self.horizontalLayout_14.addWidget(self.label_4)

        self.horizontalSpacer_right_2 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_right_2)

        self.stackedWidget_2.addWidget(self.page_2)

        self.main_hori_layout_2.addWidget(self.stackedWidget_2)


        self.verticalLayout_8.addLayout(self.main_hori_layout_2)


        self.verticalLayout_10.addWidget(self.main_backgroud)

        self.verticalSpacer_5 = QSpacerItem(10, 16, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.bottom_blank_widget = QWidget(self.widget)
        self.bottom_blank_widget.setObjectName(u"bottom_blank_widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.bottom_blank_widget.sizePolicy().hasHeightForWidth())
        self.bottom_blank_widget.setSizePolicy(sizePolicy6)
        self.bottom_blank_widget.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.bottom_blank_widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_10 = QSpacerItem(956, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.bottom_info_widget_2 = QWidget(self.bottom_blank_widget)
        self.bottom_info_widget_2.setObjectName(u"bottom_info_widget_2")
        self.bottom_info_widget_2.setMinimumSize(QSize(320, 0))
        self.bottom_info_widget_2.setMaximumSize(QSize(320, 16777215))
        self.bottom_info_widget_2.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.bottom_info_widget_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_connected_image_2 = QLabel(self.bottom_info_widget_2)
        self.label_connected_image_2.setObjectName(u"label_connected_image_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_connected_image_2.sizePolicy().hasHeightForWidth())
        self.label_connected_image_2.setSizePolicy(sizePolicy7)
        self.label_connected_image_2.setMinimumSize(QSize(14, 14))
        self.label_connected_image_2.setMaximumSize(QSize(14, 14))
        self.label_connected_image_2.setPixmap(QPixmap(u":/icons/images/connected.png"))
        self.label_connected_image_2.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_connected_image_2)

        self.label_connected_2 = QLabel(self.bottom_info_widget_2)
        self.label_connected_2.setObjectName(u"label_connected_2")
        sizePolicy7.setHeightForWidth(self.label_connected_2.sizePolicy().hasHeightForWidth())
        self.label_connected_2.setSizePolicy(sizePolicy7)
        self.label_connected_2.setMinimumSize(QSize(130, 14))
        self.label_connected_2.setMaximumSize(QSize(120, 14))
        self.label_connected_2.setStyleSheet(u"color: #a0a0a0;\n"
"font-size: 14px;")
        self.label_connected_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_connected_2)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.label_version_image_2 = QLabel(self.bottom_info_widget_2)
        self.label_version_image_2.setObjectName(u"label_version_image_2")
        sizePolicy7.setHeightForWidth(self.label_version_image_2.sizePolicy().hasHeightForWidth())
        self.label_version_image_2.setSizePolicy(sizePolicy7)
        self.label_version_image_2.setMinimumSize(QSize(14, 14))
        self.label_version_image_2.setMaximumSize(QSize(14, 14))
        self.label_version_image_2.setPixmap(QPixmap(u":/icons/images/version.png"))
        self.label_version_image_2.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_version_image_2)

        self.label_version_2 = QLabel(self.bottom_info_widget_2)
        self.label_version_2.setObjectName(u"label_version_2")
        sizePolicy7.setHeightForWidth(self.label_version_2.sizePolicy().hasHeightForWidth())
        self.label_version_2.setSizePolicy(sizePolicy7)
        self.label_version_2.setMinimumSize(QSize(80, 14))
        self.label_version_2.setMaximumSize(QSize(90, 14))
        self.label_version_2.setStyleSheet(u"color: #a0a0a0;\n"
"font-size: 14px;")
        self.label_version_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_version_2)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_10.addWidget(self.bottom_info_widget_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.verticalLayout_10.addWidget(self.bottom_blank_widget)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label_2.setText("")
        self.pushButton_min_2.setText("")
        self.pushButton_close_2.setText("")
        self.pushButton_scan_2.setText(QCoreApplication.translate("MainWindow", u"SCAN", None))
        self.pushButton_pageUp_2.setText("")
        self.pushButton_pageDown_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SCAN APPS CONCEPT", None))
        self.label_4.setText("")
        self.label_connected_image_2.setText("")
        self.label_connected_2.setText(QCoreApplication.translate("MainWindow", u"Found Devices - 0", None))
        self.label_version_image_2.setText("")
        self.label_version_2.setText(QCoreApplication.translate("MainWindow", u"V1.0.0.1", None))
    # retranslateUi


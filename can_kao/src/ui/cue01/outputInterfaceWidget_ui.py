# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'outputInterfaceWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.components.CustomComboBox import CustomComboBox

class Ui_CUE01_Output_Interface_Widget_Form(object):
    def setupUi(self, CUE01_Output_Interface_Widget_Form):
        if not CUE01_Output_Interface_Widget_Form.objectName():
            CUE01_Output_Interface_Widget_Form.setObjectName(u"CUE01_Output_Interface_Widget_Form")
        CUE01_Output_Interface_Widget_Form.resize(800, 500)
        self.horizontalLayout_9 = QHBoxLayout(CUE01_Output_Interface_Widget_Form)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_9 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line = QFrame(CUE01_Output_Interface_Widget_Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.line_2 = QFrame(CUE01_Output_Interface_Widget_Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.comboBox_pvw_format = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_pvw_format.setObjectName(u"comboBox_pvw_format")
        self.comboBox_pvw_format.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_5.addWidget(self.comboBox_pvw_format)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_6 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(93, 16777215))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.comboBox_pvw_color = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_pvw_color.setObjectName(u"comboBox_pvw_color")
        self.comboBox_pvw_color.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_5.addWidget(self.comboBox_pvw_color)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_5.addWidget(self.label_7)

        self.comboBox_pvw_range = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_pvw_range.setObjectName(u"comboBox_pvw_range")
        self.comboBox_pvw_range.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_5.addWidget(self.comboBox_pvw_range)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_3 = QFrame(CUE01_Output_Interface_Widget_Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.label_2 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_4 = QFrame(CUE01_Output_Interface_Widget_Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_6.addWidget(self.label_8)

        self.comboBox_matte_format = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_matte_format.setObjectName(u"comboBox_matte_format")
        self.comboBox_matte_format.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_6.addWidget(self.comboBox_matte_format)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_9 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(93, 16777215))

        self.horizontalLayout_6.addWidget(self.label_9)

        self.comboBox_matte_color = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_matte_color.setObjectName(u"comboBox_matte_color")
        self.comboBox_matte_color.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_6.addWidget(self.comboBox_matte_color)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_10 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_6.addWidget(self.label_10)

        self.comboBox_matte_range = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_matte_range.setObjectName(u"comboBox_matte_range")
        self.comboBox_matte_range.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_6.addWidget(self.comboBox_matte_range)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_7 = QFrame(CUE01_Output_Interface_Widget_Form)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_7)

        self.label_4 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_8 = QFrame(CUE01_Output_Interface_Widget_Form)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_14 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_8.addWidget(self.label_14)

        self.comboBox_full_format = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_full_format.setObjectName(u"comboBox_full_format")
        self.comboBox_full_format.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_8.addWidget(self.comboBox_full_format)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.label_15 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(93, 16777215))

        self.horizontalLayout_8.addWidget(self.label_15)

        self.comboBox_full_color = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_full_color.setObjectName(u"comboBox_full_color")
        self.comboBox_full_color.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_8.addWidget(self.comboBox_full_color)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_16 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_8.addWidget(self.label_16)

        self.comboBox_full_range = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_full_range.setObjectName(u"comboBox_full_range")
        self.comboBox_full_range.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_8.addWidget(self.comboBox_full_range)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_5 = QFrame(CUE01_Output_Interface_Widget_Form)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.label_3 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.line_6 = QFrame(CUE01_Output_Interface_Widget_Form)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_7.addWidget(self.label_11)

        self.comboBox_pgm_format = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_pgm_format.setObjectName(u"comboBox_pgm_format")
        self.comboBox_pgm_format.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_7.addWidget(self.comboBox_pgm_format)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_12 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(93, 16777215))

        self.horizontalLayout_7.addWidget(self.label_12)

        self.comboBox_pgm_color = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_pgm_color.setObjectName(u"comboBox_pgm_color")
        self.comboBox_pgm_color.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_7.addWidget(self.comboBox_pgm_color)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_13 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_7.addWidget(self.label_13)

        self.comboBox_pgm_range = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_pgm_range.setObjectName(u"comboBox_pgm_range")
        self.comboBox_pgm_range.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_7.addWidget(self.comboBox_pgm_range)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(18)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_aux_ouput = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_aux_ouput.setObjectName(u"comboBox_aux_ouput")
        self.comboBox_aux_ouput.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.comboBox_aux_ouput, 1, 2, 1, 1)

        self.comboBox_output_format = CustomComboBox(CUE01_Output_Interface_Widget_Form)
        self.comboBox_output_format.setObjectName(u"comboBox_output_format")
        self.comboBox_output_format.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.comboBox_output_format, 0, 2, 1, 1)

        self.label_18 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 1, 1, 1, 1)

        self.label_17 = QLabel(CUE01_Output_Interface_Widget_Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_17, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 1, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 0, 3, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.horizontalSpacer_10 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.retranslateUi(CUE01_Output_Interface_Widget_Form)

        QMetaObject.connectSlotsByName(CUE01_Output_Interface_Widget_Form)
    # setupUi

    def retranslateUi(self, CUE01_Output_Interface_Widget_Form):
        CUE01_Output_Interface_Widget_Form.setWindowTitle(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Output PVW", None))
        self.label_5.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Format", None))
        self.label_6.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Color Space", None))
        self.label_7.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Range", None))
        self.label_2.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Output PGM MATTE", None))
        self.label_8.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Format", None))
        self.label_9.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Color Space", None))
        self.label_10.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Range", None))
        self.label_4.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Output PGM FULL", None))
        self.label_14.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Format", None))
        self.label_15.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Color Space", None))
        self.label_16.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Range", None))
        self.label_3.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Output PGM", None))
        self.label_11.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Format", None))
        self.label_12.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Color Space", None))
        self.label_13.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Range", None))
        self.label_18.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Aux Output", None))
        self.label_17.setText(QCoreApplication.translate("CUE01_Output_Interface_Widget_Form", u"Output Format", None))
    # retranslateUi


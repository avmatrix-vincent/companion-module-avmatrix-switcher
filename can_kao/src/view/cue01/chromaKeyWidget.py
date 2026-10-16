import logging

# from qtpy import QtWidgets, QtCore, QtGui
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QSignalBlocker, Qt, QLine, QCoreApplication
from PySide6.QtGui import QPainter, QColor, QPen
from src.model.cue01.cue01Preferences import Cue01Preferences
from superqt import QRangeSlider
from src.components.CustomSingleSlider import CustomSingleSlider
from src.components.SwitchButton import SwitchBtn
from src.components.CustomSpinBox import CustomSpinBox
from src.components.CustomComboBox import CustomComboBox
from src.config.TranslationManager import TranslationManager
from src.config.ChromaConfig import chroma_config
from globals import relative_path, enalbed_range_slider_qss, disabled_range_slider_qss

class ChromaKeyWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(ChromaKeyWidget, self).__init__(parent)
        self._parent = parent
        self.pos_x = 1200
        self.pos_y = 800

    def setupUi(self):
        # _translate = QtCore.QCoreApplication.translate

        _layout = QtWidgets.QGridLayout(self)
        # _layout.setSpacing(5)
        # _layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        # _layout.setContentsMargins(20, 5, 0, 0)

        _fill_srcs = Cue01Preferences.get_chroma_video_sources()
        _key_colors = Cue01Preferences.get_chroma_key_colors()

        """
        Fill Source选择部分
        """
        self._fill_src_groupbox = QtWidgets.QGroupBox()
        # _fill_src_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self._fill_src_groupbox.setObjectName("fillSrcGroupbox")
        self._fill_src_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Fill Source", None))
        # _fill_src_groupbox.setTitle(_translate("fillSrcGroupbox", "键源"))

        _fill_src_groupbox_layout = QtWidgets.QGridLayout()
        _fill_src_groupbox_layout.setHorizontalSpacing(18)
        # _fill_src_groupbox_layout.setContentsMargins(30, 10, 30, 10)
        _fill_src_groupbox_layout.setContentsMargins(50, 10, 90, 0)
        _fill_src_groupbox_layout.setObjectName("fillSrcGroupboxLayout")
        # _fill_src_groupbox_layout.setAlignment(QtCore.Qt.AlignTop)

        self._chroma_status_label = QtWidgets.QLabel(self._fill_src_groupbox)
        self._chroma_status_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Status", None))
        self._chroma_status_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        self._chroma_status_checkbox = QtWidgets.QCheckBox(self._fill_src_groupbox)
        self._chroma_status_checkbox.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Inactive", None))
        self._chroma_status_checkbox.stateChanged.connect(self.chroma_status_changed)

        self._chroma_key_color_label = QtWidgets.QLabel(self._fill_src_groupbox)
        self._chroma_key_color_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Key Color", None))
        self._chroma_key_color_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        self._chroma_key_color_combobox = CustomComboBox(self._fill_src_groupbox)
        self._chroma_key_color_combobox.addItems(_key_colors)
        self._chroma_key_color_combobox.currentIndexChanged.connect(self._select_chroma_key_color)

        self._fill_src_label = QtWidgets.QLabel(self._fill_src_groupbox)
        self._fill_src_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Video Source", None))
        # _fill_src_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"视频源", None))
        self._fill_src_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _fill_src_label.setFixedWidth(80)

        self._fill_src_cb = CustomComboBox(self._fill_src_groupbox)
        for i in range(len(_fill_srcs)):
            self._fill_src_cb.addItem(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", _fill_srcs[i], None))
        self._fill_src_cb.currentIndexChanged[int].connect(self._select_fill_source)

        # 开始Fill Source部分的Grid布局
        _fill_src_groupbox_layout.addWidget(self._chroma_status_label, 0, 0, 1, 1)
        _fill_src_groupbox_layout.addWidget(self._chroma_status_checkbox, 0, 1, 1, 2)
        _fill_src_groupbox_layout.addWidget(self._chroma_key_color_label, 1, 0, 1, 1)
        _fill_src_groupbox_layout.addWidget(self._chroma_key_color_combobox, 1, 1, 1, 2)
        _fill_src_groupbox_layout.addWidget(self._fill_src_label, 2, 0, 1, 1)
        _fill_src_groupbox_layout.addWidget(self._fill_src_cb, 2, 1, 1, 2)

        self._fill_src_groupbox.setLayout(_fill_src_groupbox_layout)

        """
        Fetch选择部分
        """
        self._fetch_groupbox = QtWidgets.QGroupBox()
        # _fetch_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self._fetch_groupbox.setObjectName("fetchGroupbox")
        self._fetch_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Fetch", None))
        # _fetch_groupbox.setTitle(_translate("fetchGroupbox", "色彩采样"))
        # _fetch_groupbox.setFixedWidth(400)

        _fetch_groupbox_layout = QtWidgets.QHBoxLayout()
        _fetch_groupbox_layout.setContentsMargins(50, 20, 20, 10)
        _fetch_groupbox_layout.setObjectName("fetchGroupboxLayout")
        # _fetch_groupbox_layout.setAlignment(QtCore.Qt.AlignTop)

        self._fetch_label = QtWidgets.QLabel(self._fetch_groupbox)
        self._fetch_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Fetch", None))
        # _fetch_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"采样", None))
        self._fetch_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        self._fetch_label.setFixedWidth(35)

        self._fetch_btn = QtWidgets.QPushButton(self._fetch_groupbox)
        self._fetch_btn.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Fetch Manually", None))
        # _fetch_btn.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"手动采样"))
        self._fetch_btn.setFixedWidth(100)
        self._fetch_btn.clicked.connect(self.show_fetch_dialog)
        self._open_fetch_dialog_flag = False

        self._fetch_color_line = QtWidgets.QLineEdit(self._fetch_groupbox)
        self._fetch_color_line.setMinimumWidth(self._fetch_color_line.width())
        self._fetch_color_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._fetch_color_line.setReadOnly(True)
        self._fetch_color_line.setText("x: 0, y: 0;") # RGB(139, 139, 139)
        self._fetch_color_line.setProperty("type", "color_line")

        # 开始Fetch部分的Grid布局
        row = 0
        _fetch_groupbox_layout.addWidget(self._fetch_label)
        _fetch_groupbox_layout.addSpacing(10)
        _fetch_groupbox_layout.addWidget(self._fetch_btn)
        _fetch_groupbox_layout.addWidget(self._fetch_color_line)

        self._fetch_groupbox.setLayout(_fetch_groupbox_layout)

        """
        Color Key的设置
        """
        self._color_key_groupbox = QtWidgets.QGroupBox()
        self._color_key_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self._color_key_groupbox.setObjectName("colorKeyGroupbox")
        self._color_key_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Color Key", None))
        # _color_key_groupbox.setTitle(_translate("colorKeyGroupbox", "色彩键"))
        # _color_key_groupbox.setFixedWidth(400)

        _color_key_groupbox_layout = QtWidgets.QGridLayout()
        _color_key_groupbox_layout.setHorizontalSpacing(18)
        _color_key_groupbox_layout.setContentsMargins(30, 20, 20, 10)
        _color_key_groupbox_layout.setObjectName("colorKeyGroupboxLayout")
        # _color_key_groupbox_layout.setAlignment(QtCore.Qt.AlignTop)

        # Red
        self._color_key_red_label = QtWidgets.QLabel(self._color_key_groupbox)
        self._color_key_red_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Red", None))
        # _color_key_red_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"红", None))
        self._color_key_red_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_key_red_label.setFixedWidth(80)

        self._color_key_red_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_key_groupbox)
        # _color_key_red_slider.setFixedWidth(150)
        self._color_key_red_slider.setRange(0, 255)
        self._color_key_red_slider.setValue(0)
        self._color_key_red_slider.valueChanged.connect(self._color_key_red_slider_value_changed)

        self._color_key_red_spin_box = CustomSpinBox(self._color_key_groupbox)
        # _color_key_red_spin_box.setFixedWidth(50)
        self._color_key_red_spin_box.setRange(0, 255)
        self._color_key_red_spin_box.setValue(0)
        self._color_key_red_spin_box.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self._color_key_red_spin_box.valueChanged.connect(self._color_key_red_spin_box_value_changed)

        # Green
        self._color_key_green_label = QtWidgets.QLabel(self._color_key_groupbox)
        self._color_key_green_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Green", None))
        # _color_key_green_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"绿", None))
        self._color_key_green_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_key_green_label.setFixedWidth(80)

        self._color_key_green_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_key_groupbox)
        # _color_key_green_slider.setFixedWidth(150)
        self._color_key_green_slider.setRange(0, 255)
        self._color_key_green_slider.setValue(0)
        self._color_key_green_slider.valueChanged.connect(self._color_key_green_slider_value_changed)

        self._color_key_green_spin_box = CustomSpinBox(self._color_key_groupbox)
        # _color_key_green_spin_box.setFixedWidth(50)
        self._color_key_green_spin_box.setRange(0, 255)
        self._color_key_green_spin_box.setValue(0)
        self._color_key_green_spin_box.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self._color_key_green_spin_box.valueChanged.connect(self._color_key_green_spin_box_value_changed)

        # Blue
        self._color_key_blue_label = QtWidgets.QLabel(self._color_key_groupbox)
        self._color_key_blue_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Blue", None))
        # _color_key_blue_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"蓝", None))
        self._color_key_blue_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_key_blue_label.setFixedWidth(80)

        self._color_key_blue_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_key_groupbox)
        # _color_key_blue_slider.setFixedWidth(150)
        self._color_key_blue_slider.setRange(0, 255)
        self._color_key_blue_slider.setValue(0)
        self._color_key_blue_slider.valueChanged.connect(self._color_key_blue_slider_value_changed)

        self._color_key_blue_spin_box = CustomSpinBox(self._color_key_groupbox)
        # _color_key_blue_spin_box.setFixedWidth(50)
        self._color_key_blue_spin_box.setRange(0, 255)
        self._color_key_blue_spin_box.setValue(0)
        self._color_key_blue_spin_box.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self._color_key_blue_spin_box.valueChanged.connect(self._color_key_blue_spin_box_value_changed)

        # Angle
        self._color_key_angle_label = QtWidgets.QLabel(self._color_key_groupbox)
        self._color_key_angle_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Angle", None))
        # _color_key_angle_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"角度", None))
        self._color_key_angle_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_key_angle_label.setFixedWidth(80)

        self._color_key_angle_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_key_groupbox)
        # _color_key_angle_slider.setFixedWidth(150)
        self._color_key_angle_slider.setRange(0, 180)
        self._color_key_angle_slider.setValue(0)
        self._color_key_angle_slider.valueChanged.connect(self._color_key_angle_slider_value_changed)

        self._color_key_angle_spin_box = CustomSpinBox(self._color_key_groupbox)
        # _color_key_angle_spin_box.setFixedWidth(50)
        self._color_key_angle_spin_box.setRange(0, 180)
        self._color_key_angle_spin_box.setValue(0)
        self._color_key_angle_spin_box.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self._color_key_angle_spin_box.valueChanged.connect(self._color_key_angle_spin_box_value_changed)

        # Tolerance
        self._color_key_tolerance_label = QtWidgets.QLabel(self._color_key_groupbox)
        self._color_key_tolerance_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Tolerance", None))
        # _color_key_tolerance_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"容忍度", None))
        self._color_key_tolerance_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_key_tolerance_label.setFixedWidth(80)

        self._color_key_tolerance_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_key_groupbox)
        # _color_key_tolerance_slider.setFixedWidth(150)
        self._color_key_tolerance_slider.setRange(0, 100)
        self._color_key_tolerance_slider.setValue(0)
        self._color_key_tolerance_slider.valueChanged.connect(self._color_key_tolerance_slider_value_changed)

        self._color_key_tolerance_spin_box = CustomSpinBox(self._color_key_groupbox)
        # _color_key_tolerance_spin_box.setFixedWidth(50)
        self._color_key_tolerance_spin_box.setRange(0, 100)
        self._color_key_tolerance_spin_box.setValue(0)
        self._color_key_tolerance_spin_box.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self._color_key_tolerance_spin_box.valueChanged.connect(self._color_key_tolerance_spin_box_value_changed)

        # Softness
        self._color_key_softness_label = QtWidgets.QLabel(self._color_key_groupbox)
        self._color_key_softness_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Softness", None))
        # _color_key_softness_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"柔化度", None))
        self._color_key_softness_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_key_softness_label.setFixedWidth(80)

        self._color_key_softness_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_key_groupbox)
        # _color_key_softness_slider.setFixedWidth(150)
        self._color_key_softness_slider.setRange(0, 100)
        self._color_key_softness_slider.setValue(0)
        self._color_key_softness_slider.valueChanged.connect(self._color_key_softness_slider_value_changed)

        self._color_key_softness_spin_box = CustomSpinBox(self._color_key_groupbox)
        # _color_key_softness_spin_box.setFixedWidth(50)
        self._color_key_softness_spin_box.setRange(0, 100)
        self._color_key_softness_spin_box.setValue(0)
        self._color_key_softness_spin_box.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self._color_key_softness_spin_box.valueChanged.connect(self._color_key_softness_spin_box_value_changed)

        # 开始Color Key部分的Grid布局
        row = 0
        _color_key_groupbox_layout.addWidget(self._color_key_red_label, row, 0, 1, 1)
        _color_key_groupbox_layout.addWidget(self._color_key_red_slider, row, 1, 1, 3)
        _color_key_groupbox_layout.addWidget(self._color_key_red_spin_box, row, 4, 1, 1)

        row += 1
        _color_key_groupbox_layout.addWidget(self._color_key_green_label, row, 0, 1, 1)
        _color_key_groupbox_layout.addWidget(self._color_key_green_slider, row, 1, 1, 3)
        _color_key_groupbox_layout.addWidget(self._color_key_green_spin_box, row, 4, 1, 1)

        row += 1
        _color_key_groupbox_layout.addWidget(self._color_key_blue_label, row, 0, 1, 1)
        _color_key_groupbox_layout.addWidget(self._color_key_blue_slider, row, 1, 1, 3)
        _color_key_groupbox_layout.addWidget(self._color_key_blue_spin_box, row, 4, 1, 1)

        row += 1
        _color_key_groupbox_layout.addWidget(self._color_key_angle_label, row, 0, 1, 1)
        _color_key_groupbox_layout.addWidget(self._color_key_angle_slider, row, 1, 1, 3)
        _color_key_groupbox_layout.addWidget(self._color_key_angle_spin_box, row, 4, 1, 1)

        row += 1
        _color_key_groupbox_layout.addWidget(self._color_key_tolerance_label, row, 0, 1, 1)
        _color_key_groupbox_layout.addWidget(self._color_key_tolerance_slider, row, 1, 1, 3)
        _color_key_groupbox_layout.addWidget(self._color_key_tolerance_spin_box, row, 4, 1, 1)

        row += 1
        _color_key_groupbox_layout.addWidget(self._color_key_softness_label, row, 0, 1, 1)
        _color_key_groupbox_layout.addWidget(self._color_key_softness_slider, row, 1, 1, 3)
        _color_key_groupbox_layout.addWidget(self._color_key_softness_spin_box, row, 4, 1, 1)

        self._color_key_groupbox.setLayout(_color_key_groupbox_layout)

        """
        Chroma Key Setting
        """
        self._key_setting_groupbox = QtWidgets.QGroupBox()
        # _key_setting_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self._key_setting_groupbox.setObjectName("keySettingGroupbox")
        self._key_setting_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Key Setting", None))
        # _key_setting_groupbox.setTitle(_translate("keySettingGroupbox", "键设置"))
        # _key_setting_groupbox.setFixedWidth(400)

        _key_setting_groupbox_layout = QtWidgets.QGridLayout()
        _key_setting_groupbox_layout.setHorizontalSpacing(18)
        _key_setting_groupbox_layout.setContentsMargins(10, 15, 20, 5)
        _key_setting_groupbox_layout.setObjectName("keySettingGroupboxLayout")
        # _key_setting_groupbox_layout.setAlignment(QtCore.Qt.AlignTop)

        self._key_setting_foreground_label = QtWidgets.QLabel(self._key_setting_groupbox)
        self._key_setting_foreground_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Foreground", None))
        # _key_setting_foreground_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"前景", None))
        self._key_setting_foreground_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _key_setting_foreground_label.setFixedWidth(80)

        self._key_setting_foreground_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._key_setting_groupbox)
        # _key_setting_foreground_slider.setFixedWidth(150)
        self._key_setting_foreground_slider.setRange(0, 1000)
        self._key_setting_foreground_slider.setValue(0)
        self._key_setting_foreground_slider.valueChanged.connect(self._on_key_setting_foreground_slider_value_changed)

        self._key_setting_foreground_line_edit = QtWidgets.QLineEdit(self._key_setting_groupbox)
        self._key_setting_foreground_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._key_setting_foreground_line_edit.setFixedWidth(50)
        self._key_setting_foreground_line_edit.setText("0.0%")
        self._key_setting_foreground_line_edit.setReadOnly(True)

        self._key_setting_background_label = QtWidgets.QLabel(self._key_setting_groupbox)
        self._key_setting_background_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Background", None))
        # _key_setting_background_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"背景", None))
        self._key_setting_background_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _key_setting_background_label.setFixedWidth(80)

        self._key_setting_background_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._key_setting_groupbox)
        # _key_setting_background_slider.setFixedWidth(150)
        self._key_setting_background_slider.setRange(0, 1000)
        self._key_setting_background_slider.setValue(0)
        self._key_setting_background_slider.valueChanged.connect(self._on_key_setting_background_slider_value_changed)

        self._key_setting_background_line_edit = QtWidgets.QLineEdit(self._key_setting_groupbox)
        self._key_setting_background_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._key_setting_background_line_edit.setFixedWidth(50)
        self._key_setting_background_line_edit.setText("0.0%")
        self._key_setting_background_line_edit.setReadOnly(True)

        self._key_setting_key_edge_label = QtWidgets.QLabel(self._key_setting_groupbox)
        self._key_setting_key_edge_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Key Edge", None))
        # _key_setting_key_edge_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"边缘", None))
        self._key_setting_key_edge_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _key_setting_key_edge_label.setFixedWidth(80)

        self._key_setting_key_edge_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._key_setting_groupbox)
        # _key_setting_key_edge_slider.setFixedWidth(150)
        self._key_setting_key_edge_slider.setRange(0, 1000)
        self._key_setting_key_edge_slider.setValue(0)
        self._key_setting_key_edge_slider.valueChanged.connect(self._on_key_setting_key_edge_slider_value_changed)

        self._key_setting_key_edge_line_edit = QtWidgets.QLineEdit(self._key_setting_groupbox)
        self._key_setting_key_edge_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._key_setting_key_edge_line_edit.setFixedWidth(50)
        self._key_setting_key_edge_line_edit.setText("0.0%")
        self._key_setting_key_edge_line_edit.setReadOnly(True)

        # 开始Key Setting部分的Grid布局
        row = 0
        _key_setting_groupbox_layout.addWidget(self._key_setting_foreground_label, row, 0, 1, 1)
        _key_setting_groupbox_layout.addWidget(self._key_setting_foreground_slider, row, 1, 1, 3)
        _key_setting_groupbox_layout.addWidget(self._key_setting_foreground_line_edit, row, 4, 1, 1)

        row += 1
        _key_setting_groupbox_layout.addWidget(self._key_setting_background_label, row, 0, 1, 1)
        _key_setting_groupbox_layout.addWidget(self._key_setting_background_slider, row, 1, 1, 3)
        _key_setting_groupbox_layout.addWidget(self._key_setting_background_line_edit, row, 4, 1, 1)

        row += 1
        _key_setting_groupbox_layout.addWidget(self._key_setting_key_edge_label, row, 0, 1, 1)
        _key_setting_groupbox_layout.addWidget(self._key_setting_key_edge_slider, row, 1, 1, 3)
        _key_setting_groupbox_layout.addWidget(self._key_setting_key_edge_line_edit, row, 4, 1, 1)

        self._key_setting_groupbox.setLayout(_key_setting_groupbox_layout)

        self._key_setting_groupbox.hide()

        """
        Chroma Key Clip
        """
        self._key_clip_groupbox = QtWidgets.QGroupBox()
        # _key_clip_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self._key_clip_groupbox.setObjectName("keyClipGroupbox")
        self._key_clip_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Key Clip", None))
        # _key_clip_groupbox.setTitle(_translate("keyClipGroupbox", "限幅"))
        # _key_clip_groupbox.setFixedWidth(400)

        _key_clip_groupbox_layout = QtWidgets.QGridLayout()
        _key_clip_groupbox_layout.setContentsMargins(40, 5, 15, 10)
        _key_clip_groupbox_layout.setObjectName("keyClipGroupboxLayout")
        _key_clip_groupbox_layout.setHorizontalSpacing(18)
        # _key_clip_groupbox_layout.setAlignment(QtCore.Qt.AlignTop)

        # Key Clip使能
        self._key_clip_switch_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Clip On/Off", None))
        # _key_clip_switch_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"开/关", None))
        self._key_clip_switch_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _key_clip_switch_label.setFixedSize(100, 40)

        self._key_clip_switch_btn = SwitchBtn()
        self._key_clip_switch_btn.checkedChanged.connect(self._on_key_clip_switch_rbtn_clicked)

        # Key Clip Curve使能
        self._key_clip_curve_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Curve On/Off", None))
        # _key_clip_curve_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"曲线 开/关", None))
        self._key_clip_curve_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _key_clip_curve_label.setFixedSize(100, 40)

        self._key_curve_switch_btn = SwitchBtn()
        self._key_curve_switch_btn.checkedChanged.connect(self._on_key_clip_curve_rbtn_clicked)

        # Key Clip range
        self._key_clip_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Key Clip", None))
        # _key_clip_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"限幅", None))
        self._key_clip_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _key_clip_label.setFixedSize(100, 40)

        self._key_clip_left_value = QtWidgets.QLabel("0.0%")
        self._key_clip_left_value.setAlignment(QtCore.Qt.AlignCenter)
        # _key_clip_left_value.setFixedSize(50, 40)

        self._key_clip_right_value = QtWidgets.QLabel("100.0%")
        self._key_clip_right_value.setAlignment(QtCore.Qt.AlignCenter)
        # _key_clip_right_value.setFixedSize(50, 40)

        self._key_clip_range_slider = QRangeSlider(QtCore.Qt.Orientation.Horizontal)
        self._key_clip_range_slider.setBarMovesAllHandles(False)
        self._key_clip_range_slider.setRange(0, 1000)
        self._key_clip_range_slider.setValue((200, 800))
        self._key_clip_range_slider.valueChanged.connect(self._on_key_clip_range_slider_value_changed)
        # _key_clip_range_slider.setFixedWidth(160)

        # 开始Chroma Key Clip部分的布局
        _clip_switch_layout = QtWidgets.QHBoxLayout()
        _clip_switch_layout.setContentsMargins(20, 20, 15, 5)
        _clip_switch_layout.addWidget(self._key_clip_switch_label)
        _clip_switch_layout.addSpacing(8)
        _clip_switch_layout.addWidget(self._key_clip_switch_btn)
        _clip_switch_layout.addStretch()
        _clip_switch_layout.addWidget(self._key_clip_curve_label)
        _clip_switch_layout.addSpacing(8)
        _clip_switch_layout.addWidget(self._key_curve_switch_btn)

        # row = 0
        # _key_clip_groupbox_layout.addWidget(_key_clip_switch_label, row, 0, 1, 1)
        # _key_clip_groupbox_layout.addWidget(_key_clip_switch_btn, row, 1, 1, 1)

        # # row += 1
        # _key_clip_groupbox_layout.addWidget(_key_clip_curve_label, row, 2, 1, 1)
        # _key_clip_groupbox_layout.addWidget(_key_curve_switch_btn, row, 3, 1, 1)

        # row += 1
        row = 0
        _key_clip_groupbox_layout.addWidget(self._key_clip_label, row, 0, 1, 1)
        _key_clip_groupbox_layout.addWidget(self._key_clip_left_value, row, 1, 1, 1)
        _key_clip_groupbox_layout.addWidget(self._key_clip_range_slider, row, 2, 1, 1)
        _key_clip_groupbox_layout.addWidget(self._key_clip_right_value, row, 3, 1, 1)

        keyclip_main_layout = QtWidgets.QVBoxLayout()
        keyclip_main_layout.addLayout(_clip_switch_layout)
        keyclip_main_layout.addLayout(_key_clip_groupbox_layout)

        # _key_clip_groupbox.setLayout(_key_clip_groupbox_layout)
        self._key_clip_groupbox.setLayout(keyclip_main_layout)

        """
        设置Chroma Spill Correction
        """
        self._spill_correction_groupbox = QtWidgets.QGroupBox()
        # _spill_correction_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self._spill_correction_groupbox.setObjectName("spillCorrectionGroupbox")
        self._spill_correction_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Spill Correction", None))
        # _spill_correction_groupbox.setTitle(_translate("spillCorrectionGroupbox", "溢出校正"))
        # _spill_correction_groupbox.setFixedWidth(400)

        _spill_correction_groupbox_layout = QtWidgets.QGridLayout()
        _spill_correction_groupbox_layout.setHorizontalSpacing(18)
        _spill_correction_groupbox_layout.setContentsMargins(3, 5, 10, 5)
        _spill_correction_groupbox_layout.setObjectName("spillCorrectionGroupboxLayout")
        # _spill_correction_groupbox_layout.setAlignment(QtCore.Qt.AlignTop)

        # Spill Correction使能
        self._spill_switch_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill On/Off", None))
        # _spill_switch_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"开/关", None))
        self._spill_switch_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _spill_switch_label.setFixedSize(100, 40)

        self._spill_switch_btn = SwitchBtn(self._spill_correction_groupbox)
        self._spill_switch_btn.checkedChanged.connect(self._on_spill_switch_rbtn_clicked)

        self._spill_edge_label = QtWidgets.QLabel(self._spill_correction_groupbox)
        self._spill_edge_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill Edge", None))
        # _spill_edge_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"边缘溢出", None))
        self._spill_edge_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _spill_edge_label.setFixedWidth(80)

        self._spill_edge_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._spill_correction_groupbox)
        # _spill_edge_slider.setFixedWidth(150)
        self._spill_edge_slider.setRange(0, 1000)
        self._spill_edge_slider.setValue(0)
        self._spill_edge_slider.valueChanged.connect(self._on_spill_edge_slider_value_changed)

        self._spill_edge_line_edit = QtWidgets.QLineEdit(self._spill_correction_groupbox)
        self._spill_edge_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._spill_edge_line_edit.setFixedWidth(50)
        self._spill_edge_line_edit.setText("0")
        self._spill_edge_line_edit.setReadOnly(True)

        self._spill_background_label = QtWidgets.QLabel(self._spill_correction_groupbox)
        self._spill_background_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Background", None))
        # _spill_background_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"背景", None))
        self._spill_background_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _spill_background_label.setFixedWidth(80)

        self._spill_background_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._spill_correction_groupbox)
        # _spill_background_slider.setFixedWidth(150)
        self._spill_background_slider.setRange(0, 1000)
        self._spill_background_slider.setValue(0)
        self._spill_background_slider.valueChanged.connect(self._on_spill_background_slider_value_changed)

        self._spill_background_line_edit = QtWidgets.QLineEdit(self._spill_correction_groupbox)
        self._spill_background_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._spill_background_line_edit.setFixedWidth(50)
        self._spill_background_line_edit.setText("0")
        self._spill_background_line_edit.setReadOnly(True)

        # 开始Chroma Spill Correction部分的Grid布局

        _spill_collection_switch_layout = QtWidgets.QHBoxLayout()
        _spill_collection_switch_layout.setContentsMargins(0, 15, 270, 0)
        _spill_collection_switch_layout.addWidget(self._spill_switch_label)
        _spill_collection_switch_layout.addSpacing(5)
        _spill_collection_switch_layout.addWidget(self._spill_switch_btn)

        # row = 0
        # _spill_correction_groupbox_layout.addWidget(_spill_switch_label, row, 0, 1, 1)
        # _spill_correction_groupbox_layout.addWidget(_spill_switch_btn, row, 1, 1, 1)

        # row += 1
        row = 0
        _spill_correction_groupbox_layout.addWidget(self._spill_edge_label, row, 0, 1, 1)
        _spill_correction_groupbox_layout.addWidget(self._spill_edge_slider, row, 1, 1, 3)
        _spill_correction_groupbox_layout.addWidget(self._spill_edge_line_edit, row, 4, 1, 1)

        row += 1
        _spill_correction_groupbox_layout.addWidget(self._spill_background_label, row, 0, 1, 1)
        _spill_correction_groupbox_layout.addWidget(self._spill_background_slider, row, 1, 1, 3)
        _spill_correction_groupbox_layout.addWidget(self._spill_background_line_edit, row, 4, 1, 1)

        _spill_correction_main_layout = QtWidgets.QVBoxLayout()
        _spill_correction_main_layout.addLayout(_spill_collection_switch_layout)
        _spill_correction_main_layout.addLayout(_spill_correction_groupbox_layout)

        self._spill_correction_groupbox.setLayout(_spill_correction_main_layout)

        """
        设置Chroma Spill Correction2
        """
        self._spill_correction2_groupbox = QtWidgets.QGroupBox()
        # _spill_correction2_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self._spill_correction2_groupbox.setObjectName("spillCorrection2Groupbox")
        self._spill_correction2_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Spill Correction2", None))
        # _spill_correction2_groupbox.setTitle(_translate("spillCorrection2Groupbox", "溢出校正2", None))
        # _spill_correction2_groupbox.setFixedWidth(400)

        _spill_correction2_groupbox_layout = QtWidgets.QGridLayout()
        _spill_correction2_groupbox_layout.setContentsMargins(25, 0, 50, 5)
        _spill_correction2_groupbox_layout.setObjectName("spillCorrection2GroupboxLayout")
        # _spill_correction2_groupbox_layout.setAlignment(QtCore.Qt.AlignTop)

        # Spill Correction2使能
        self._spill2_switch_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill2 On/Off", None))
        # _spill2_switch_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"开/关", None))
        self._spill2_switch_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _spill2_switch_label.setFixedSize(100, 40)

        self._spill2_switch_btn = SwitchBtn(self._spill_correction2_groupbox)
        self._spill2_switch_btn.checkedChanged.connect(self._on_spill2_switch_rbtn_clicked)

        # Spill2颜色
        self._spill2_color_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill2 Color", None))
        # _spill2_color_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"溢出颜色", None))
        self._spill2_color_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _spill2_color_label.setFixedSize(100, 40)

        _spill2_colors = Cue01Preferences.get_spill_correction2_colors()
        self._spill2_color_cb = CustomComboBox(self._spill_correction2_groupbox)
        for i in range(len(_spill2_colors)):
            self._spill2_color_cb.addItem(_spill2_colors[i])
        self._spill2_color_cb.currentIndexChanged[int].connect(self._select_spill2_color)

        # Spill2 Value
        self._spill2_value_left_label = QtWidgets.QLabel(self._spill_correction2_groupbox)
        self._spill2_value_left_label.setText("-")
        self._spill2_value_left_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _spill2_value_left_label.setFixedWidth(20)

        self._spill2_value_right_label = QtWidgets.QLabel(self._spill_correction2_groupbox)
        self._spill2_value_right_label.setText("-")
        self._spill2_value_right_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        # _spill2_value_right_label.setFixedWidth(20)

        self._spill2_value_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._spill_correction2_groupbox)
        # _spill2_value_slider.setFixedWidth(260)
        self._spill2_value_slider.setRange(0, 20000)
        self._spill2_value_slider.setValue(10000)
        self._spill2_value_slider.setSingleStep(5)
        self._spill2_value_slider.valueChanged.connect(self._on_spill2_value_slider_value_changed)

        self._spill2_value_line_edit = QtWidgets.QLineEdit(self._spill_correction2_groupbox)
        self._spill2_value_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._spill2_value_line_edit.setFixedWidth(50)
        self._spill2_value_line_edit.setText("0")
        self._spill2_value_line_edit.setReadOnly(True)

        # Spill2复位
        self._spill2_reset_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill2 Reset", None))
        # _spill2_reset_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"溢出重置", None))
        self._spill2_reset_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _spill2_reset_label.setFixedSize(100, 40)

        self._spill2_reset_btn = QtWidgets.QPushButton(self._spill_correction2_groupbox)
        self._spill2_reset_btn.setFixedWidth(70)
        self._spill2_reset_btn.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Reset", None))
        # _spill2_reset_btn.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"重置", None))
        self._spill2_reset_btn.clicked.connect(self._on_spill2_reset_btn_clicked)

        _spill_correction2_groupbox_layout.setHorizontalSpacing(18)

        _spill_switch_layout = QtWidgets.QHBoxLayout()
        _spill_switch_layout.setContentsMargins(0, 10, 253, 0)
        _spill_switch_layout.addWidget(self._spill2_switch_label)
        _spill_switch_layout.addSpacing(8)
        _spill_switch_layout.addWidget(self._spill2_switch_btn)

        # 开始Chroma Spill Correction2部分的Grid布局
        # row = 0
        # _spill_correction2_groupbox_layout.addWidget(_spill2_switch_label, row, 0, 1, 1)
        # _spill_correction2_groupbox_layout.addWidget(_spill2_switch_btn, row, 1, 1, 1)

        # row += 1
        row = 0
        _spill_correction2_groupbox_layout.addWidget(self._spill2_color_label, row, 0, 1, 1)
        _spill_correction2_groupbox_layout.addWidget(self._spill2_color_cb, row, 1, 1, 4)

        row += 1
        _spill_correction2_groupbox_layout.addWidget(self._spill2_value_left_label, row, 0, 1, 1)
        _spill_correction2_groupbox_layout.addWidget(self._spill2_value_slider, row, 1, 1, 3)
        _spill_correction2_groupbox_layout.addWidget(self._spill2_value_right_label, row, 4, 1, 1)
        _spill_correction2_groupbox_layout.addWidget(self._spill2_value_line_edit, row, 5, 1, 1)

        row += 1
        _spill_correction2_groupbox_layout.addWidget(self._spill2_reset_label, row, 0, 1, 1)
        _spill_correction2_groupbox_layout.addWidget(self._spill2_reset_btn, row, 1, 1, 3)

        _spill_collection2_main_layout = QtWidgets.QVBoxLayout()
        _spill_collection2_main_layout.addLayout(_spill_switch_layout)
        _spill_collection2_main_layout.addLayout(_spill_correction2_groupbox_layout)

        self._spill_correction2_groupbox.setLayout(_spill_collection2_main_layout)

        """
        Chroma Color Adjustment
        """
        self._color_adjustment_groupbox = QtWidgets.QGroupBox()
        # _color_adjustment_groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self._color_adjustment_groupbox.setObjectName("colorAdjustmentGroupbox")
        self._color_adjustment_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Color Adjustment", None))
        # _color_adjustment_groupbox.setTitle(_translate("colorAdjustmentGroupbox", "色彩调整"))
        # _color_adjustment_groupbox.setFixedWidth(400)

        _color_adjustment_groupbox_layout = QtWidgets.QGridLayout()
        _color_adjustment_groupbox_layout.setHorizontalSpacing(18)
        _color_adjustment_groupbox_layout.setContentsMargins(10, 20, 20, 10)
        _color_adjustment_groupbox_layout.setObjectName("colorAdjustmentGroupboxLayout")
        # _color_adjustment_groupbox_layout.setAlignment(QtCore.Qt.AlignTop)

        # Brightness
        self._color_adj_brightness_label = QtWidgets.QLabel(self._color_adjustment_groupbox)
        self._color_adj_brightness_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Brightness", None))
        # _color_adj_brightness_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"亮度", None))
        self._color_adj_brightness_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_adj_brightness_label.setFixedWidth(80)

        self._color_adj_brightness_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_adjustment_groupbox)
        # _color_adj_brightness_slider.setFixedWidth(150)
        self._color_adj_brightness_slider.setRange(0, 200)
        self._color_adj_brightness_slider.setValue(0)
        self._color_adj_brightness_slider.valueChanged.connect(self._on_color_adj_brightness_slider_value_changed)

        self._color_adj_brightness_line_edit = QtWidgets.QLineEdit(self._color_adjustment_groupbox)
        self._color_adj_brightness_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._color_adj_brightness_line_edit.setFixedWidth(50)
        self._color_adj_brightness_line_edit.setText("0.0%")
        self._color_adj_brightness_line_edit.setReadOnly(True)

        # Contract
        self._color_adj_contract_label = QtWidgets.QLabel(self._color_adjustment_groupbox)
        self._color_adj_contract_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Contract", None))
        # _color_adj_contract_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"对比度", None))
        self._color_adj_contract_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_adj_contract_label.setFixedWidth(80)

        self._color_adj_contract_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_adjustment_groupbox)
        # _color_adj_contract_slider.setFixedWidth(150)
        self._color_adj_contract_slider.setRange(0, 200)
        self._color_adj_contract_slider.setValue(0)
        self._color_adj_contract_slider.valueChanged.connect(self._on_color_adj_contract_slider_value_changed)

        self._color_adj_contract_line_edit = QtWidgets.QLineEdit(self._color_adjustment_groupbox)
        self._color_adj_contract_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._color_adj_contract_line_edit.setFixedWidth(50)
        self._color_adj_contract_line_edit.setText("0.0%")
        self._color_adj_contract_line_edit.setReadOnly(True)

        # Saturation
        self._color_adj_saturation_label = QtWidgets.QLabel(self._color_adjustment_groupbox)
        self._color_adj_saturation_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Saturation", None))
        # _color_adj_saturation_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"饱和度", None))
        self._color_adj_saturation_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_adj_saturation_label.setFixedWidth(80)

        self._color_adj_saturation_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_adjustment_groupbox)
        # _color_adj_saturation_slider.setFixedWidth(150)
        self._color_adj_saturation_slider.setRange(0, 200)
        self._color_adj_saturation_slider.setValue(0)
        self._color_adj_saturation_slider.valueChanged.connect(self._on_color_adj_saturation_slider_value_changed)

        self._color_adj_saturation_line_edit = QtWidgets.QLineEdit(self._color_adjustment_groupbox)
        self._color_adj_saturation_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._color_adj_saturation_line_edit.setFixedWidth(50)
        self._color_adj_saturation_line_edit.setText("0.0%")
        self._color_adj_saturation_line_edit.setReadOnly(True)

        # Red
        self._color_adj_red_label = QtWidgets.QLabel(self._color_adjustment_groupbox)
        self._color_adj_red_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Red", None))
        # _color_adj_red_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"红", None))
        self._color_adj_red_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_adj_red_label.setFixedWidth(80)

        self._color_adj_red_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_adjustment_groupbox)
        # _color_adj_red_slider.setFixedWidth(150)
        self._color_adj_red_slider.setRange(0, 200)
        self._color_adj_red_slider.setValue(0)
        self._color_adj_red_slider.valueChanged.connect(self._on_color_adj_red_slider_value_changed)

        self._color_adj_red_line_edit = QtWidgets.QLineEdit(self._color_adjustment_groupbox)
        self._color_adj_red_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._color_adj_red_line_edit.setFixedWidth(50)
        self._color_adj_red_line_edit.setText("0.0%")
        self._color_adj_red_line_edit.setReadOnly(True)

        # Green
        self._color_adj_green_label = QtWidgets.QLabel(self._color_adjustment_groupbox)
        self._color_adj_green_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Green", None))
        # _color_adj_green_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"绿", None))
        self._color_adj_green_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_adj_green_label.setFixedWidth(80)

        self._color_adj_green_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_adjustment_groupbox)
        # _color_adj_green_slider.setFixedWidth(150)
        self._color_adj_green_slider.setRange(0, 200)
        self._color_adj_green_slider.setValue(0)
        self._color_adj_green_slider.valueChanged.connect(self._on_color_adj_green_slider_value_changed)

        self._color_adj_green_line_edit = QtWidgets.QLineEdit(self._color_adjustment_groupbox)
        self._color_adj_green_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._color_adj_green_line_edit.setFixedWidth(50)
        self._color_adj_green_line_edit.setText("0.0%")
        self._color_adj_green_line_edit.setReadOnly(True)

        # Blue
        self._color_adj_blue_label = QtWidgets.QLabel(self._color_adjustment_groupbox)
        self._color_adj_blue_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Blue", None))
        # _color_adj_blue_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"蓝", None))
        self._color_adj_blue_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_adj_blue_label.setFixedWidth(80)

        self._color_adj_blue_slider = CustomSingleSlider(QtCore.Qt.Horizontal, self._color_adjustment_groupbox)
        # _color_adj_blue_slider.setFixedWidth(150)
        self._color_adj_blue_slider.setRange(0, 200)
        self._color_adj_blue_slider.setValue(0)
        self._color_adj_blue_slider.valueChanged.connect(self._on_color_adj_blue_slider_value_changed)

        self._color_adj_blue_line_edit = QtWidgets.QLineEdit(self._color_adjustment_groupbox)
        self._color_adj_blue_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self._color_adj_blue_line_edit.setFixedWidth(50)
        self._color_adj_blue_line_edit.setText("0.0%")
        self._color_adj_blue_line_edit.setReadOnly(True)

        # Reset
        self._color_adj_reset_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Reset", None))
        # _color_adj_reset_label = QtWidgets.QLabel(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"重置", None))
        self._color_adj_reset_label.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        # _color_adj_reset_label.setFixedWidth(80)

        self._color_adj_reset_btn = QtWidgets.QPushButton(self._color_adjustment_groupbox)
        self._color_adj_reset_btn.setFixedWidth(70)
        self._color_adj_reset_btn.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Reset", None))
        # _color_adj_reset_btn.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"重置", None))
        self._color_adj_reset_btn.clicked.connect(self._on_color_adj_reset_btn_clicked)

        # Chroma Color Adjustment布局
        row = 0
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_brightness_label, row, 0, 1, 1)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_brightness_slider, row, 1, 1, 3)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_brightness_line_edit, row, 4, 1, 1)

        row += 1
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_contract_label, row, 0, 1, 1)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_contract_slider, row, 1, 1, 3)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_contract_line_edit, row, 4, 1, 1)

        row += 1
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_saturation_label, row, 0, 1, 1)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_saturation_slider, row, 1, 1, 3)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_saturation_line_edit, row, 4, 1, 1)

        row += 1
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_red_label, row, 0, 1, 1)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_red_slider, row, 1, 1, 3)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_red_line_edit, row, 4, 1, 1)

        row += 1
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_green_label, row, 0, 1, 1)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_green_slider, row, 1, 1, 3)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_green_line_edit, row, 4, 1, 1)

        row += 1
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_blue_label, row, 0, 1, 1)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_blue_slider, row, 1, 1, 3)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_blue_line_edit, row, 4, 1, 1)

        row += 1
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_reset_label, row, 0, 1, 1)
        _color_adjustment_groupbox_layout.addWidget(self._color_adj_reset_btn, row, 1, 1, 3)

        self._color_adjustment_groupbox.setLayout(_color_adjustment_groupbox_layout)

        """
        页面整体布局
        """
        # row = 0
        # _layout.addWidget(_fill_src_groupbox, row, 0, 1, 1)
        # _layout.addWidget(_fetch_groupbox, row, 1, 1, 1)

        # row += 1
        # _layout.addWidget(_color_key_groupbox, row, 0, 3, 1)
        # _layout.addWidget(_key_setting_groupbox, row, 1, 2, 1)

        # row += 1
        # _layout.addWidget(_key_clip_groupbox, row+2, 0, 2, 1)
        # _layout.addWidget(_spill_correction_groupbox, row+1, 1, 2, 1)

        # row += 1
        # _layout.addWidget(_spill_correction2_groupbox, row+3, 0, 3, 1)
        # _layout.addWidget(_color_adjustment_groupbox, row+2, 1, 4, 1)

        # 第一列
        _layout.addWidget(self._fill_src_groupbox, 0, 0, 2, 1)
        _layout.addWidget(self._key_clip_groupbox, 2, 0, 2, 1)
        _layout.addWidget(self._spill_correction_groupbox, 4, 0, 2, 1)
        _layout.addWidget(self._spill_correction2_groupbox, 6, 0, 3, 1)
        # 第二列
        _layout.addWidget(self._fetch_groupbox, 0, 1, 1, 1)
        _layout.addWidget(self._color_key_groupbox, 1, 1, 4, 1)
        _layout.addWidget(self._color_adjustment_groupbox, 5, 1, 4, 1)

        """
        记录控件，以备更新UI
        """
        self._fill_src_value= {
            "StatusCheckBox": self._chroma_status_checkbox,
            "KeyColorComboBox": self._chroma_key_color_combobox,
            "FillSourceComboBox": self._fill_src_cb,
            "FillSourceIndex": 0
        }
        self._fetch_value = {
            "FetchLineEdit": self._fetch_color_line
        }
        self._color_key_value= {
            "ColorKeyRedSlider": self._color_key_red_slider,
            "ColorKeyRedSpinBox": self._color_key_red_spin_box,
            "ColorKeyGreenSlider": self._color_key_green_slider,
            "ColorKeyGreenSpinBox": self._color_key_green_spin_box,
            "ColorKeyBlueSlider": self._color_key_blue_slider,
            "ColorKeyBlueSpinBox": self._color_key_blue_spin_box,
            "ColorKeyAngleSlider": self._color_key_angle_slider,
            "ColorKeyAngleSpinBox": self._color_key_angle_spin_box,
            "ColorKeyToleranceSlider": self._color_key_tolerance_slider,
            "ColorKeyToleranceSpinBox": self._color_key_tolerance_spin_box,
            "ColorKeySoftnessSlider": self._color_key_softness_slider,
            "ColorKeySoftnessSpinBox": self._color_key_softness_spin_box,
        }
        self._key_setting_value= {
            "KeySettingForegroundSlider": self._key_setting_foreground_slider,
            "KeySettingForegroundLineEdit": self._key_setting_foreground_line_edit,
            "KeySettingForegroundValue": 0,
            "KeySettingBackgroundSlider": self._key_setting_background_slider,
            "KeySettingBackgroundLineEdit": self._key_setting_background_line_edit,
            "KeySettingBackgroundValue": 0,
            "KeySettingKeyEdgeSlider": self._key_setting_key_edge_slider,
            "KeySettingKeyEdgeLineEdit": self._key_setting_key_edge_line_edit,
            "KeySettingKeyEdgeValue": 0,
        }
        self._key_clip_value= {
            "KeyClipSwitchButton": self._key_clip_switch_btn,
            "KeyClipCurveSwitchButton": self._key_curve_switch_btn,
            "KeyClipLeftLabel": self._key_clip_left_value,
            "KeyClipRightLabel": self._key_clip_right_value,
            "KeyClipRangeSlider": self._key_clip_range_slider,
            "KeyClipLeftValue": 0,
            "KeyClipRightValue": 1000,
        }
        self._spill_correction_value = {
            "SpillSwitchButton": self._spill_switch_btn,
            "SpillEdgeSlider": self._spill_edge_slider,
            "SpillEdgeLineEdit": self._spill_edge_line_edit,
            "SpillEdgeValue": 0,
            "SpillBackgroundSlider": self._spill_background_slider,
            "SpillBackgroundLineEdit": self._spill_background_line_edit,
            "SpillBackgroundValue": 0,
        }
        self._spill_correction2_value = {
            "Spill2SwitchButton": self._spill2_switch_btn,
            "Spill2ColorComboBox": self._spill2_color_cb,
            "Spill2ColorIndex": 0,
            "Spill2ValueSlider": self._spill2_value_slider,
            "Spill2ValueLineEdit": self._spill2_value_line_edit,
            "Spill2ValueLeftLabel": self._spill2_value_left_label,
            "Spill2ValueRightLabel": self._spill2_value_right_label,
            "Spill2RedValue": 0,
            "Spill2GreenValue": 0,
            "Spill2BlueValue": 0,
            "Spill2ResetButton": self._spill2_reset_btn,
        }
        self._color_adjustment_value = {
            "ColorAdjBrightnessSlider": self._color_adj_brightness_slider,
            "ColorAdjBrightnessLineEdit": self._color_adj_brightness_line_edit,
            "ColorAdjBrightnessValue": 0,
            "ColorAdjContractSlider": self._color_adj_contract_slider,
            "ColorAdjContractLineEdit": self._color_adj_contract_line_edit,
            "ColorAdjContractValue": 0,
            "ColorAdjSaturationSlider": self._color_adj_saturation_slider,
            "ColorAdjSaturationLineEdit": self._color_adj_saturation_line_edit,
            "ColorAdjSaturationValue": 0,
            "ColorAdjRedSlider": self._color_adj_red_slider,
            "ColorAdjRedLineEdit": self._color_adj_red_line_edit,
            "ColorAdjRedValue": 0,
            "ColorAdjGreenSlider": self._color_adj_green_slider,
            "ColorAdjGreenLineEdit": self._color_adj_green_line_edit,
            "ColorAdjGreenValue": 0,
            "ColorAdjBlueSlider": self._color_adj_blue_slider,
            "ColorAdjBlueLineEdit": self._color_adj_blue_line_edit,
            "ColorAdjBlueValue": 0,
            "ColorAdjResetButton": self._color_adj_reset_btn,
        }

        self.setLayout(_layout)
        # self.retranslateUi()

        self.change_able_status_groupboxs = [
            self._spill_correction_groupbox, self._spill_correction2_groupbox, self._key_clip_groupbox,
            self._fetch_groupbox, self._color_key_groupbox, self._key_clip_groupbox, self._color_adjustment_groupbox
        ]
        
        self.control_chroma_status(False)

    def control_chroma_status(self, status): # 是否禁用除了status checkbox 以外的控件
        # 改变除了_fill_src_groupbox区域内的所有控件的可用状态
        for groupbox in self.change_able_status_groupboxs:
                groupbox.setEnabled(status)
        # 改变_fill_src_value中的除了status checkbox 以外的控件的可用状态
        for key, widget in self._fill_src_value.items():
                if key == "StatusCheckBox":
                    widget.setEnabled(True) # Status复选框始终可用
                elif isinstance(widget, QtWidgets.QWidget):
                    widget.setEnabled(status)
        if status:
            # 设置Chroma正在使用，luma不可用
            chroma_config.using_chroma = True
            # self._parent.controller.update_luma_or_chroma_status("chroma")
            # 本来禁用的部分控件因被遍历启用，需要重新禁用
            if not self._key_clip_value["KeyClipSwitchButton"].checked:
                self.change_group_status(False, self._key_clip_value, "KeyClipSwitchButton")
            else:
                self._key_clip_value["KeyClipRangeSlider"].setStyleSheet(enalbed_range_slider_qss)
            if not self._spill_correction_value["SpillSwitchButton"].checked:
                self.change_group_status(False, self._spill_correction_value, "SpillSwitchButton")
            if not self._spill_correction2_value["Spill2SwitchButton"].checked:
                self.change_group_status(False, self._spill_correction2_value, "Spill2SwitchButton")
        else:
            chroma_config.using_chroma = False
            self._key_clip_value["KeyClipRangeSlider"].setStyleSheet(disabled_range_slider_qss)

    def change_group_status(self, status:bool, group_dict:dict, exclude_key:str):
        for key, widget in group_dict.items():
            if isinstance(widget, QRangeSlider):
                if status: widget.setStyleSheet(enalbed_range_slider_qss)
                else: widget.setStyleSheet(disabled_range_slider_qss)
            if not isinstance(widget, QtWidgets.QWidget): continue
            if key == exclude_key: continue
            widget.setEnabled(status)

    def update_translations(self):
        """
        递归更新所有子控件的文本
        :param widget: 父控件
        """
        # for child in widget.children():
        #     if isinstance(child, QtWidgets.QWidget):
        #         ChromaKeyWidget.update_translations(child)
            
        #     original_text = child.property("origion_text")
        #     if not child.property("origion_text"):
        #         if hasattr(child, "setText") and callable(child.setText):
        #             original_text = child.text()
        #         elif hasattr(child, "setTitle") and callable(child.setTitle):
        #             original_text = child.title()
        #         child.setProperty("origion_text", original_text)
        #     if original_text:
        #         # translated_text = _translate(child.__class__.__name__, original_text)
        #         translated_text = QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", original_text, None)
        #         if hasattr(child, "setText") and callable(child.setText):
        #             child.setText(translated_text)
        #         elif hasattr(child, "setTitle") and callable(child.setTitle):
        #             child.setTitle(translated_text)

        self._fill_src_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Fill Source", None))
        self._chroma_status_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Status", None))
        self._chroma_status_checkbox.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Inactive", None))
        self._chroma_key_color_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Key Color", None))
        self._fill_src_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Video Source", None))
        self._fetch_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Fetch", None))
        self._fetch_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Fetch", None))
        self._fetch_btn.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Fetch Manually", None))
        self._color_key_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Color Key", None))
        self._color_key_red_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Red", None))
        self._color_key_green_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Green", None))
        self._color_key_blue_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Blue", None))
        self._color_key_angle_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Angle", None))
        self._color_key_tolerance_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Tolerance", None))
        self._color_key_softness_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Softness", None))
        self._key_setting_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Key Setting", None))
        self._key_setting_foreground_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Foreground", None))
        self._key_setting_background_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Background", None))
        self._key_setting_key_edge_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Key Edge", None))
        self._key_clip_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Key Clip", None))
        self._key_clip_switch_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Clip On/Off", None))
        self._key_clip_curve_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Curve On/Off", None))
        self._key_clip_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Key Clip", None))
        self._spill_correction_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Spill Correction", None))
        self._spill_switch_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill On/Off", None))
        self._spill_edge_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill Edge", None))
        self._spill_background_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Background", None))
        self._spill_correction2_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Spill Correction2", None))
        self._spill2_switch_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill2 On/Off", None))
        self._spill2_color_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill2 Color", None))
        self._spill2_reset_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Spill2 Reset", None))
        self._spill2_reset_btn.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Reset", None))
        self._color_adjustment_groupbox.setTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Chroma Color Adjustment", None))
        self._color_adj_brightness_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Brightness", None))
        self._color_adj_contract_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Contract", None))
        self._color_adj_saturation_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Saturation", None))
        self._color_adj_red_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Red", None))
        self._color_adj_green_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Green", None))
        self._color_adj_blue_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Blue", None))
        self._color_adj_reset_label.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Reset", None))
        self._color_adj_reset_btn.setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Reset", None))

    def retranslateUi(self):
        self.update_translations()

        _fill_srcs = Cue01Preferences.get_chroma_video_sources()
        _key_colors = Cue01Preferences.get_chroma_key_colors()
        _spill2_colors = Cue01Preferences.get_spill_correction2_colors()
        

        _fill_src_cb = self._fill_src_value["FillSourceComboBox"]
        _chroma_key_color_combobox = self._fill_src_value["KeyColorComboBox"]
        _spill2_color_cb = self._spill_correction2_value["Spill2ColorComboBox"]

        for i in range(len(_fill_srcs)):
            _item_text = QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", _fill_srcs[i], None)
            _fill_src_cb.setItemText(i, _item_text)
        
        for i in range(len(_key_colors)):
            _item_text = QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", _key_colors[i], None)
            _chroma_key_color_combobox.setItemText(i, _item_text)

        for i in range(len(_spill2_colors)):
            _item_text = QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", _spill2_colors[i], None)
            _spill2_color_cb.setItemText(i, _item_text)

    def show_fetch_dialog(self):
        self._parent.controller.get_input_status()
        self._open_fetch_dialog_flag = True
        # self.sc = ScreenSelector(self.pos_x, self.pos_y, self)
        # self.sc.position_signal.connect(self.get_rgb_color)
        # self.sc.exec()

    def get_rgb_color(self, position:tuple):
        # print("收到", position)
        args = {
            "PosX": position[0],
            "PosY": position[1]
        }
        logging.debug("args:{}".format(args))
        self._parent.controller.set_chroma_fetch_position(args)
        # self._parent.controller.get_chroma() # 选择坐标后重新刷新获取颜色，后续会自动主动上报，则取消这句

    def chroma_status_changed(self, status):
        sender = self.sender()
        checked = sender.isChecked()
        if checked:
            logging.debug("Chroma Status ON")
            self._fill_src_value["StatusCheckBox"].setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Active", None))
            _args = {
                "Status": 1
            }
            self.control_chroma_status(True)
            self._parent.controller.set_chroma_fill_src(_args)
        else:
            logging.debug("Chroma Status OFF")
            self._fill_src_value["StatusCheckBox"].setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Inactive", None))
            _args = {
                "Status": 0
            }
            self.control_chroma_status(False)
            self._parent.controller.set_chroma_fill_src(_args)

    def _select_chroma_key_color(self, index):
        logging.debug("Chroma Key Color:{}".format(index))
        _args = {
            "KeyColor": Cue01Preferences.get_chroma_key_color_by_index(index)
        }
        self._parent.controller.set_chroma_fill_src(_args)

    def _select_fill_source(self, index):
        sender = self.sender()

        if self._fill_src_value["FillSourceComboBox"] == sender:
            if self._fill_src_value["FillSourceIndex"] != index:
                logging.debug("select FillSourceIndex:{}".format(index))
                self._fill_src_value["FillSourceIndex"] = index
                _args = {
                    "FillSource": Cue01Preferences.get_chroma_video_src_by_index(index)
                }
                self._parent.controller.set_chroma_fill_src(_args)

    def _color_key_red_slider_value_changed(self, value):
        if self._color_key_value["ColorKeyRedSpinBox"].value() != value:
            self._color_key_value["ColorKeyRedSpinBox"].setValue(value)
            _args = {
                "ColorKeyRed": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _color_key_red_spin_box_value_changed(self, value):
        if self._color_key_value["ColorKeyRedSlider"].value() != value:
            self._color_key_value["ColorKeyRedSlider"].setValue(value)
            _args = {
                "ColorKeyRed": value
            }
            self._parent.controller.set_chroma_color_key(_args)
    
    def _color_key_green_slider_value_changed(self, value):
        if self._color_key_value["ColorKeyGreenSpinBox"].value() != value:
            self._color_key_value["ColorKeyGreenSpinBox"].setValue(value)
            _args = {
                "ColorKeyGreen": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _color_key_green_spin_box_value_changed(self, value):
        if self._color_key_value["ColorKeyGreenSlider"].value() != value:
            self._color_key_value["ColorKeyGreenSlider"].setValue(value)
            _args = {
                "ColorKeyGreen": value
            }
            self._parent.controller.set_chroma_color_key(_args)
    
    def _color_key_blue_slider_value_changed(self, value):
        if self._color_key_value["ColorKeyBlueSpinBox"].value() != value:
            self._color_key_value["ColorKeyBlueSpinBox"].setValue(value)
            _args = {
                "ColorKeyBlue": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _color_key_blue_spin_box_value_changed(self, value):
        if self._color_key_value["ColorKeyBlueSlider"].value() != value:
            self._color_key_value["ColorKeyBlueSlider"].setValue(value)
            _args = {
                "ColorKeyBlue": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _color_key_angle_slider_value_changed(self, value):
        if self._color_key_value["ColorKeyAngleSpinBox"].value() != value:
            self._color_key_value["ColorKeyAngleSpinBox"].setValue(value)
            _args = {
                "ColorKeyAngle": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _color_key_angle_spin_box_value_changed(self, value):
        if self._color_key_value["ColorKeyAngleSlider"].value() != value:
            self._color_key_value["ColorKeyAngleSlider"].setValue(value)
            _args = {
                "ColorKeyAngle": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _color_key_tolerance_slider_value_changed(self, value):
        if self._color_key_value["ColorKeyToleranceSpinBox"].value() != value:
            self._color_key_value["ColorKeyToleranceSpinBox"].setValue(value)
            _args = {
                "ColorKeyTolerance": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _color_key_tolerance_spin_box_value_changed(self, value):
        if self._color_key_value["ColorKeyToleranceSlider"].value() != value:
            self._color_key_value["ColorKeyToleranceSlider"].setValue(value)
            _args = {
                "ColorKeyTolerance": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _color_key_softness_slider_value_changed(self, value):
        if self._color_key_value["ColorKeySoftnessSpinBox"].value() != value:
            self._color_key_value["ColorKeySoftnessSpinBox"].setValue(value)
            _args = {
                "ColorKeySoftness": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _color_key_softness_spin_box_value_changed(self, value):
        if self._color_key_value["ColorKeySoftnessSlider"].value() != value:
            self._color_key_value["ColorKeySoftnessSlider"].setValue(value)
            _args = {
                "ColorKeySoftness": value
            }
            self._parent.controller.set_chroma_color_key(_args)

    def _on_key_setting_foreground_slider_value_changed(self, value):
        # logging.debug("KeySettingForegroundValue:{}, value:{}".format(self._key_setting_value["KeySettingForegroundValue"], value))
        if self._key_setting_value["KeySettingForegroundValue"] != value:
            self._key_setting_value["KeySettingForegroundLineEdit"].setText("{}%".format(value/10.0))
            self._key_setting_value["KeySettingForegroundValue"] = value
            _args = {
                "KeySettingForeground": value
            }
            self._parent.controller.set_chroma_key_setting(_args)
    
    def _on_key_setting_background_slider_value_changed(self, value):
        if self._key_setting_value["KeySettingBackgroundValue"] != value:
            self._key_setting_value["KeySettingBackgroundLineEdit"].setText("{}%".format(value/10.0))
            self._key_setting_value["KeySettingBackgroundValue"] = value
            _args = {
                "KeySettingBackground": value
            }
            self._parent.controller.set_chroma_key_setting(_args)

    def _on_key_setting_key_edge_slider_value_changed(self, value):
        if self._key_setting_value["KeySettingKeyEdgeValue"] != value:
            self._key_setting_value["KeySettingKeyEdgeLineEdit"].setText("{}%".format(value/10.0))
            self._key_setting_value["KeySettingKeyEdgeValue"] = value
            _args = {
                "KeySettingKeyEdge": value
            }
            self._parent.controller.set_chroma_key_setting(_args)
    
    def _on_key_clip_switch_rbtn_clicked(self, checked:bool):
        if checked:
            logging.debug("Key Clip ON")
            _args = {
                "KeyClip": "On"
            }
            self.change_group_status(True, self._key_clip_value, "KeyClipSwitchButton")
            self._parent.controller.set_chroma_key_clip(_args)
        else:
            logging.debug("Key Clip OFF")
            _args = {
                "KeyClip": "Off"
            }
            self.change_group_status(False, self._key_clip_value, "KeyClipSwitchButton")
            self._parent.controller.set_chroma_key_clip(_args)

    def _on_key_clip_curve_rbtn_clicked(self, checked:bool):
        if checked:
            logging.debug("Key Clip Curve ON")
            _args = {
                "KeyClipCurve": "On"
            }
            self._parent.controller.set_chroma_key_clip(_args)
        else:
            logging.debug("Key Clip Curve OFF")
            _args = {
                "KeyClipCurve": "Off"
            }
            self._parent.controller.set_chroma_key_clip(_args)

    def _on_key_clip_range_slider_value_changed(self, value):
        _key_clip_left = value[0]
        _key_clip_right = value[1]

        self._key_clip_value["KeyClipLeftLabel"].setText("{}%".format(_key_clip_left/10.0))
        self._key_clip_value["KeyClipRightLabel"].setText("{}%".format(_key_clip_right/10.0))

        if self._key_clip_value["KeyClipLeftValue"] != _key_clip_left or self._key_clip_value["KeyClipRightValue"] != _key_clip_right:
            logging.debug("Key Clip Range:{}".format(value))

            self._key_clip_value["KeyClipLeftValue"] = _key_clip_left
            self._key_clip_value["KeyClipRightValue"] = _key_clip_right
            _args = {
                "ClipLeft": _key_clip_left,
                "ClipRight": _key_clip_right
            }
            self._parent.controller.set_chroma_key_clip(_args)
    
    def _on_spill_switch_rbtn_clicked(self, checked:bool):
        if checked:
            logging.debug("Spill Correction ON")
            _args = {
                "SpillCorrectionSwitch": "On"
            }
            self.change_group_status(True, self._spill_correction_value, "SpillSwitchButton")
            self._parent.controller.set_chroma_spill_correction(_args)
        else:
            logging.debug("Spill Correction OFF")
            _args = {
                "SpillCorrectionSwitch": "Off"
            }
            self.change_group_status(False, self._spill_correction_value, "SpillSwitchButton")
            self._parent.controller.set_chroma_spill_correction(_args)
    
    def _on_spill_edge_slider_value_changed(self, value):
        if self._spill_correction_value["SpillEdgeValue"] != value:
            self._spill_correction_value["SpillEdgeLineEdit"].setText("{}%".format(value/10.0))
            self._spill_correction_value["SpillEdgeValue"] = value
            _args = {
                "SpillEdge": value
            }
            self._parent.controller.set_chroma_spill_correction(_args)

    def _on_spill_background_slider_value_changed(self, value):
        if self._spill_correction_value["SpillBackgroundValue"] != value:
            self._spill_correction_value["SpillBackgroundLineEdit"].setText("{}%".format(value/10.0))
            self._spill_correction_value["SpillBackgroundValue"] = value
            _args = {
                "SpillBackground": value
            }
            self._parent.controller.set_chroma_spill_correction(_args)
    
    def _on_spill2_switch_rbtn_clicked(self, checked:bool):
        if checked:
            logging.debug("Spill Correction2 ON")
            _args = {
                "SpillCorrection2Switch": "On"
            }
            self.change_group_status(True, self._spill_correction2_value, "Spill2SwitchButton")
            self._parent.controller.set_chroma_spill_correction2(_args)
        else:
            logging.debug("Spill Correction2 OFF")
            _args = {
                "SpillCorrection2Switch": "Off"
            }
            self.change_group_status(False, self._spill_correction2_value, "Spill2SwitchButton")
            self._parent.controller.set_chroma_spill_correction2(_args)
    
    def _select_spill2_color(self, index):
        sender = self.sender()

        if self._spill_correction2_value["Spill2ColorComboBox"] == sender:
            if self._spill_correction2_value["Spill2ColorIndex"] != index:
                logging.debug(f"select Spill2ColorIndex:{index}, send {index + 1}")
                self._spill_correction2_value["Spill2ColorIndex"] = index
                _color = Cue01Preferences.get_spill_correction2_color_by_index(index)
                if _color == "Red":
                    self._spill_correction2_value["Spill2ValueLeftLabel"].setText("G")
                    self._spill_correction2_value["Spill2ValueRightLabel"].setText("B")
                elif _color == "Green":
                    self._spill_correction2_value["Spill2ValueLeftLabel"].setText("B")
                    self._spill_correction2_value["Spill2ValueRightLabel"].setText("R")
                elif _color == "Blue":
                    self._spill_correction2_value["Spill2ValueLeftLabel"].setText("R")
                    self._spill_correction2_value["Spill2ValueRightLabel"].setText("G")
                else:
                    self._spill_correction2_value["Spill2ValueLeftLabel"].setText("-")
                    self._spill_correction2_value["Spill2ValueRightLabel"].setText("-")

                _args = {
                    "Spill2Color": _color
                }
                self._parent.controller.set_chroma_spill_correction2(_args)

    def _on_spill2_value_slider_value_changed(self, value):
        if self._spill_correction2_value["Spill2RedValue"] != value:
            self._spill_correction2_value["Spill2ValueLineEdit"].setText("{}".format((value - 10000)/100.0))
            self._spill_correction2_value["Spill2RedValue"] = value
            _args = {
                "Spill2Value": value
            }
            self._parent.controller.set_chroma_spill_correction2(_args)

    def _on_spill2_reset_btn_clicked(self):
        logging.debug("Spill2 Reset button clicked")
        _args = {
            "SpillCorrection2Reset": "ON"
        }
        self._parent.controller.set_chroma_spill_correction2(_args)

    def _on_color_adj_brightness_slider_value_changed(self, value):
        if self._color_adjustment_value["ColorAdjBrightnessValue"] != value:
            self._color_adjustment_value["ColorAdjBrightnessLineEdit"].setText("{}%".format((value-100)*1.0))
            self._color_adjustment_value["ColorAdjBrightnessValue"] = value
            _args = {
                "ColorAdjBrightness": value
            }
            self._parent.controller.set_chroma_color_adjustment(_args)
    
    def _on_color_adj_contract_slider_value_changed(self, value):
        if self._color_adjustment_value["ColorAdjContractValue"] != value:
            self._color_adjustment_value["ColorAdjContractLineEdit"].setText("{}%".format((value-100)*1.0))
            self._color_adjustment_value["ColorAdjContractValue"] = value
            _args = {
                "ColorAdjContract": value
            }
            self._parent.controller.set_chroma_color_adjustment(_args)
    
    def _on_color_adj_saturation_slider_value_changed(self, value):
        if self._color_adjustment_value["ColorAdjSaturationValue"] != value:
            self._color_adjustment_value["ColorAdjSaturationLineEdit"].setText("{}%".format((value-100)*1.0))
            self._color_adjustment_value["ColorAdjSaturationValue"] = value
            _args = {
                "ColorAdjSaturation": value
            }
            self._parent.controller.set_chroma_color_adjustment(_args)
    
    def _on_color_adj_red_slider_value_changed(self, value):
        if self._color_adjustment_value["ColorAdjRedValue"] != value:
            self._color_adjustment_value["ColorAdjRedLineEdit"].setText("{}%".format((value-100)*1.0))
            self._color_adjustment_value["ColorAdjRedValue"] = value
            _args = {
                "ColorAdjRed": value
            }
            self._parent.controller.set_chroma_color_adjustment(_args)
    
    def _on_color_adj_green_slider_value_changed(self, value):
        if self._color_adjustment_value["ColorAdjGreenValue"] != value:
            self._color_adjustment_value["ColorAdjGreenLineEdit"].setText("{}%".format((value-100)*1.0))
            self._color_adjustment_value["ColorAdjGreenValue"] = value
            _args = {
                "ColorAdjGreen": value
            }
            self._parent.controller.set_chroma_color_adjustment(_args)
    
    def _on_color_adj_blue_slider_value_changed(self, value):
        if self._color_adjustment_value["ColorAdjBlueValue"] != value:
            self._color_adjustment_value["ColorAdjBlueLineEdit"].setText("{}%".format((value-100)*1.0))
            self._color_adjustment_value["ColorAdjBlueValue"] = value
            _args = {
                "ColorAdjBlue": value
            }
            self._parent.controller.set_chroma_color_adjustment(_args)
    
    def _on_color_adj_reset_btn_clicked(self):
        logging.debug("Color Adjustment Reset button clicked")
        _args = {
            "ColorAdjReset": "ON"
        }
        self._parent.controller.set_chroma_color_adjustment(_args)
    
    def showEvent(self, event):
        self._parent.controller.get_chroma()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_chroma_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))

            """
            同步视频源
            """
            _fill_src = args["VideoSource"]
            _status = args["Status"]
            _keyColor_index = args["KeyColor"]
            _fill_src_index = Cue01Preferences.get_index_by_chroma_video_src(_fill_src)
            if _fill_src_index != 0xFF:
                self._fill_src_value["FillSourceIndex"] = _fill_src_index
                self._fill_src_value["FillSourceComboBox"].setCurrentIndex(_fill_src_index)
            with QtCore.QSignalBlocker(self._fill_src_value["StatusCheckBox"]):
                if _status == 0:
                    self._fill_src_value["StatusCheckBox"].setChecked(False)
                    self._fill_src_value["StatusCheckBox"].setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Inactive", None))
                    self.control_chroma_status(False)
                elif _status == 1:
                    self._fill_src_value["StatusCheckBox"].setChecked(True)
                    self._fill_src_value["StatusCheckBox"].setText(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Active", None))
                    self.control_chroma_status(True)
            if _keyColor_index == 0xFF:
                logging.error("key color error: {}".format(_keyColor_index))
            with QtCore.QSignalBlocker(self._fill_src_value["KeyColorComboBox"]):
                self._fill_src_value["KeyColorComboBox"].setCurrentIndex(_keyColor_index)

            """
            同步取色坐标
            """
            _fetch_pos_x = args["PosX"] # 上一次点击发送的值
            _fetch_pos_y = args["PosY"]
            self.pos_x = _fetch_pos_x
            self.pos_y = _fetch_pos_y
            """
            同步Color Key
            """
            _color_key_red = args["ColorKeyRed"]
            _color_key_green = args["ColorKeyGreen"]
            _color_key_blue = args["ColorKeyBlue"]
            _color_key_angle = args["ColorKeyAngle"]
            _color_key_tolerance = args["ColorKeyTolerance"]
            _color_key_softness = args["ColorKeySoftness"]

            r_str = str(_color_key_red)
            g_str = str(_color_key_green)
            b_str = str(_color_key_blue)
            # import random
            # r_str = random.randint(0, 255)
            # g_str = random.randint(0, 255)
            # b_str = random.randint(0, 255)

            fetch_text = f"x: {_fetch_pos_x}, y: {_fetch_pos_y}; RGB({r_str}, {g_str}, {b_str})"
            self._fetch_value["FetchLineEdit"].setText(fetch_text)
            fetch_rgb_value = "background-color: rgb(%s, %s, %s);"%(r_str, g_str, b_str)
            # print(fetch_rgb_value)
            self._fetch_value["FetchLineEdit"].setStyleSheet(fetch_rgb_value)

            with QSignalBlocker(self._color_key_value["ColorKeyRedSpinBox"]):
                self._color_key_value["ColorKeyRedSpinBox"].setValue(_color_key_red)
            with QSignalBlocker(self._color_key_value["ColorKeyGreenSpinBox"]):
                self._color_key_value["ColorKeyGreenSpinBox"].setValue(_color_key_green)
            with QSignalBlocker(self._color_key_value["ColorKeyBlueSpinBox"]):
                self._color_key_value["ColorKeyBlueSpinBox"].setValue(_color_key_blue)
            with QSignalBlocker(self._color_key_value["ColorKeyAngleSpinBox"]):
                self._color_key_value["ColorKeyAngleSpinBox"].setValue(_color_key_angle)
            with QSignalBlocker(self._color_key_value["ColorKeyToleranceSpinBox"]):
                self._color_key_value["ColorKeyToleranceSpinBox"].setValue(_color_key_tolerance)
            with QSignalBlocker(self._color_key_value["ColorKeySoftnessSpinBox"]):
                self._color_key_value["ColorKeySoftnessSpinBox"].setValue(_color_key_softness)
            with QSignalBlocker(self._color_key_value["ColorKeyRedSlider"]):
                self._color_key_value["ColorKeyRedSlider"].setValue(_color_key_red)
            with QSignalBlocker(self._color_key_value["ColorKeyGreenSlider"]):
                self._color_key_value["ColorKeyGreenSlider"].setValue(_color_key_green)
            with QSignalBlocker(self._color_key_value["ColorKeyBlueSlider"]):
                self._color_key_value["ColorKeyBlueSlider"].setValue(_color_key_blue)
            with QSignalBlocker(self._color_key_value["ColorKeyAngleSlider"]):
                self._color_key_value["ColorKeyAngleSlider"].setValue(_color_key_angle)
            with QSignalBlocker(self._color_key_value["ColorKeyToleranceSlider"]):
                self._color_key_value["ColorKeyToleranceSlider"].setValue(_color_key_tolerance)
            with QSignalBlocker(self._color_key_value["ColorKeySoftnessSlider"]):
                self._color_key_value["ColorKeySoftnessSlider"].setValue(_color_key_softness)

            """
            同步Key Setting
            """
            # _key_set_foreground = args["KeySetForeground"]
            # _key_set_background = args["KeySetBackground"]
            # _key_set_edge = args["KeySetEdge"]

            # self._key_setting_value["KeySettingForegroundValue"] = _key_set_foreground
            # self._key_setting_value["KeySettingForegroundLineEdit"].setText("{}%".format(_key_set_foreground/10.0))
            # self._key_setting_value["KeySettingForegroundSlider"].setValue(_key_set_foreground)

            # self._key_setting_value["KeySettingBackgroundValue"] = _key_set_background
            # self._key_setting_value["KeySettingBackgroundLineEdit"].setText("{}%".format(_key_set_background/10.0))
            # self._key_setting_value["KeySettingBackgroundSlider"].setValue(_key_set_background)

            # self._key_setting_value["KeySettingKeyEdgeValue"] = _key_set_edge
            # self._key_setting_value["KeySettingKeyEdgeLineEdit"].setText("{}%".format(_key_set_edge/10.0))
            # self._key_setting_value["KeySettingKeyEdgeSlider"].setValue(_key_set_edge)

            """
            同步Key Clip
            """
            _clip_switch = args["ClipSwitch"]
            _clip_curve_switch = args["ClipCurveSwitch"]
            _clip_left = args["ClipLeft"]
            _clip_right = args["ClipRight"]

            if _clip_switch == "On" or _clip_switch == "ON":
                self._key_clip_value["KeyClipSwitchButton"].set_checked(True)
                self.change_group_status(True, self._key_clip_value, "KeyClipSwitchButton")
            else:
                self._key_clip_value["KeyClipSwitchButton"].set_checked(False)
                self.change_group_status(False, self._key_clip_value, "KeyClipSwitchButton")
            
            if _clip_curve_switch == "On" or _clip_curve_switch == "ON":
                self._key_clip_value["KeyClipCurveSwitchButton"].set_checked(True)
            else:
                self._key_clip_value["KeyClipCurveSwitchButton"].set_checked(False)
            
            if 0 <= _clip_left <= _clip_right and  _clip_right <= 1000:
                # 先同步变量的值，确保此处更新的值，不会触发设置
                self._key_clip_value["KeyClipLeftValue"] = _clip_left
                self._key_clip_value["KeyClipRightValue"] = _clip_right
                # 更新UI，其中setValue会触发回调，因此要确保先同步变量的值
                self._key_clip_value["KeyClipLeftLabel"].setText("{}%".format(_clip_left/10.0))
                self._key_clip_value["KeyClipRightLabel"].setText("{}%".format(_clip_right/10.0))
                self._key_clip_value["KeyClipRangeSlider"].setValue((_clip_left, _clip_right))
            
            """
            同步Spill Correction
            """
            _spill_switch = args["SpillCorrectionSwitch"]
            _spill_edge = args["SpillCorrectionEdge"]
            _spill_background = args["SpillCorrectionBackground"]

            if _spill_switch == "On" or _spill_switch == "ON":
                self._spill_correction_value["SpillSwitchButton"].set_checked(True)
                self.change_group_status(True, self._spill_correction_value, "SpillSwitchButton")
            else:
                self._spill_correction_value["SpillSwitchButton"].set_checked(False)
                self.change_group_status(False, self._spill_correction_value, "SpillSwitchButton")
            
            if 0 <= _spill_edge <= 1000:
                self._spill_correction_value["SpillEdgeValue"] = _spill_edge
                self._spill_correction_value["SpillEdgeLineEdit"].setText("{}%".format(_spill_edge/10.0))
                self._spill_correction_value["SpillEdgeSlider"].setValue(_spill_edge)
            
            if 0 <= _spill_background <= 1000:
                self._spill_correction_value["SpillBackgroundValue"] = _spill_background
                self._spill_correction_value["SpillBackgroundLineEdit"].setText("{}%".format(_spill_background/10.0))
                self._spill_correction_value["SpillBackgroundSlider"].setValue(_spill_background)

            """
            同步Spill Correction2
            """
            _spill2_switch = args["SpillCorrection2Switch"]
            _spill2_param = args["SpillCorrection2Param"]
            _spill2_value = args["SpillCorrection2Value"]

            if _spill2_switch == "On" or _spill2_switch == "ON":
                self._spill_correction2_value["Spill2SwitchButton"].set_checked(True)
                self.change_group_status(True, self._spill_correction2_value, "Spill2SwitchButton")
            else:
                self._spill_correction2_value["Spill2SwitchButton"].set_checked(False)
                self.change_group_status(False, self._spill_correction2_value, "Spill2SwitchButton")
            
            _spill2_color_index = Cue01Preferences.get_index_by_spill_correction2_color(_spill2_param)
            if _spill2_color_index != 0xFF:
                self._spill_correction2_value["Spill2ColorIndex"] = _spill2_color_index
                self._spill_correction2_value["Spill2ColorComboBox"].setCurrentIndex(_spill2_color_index)

            if _spill2_param == "Red":
                self._spill_correction2_value["Spill2ValueLeftLabel"].setText("G")
                self._spill_correction2_value["Spill2ValueRightLabel"].setText("B")
            elif _spill2_param == "Green":
                self._spill_correction2_value["Spill2ValueLeftLabel"].setText("B")
                self._spill_correction2_value["Spill2ValueRightLabel"].setText("R")
            elif _spill2_param == "Blue":
                self._spill_correction2_value["Spill2ValueLeftLabel"].setText("R")
                self._spill_correction2_value["Spill2ValueRightLabel"].setText("G")
            else:
                self._spill_correction2_value["Spill2ValueLeftLabel"].setText("-")
                self._spill_correction2_value["Spill2ValueRightLabel"].setText("-")
            
            if 0 <= _spill2_value <= 20000:
                self._spill_correction2_value["Spill2RedValue"] = _spill2_value
                self._spill_correction2_value["Spill2ValueLineEdit"].setText("{}".format((_spill2_value - 10000)/100.0))
                self._spill_correction2_value["Spill2ValueSlider"].setValue(_spill2_value)
            
            """
            同步Color Adjustment
            """
            _color_adj_brightness = args["ColorAdjBrightness"]
            _color_adj_contract = args["ColorAdjContract"]
            _color_adj_saturation = args["ColorAdjSaturation"]
            _color_adj_red = args["ColorAdjRed"]
            _color_adj_green = args["ColorAdjGreen"]
            _color_adj_blue = args["ColorAdjBlue"]

            if 0 <= _color_adj_brightness <= 255:
                self._color_adjustment_value["ColorAdjBrightnessValue"] = _color_adj_brightness
                self._color_adjustment_value["ColorAdjBrightnessLineEdit"].setText("{}%".format((_color_adj_brightness-100)*1.0))
                self._color_adjustment_value["ColorAdjBrightnessSlider"].setValue(_color_adj_brightness)
            
            if 0 <= _color_adj_contract <= 255:
                self._color_adjustment_value["ColorAdjContractValue"] = _color_adj_contract
                self._color_adjustment_value["ColorAdjContractLineEdit"].setText("{}%".format((_color_adj_contract-100)*1.0))
                self._color_adjustment_value["ColorAdjContractSlider"].setValue(_color_adj_contract)
            
            if 0 <= _color_adj_saturation <= 255:
                self._color_adjustment_value["ColorAdjSaturationValue"] = _color_adj_saturation
                self._color_adjustment_value["ColorAdjSaturationLineEdit"].setText("{}%".format((_color_adj_saturation-100)*1.0))
                self._color_adjustment_value["ColorAdjSaturationSlider"].setValue(_color_adj_saturation)
            
            if 0 <= _color_adj_red <= 255:
                self._color_adjustment_value["ColorAdjRedValue"] = _color_adj_red
                self._color_adjustment_value["ColorAdjRedLineEdit"].setText("{}%".format((_color_adj_red-100)*1.0))
                self._color_adjustment_value["ColorAdjRedSlider"].setValue(_color_adj_red)
            
            if 0 <= _color_adj_green <= 255:
                self._color_adjustment_value["ColorAdjGreenValue"] = _color_adj_green
                self._color_adjustment_value["ColorAdjGreenLineEdit"].setText("{}%".format((_color_adj_green-100)*1.0))
                self._color_adjustment_value["ColorAdjGreenSlider"].setValue(_color_adj_green)
            
            if 0 <= _color_adj_blue <= 255:
                self._color_adjustment_value["ColorAdjBlueValue"] = _color_adj_blue
                self._color_adjustment_value["ColorAdjBlueLineEdit"].setText("{}%".format((_color_adj_blue-100)*1.0))
                self._color_adjustment_value["ColorAdjBlueSlider"].setValue(_color_adj_blue)
        elif obj["function"] == "set_chroma_fill_src":
            args = obj["args"]
            logging.debug("Set chroma fill source args:{}".format(args))
        elif obj["function"] == "set_chroma_fetch_position":
            args = obj["args"]
            logging.debug("Set chroma fetch position args:{}".format(args))
        elif obj["function"] == "set_chroma_color_key":
            args = obj["args"]
            logging.debug("Set chroma color key args:{}".format(args))
        elif obj["function"] == "set_chroma_key_setting":
            args = obj["args"]
            logging.debug("Set chroma key setting args:{}".format(args))
        elif obj["function"] == "set_chroma_key_clip":
            args = obj["args"]
            logging.debug("Set chroma key clip args:{}".format(args))
        elif obj["function"] == "set_chroma_spill_correction":
            args = obj["args"]
            logging.debug("Set chroma spill correction args:{}".format(args))
        elif obj["function"] == "set_chroma_spill_correction2":
            args = obj["args"]
            logging.debug("Set chroma spill correction2 args:{}".format(args))
        elif obj["function"] == "set_chroma_color_adjustment":
            args = obj["args"]
            logging.debug("Set chroma color adjustment args:{}".format(args))
        elif obj["function"] == "get_input_status":
            args = obj["args"]
            logging.debug("args:{}".format(args))

            # 获取到前景的视频格式后，再打开坐标选择窗口
            if self._open_fetch_dialog_flag:
                _fg_input = args["Video"][0]
                _format = _fg_input["Format"]

                if _format == "None":
                    _format = "1080p60"
                    # _format = "2160p60"
                
                chroma_config.set_ratio_by_format(_format)
                self.sc = ScreenSelector(self.pos_x, self.pos_y, self)
                self.sc.position_signal.connect(self.get_rgb_color)
                self.sc.exec()
                self._open_fetch_dialog_flag = False


class ScreenSelector(QtWidgets.QDialog):
    """ 采样选择弹窗 """

    position_signal = QtCore.Signal(tuple)

    def __init__(self, x, y, parent=None):
        super().__init__(parent)
        self.setFixedSize(800, 450)
        resolution_ratio = chroma_config.get_fetch_resolution_ratio()
        self.width_ratio = resolution_ratio[0] / self.width()
        self.height_ratio = resolution_ratio[1] / self.height()
        self.selected_position = QtCore.QPoint(x // self.width_ratio, y // self.height_ratio)
        # self.setWindowTitle(QCoreApplication.translate("CUE01_Chroma_Key_Widget_Form", u"Screen Selector", None))
        self.setWindowTitle("Screen Selector" if TranslationManager().current_language_index == 0 else "屏幕选择器")
        self.setWindowIcon(QtGui.QIcon("res/images/screen_selector.png"))
        self.setWindowModality(Qt.ApplicationModal)  # 设置模态对话框，阻止对父窗口之外的窗口的输入
        self.setProperty("type", "chroma_fetch_dialog")
        self.setMouseTracking(True)

        # 创建一个标签用于显示坐标值
        self.coord_label = QtWidgets.QLabel(self)
        self.coord_label.setStyleSheet("background-color: transparent; color: #8b8b8b; border: 1px solid #8b8b8b;")
        # self.coord_label.setFixedHeight(20)
        self.update_coord_label()

    def update_coord_label(self):
        """ 更新坐标标签的位置和文本 """
        x = int(self.selected_position.x() * self.width_ratio)
        y = int(self.selected_position.y() * self.height_ratio)
        self.coord_label.setText(f"({x}, {y})")
        self.coord_label.adjustSize()  # 根据文本内容调整标签大小

        # 调整标签位置以保证在窗口内部
        label_x = self.selected_position.x() + 10
        label_y = self.selected_position.y() - 30

        if label_x + self.coord_label.width() > self.width():
            label_x = self.selected_position.x() - self.coord_label.width() - 10
        if label_x < 0:
            label_x = 0
        if label_y < 0:
            label_y = self.selected_position.y() + 10
        if label_y + self.coord_label.height() > self.height():
            label_y = self.height() - self.coord_label.height()

        self.coord_label.move(label_x, label_y)
        self.coord_label.show()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制屏幕选择器
        pen = QPen(QColor("#3a3a3a"))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRect(self.rect())

        # 绘制水平分割线
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        line1 = QLine(0, self.height() // 2, self.width(), self.height() // 2)
        painter.drawLine(line1)

        # 绘制垂直分割线
        line2 = QLine(self.width() // 2, 0, self.width() // 2, self.height())
        painter.drawLine(line2)

        # 绘制16x16的小方框
        pen.setStyle(Qt.SolidLine)
        pen.setWidth(1)
        pen.setColor(Qt.white)
        painter.setPen(pen)
        painter.drawRect(self.selected_position.x() - 8, self.selected_position.y() - 8, 16, 16)

        # # 绘制小加号
        # pen.setStyle(Qt.SolidLine)
        # pen.setWidth(2)
        # pen.setColor(Qt.white)
        # painter.setPen(pen)
        # painter.drawLine(self.selected_position.x() - 5, self.selected_position.y(),
        #                  self.selected_position.x() + 5, self.selected_position.y())
        # painter.drawLine(self.selected_position.x(), self.selected_position.y() - 5,
        #                  self.selected_position.x(), self.selected_position.y() + 5)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 获取鼠标点击的坐标
            self.selected_position = self.limit_position(event.pos())
            self.update_coord_label()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            # 更新小加号的位置
            self.selected_position = self.limit_position(event.pos())
            self.update_coord_label()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 将点击的坐标映射到实际坐标
            x = int(self.selected_position.x() * self.width_ratio)
            y = int(self.selected_position.y() * self.height_ratio)
            logging.info(f"Selected Position (x, y): {x}, {y}")
            self.position_signal.emit((x, y))

    def limit_position(self, pos):
        """ 限制位置在窗口范围内 """
        x = min(max(pos.x(), 0), self.width())
        y = min(max(pos.y(), 0), self.height())
        return QtCore.QPoint(x, y)
    
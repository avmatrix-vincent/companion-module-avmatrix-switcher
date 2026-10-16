import os, sys, logging
import time

from PIL.ImageCms import Flags
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QButtonGroup, QMessageBox,QLabel
from PySide6.QtCore import QSignalBlocker, Signal, QCoreApplication, QPropertyAnimation, QRect, QEasingCurve,QTimer
from src.ui.sc2020_12G.SC2020_12G_setting_ui import Ui_SC2020_12G_Setting_Form
from src.model.modelPreferences import ModelPreferences
from src.model.sc2020_12G.sc2020_12G_Preferences import SC2020_12G_Preferences
import threading

class SC2020_12G_Setting(Ui_SC2020_12G_Setting_Form, QWidget):
    is_pc_signal = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.hdmi_out_color_comBox.addItems(SC2020_12G_Preferences.get_hdmi_out_color())
        self.sdi_3g_out_comBox_2.addItems(SC2020_12G_Preferences.get_3g_sdi_out())
        self.sdi_sfp_mode_comBox_2.addItems(SC2020_12G_Preferences.get_sdi_sfp_in_mode())



        self.hdmi_out_range_comBox_2.addItems(SC2020_12G_Preferences.get_hdmi_out_range())
        self.color_metry_comBox_2.addItems(SC2020_12G_Preferences.get_color_metry())
        self.fan_speed_comBox.addItems(SC2020_12G_Preferences.get_fan_speed())
        self.hdmi_out_src_comBox_2.addItems(SC2020_12G_Preferences._hdmi_out_src_sfp)
        self.sdi_out_src_comBox_2.addItems(SC2020_12G_Preferences._sdi_sfp_out_src_sfp)

        self.hdmi_color_cbIndex = self.hdmi_out_color_comBox.currentIndex()  # 获取当前索引
        self.fan_speed_cbIndex = self.fan_speed_comBox.currentIndex()
        self.color_metry_cbIndex = self.color_metry_comBox_2.currentIndex()
        self.hdmi_out_range_cbIndex = self.hdmi_out_range_comBox_2.currentIndex()
        self.sdi_out_src_cbIndex = self.sdi_out_src_comBox_2.currentIndex()
        self.hdmi_out_src_cbIndex = self.hdmi_out_src_comBox_2.currentIndex()
        self.sdi_sfp_mode_cbIndex = self.sdi_sfp_mode_comBox_2.currentIndex()
        self.sdi_3g_cbIndex = self.sdi_3g_out_comBox_2.currentIndex()
        self.fan_speed_cbIndex = self.fan_speed_comBox.currentIndex()

        # if self.sdi_sfp_mode_cbIndex == 0:
        #     self.hdmi_out_src_comBox_2.addItems(SC2020_12G_Preferences._hdmi_out_src_sfp)
        #     self.sdi_out_src_comBox_2.addItems(SC2020_12G_Preferences._sdi_sfp_out_src_sfp)
        # else:
        #     self.hdmi_out_src_comBox_2.addItems(SC2020_12G_Preferences._hdmi_out_src_sdi)
        #     self.sdi_out_src_comBox_2.addItems(SC2020_12G_Preferences._sdi_sfp_out_src_sdi)

        self.hdmi_out_color_comBox.currentIndexChanged.connect(self._on_color_space_changed)
        self.fan_speed_comBox.currentIndexChanged.connect(self._on_fan_speed_changed)
        self.color_metry_comBox_2.currentIndexChanged.connect(self._on_color_metry_changed)
        self.hdmi_out_range_comBox_2.currentIndexChanged.connect(self._on_hdmi_out_range_changed)
        self.sdi_out_src_comBox_2.currentIndexChanged.connect(self._on_sdi_out_src_changed)

        self.hdmi_out_src_comBox_2.currentIndexChanged.connect(self._on_hdmi_out_src_changed)
        self.sdi_sfp_mode_comBox_2.currentIndexChanged.connect(self._on_sdi_sfp_mode_changed)

        self.sdi_3g_out_comBox_2.currentIndexChanged.connect(self._on_sdi_3g_out_changed)
        self.fan_speed_comBox.currentIndexChanged.connect(self._on_fan_speed_changed)

        # 设置设备信息  固定信息
        self.sn_msg.setText(str(self._parent.controller.get_sn()))
        #self.color_space_sdi_msg.setText("RGB 4:4:4")
        self.bit_sdi_msg.setText("10bits")

        self._control_state_checked =False

        # 初始化动画相关属性
        self.temp_animation = None
        self.old_temp_label = None
        self.new_temp_label = None

        self.is_pc_signal.connect(self._Is_Pc_Control_Widget)

        # 初始化线程相关变量
        self._version_thread = None
        self._version_thread_stop = threading.Event()
        self.isOpenThreading=True

    """
    判断是否是上位机控制的状态
    """
    def is_pc_control(self):
        if  self.control_msg.text() == SC2020_12G_Preferences._control_tag[1]:
            return  True
        return False

    def _on_fan_speed_changed(self, index):
        # sender = self.sender()
        _fan_speed = SC2020_12G_Preferences.get_fan_speed_by_index(index)
        if self.is_pc_control():
            self.fan_speed_cbIndex = index
            self._parent.controller.set_setting_params({"Fan_Speed": _fan_speed})
        else:
            self.fan_speed_comBox.blockSignals(True)
            self.fan_speed_comBox.setCurrentIndex(self.fan_speed_cbIndex)
            self.fan_speed_comBox.blockSignals(False)
            self.is_pc_signal.emit()

    def _on_color_metry_changed(self, index):
        # sender = self.sender()
        _color_metry = SC2020_12G_Preferences.get_color_metry_by_index(index)
        if self.is_pc_control():
            self.color_metry_cbIndex = index
            self._parent.controller.set_setting_params({"Color_Metry": _color_metry})
        else:
            self.color_metry_comBox_2.blockSignals(True)
            self.color_metry_comBox_2.setCurrentIndex(self.color_metry_cbIndex)
            self.color_metry_comBox_2.blockSignals(False)
            self.is_pc_signal.emit()

    def _on_hdmi_out_range_changed(self, index):
        #sender = self.sender()
        _hdmi_out_range = SC2020_12G_Preferences.get_hdmi_out_range_by_index(index)
        if self.is_pc_control():
            self.hdmi_out_range_cbIndex = index
            self._parent.controller.set_setting_params({"HDMI_Out_Range": _hdmi_out_range})
        else:
            self.hdmi_out_range_comBox_2.blockSignals(True)
            self.hdmi_out_range_comBox_2.setCurrentIndex(self.hdmi_out_range_cbIndex)
            self.hdmi_out_range_comBox_2.blockSignals(False)
            self.is_pc_signal.emit()

    def _on_sdi_out_src_changed(self, index):
        #sender = self.sender()
        _sdi_out_src = SC2020_12G_Preferences.get_sdi_sfp_out_by_index(index)
        if self.is_pc_control():
            self.sdi_out_src_cbIndex = index
            self._parent.controller.set_setting_params({"SDI_SFP_Out_Src": index})  # _sdi_out_src
        else:
            self.sdi_out_src_comBox_2.blockSignals(True)
            self.sdi_out_src_comBox_2.setCurrentIndex(self.sdi_out_src_cbIndex)
            self.sdi_out_src_comBox_2.blockSignals(False)
            self.is_pc_signal.emit()

    def _on_hdmi_out_src_changed(self, index):
        #sender = self.sender()
        _hdmi_out_src = SC2020_12G_Preferences.get_hdmi_out_src_by_index(index)
        if self.is_pc_control():
            self.hdmi_out_src_cbIndex = index
            self._parent.controller.set_setting_params({"HDMI_Out_Source": index}) #_hdmi_out_src
        else:
            self.hdmi_out_src_comBox_2.blockSignals(True)
            self.hdmi_out_src_comBox_2.setCurrentIndex(self.hdmi_out_src_cbIndex)
            self.hdmi_out_src_comBox_2.blockSignals(False)
            self.is_pc_signal.emit()

    def _on_sdi_sfp_mode_changed(self, index):
        #sender = self.sender()
        _sdi_sfp_mode = SC2020_12G_Preferences.get_sdi_sfp_in_mode_by_index(index)
        if self.is_pc_control():
            self.sdi_sfp_mode_cbIndex = index
            self._parent.controller.set_setting_params({"SDI_SFP_Mode": _sdi_sfp_mode})

            self.hdmi_out_src_cbIndex = self.hdmi_out_src_comBox_2.currentIndex()
            self.sdi_out_src_cbIndex = self.sdi_out_src_comBox_2.currentIndex()
            if _sdi_sfp_mode == "SFP In":
                with QSignalBlocker(self.hdmi_out_src_comBox_2):
                    self.hdmi_out_src_comBox_2.clear()
                    self.hdmi_out_src_comBox_2.addItems(SC2020_12G_Preferences._hdmi_out_src_sfp)
                    if self.hdmi_out_src_comBox_2.view() and not self.hdmi_out_src_comBox_2.view().isVisible():
                        self.hdmi_out_src_comBox_2.setCurrentIndex(self.hdmi_out_src_cbIndex)
                with QSignalBlocker(self.sdi_out_src_comBox_2):
                    self.sdi_out_src_comBox_2.clear()
                    self.sdi_out_src_comBox_2.addItems(SC2020_12G_Preferences._sdi_sfp_out_src_sfp)
                    if self.sdi_out_src_comBox_2.view() and not self.sdi_out_src_comBox_2.view().isVisible():
                        self.sdi_out_src_comBox_2.setCurrentIndex(self.sdi_out_src_cbIndex)
            if _sdi_sfp_mode == "SDI In":
                with QSignalBlocker(self.hdmi_out_src_comBox_2):
                    self.hdmi_out_src_comBox_2.clear()
                    self.hdmi_out_src_comBox_2.addItems(SC2020_12G_Preferences._hdmi_out_src_sdi)
                    if self.hdmi_out_src_comBox_2.view() and not self.hdmi_out_src_comBox_2.view().isVisible():
                        self.hdmi_out_src_comBox_2.setCurrentIndex(self.hdmi_out_src_cbIndex)
                with QSignalBlocker(self.sdi_out_src_comBox_2):
                    self.sdi_out_src_comBox_2.clear()
                    self.sdi_out_src_comBox_2.addItems(SC2020_12G_Preferences._sdi_sfp_out_src_sdi)
                    if self.sdi_out_src_comBox_2.view() and not self.sdi_out_src_comBox_2.view().isVisible():
                        self.sdi_out_src_comBox_2.setCurrentIndex(self.sdi_out_src_cbIndex)
        else:
            self.sdi_sfp_mode_comBox_2.blockSignals(True)
            self.sdi_sfp_mode_comBox_2.setCurrentIndex(self.sdi_sfp_mode_cbIndex)
            self.sdi_sfp_mode_comBox_2.blockSignals(False)
            self.is_pc_signal.emit()

    def _on_sdi_3g_out_changed(self, index):
        #sender = self.sender()
        _sdi_3g = SC2020_12G_Preferences.get_3g_sdi_out_by_index(index)
        if self.is_pc_control():
            self.sdi_3g_cbIndex = index
            self._parent.controller.set_setting_params({"3G_SDI_Out": _sdi_3g})
        else:
            self.sdi_3g_out_comBox_2.blockSignals(True)
            self.sdi_3g_out_comBox_2.setCurrentIndex(self.sdi_3g_cbIndex)
            self.sdi_3g_out_comBox_2.blockSignals(False)
            self.is_pc_signal.emit()

    def _on_color_space_changed(self, index):
        #sender = self.sender()
        _color_space = SC2020_12G_Preferences.get_hdmi_out_color_by_index(index)
        if self.is_pc_control():
            self.hdmi_color_cbIndex = index
            self._parent.controller.set_setting_params({"HDMI_Out_Color": _color_space})
        else:
            self.hdmi_out_color_comBox.blockSignals(True)
            self.hdmi_out_color_comBox.setCurrentIndex(self.hdmi_color_cbIndex)
            self.hdmi_out_color_comBox.blockSignals(False)
            self.is_pc_signal.emit()

    def deal_hdmi_in_format(self, value):
        fresh_rate = value & 0xF
        format_value = (value >> 4) & 0xF
        return (format_value,fresh_rate)

    def thread_get_param(self):
        # 如果已有线程在运行，先停止它
        if self._version_thread and self._version_thread.is_alive():
            self._version_thread_stop.set()
            self._version_thread.join(timeout=1.0)  # 等待线程结束，最多等待1秒

        # 重置停止事件并创建新线程
        self._version_thread_stop.clear()
        self._version_thread = threading.Thread(target=self.thread_get_version_timer)
        self._version_thread.daemon = True  # 设置为守护线程
        self._version_thread.start()
        #threading.Thread(target=self.thread_get_version_timer).start()

    def thread_get_version_timer(self):
        while not self._version_thread_stop.is_set():
            self._parent.controller.get_setting_params()
            # 每隔1秒检查一次是否需要停止
            if self._version_thread_stop.wait(timeout=1.0):
                break

    def __del__(self):
        # 在对象销毁时确保线程被正确停止
        if self._version_thread and self._version_thread.is_alive():
            self._version_thread_stop.set()
            self._version_thread.join(timeout=1.0)


    def showEvent(self, event):
        self._parent.controller.get_version_info()
        if self.isOpenThreading:
            self.thread_get_param()
            self.isOpenThreading =False



        #self._parent.controller.thread_get_version()
        #self._parent.controller.get_setting_params()

        super().showEvent(event)  # 调用基类的 showEvent 方法

    def hideEvent(self, event):
        # 当窗口隐藏时停止线程以节省资源
        if self._version_thread and self._version_thread.is_alive():
            self._version_thread_stop.set()
            self._version_thread.join(timeout=1.0)  # 等待线程结束，最多等待1秒
        self.isOpenThreading = True  # 重置标志，以便下次显示时重新启动线程
        super().hideEvent(event)

    def _Is_Pc_Control_Widget(self):
        # widget = self.sender()
        # 在代码中定义需要翻译的字符串，使用占位符
        # message_template = QCoreApplication.translate("Global_Tips", u"Are you sure you want to remove device?", None)
        # 使用字符串替换方法来插入变量值
        message_template="Please set DIP switches to PC"
        #message = message_template.format(widget.device_name_label.text())
        #title = QCoreApplication.translate("Global_Tips", u"Warning", None)
        title = "Control Mode"

        msg_box = QMessageBox(QMessageBox.Question, title, message_template, QMessageBox.Yes)

        yes_button = msg_box.button(QMessageBox.StandardButton.Yes)
        yes_button.setText("OK") # QCoreApplication.translate("MainWidget", u"Yes", None)
        # no_button = msg_box.button(QMessageBox.StandardButton.No)
        # no_button.setText(QCoreApplication.translate("MainWidget", u"No", None))

        response = msg_box.exec()

    def toggle_temp_display(self):
        # 交替显示摄氏度和华氏度
        if self.display_celsius:
            self.temp_msg.setText("{:.1f}℉".format(self.current_temp_f))
            # self.animate_temp_display("{:.1f}℉".format(self.current_temp_f))
            self.display_celsius = False
        else:
            self.temp_msg.setText("{:.1f}℃".format(self.current_temp_c))
            # self.animate_temp_display("{:.1f}℃".format(self.current_temp_c))
            self.display_celsius = True

    #  ---------------
    def animate_temp_display(self, text):
        # 创建滚动动画效果
        if not hasattr(self, 'temp_animation') or self.temp_animation is None:
            # 创建动画对象
            self.temp_animation = QPropertyAnimation()
            self.temp_animation.setDuration(500)  # 动画持续时间500毫秒
            self.temp_animation.setEasingCurve(QEasingCurve.OutCubic)  # 缓动曲线

        # 获取当前标签的几何信息
        original_geometry = self.temp_msg.geometry()

        # 创建旧文本标签（当前显示的文本）
        if hasattr(self, 'old_temp_label') and self.old_temp_label is not None:
            self.old_temp_label.deleteLater()

        self.old_temp_label = QLabel(self.temp_msg.parent())
        self.old_temp_label.setGeometry(original_geometry)
        self.old_temp_label.setText(self.temp_msg.text())
        self.old_temp_label.setStyleSheet(self.temp_msg.styleSheet())
        self.old_temp_label.setAlignment(self.temp_msg.alignment())
        self.old_temp_label.show()

        # 创建新文本标签（即将显示的文本）
        if hasattr(self, 'new_temp_label') and self.new_temp_label is not None:
            self.new_temp_label.deleteLater()

        self.new_temp_label = QLabel(self.temp_msg.parent())
        # 将新标签放置在原始位置的下方（隐藏状态）
        self.new_temp_label.setGeometry(QRect(
            original_geometry.x(),
            original_geometry.y() + original_geometry.height(),
            original_geometry.width(),
            original_geometry.height()
        ))
        self.new_temp_label.setText(text)
        self.new_temp_label.setStyleSheet(self.temp_msg.styleSheet())
        self.new_temp_label.setAlignment(self.temp_msg.alignment())
        self.new_temp_label.show()

        # 设置动画属性 - 旧标签向上移动
        self.temp_animation.setTargetObject(self.old_temp_label)
        self.temp_animation.setPropertyName(b"geometry")
        self.temp_animation.setStartValue(original_geometry)
        self.temp_animation.setEndValue(QRect(
            original_geometry.x(),
            original_geometry.y() - original_geometry.height(),
            original_geometry.width(),
            original_geometry.height()
        ))

        # 创建第二个动画 - 新标签从下方滚动到原位置
        self.new_temp_animation = QPropertyAnimation(self.new_temp_label, b"geometry")
        self.new_temp_animation.setDuration(500)
        self.new_temp_animation.setEasingCurve(QEasingCurve.OutCubic)
        self.new_temp_animation.setStartValue(QRect(
            original_geometry.x(),
            original_geometry.y() + original_geometry.height(),
            original_geometry.width(),
            original_geometry.height()
        ))
        self.new_temp_animation.setEndValue(original_geometry)

        # 启动动画
        self.temp_animation.start()
        self.new_temp_animation.start()

        # 动画结束后清理
        self.new_temp_animation.finished.connect(self.on_animation_finished)

    def on_animation_finished(self):
        # 动画完成后，更新主标签文本并清理临时标签
        if self.new_temp_label is not None:
            self.temp_msg.setText(self.new_temp_label.text())
            self.new_temp_label.deleteLater()
            self.new_temp_label = None

        if self.old_temp_label is not None:
            self.old_temp_label.deleteLater()
            self.old_temp_label = None

    # ------------------
    def handle_async_callback(self, obj):
        if obj["function"] == "get_version_info":
            # _model = self._parent.args["args"]["model"]
            # _manufacturer = self._parent.args["args"]["manufacturer"]
            # _sn = self._parent.args["args"]["sn"]
            # self.label_model.setText(_model)
            # self.label_manufacturer.setText(_manufacturer)
            # self.label_sn.setText(_sn)

            args = obj["args"]
            logging.debug("args:{}".format(args))
            _mcu_mode = ModelPreferences.get_mcu_mode_by_index(args["MCUMode"])
            _protocol_version = "V%d.%d" % (args["ProtocolVersion"][0], args["ProtocolVersion"][1])
            _boot_version = ""
            _app_version = ""
            _fpga_version = ""
            _hardware_version = ""
            if args["BootVersion"][3] != 0:
                _boot_version = "V%d.%d.%d.%d" % (args["BootVersion"][0], args["BootVersion"][1],
                                                  args["BootVersion"][2], args["BootVersion"][3])
            else:
                _boot_version = "V%d.%d.%d" % (args["BootVersion"][0], args["BootVersion"][1], args["BootVersion"][2])
            if args["APPVersion"][3] != 0:
                _app_version = "V%d.%d.%d.%d" % (args["APPVersion"][0], args["APPVersion"][1],
                                                 args["APPVersion"][2], args["APPVersion"][3])
            else:
                _app_version = "V%d.%d.%d" % (args["APPVersion"][0], args["APPVersion"][1], args["APPVersion"][2])
            if args["FPGAVersion"][3] != 0:
                _fpga_version = "V%d.%d.%d.%d" % (args["FPGAVersion"][0], args["FPGAVersion"][1],
                                                  args["FPGAVersion"][2], args["FPGAVersion"][3])
            else:
                _fpga_version = "V%d.%d.%d" % (args["FPGAVersion"][0], args["FPGAVersion"][1], args["FPGAVersion"][2])
            if args["HardwareVersion"][3] != 0:
                _hardware_version = "V%d.%d.%d.%d" % (args["HardwareVersion"][0], args["HardwareVersion"][1],
                                                      args["HardwareVersion"][2], args["HardwareVersion"][3])
            elif args["HardwareVersion"][2] != 0:
                _hardware_version = "V%d.%d.%d" % (args["HardwareVersion"][0], args["HardwareVersion"][1], args["HardwareVersion"][2])
            else:
                _hardware_version = "V%d.%d" % (args["HardwareVersion"][0], args["HardwareVersion"][1])
            # self.label_mcu_mode.setText(_mcu_mode)
            # self.label_protocol_ver.setText(_protocol_version)
            # self.label_boot_version.setText(_boot_version)
            # self.label_app_version.setText(_app_version)
            # self.label_fpga_version.setText(_fpga_version)
            # self.label_hardware_ver.setText(_hardware_version)
            self.system_msg.setText(_app_version)
            self.yingjian_msg.setText(_hardware_version)
            self.image_msg.setText(_fpga_version)
        if obj["function"] == "get_setting_params":
            args = obj["args"]
            #logging.debug("args:{}".format(args))

            if "SDI_SFP_Out_Src" in args:
                self.sdi_out_src_comBox_2.blockSignals(True)
                self.sdi_out_src_comBox_2.setCurrentIndex(args["SDI_SFP_Out_Src"])
                self.sdi_out_src_comBox_2.blockSignals(False)

            if "HDMI_Out_Source" in args:
                self.hdmi_out_src_comBox_2.blockSignals(True)
                if self.hdmi_out_src_comBox_2.view() and not self.hdmi_out_src_comBox_2.view().isVisible():
                    self.hdmi_out_src_comBox_2.setCurrentIndex(args["HDMI_Out_Source"])

                self.hdmi_out_src_comBox_2.blockSignals(False)

            if "HDMI_Out_Range" in args:
                self.hdmi_out_range_comBox_2.blockSignals(True)
                self.hdmi_out_range_comBox_2.setCurrentIndex(args["HDMI_Out_Range"])
                self.hdmi_out_range_comBox_2.blockSignals(False)

            if "3G_SDI_Out" in args:
                self.sdi_3g_out_comBox_2.blockSignals(True)
                self.sdi_3g_out_comBox_2.setCurrentIndex(args["3G_SDI_Out"])
                self.sdi_3g_out_comBox_2.blockSignals(False)

            if "HDMI_Out_Color" in args:
                self.hdmi_out_color_comBox.blockSignals(True)
                self.hdmi_out_color_comBox.setCurrentIndex(args["HDMI_Out_Color"])
                self.hdmi_out_color_comBox.blockSignals(False)

            if "SDI_SFP_Mode" in args:
                self.sdi_sfp_mode_comBox_2.blockSignals(True)
                self.sdi_sfp_mode_comBox_2.setCurrentIndex(args["SDI_SFP_Mode"])
                self.sdi_sfp_mode_comBox_2.blockSignals(False)
                self.hdmi_out_src_cbIndex = self.hdmi_out_src_comBox_2.currentIndex()
                self.sdi_out_src_cbIndex = self.sdi_out_src_comBox_2.currentIndex()
                if args["SDI_SFP_Mode"] == 0:
                    with QSignalBlocker(self.hdmi_out_src_comBox_2):
                        if self.hdmi_out_src_comBox_2.view() and not self.hdmi_out_src_comBox_2.view().isVisible():
                            self.hdmi_out_src_comBox_2.clear()
                            self.hdmi_out_src_comBox_2.addItems(SC2020_12G_Preferences._hdmi_out_src_sfp)
                            self.hdmi_out_src_comBox_2.setCurrentIndex(self.hdmi_out_src_cbIndex)
                    with QSignalBlocker(self.sdi_out_src_comBox_2):
                        if self.sdi_out_src_comBox_2.view() and not self.sdi_out_src_comBox_2.view().isVisible():
                            self.sdi_out_src_comBox_2.clear()
                            self.sdi_out_src_comBox_2.addItems(SC2020_12G_Preferences._sdi_sfp_out_src_sfp)
                            self.sdi_out_src_comBox_2.setCurrentIndex(self.sdi_out_src_cbIndex)
                else:
                    with QSignalBlocker(self.hdmi_out_src_comBox_2):
                        if self.hdmi_out_src_comBox_2.view() and not self.hdmi_out_src_comBox_2.view().isVisible():
                            self.hdmi_out_src_comBox_2.clear()
                            self.hdmi_out_src_comBox_2.addItems(SC2020_12G_Preferences._hdmi_out_src_sdi)
                            self.hdmi_out_src_comBox_2.setCurrentIndex(self.hdmi_out_src_cbIndex)
                    with QSignalBlocker(self.sdi_out_src_comBox_2):
                        if self.sdi_out_src_comBox_2.view() and not self.sdi_out_src_comBox_2.view().isVisible():
                            self.sdi_out_src_comBox_2.clear()
                            self.sdi_out_src_comBox_2.addItems(SC2020_12G_Preferences._sdi_sfp_out_src_sdi)
                            self.sdi_out_src_comBox_2.setCurrentIndex(self.sdi_out_src_cbIndex)


            if "Color_Metry" in args:
                self.color_metry_comBox_2.blockSignals(True)
                self.color_metry_comBox_2.setCurrentIndex(args["Color_Metry"])
                self.color_metry_comBox_2.blockSignals(False)

            if "FPGA_Temperature" in args:
                _temp = args["FPGA_Temperature"]*503.975/65536 -273.15
                _f_temp = _temp * 9/5 + 32
                # self.temp_msg.setText("{:.1f}℃/{:.1f}℉".format(_temp,_f_temp))
                # 保存温度值供定时器使用
                if _temp>0:
                    self.current_temp_c = _temp
                    self.current_temp_f = _f_temp

                # 创建定时器用于交替显示温度
                if not hasattr(self, 'temp_display_timer'):
                    self.temp_display_timer = QTimer()
                    self.temp_display_timer.timeout.connect(self.toggle_temp_display)
                    self.display_celsius = True  # 标记当前显示摄氏度还是华氏度

                # 立即显示摄氏度温度
                self.temp_msg.setText("{:.1f}℃".format(self.current_temp_c))

                # 启动定时器，每3秒切换一次显示
                if not self.temp_display_timer.isActive():
                    self.temp_display_timer.start(2500)  # 3秒间隔

            if "HDMI_In_Format" in args :
                _format_value , _fresh_rate_value = self.deal_hdmi_in_format(args["HDMI_In_Format"])
                _fenbianlv = SC2020_12G_Preferences.get_format_list_by_index(_format_value)  # 分辨率
                _zhenlv = SC2020_12G_Preferences.get_fresh_rate_list_by_index(_fresh_rate_value)  # 帧率

                if _format_value !=0 and _fenbianlv != "Unknow" and _fenbianlv != "No Signal":
                    res_value = _fenbianlv[:-1]  # 取到分辨率
                    if '/' in _zhenlv:
                        rt = _zhenlv.split('/')
                        if _fenbianlv[-1].lower() == 'p':
                            _zhenlv = _fenbianlv[-1].lower() + rt[0]
                        else:
                            _zhenlv = _fenbianlv[-1].lower() + rt[1]

                    _fenbianlv = res_value

                self.fenbianlv_hdmi_msg.setText(_fenbianlv)
                self.rate_hdmi_msg.setText(_zhenlv)

                # 处理其他输入源
                if _format_value !=0:
                    if "HDMI_In_Color" in args:
                        self.color_space_hdmi_msg.setText(SC2020_12G_Preferences.get_hdmi_in_color_by_index(args["HDMI_In_Color"]))
                    if "HDMI_IN_Color_depth" in args:
                        self.bit_hdmi_msg.setText(SC2020_12G_Preferences.get_hdmi_in_color_depth_by_index(args["HDMI_IN_Color_depth"]))
                    if "HDMI_In_Colorimetry" in args:
                        self.seyu_hdmi_msg.setText(SC2020_12G_Preferences.get_color_metry_by_index(args["HDMI_In_Colorimetry"]))
                else:
                    self.color_space_hdmi_msg.setText(SC2020_12G_Preferences.format_list[0])
                    self.bit_hdmi_msg.setText(SC2020_12G_Preferences.format_list[0])
                    self.seyu_hdmi_msg.setText(SC2020_12G_Preferences.format_list[0])

            if "SDI_SFP_In_Format" in args:
                _sdi_format_value, _sdi_fresh_rate_value = self.deal_hdmi_in_format(args["SDI_SFP_In_Format"])
                _sdi_fenbianlv = SC2020_12G_Preferences.get_format_list_by_index(_sdi_format_value)  # 分辨率
                _sdi_zhenlv = SC2020_12G_Preferences.get_fresh_rate_list_by_index(_sdi_fresh_rate_value)  # 帧率

                if _sdi_format_value != 0 and _sdi_fenbianlv != "Unknow" and _sdi_fenbianlv != "No Signal":
                    res_values = _sdi_fenbianlv[:-1]  # 取到分辨率
                    if '/' in _sdi_zhenlv:
                        rt = _sdi_zhenlv.split('/')
                        if _sdi_fenbianlv[-1].lower() == 'p':
                            _sdi_zhenlv = _sdi_fenbianlv[-1].lower() + rt[0]
                        else:
                            _sdi_zhenlv = _sdi_fenbianlv[-1].lower() + rt[1]

                    _sdi_fenbianlv = res_values

                self.fenbianlv_sdi_msg.setText(_sdi_fenbianlv)
                self.rate_sdi_msg.setText(_sdi_zhenlv)

                # 处理其他输入源
                if _sdi_format_value != 0 and _sdi_fenbianlv != "Unknow":
                    if "SDI_In_Color" in args:
                        self.color_space_sdi_msg.setText(SC2020_12G_Preferences.get_hdmi_in_color_by_index(args["SDI_In_Color"]))

                    self.bit_sdi_msg.setText("10bits")
                    self.seyu_sdi_msg.setText(SC2020_12G_Preferences.format_list[0])
                else:
                    self.color_space_sdi_msg.setText(SC2020_12G_Preferences.format_list[0])
                    self.bit_sdi_msg.setText(SC2020_12G_Preferences.format_list[0])
                    self.seyu_sdi_msg.setText(SC2020_12G_Preferences.format_list[0])

            if "Fan_Speed" in args:
                self.fan_speed_comBox.blockSignals(True)
                self.fan_speed_comBox.setCurrentIndex(args["Fan_Speed"])
                self.fan_speed_comBox.blockSignals(False)

            if "DIP_PC_Flag" in args:
                self.control_msg.setText(SC2020_12G_Preferences.get_control_tag_by_index(args["DIP_PC_Flag"]))
                # 绑定是否电脑上位机控制 信号
                if not self._control_state_checked:
                    self._control_state_checked = True
                    if not self.is_pc_control():
                        self._Is_Pc_Control_Widget()


        elif obj["function"] == "set_setting_params":
            args = obj["args"]
            logging.debug("Set setting params args args:{}".format(args))
import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSignalBlocker, Qt, Signal, QCoreApplication
from src.ui.mividcon_sh_cross.cross_audio_ui import Ui_Cross_Audio_Form
from src.model.modelPreferences import ModelPreferences
from src.model.mividcon_sh_cross.CrossPreferences import CrossPreferences
from globals import relative_path, global_qss

class CrossAudio(Ui_Cross_Audio_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.sdi_long = 0
        self.hdmi_long = 0

        self.translated_items_hdmi_out = [
            QCoreApplication.translate("Cross_Audio_Form", item, None)
            for item in CrossPreferences._hdmi_out_audio_channels
        ]
        self.translated_items_hdmi_out_sdi = [
            QCoreApplication.translate("Cross_Audio_Form", item, None)
            for item in CrossPreferences._hdmi_out_audio_channels_sdi
        ]
        self.translated_items_tpg_audio = [
            QCoreApplication.translate("Cross_Audio_Form", item, None)
            for item in CrossPreferences._tpg_audio_test
        ]

        self.hdmiOutCh_1_2_comboBox.addItems(self.translated_items_hdmi_out)
        self.hdmiOutCh_3_4_comboBox.addItems(self.translated_items_hdmi_out)
        self.hdmiOutCh_5_6_comboBox.addItems(self.translated_items_hdmi_out)
        self.hdmiOutCh_7_8_comboBox.addItems(self.translated_items_hdmi_out)
        self.sdiOutCh_1_2_comboBox.addItems(CrossPreferences._sdi_out_audio_channels)
        self.sdiOutCh_3_4_comboBox.addItems(CrossPreferences._sdi_out_audio_channels)
        self.sdiOutCh_5_6_comboBox.addItems(CrossPreferences._sdi_out_audio_channels)
        self.sdiOutCh_7_8_comboBox.addItems(CrossPreferences._sdi_out_audio_channels)
        self.sdiOutCh_9_10_comboBox.addItems(CrossPreferences._sdi_out_audio_channels)
        self.sdiOutCh_11_12_comboBox.addItems(CrossPreferences._sdi_out_audio_channels)
        self.sdiOutCh_13_14_comboBox.addItems(CrossPreferences._sdi_out_audio_channels)
        self.sdiOutCh_15_16_comboBox.addItems(CrossPreferences._sdi_out_audio_channels)
        self.analog_audio_comboBox.addItems(CrossPreferences._Analog_Audio_Out)  #新增
        self.tpg_audio_comboBox.addItems(self.translated_items_tpg_audio)  #新增

        self.hdmiOutCh_1_2_comboBox.currentIndexChanged.connect(lambda index: self._on_hdmi_audio_channel_index_changed(index, "HDMIOutChannel_1_2"))
        self.hdmiOutCh_3_4_comboBox.currentIndexChanged.connect(lambda index: self._on_hdmi_audio_channel_index_changed(index, "HDMIOutChannel_3_4"))
        self.hdmiOutCh_5_6_comboBox.currentIndexChanged.connect(lambda index: self._on_hdmi_audio_channel_index_changed(index, "HDMIOutChannel_5_6"))
        self.hdmiOutCh_7_8_comboBox.currentIndexChanged.connect(lambda index: self._on_hdmi_audio_channel_index_changed(index, "HDMIOutChannel_7_8"))
        self.sdiOutCh_1_2_comboBox.currentIndexChanged.connect(lambda index: self._on_sdi_audio_channel_index_changed(index, "SDIOutChannel_1_2"))
        self.sdiOutCh_3_4_comboBox.currentIndexChanged.connect(lambda index: self._on_sdi_audio_channel_index_changed(index, "SDIOutChannel_3_4"))
        self.sdiOutCh_5_6_comboBox.currentIndexChanged.connect(lambda index: self._on_sdi_audio_channel_index_changed(index, "SDIOutChannel_5_6"))
        self.sdiOutCh_7_8_comboBox.currentIndexChanged.connect(lambda index: self._on_sdi_audio_channel_index_changed(index, "SDIOutChannel_7_8"))
        self.sdiOutCh_9_10_comboBox.currentIndexChanged.connect(lambda index: self._on_sdi_audio_channel_index_changed(index, "SDIOutChannel_9_10"))
        self.sdiOutCh_11_12_comboBox.currentIndexChanged.connect(lambda index: self._on_sdi_audio_channel_index_changed(index, "SDIOutChannel_11_12"))
        self.sdiOutCh_13_14_comboBox.currentIndexChanged.connect(lambda index: self._on_sdi_audio_channel_index_changed(index, "SDIOutChannel_13_14"))
        self.sdiOutCh_15_16_comboBox.currentIndexChanged.connect(lambda index: self._on_sdi_audio_channel_index_changed(index, "SDIOutChannel_15_16"))
        self.analog_audio_comboBox.currentIndexChanged.connect(lambda index: self._on_analog_audio_channel_index_changed(index, "AnalogAudio")) # 新增
        self.tpg_audio_comboBox.currentIndexChanged.connect(lambda index: self._on_tpg_audio_channel_index_changed(index, "TPGAudio"))   # 新增

    def _on_analog_audio_channel_index_changed(self, index, channel):
        _args = {
            channel:  CrossPreferences.get_analog_audio_out_by_index(index)
        }
        logging.debug(f"_on_analog_audio_channel_index_changed: _args={_args}")
        self._parent.controller.set_audio_params(_args)

    def _on_tpg_audio_channel_index_changed(self, index, channel):
        _args = {
            channel:  CrossPreferences.get_tpg_audio_test_by_index(index)
        }
        logging.debug(f"_on_tpg_audio_channel_index_changed: _args={_args}")
        self._parent.controller.set_audio_params(_args)

    def _on_hdmi_audio_channel_index_changed(self, index, channel):
        _args ={}
        if self.hdmi_long == 1:
            _args = {
                channel:  CrossPreferences.get_hdmi_out_audio_channel_by_index(index),
                "flag": self.hdmi_long
            }
        elif self.hdmi_long == 0:
            _args = {
                channel:  CrossPreferences.get_hdmi_out_audio_channel_sdi_by_index(index),
                "flag": self.hdmi_long
            }
        logging.debug(f"_on_hdmi_channel_index_changed: _args={_args}")
        self._parent.controller.set_audio_params(_args)

    def _on_sdi_audio_channel_index_changed(self, index, channel):
        _args={}
        if self.sdi_long == 1:
            _args = {
                channel:  CrossPreferences.get_sdi_out_audio_channel_by_index(index),
                "flag":self.sdi_long
            }
        elif self.sdi_long == 0:
            _args = {
                channel:  CrossPreferences.get_sdi_out_audio_channel_sdi_by_index(index),
                "flag": self.sdi_long
            }
        logging.debug(f"_on_sdi_channel_index_changed: _args={_args}")
        self._parent.controller.set_audio_params(_args)

    def showEvent(self, event):
        self._parent.controller.get_output_video_params()
        self._parent.controller.get_output_audio_params()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):

        if obj["function"] == "get_output_video_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))

            self.hdmiOutCh_1_2_comboBox.blockSignals(True)
            self.hdmiOutCh_3_4_comboBox.blockSignals(True)
            self.hdmiOutCh_5_6_comboBox.blockSignals(True)
            self.hdmiOutCh_7_8_comboBox.blockSignals(True)
            self.sdiOutCh_1_2_comboBox.blockSignals(True)
            self.sdiOutCh_3_4_comboBox.blockSignals(True)
            self.sdiOutCh_5_6_comboBox.blockSignals(True)
            self.sdiOutCh_7_8_comboBox.blockSignals(True)
            self.sdiOutCh_9_10_comboBox.blockSignals(True)
            self.sdiOutCh_11_12_comboBox.blockSignals(True)
            self.sdiOutCh_13_14_comboBox.blockSignals(True)
            self.sdiOutCh_15_16_comboBox.blockSignals(True)
            self.tpg_audio_comboBox.blockSignals(True)

            # 翻译下拉列表项
            self.translated_items_hdmi_out = [
                QCoreApplication.translate("Cross_Audio_Form", item, None)
                for item in CrossPreferences._hdmi_out_audio_channels
            ]
            self.translated_items_hdmi_out_sdi = [
                QCoreApplication.translate("Cross_Audio_Form", item, None)
                for item in CrossPreferences._hdmi_out_audio_channels_sdi
            ]
            self.translated_items_sdi_out = [
                QCoreApplication.translate("Cross_Audio_Form", item, None)
                for item in CrossPreferences._sdi_out_audio_channels
            ]
            self.translated_items_sdi_out_sdi = [
                QCoreApplication.translate("Cross_Audio_Form", item, None)
                for item in CrossPreferences._sdi_out_audio_channels_sdi
            ]
            self.translated_items_tpg_audio = [
                QCoreApplication.translate("Cross_Audio_Form", item, None)
                for item in CrossPreferences._tpg_audio_test
            ]
            self.tpg_audio_comboBox.clear()
            self.tpg_audio_comboBox.addItems(self.translated_items_tpg_audio)
            try:
                self.sdi_long=args['SDIOut']["source"]
                self.hdmi_long = args['HDMIOut']["source"]
                if self.sdi_long==2:
                    self.sdi_long=args['Scaler']["source"]
                if self.hdmi_long == 2:
                    self.hdmi_long = args['Scaler']["source"]
                # 保存当前选中的索引值
                hdmi_indices = [
                    self.hdmiOutCh_1_2_comboBox.currentIndex(),
                    self.hdmiOutCh_3_4_comboBox.currentIndex(),
                    self.hdmiOutCh_5_6_comboBox.currentIndex(),
                    self.hdmiOutCh_7_8_comboBox.currentIndex()
                ]

                sdi_indices = [
                    self.sdiOutCh_1_2_comboBox.currentIndex(),
                    self.sdiOutCh_3_4_comboBox.currentIndex(),
                    self.sdiOutCh_5_6_comboBox.currentIndex(),
                    self.sdiOutCh_7_8_comboBox.currentIndex(),
                    self.sdiOutCh_9_10_comboBox.currentIndex(),
                    self.sdiOutCh_11_12_comboBox.currentIndex(),
                    self.sdiOutCh_13_14_comboBox.currentIndex(),
                    self.sdiOutCh_15_16_comboBox.currentIndex()
                ]



                self.hdmiOutCh_1_2_comboBox.clear()
                self.hdmiOutCh_3_4_comboBox.clear()
                self.hdmiOutCh_5_6_comboBox.clear()
                self.hdmiOutCh_7_8_comboBox.clear()
                self.sdiOutCh_1_2_comboBox.clear()
                self.sdiOutCh_3_4_comboBox.clear()
                self.sdiOutCh_5_6_comboBox.clear()
                self.sdiOutCh_7_8_comboBox.clear()
                self.sdiOutCh_9_10_comboBox.clear()
                self.sdiOutCh_11_12_comboBox.clear()
                self.sdiOutCh_13_14_comboBox.clear()
                self.sdiOutCh_15_16_comboBox.clear()

                if args['SDIOut']["source"] == 1:  # HDMI In
                    self.sdiOutCh_1_2_comboBox.addItems(self.translated_items_sdi_out)
                    self.sdiOutCh_3_4_comboBox.addItems(self.translated_items_sdi_out)
                    self.sdiOutCh_5_6_comboBox.addItems(self.translated_items_sdi_out)
                    self.sdiOutCh_7_8_comboBox.addItems(self.translated_items_sdi_out)
                    self.sdiOutCh_9_10_comboBox.addItems(self.translated_items_sdi_out)
                    self.sdiOutCh_11_12_comboBox.addItems(self.translated_items_sdi_out)
                    self.sdiOutCh_13_14_comboBox.addItems(self.translated_items_sdi_out)
                    self.sdiOutCh_15_16_comboBox.addItems(self.translated_items_sdi_out)
                elif args['SDIOut']["source"] == 0:
                    self.sdiOutCh_1_2_comboBox.addItems(self.translated_items_sdi_out_sdi)
                    self.sdiOutCh_3_4_comboBox.addItems(self.translated_items_sdi_out_sdi)
                    self.sdiOutCh_5_6_comboBox.addItems(self.translated_items_sdi_out_sdi)
                    self.sdiOutCh_7_8_comboBox.addItems(self.translated_items_sdi_out_sdi)
                    self.sdiOutCh_9_10_comboBox.addItems(self.translated_items_sdi_out_sdi)
                    self.sdiOutCh_11_12_comboBox.addItems(self.translated_items_sdi_out_sdi)
                    self.sdiOutCh_13_14_comboBox.addItems(self.translated_items_sdi_out_sdi)
                    self.sdiOutCh_15_16_comboBox.addItems(self.translated_items_sdi_out_sdi)

                if args['HDMIOut']["source"] == 1:  # HDMI In
                    self.hdmiOutCh_1_2_comboBox.addItems(self.translated_items_hdmi_out)
                    self.hdmiOutCh_3_4_comboBox.addItems(self.translated_items_hdmi_out)
                    self.hdmiOutCh_5_6_comboBox.addItems(self.translated_items_hdmi_out)
                    self.hdmiOutCh_7_8_comboBox.addItems(self.translated_items_hdmi_out)
                elif args['HDMIOut']["source"] == 0:
                    self.hdmiOutCh_1_2_comboBox.addItems(self.translated_items_hdmi_out_sdi)
                    self.hdmiOutCh_3_4_comboBox.addItems(self.translated_items_hdmi_out_sdi)
                    self.hdmiOutCh_5_6_comboBox.addItems(self.translated_items_hdmi_out_sdi)
                    self.hdmiOutCh_7_8_comboBox.addItems(self.translated_items_hdmi_out_sdi)

                if args['SDIOut']["source"]==2:
                    if args['Scaler']["source"] == 1:  # HDMI In
                        self.sdiOutCh_1_2_comboBox.addItems(self.translated_items_sdi_out)
                        self.sdiOutCh_3_4_comboBox.addItems(self.translated_items_sdi_out)
                        self.sdiOutCh_5_6_comboBox.addItems(self.translated_items_sdi_out)
                        self.sdiOutCh_7_8_comboBox.addItems(self.translated_items_sdi_out)
                        self.sdiOutCh_9_10_comboBox.addItems(self.translated_items_sdi_out)
                        self.sdiOutCh_11_12_comboBox.addItems(self.translated_items_sdi_out)
                        self.sdiOutCh_13_14_comboBox.addItems(self.translated_items_sdi_out)
                        self.sdiOutCh_15_16_comboBox.addItems(self.translated_items_sdi_out)
                    else:
                        self.sdiOutCh_1_2_comboBox.addItems(self.translated_items_sdi_out_sdi)
                        self.sdiOutCh_3_4_comboBox.addItems(self.translated_items_sdi_out_sdi)
                        self.sdiOutCh_5_6_comboBox.addItems(self.translated_items_sdi_out_sdi)
                        self.sdiOutCh_7_8_comboBox.addItems(self.translated_items_sdi_out_sdi)
                        self.sdiOutCh_9_10_comboBox.addItems(self.translated_items_sdi_out_sdi)
                        self.sdiOutCh_11_12_comboBox.addItems(self.translated_items_sdi_out_sdi)
                        self.sdiOutCh_13_14_comboBox.addItems(self.translated_items_sdi_out_sdi)
                        self.sdiOutCh_15_16_comboBox.addItems(self.translated_items_sdi_out_sdi)

                if args['HDMIOut']["source"] == 2:
                    if args['Scaler']["source"] == 1:  # HDMI In
                        self.hdmiOutCh_1_2_comboBox.addItems(self.translated_items_hdmi_out)
                        self.hdmiOutCh_3_4_comboBox.addItems(self.translated_items_hdmi_out)
                        self.hdmiOutCh_5_6_comboBox.addItems(self.translated_items_hdmi_out)
                        self.hdmiOutCh_7_8_comboBox.addItems(self.translated_items_hdmi_out)
                    else:
                        self.hdmiOutCh_1_2_comboBox.addItems(self.translated_items_hdmi_out_sdi)
                        self.hdmiOutCh_3_4_comboBox.addItems(self.translated_items_hdmi_out_sdi)
                        self.hdmiOutCh_5_6_comboBox.addItems(self.translated_items_hdmi_out_sdi)
                        self.hdmiOutCh_7_8_comboBox.addItems(self.translated_items_hdmi_out_sdi)

                self.hdmiOutCh_1_2_comboBox.setCurrentIndex(hdmi_indices[0])
                self.hdmiOutCh_3_4_comboBox.setCurrentIndex(hdmi_indices[1])
                self.hdmiOutCh_5_6_comboBox.setCurrentIndex(hdmi_indices[2])
                self.hdmiOutCh_7_8_comboBox.setCurrentIndex(hdmi_indices[3])
                self.sdiOutCh_1_2_comboBox.setCurrentIndex(sdi_indices[0])
                self.sdiOutCh_3_4_comboBox.setCurrentIndex(sdi_indices[1])
                self.sdiOutCh_5_6_comboBox.setCurrentIndex(sdi_indices[2])
                self.sdiOutCh_7_8_comboBox.setCurrentIndex(sdi_indices[3])
                self.sdiOutCh_9_10_comboBox.setCurrentIndex(sdi_indices[4])
                self.sdiOutCh_11_12_comboBox.setCurrentIndex(sdi_indices[5])
                self.sdiOutCh_13_14_comboBox.setCurrentIndex(sdi_indices[6])
                self.sdiOutCh_15_16_comboBox.setCurrentIndex(sdi_indices[7])
                # 恢复信号
                self.hdmiOutCh_1_2_comboBox.blockSignals(False)
                self.hdmiOutCh_3_4_comboBox.blockSignals(False)
                self.hdmiOutCh_5_6_comboBox.blockSignals(False)
                self.hdmiOutCh_7_8_comboBox.blockSignals(False)
                self.sdiOutCh_1_2_comboBox.blockSignals(False)
                self.sdiOutCh_3_4_comboBox.blockSignals(False)
                self.sdiOutCh_5_6_comboBox.blockSignals(False)
                self.sdiOutCh_7_8_comboBox.blockSignals(False)
                self.sdiOutCh_9_10_comboBox.blockSignals(False)
                self.sdiOutCh_11_12_comboBox.blockSignals(False)
                self.sdiOutCh_13_14_comboBox.blockSignals(False)
                self.sdiOutCh_15_16_comboBox.blockSignals(False)
                self.tpg_audio_comboBox.blockSignals(False)

            except Exception as e:
                logging.error("Update output video error!")

        if obj["function"] == "get_output_audio_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))
            try:
                self.hdmiOutCh_1_2_comboBox.blockSignals(True)
                self.hdmiOutCh_1_2_comboBox.setCurrentIndex(args["HDMIOutChannel_1_2"]["format"])
                self.hdmiOutCh_1_2_comboBox.blockSignals(False)

                self.hdmiOutCh_3_4_comboBox.blockSignals(True)
                self.hdmiOutCh_3_4_comboBox.setCurrentIndex(args["HDMIOutChannel_3_4"]["format"])
                self.hdmiOutCh_3_4_comboBox.blockSignals(False)

                self.hdmiOutCh_5_6_comboBox.blockSignals(True)
                self.hdmiOutCh_5_6_comboBox.setCurrentIndex(args["HDMIOutChannel_5_6"]["format"])
                self.hdmiOutCh_5_6_comboBox.blockSignals(False)

                self.hdmiOutCh_7_8_comboBox.blockSignals(True)
                self.hdmiOutCh_7_8_comboBox.setCurrentIndex(args["HDMIOutChannel_7_8"]["format"])
                self.hdmiOutCh_7_8_comboBox.blockSignals(False)

                self.sdiOutCh_1_2_comboBox.blockSignals(True)
                self.sdiOutCh_1_2_comboBox.setCurrentIndex(args["SDIOutChannel_1_2"]["format"])
                self.sdiOutCh_1_2_comboBox.blockSignals(False)

                self.sdiOutCh_3_4_comboBox.blockSignals(True)
                self.sdiOutCh_3_4_comboBox.setCurrentIndex(args["SDIOutChannel_3_4"]["format"])
                self.sdiOutCh_3_4_comboBox.blockSignals(False)

                self.sdiOutCh_5_6_comboBox.blockSignals(True)
                self.sdiOutCh_5_6_comboBox.setCurrentIndex(args["SDIOutChannel_5_6"]["format"])
                self.sdiOutCh_5_6_comboBox.blockSignals(False)

                self.sdiOutCh_7_8_comboBox.blockSignals(True)
                self.sdiOutCh_7_8_comboBox.setCurrentIndex(args["SDIOutChannel_7_8"]["format"])
                self.sdiOutCh_7_8_comboBox.blockSignals(False)

                self.sdiOutCh_9_10_comboBox.blockSignals(True)
                self.sdiOutCh_9_10_comboBox.setCurrentIndex(args["SDIOutChannel_9_10"]["format"])
                self.sdiOutCh_9_10_comboBox.blockSignals(False)

                self.sdiOutCh_11_12_comboBox.blockSignals(True)
                self.sdiOutCh_11_12_comboBox.setCurrentIndex(args["SDIOutChannel_11_12"]["format"])
                self.sdiOutCh_11_12_comboBox.blockSignals(False)

                self.sdiOutCh_13_14_comboBox.blockSignals(True)
                self.sdiOutCh_13_14_comboBox.setCurrentIndex(args["SDIOutChannel_13_14"]["format"])
                self.sdiOutCh_13_14_comboBox.blockSignals(False)

                self.sdiOutCh_15_16_comboBox.blockSignals(True)
                self.sdiOutCh_15_16_comboBox.setCurrentIndex(args["SDIOutChannel_15_16"]["format"])
                self.sdiOutCh_15_16_comboBox.blockSignals(False)

                self.analog_audio_comboBox.blockSignals(True)
                self.analog_audio_comboBox.setCurrentIndex(args["Analog_audio_out"]["format"])
                self.analog_audio_comboBox.blockSignals(False)

                self.tpg_audio_comboBox.blockSignals(True)
                self.tpg_audio_comboBox.setCurrentIndex(args["TPG_Audio_test"]["format"])
                self.tpg_audio_comboBox.blockSignals(False)

            except Exception as e:
                logging.error("Update output audio error!")


        elif obj["function"] == "set_audio_params":
            args = obj["args"]
            logging.debug("Get volume args:{}".format(args))


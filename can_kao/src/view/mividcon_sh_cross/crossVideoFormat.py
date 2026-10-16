import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox, QFileDialog, QDialog, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSignalBlocker, Qt, Signal, QCoreApplication
from src.ui.mividcon_sh_cross.cross_videoFormat_ui import Ui_Cross_Video_Format_Form
from src.model.modelPreferences import ModelPreferences
from src.model.mividcon_sh_cross.CrossPreferences import CrossPreferences
from globals import relative_path, global_qss

class CrossVideoFormat(Ui_Cross_Video_Format_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.need_reshow = True # 翻译后需要重新显示相关文本
        self.setupUi(self)

        self.outputFormat_comboBox.addItems(CrossPreferences._output_formats)
        self.hdmiColorSpace_comboBox.addItems(CrossPreferences._color_spaces)
        self.sdiImageFlip_comboBox.addItems(CrossPreferences._image_flip_modes)
        self.hdmiImageFlip_comboBox.addItems(CrossPreferences._image_flip_modes)
        self.SD2SD_aspect_comboBox.addItems(CrossPreferences._sd2sd_aspects)
        self.SD2HD_aspect_comboBox.addItems(CrossPreferences._sd2hd_aspects)
        self.HD2SD_aspect_comboBox.addItems(CrossPreferences._hd2sd_aspects)
        self.HD2HD_aspect_comboBox.addItems(CrossPreferences._hd2hd_aspects)
        self.pattern_combox.addItems(CrossPreferences._pattens)
        self.sdiOutputFormat_comboBox.addItems(CrossPreferences._sdi_out_level_modes)
        self.sdiImageFlip_combox.addItems(CrossPreferences._tpg_ops)
        self.deinterlace__comboBox.addItems(CrossPreferences._deinterlaces)
        self.i2psfMode_comboBox.addItems(["No", "Yes"])

        self.sdiOutputFormat_comboBox.currentIndexChanged.connect(self._on_sdiOutputFormat_index_changed)
        self.outputFormat_comboBox.currentIndexChanged.connect(self._on_output_format_index_changed)
        self.hdmiColorSpace_comboBox.currentIndexChanged.connect(self._on_hdmi_color_space_index_changed)
        self.SD2SD_aspect_comboBox.currentIndexChanged.connect(self._on_sd2sd_aspect_index_changed)
        self.SD2HD_aspect_comboBox.currentIndexChanged.connect(self._on_sd2hd_aspect_index_changed)  # 新增
        self.HD2SD_aspect_comboBox.currentIndexChanged.connect(self._on_hd2sd_aspect_index_changed)  # 新增
        self.HD2HD_aspect_comboBox.currentIndexChanged.connect(self._on_hd2hd_aspect_index_changed)  # 新增
        self.pattern_combox.currentIndexChanged.connect(self._on_pattern_index_changed)   # 新增
        self.sdiImageFlip_comboBox.currentIndexChanged.connect(self._on_sdi_image_flip_index_changed)
        self.hdmiImageFlip_comboBox.currentIndexChanged.connect(self._on_hdmi_image_flip_index_changed)
        self.sdiImageFlip_combox.currentIndexChanged.connect(self._on_tgp_op_index_changed)  # 新增
        self.deinterlace__comboBox.currentIndexChanged.connect(self._on_deinterlace_index_changed)
        self.i2psfMode_comboBox.currentIndexChanged.connect(self._on_i2psfMode_index_changed)


    def _on_sdiOutputFormat_index_changed(self,index):
        _args = {
            "SDIOutLevelMode": CrossPreferences.get_sdi_out_level_mode_by_index(index)
        }

        self._parent.controller.set_video_format_params(_args)

    def _on_i2psfMode_index_changed(self, index):
        logging.debug(f"_on_i2psfMode_index_changed: result={index}")
        _args = {
            "IsPsf": index == 1
        }
        self._parent.controller.set_video_format_params(_args)
    def _on_deinterlace_index_changed(self, index):
        logging.debug(f"_on_deinterlace_index_changed: index={index}")
        _args = {
            "Deinterlace": CrossPreferences.get_deinterlaces_by_index(index)
        }
        self._parent.controller.set_video_format_params(_args)

    def _on_tgp_op_index_changed(self, index):
        logging.debug(f"_on_tgp_op_index_changed: index={index}")
        _args = {
            "TGP": CrossPreferences.get_tpgop_by_index(index)
        }
        self._parent.controller.set_video_format_params(_args)

    def _on_sd2hd_aspect_index_changed(self, index):
        _args = {
            "SD2HDAspect": CrossPreferences.get_sd2hd_aspect_by_index(index)
        }
        logging.debug(f"_on_sd2hd_aspect_index_changed: _args={_args}")
        self._parent.controller.set_video_format_params(_args)

    def _on_hd2sd_aspect_index_changed(self, index):
        _args = {
            "HD2SDAspect": CrossPreferences.get_hd2sd_aspect_by_index(index)
        }
        logging.debug(f"_on_hd2sd_aspect_index_changed: _args={_args}")
        self._parent.controller.set_video_format_params(_args)

    def _on_hd2hd_aspect_index_changed(self, index):
        _args = {
            "HD2HDAspect": CrossPreferences.get_hd2hd_aspect_by_index(index)
        }
        logging.debug(f"_on_hd2hd_aspect_index_changed: _args={_args}")
        self._parent.controller.set_video_format_params(_args)

    def _on_pattern_index_changed(self, index):
        _args = {
            "Pattern": CrossPreferences.get_pattens_by_index(index)
        }
        logging.debug(f"_on_pattern_index_changed: _args={_args}")
        self._parent.controller.set_video_format_params(_args)

    def _on_deinterlace_buttonGroup_clicked(self, index):
        logging.debug(f"Deinterlace_clicked: index={index}")
        _args = {
            "Deinterlace": CrossPreferences.get_deinterlaces_by_index(index)
        }
        self._parent.controller.set_video_format_params(_args)

    def _on_tgp_op_buttonGroup_clicked(self, index):
        logging.debug(f"_on_tgp_op_buttonGroup_clicked: index={index}")
        _args = {
            "TGP": CrossPreferences.get_tpgop_by_index(index)
        }
        self._parent.controller.set_video_format_params(_args)

    def _on_sdiOutputFormat_levelMode_buttonGroup_clicked(self, index):
        logging.debug(f"_on_sdiOutputFormat_levelMode_buttonGroup_clicked: index={index}")
        _args = {
            "SDIOutLevelMode": CrossPreferences.get_sdi_out_level_mode_by_index(index)
        }
        self._parent.controller.set_video_format_params(_args)

    def _on_i2psfMode_buttonGroup_clicked(self, result):
        logging.debug(f"_on_i2psfMode_buttonGroup_clicked: result={result}")
        _args = {
            "IsPsf": result
        }
        self._parent.controller.set_video_format_params(_args)

    def _on_output_format_index_changed(self, index):
        _args = {
            "OutputFormat":  CrossPreferences.get_output_format_by_index(index)
        }
        logging.debug(f"_on_output_format_index_changed: _args={_args}")
        self._parent.controller.set_video_format_params(_args)

    def _on_hdmi_color_space_index_changed(self, index):
        _args = {
            "HDMIColorSpace":  CrossPreferences.get_color_space_by_index(index)
        }
        logging.debug(f"_on_hdmi_color_space_index_changed: _args={_args}")
        self._parent.controller.set_video_format_params(_args)

    def _on_sd2sd_aspect_index_changed(self, index):
        _args = {
            "SD2SDAspect":  CrossPreferences.get_sd2sd_aspect_by_index(index)
        }
        logging.debug(f"_on_sd2sd_aspect_index_changed: _args={_args}")
        self._parent.controller.set_video_format_params(_args)
    
    def _on_sdi_image_flip_index_changed(self, index):
        _args = {
            "SDIImageFlip":  CrossPreferences.get_image_flip_mode_by_index(index)
        }
        logging.debug(f"_on_sdi_image_flip_index_changed: _args={_args}")
        self._parent.controller.set_video_format_params(_args)

    def _on_hdmi_image_flip_index_changed(self, index):
        _args = {
            "HDMIImageFlip":  CrossPreferences.get_image_flip_mode_by_index(index)
        }
        logging.debug(f"_on_hdmi_image_flip_index_changed: _args={_args}")
        self._parent.controller.set_video_format_params(_args)

    def showEvent(self, event):
        self._parent.controller.get_output_video_format_params()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def  translateList(self):
        self.outputFormat_comboBox.blockSignals(True)
        self.hdmiColorSpace_comboBox.blockSignals(True)
        self.sdiOutputFormat_comboBox.blockSignals(True)
        self.SD2SD_aspect_comboBox.blockSignals(True)
        self.i2psfMode_comboBox.blockSignals(True)
        self.sdiImageFlip_comboBox.blockSignals(True)
        self.hdmiImageFlip_comboBox.blockSignals(True)
        self.SD2HD_aspect_comboBox.blockSignals(True)
        self.HD2SD_aspect_comboBox.blockSignals(True)
        self.HD2HD_aspect_comboBox.blockSignals(True)
        self.deinterlace__comboBox.blockSignals(True)
        self.pattern_combox.blockSignals(True)
        self.sdiImageFlip_combox.blockSignals(True)

        # self.pattern_combox.clear()
        # self.pattern_combox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
        #         for item in CrossPreferences._pattens)

        self.deinterlace__comboBox.clear()
        self.deinterlace__comboBox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
                for item in CrossPreferences._deinterlaces)

        self.i2psfMode_comboBox.clear()
        self.i2psfMode_comboBox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
                for item in ["No", "Yes"])

        self.sdiImageFlip_comboBox.clear()
        self.sdiImageFlip_comboBox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
                for item in CrossPreferences._image_flip_modes)

        self.hdmiImageFlip_comboBox.clear()
        self.hdmiImageFlip_comboBox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
                                            for item in CrossPreferences._image_flip_modes)

        self.sdiImageFlip_combox.clear()
        self.sdiImageFlip_combox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
                                            for item in CrossPreferences._tpg_ops)

        self.SD2SD_aspect_comboBox.clear()
        self.SD2SD_aspect_comboBox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
                                            for item in CrossPreferences._sd2sd_aspects)
        self.SD2HD_aspect_comboBox.clear()
        self.SD2HD_aspect_comboBox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
                                            for item in CrossPreferences._sd2hd_aspects)

        self.HD2SD_aspect_comboBox.clear()
        self.HD2SD_aspect_comboBox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
                                            for item in CrossPreferences._hd2sd_aspects)

        self.HD2HD_aspect_comboBox.clear()
        self.HD2HD_aspect_comboBox.addItems(QCoreApplication.translate("Cross_Video_Format_Form", item, None)
                                            for item in CrossPreferences._hd2hd_aspects)

    def handle_async_callback(self, obj):

        if obj["function"] == "get_output_video_format_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))
            self.translateList()
            try:
                # self.outputFormat_comboBox.blockSignals(True)
                # self.hdmiColorSpace_comboBox.blockSignals(True)
                # self.sdiOutputFormat_comboBox.blockSignals(True)
                # self.SD2SD_aspect_comboBox.blockSignals(True)
                # self.i2psfMode_comboBox.blockSignals(True)
                # self.sdiImageFlip_comboBox.blockSignals(True)
                # self.hdmiImageFlip_comboBox.blockSignals(True)
                # self.SD2HD_aspect_comboBox.blockSignals(True)
                # self.HD2SD_aspect_comboBox.blockSignals(True)
                # self.HD2HD_aspect_comboBox.blockSignals(True)
                # self.deinterlace__comboBox.blockSignals(True)
                # self.pattern_combox.blockSignals(True)
                # self.sdiImageFlip_combox.blockSignals(True)

                self.outputFormat_comboBox.setCurrentIndex(args["Output"]["format"])
                self.hdmiColorSpace_comboBox.setCurrentIndex(args["HDMI"]["colorSpace"])
                self.sdiOutputFormat_comboBox.setCurrentIndex(args["3G-SDIOut"]["levelMode"])
                self.SD2SD_aspect_comboBox.setCurrentIndex(args["SD2SD ASPECT"]["aspect"])
                self.i2psfMode_comboBox.setCurrentIndex(args["1080i=1080psf"]["isPsf"])
                self.sdiImageFlip_comboBox.setCurrentIndex(args["SDIImage"]["flipMode"])
                self.hdmiImageFlip_comboBox.setCurrentIndex(args["HDMIImage"]["flipMode"])
                self.SD2HD_aspect_comboBox.setCurrentIndex(args["SD2HD ASPECT"]["aspect"])
                self.HD2SD_aspect_comboBox.setCurrentIndex(args["HD2SD ASPECT"]["aspect"])
                self.HD2HD_aspect_comboBox.setCurrentIndex(args["HD2HD ASPECT"]["aspect"])
                self.deinterlace__comboBox.setCurrentIndex(args["Deinterlace Mode"]["mode"])
                self.pattern_combox.setCurrentIndex(args["Pattern"]["aspect"])
                self.sdiImageFlip_combox.setCurrentIndex(args["TPG OP"]["mode"])


                self.hdmiColorSpace_comboBox.blockSignals(False)
                self.sdiOutputFormat_comboBox.blockSignals(False)
                self.SD2SD_aspect_comboBox.blockSignals(False)
                self.i2psfMode_comboBox.blockSignals(False)
                self.sdiImageFlip_comboBox.blockSignals(False)
                self.hdmiImageFlip_comboBox.blockSignals(False)
                self.sdiImageFlip_combox.blockSignals(False)
                self.outputFormat_comboBox.blockSignals(False)
                self.pattern_combox.blockSignals(False)
                self.deinterlace__comboBox.blockSignals(False)
                self.HD2HD_aspect_comboBox.blockSignals(False)
                self.HD2SD_aspect_comboBox.blockSignals(False)
                self.SD2HD_aspect_comboBox.blockSignals(False)


            except Exception as e:
                logging.error("Update output video format error!")
            
        elif obj["function"] == "set_video_format_params":
            args = obj["args"]
            logging.debug("Set video format args:{}".format(args))

           
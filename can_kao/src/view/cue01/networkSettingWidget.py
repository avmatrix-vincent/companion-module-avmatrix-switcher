
import os, sys, re, logging
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from src.ui.cue01.networkSettingWidget_ui import Ui_CUE01_Network_Setting_Widget_Form

class NetworkSettingWidget(Ui_CUE01_Network_Setting_Widget_Form, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.setupUi(self)
        
    def init_ui(self):
        self._network_value = {
            "DHCPSwitchButton": self.widget_hcp_switchbtn,
            "IPAddressLineEdit": self.clearableLineEdit_ip.line_edit,
            "SubnetMaskLineEdit": self.clearableLineEdit_mask.line_edit,
            "GatewayLineEdit": self.clearableLineEdit_gateway.line_edit
        }

        self.pushButton_save.clicked.connect(self._save_network_setting)
        self.widget_hcp_switchbtn.checkedChanged.connect(self._save_network_setting)


    def _is_valid_ipv4_address(self, address):  
        # pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"  
        pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        return bool(re.match(pattern, address)) 
    
    def _is_valid_subnet_mask(self, mask):  
        parts = mask.split(".")  
        if len(parts) != 4:  
            return False  
        
        mask_int = 0  
        for part in parts:  
            if not part.isdigit() or int(part) < 0 or int(part) > 255:  
                return False  
            mask_int = (mask_int << 8) + int(part)  
        
        # 检查是否连续的1后跟着连续的0  
        binary_str = bin(mask_int)[2:].zfill(32)  
        return all(binary_str[i] >= binary_str[i+1] for i in range(31)) 

    # def _switch_dhcp_status(self, checked)

    def _set_network_manual_setting_disable(self, disable):
        self._network_value["IPAddressLineEdit"].setEnabled(disable)
        self._network_value["SubnetMaskLineEdit"].setEnabled(disable)
        self._network_value["GatewayLineEdit"].setEnabled(disable)

    def _save_network_setting(self, checked=False):
        _checked = checked
        if not checked: # 通过点击save按钮，保持当前hcp状态
            _checked = self.widget_hcp_switchbtn.checked
        
        self._set_network_manual_setting_disable(not _checked)
        _ip_address = self._network_value["IPAddressLineEdit"].text()
        _subnet_mask = self._network_value["SubnetMaskLineEdit"].text()
        _gateway = self._network_value["GatewayLineEdit"].text()

        if not self._is_valid_ipv4_address(_ip_address):
            QMessageBox.critical(None, "Network Error", "IP Address Error")
            return
        
        if not self._is_valid_subnet_mask(_subnet_mask):
            QMessageBox.critical(None, "Network Error", "Subnet Mask Error")
            return

        if not self._is_valid_ipv4_address(_gateway):
            QMessageBox.critical(None, "Network Error", "Gateway Error")
            return

        logging.debug("Set network: ip({}), subnet mask({}), gateway({})".format(_ip_address, _subnet_mask, _gateway))
        # QMessageBox.information(None, "Network Setting", "The network settings function will be supported in the future!")
        _args = {
            "checked": _checked,
            "ip_address": [int(num) for num in _ip_address.split(".")],
            "subnet_mask": [int(num) for num in _subnet_mask.split(".")],
            "gateway": [int(num) for num in _gateway.split(".")]
        }
        self._parent.controller.set_network_setting(_args)

    def showEvent(self, event):
        self._parent.controller.get_system()
        super().showEvent(event)  # 调用基类的 showEvent 方法

    def handle_async_callback(self, obj):
        if obj["function"] == "get_system_params":
            args = obj["args"]
            logging.debug("args:{}".format(args))

            _dhcp_switch = args["DHCP"]
            _ip_address = args["IPAddress"]
            _subnet_mask = args["SubnetMask"]
            _gateway = args["Gateway"]

            # if _dhcp_switch == "On" or _dhcp_switch == "ON":
            if _dhcp_switch:
                self._network_value["DHCPSwitchButton"].set_checked(True)
            else:
                self._network_value["DHCPSwitchButton"].set_checked(False)

            self._network_value["IPAddressLineEdit"].setText(_ip_address)
            self._network_value["SubnetMaskLineEdit"].setText(_subnet_mask)
            self._network_value["GatewayLineEdit"].setText(_gateway)

            self._set_network_manual_setting_disable(not _dhcp_switch)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("res/theme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = NetworkSettingWidget()
    window.show()
    sys.exit(app.exec())
    
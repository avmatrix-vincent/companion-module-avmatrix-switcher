import sys
import logging
import random
import threading
import traceback
from src.avm_stack.usb_stack.packet.parser import Parser
if sys.platform.startswith('darwin'):
    from src.avm_stack.usb_stack.phy.udevice_mac import UDevice
else:
    from src.avm_stack.usb_stack.phy.udevice import UDevice
from src.avm_stack.usb_stack.transport.core import TransCore
from src.avm_stack.usb_stack.server.common import ComServer
from src.model.modelPreferences import ModelPreferences

class UsbCCP():
    
    def __init__(self):
        self._index = 0
        self._unknow_sn_index = 0 # 未知设备的sn索引
        self._devs = []
        self._phy = UDevice()
        self._transport = TransCore(self._phy)
        self._comserver = ComServer(self._transport)
        self._dev_lock = threading.Lock()
        self._app_cbs = []
        self._cbs_lock = threading.Lock()
        self._invalid_dev_sns = [] # 曾经连接但已不在当前网段且未删除的设备sn列表

    def start_scan(self):
        logging.debug("start usb scan")
        
        if len(self._devs) > 0: # 如果之前添加过设备，将设备sn填入临时列表中
            with self._dev_lock:
                self._invalid_dev_sns.clear()
                for dev in self._devs:
                    self._invalid_dev_sns.append(dev["sn"])

        new_devs = self.scan()
        if new_devs is not None:
            for new_dev_dict in new_devs:
                self.add_device(new_dev_dict)
        self.check_invalid_devs()

    def check_invalid_devs(self):
        if len(self._invalid_dev_sns) == 0: return
        for sn in self._invalid_dev_sns:
            args = {
                    "type": "scanner",
                    "action": "disconnected",
                    "args": {
                        "sn": sn
                        }
                    }
            logging.debug("args: {}".format(args))
            # 通知上层，扫描的状态更新
            if self._device_status_listener is not None:
                self._device_status_listener(args) # 上报主界面删除设备

    def scan(self):
        try:
            devlist = self._phy.scan()
            logging.info("Scan device list:")
            logging.info(devlist)
            return devlist
        except BaseException as error:
            logging.error(traceback.format_exc())

        return None

    def __get_device_name_callback(self, dev_sn, args):
        dev_dict = self.__find_dev_dict_by_sn(dev_sn)
        if dev_dict is None:
            logging.error("USB CCP: 未找到SN为" + dev_sn + "的device")
            return False

        logging.debug(f"args: {args}")

        if all(args[8 + i] != 0 for i in range(3)): # 开头的3个字符不为零，即判断设备名称有效
            dev_dict["name"] = bytes(args[8:32]).decode("UTF-8").rstrip('\x00')
            dev_dict["canModifyName"] = True

        _args = {
            "type": "device",
            "action": "new",
            "args": dev_dict
        }

        logging.debug("Report new device: {}".format(_args))
        if self._device_status_listener is not None:
            self._device_status_listener(_args)

    def add_device(self, devinfo_dict):
        if not devinfo_dict: return
        logging.debug("usb devinfo_dict: {}".format(devinfo_dict))
        if not devinfo_dict["sn"]:
            sn = "unknown sn " + str(self._unknow_sn_index)
            self._unknow_sn_index += 1

        sn = devinfo_dict["sn"]
        if sn in self._invalid_dev_sns:
            self._invalid_dev_sns.remove(sn)

        _args = {
            "interface": "USB",
            "manufacturer": devinfo_dict["manufacturer"],
            "model": devinfo_dict["product"],
            "sn": sn,
            "name": devinfo_dict["product"],
            "canModifyName": False,
            "activated": False   # 设备是否激活  2025-11-12
        }
        self._dev_lock.acquire()
        is_exist = next((d for d in self._devs if d['sn'] == sn), None)
        # print(">>>>>>>>>>>", is_exist)
        if not is_exist:
            logging.debug("New device: {}".format(_args))
            self._devs.append(_args)
            # 通知上层，设备状态有改变
            # if self._device_status_listener is not None:
            #     self._device_status_listener(_args)
            self._dev_lock.release()

            # 获取设备名称，该名称允许用户修改，拿到设备名称后再上报新设备
            _cmd = 0x1A
            _data = []

            self.async_action(sn, _cmd, _data, self.__get_device_name_callback)
        else:
            self._dev_lock.release()

    def delete_device(self, sn):
        logging.debug("sn: {}".format(sn))
        self._dev_lock.acquire()
        for d in self._devs:
            if d['sn'] == sn:
                self._devs.remove(d)
                break
        self._dev_lock.release()
        logging.debug(f"删除后，列表={self._devs}")

    def set_device_status_listener(self, device_status_listener):
        self._device_status_listener = device_status_listener

    def set_device_heartbeat_listener(self, heartbeat_listener):
        self._heartbeat_listener = heartbeat_listener

    def get_device_info_list(self):
        return self._devs
        # dev_info_list = []
        
        # self._dev_lock.acquire()

        # for dev in self._devs:
        #     dev_info = {
        #         "sn": dev['sn']
        #     }
        #     dev_info_list.append(dev_info)

        # self._dev_lock.release()

        # logging.debug("usb dev_info_list: {}".format(dev_info_list))
        # return dev_info_list

    def connect(self, devinfo_dict):
        try:
            logging.info("Connect device information:")
            logging.info(devinfo_dict)
            #self._phy.disconnect()  ###########
            ret = self._phy.connect(devinfo_dict)
            return ret
        except BaseException as error:
            logging.error(traceback.format_exc())

        return False

    def disconnect(self):
        try:
            logging.info("Disconnect device")
            self._phy.disconnect()
            return True
        except BaseException as error:
            logging.error(traceback.format_exc())

        return False

    def get_device_infor(self):
        try:
            devinfo = self._comserver.get_device_infor()

            logging.info("Device detail:")
            logging.info(f"\n{devinfo}")
            return devinfo
        except BaseException as error:
            logging.error(traceback.format_exc())

        return None

    def get_configure_chips(self):
        try:
            chip_list = self._comserver.get_configure_chips()

            logging.info("Configure chips:")
            logging.info(chip_list)
            return chip_list
        except BaseException as error:
            logging.error(traceback.format_exc())

        return None

    def __find_dev_dict_by_sn(self, dev_sn):
        self._dev_lock.acquire()
        dev_dict = next((d for d in self._devs if d['sn'] == dev_sn), None)
        self._dev_lock.release()
        return dev_dict

    def __prepare_do_action(self, cmd, callback):
        self._index += 1
        session = random.randint(0, 100000000)
        byte_session = session.to_bytes(4, "little")
        # logging.debug("send session:{}".format(session))
        # logging.debug("byte_session:{}".format(byte_session))

        self._cbs_lock.acquire()
        for _cb in self._app_cbs:
            if _cb["session"] == byte_session and _cb["cmd"] == cmd:
                self._cbs_lock.release()
                return False, 0

        _cb = {
            "session": session,
            "cmd": cmd,
            "function": callback
        }

        self._app_cbs.append(_cb)
        self._cbs_lock.release()

        return True, byte_session

    def async_action(self, dev_sn, cmd, data:list, callback):
        # 先根据device sn找到对应的device
        dev_dict = self.__find_dev_dict_by_sn(dev_sn)
        if dev_dict is None:
            logging.error("USB CCP: 未找到SN为" + dev_sn + "的device")
            return False

        # 检查设备是否已激活，未激活的设备不进行通信  2025-11-12
        # if not dev_dict.get("activated", False):
        #     logging.info("设备 {} 未激活，不进行通信".format(dev_sn))
        #     return False

        #self.disconnect()
        self.connect(dev_dict)
        # 再生成随机的session，并把cmd、callback，与session一起存入回调列表中，等待回应报文的处理
        ret, session = self.__prepare_do_action(cmd, callback)
        if ret:
            new_data = []
            new_data += session
            # new_data += dev_id.to_bytes(1, "little")
            new_data += data
            logging.debug(f"Ready action data: {new_data}, cmd = {cmd:#x}")
            r = self._transport.send_paging_data(self._index, cmd, new_data, len(new_data), timeout=2000)
            if r:
                logging.debug("UsbCCP: 发送action成功")
                if self._heartbeat_listener is not None:
                    self._heartbeat_listener(dev_sn, "reset") # 通知上层，心跳重新计时
                ret, t = self._transport.receive(timeout=4000)
                # logging.debug(f"t: {t}")
                # logging.debug(f"ret:{ret}")
                while ret:
                    ret, t0 = self._transport.receive(timeout=100)
                    # logging.debug(f"t0: {t0}")
                    
                    if ret:
                        t = t + t0

                    if not ret:
                        logging.debug(f"received row data: {t}")
                        self.receive_handle(dev_sn, t)
            else:
                logging.error("Write register with mask error: send data error")
                return False
            return True
        else:
            return False

    def receive_handle(self, dev_sn, t):
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # print(args['data'].decode('utf-8'))
        # import binascii
        # print(binascii.hexlify(args['data']).decode('utf-8'))
        _cb_func = None

        # 收到回应报文，查找同样session和cmd的回调函数，取出后进行回调
        self._cbs_lock.acquire()
        magic_number = int.from_bytes(t[0:4], byteorder='little')
        response_session = int.from_bytes(t[4:8], byteorder='little')
        # dev_id = int.from_bytes(t[8], byteorder='little')
        # dev_id = t[8]
        # logging.debug(f"magic_number:{magic_number}")
        # logging.debug(f"response_session:{response_session}")
        # logging.debug(f"Parser's magic number:{Parser.get_magic_number()}")
        for _cb in self._app_cbs:
            if magic_number == Parser.get_magic_number() and _cb["session"] == response_session:
                _cb_func = _cb["function"]
                self._app_cbs.remove(_cb)
        self._cbs_lock.release()

        if _cb_func is not None:
            _cb_func(dev_sn, t)


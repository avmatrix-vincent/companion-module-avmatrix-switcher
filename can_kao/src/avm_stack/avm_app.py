import logging
from globals import extract_leading_numbers

# from src.avm_stack.udp_stack.avm_ccp import AvmCCP
from src.avm_stack.udp_stack.avm_ccp import AvmCCP
from src.avm_stack.usb_stack.usb_ccp import UsbCCP
from src.avm_stack.avm_notice import AvmNotice
from src.avm_stack.lib_rtice.rtice_ccp import RticeCCP
from src.model.modelPreferences import ModelPreferences

class AvmApp(object):
    """
    主应用程序类，负责管理设备和模型
    """
    def __init__(self, notice:AvmNotice) -> None:
        """
        初始化应用程序，设置版本号和各种监听器
        """
        self._version = "V1.2.3"
        self._udp_ccp = AvmCCP()
        self._notice = notice
        self._udp_ccp.set_device_status_listener(self.__handle_ccp_device_status)
        self._udp_ccp.set_device_heartbeat_listener(self.__handle_device_heartbeat_status)
        self._udp_ccp.set_report_listener(self.__handle_ccp_report)
        self._usb_ccp = UsbCCP()
        self._usb_ccp.set_device_status_listener(self.__handle_ccp_device_status)
        self._usb_ccp.set_device_heartbeat_listener(self.__handle_device_heartbeat_status)
        self._rtice_ccp = RticeCCP()

        self._model_obj_table = []
        self._sn_model = {}

    """
    _model_obj_table: [
        {
            "name": "xxx1-model",
            "object": xxx1Model,
        },{
            "name": "xxx2-model",
            "object": xxx3Model
        }
    ]
    """
    def register_model_class(self, model_class_table):
        if len(self._model_obj_table) == 0:
            try:
                for _table in model_class_table:
                    _model_obj = {
                        "models": _table["models"],
                        "object": _table["class"](self)
                    }
                    self._model_obj_table.append(_model_obj)
            except Exception as e:
                logging.error("Register model class to app error!")
                return
            
            logging.info("Register model class to app success!")
        else:
            logging.error("Can't register model class to app error!")

    def register_model(self, dev_sn, model_name):
        for _table in self._model_obj_table:
            for _model in _table["models"]:
                if model_name.startswith(_model):
                    _model_obj = _table["object"]
                    self._sn_model[dev_sn] = _model_obj
                    return _model_obj
        
        return None

    def __handle_ccp_device_status(self, args):
        """
        处理CCP设备状态上报
        """
        _args = {
            "message_type": args["type"],
            "message": args
        }
        self._notice.dispatch(_args)

    def __handle_ccp_report(self, dev_sn, cmd, data):
        """
        处理CCP报告，解析协议数据并交给对应模型处理
        """
        if dev_sn in self._sn_model:
            model = self._sn_model[dev_sn]
            model.handle_ccp_report(dev_sn, cmd, data)

    def __handle_device_heartbeat_status(self, dev_sn, status:str):
        """
        处理设备心跳状态
        """
        message_type = "update_heartbeat_status"
        action = ""
        if status == "reset":
            action = "heartbeat_reset"
        elif status == "stop":
            action = "heartbeat_stop"
        elif status == "received":
            action = "heartbeat_received"
        elif status == "disable": # 设备能扫描到，但是不可控，如SC7030拨码未打开
            action = "Device_Disable"
        _args = {
            "message_type": message_type,
            "message": {
                "action": action,
                "sn": dev_sn
                }
        }
        self._notice.dispatch(_args)

    def handle_model_report(self, dev_sn, args):
        """
        处理模型报告
        """
        _args = {
            "message_type": "device.{}.report".format(dev_sn),
            "message": args
        }
        self._notice.dispatch(_args)

    def start_scan(self):
        """
        启动扫描
        """
        logging.debug("start scan")
        self._usb_ccp.start_scan()
        self._udp_ccp.start_scan()

    def stop_scan(self):
        """
        停止扫描
        """
        logging.debug("stop scan")
        self._udp_ccp.stop_scan()

    def delete_device(self, dev_sn, interface):
        """
        删除设备
        """
        logging.debug(f"delete device with sn:{dev_sn} on interface: {interface}")
        if interface == "Ethernet":
            self._udp_ccp.delete_device(dev_sn)
        elif interface == "USB":
            self._usb_ccp.delete_device(dev_sn)

    def get_device_info_list(self):
        """
        获取设备信息列表
        """
        return self._udp_ccp.get_device_info_list() + self._usb_ccp.get_device_info_list()

    def async_callback(self, dev_sn, args):
        """
        处理模型回调函数
        """
        _args = {
            "message_type": "device.{}.cb".format(dev_sn),
            "message": args
        }
        self._notice.dispatch(_args)

    def async_action(self, dev_sn, cmd, data:list, callback):
        """
        异步操作
        """
        self._udp_ccp.async_action(dev_sn, cmd, data, callback)

    def async_action_usb(self, dev_sn, cmd, data:list, callback):
        """
        USB异步操作
        """
        self._usb_ccp.async_action(dev_sn, cmd, data, callback)

    def send_heartbeat_packet(self, args):
        """
        发送心跳包
        """
        _sn = args["sn"]
        _model = args["model"]
        _interface = args["interface"]
        logging.debug(f"Send Heartbeat ===> SN: {_sn}, Model: {_model}, interface: {_interface}")
        # udp
        if _interface == "Ethernet":
            _device_type = ModelPreferences.get_udp_model_index(_model)
            _mac = args["mac"]
            self._udp_ccp.send_heartbeat_instruction(_sn, _device_type, _mac)
            return
        # usb
        elif _interface == "USB":
            # self.__handle_device_heartbeat_status(_sn, "received")
            # return # 暂时取消对USB设备的心跳包发送
            
            device_info = self._usb_ccp.get_device_infor()
            if device_info is None:
                logging.warning(">>> USB HeartBeat查询未回复")
                return
            self.__handle_device_heartbeat_status(_sn, "received")
            if not device_info.get_control_status(): # 设备不可控
                logging.warning(">>> USB HeartBeat查询到设备不可控")
                self.__handle_device_heartbeat_status(_sn, "disable")

    def async_action_rtice(self, dev_sn, func, args, callback):
        return self._rtice_ccp.async_action(dev_sn, func, args, callback)

    # 该命令本不该在此处进行数据解析，应该需要一个通用的model来处理
    # 临时先放在此处处理
    def rename_device(self, args, callback):
        _sn = args["sn"]
        _name = args["name"]
        _interface = args["interface"]
        
        if _interface == "Ethernet":
            _cmd = 0xBB00
            _length = 24
            _data = (_name.encode() + b'\0' * (_length - len(_name)))[:_length]
            # logging.error(f"_data:{_data}")
            self._udp_ccp.async_action(_sn, _cmd, _data, callback)
        elif _interface == "USB":
            _cmd = 0x19
            _length = 24
            _data = (_name.encode() + b'\0' * (_length - len(_name)))[:_length]
            # logging.error(f"_data:{_data}")
            self._usb_ccp.async_action(_sn, _cmd, _data, callback)
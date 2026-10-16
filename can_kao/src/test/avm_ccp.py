import logging
import random
from _thread import *
import threading
import socket
import traceback
from src.avm_stack.udp_stack.avm_phy import AvmPhy, AvmScannerPhy
# from src.avm_stack.CommandBatcher import CommandBatcher
# from src.avm_stack.BatchCMDHandler import CommandBatcher
# from src.avm_stack.command_batcher import CommandBatcherThread
from src.model.modelPreferences import ModelPreferences
from globals import FILTER_CMD_LIST

class AvmCCP(object):
    """
    报文打包与解析需要用到的工具
    """
    class Util(object):
        @staticmethod
        def calc_sum(data, num):
            sum = 0

            for i in range(num):
                sum += data[i]

            sum = 0xffff & sum
            return sum.to_bytes(2, "big")

    """
    报文头的参数定义
    """
    class Header(object):
        _head = [0xA5, 0x5A]
        _version = 0x0100
        _padding = [0x00] * 8
        _data_max_len = 512
        _tail = [0xA6, 0x6A]
        _cmd_type = 0x00     # 0x00: Host CMD to Client
        _resp_type = 0x01    # 0x01: Client response to Host
        _report_type = 0x02  # 0x02: Client report to Host

    """
    报文打包的类定义
    """
    class Packer(object):
        @staticmethod
        def command_data_packing(index, session, cmd, data, datalen):
            """
            :param index: 数据包序号
            :param cmd: 指令值
            :param data: 数据
            :param datalen: 数据长度
            :return: 返回封装好的报文
            """
            packet_data_len = 25 + datalen + 4
            packet = []
            packet += AvmCCP.Header._head
            packet += AvmCCP.Header._version.to_bytes(2, "big")
            packet += packet_data_len.to_bytes(2, "big")
            packet += index.to_bytes(2, "big")
            packet += AvmCCP.Header._padding
            packet += AvmCCP.Header._cmd_type.to_bytes(1, "big")
            packet += cmd.to_bytes(2, "big")
            packet += session.to_bytes(4, "big")
            packet += datalen.to_bytes(2, "big")
            packet += data
            packet += AvmCCP.Util.calc_sum(packet, packet_data_len - 4)
            packet += AvmCCP.Header._tail

            return packet

        @staticmethod
        def response_data_packing(index, session, cmd, data, datalen):
            """
            :param index: 数据包序号
            :param cmd: 指令值
            :param data: 数据
            :param datalen: 数据长度
            :return: 返回封装好的报文
            """
            packet_data_len = 25 + datalen + 4
            packet = []
            packet += AvmCCP.Header._head
            packet += AvmCCP.Header._version.to_bytes(2, "big")
            packet += packet_data_len.to_bytes(2, "big")
            packet += index.to_bytes(2, "big")
            packet += AvmCCP.Header._padding
            packet += AvmCCP.Header._resp_type.to_bytes(1, "big")
            packet += cmd.to_bytes(2, "big")
            packet += session.to_bytes(4, "big")
            packet += datalen.to_bytes(2, "big")
            packet += data
            packet += AvmCCP.Util.calc_sum(packet, packet_data_len - 4)
            packet += AvmCCP.Header._tail

            return packet

        @staticmethod
        def report_data_packing(index, data, datalen):
            """
            :param index: 数据包序号
            :param data: 数据
            :param datalen: 数据长度
            :return: 返回封装好的报文
            """
            packet_data_len = 25 + datalen + 4
        
            packet = []
            packet += AvmCCP.Header._head
            packet += AvmCCP.Header._version.to_bytes(2, "big")
            packet += packet_data_len.to_bytes(2, "big")
            packet += index.to_bytes(2, "big")
            packet += AvmCCP.Header._padding
            packet += AvmCCP.Header._report_type.to_bytes(1, "big")
            packet += ([0x00] * 2) # CMD
            packet += ([0x00] * 4) # session 
            packet += datalen.to_bytes(2, "big")
            packet += data
            packet += AvmCCP.Util.calc_sum(packet, packet_data_len - 4)
            packet += AvmCCP.Header._tail

            return packet

    """
    报文解析的类定义
    """
    class Parser(object):
        @staticmethod
        def packet_parser(packet):
            _packet_len = len(packet)
            if _packet_len < 29:
                raise ValueError("Packet's length is less than 29, length=%d" % _packet_len)

            #_head = packet[0:2]
            _version = int.from_bytes(packet[2:4], byteorder='big')
            _length = int.from_bytes(packet[4:6], byteorder='big')
            if _packet_len != _length:
                raise ValueError("Packet's length is not equal to _length, _packet_len=%d, _length=%d" % (_packet_len, _length))

            _index = int.from_bytes(packet[6:8], byteorder='big')
            #_padding = packet[8:16]
            _type = packet[16]
            _cmd = int.from_bytes(packet[17:19], byteorder='big')
            _session = int.from_bytes(packet[19:23], byteorder='big')
            _data_length = int.from_bytes(packet[23:25], byteorder='big')
            if _data_length != _length - 29:
                raise ValueError("Packet data's length is error, _data_length=%d" % (_data_length))

            _data = packet[25:25+_data_length]

            _sum = int.from_bytes(packet[25+_data_length:27+_data_length], byteorder='big')
            _check_sum = int.from_bytes(AvmCCP.Util.calc_sum(packet, _length - 4), byteorder='big')
            if _sum != _check_sum:
                raise ValueError("Check sum is error, _sum=0x%02X, _check_sum=0x%02X" % (_sum, _check_sum))

            #_tail = packet[27+_data_length:29+_data_length]

            _data_dict = {
                "version": _version,
                "index": _index,
                "type": _type,
                "session": _session,
                "cmd": _cmd,
                "data": _data
            }

            return _data_dict

        @staticmethod
        def mac_string_to_hex(mac_str):
            # 分割MAC地址字符串，以冒号作为分隔符
            mac_parts = mac_str.split(':')
            # 将每个分割后的部分从16进制字符串转换为整数
            mac_hex = [int(part, 16) for part in mac_parts]

            return mac_hex

    class Scanner(object):
        _MAX_TIMES = 4

        def __init__(self, ccp) -> None:
            self._target_ip = "255.255.255.255" # 组播地址
            self._target_port = 7000 # 组播端口
            self._phys = []
            self._ccp = ccp
            self._timer_counter = 0
            self._timer = None
            self.host_name = socket.gethostname()
            self.ip = socket.gethostbyname(self.host_name)

            self._create_netif_phy()

        # 需要为每个网络接口创建一个对应的Phy
        def _create_netif_phy(self):
             # 获取所有网络接口
            netifs = socket.getaddrinfo(self.host_name, None)
            for netif in netifs:
                # 为每一个IPv4的接口创建一个Phy
                if netif[0] == socket.AF_INET:
                    # addr格式为(family, type, proto, canonname, sockaddr)
                    ip_info = netif[4]
                    
                    _phy = AvmScannerPhy()
                    _phy.run(self._recv_handle, ip_info[0])
                    self._phys.append(_phy)

        # 给每个网络接口的Phy都发送广播数据
        def _send_packet_to_phy(self, packet):
            for _phy in self._phys:
                _phy.send(packet, (self._target_ip, self._target_port))

        def _recv_handle(self, args, addr):
            # logging.debug("Scanner _recv_handle args: {}".format(args))
            # logging.debug("Scanner _recv_handle addr: {}".format(addr))

            try:
                _data = AvmCCP.Parser.packet_parser(args)
                # print(">>>>>>>>>>>>>>>>>>>>> parsed_scanner_data:", _data)

                _product_type = _data["data"][22]

                _type = ModelPreferences.get_product_type_by_index(_product_type)

                _args = {
                    "type": "device",
                    "action": "new",
                    "args": {
                        "addr": addr,
                        "interface": "Ethernet",
                        "vendor": _data["data"][0:6].decode("ascii").rstrip('\x00'),
                        "productName": _data["data"][6:22].decode("ascii").rstrip('\x00'),
                        "type": _type,
                        "model": _data["data"][23:33].decode("ascii").rstrip('\x00'),
                        "deviceId": int.from_bytes(_data["data"][33:37], byteorder='big'),
                        "sn": _data["data"][37:45].decode("ascii").rstrip('\x00'),
                        "mac": "{:02X}:{:02X}:{:02X}:{:02X}:{:02X}:{:02X}".format(_data["data"][45], _data["data"][46], _data["data"][47], _data["data"][48], _data["data"][49], _data["data"][50]),
                        "protocolVer": "V{}.{}".format(_data["data"][51], _data["data"][52]),
                        "name": _data["data"][23:33].decode("ascii").rstrip('\x00')
                        # "name": _data["data"][23:33].decode("ascii").rstrip('\x00') + "-{:02X}{:02X}{:02X}".format(_data["data"][48], _data["data"][49], _data["data"][50])
                    }
                }

                if _args["args"]["sn"] == "":
                    _args["args"]["sn"] = "{:02X}{:02X}{:02X}{:02X}{:02X}{:02X}".format(_data["data"][45], _data["data"][46], _data["data"][47], _data["data"][48], _data["data"][49], _data["data"][50])

                self._ccp.add_device(_args)
            except Exception as e:
                logging.error("Drop this packet")
                logging.error(traceback.format_exc())

        def _gen_discover_packet(self):
            _index = 0x0001
            _session = 0x00000001
            _cmd = 0xFFFF
            _data = [0xFF] # 扫描所有的设备
            # _data = [0x01, 0x03] # 只扫描CUE01

            # 生成扫描的报文
            packet = AvmCCP.Packer.command_data_packing(_index, _session, _cmd, _data, len(_data))
            
            # import binascii 
            # print("扫描指令转换成16进制后：")
            # print(binascii.hexlify(bytes(packet)).decode('utf-8'))

            return packet

        def start(self):
            if self._timer is None:
                logging.debug("timer begin")
                self._timer_counter = 0
                self._timer = threading.Timer(0.1, self._scan_timer_handler_)
                self._timer.start()
                # 扫描正式开始，通知上层
                args = {
                    "type": "scanner",
                    "action": "start",
                    "args": ""
                }
                self._ccp.update_scanner_status(args)
            else:
                logging.debug("timer is not None")
                
        def _scan_timer_handler_(self):
            # logging.debug("timer_counter=%d" % self._timer_counter)
            if self._timer_counter < self._MAX_TIMES:
                self._timer_counter += 1
                # if self._timer_counter % 5 == 1:
                if self._timer_counter % 1 == 0:
                    packet = self._gen_discover_packet()
                    # 第一次进来就要发送一次，然后间隔5秒发送一次
                    self._send_packet_to_phy(packet)
                    logging.debug(f"第{self._timer_counter}次发送UDP扫描指令")
                self._timer = threading.Timer(1.0, self._scan_timer_handler_)
                self._timer.start()
                # # 可以在这里反馈扫描进度信息给上层
                # _progress = round(self._timer_counter * 100 / (self._MAX_TIMES + 1))
                # args = {
                #     "type": "scanner",
                #     "action": "process",
                #     "args": {
                #         "progress": _progress
                #     }
                # }
                # self._ccp.update_scanner_status(args)
            else:
                self._timer_counter = 0
                self._timer.cancel()
                self._timer = None
                # 可以在这里反馈扫描结束信息给上层
                # 扫描停止，通知上层
                args = {
                    "type": "scanner",
                    "action": "stop",
                    "args": ""
                }
                self._ccp.update_scanner_status(args)
                if len(self._ccp._invalid_dev_sns) == 0: return
                for sn in self._ccp._invalid_dev_sns:
                    args = {
                    "type": "scanner",
                    "action": "disconnected",
                    "args": {
                        "sn": sn
                        }
                    }
                    if self._ccp._device_status_listener is not None:
                        self._ccp._device_status_listener(args) # 上报主界面删除设备
        
        def stop(self):
            if self._timer is not None and self._timer.is_alive():
                logging.debug("timer cancel")
                self._timer.cancel()
                self._timer = None
                self._timer_counter = 0
                # 可以在这里反馈扫描结束信息给上层
                # 扫描停止，通知上层
                args = {
                    "type": "scanner",
                    "action": "stop",
                    "args": ""
                }
                self._ccp.update_scanner_status(args)
            else:
                logging.debug("timer is None or is not alive")

    class DevicePhy(object):
        def __init__(self, ccp, sn, addr) -> None:
            self._sn = sn
            self._addr = addr
            self._phy = AvmPhy()
            self._phy.run(self._recv_handle)
            self._ccp = ccp
        
        def _recv_handle(self, data, dev_addr):
            try:
                _data = AvmCCP.Parser.packet_parser(data)
                # print(">>>>> parsed _data:", _data)
                self._ccp._recv_handle(self._sn, _data)
            except Exception as e:
                import traceback
                logging.error("Drop this packet")
                print(traceback.format_exc())

        def send(self, packet):
            self._phy.send(packet, self._addr)

    def __init__(self) -> None:
        self._scanner = AvmCCP.Scanner(self)
        self._devs = []
        self._dev_lock = threading.Lock()
        self._index = 0
        self._app_cbs = []
        self._cbs_lock = threading.Lock()
        self._temp_deleted_devs = [] # 在某次扫描过程中被删除的设备SN
        self._temp_lock = threading.Lock()
        self._invalid_dev_sns = [] # 曾经连接但已不在当前网段且未删除的设备sn列表

        # self._command_thread = CommandBatcherThread()
        # self._command_thread.start()
        # self.async_action = self._command_thread.command_batcher.filter_batch_wrapper(self.async_action) # 手动将装饰器应用到方法上

        # self.command_batcher = CommandBatcher()
        # self.async_action = self.command_batcher.filter_batch_wrapper(self.async_action)

        ''' 模拟设备主动上报 '''
        # data = b'\x01\x01\x01\xc0\xa8\x03\xc6\xff\xff\xff\x00\xc0\xa8\x03\x01\x00' # 中文，风扇开，dhcp设置开
        # cmd = 152 # 网络设置同步上报
        # data = b'\x33\x66\x5f\x23\x13\xb5'
        # cmd = 147 # 
        # threading.Timer(10, self._recv_handle, ("52B7C1417B23", {'version': 256, 'index': 3, 'type': 2, 'session': 3, 'cmd': cmd, 'data': data})).start() # 

    def start_scan(self):
        logging.debug("start scan")
        host_name = socket.gethostname()
        ip = socket.gethostbyname(host_name)
        if host_name != self._scanner.host_name or ip != self._scanner.ip:
            logging.warning(">>> The Hostname or Host was changed.")
            for phy in self._scanner._phys:
                phy.thread_running = False # 关闭无需使用但正在运行的线程
            self._scanner = AvmCCP.Scanner(self) # 网络发生变化,重新创建Scanner对象
        
        if len(self._devs) > 0: # 如果之前添加过设备，将设备sn填入临时列表中
            with self._dev_lock:
                self._invalid_dev_sns.clear()
                for dev in self._devs:
                    self._invalid_dev_sns.append(dev["sn"])

        self._scanner.start()

    def stop_scan(self):
        logging.debug("stop scan")
        self._scanner.stop()
        with self._temp_lock:
            self._temp_deleted_devs.clear()

    def update_scanner_status(self, args):
        logging.debug("args: {}".format(args))
        self._dev_lock.acquire()
        # 通知上层，扫描的状态更新
        if self._device_status_listener is not None:
            self._device_status_listener(args)
        self._dev_lock.release()
        with self._temp_lock:
            if args["action"] == "stop":
                self._temp_deleted_devs.clear()
        
    def add_device(self, args):
        logging.debug("args: {}".format(args))
        if args["type"] == "device" and args["action"] == "new":
            with self._temp_lock:
                self._dev_lock.acquire()
                _args = args["args"]
                sn = _args["sn"]

                if sn in self._invalid_dev_sns:
                    self._invalid_dev_sns.remove(sn)
                
                if sn in self._temp_deleted_devs:
                    logging.info("扫描到已被删除的设备，此扫描过程不再添加")
                    self._dev_lock.release() # 貌似死锁就归咎于此处没有释放！
                    return
                is_exist = next((d for d in self._devs if d['sn'] == sn), None)
                # print(f">>> udp is Exist = {is_exist}")
                
                if not is_exist:
                    phy = AvmCCP.DevicePhy(self, sn, _args['addr'])
                    _args.update([('phy', phy)])
                    logging.debug("New device: {}".format(_args))
                    self._devs.append(_args)
                    logging.debug("All devices: {}".format(self._devs))
                    # 通知上层，设备状态有改变
                    if self._device_status_listener is not None:
                        self._device_status_listener(args)

                self._dev_lock.release()
    
    def delete_device(self, sn):
        logging.debug("sn: {}".format(sn))
        with self._temp_lock:
            # self._dev_lock.acquire()
            with self._dev_lock:

                for d in self._devs:
                    if d['sn'] == sn:
                        self._devs.remove(d)
                        
                        if self._scanner._timer_counter != 0: # 在扫描过程中删除过的设备，添加到临时被删除设备列表
                            self._temp_deleted_devs.append(d['sn'])
                        break

        # self._dev_lock.release()
        logging.debug(f"删除后，列表={self._devs}")

    def set_device_status_listener(self, device_status_listener):
        self._device_status_listener = device_status_listener

    def set_report_listener(self, report_listener):
        self._report_listener = report_listener

    def set_device_heartbeat_listener(self, heartbeat_listener):
        self._heartbeat_listener = heartbeat_listener

    def get_device_info_list(self):
        dev_info_list = []
        
        self._dev_lock.acquire()

        for dev in self._devs:
            dev_info = {
                "sn": dev['sn']
            }
            dev_info_list.append(dev_info)

        self._dev_lock.release()

        logging.debug("udp dev_info_list: {}".format(dev_info_list))
        return dev_info_list

    def _recv_handle(self, dev_sn, args):
        """
        args = {
                "version": _version,
                "index": _index,
                "type": _type,
                "session": _session,
                "cmd": _cmd,
                "data": _data
            }
        """
        # print("+++++++++++++++++++++++++ 收到指令的 data 部分 +++++++++++++++++++++++++++++++++++++")
        # print(args["data"])
        # print(args['data'].decode('utf-8'))
        # import binascii
        # print(binascii.hexlify(args['data']).decode('utf-8'))
        if args['type'] == AvmCCP.Header._resp_type:
            _cb_func = None

            # 收到回应报文，查找同样session和cmd的回调函数，取出后进行回调
            self._cbs_lock.acquire()
            for _cb in self._app_cbs:
                if _cb["session"] == args["session"] and _cb["cmd"] == args["cmd"]:
                    _cb_func = _cb["function"]
                    self._app_cbs.remove(_cb)
            self._cbs_lock.release()

            if _cb_func is not None:
                _cb_func(dev_sn, args["data"])
                # 处理完上一条回复结果，判断是否是需要批量处理的指令回复
                # if args["cmd"] in FILTER_CMD_LIST:
                #     # self._command_thread.trigger_send() # 通知发送当前批量指令中的最后一条
                #     logging.info(f" 收到回复 cmd={args["cmd"]:#x}在需要过滤的cmd列表中，判断是否需要通知set")
                #     self.command_batcher.trigger_send(dev_sn, args["cmd"])

        elif args['type'] == AvmCCP.Header._report_type:
            logging.info(">>>>>>>>>>>>>>>>>>>>>>>> 收到设备主动上报 >>>>>>>>>>>>>>>>>>>>>")
            if self._report_listener is not None:
                self._report_listener(dev_sn, args["cmd"], args["data"])

    def __find_device_by_sn(self, dev_sn):
        self._dev_lock.acquire()

        dev = next((d for d in self._devs if d['sn'] == dev_sn), None)

        self._dev_lock.release()

        return dev

    def __prepare_do_action(self, cmd, callback):
        self._index += 1
        session = random.randint(0, 0xFFFFFFFF)

        self._cbs_lock.acquire()
        for _cb in self._app_cbs:
            if _cb["session"] == session and _cb["cmd"] == cmd:
                self._cbs_lock.release()
                return False, 0

        _cb = {
            "session": session,
            "cmd": cmd,
            "function": callback
        }

        self._app_cbs.append(_cb)
        self._cbs_lock.release()

        return True, session

    def async_action(self, dev_sn, cmd, data:list, callback):
        # 先根据device sn找到对应的device
        dev = self.__find_device_by_sn(dev_sn)
        if dev is None:
            logging.error("AvmCCP: 未找到SN为" + dev_sn + "的device")
            return False

        # 再生成随机的session，并把cmd、callback，与session一起存入回调列表中，等待回应报文的处理
        ret, session = self.__prepare_do_action(cmd, callback)
        if ret:
            packet = AvmCCP.Packer.command_data_packing(self._index, session, cmd, data, len(data))
            phy = dev['phy']
            assert(phy is not None)
            phy.send(packet)
            logging.debug("AvmCCP: 发送action成功")
            # import binascii 
            # print("=================================发送指令转换成16进制后：=================================")
            # print(binascii.hexlify(bytes(packet)).decode('utf-8'))
            # logging.info(">>> restart to send heartbeat")
            if self._heartbeat_listener is not None:
                self._heartbeat_listener(dev_sn, "reset") # 通知上层，心跳重新计时
            return True
        else:
            return False
            
    def send_heartbeat_instruction(self, dev_sn, device_type, mac_row):
        _mac_addr = AvmCCP.Parser.mac_string_to_hex(mac_row)
        _cmd = 0xEEEE
        _data = [device_type] + _mac_addr

        dev = self.__find_device_by_sn(dev_sn)
        if dev is None:
            logging.error("AvmCCP: 未找到SN为" + dev_sn + "的device")
            return False
        ret, session = self.__prepare_do_action(_cmd, self.__handle_received_heartbeat)
        if ret:
            packet = AvmCCP.Packer.command_data_packing(self._index, session, _cmd, _data, len(_data))
            phy = dev['phy']
            assert(phy is not None)
            phy.send(packet)
            logging.debug("Avm UDP CCP: 发送心跳包成功")
            # import binascii 
            # print("心跳包指令转换成16进制后：")
            # print(binascii.hexlify(bytes(packet)).decode('utf-8'))

    def __handle_received_heartbeat(self, dev_sn, args): # 解析心跳数据，检查是否符合协议，上报结果
        logging.debug("args:{}".format(args))
        dev = self.__find_device_by_sn(dev_sn)
        if dev is None and self._heartbeat_listener is not None:
            self._heartbeat_listener(dev_sn, "stop") # 设备可能已经被删除，上报停止心跳
            return
        _mac = dev["mac"]
        _ret_mac = "{:02X}:{:02X}:{:02X}:{:02X}:{:02X}:{:02X}".format(args[16], args[17], args[18], args[19], args[20], args[21])
        if _mac != _ret_mac: return # mac地址不一样，心跳不重新计时
        self._heartbeat_listener(dev_sn, "received")


import logging
import traceback
import random
import socket
import time
from _thread import *
import threading
from datetime import datetime

class AvmPhy(object):
    def __init__(self):
        self.__recv_handle = None
        self._has_send_data = False
        # self.__report_listener = None
        # self.__dev_sta_listener = None
        self._sock = None

    # def init_phy(self, recv_handle):
    #     self.__recv_handle = recv_handle
    
    # def __run_scan_thread(self) -> None:
    #     scan_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    #     #start_new_thread(self.__scan_thread__, (scan_sock,))
    #     start_new_thread(self.__scan_recv_thread__, (scan_sock,))
    #     return

    # def __run_packet_thread(self) -> None:
    #     self.__packet_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    #     start_new_thread(self.__packet_recv_thread__, (self.__packet_sock,))
    #     return

    def run(self, recv_handle):
        self.__recv_handle = recv_handle

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        start_new_thread(self.__recv_thread__, (self._sock,))
        return

    # def set_report_listener(self, report_listener):
    #     self.__report_listener = report_listener

    # def set_device_status_listener(self, dev_sta_listener):
    #     self.__dev_sta_listener = dev_sta_listener

    def send(self, packet, addr):
        try:
            self._sock.sendto(bytes(packet), addr)

            # 设置已经发送给server端数据包的标记，以便可以准备recvfrom，否则会抛出异常
            if self._has_send_data is False:
                self._has_send_data = True
        except Exception as e:
            logging.error("AvmPhy在发送数据时通信异常")
            logging.error(traceback.format_exc())
            self._sock.close()

    # def __scan_thread__(self, sock):
    #     pass

    # def __scan_recv_thread__(self, sock):
    #     while True:
    #         data, dev_addr = sock.recvfrom(1560)
    #         try:
    #             if self.__dev_sta_listener != None:
    #                 self.__dev_sta_listener(data, dev_addr)
    #         except Exception as e:
    #             logging.error(e)
    #             logging.error("Drop the scan receive data")

    def __recv_thread__(self, sock):
        # 等待发送数据包给server端已经完成，再开始recvfrom
        while self._has_send_data is False:
            time.sleep(0.1)

        while True:
            data, addr = self._sock.recvfrom(1560)
            # print(">>>>> row data: ", data)
            # import binascii
            # print(binascii.hexlify(data).decode('utf-8'))
            # logging.debug("data:", data)
            # logging.debug("addr:", addr)
            try:
                if self.__recv_handle != None:
                    self.__recv_handle(data, addr)
            except Exception as e:
                logging.error("Drop the receive data")
                logging.error(traceback.format_exc())

class AvmScannerPhy(object):
    def __init__(self):
        self._local_port = 52588
        self.__recv_handle = None
        self._has_send_data = False
        self._sock = None
        # self._send_flag = False

        # 模拟多个设备
        # self._devs = []
        # self.__fake_devices()

        self.thread_running = True

    '''
    def _generate_serial_number(self, prefix, length):
        chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return prefix + '-' + ''.join(random.choice(chars) for _ in range(length))

    def _generate_mac(self):
        chars = '0123456789ABCDEF'

        mac_str = ''.join(random.choice(chars) for _ in range(2))
        for _ in range(5):
            mac_str = mac_str + '-' + ''.join(random.choice(chars) for _ in range(2))

        return mac_str

    def _generate_model(self):
        models = [
            {
                "model":"SC7030",
                "type":"CONVERTER",
                "interface":"USB"
            },
            {
                "model":"CUE01",
                "type":"CHROMA",
                "interface":"Ethernet"
            },
            {
                "model":"VS0605E",
                "type":"SWITCHER",
                "interface":"Ethernet"
            },
            {
                "model":"PVS0403E",
                "type":"SWITCHER",
                "interface":"Ethernet"
            }
        ]

        # index = random.randint(0, 3)
        index = 1
        print("index:", index)

        return models[index]

    def __fake_devices(self):
        port_base = 8000

        self._devs.clear()

        for i in range(1):
            model = self._generate_model()
            sn = self._generate_serial_number(model["model"], 8)
            mac_str = self._generate_mac()
            name = model["model"] + '-' + mac_str[12:14] + mac_str[15:]
            dev = {
                "addr": ("192.168.3.198", port_base),
                "model": model["model"],
                "type": model["type"],
                "interface": model["interface"],
                "sn": sn,
                "name": name,
                "mac": mac_str
            }
            self._devs.append(dev)

            port_base = port_base + 1
    '''

    def run(self, recv_handle, bind_ip = None):
        self.__recv_handle = recv_handle

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 允许地址复用
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 设置广播模式
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # 绑定到特定的本地地址和端口 
        if bind_ip != None: 
            # self._sock.bind((bind_ip, self._local_port))
            self._sock.bind((bind_ip, 0)) # 改为系统自动分配端口号
        
        assigned_port = self._sock.getsockname()[1]
        logging.info(f"Assigned Scanner Port: {assigned_port}")
        
        start_new_thread(self.__recv_thread__, (self._sock,))
        return

    def send(self, packet, addr):
        try:
            # logging.debug("send packet:{}".format(packet))
            # logging.debug("send addr:{}".format(addr))
            self._sock.sendto(bytes(packet), addr)

            # self._send_flag = True
            # 设置已经发送给server端数据包的标记，以便可以准备recvfrom，否则会抛出异常
            if self._has_send_data is False:
                self._has_send_data = True

        except Exception as e:
            # logging.error(e)
            logging.error("AvmScannerPhy在发送数据时通信异常如下")
            logging.error(traceback.format_exc())
            self._sock.close()

    def __recv_thread__(self, sock):
        # 等待发送数据包给server端已经完成，再开始recvfrom
        while self._has_send_data is False:
            time.sleep(0.1)

        while self.thread_running:
            # time.sleep(0.1)

            # if self._send_flag is False:
            #     continue
            # else:
            #     logging.debug("AvmScannerPhy: recv handle")

            # self._send_flag = False
            data, addr = self._sock.recvfrom(1560)
            # index = random.randint(0, len(self._devs) - 1)
            # dev = self._devs[index]

            # addr = dev["addr"]
            
            # print(">>>>>>>>>> row_scanner_data:", data)
            # import binascii 
            # print("转换成16进制后：")
            # print(binascii.hexlify(data).decode('utf-8'))

            try:
                if self.__recv_handle != None:
                    self.__recv_handle(data, addr)
            except Exception as e:
                logging.error("Drop the receive data")
                logging.error(traceback.format_exc())
            

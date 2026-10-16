import logging
import random

from src.avm_stack.usb_stack.packet.command import CmdEnum
from src.avm_stack.usb_stack.packet.parser import Parser


class DeviceInfor(object):
    def __init__(self):
        self.__str_proto_ver = None
        self.__str_boot_ver = None
        self.__str_app_ver = None
        self.__str_fpga_ver = None
        self.__str_hardware_ver = None
        self.__mcu_mode = 0
        self.__has_fpga = 0
        self.__can_control = True # 设备是否可控，默认可控

    def set_control_status(self, status:bool):
        self.__can_control = status
    
    def get_control_status(self):
        return self.__can_control

    def set_byte_protocol_version(self, byte_proto_ver):
        self.__str_proto_ver = "V%d.%d" % (byte_proto_ver[0], byte_proto_ver[1])

    def get_protocol_version(self):
        return self.__str_proto_ver

    def set_mcu_mode(self, mode):
        self.__mcu_mode = mode

    def get_mcu_mode(self):
        return self.__mcu_mode

    def set_has_fpga(self, has_fpga):
        self.__has_fpga = has_fpga

    def get_has_fpga(self):
        return self.__has_fpga

    def set_byte_boot_version(self, byte_boot_ver):
        if byte_boot_ver[3] != 0:
            self.__str_boot_ver = "V%d.%d.%d.%d" % (byte_boot_ver[0], byte_boot_ver[1],
                                                    byte_boot_ver[2], byte_boot_ver[3])
        else:
            self.__str_boot_ver = "V%d.%d.%d" % (byte_boot_ver[0], byte_boot_ver[1], byte_boot_ver[2])

    def get_boot_version(self):
        return self.__str_boot_ver

    def set_byte_app_version(self, byte_app_ver):
        if byte_app_ver[3] != 0:
            self.__str_app_ver = "V%d.%d.%d.%d" % (byte_app_ver[0], byte_app_ver[1],
                                                    byte_app_ver[2], byte_app_ver[3])
        else:
            self.__str_app_ver = "V%d.%d.%d" % (byte_app_ver[0], byte_app_ver[1], byte_app_ver[2])

    def get_app_version(self):
        return self.__str_app_ver

    def set_byte_fpga_version(self, byte_fpga_ver):
        if byte_fpga_ver[3] != 0:
            self.__str_fpga_ver = "V%d.%d.%d.%d" % (byte_fpga_ver[0], byte_fpga_ver[1],
                                                    byte_fpga_ver[2], byte_fpga_ver[3])
        else:
            self.__str_fpga_ver = "V%d.%d.%d" % (byte_fpga_ver[0], byte_fpga_ver[1], byte_fpga_ver[2])

    def get_fpga_version(self):
        return self.__str_fpga_ver

    def set_byte_hardware_version(self, byte_hardware_ver):
        if byte_hardware_ver[3] != 0:
            self.__str_hardware_ver = "V%d.%d.%d.%d" % (byte_hardware_ver[0], byte_hardware_ver[1],
                                                        byte_hardware_ver[2], byte_hardware_ver[3])
        elif byte_hardware_ver[2] != 0:
            self.__str_hardware_ver = "V%d.%d.%d" % (byte_hardware_ver[0], byte_hardware_ver[1], byte_hardware_ver[2])
        else:
            self.__str_hardware_ver = "V%d.%d" % (byte_hardware_ver[0], byte_hardware_ver[1])

    def get_hardware_version(self):
        return self.__str_hardware_ver

    def __str__(self):
        str = "Protocol Version:{}\n".format(self.__str_proto_ver)
        str = str + "MCU Mode:{}\n".format(self.__mcu_mode)
        str = str + "Has FPGA:{}\n".format(self.__has_fpga)
        str = str + "Boot Version:{}\n".format(self.__str_boot_ver)
        str = str + "App Version:{}\n".format(self.__str_app_ver)
        str = str + "FPGA Version:{}\n".format(self.__str_fpga_ver)
        str = str + "Hardware Version:{}\n".format(self.__str_hardware_ver)
        return str


class ComServer(object):
    def __init__(self, transport):
        self.__transport = transport

    def get_protocal_version(self):
        ret = self.__transport.send_command(CmdEnum.GET_MCU_VER.value, timeout=2000)
        if ret is not True:
            logging.error("Get protocol version error: send command error")
            return None

        ret, t = self.__transport.receive(timeout=2000)
        if ret:
            logging.debug(t)
            magic_number = int.from_bytes(t[8:12], byteorder='little')
            if magic_number == Parser.get_magic_number():
                return "V%d.%d" % (t[12], t[13])
            else:
                logging.error("Not support Matrix's USB protocol V1.0")
                return None
        else:
            logging.error("Receive error")
            return None

    def get_device_infor(self):
        import binascii
        
        session = random.randint(0, 100000000)
        byte_session = session.to_bytes(4, "little")

        ret = self.__transport.send_data(CmdEnum.QUERY_DEV_INFO.value, byte_session, len(byte_session), timeout=2000)
        if ret is False:
            logging.error("Get device information error: send command error")
            return None

        ret, t = self.__transport.receive(timeout=2000)
        if ret:
            # logging.debug(binascii.hexlify(t).decode('utf-8'))
            magic_number = int.from_bytes(t[0:4], byteorder='little')
            response_session = int.from_bytes(t[4:8], byteorder='little')
            # logging.debug("magic_number:{}".format(binascii.hexlify(magic_number.to_bytes(4, "little")).decode('utf-8')))
            # logging.debug("response_session:{}".format(binascii.hexlify(response_session.to_bytes(4, "little")).decode('utf-8')))
            # logging.debug("Parser's magic number:{}".format(binascii.hexlify(Parser.get_magic_number().to_bytes(4, "little")).decode('utf-8')))
            # logging.debug("send session:{}".format(binascii.hexlify(session.to_bytes(4, "little")).decode('utf-8')))
            if magic_number == Parser.get_magic_number() and session == response_session:
                devinfo = DeviceInfor()
                devinfo.set_byte_protocol_version(t[8:10])
                devinfo.set_mcu_mode(t[10])
                devinfo.set_has_fpga(t[11])
                devinfo.set_byte_boot_version(t[12:16])
                devinfo.set_byte_app_version(t[16:20])
                devinfo.set_byte_fpga_version(t[20:24])
                devinfo.set_byte_hardware_version(t[24:28])
                if len(t) > 30:
                    if t[29] == 1: # 1：不可控，0：可控
                        logging.info(f"args[21] = {t[21]}，设备不可控")
                        devinfo.set_control_status(False)
                return devinfo
            else:
                logging.error("Error device information")
                return None
        else:
            logging.error("Receive error")
            return None

    def get_configure_chips(self):
        session = random.randint(0, 100000000)
        byte_session = session.to_bytes(4, "little")
        # logging.debug("send session:{}".format(session))
        ret = self.__transport.send_data(CmdEnum.QUERY_CONFIG_CHIPS.value, byte_session, len(byte_session), timeout=2000)
        if ret is False:
            logging.error("Get configure chips error")
            return None

        ret, t = self.__transport.receive(timeout=2000)
        if ret:
            logging.debug(t)
            magic_number = int.from_bytes(t[0:4], byteorder='little')
            response_session = int.from_bytes(t[4:8], byteorder='little')
            # logging.debug("magic_number:{}".format(magic_number))
            # logging.debug("response_session:{}".format(response_session))
            # logging.debug("Parser's magic number:{}".format(Parser.get_magic_number()))
            if magic_number == Parser.get_magic_number() and session == response_session:
                chips_num = t[8]
                chip_list = []

                for i in range(chips_num):
                    base_offset = 9 + i*7
                    model_code = int.from_bytes(t[base_offset:base_offset + 2], byteorder='little')
                    chip_addr = t[base_offset + 2]
                    iport_map = t[base_offset + 3]
                    oport_map = t[base_offset + 5]
                    chip_dict = {
                        'model_code': model_code,
                        'chip_addr': chip_addr,
                        'iport_map': iport_map,
                        'oport_map': oport_map
                    }
                    chip_list.append(chip_dict)
                return chip_list
            else:
                logging.error("Error configure chips")
                return None
        else:
            logging.error("Receive error")
            return None

    def test(self):
        ret = self.__transport.send_command(CmdEnum.GET_MCU_VER.value, timeout=2000)
        if ret is not True:
            logging.error("Get protocol version error")
            return None

        ret, t = self.__transport.receive()
        if ret:
            magic_number = int.from_bytes(t[8:11], byteorder='little')
            if magic_number == Parser.get_magic_number():
                return t[12:13]
            else:
                logging.error("Not support Matrix's USB protocol V1.0")
                return None
        else:
            logging.error("Receive error")
            return None
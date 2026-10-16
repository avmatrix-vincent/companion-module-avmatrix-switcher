import logging
import os
import platform
import sys
import usb

class DataChecker:
    @staticmethod
    def calc_sum(data, num):
        sum = 0

        for i in range(num):
            sum += data[i]

        sum = 0xffff & sum
        return sum.to_bytes(2, "little")
    
class Packer(object):
    __packet_head = [0xa5, 0x6c]
    __packet_unknow = [0x81, 0x01, 0x03]
    __packet_data_max_len = 512
    __packet_tail = 0xae

    @staticmethod
    def paging_packet(page, cmd, data, datalen):
        """
        :param page: 分页序号
        :param cmd: 指令值
        :param data: 数据
        :param datalen: 数据长度
        :return: 返回封装好的报文
        """
        packet_data_len = 17 + datalen + 3
        zero_fill_len = 576 - packet_data_len
        packet = []
        packet += Packer.__packet_head
        packet += packet_data_len.to_bytes(2, "little")
        packet += Packer.__packet_unknow
        packet += page.to_bytes(2, "little")
        packet += ([0x00] * 7)
        packet += cmd.to_bytes(1, "little")
        packet += data
        packet += DataChecker.calc_sum(packet, packet_data_len - 3)
        packet += Packer.__packet_tail.to_bytes(1, "little")
        packet += [0x00] * zero_fill_len


        return packet

class TestLibusb(object):
    def __init__(self):
        self.__idVendor = 0x0483
        self.__idProduct = 0x5750
        self.__uc7018_pid = 2

    def __resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        return os.path.join(base_path, relative_path)

    def __find_library(self, libfile):
        libfile = "lib" + libfile + ".dll"
        logging.info(libfile)
        machine = platform.machine()
        if machine.upper() == 'x86'.upper():
            libfile = self.__resource_path("res\\libusb\\x86\\"+libfile)
        else:
            libfile = self.__resource_path("res\\libusb\\x64\\" + libfile)

        if os.path.exists(libfile):
            logging.info(libfile)
            return libfile

        return None

    def __get_backend(self):
        import usb.backend.libusb1
        usb.backend.libusb1._logger.setLevel(logging.INFO)
        backend = usb.backend.libusb1.get_backend(find_library=self.__find_library)
        if backend is None:
            logging.error("Have not got local backend")

        return backend

    def test(self):
        backend = self.__get_backend()
        self.__device = usb.core.find(backend=backend, idVendor=self.__idVendor, idProduct=self.__idProduct)
        if self.__device is None:
            raise ValueError('Device not found')

        logging.info("Find out device")
        logging.info("Device info:")
        logging.info("bcdDevice: 0x%04X" % self.__device.bcdDevice)
        logging.info("bDeviceClass: 0x%02X" % self.__device.bDeviceClass)
        logging.info("bDeviceSubClass: 0x%02X" % self.__device.bDeviceSubClass)
        logging.info("bDeviceProtocol: 0x%02X" % self.__device.bDeviceProtocol)
        logging.info("bNumConfigurations: %d" % self.__device.bNumConfigurations)
        logging.info(usb.util.get_string(self.__device, self.__device.iManufacturer))
        logging.info(usb.util.get_string(self.__device, self.__device.iProduct))
        logging.info(usb.util.get_string(self.__device, self.__device.iSerialNumber))

        import random
        session = random.randint(0, 100000000)
        byte_session = session.to_bytes(4, "little")
        data = []
        data += byte_session
        data += self.__uc7018_pid.to_bytes(1, "little")

        # Get device's configuration: the command is 0xB0
        _packet = Packer.paging_packet(0, 0xB0, data, len(data))
        # Write the command packet to the device
        self.__device.write(0x01, _packet, timeout=3000)
        # Read the response from the device
        t = self.__device.read(0x81, 64, timeout=3000)
        
        param_valid = int.from_bytes(t[9:11], byteorder='little')
        output_timing = t[11] if param_valid & 0x01 == 0x01 else 0 # bit0
        imput_mode = t[12] if param_valid & 0x02 == 0x02 else 0 # bit1
        audio_input = t[13] if param_valid & 0x04 == 0x04 else 0 # bit2
        aspect_ratio = t[14] if param_valid & 0x08 == 0x08 else 0 # bit3
        hdmi_color_range = t[15] if param_valid & 0x10 == 0x10 else 0 # bit4
        sdi_mode = t[16] if param_valid & 0x20 == 0x20 else 0 # bit5
        color_space = t[17] if param_valid & 0x40 == 0x40 else 0 # bit6
        pc_flag = t[18] if param_valid & 0x80 == 0x80 else 0 # bit7

        session = random.randint(0, 100000000)
        byte_session = session.to_bytes(4, "little")
        data = []
        data += byte_session
        data += self.__uc7018_pid.to_bytes(1, "little")

        imput_mode = 4 # 0: SDI, 1: HDMI, 2: DVI, 3: VGA, 4: YPbPr, 5: S-Video, 6: CVBS, 7: SDI + HDMI
        param_valid = 0x0002 # bit1, only imput_mode is valid
        data += param_valid.to_bytes(2, "little")
        data += [0] # output_timing
        data += imput_mode.to_bytes(1, "little")
        data += [0] * 5 # audio_input, aspect_ratio, hdmi_color_range, sdi_mode, color_space

        # Set device's configuration: the command is 0xB1
        _packet = Packer.paging_packet(0, 0xB1, data, len(data))
        # Write the command packet to the device
        self.__device.write(0x01, _packet, timeout=3000)
        # Read the response from the device
        t = self.__device.read(0x81, 64, timeout=3000)
        logging.info("Set device's configuration response: %s" % "success" if t[9] == 0x00 else "fail")

        return True

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # tlb = TestLibusb()
    # try:
    #     tlb.test()
    # except BaseException as error:
    #     logging.error(error)
    chengben = 26
    zzshuilv = 0.13

    maolilv_list = [0.2, 0.3, 0.4, 0.5]

    for maolilv in maolilv_list:    
        maoli = round(chengben/(1-maolilv) - chengben, 2)
        zzshui = round(maoli * zzshuilv, 2)
        baojia = round(chengben + maoli + zzshui, 2)
        print("成本: %.2f, 毛利率: %.2f, 增值税税率: %.2f, 毛利: %.2f, 增值税: %.2f, 报价: %.2f" % (chengben, maolilv, zzshuilv, maoli, zzshui, baojia))
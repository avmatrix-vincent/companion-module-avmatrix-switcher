import os
import sys
import shutil
import logging
import platform
import hid
from globals import relative_path

ARM64_HIDAPI_FILE_PATH = "res/hidapi/Mac/arm64/libhidapi.dylib" # hidapi 无需后端文件，此处是 pyusb 遗留
X86_64_HIDAPI_FILE_PATH = ""

class UDevice(object):
    def __init__(self, vendor_id=0x0483, product_id=0x5750):
        self.__idVendor = vendor_id
        self.__idProduct = product_id
        self.__devices = None
        self.__select_device = None
        self.__current_hidapi_path = ""

    def __find_library(self, libname):
        if platform.system() == "Darwin":  # MacOS
            hidapi_path = relative_path(self.__current_hidapi_path)
            if os.path.exists(hidapi_path):
                logging.info(f"Found macos hidapi file: {hidapi_path}")
                return hidapi_path
        return None

    def __get_backend(self):
        logging.info(platform.machine())
        if "arm64" in platform.machine():
            self.__current_hidapi_path = ARM64_HIDAPI_FILE_PATH
        else:
            self.__current_hidapi_path = X86_64_HIDAPI_FILE_PATH
        if getattr(sys, 'frozen', False):
            logging.info("执行复制dylib文件操作")
            shutil.copy2(os.path.join(sys._MEIPASS, self.__current_hidapi_path), os.path.join(sys._MEIPASS, os.path.basename(self.__current_hidapi_path)))
        return self.__find_library

    def scan(self):
        # self.__get_backend() # hidapi 无需后端文件，此处是 pyusb 遗留
        self.__devices = hid.enumerate(self.__idVendor, self.__idProduct)
        if not self.__devices:
            raise ValueError('Device not found')
        return self.__get_device_list()

    def __get_device_list(self):
        device_list = []
        if self.__devices is None:
            return None

        for device in self.__devices:
            devinfo_dict = {
                'manufacturer': device['manufacturer_string'],
                'product': device['product_string'],
                'sn': device['serial_number']
            }
            device_list.append(devinfo_dict)

        return device_list

    def connect(self, devinfo_dict):
        if self.__devices is None:
            return False

        for device in self.__devices:
            if devinfo_dict['manufacturer'] == device['manufacturer_string'] and \
               devinfo_dict['model'] == device['product_string'] and \
               devinfo_dict['sn'] == device['serial_number']:
                self.__select_device = hid.device(path=device['path'])
                self.__select_device.open(self.__idVendor, self.__idProduct)
                return True

        return False

    def disconnect(self):
        if self.__select_device:
            self.__select_device.close()
        self.__select_device = None

    def is_connected(self):
        return self.__select_device is not None

    def send(self, packet, timeout=1000):
        try:
            if self.is_connected():
                self.__select_device.write(bytearray(packet))
                return True
            return False
        except Exception as error:
            logging.error(error)
            import traceback
            logging.error(traceback.format_exc())
            return False

    def receive(self, length, timeout=1000):
        try:
            if self.is_connected():
                data = self.__select_device.read(length, timeout)
                return True, data
            return False, None
        except Exception as error:
            logging.info(error)
            return False, None

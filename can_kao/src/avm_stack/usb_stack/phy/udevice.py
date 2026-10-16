import os, sys, shutil
import logging
import platform
import usb.backend.libusb1
import usb.core
import usb.util
from globals import relative_path


class UDevice(object):
    def __init__(self, vendor_id=0x0483, product_id=0x5750):
        self.__idVendor = vendor_id
        self.__idProduct = product_id
        self.__devices = None
        self.__select_device = None
        self.__backend = None

    def __resource_path(self, relative_path):
        # runtime_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))), 'res')
        runtime_path = "res"
        base_path = getattr(sys, '_MEIPASS', runtime_path)
        real_path = os.path.join(base_path, relative_path)
        print(f"real backend path={real_path}")
        return real_path

    def __find_library(self, libfile): # 打包后的exe不会使用这个方法查找dll文件
        logging.info("use custom function to find dll文件")
        libfile = "lib" + libfile + ".dll"
        machine = platform.machine()
        if machine.upper() == 'x86'.upper():
            logging.info(">>> x86 dll file")
            # libfile = self.__resource_path("libusb\\x86\\" + libfile)
            libfile = relative_path("res\\libusb\\x86\\" + libfile)
        else:
            logging.info(">>> x64 dll file")
            # libfile = self.__resource_path("libusb\\x64\\" + libfile)
            libfile = relative_path("res\\libusb\\x64\\" + libfile)

        logging.info(f">>> libfile={libfile}")
        if os.path.exists(libfile):
            logging.info(">>> exist backend file")
            return libfile
        logging.warning(">>> not exist backend file")
        return None

    def __get_backend(self):
        if getattr(sys, 'frozen', False):
            # logging.info("执行复制dll文件操作")
            logging.info(platform.machine())
            if "86" in platform.machine():
                if not os.path.exists(os.path.join(sys._MEIPASS, "libusb-1.0.dll")):
                    shutil.copy2(os.path.join(sys._MEIPASS, "res/libusb/x86/libusb-1.0.dll"), os.path.join(sys._MEIPASS, "libusb-1.0.dll"))
                    logging.info(">>> copy x86 dll from MEIPASS/res/libusb/x86 to MEIPASS ")
            else:
                if not os.path.exists(os.path.join(sys._MEIPASS, "libusb-1.0.dll")):
                    shutil.copy2(os.path.join(sys._MEIPASS, "res/libusb/x64/libusb-1.0.dll"), os.path.join(sys._MEIPASS, "libusb-1.0.dll"))
                    logging.info(">>> copy x64 dll from MEIPASS/res/libusb/x64 to MEIPASS ")
        usb.backend.libusb1._logger.setLevel(logging.INFO)
        backend = usb.backend.libusb1.get_backend(find_library=self.__find_library)
        if backend is None:
            logging.error("Have not got local backend")

        return backend

    def scan(self):
        if self.__backend is None:
            self.__backend = self.__get_backend()
        self.__devices = usb.core.find(find_all=True, backend=self.__backend,
                                       idVendor=self.__idVendor, idProduct=self.__idProduct)
        if self.__devices is None:
            raise ValueError('Device not found 1')

        device_list = self.__get_device_list()

        """
        不知道什么原因，在对self.__devices进行遍历后，就需要再次find，self.__devices才能
        继续有效使用
        """
        self.__devices = usb.core.find(find_all=True, backend=self.__backend,
                                       idVendor=self.__idVendor, idProduct=self.__idProduct)
        if self.__devices is None:
            raise ValueError('Device not found 2')

        return device_list

    def __get_device_list(self):
        device_list = []
        if self.__devices is None:
            return None

        for device in self.__devices:
            devinfo_dict = {'manufacturer': usb.util.get_string(device, device.iManufacturer),
                            'product': usb.util.get_string(device, device.iProduct),
                            'model': usb.util.get_string(device, device.iProduct),
                            'sn': usb.util.get_string(device, device.iSerialNumber)}
            device_list.append(devinfo_dict)

        return device_list
 
    def connect(self, devinfo_dict):
        #self.scan()
        # 这是为了避免多设备同时向同一设备设置一个值，当前是为了重新find一下这个对象，不然里面配置都是错误的。
        self.__devices = usb.core.find(find_all=True, backend=self.__backend,
                                       idVendor=self.__idVendor, idProduct=self.__idProduct)
        if self.__devices is None:
            raise ValueError('Device not found 2')


        if self.__devices is None:
            return False

        for device in self.__devices:
            if devinfo_dict['manufacturer'] == usb.util.get_string(device, device.iManufacturer) and \
                devinfo_dict['model'] == usb.util.get_string(device, device.iProduct) and \
                    devinfo_dict['sn'] == usb.util.get_string(device, device.iSerialNumber):
                self.__select_device = device
                return True

        return False

    def disconnect(self):
        self.__select_device = None

    def is_connected(self):
        if self.__select_device is not None:
            return True

        return False

    def send(self, packet, timeout=1000):
        try:
            if self.is_connected():
                self.__select_device.write(0x01, bytearray(packet), timeout=timeout)
                return True

            return False
        except BaseException as error:
            logging.info(error)
            return False

    def receive(self, length, timeout=1000):
        try:
            if self.is_connected():
                t = self.__select_device.read(0x81, length, timeout=timeout)
                return True, t

            return False, None
        except BaseException as error:
            logging.info(error)
            return False, None


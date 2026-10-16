import logging
import random
import os
import traceback
from _thread import *
import threading
import queue
import platform
from globals import relative_path
from src.avm_stack.lib_rtice.rtice_dev import RticeDevice

class RticeCCP(object):
    def __init__(self) -> None:
        self._libfile = self.__find_library(libfile="RTICE_SDK_x64")
        logging.info(f"RTICE libfile: {self._libfile}")

        """
        item:{
            "sn": "xxxx",
            "dev": RticeDevice()
        }
        """
        self._devs = []
        self._dev_lock = threading.Lock()
        self._task_queue = queue.Queue()
        start_new_thread(self._do_function, (self._task_queue,))
    
    def __find_library(self, libfile): # 打包后的exe不会使用这个方法查找dll文件
        logging.info("use custom function to find dll文件")
        libfile = libfile + ".dll"
        machine = platform.machine()
        if machine.upper() == 'x86'.upper():
            logging.info(">>> x86 dll file")
            libfile = relative_path("res\\librtice\\x86\\" + libfile)
        else:
            logging.info(">>> x64 dll file")
            libfile = relative_path("res\\librtice\\x64\\" + libfile)

        logging.info(f"RTICE libfile: {libfile}")
        if os.path.exists(libfile):
            logging.info(">>> exist RTICE libfile")
            return libfile

        logging.error(">>> not exist RTICE libfile")
        return None

    def _find_device_by_sn(self, dev_sn):
        _dev = None

        with self._dev_lock:
            _dev = next((d for d in self._devs if d['sn'] == dev_sn), None)
        
        return _dev["dev"] if _dev is not None else None

    def _register_device(self, dev_sn, dev):
        with self._dev_lock:
            _dev = next((d for d in self._devs if d['sn'] == dev_sn), None)
            if _dev is None:
                _dev = {
                    "sn": dev_sn,
                    "dev": dev
                }
                self._devs.append(_dev)

    def _delete_device(self, dev_sn):
        with self._dev_lock:
            self._devs = [d for d in self._devs if d['sn'] != dev_sn]
    
    def __init_device(self, dev_sn):
        # 查找dll是否已经在列表中, 代表已经初始化过了
        _dev = self._find_device_by_sn(dev_sn)
        if _dev is not None:
            return True

        _dev = RticeDevice(dev_sn, self._libfile)
        ret = _dev.init_device()

        if ret: 
            self._register_device(dev_sn, _dev)

        return ret

    def __deinit_device(self, dev_sn):
        # 查找dll是否已经在列表中, 代表已经初始化过了
        _dev = self._find_device_by_sn(dev_sn)
        if _dev is None:
            return True

        ret = _dev.deinit_device()

        if ret: 
            self._delete_device(dev_sn)

        return ret

    def __async_callback(self, dev_sn, callback, args):
        if callback is not None:
            callback(dev_sn, args)

    def async_action(self, dev_sn, func, args, callback):
        _task = {
            "func": func,
            "args": args,
            "cb": callback,
            "sn": dev_sn
        }
        
        self._task_queue.put(_task)

        return True
        
    def _do_function(self, task_queue):
        while True:
            task = task_queue.get()  # 从队列中获取任务
            if task is None:  # 如果任务是None，表示结束信号
                break
            # 执行任务
            logging.debug(f"Processing task: {task}")
            
            if task["func"] == "init_device":
                ret = self.__init_device(task["sn"])
                _args = {
                    "Result": ret
                }
                self.__async_callback(task["sn"], task["cb"], _args)
            elif task["func"] == "deinit_device":
                ret = self.__deinit_device(task["sn"])
                _args = {
                    "Result": ret
                }
                self.__async_callback(task["sn"], task["cb"], _args)
            else:
                # 先根据device sn找到对应的device
                dev = self._find_device_by_sn(task["sn"])

                if dev is None:
                    logging.error("RticeCCP: 未找到SN为" + task["sn"] + "的device")
                    _args = {
                        "Result": False
                    }
                    self.__async_callback(task["sn"], task["cb"], _args)
                else:
                    # if task["func"] == "get_customer_version":
                    if hasattr(dev, task["func"]):
                        _func = getattr(dev, task["func"])
                        _args = _func(task["args"])

                        if not _args["Result"]:
                            logging.error("执行任务时发生错误：错误码=" + str(_args["ErrorCode"]) + ", 错误描述=" + _args["ErrorDescription"])
                            if _args["ErrorCode"] > 0:
                                ret = self.__init_device(task["sn"])
                                logging.error(f"重新初始化设备, ret={ret}")
                                if ret:
                                    _args = _func(task["args"])
                                    logging.error(f"重新执行任务, _args={_args}")
                        
                        self.__async_callback(task["sn"], task["cb"], _args)
                    else:
                        _args = {
                            "Result": False,
                            "Reason": "Unsupport function"
                        }
                        self.__async_callback(task["cb"], _args)

            task_queue.task_done()  # 标记任务完成
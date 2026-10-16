import logging
import threading
import queue
from _thread import *
import traceback

class ModelPreferences(object):
    _product_type = ["Unknow", "Switcher", "Encoder", "Chroma"]
    _mcu_mode = ["Boot Mode", "App Mode"]
    _usb_model_list = ["SC7030", "SC7018", "SC1112-12G", "SC1221-12G", "SD1242-4K", "UC1218-4K"]
    _color_space_list = ["RGB", "YUV422", "YUV444"]

    _udp_model_index_map = [
        {
            "models": ["VS0605E"],
            "index": 1
        },{
            "models": ["SE2017"],
            "index": 2,
        },{
            "models": ["CUE01", "KM32-4K"],
            "index": 3,
        },{
            "models": ["HVS041E"],
            "index": 4,
        }
    ]

    @staticmethod
    def get_udp_model_index(model):
        for item in ModelPreferences._udp_model_index_map:
            if model in item["models"]:
                return item["index"]
        
        return 0xff

    @staticmethod
    def get_color_space_list():
        return ModelPreferences._color_space_list
    
    @staticmethod
    def get_color_space_by_index(index):
        if index >= len(ModelPreferences._color_space_list):
            return "Unknow"
        
        return ModelPreferences._color_space_list[index]

    @staticmethod
    def get_product_type_by_index(index):
        if index >= len(ModelPreferences._product_type):
            return "Unknow"
        
        return ModelPreferences._product_type[index]
    
    @staticmethod
    def get_mcu_mode_by_index(index):
        if index >= len(ModelPreferences._mcu_mode):
            return "Unknow"
        
        return ModelPreferences._mcu_mode[index]

    @staticmethod
    def sc_handle_version_info(args): # 处理USB类设备的版本信息
        logging.debug("args:{}".format(args))

        _args = {
            "function": "get_version_info",
            "args": {
                "ProtocolVersion": args[8:10],
                "MCUMode": args[10],
                "BootVersion": args[12:16],
                "APPVersion": args[16:20],
                "FPGAVersion": args[20:24],
                "HardwareVersion": args[24:28]
            }
        }
        return _args

    @staticmethod
    def byte_to_binary_list(byte_value):
        # 检查输入是否为16进制整数
        if isinstance(byte_value, int) and byte_value < 0:
            try:
                byte_value = int(hex(byte_value), 16)
            except:
                logging.error("此参数值必须是0到255之间的整数或有效的16进制整数")
        
        # 确保输入是一个字节
        if not isinstance(byte_value, int) or byte_value < 0 or byte_value > 255:
            logging.error("此参数值必须是0到255之间的整数或有效的16进制整数！")
        
        # 将字节转换为二进制列表
        binary_list = [(byte_value >> i) & 1 for i in range(8)]
        logging.debug("byte_value:{}, binary_list:{}".format(byte_value, binary_list))
        return binary_list

import time
class ModelContinuousTask(object):
    def __init__(self, action_handle) -> None:
        self._action_handle = action_handle

        self._task_queue = queue.Queue()
        start_new_thread(self._do_continuous_task_thread, (self._task_queue,))

        self._task_lock = threading.Lock()
        self._is_running = False
        self._data_list = []

    def do_current_task(self, action, task):
        with self._task_lock:
            now = time.time()
            timeout_data_list = [x for x in self._data_list if (now - x['time'] > 1.0)]
            if len(timeout_data_list) > 0: # 存在超时的数据，表明有报文没有回应，应该清理掉所有数据
                self._data_list.clear()
                self._is_running = False # 此时应该认为持续发送的任务已经停止

            if self._is_running:
                data = {
                    "action": action,
                    "time": time.time(),
                    "task":task
                }
                self._data_list.append(data)
            else: # 直接触发task
                self._is_running = True
                self._task_queue.put(task)

    def do_next_task(self, action):
        with self._task_lock:
            data_list = [x for x in self._data_list if x['action'] == action]
            self._data_list = [x for x in self._data_list if x['action'] != action]

            while len(data_list) > 1:
                task = data_list.pop(0)["task"]
                logging.debug("Drop task args:{}".format(task["args"]))

            if len(data_list) > 0:
                task = data_list.pop(0)["task"]
                logging.debug("Handle task args:{}".format(task["args"]))
                self._task_queue.put(task)
                # logging.debug("After handle task, data's length:{}".format(len(data_list)))
            elif len(self._data_list) == 0: # data_list为空，代表是该action的最后一个回应，同时整个持续发送的数据已经被全部发送完毕，才能代表running结束
                self._is_running = False
            else: # data_list为空，self._data_list不为空，代表有不同的action在排队等待执行
                other_task = self._data_list.pop(0)["task"]
                logging.debug("Start to do other task args:{}".format(other_task["args"]))
                self._task_queue.put(other_task)

    def _do_continuous_task_thread(self, task_queue):
        while True:
            task = task_queue.get()  # 从队列中获取任务
            if task is None:  # 如果任务是None，表示结束信号
                break
            # 执行任务
            try:
                self._action_handle(task)
            except Exception as e:
                logging.error(f"e:{e}")
                logging.error(traceback.format_exc())

            task_queue.task_done()  # 标记任务完成

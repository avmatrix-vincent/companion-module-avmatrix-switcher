import threading  
from PySide6.QtCore import QObject, Signal
import logging
  
class AvmNotice(QObject):  
    __dispatch_sig = Signal(object)

    def __init__(self):  
        super(AvmNotice, self).__init__()
        self.listeners = {}  
        self.lock = threading.Lock()  # 创建一个锁对象用于同步  
        self.__dispatch_sig.connect(self._handle_dispatch_signal)
  
    def register(self, message_type, callback):  
        with self.lock:  # 使用锁来确保注册操作的线程安全性  
            if message_type not in self.listeners:  
                self.listeners[message_type] = []  
            self.listeners[message_type].append(callback)  

        # logging.debug("listeners: {}".format(self.listeners))
  
    def unregister(self, message_type, callback):  
        with self.lock:  # 使用锁来确保取消注册操作的线程安全性  
            if message_type in self.listeners:  
                self.listeners[message_type].remove(callback)  
  
    def dispatch(self, args):  
        logging.debug("args: {}".format(args))
        self.__dispatch_sig.emit(args)
    
    def _handle_dispatch_signal(self, args):
        message_type = args["message_type"]
        message = args["message"]

        with self.lock:  # 使用锁来确保分发操作的线程安全性  
            if message_type in self.listeners:  
                listeners = self.listeners[message_type]  
            else:  
                listeners = []  
  
        # 释放锁之后调用回调，避免在回调执行期间占用锁  
        for callback in listeners:  
            callback(message)

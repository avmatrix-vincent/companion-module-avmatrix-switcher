import logging
import traceback
from functools import wraps
from collections import defaultdict
from PySide6.QtCore import QObject, QThread, QTimer, QWaitCondition, QMutex, Signal
from globals import FILTER_CMD_LIST

class CommandBatcherThread(QThread):
    def __init__(self):
        super().__init__()
        self.command_batcher = CommandBatcher()

    def run(self):
        self.command_batcher.handle_batch_commands()

    def stop(self):
        self.command_batcher.thread_running = False

    def trigger_send(self):
        self.command_batcher.trigger_send_signal.emit()

class CommandBatcher(QObject):

    trigger_send_signal = Signal()

    def __init__(self):
        super().__init__()
        self.command_batches = defaultdict(list)
        self.lock = QMutex()
        self.wait_condition = QWaitCondition()
        self.current_cmd = ""
        self.current_sn = ""
        self.timer = QTimer()
        self.timer.timeout.connect(self._handle_missing_commands)
        self.timer_interval = 2000  # 2秒，单位是毫秒
        self.dont_go_ahead = True # 是否进入wait()的标志
        self.thread_running = False
        self.handle_batch_commands_thread = QThread()
        self.moveToThread(self.handle_batch_commands_thread)
        self.handle_batch_commands_thread.started.connect(self.handle_batch_commands)
        self.trigger_send_signal.connect(self.trigger_send)

    # 过滤批量指令的装饰器
    def filter_batch_wrapper(self, func):
        @wraps(func)
        def wrapper(dev_sn, cmd, data, callback):
            if cmd not in FILTER_CMD_LIST:
                func(dev_sn, cmd, data, callback)
            else:
                with self.lock:
                    self.current_sn = dev_sn
                    self.current_cmd = cmd
                    self.command_batches[(cmd, dev_sn)].append((func, data, callback))
                    if not self.thread_running:
                        self.thread_running = True
                        self.handle_batch_commands_thread.start()
                    if self.timer.isActive():
                        self.timer.stop()
                    if len(self.command_batches[(cmd, dev_sn)]) == 1:
                        func(dev_sn, cmd, data, callback)
                    else:
                        self.dont_go_ahead = False
                        logging.info(f">>> 当前批量指令长度为 {len(self.command_batches[(self.current_cmd, self.current_sn)])}")
                        logging.info(">>> 等待上一条指令发送的回复处理之后，发送当前批量的最后一条指令")
            return wrapper

    def handle_batch_commands(self):
        while self.thread_running:
            if self.dont_go_ahead: 
                continue
            with self.lock:
                self.wait_condition.wait(self.lock)
                if not self.command_batches[(self.current_cmd, self.current_sn)]:
                    continue
                func, data, callback = self.command_batches[(self.current_cmd, self.current_sn)][-1]
                func(self.current_sn, self.current_cmd, data, callback)
                logging.info(f">>>>> 已发送当前批量指令的最后一条, sn={self.current_sn}, cmd={self.current_cmd}")
                self.command_batches.pop((self.current_cmd, self.current_sn))
                self.dont_go_ahead = True
                if not self.timer.isActive():
                    self.timer.start(self.timer_interval)
                self.wait_condition.wakeAll()

    def trigger_send(self):
        # self.dont_go_ahead = False
        self.wait_condition.wakeAll()

    def stop(self):
        self.thread_running = False
        self.wait_condition.wakeAll()
        if self.timer.isActive():
            self.timer.stop()
        self.command_batches.clear()

    def _handle_missing_commands(self):
        for k, v in self.command_batches.items():
            if len(v) > 2:
                continue
            logging.info(f">>> 发现残留指令未发送, {k}, {v}")
            try:
                for args in v:
                    dev_sn, cmd = k
                    func, data, callback = args
                    func(dev_sn, cmd, data, callback)
                    logging.info(f"已发送设备{dev_sn}的 cmd={cmd}，data={data} 残留指令")
            except:
                logging.error("处理残留指令出错！")
                logging.error(traceback.format_exc())

# 示例用法
if __name__ == "__main__":
    import sys
    from PySide6.QtCore import QCoreApplication
    
    app = QCoreApplication(sys.argv)
    command_batcher = CommandBatcher()

    # 你可以在这里进行一些触发事件的操作，来测试 CommandBatcher 的功能
    command_batcher.trigger_send()

    sys.exit(app.exec())

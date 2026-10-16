import logging
from PySide6.QtCore import QObject, QTimer, Signal

class HeartbeatManager(QObject):
    connection_lost = Signal()  # 用于通知连接已断开的信号

    def __init__(self, args, send_heartbeat_callback, interval=5000, max_missed=3):
        super().__init__()
        self.args = args
        self.send_heartbeat_callback = send_heartbeat_callback # 发送指令的具体函数，来自外部
        self.interval = interval*10 # 心跳发送间隔（毫秒）
        self.max_missed = max_missed # 最大未回复次数
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.send_heartbeat)

        self.missed_count = 0 # 设备未回复次数

    # 开始发送心跳包，设备激活（选中）时触发
    def start(self):
        # return
        if not self.timer.isActive() and self.send_heartbeat_callback is not None:
            self.timer.start(self.interval)
            logging.debug(f">>> Device {self.args['name']} start heartbeat")

    # 停止发送心跳包，设备删除或断开连接时触发
    def stop(self):
        # return
        if self.timer.isActive():
            self.timer.stop()
            logging.debug(f">>> Device {self.args['name']} stop heartbeat")

    # 重启心跳发送，用于其他指令发送后触发
    def reset(self):
        # return
        self.missed_count = 0
        if self.timer.isActive():
            self.timer.stop()
        self.timer.start(self.interval)
        logging.debug(f">>> Device {self.args['name']} reset heartbeat")

    # 计时器定时调用此方法处理发送心跳包和判断设备是否回复并处理
    def send_heartbeat(self):
        # return
        if self.send_heartbeat_callback is None:
            return
        self.send_heartbeat_callback(self.args) # 调用接口发送心跳指令，并得到回复结果
        self.missed_count += 1 # 未回复次数加一
        if self.missed_count >= self.max_missed: # 当次数=3时已经是第四次发送
            self.stop()
            logging.debug(f">>> Device {self.args['name']} has been disconnected")
            self.connection_lost.emit() # 通知 断开连接

    # 收到设备回复
    def receive_heartbeat(self):
        # return
        # 收到设备回复
        self.missed_count = 0 # 重置未回复次数
        logging.debug(f">>> Device {self.args['name']} received heartbeat")

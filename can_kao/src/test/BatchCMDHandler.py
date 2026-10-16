import threading
import logging
import traceback
from functools import wraps
from collections import defaultdict
from globals import FILTER_CMD_LIST

class CommandBatcher:
    def __init__(self):
        self.command_batches = defaultdict(list)
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.current_cmd = ""
        self.current_sn = ""
        self.wait_count = 0 # 需要阻塞的次数
        self.timer = None # 判断是否有残余未执行指令的定时器
        self.timer_interval = 2 # 判断间隔 2 秒
        self.go_ahead = False # 阻塞等待下方的代码是否需要执行的标志
        self.thread_running = False # 
        self.handle_batch_commands_thread = threading.Thread(target=self.handle_batch_commands)

    # 过滤批量指令的装饰器
    def filter_batch_wrapper(self, func):
        @wraps(func)
        def wrapper(dev_sn, cmd, data, callback):
            if cmd not in FILTER_CMD_LIST: # 不在需要过滤的cmd列表中的，直接执行
                func(dev_sn, cmd, data, callback)
            else:
                with self.lock:
                    logging.info(f">>> 新指令进入装饰器 cmd={cmd:#x},sn={dev_sn},data={data}")
                    self.command_batches[(cmd, dev_sn)].append((func, data, callback))
                    ''' 只 start 一次 '''
                    if not self.thread_running: # 
                        logging.info("============================ 开启批量收集指令线程 =================================")
                        self.thread_running = True
                        self.handle_batch_commands_thread.start()
                    if self.timer: # 因有新的指令进来，暂停定时器检查残余指令
                        self.timer.cancel()
                    if len(self.command_batches[(cmd, dev_sn)]) == 1:   # 当前cmd和sn对应只有单个指令，直接执行
                        # 发送第一个指令
                        logging.info(f">>>>>>>> < 直接发送 > 当前cmd第一条指令  cmd={cmd:#x}, data={data}, sn={dev_sn}")
                        func(dev_sn, cmd, data, callback)
                    else: # 当前cmd和sn对应有大于1个指令，阻塞等待
                        if len(self.command_batches[(cmd, dev_sn)]) == 2: 
                            self.wait_count += 1 # 同一个sn和cmd的指令数量等于2条时 才增加一次阻塞！
                        logging.info(f">>> 当前cmd={cmd:#x},sn={dev_sn}的批量指令数量为 {len(self.command_batches[(cmd, dev_sn)])}")
                        logging.info(">>> 等待上一条指令发送的回复处理之后再发送当前批量的最后一条指令")
        return wrapper

    def handle_batch_commands(self):
        while self.thread_running: # 保持此方法线程运行的标志
            with self.condition:
                while self.wait_count > 0: 
                    logging.info("|||||||||||||||||||||||||||||||||| 程序阻塞 |||||||||||||||||||||||||||||||||||||")
                    self.condition.wait() # 阻塞当前指令发送
                    ''' 被 notify() 通知 condition 停止阻塞，发送当前批量指令的最后一条指令 '''
                    logging.info("》》》》》》》》》》》》》》》》》》 停止阻塞，继续执行下方代码 》》》》》》》》》》》》》》》》》》")
                    if self.wait_count > 0: self.wait_count -= 1
                    print("wait_count =", self.wait_count)
                    if (self.current_cmd, self.current_sn) not in self.command_batches: continue
                    if len(self.command_batches[(self.current_cmd, self.current_sn)]) != 0:
                        func, data, callback = self.command_batches[(self.current_cmd, self.current_sn)].pop()
                        func(self.current_sn, self.current_cmd, data, callback)
                        logging.info(f">>>>>>>> < 已发送 > 当前批量指令的最后一条, sn={self.current_sn}, cmd={self.current_cmd:#x}, data={data}")
                    else:
                        logging.info(f">>> cmd={self.current_cmd:#x}, sn={self.current_sn}的data和callback为空")
                    del self.command_batches[(self.current_cmd, self.current_sn)]

    def trigger_send(self, dev_sn, cmd):
        # 在外部（回复了上一条指令后）触发发送当前队列中的最后一条指令
        self.current_cmd = cmd
        self.current_sn = dev_sn
        if (cmd, dev_sn) not in self.command_batches: 
            logging.info(f">>> cmd：{cmd:#x} 不在字典中，已无指令需要再发送")
            return
        if len(self.command_batches[(cmd, dev_sn)]) > 0:
            logging.info(f"》》》 cmd：{cmd:#x} 通知发送当前批量指令中的最后一条") # 已收到并处理上次发送的回复结果
            with self.condition:
                self.condition.notify()

    def stop(self):
        self.wait_count = -1
        with self.condition:
            self.condition.notify_all()
        self.thread_running = False
        if self.timer:
            self.timer.cancel()
        self.command_batches.clear()

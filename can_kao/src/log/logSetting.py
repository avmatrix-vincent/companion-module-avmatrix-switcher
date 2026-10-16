import logging, os, sys


class LogSetting(object):
    @staticmethod
    def config(filename=None, level=logging.WARNING):
        log_format = "[%(asctime)s] - %(levelname)s - [%(funcName)s: %(filename)s, %(lineno)d] %(message)s"
        # 检查日志文件行数，超过10000行则先清空
        if os.path.exists(filename):
            with open(filename, 'r', encoding="utf-8") as f:
                lines = f.readlines()
                if len(lines) >= 10000:
                    # 清空日志文件
                    with open(filename, 'w') as f:
                        f.truncate()
        try:
            logging.basicConfig(filename=filename, level=level, format=log_format, encoding="utf-8")
        except:
            # Mac系统日志放桌面，可能避免权限问题，windows出错也尝试这种做法
            home_dir = os.path.expanduser('~') # 获取用户的主目录
            filename = os.path.join(home_dir, 'Desktop', filename) # 拼接桌面路径和文件
            logging.basicConfig(filename=filename, level=level, format=log_format, encoding="utf-8")


    @staticmethod
    def welcome():
        logging.warning('==================================================')
        logging.warning('++++++++ Welcome to AVM Config Tools Log ++++++++++')
        logging.warning('==================================================')

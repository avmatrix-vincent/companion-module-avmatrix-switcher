import os, logging
import tempfile
import socket

# 通知已存在的进程显示在前面
def bring_existing_instance_to_front():
    logging.debug("Bringing the existing instance to front...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(("localhost", 9999))
            s.sendall(b"show")
            logging.info("Message sent to the existing instance.")
        except ConnectionRefusedError:
            logging.error("Failed to connect to the existing instance.")

class WindowsInstanceChecker:
    def __init__(self):
        self.lock_file = os.path.join(tempfile.gettempdir(), "app.lock")
        self.lock = None

    def is_instance_running(self):
        try:
            if os.path.exists(self.lock_file):
                os.remove(self.lock_file)
            self.lock = open(self.lock_file, "w")
            import msvcrt
            msvcrt.locking(self.lock.fileno(), msvcrt.LK_NBLCK, 1)
            logging.debug("No other instance running. Lock file created.")
            return False
        except OSError:
            logging.info("Another instance is already running.")
            return True

    def release_lock(self):
        if self.lock:
            import msvcrt
            msvcrt.locking(self.lock.fileno(), msvcrt.LK_UNLCK, 1)
            self.lock.close()
            os.remove(self.lock_file)

class UnixInstanceChecker:
    def __init__(self):
        self.lock_file = os.path.join(tempfile.gettempdir(), "app.lock")
        self.lock = None

    def is_instance_running(self):
        try:
            self.lock = open(self.lock_file, "w")
            import fcntl
            fcntl.flock(self.lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            logging.debug("No other instance running. Lock file created.")
            return False
        except IOError:
            logging.info("Another instance is already running.")
            return True

    def release_lock(self):
        if self.lock:
            import fcntl
            fcntl.flock(self.lock, fcntl.LOCK_UN)
            self.lock.close()
            os.remove(self.lock_file)

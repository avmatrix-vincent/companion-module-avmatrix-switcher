from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from src.avm_stack.heartbeat import HeartbeatManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Heartbeat Example")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        self.label = QLabel("Status: Connected")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.heartbeat_manager = HeartbeatManager(self.send_heartbeat)
        self.heartbeat_manager.connection_lost.connect(self.handle_connection_lost)

        self.start_button = QPushButton("Start Heartbeat")
        self.start_button.clicked.connect(self.start_heartbeat)
        self.layout.addWidget(self.start_button)

        self.reset_button = QPushButton("Reset Heartbeat")
        self.reset_button.clicked.connect(self.reset_heartbeat)
        self.layout.addWidget(self.reset_button)

    def send_heartbeat(self):
        print("Sending heartbeat...")
        # 在这里调用发送接口发送心跳包，接收心跳回复，返回给心跳包类判断
        result = self.send_heartbeat_callback()
        return result

    def handle_connection_lost(self):
        self.label.setText("Status: Disconnected")
        print("Connection lost!")

    def start_heartbeat(self):
        self.heartbeat_manager.start()
        self.label.setText("Status: Connected")
        print("Heartbeat started.")

    def reset_heartbeat(self):
        self.heartbeat_manager.reset()
        self.label.setText("Status: Connected")
        print("Heartbeat reset.")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

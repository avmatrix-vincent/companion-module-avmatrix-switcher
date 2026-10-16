import sys
from PySide6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget
from PySide6.QtCore import QSignalBlocker

class CustomComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        
    # 重写此方法，以保证每此打开下拉列表能选中且定位到当前项
    def showPopup(self):
        # Call the original showPopup method
        super().showPopup()
        # Ensure the current selected item is visible
        index = self.currentIndex()
        with QSignalBlocker(self):
            self.view().setCurrentIndex(self.model().index(index, 0))
            self.view().scrollTo(self.model().index(index, 0))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.comboBox_output_resolution = CustomComboBox(self)
        self.comboBox_output_resolution.addItems(["Option 1", "Option 2", "Option 3", "Option 4", "Option 1", "Option 2", "Option 3", "Option 4", "Option 1", "Option 2", "Option 3", "Option 4"])
        self.comboBox_output_resolution.setCurrentIndex(8)
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox_output_resolution)
        self.setLayout(layout)
        
        # Set the showPopup method to our custom implementation
        self.comboBox_output_resolution.showPopup = self.comboBox_output_resolution.showPopup

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

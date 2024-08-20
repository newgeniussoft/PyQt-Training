import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        layout = QVBoxLayout()
        label = QLabel("This is the second window")
        layout.addWidget(label)
        self.setLayout(layout)
        self.resize(300, 200)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(400, 300)

        # Button to open the second window
        self.open_button = QPushButton("Open Second Window")
        self.open_button.clicked.connect(self.open_second_window)

        # Set up the layout for the main window
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.open_button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

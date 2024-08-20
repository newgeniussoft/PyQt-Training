import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import os

class WebView(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the title and size of the window
        self.setWindowTitle('PyQt WebView Example')
        self.setGeometry(100, 100, 800, 600)

        # Create a QWebEngineView object
        self.browser = QWebEngineView()

        # Get the path to the local HTML file
        file_path = os.path.join(os.path.dirname(__file__), 'index.html')
        file_url = QUrl.fromLocalFile(file_path)

        # Set the URL to load the local HTML file
        self.browser.setUrl(file_url)

        # Set the central widget of the window
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebView()
    window.show()
    sys.exit(app.exec_())

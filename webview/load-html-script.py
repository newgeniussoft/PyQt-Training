from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        
        # HTML content as a string
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Page</title>
            <style>
                body { font-family: Arial, sans-serif; }
                h1 { color: #4CAF50; }
            </style>
        </head>
        <body>
            <h1>Hello, PyQt5!</h1>
            <p>This is a sample HTML string loaded into QWebEngineView.</p>
        </body>
        </html>
        """
        
        # Load the HTML string into the QWebEngineView
        self.browser.setHtml(html_content)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

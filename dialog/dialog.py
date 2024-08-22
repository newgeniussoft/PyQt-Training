import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebViewDialog(QDialog):
    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Web View Dialog")
        self.setGeometry(100, 100, 800, 600)  # Set the initial size of the dialog
        
        # Create layout
        layout = QVBoxLayout()
        
        # Create QWebEngineView
        self.web_view = QWebEngineView()
        
        # Load a URL
        self.web_view.setUrl(url)
        
        # Create buttons
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        
        # Add widgets to layout
        layout.addWidget(self.web_view)
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)
        
        # Set layout for the dialog
        self.setLayout(layout)
        
        # Connect button signals to slots
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

def main():
    app = QApplication(sys.argv)
    
    # Create and show web view dialog
    url = "https://www.google.com"  # Change this to the URL you want to load
    dialog = WebViewDialog(url)
    
    if dialog.exec_() == QDialog.Accepted:
        print("Dialog accepted")
    else:
        print("Dialog canceled")
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

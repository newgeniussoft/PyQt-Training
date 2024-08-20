import sys
import os
from PyQt5 import QtCore, QtWidgets, QtPrintSupport, QtWebEngineWidgets

class WebPrinterApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Print Web Page Example')
        self.setGeometry(100, 100, 800, 600)
        
        # Initialize QWebEngineView for preview
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.browser)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Create a QWebEnginePage and set its content
        html_content = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Page</title>
            <style>
                body { font-family: Arial, sans-serif; }
                h1 { color: #4CAF50; }
                table, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
            </style>
        </head>
        <body>
            <h1>Hello, PyQt5!</h1>
            <p>This is a sample HTML string loaded into QWebEngineView.</p>
            <img src="img/Python-Logo.png" alt="logo" width="280">
            <table>
                <tr>
                    <td>Name</td>
                    <td>Lastname</td>
                    <td>Age</td>
                </tr>
                <tr>
                    <td>Georginot</td>
                    <td>Armelin</td>
                    <td>12</td>
                </tr>
            </table>
        </body>
        </html>
        '''
        self.browser.setHtml(html_content, QtCore.QUrl.fromLocalFile(os.path.join(current_dir, "public/index.html")))
        # Show the preview
        self.browser.show()

        # Add a print action to the menu
        print_action = QtWidgets.QAction('Print', self)
        print_action.triggered.connect(self.show_print_dialog)
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(print_action)



    def show_print_dialog(self):
        # Configure the printer
        self._printer = QtPrintSupport.QPrinter()
        self._printer.setPaperSize(QtCore.QSizeF(80, 297), QtPrintSupport.QPrinter.Millimeter)
        self._printer.setResolution(300)

        # Create and show the print dialog
        print_dialog = QtPrintSupport.QPrintDialog(self._printer, self)
        if print_dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.browser.page().print(self._printer, self.print_completed)

    def print_completed(self, result):
        if result:
            QtWidgets.QMessageBox.information(self, 'Print', 'Print job completed successfully.')
        else:
            QtWidgets.QMessageBox.warning(self, 'Print', 'Print job failed.')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = WebPrinterApp()
    window.show()
    sys.exit(app.exec_())

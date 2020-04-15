from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets 
import sys 
import requests
  
class Main(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DNV PoC')

        self.webView = QtWebEngineWidgets.QWebEngineView()

        self.webView.setHtml("Not clicked")

        self.testButton = QtWidgets.QPushButton('Test', self)
        self.testButton.resize(self.testButton.sizeHint())
        self.testButton.clicked.connect(self.testButton_clicked)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.testButton)
        lay.addWidget(self.webView)

    def testButton_clicked(self):
        try:
            r = requests.get('http://127.0.0.1:5000/status')
            self.webView.setHtml(r.json()['status'])
        except:
            self.webView.setHtml("404")

app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
app.exec_()

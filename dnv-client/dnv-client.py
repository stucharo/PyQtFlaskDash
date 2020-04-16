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

        self.demoButton1 = QtWidgets.QPushButton('Demo 1', self)
        self.demoButton2 = QtWidgets.QPushButton('Demo 2', self)
        self.demoButton1.resize(self.demoButton1.sizeHint())
        self.demoButton2.resize(self.demoButton2.sizeHint())
        self.demoButton1.clicked.connect(self.demoButton1_clicked)
        self.demoButton2.clicked.connect(self.demoButton2_clicked)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.demoButton1)
        lay.addWidget(self.demoButton2)
        lay.addWidget(self.webView)

    def demoButton1_clicked(self):
        self.webView.load(QtCore.QUrl('http://127.0.0.1:5000/demo1/'))

    def demoButton2_clicked(self):
        self.webView.load(QtCore.QUrl('http://127.0.0.1:5000/demo2/'))

app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
app.exec_()
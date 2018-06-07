import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMdiArea,QMdiSubWindow, QTextEdit, QTabBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Example(QMainWindow):

    def __init__(self, parent=parent):
        super().__init__(self,parent)
        screen_resolution = app.desktop().screenGeometry()
        width,height = screen_resolution.width(), screen_resolution.height()

        self.initUI()


    def initUI(self):

        self.statusBar().showMessage('Ready')


        self.btn = QPushButton("Button",self)
        self.btn.setToolTip("Test Button")
        self.btn.setIcon(QIcon("/home/hsa/PycharmProjects/test12/home-6x.png"))
        #btn.setIconSize(QSize(24,24))
        self.btn.move(50,50)
        self.btn.clicked.connect(self.on_clicked)

        self.setGeometry(0,0, width, height)
        self.setWindowTitle('MainWindow')
        #self.mysubwindow()

    def mysubwindow (self):
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.sub = QMdiSubWindow()
        self.sub.setGeometry(10,10,width-30, height-100)
        self.tabbar = QTabBar()
        self.sub.setWidget(self.tabbar)
        self.tabbar.addTab("Test1")
        self.tabbar.addTab("Test2")
        self.sub.setWindowTitle("subwindow")
        self.mdi.addSubWindow(self.sub)
        self.sub.show()


    @pyqtSlot()
    def on_clicked(self):
        print("Button clicked")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

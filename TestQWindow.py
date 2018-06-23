import sys
from PyQt5 import QtGui, QtWidgets, QtCore

class AnaPencere(QtWidgets.QMainWindow):
    def __init__(self, ):
        super ().__init__()
        self.setup_UIMain()

    def setup_UIMain(self):

        bar = QtWidgets.QMenuBar(self)
        file = bar.addMenu("&File")
        file.addAction("show")
        file.addAction("add")
        file.addAction("remove")
        file.addAction("Save")
        file.addAction("&Delete")
        file.addSeparator()
        file.addAction("&Close")
        file.triggered[QtWidgets.QAction].connect(self.processtrigger)

        about = bar.addMenu("About")

        self.qw = QtWidgets.QWidget(self)
        self.qw.setGeometry(10, 1, 700, 100)
        self.hlayout = QtWidgets.QHBoxLayout(self.qw)

        self.pb1 = QtWidgets.QPushButton(self)
        self.pb1.setText("Add Window1")
        self.pb1.clicked.connect(self.btn1_act)

        self.pb2 = QtWidgets.QPushButton(self)
        self.pb2.setText("Add Window2")
        self.pb2.clicked.connect(self.btn2_act)

        self.pb3 = QtWidgets.QPushButton(self)
        self.pb3.setText("Add Window3")
        self.pb3.clicked.connect(self.btn3_act)

        self.pb4 = QtWidgets.QPushButton(self)
        self.pb4.setText("Tile Window")
        self.pb4.clicked.connect(self.btn4_act)

        self.pb5 = QtWidgets.QPushButton(self)
        self.pb5.setText("Cascade Window")
        self.pb5.clicked.connect(self.btn5_act)

        #self.hlayout.addStretch(1)
        self.hlayout.addWidget(self.pb1)
        self.hlayout.addWidget(self.pb2)
        self.hlayout.addWidget(self.pb3)
        self.hlayout.addWidget(self.pb4)
        self.hlayout.addWidget(self.pb5)

        self.setLayout(self.hlayout)

        self.setGeometry(10, 10, 1200, 600)
        self.statusBar = QtWidgets.QStatusBar()
        self.setWindowTitle("Main Window")

        self.setStatusBar(self.statusBar)
        self.b = QtWidgets.QPushButton("click here")

    def btn1_act(self):

        self.mdiArea.addSubWindow(self)

        #self.wgt = QtWidgets.QMdiSubWindow(self)
        #self.wgt.setWindowTitle("Sub Window-1")
        #self.wgt.setGeometry(10, 70, 500, 500)
        #self.wgt.show()
    def btn2_act(self):
        self.wgt = QtWidgets.QMdiSubWindow(self)
        self.wgt.setWindowTitle("Sub Window-2")
        self.wgt.setGeometry(510, 70, 500, 500)
        self.wgt.show()
    def btn3_act(self):
        self.wgt = QtWidgets.QMdiSubWindow(self)
        self.wgt.setWindowTitle("Sub Window-3")
        self.wgt.setGeometry(1010, 70, 500, 500)
        self.wgt.show()

    #self.mdiArea = QtWidgets.QMdiArea()
    #self.setCentralWidget(self.mdiArea)

    def btn4_act(self):

        self.wgt = QtWidgets.QMdiSubWindow(self)
        self.wgt.setWindowTitle("Sub Window-1")
        self.wgt.setGeometry(1010, 70, 500, 500)
        self.wgt.show()


    def btn5_act(self):
        self.wgt = QtWidgets.QMdiSubWindow(self)
        self.wgt.setWindowTitle("Sub Window-3")
        self.wgt.setGeometry(1010, 70, 500, 500)
        self.wgt.show()

    def processtrigger(self, q):

        if q.text() == "show":

            self.statusBar.showMessage(q.text() + " is clicked", 2000)

        if q.text() == "add":
            self.statusBar.addWidget(self.b)

        if q.text() == "remove":
            self.statusBar.removeWidget(self.b)
            self.statusBar.show()
        if q.text() == "Close":
                pass
            #buttonReply = QtWidgets.QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?",
                                                        # QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            #msgBox = QtWidgets.QMessageBox()
            #msgBox.setWindowTitle("Closing application")
            #msgBox.text("Are you sure you want to quit?")
            #msgBox.addButton(self, QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)

            #self.QtGui.QGuiApplication.quit()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.QtGui.QGuiApplication.quit()


def anaProg():
    Anaprg = QtWidgets.QApplication(sys.argv)
    anapencere = AnaPencere()
    anapencere.show()
    sys.exit(Anaprg.exec_())


if __name__== "__main__":
    anaProg()
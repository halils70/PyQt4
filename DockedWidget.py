import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        widget1 = QtGui.QDockWidget("Page 1")
        widget1.setWidget(QtGui.QLabel("Page 1"))
        widget2 = QtGui.QDockWidget("Page 2")
        widget2.setWidget(QtGui.QLabel("Page 2"))
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, widget1)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, widget2)

        btn1 = QtGui.QPushButton("Page 1")
        btn1.setCheckable(True)
        btn1.setChecked(True)
        btn1.toggled.connect(widget1.setShown)
        widget1.visibilityChanged.connect(btn1.setChecked)
        btn2 = QtGui.QPushButton("Page 2")
        btn2.setCheckable(True)
        btn2.setChecked(True)
        btn2.toggled.connect(widget2.setShown)
        widget2.visibilityChanged.connect(btn2.setChecked)

        hlayout = QtGui.QHBoxLayout()
        hlayout.addWidget(btn1)
        hlayout.addWidget(btn2)

        widget = QtGui.QWidget()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Window()
    w.show()
sys.exit(app.exec_())
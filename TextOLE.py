import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class Life2Coding(QDialog):
    def __init__(self):
        super(Life2Coding, self).__init__()
        loadUi("life2coding.ui",self)
        self.setWindowTitle("Deneme Sayfası")
        self.pushButton.clicked.connect(self.on_pushbuttonclicked)

    #@pyqtSlot()
    def on_pushbuttonclicked (self):
        self.label_1.setText("Welcome: "+self.lineEdit.text())


class main:
    app = QApplication(sys.argv)
    widget = Life2Coding()
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()






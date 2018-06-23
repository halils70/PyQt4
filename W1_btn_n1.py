# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W1_btn_n1.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName(_fromUtf8("MainWindow1"))
        MainWindow1.resize(796, 593)
        self.centralwidget = QtGui.QWidget(MainWindow1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 551, 381))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayoutWidget = QtGui.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 231))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.formLayoutWidget)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.dateTimeEdit)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(110, 230, 441, 121))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(0, 266, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 291, 192))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow1)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow1", "Name", None))
        self.label_4.setText(_translate("MainWindow1", "Surname", None))
        self.label_5.setText(_translate("MainWindow1", "Customer Number", None))
        self.label_6.setText(_translate("MainWindow1", "Company ", None))
        self.label_7.setText(_translate("MainWindow1", "Description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow1", "Tab 1", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow1", "1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow1", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow1", "Surname", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow1", "Number", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow1", "Tab 2", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow1 = QtGui.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())


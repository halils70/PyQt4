from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


import csv
import sys
from datetime import datetime, timedelta, time
import os

from ci_co_table import *
from login import *

class Ci_Co(QMainWindow):
    """Check in and check out module"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Login(QDialog):
    """User login """
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(lambda: self.handle_login(servers=servers))
        servers = {}
        with open('servers.csv', newline='') as csvfile:
            server_reader = csv.reader(csvfile)
            for row in server_reader:
                self.ui.cbo_db_name.addItem(row[1])
                servers[row[1]] = (row[0],row[2])

    def handle_login(self, servers=''):
        global user
        global pword
        global database
        global server
        global bg_colour
        user = self.ui.username.text()
        pword = self.ui.password.text()
        database = self.ui.cbo_db_name.currentText()
        server = servers[database][0]
        bg_colour = servers[database][1]


if __name__=="__main__":
    app=QApplication(sys.argv)
    global hotdate
    global hotdate_string
    global folio_num
    global user
    global pword
    global dbase
    global server
    pword = ""
    global database
    global bg_colour
    #Login
    while True:
        if Login().exec_() == QDialog.Accepted:
            db = QSqlDatabase.addDatabase("QPSQL");
            db.setHostName(server)
            db.setDatabaseName(database);
            db.setUserName(user);
            db.setPassword(pword)
            if (db.open()==False):     
                QMessageBox.critical(None, "Database Error", db.lastError().text())
            else:
                break
        else:
            #QApplication.quit()
            QCoreApplication.instance().quit()            
            #sys.exit()


    myapp = Ci_Co()
    myapp.show()
    sys.exit(app.exec_())
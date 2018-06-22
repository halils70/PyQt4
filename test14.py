import sys
import PyQt4.QtCore
import PyQt4.QtGui
import PyQt4.uic


class MainWindow(PyQt4.QtGui.QMainWindow):
    count = 0
    win_title = ""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.mdi = PyQt4.QtGui.QMdiArea()
        self.setCentralWidget(self.mdi)
        pix = PyQt4.QtGui.QBrush(PyQt4.QtGui.QPixmap("Death_Valley_Dunes.jpg"))
        self.mdi.setBackground(pix)

        bar = self.menuBar()
        file = bar.addMenu("&Dosya İşlemleri")
        file.addAction("N&ew",self.new_win)
        file.addAction("&Pencereleri Üst Üste Sırala",self.mdi.cascadeSubWindows)
        file.addAction("Pencereleri &Yanyana Sırala ",self.mdi.tileSubWindows)
        file.addSeparator()
        file.addAction("&Çıkış",sys.exit)
        self.setWindowTitle("İşletme Yönetimi")

        about = bar.addMenu("&Yardım")
        about.addAction("&Yardım")
        about.addAction("&Lisans")
        about.addAction("&Yazılım Hakkında",self.about)

        tb = self.addToolBar("File")
        n1_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("icons8-number-1-24.png"), "Cari Hesap Karti", self)
        tb.addAction(n1_tb)
        n1_tb.triggered.connect(self._n1_tb)

        n2_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("icons8-number-2-24.png"), "Stok Karti", self)
        tb.addAction(n2_tb)
        n2_tb.triggered.connect(self._n2_tb)

        n3_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("icons8-3-c-24.png"), "Cari Hesap Harekatlari", self)
        tb.addAction(n3_tb)
        n3_tb.triggered.connect(self._n3_tb)

        n4_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("icons8-number-4-24.png"), "Stok Harekatlari", self)
        tb.addAction(n4_tb)
        n5_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("icons8-5-c-24.png"), "Bankalar", self)
        tb.addAction(n5_tb)
        n6_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("icons8-number-6-24.png"), "Kasa", self)
        tb.addAction(n6_tb)
        n7_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("icons8-7-c-24.png"), "Raporlar", self)
        tb.addAction(n7_tb)
        n8_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("icons8-8-c-24.png"), "Personel", self)
        tb.addAction(n8_tb)
        n9_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("icons8-9-c-24.png"), "Diger", self)
        tb.addAction(n9_tb)

        tb.addSeparator()
        cascadeSubWindows_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("layers-6x.png"), "Pencereleri Üst Üste Sırala", self)
        tb.addAction(cascadeSubWindows_tb)

        tileSubWindows_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("grid-three-up-6x.png"), "Pencereleri Yanyana Sırala", self)
        tb.addAction(tileSubWindows_tb)

        Exit_tb = PyQt4.QtGui.QAction(PyQt4.QtGui.QIcon("x-6x.png"), "Çıkış", self)
        tb.addAction(Exit_tb)

        tb.actionTriggered[PyQt4.QtGui.QAction].connect(self.toolbtnpressed)
        # tb.actionTriggered[QAction].connect(self.toolbtnpressed)
    def _n1_tb(self):
        sub1 = PyQt4.QtGui.QMdiSubWindow()
        sub1.setWidget(PyQt4.QtGui.QWidget(self))
        sub1.setMinimumSize(200, 200)
        sub1.setWindowTitle("Cari Hesap Karti")
        sub1.setWindowIcon(PyQt4.QtGui.QIcon("icons8-capital-50.png"))
        self.mdi.addSubWindow(sub1)
        btn_sub1 = PyQt4.QtGui.QPushButton("Test1", sub1)
        btn_sub1.move(0, 23)
        sub1.show()

    def _n2_tb(self):
        sub2 = PyQt4.QtGui.QMdiSubWindow()
        sub2.setWidget(PyQt4.QtGui.QWidget(self))
        sub2.setMinimumSize(200,200)
        sub2.setWindowTitle("Stok Karti")
        sub2.setWindowIcon(PyQt4.QtGui.QIcon("icons8-product-32.png"))
        self.mdi.addSubWindow(sub2)
        sub2.show()

    def _n3_tb(self):
        pass

    def toolbtnpressed(self, a):
        #print ("pressed tool button is "+a.text())
        if a.text() == "New":
            self.new_win()
        if a.text() == "Pencereleri Üst Üste Sırala":
            self.mdi.cascadeSubWindows()
        if a.text() == "Pencereleri Yanyana Sırala":
            self.mdi.tileSubWindows()
        if a.text() == "Çıkış":
            self.close()

    def new_win(self):

        self.count = self.count+1
        sub = PyQt4.QtGui.QMdiSubWindow()
        sub.setWidget(PyQt4.QtGui.QWidget(self))
        sub.setMinimumSize(200,200)
        sub.setWindowTitle("subwindow-"+str(self.count))
        self.mdi.addSubWindow(sub)
        #sub.showNormal ()

        sub.show()

    def keyPressEvent(self, event):
        if event.key() == PyQt4.QtCore.Qt.Key_Escape:
            self.close()
    def about(self):

        msg = PyQt4.QtGui.QMessageBox(self)
        msg.setIcon(PyQt4.QtGui.QMessageBox.Information)
        msg.setText("Yazılım kullanım lisansı")
        msg.setInformativeText("Bilgi almak için lütfen arayınız.")
        msg.setWindowTitle("Yazılım Hakkında")
        msg.setDetailedText("ABC Firması yazılım lisansına sahiptir.")
        msg.setStandardButtons(PyQt4.QtGui.QMessageBox.Ok)
        msg.show()
        #QMessageBox.about(self, self.tr("Yazılım Hakkında"), self.tr("Bu yazılım "))

class Login(PyQt4.QtGui.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        PyQt4.QtGui.QDialog.__init__(self)
        size = self.size()
        desktopSize = PyQt4.QtGui.QDesktopWidget().screenGeometry()
        top = (desktopSize.height() / 2) - (size.height() / 2)
        left = (desktopSize.width() / 2) - (size.width() / 2)
        self.move(left, top)
        self.resize(250,130)
        self.setWindowTitle("Uygulama Giriş")
        self.textName = PyQt4.QtGui.QLineEdit(self)
        self.textPass = PyQt4.QtGui.QLineEdit(self)
        self.textName.setPlaceholderText("Kullanıcı adınızı yazınız.")
        self.textPass.setPlaceholderText("Şifrenizi yazınız.")
        self.textPass.setEchoMode(PyQt4.QtGui.QLineEdit.Password)

        self.buttonLogin = PyQt4.QtGui.QPushButton('Giriş', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = PyQt4.QtGui.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        self.setFocus()

    def handleLogin(self):
        if (self.textName.text() == '1') and (self.textPass.text() == '1'):
            self.accept()
        else:
            PyQt4.QtGui.QMessageBox.warning(self, 'Uyarı!', 'Kullanıcı adı veya şifre yanlış!')

def main():
    app = PyQt4.QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.setGeometry(10, 10, 1024, 600)
    login = Login()
    ex.show()

    if login.exec_() == PyQt4.QtGui.QDialog.Accepted:
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()

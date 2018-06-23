import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
	count = 0
	win_title = ""
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		pix = QPixmap("Death_Valley_Dunes.jpg")
		l = QLabel()
		l.setPixmap(pix)
		#self.central_widget = QWidget(self.mdi)
		self.setCentralWidget(self.mdi)
		#self.setCentralWidget(l)

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
		n1_tb = QAction(QIcon("icons8-number-1-24.png"),"Cari Hesap Karti",self)
		tb.addAction(n1_tb)
		n1_tb.triggered.connect(self._n1_tb)

		n2_tb = QAction(QIcon("icons8-number-2-24.png"),"Stok Karti",self)
		tb.addAction(n2_tb)
		n2_tb.triggered.connect(self._n2_tb)

		n3_tb = QAction(QIcon("icons8-3-c-24.png"),"Cari Hesap Harekatlari",self)
		tb.addAction(n3_tb)
		n4_tb = QAction(QIcon("icons8-number-4-24.png"),"Stok Harekatlari",self)
		tb.addAction(n4_tb)
		n5_tb = QAction(QIcon("icons8-5-c-24.png"),"Bankalar",self)
		tb.addAction(n5_tb)
		n6_tb = QAction(QIcon("icons8-number-6-24.png"),"Kasa",self)
		tb.addAction(n6_tb)
		n7_tb = QAction(QIcon("icons8-7-c-24.png"),"Raporlar",self)
		tb.addAction(n7_tb)
		n8_tb = QAction(QIcon("icons8-8-c-24.png"),"Personel",self)
		tb.addAction(n8_tb)
		n9_tb = QAction(QIcon("icons8-9-c-24.png"),"Diger",self)
		tb.addAction(n9_tb)

		tb.addSeparator()
		cascadeSubWindows_tb = QAction(QIcon("layers-6x.png"),"Pencereleri Üst Üste Sırala",self)
		tb.addAction(cascadeSubWindows_tb)

		tileSubWindows_tb = QAction(QIcon("grid-three-up-6x.png"),"Pencereleri Yanyana Sırala",self)
		tb.addAction(tileSubWindows_tb)

		Exit_tb = QAction(QIcon("x-6x.png"),"Çıkış",self)
		tb.addAction(Exit_tb)

		tb.actionTriggered[QAction].connect(self.toolbtnpressed)
		#tb.actionTriggered[QAction].connect(self.toolbtnpressed)
	def _n1_tb(self):
		sub = QMdiSubWindow()
		sub.setWidget(QWidget(self))
		sub.setMinimumSize(200,200)
		sub.setWindowTitle("Cari Hesap Karti")
		self.mdi.addSubWindow(sub)
		btn = QPushButton("Test",self.mdi)
		btn.clicked.connect(self.new_win)
		sub.show()

	def _n2_tb(self):
		sub = QMdiSubWindow()
		sub.setWidget(QWidget(self))
		sub.setMinimumSize(200,200)
		sub.setWindowTitle("Stok Karti")
		self.mdi.addSubWindow(sub)
		sub.show()

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
	      sub = QMdiSubWindow()
	      sub.setWidget(QWidget(self))
	      sub.setMinimumSize(200,200)
	      sub.setWindowTitle("subwindow-"+str(self.count))
	      self.mdi.addSubWindow(sub)
	      #sub.showNormal ()
	      sub.show()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Escape:
			self.close()
	def about(self):
		msg = QMessageBox(self)
		msg.setIcon(QMessageBox.Information)
		msg.setText("Yazılım kullanım lisansı")
		msg.setInformativeText("Bilgi almak için lütfen arayınız.")
		msg.setWindowTitle("Yazılım Hakkında")
		msg.setDetailedText("ABC Firması yazılım lisansına sahiptir.")
		msg.setStandardButtons(QMessageBox.Ok)
		msg.show()
		#QMessageBox.about(self, self.tr("Yazılım Hakkında"), self.tr("Bu yazılım "))

class Login(QDialog):
	def __init__(self, parent=None):
		super(Login, self).__init__(parent)
		#self.setCentralWidget()
		self.setWindowTitle("Uygulama Yetkilendirme")
		self.textName = QLineEdit(self)
		self.textPass = QLineEdit(self)
		self.textName.setPlaceholderText("Kullanıcı adınızı Yazınız.")
		self.textPass.setPlaceholderText("Şifrenizi yazınız.")
		self.textPass.setEchoMode(QLineEdit.Password)

		self.buttonLogin = QPushButton('Giriş', self)
		self.buttonLogin.clicked.connect(self.handleLogin)
		layout = QVBoxLayout(self)
		layout.addWidget(self.textName)
		layout.addWidget(self.textPass)
		layout.addWidget(self.buttonLogin)

	def handleLogin(self):
		if (self.textName.text() == '1' and self.textPass.text() == '1'):
		    self.accept()
		else:
		    QMessageBox.warning(self, 'Uyarı!', 'Kullanıcı adı veya şifre yanlış!')

def main() -> object:
	app = QApplication(sys.argv)
	ex = MainWindow()
	ex.setGeometry(10,10,1024,600)
	#pix = QPixmap("Death_Valley_Dunes.jpg")
	#l = QLabel(ex)
	#l.resize(ex.width(),ex.height())
	#l.setPixmap(pix)
	#ex.setCentralWidget(l)
	ex.show()
	login = Login()
	if login.exec_() == QDialog.Accepted:
		sys.exit(app.exec_())

if __name__ == '__main__':
	main()

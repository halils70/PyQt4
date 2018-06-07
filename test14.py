import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
	count = 0

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.mdi = QMdiArea()
		self.setCentralWidget(self.mdi)
		bar = self.menuBar()
		file = bar.addMenu("&File")
		file.addAction("N&ew",self.new_win)
		file.addAction("&Cascade Windows",self.mdi.cascadeSubWindows)
		file.addAction("&Tile Windows",self.mdi.tileSubWindows)
		file.addSeparator()
		file.addAction("&Quit App.",sys.exit)
		self.setWindowTitle("MDI demo")
		
		about = bar.addMenu("&About")
		about.addAction("&About")
		about.addAction("&Licence")
		
		tb = self.addToolBar("File")
		new_tb = QAction(QIcon("tablet-6x.png"),"New",self)
		tb.addAction(new_tb)
		
		cascadeSubWindows_tb = QAction(QIcon("layers-6x.png"),"Cascade Windows",self)
		tb.addAction(cascadeSubWindows_tb)
		
		tileSubWindows_tb = QAction(QIcon("grid-three-up-6x.png"),"Tile Windows",self)
		tb.addAction(tileSubWindows_tb)
		tb.actionTriggered[QAction].connect(self.toolbtnpressed)
		
	def toolbtnpressed(self,a):
		#print ("pressed tool button is",a.text())
		if a.text() == "New":
			self.new_win()
		if a.text() == "Cascade Windows":
			self.mdi.cascadeSubWindows()
		if a.text() == "Tile Windows":
			self.mdi.tileSubWindows()
	
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
def main():
	app = QApplication(sys.argv)
	ex = MainWindow()
	ex.show()
	sys.exit(app.exec_())
      
if __name__ == '__main__':
	main()

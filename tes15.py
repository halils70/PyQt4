from PyQt4 import QtGui, QtCore 
import sys , os 
import ui_test1, cari_test  

class SeconWindow (QtGui.QDialog, cari_test.Ui_Dialog1):
	def _init_(self):
		super(self._class_,self)._init_()
		
class ExampleApp(QtGui.QMainWindow, ui_test1.Ui_MainWindow):
	
	def __init__(self, parent=None):
		super(ui_test1.Ui_MainWindow, self).__init__(parent)
	
		self.pushButton2.clicked.connect(self.click_secon_win)
		self.setupUi(self)  # This is defined in design.py file automatically
     
	def click_secon_win(self):
		self.Dialog1.show()
		
	def browse_folder(self):
		self.listWidget.clear() # In case there are any existing elements in the list
		directory = QtGui.QFileDialog.getExistingDirectory(self,"Pick a folder")
		if directory: # if user didn't pick a directory don't continue
		    for file_name in os.listdir(directory): 
			    self.listWidget.addItem(file_name)  # add file to the listWidget

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function

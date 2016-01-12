import sys
import os
from PyQt4 import QtGui


class receptorImport(QtGui.QWidget):
	def init(self):
		fname = str(QtGui.QFileDialog.getOpenFileName(self, 'Open file','/home',"PDBQT (*.pdbqt)"))
		os.system("cp "+fname+" resources/receptor/")
		fname=fname[fname.rindex('/')+1:]
		return fname
		
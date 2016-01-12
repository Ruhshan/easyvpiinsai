import sys
import os
from PyQt4 import QtGui


class receptorImport(QtGui.QWidget):
	def init(self):
		fname = str(QtGui.QFileDialog.getOpenFileName(self, 'Open Receptor','/home',"PDBQT (*.pdbqt)"))
		os.system("mkdir resources/receptor")
		os.system("cp "+fname+" resources/receptor/")
		fname=fname[fname.rindex('/')+1:]
		return fname

class ligandsImport(QtGui.QWidget):
	def init(self):
		os.system("mkdir resources/ligands")
		paths=[]
		names=[]
		for path in QtGui.QFileDialog.getOpenFileNames(self, "Open Ligands","/home","PDBQT (*.pdbqt)"):
			paths.append(str(path))
		
		for path in paths:
			os.system("cp "+path+" resources/ligands")
			name=path[path.rindex('/')+1:]
			names.append(name)
		return names
		
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easy.ui'
#
# Created: Mon Jan 11 01:14:04 2016
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!
import os,time
from PyQt4 import QtCore, QtGui
from importer import receptorImport,ligandsImport
from configman import ConfigManager
from docker import Docker

from PyQt4.QtCore import QThread, SIGNAL

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s
message="<html><head/><body><p style=font-size:12px>Welcome to EasyVina!</p></body></html>"
class Ui_mainwindow(object):
	
	def setupUi(self, mainwindow):
		sshFile="style/darkorange.stylesheet"
		with open(sshFile,"r") as fh:
			mainwindow.setStyleSheet(fh.read())
		
		mainwindow.setObjectName(_fromUtf8("mainwindow"))
		mainwindow.setWindowModality(QtCore.Qt.NonModal)
		mainwindow.resize(424, 384)
		mainwindow.setMaximumSize(424,384)
		mainwindow.setWindowOpacity(100.0)
		
		mainwindow.setAutoFillBackground(True)
		
		self.progressBar = QtGui.QProgressBar(mainwindow)
		self.progressBar.setGeometry(QtCore.QRect(9, 350, 401, 25))
		self.progressBar.setProperty("value", 0)
		self.progressBar.setTextVisible(False)
		self.progressBar.setFormat(_fromUtf8("%p%"))
		self.progressBar.setObjectName(_fromUtf8("progressBar"))
		
		self.dock = QtGui.QPushButton(mainwindow)
		self.dock.setGeometry(QtCore.QRect(300, 250, 119, 27))
		self.dock.setText(_fromUtf8("Dock!"))
		self.dock.setObjectName(_fromUtf8("dock"))
		
		self.abort = QtGui.QPushButton(mainwindow)
		self.abort.setGeometry(QtCore.QRect(300, 280, 119, 27))
		self.abort.setText(_fromUtf8("Abort!"))
		self.abort.setDefault(False)
		self.abort.setObjectName(_fromUtf8("abort"))
		
		self.csvexport = QtGui.QPushButton(mainwindow)
		self.csvexport.setGeometry(QtCore.QRect(300, 310, 119, 27))
		self.csvexport.setText(_fromUtf8("CSV export"))
		self.csvexport.setObjectName(_fromUtf8("csvexport"))
		
		self.scrollArea = QtGui.QScrollArea(mainwindow)
		self.scrollArea.setGeometry(QtCore.QRect(10, 250, 281, 80))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents = QtGui.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 78))
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		
		self.outputArea = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.outputArea.setGeometry(QtCore.QRect(0, 0, 281, 81))
		self.outputArea.setMaximumSize(QtCore.QSize(281, 2000))
		#self.outputArea.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
		self.outputArea.setText(_fromUtf8(message))
		self.outputArea.setObjectName(_fromUtf8("outputArea"))
		self.scrollArea.setWidget(self.outputArea)
		
		self.widget = QtGui.QWidget(mainwindow)
		self.widget.setGeometry(QtCore.QRect(9, 9, 411, 62))
		self.widget.setObjectName(_fromUtf8("widget"))
		
		self.gridLayout = QtGui.QGridLayout(self.widget)
		self.gridLayout.setMargin(0)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		
		self.ligandbox = QtGui.QComboBox(self.widget)
		self.ligandbox.addItems(["       Ligand List"])
		self.ligandbox.currentIndexChanged.connect(self.resetComboBox)
		self.ligandbox.setObjectName(_fromUtf8("ligandbox"))
		self.gridLayout.addWidget(self.ligandbox, 1, 2, 1, 1)
		
		self.addLigand = QtGui.QPushButton(self.widget)
		self.addLigand.setText(_fromUtf8("Add Ligands"))
		self.addLigand.setObjectName(_fromUtf8("addLigand"))
		self.gridLayout.addWidget(self.addLigand, 1, 1, 1, 1)
		
		self.recName = QtGui.QLabel(self.widget)
		self.recName.setFrameShape(QtGui.QFrame.NoFrame)
		self.recName.setText(_fromUtf8("Receptor Name"))
		self.recName.setAlignment(QtCore.Qt.AlignCenter)
		self.recName.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.recName.setObjectName(_fromUtf8("recName"))
		
		self.gridLayout.addWidget(self.recName, 0, 2, 1, 1)
		
		self.addReceptor = QtGui.QPushButton(self.widget)
		self.addReceptor.setText(_fromUtf8("Add Receptor"))
		self.addReceptor.setObjectName(_fromUtf8("addReceptor"))
		
		
		self.gridLayout.addWidget(self.addReceptor, 0, 1, 1, 1)
		
		self.recCheckbox = QtGui.QCheckBox(self.widget)
		self.recCheckbox.setText(_fromUtf8("Added!"))
		self.recCheckbox.setCheckState(QtCore.Qt.Checked)
		self.recCheckbox.setObjectName(_fromUtf8("recCheckbox"))
		self.recCheckbox.setCheckable(False)
		self.gridLayout.addWidget(self.recCheckbox, 0, 3, 1, 1)
		
		self.ligCheckbox = QtGui.QCheckBox(self.widget)
		self.ligCheckbox.setText(_fromUtf8("Found!"))
		self.ligCheckbox.setShortcut(_fromUtf8(""))
		self.ligCheckbox.setCheckable(False)
		self.ligCheckbox.setObjectName(_fromUtf8("ligCheckbox"))
		self.gridLayout.addWidget(self.ligCheckbox, 1, 3, 1, 1)
		
		self.widget1 = QtGui.QWidget(mainwindow)
		self.widget1.setGeometry(QtCore.QRect(9, 68, 406, 155))
		self.widget1.setObjectName(_fromUtf8("widget1"))
		
		self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
		self.verticalLayout.setMargin(0)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		
		self.configlab = QtGui.QLabel(self.widget1)
		self.configlab.setText(_fromUtf8("Configuration"))
		self.configlab.setAlignment(QtCore.Qt.AlignCenter)
		self.configlab.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.configlab.setObjectName(_fromUtf8("configlab"))
		self.verticalLayout.addWidget(self.configlab)
		
		self.gridLayout_2 = QtGui.QGridLayout()
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.formLayout_3 = QtGui.QFormLayout()
		self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
		self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
		
		self.cxl = QtGui.QLabel(self.widget1)
		self.cxl.setText(_fromUtf8("Center of X"))
		self.cxl.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.cxl.setObjectName(_fromUtf8("cxl"))
		
		self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.cxl)
		self.cx = QtGui.QLineEdit(self.widget1)
		self.cx.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
		self.cx.setText(_fromUtf8(""))
		self.cx.setObjectName(_fromUtf8("cx"))
		self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.cx)
		
		self.cyl = QtGui.QLabel(self.widget1)
		self.cyl.setText(_fromUtf8("Center of Y"))
		self.cyl.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.cyl.setObjectName(_fromUtf8("cyl"))
		self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.cyl)
		
		self.cy = QtGui.QLineEdit(self.widget1)
		self.cy.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
		self.cy.setText(_fromUtf8(""))
		self.cy.setObjectName(_fromUtf8("cy"))
		self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.cy)
		
		self.czl = QtGui.QLabel(self.widget1)
		self.czl.setText(_fromUtf8("Center of Z"))
		self.czl.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.czl.setObjectName(_fromUtf8("czl"))
		self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.czl)
		
		self.cz = QtGui.QLineEdit(self.widget1)
		self.cz.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
		self.cz.setText(_fromUtf8(""))
		self.cz.setObjectName(_fromUtf8("cz"))
		self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.cz)
		
		self.gridLayout_2.addLayout(self.formLayout_3, 0, 0, 1, 1)
		self.formLayout_4 = QtGui.QFormLayout()
		self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
		
		self.sxl = QtGui.QLabel(self.widget1)
		self.sxl.setText(_fromUtf8("Size of X"))
		self.sxl.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.sxl.setObjectName(_fromUtf8("sxl"))
		self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.sxl)
		
		self.syl = QtGui.QLabel(self.widget1)
		self.syl.setText(_fromUtf8("Size of Y"))
		self.syl.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.syl.setObjectName(_fromUtf8("syl"))
		self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.syl)
		
		self.szl = QtGui.QLabel(self.widget1)
		self.szl.setText(_fromUtf8("Size of Z"))
		self.szl.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.szl.setObjectName(_fromUtf8("szl"))
		self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.szl)
		
		self.sx = QtGui.QLineEdit(self.widget1)
		self.sx.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
		self.sx.setText(_fromUtf8(""))
		self.sx.setObjectName(_fromUtf8("sx"))
		self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.sx)
		
		self.sy = QtGui.QLineEdit(self.widget1)
		self.sy.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
		self.sy.setText(_fromUtf8(""))
		self.sy.setObjectName(_fromUtf8("sy"))
		self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.sy)
		
		self.sz = QtGui.QLineEdit(self.widget1)
		self.sz.setAutoFillBackground(False)
		self.sz.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
		self.sz.setText(_fromUtf8(""))
		self.sz.setObjectName(_fromUtf8("sz"))
		self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.sz)
		
		self.gridLayout_2.addLayout(self.formLayout_4, 0, 1, 1, 1)
		self.verticalLayout.addLayout(self.gridLayout_2)
		
		self.createConfig = QtGui.QPushButton(self.widget1)
		self.createConfig.setText(_fromUtf8("Create"))
		self.createConfig.setAutoDefault(False)
		self.createConfig.setDefault(True)
		self.createConfig.setFlat(False)
		self.createConfig.setObjectName(_fromUtf8("createConfig"))
		self.verticalLayout.addWidget(self.createConfig)

		self.retranslateUi(mainwindow)
		QtCore.QMetaObject.connectSlotsByName(mainwindow)

		self.addReceptor.clicked.connect(self.addReceptorActions)
		self.addLigand.clicked.connect(self.addLigandActions)
		self.createConfig.clicked.connect(self.createConfigActions)
		self.recCheckbox.clicked.connect(self.recCheckboxAction)
		self.ligCheckbox.clicked.connect(self.ligCheckboxAction)
		self.dock.clicked.connect(self.dockActions)
	
	def addReceptorActions(self):
		rImport=receptorImport()
		receptorName=rImport.init()
		outputMessage="Receptor:"+receptorName+" Added"
		self.recName.setText(receptorName)
		self.recCheckbox.setCheckable(True)
		self.recCheckbox.setCheckState(QtCore.Qt.Checked)
		self.postMessage(outputMessage)
	
	def addLigandActions(self):
		lImport=ligandsImport()
		ligandlist=lImport.init()
		outputMessage=str(len(ligandlist))+" Ligands Added"
		self.ligCheckbox.setCheckable(True)
		self.ligCheckbox.setCheckState(QtCore.Qt.Checked)
		self.ligandbox.addItems(ligandlist)
		self.postMessage(outputMessage)
	def resetComboBox(self):
		self.ligandbox.setCurrentIndex(0)

	def createConfigActions(self):
		coordinates=[]
		coordinates.append(str(self.cx.text()))
		coordinates.append(str(self.cy.text()))
		coordinates.append(str(self.cz.text()))

		sizes=[]
		sizes.append(str(self.sx.text()))
		sizes.append(str(self.sy.text()))
		sizes.append(str(self.sz.text()))

		configinstance=ConfigManager(coordinates, sizes)
		
		coordcheckresponse=configinstance.checkcords()
		for resps in coordcheckresponse:
			self.postMessage(resps)

		sizecheckresponse=configinstance.checksizes()
		for resps in sizecheckresponse:
			self.postMessage(resps)
		if "Okay" in coordcheckresponse[0] and "Okay" in sizecheckresponse[0]:
			writeresponse=configinstance.writefile()
			self.postMessage(writeresponse)

	def recCheckboxAction(self):
		if self.recCheckbox.isCheckable()==True:
			self.recCheckbox.setCheckState(QtCore.Qt.Checked)

	def ligCheckboxAction(self):
		if self.ligCheckbox.isCheckable()==True:
			self.ligCheckbox.setCheckState(QtCore.Qt.Checked)

	def dockActions(self):
		try:
			ligandlist=os.listdir("resources/ligands")
		except:
			self.postMessage("ligands folder not found!")

		try:
			receptor=os.listdir("resources/receptor")
		except:
			self.postMessage("receptor folder not found!")

		if len(ligandlist)==0:
			self.postMessage("ligands folder empty!")
		if len(receptor)==0:
			self.postMessage("receptor folder empty!")
		try:
			conf=file("resources/baseconf").read()
		except:
			self.postMessage("baseconf not found")
		if len(conf)==0:
			self.postMessage("baseconf is empty")

		progressBarUnit=int(100/len(ligandlist))

		self.instance=DockerThread()
		#self.connect(self.instance, SIGNAL('progressBarUpdate(unit)'),self.progressBarUpdate)
		self.instance.start()



		# if len(ligandlist)>0 and len(receptor)>0 and len(conf)>0:
		# 	for lig in ligandlist:
		# 		instance=Docker(receptor[0], lig, conf)
		# 		try:
		# 			response=instance.copyfiles()
		# 			self.postMessage(response)
		# 		except:
		# 			self.postMessage("Error with "+lig+" config creation")
		# 			break
		# 		instance.dock()
		# 		self.progressBarUpdate(progressBarUnit)


	def postMessage(self,outputMessage):
		global message
		message=message.replace("</body></html>","")
		message=message+"<p style=font-size:12px>"+outputMessage+"</body></html>"
		self.outputArea.setText(message)
	def progressBarUpdate(self, unit):
		curr=self.progressBar.value()
		for i in range(unit):
			self.progressBar.setProperty("value", curr+i)
			#time.sleep(0.02)


	def retranslateUi(self, mainwindow):
		mainwindow.setWindowTitle(QtGui.QApplication.translate("mainwindow", "EasyVina", None, QtGui.QApplication.UnicodeUTF8))

class DockerThread(QThread):
		def __init__(self):
			QThread.__init__(self)

		def __del__(self):
			self.wait()
		def run(self):
			for i in range(100):
				print i
				#self.emit(SIGNAL('progressBarUpdate(unit)'),i)
				time.sleep(2) 

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	app.setStyle("cleanlooks")
	mainwindow = QtGui.QWidget()
	ui = Ui_mainwindow()
	ui.setupUi(mainwindow)
	mainwindow.show()
	sys.exit(app.exec_())


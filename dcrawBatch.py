import sys, os, glob
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
import multiprocessing, subprocess, platform
import dcrawBatchUi

import taskManager



class MainUiClass(QtWidgets.QMainWindow, dcrawBatchUi.Ui_MainWindow ):
	def __init__(self, parent=None):

		super(MainUiClass, self).__init__(parent)
		self.setupUi(self)

		self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)


		#setup the task manager
		self.manager = taskManager.TaskManager(self)
		self.manager.numbersTaskRunningChanged.connect(self.runningProcessesLabel.setNum)
		self.manager.messageChanged.connect(self.ProcessTextEdit.append)
		self.manager.setMaxTask(multiprocessing.cpu_count())


		self.model = QtGui.QStandardItemModel(self.ImagesListView)
		self.CommandLineEdit.setEnabled(False)
		self.spinBox.setValue(multiprocessing.cpu_count())
		self.files =[]
		self.dcrawPathLineEdit.setText(self.checkDcraw())


		#signals and slots
		self.ImagesFolderSelectPushButton.clicked.connect(self.selectFilesFolder)
		self.dcrawPathSelectPushButton.clicked.connect(self.selectDcrawFolder)
		self.ArgsLineEdit.textChanged.connect(self.generateCommand)
		self.dcrawPathLineEdit.textChanged.connect(self.generateCommand)
		self.ConvertPushButton.clicked.connect(self.convert)
		self.StopConvertPushButton.clicked.connect(self.manager.stop)
		self.spinBox.valueChanged.connect(self.manager.setMaxTask)


		self.generateCommand()



	def selectFilesFolder(self):
		dialog = QtWidgets.QFileDialog()
		folderPath = dialog.getExistingDirectory(None, "Select Folder")
		self.ImagesFolderLineEdit.setText(folderPath)
		self.files = glob.glob(folderPath+'/*.*')
		self.model.clear()

		for file in self.files:
			item = QtGui.QStandardItem(file)
			item.setCheckable(True)
			item.setCheckState(Qt.Checked)
			self.model.appendRow(item)

		self.ImagesListView.setModel(self.model)
		self.generateCommand()


	def checkDcraw(self):

		p = subprocess.Popen("which dcraw", stdout=subprocess.PIPE, shell=True)

		(output, err) = p.communicate()

		## Wait for which to terminate. Get return returncode ##
		p_status = p.wait()
		if p_status == 0:
			return output
			self.generateCommand()
		else:
			self.errorLogLabel.setText('could not find dcraw in system path, please select it manually under settings tab!')
			return ''

	def selectDcrawFolder(self):
		dialog = QtWidgets.QFileDialog()
		folderPath = dialog.getOpenFileName(None, "Select dcraw Executable")
		self.dcrawPathLineEdit.setText(folderPath[0])

		self.generateCommand()



	def generateCommand(self):
		command = self.dcrawPathLineEdit.text() + " " + self.ArgsLineEdit.text()
		self.CommandLineEdit.clear()
		self.CommandLineEdit.setText(command)


	def convert(self):
		task_list=[]
		for file in range(self.model.rowCount()):
			item = self.model.item(file)
			if item.checkState()== QtCore.Qt.Checked:
				task_list.append(self.CommandLineEdit.text() +' '+ item.text())

		for task in task_list:
			self.manager.appendTask(task)

		self.manager.start()

if __name__ == '__main__':
	a = QtWidgets.QApplication(sys.argv)
	app = MainUiClass()
	app.show()
	a.exec_()

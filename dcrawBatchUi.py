# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dcrawBatch.ui',
# licensing of 'dcrawBatch.ui' applies.
#
# Created: Wed May 22 13:34:21 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.cpuHorizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        self.processesLabel = QtWidgets.QLabel('Running Processes')
        self.runningProcessesLabel = QtWidgets.QLabel('0')
        self.cpuLabel = QtWidgets.QLabel('Max Processes')
        self.verticalLayout_2.addWidget(self.runningProcessesLabel)

        self.spinBox = QtWidgets.QSpinBox()


        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ImagesFolderLabel = QtWidgets.QLabel(self.tab)
        self.ImagesFolderLabel.setObjectName("ImagesFolderLabel")
        self.horizontalLayout.addWidget(self.ImagesFolderLabel)
        self.ImagesFolderLineEdit = QtWidgets.QLineEdit(self.tab)
        self.ImagesFolderLineEdit.setObjectName("ImagesFolderLineEdit")
        self.horizontalLayout.addWidget(self.ImagesFolderLineEdit)
        self.ImagesFolderSelectPushButton = QtWidgets.QPushButton(self.tab)
        self.ImagesFolderSelectPushButton.setObjectName("ImagesFolderSelectPushButton")
        self.horizontalLayout.addWidget(self.ImagesFolderSelectPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ImagesListView = QtWidgets.QListView(self.tab)
        self.ImagesListView.setObjectName("ImagesListView")
        self.verticalLayout.addWidget(self.ImagesListView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ArgsLabel = QtWidgets.QLabel(self.tab)
        self.ArgsLabel.setObjectName("ArgsLabel")
        self.horizontalLayout_5.addWidget(self.ArgsLabel)
        self.ArgsLineEdit = QtWidgets.QLineEdit(self.tab)
        self.ArgsLineEdit.setObjectName("ArgsLineEdit")
        self.horizontalLayout_5.addWidget(self.ArgsLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CommandLabel = QtWidgets.QLabel(self.tab)
        self.CommandLabel.setObjectName("CommandLabel")
        self.horizontalLayout_4.addWidget(self.CommandLabel)
        self.CommandLineEdit = QtWidgets.QLineEdit(self.tab)
        self.CommandLineEdit.setObjectName("CommandLineEdit")
        self.horizontalLayout_4.addWidget(self.CommandLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.ProcessTextEdit = QtWidgets.QTextEdit(self.tab)
        self.ProcessTextEdit.setObjectName("ProcessTextEdit")
        self.verticalLayout_2.addWidget(self.ProcessTextEdit)
        self.ConvertPushButton = QtWidgets.QPushButton(self.tab)
        self.ConvertPushButton.setObjectName("ConvertPushButton")
        self.StopConvertPushButton = QtWidgets.QPushButton(self.tab)
        self.StopConvertPushButton.setObjectName("StopConvertPushButton")
        self.verticalLayout_2.addWidget(self.ConvertPushButton)
        self.verticalLayout_2.addWidget(self.StopConvertPushButton)




        self.cpuHorizontalLayout.addWidget(self.cpuLabel)
        self.cpuHorizontalLayout.addWidget(self.spinBox)
        self.cpuHorizontalLayout.addWidget(self.processesLabel)
        self.cpuHorizontalLayout.addWidget(self.runningProcessesLabel)
        self.verticalLayout_2.addLayout(self.cpuHorizontalLayout)

        self.errorLogLabel = QtWidgets.QLabel()
        self.verticalLayout_2.addWidget(self.errorLogLabel)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 751, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dcrawPathLabel = QtWidgets.QLabel(self.layoutWidget)
        self.dcrawPathLabel.setObjectName("dcrawPathLabel")
        self.horizontalLayout_3.addWidget(self.dcrawPathLabel)
        self.dcrawPathLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.dcrawPathLineEdit.setObjectName("dcrawPathLineEdit")
        self.horizontalLayout_3.addWidget(self.dcrawPathLineEdit)
        self.dcrawPathSelectPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.dcrawPathSelectPushButton.setObjectName("dcrawPathSelectPushButton")
        self.horizontalLayout_3.addWidget(self.dcrawPathSelectPushButton)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "dcraw batch", None, -1))
        self.ImagesFolderLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Images Folder", None, -1))
        self.ImagesFolderSelectPushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.ArgsLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Args", None, -1))
        self.CommandLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Command", None, -1))
        self.ConvertPushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Convert", None, -1))
        self.StopConvertPushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Stop", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Convert", None, -1))
        self.dcrawPathLabel.setText(QtWidgets.QApplication.translate("MainWindow", "dcraw Path", None, -1))
        self.dcrawPathSelectPushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))


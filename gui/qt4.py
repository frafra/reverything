# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4.ui'
#
# Created: Sat Jul 26 19:54:00 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,423,412).size()).expandedTo(MainWindow.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridlayout.addWidget(self.lineEdit,0,1,1,1)

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,0,1,1)

        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridlayout.addWidget(self.lineEdit_2,1,1,1,1)

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,2,0,1,1)

        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridlayout.addWidget(self.lineEdit_3,2,1,1,1)

        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,3,0,1,1)

        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.gridlayout.addWidget(self.tableWidget,3,1,1,1)

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")

        spacerItem = QtGui.QSpacerItem(201,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem,0,0,1,1)

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridlayout1.addWidget(self.pushButton,0,1,1,1)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridlayout1.addWidget(self.pushButton_2,0,2,1,1)
        self.gridlayout.addLayout(self.gridlayout1,4,0,1,2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,423,27))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")

        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Reverything", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "New name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("MainWindow", "Old name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("MainWindow", "New name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(1,headerItem1)
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Rename", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))


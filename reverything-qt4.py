#!/usr/bin/env python
# -*- utf-8 -*-
#
# reverything-qt4.py
#
# Copyright 2008 Francesco Frassinelli <fraph24@gmail.com>
# 
#    This file is part of Reverything.
#    
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

### [1] This version doesn't work, it only do a preview, but don't rename
import os, sys
from reverything import Reverything
from gui.qt4 import * 

class MainWindow(QtGui.QMainWindow, Ui_MainWindow, Reverything):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Reverything.__init__(self, '', '')
        self.setupUi(self)
        self.lineEdit.setText(self.directory)
        
        self.connect(self.lineEdit,
            QtCore.SIGNAL("textEdited(QString)"), self.on_lineEdit_textEdited)
        self.connect(self.lineEdit_2,
            QtCore.SIGNAL("textEdited(QString)"), self.on_lineEdit_2_textEdited)
        self.connect(self.lineEdit_3,
            QtCore.SIGNAL("textEdited(QString)"), self.on_lineEdit_3_textEdited)
        
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.clear)
        self.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.rename)
        
        self.refresh()

    def on_lineEdit_textEdited(self):
        self.directory = str(self.lineEdit.text())
        self.refresh()
    
    def on_lineEdit_2_textEdited(self):
        self.regex = str(self.lineEdit_2.text())
        self.refresh()
    
    def on_lineEdit_3_textEdited(self):
        self.name = str(self.lineEdit_3.text())
        self.refresh()
    
    def clear(self):
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.refresh()
        
    def rename(self):
        self.rn()
        self.refresh()
    
    def refresh(self):
        try:
            self.ls()
        except:
            return
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(self.items))
        
        ### [2] Dirty fix to block strange renaming of columns
        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("MainWindow", "Old name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(0,headerItem)
        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("MainWindow", "New name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(1,headerItem1)
        
        for n, item in enumerate(self.items):
            ### [3] QT4 do this automatically...
            ###     How to remove this pseudo-column?
            #headerItem = QtGui.QTableWidgetItem()
            #headerItem.setText(str(n))
            #self.tableWidget.setVerticalHeaderItem(n, headerItem)
            
            item_tmp = QtGui.QTableWidgetItem()
            item_tmp.setText(item)
            self.tableWidget.setItem(n, 0, item_tmp)
            
            item_tmp = QtGui.QTableWidgetItem()
            item_tmp.setText(self.items[item])
            self.tableWidget.setItem(n, 1, item_tmp)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


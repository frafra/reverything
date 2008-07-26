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
### [2] Dirty hacks here, I should clean up the code
from sys import argv, exit
from sys import path as ppath
from os import getcwd, path
from reverything import Reverything
ppath.append(path.join(getcwd(), 'gui'))
from qt4 import *

class MainWindow(QtGui.QMainWindow, Ui_MainWindow, Reverything):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Reverything.__init__(self, '', '')
        self.setupUi(self)
        self.lineEdit.setText(self.directory)
        
        QtCore.QObject.connect(self.lineEdit_2,
            QtCore.SIGNAL("textEdited(QString)"),self.on_lineEdit_2_textEdited)
        QtCore.QObject.connect(self.lineEdit_3,
            QtCore.SIGNAL("textEdited(QString)"),self.on_lineEdit_3_textEdited)
    
    def on_lineEdit_2_textEdited(self):
        self.regex = str(self.lineEdit_2.text())
        self.refresh()
    
    def on_lineEdit_3_textEdited(self):
        self.name = str(self.lineEdit_3.text())
        self.refresh()
    
    def refresh(self):
        try:
            items = self.ls()
        except:
            return
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(items))
        for n, item in enumerate(items):
            headerItem = QtGui.QTableWidgetItem()
            headerItem.setText(str(n))
            self.tableWidget.setVerticalHeaderItem(n, headerItem)
            
            item1 = QtGui.QTableWidgetItem()
            item1.setText(item)
            self.tableWidget.setItem(n,0,item1)
            
            item2 = QtGui.QTableWidgetItem()
            item2.setText(items[item])
            self.tableWidget.setItem(n,1,item2)

if __name__ == "__main__":
    app = QtGui.QApplication(argv)
    ui = MainWindow()
    ui.show()
    exit(app.exec_())


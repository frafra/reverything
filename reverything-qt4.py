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

import os, sys
from reverything import Reverything
from gui.qt4 import * 

class MainWindow(QtGui.QMainWindow, Ui_MainWindow, Reverything):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Reverything.__init__(self, '', '', [os.getcwd()])
        self.setupUi(self)
        self.lineEdit.setText(self.dirs[0])
        
        self.connect(self.lineEdit,
            QtCore.SIGNAL("textEdited(QString)"), self.on_lineEdit_textEdited)
        self.connect(self.lineEdit_2,
            QtCore.SIGNAL("textEdited(QString)"), self.on_lineEdit_2_textEdited)
        self.connect(self.lineEdit_3,
            QtCore.SIGNAL("textEdited(QString)"), self.on_lineEdit_3_textEdited)
        
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.refresh)
        self.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.rename)
        
        self.refresh()

    def on_lineEdit_textEdited(self):
        changed = str(self.lineEdit.text())
        if os.path.isdir(changed):
            self.dirs = [changed]
            self.refresh()

    def on_lineEdit_2_textEdited(self):
        self.regex_in = str(self.lineEdit_2.text())
        self.refresh()
    
    def on_lineEdit_3_textEdited(self):
        self.regex_out = str(self.lineEdit_3.text())
        self.refresh()
        
    def rename(self):
        self.apply()
        self.refresh()
    
    def refresh(self):
        self.preview()
        model = QtGui.QStandardItemModel(self)
        item = QtCore.QStringList()
        item.insert(0, 'Old name')
        item.insert(1, 'New name')
        model.setHorizontalHeaderLabels(item)
        parentItem = model.invisibleRootItem()
        for folder in self.map:
            item = QtGui.QStandardItem(QtCore.QString(folder))
            item2 = QtGui.QStandardItem(QtCore.QString(folder))
            parentItem.appendRow([item, item2])
            parentItem = item
            for obj in self.map[folder]:
                item = QtGui.QStandardItem(QtCore.QString(obj))
                item2 = QtGui.QStandardItem(QtCore.QString(self.map[folder][obj]))
                parentItem.appendRow([item, item2])
        self.treeView.setModel(model)  

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


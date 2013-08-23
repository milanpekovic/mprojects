#!/usr/bin/env python
 # -*- coding: utf-8 -*-

import sys
import platform
from PySide import QtGui
from PySide import QtCore

__version__ = '0.0.0'

class MainWindow(QtGui.QMainWindow):
    sequenceNumber = 1
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()      

    def initUI(self):
        self.textEdit = QtGui.QTextEdit() 
        self.setCentralWidget(self.textEdit)
        font = QtGui.QFont('Serif', 10, QtGui.QFont.Light)
        self.textEdit.setFont(font)
        
        
        self.statusBar()
	self.create_actions()
	self.create_menubar()
	self.show_window()

#-----------------------------------------------------------------------------
    # Creating Menu and Menu actions
    # Need images
   
    def create_actions(self):
	# File Menu
        self.newAct = QtGui.QAction(QtGui.QIcon('icons/document_alt_stroke_12x16.png'), '&New', self)
        self.newAct.setShortcut(QtGui.QKeySequence.New)
        self.newAct.setStatusTip('Create a new file')
        self.newAct.triggered.connect(self.newFile)

        self.openAct = QtGui.QAction(QtGui.QIcon('open.png'), '&Open', self)
        self.openAct.setShortcuts(QtGui.QKeySequence.Open)
        self.openAct.setStatusTip('Open an existing file')
        self.openAct.triggered.connect(self.openFile)

        self.saveAct = QtGui.QAction(QtGui.QIcon('save.png'), '&Save', self)
        self.saveAct.setShortcuts(QtGui.QKeySequence.Save)
        self.saveAct.setStatusTip('Save file')
        self.saveAct.triggered.connect(self.saveFile)

        self.exitAct = QtGui.QAction(QtGui.QIcon('close.png'), '&Close', self)
        self.exitAct.setShortcuts(QtGui.QKeySequence.Close)
        self.exitAct.setStatusTip('Exit editor')
        self.exitAct.triggered.connect(self.close)
        
	# Help Menu
        self.aboutAct = QtGui.QAction(QtGui.QIcon('about.png'), '&About', self)
        self.aboutAct.setStatusTip('About this application')
        self.aboutAct.triggered.connect(self.about)
        
        # Toolbar
        self.toolbar = self.addToolBar('New')
        self.toolbar.addAction(self.newAct)
        
    def create_menubar(self):
        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.exitAct)
        
        self.helpMenu = self.menubar.addMenu('&Help')
        self.helpMenu.addAction(self.aboutAct)
#-----------------------------------------------------------------------------       
    # Creating Menu dialogs
    # Need better setWindowTitle process, better alternatives from PySide doc?
    def newFile(self):
	MainWindow.sequenceNumber += 1
	self.curFile = 'Untitled{}.txt '.format(str(MainWindow.sequenceNumber))
        self.setWindowTitle(self.curFile +'- Leminator')
        self.textEdit.clear()
        print self.textEdit.fontFamily()
        
    def openFile(self):
	# filtr is useless atm
        fname, filtr = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.')
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
        self.curFile = fname
        self.setWindowTitle(self.curFile +' - Leminator')
     
    def saveFile(self):
        fname, _ = QtGui.QFileDialog.getSaveFileName(self, 'Save file', '.')
	f = open(fname, 'w+')
	with f:
	    data = self.textEdit.toPlainText() 
	    f.write(data)
	
    def about(self):
	QtGui.QMessageBox.about(self, 'About Leminator',
		   '''
                   About this program. v {}
                   This app is my project for learning
                   PySide and GUI managment.
                   Copyright © 2013 Milan Pekovic.
                   All rights reserved in accordance with
                   GPL v2 or later - NO WARRANTIES!
                   '''.format(__version__))
                   
#-----------------------------------------------------------------------------
    # Window settings
    def show_window(self):
        self.setGeometry(100, 100, 600, 450)
        # NoType bug when creating and formating __appname__ = 'Leminator'
        self.setWindowTitle('Untitled{}.txt - Leminator'
			    .format(str(MainWindow.sequenceNumber)))
        self.show()
        self.setMinimumSize(QtCore.QSize(600, 450))
       
#-----------------------------------------------------------------------------    
# Main loop
def main():
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

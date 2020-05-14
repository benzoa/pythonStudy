import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore

form_class = uic.loadUiType("ui/main_window.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUi()
    
    def initUi(self):
        self.setWindowTitle('Main Window')
        self.setWindowIcon(QIcon('resources/web.png'))

        self.label = QLabel("Auto Save is deactivated.")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.setCentralWidget(self.label)

        # statusBar
        self.statusBar().showMessage('Ready', 3000)

        # menuBar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')

        newFile = QAction('New File', self)
        newFile.setShortcut('Ctrl+N')
        newFile.setStatusTip('New File')
        filemenu.addAction(newFile)

        newWindow = QAction('New Window', self)
        newWindow.setShortcut('Ctrl+Shift+N')
        newWindow.setStatusTip('New Window')
        filemenu.addAction(newWindow)
        filemenu.addSeparator()

        openFile = QAction('Open File...', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        filemenu.addAction(openFile)

        openFolder = QAction('Open Folder...', self)
        openFolder.setShortcut('Ctrl+K Ctrl+O')
        openFolder.setStatusTip('Open Folder')
        filemenu.addAction(openFolder)
        
        openRecent = filemenu.addMenu('Open Recent')
        open123 = QAction('123', self)
        open456 = QAction('456', self)
        openRecent.addAction(open123)
        openRecent.addAction(open456)
        filemenu.addSeparator()

        autoSave = QAction('&Auto Save', self, checkable=True)
        autoSave.setStatusTip('Auto Save')
        autoSave.triggered.connect(self.toggleLabel)
        filemenu.addAction(autoSave)

        preference = filemenu.addMenu('Preference')
        preference.addAction(open123)
        preference.addAction(open456)
        filemenu.addSeparator()
        
        exitAction = QAction(QIcon('resources/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        filemenu.addAction(exitAction)

        # toolBar
        saveAction = QAction(QIcon('resources/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save application')

        editAction = QAction(QIcon('resources/edit.png'), 'Edit', self)
        editAction.setStatusTip('Edit application')

        toolbar = self.addToolBar('Exit')
        toolbar.setMovable(False)
        toolbar.addAction(saveAction)
        toolbar.addAction(editAction)
        toolbar.addSeparator()

    def toggleLabel(self, state):
        self.label.setText("Auto Save is {}.".format("activated" if state else "deactivated"))


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
 
 
class TestThread(QThread):
    threadEvent = QtCore.pyqtSignal(int)
 
    def __init__(self, parent=None):
        super().__init__()
        self.n = 0
        self.main = parent
        self.isRun = False
 
    def run(self):
        while self.isRun:
            print('Thread : ' + str(self.n))
 
            self.threadEvent.emit(self.n)
            self.n += 1
            self.sleep(1)
 
 
class TestGUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
 
        self.btn1 = QPushButton("Start Thread", self)
        self.btn2 = QPushButton("Stop Thread", self)
 
        vertBox = QVBoxLayout()
        vertBox.addWidget(self.btn1)
        vertBox.addWidget(self.btn2)
        self.setLayout(vertBox)
        self.setGeometry(700, 500, 300, 100)
 
        self.btn1.clicked.connect(self.threadStart)
        self.btn2.clicked.connect(self.threadStop)
        self.show()

        self.th = TestThread(self)
        self.th.threadEvent.connect(self.threadEventHandler)
 
    @pyqtSlot()
    def threadStart(self):
        if not self.th.isRun:
            print('Main : Started Thread')
            self.th.isRun = True
            self.th.start()
 
    @pyqtSlot()
    def threadStop(self):
        if self.th.isRun:
            print('Main : Stoped Thread')
            self.th.isRun = False
 
    @pyqtSlot(int)
    def threadEventHandler(self, n):
        print('Main : threadEvent(self,' + str(n) + ')')
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = TestGUI()
    app.exec_()

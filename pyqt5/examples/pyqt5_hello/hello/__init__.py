import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

scriptdir, script = os.path.split(__file__)
editor_act = False

if editor_act == True:
    from hello import Ui_hello
else:
    from .hello import Ui_hello

class WindowClass(QWidget):
    def __init__(self) :
        super().__init__()
        self.ui = Ui_hello()
        self.ui.setupUi(self)
        # The icon is displayed normally only when the title bar icon is an absolute path.
        self.setWindowIcon(QIcon(scriptdir + '\\' + "hello_64.ico"))
        self.fmt = "yyyy-MM-dd hh:mm:ss"
        self.timer_timeout()
        self.timer_start()

    def timer_start(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_timeout)
        self.timer.start()

    def timer_timeout(self):
        self.dateTimeVar = QDateTime.currentDateTime()
        self.ui.date_time_lb.setText(self.dateTimeVar.toString(self.fmt))


if editor_act == True:
    if __name__ == '__main__':
        pass
else:
    def main():
        pass

app = QApplication(sys.argv)
myWindow = WindowClass()
myWindow.show()
app.exec_()

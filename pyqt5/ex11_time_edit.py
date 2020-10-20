import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTime
from PyQt5 import uic

form_class = uic.loadUiType("ui/time_edit.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # TimeEdit
        self.curTimeVar = QTime.currentTime()
        self.time_edit.setTime(self.curTimeVar)

        self.time_edit.timeChanged.connect(self.te_changed)

        self.time_info.clicked.connect(self.te_info_disp)
        self.time_set_time.clicked.connect(self.te_set_time)
        self.time_change_format.clicked.connect(self.te_change_format)

    def te_changed(self):
        print(self.time_edit.time())

    def te_info_disp(self):
        self.timeVar = self.time_edit.time()
        self.fmt = "AP hh:mm:ss"
        self.time_lb.setText(self.timeVar.toString(self.fmt))

    def te_set_time(self):
        self.le_time = self.time_le.text()
        self.le_time_var = QTime.fromString(self.le_time, "hh:mm:ss")
        self.time_edit.setTime(self.le_time_var)

    def te_change_format(self):
        self.new_format = self.time_disp_format_le.text()
        self.time_edit.setDisplayFormat(self.new_format)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

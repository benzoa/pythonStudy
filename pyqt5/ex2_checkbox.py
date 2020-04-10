import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/checkbox.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # group check box signal
        self.group_check_box1.stateChanged.connect(self.check_group_box_func)
        self.group_check_box2.stateChanged.connect(self.check_group_box_func)
        self.group_check_box3.stateChanged.connect(self.check_group_box_func)

        # group check box signal
        self.check_box1.stateChanged.connect(self.check_box_func)
        self.check_box2.stateChanged.connect(self.check_box_func)
        self.check_box3.stateChanged.connect(self.check_box_func)
    
    def check_group_box_func(self):
        if self.group_check_box1.isChecked(): print("group checkbox1 checked")
        if self.group_check_box2.isChecked(): print("group checkbox2 checked")
        if self.group_check_box3.isChecked(): print("group checkbox3 checked")

    def check_box_func(self):
        if self.check_box1.isChecked(): print("checkbox1 checked")
        if self.check_box2.isChecked(): print("checkbox2 checked")
        if self.check_box3.isChecked(): print("checkbox3 checked")


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

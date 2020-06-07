import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/checkbox.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #  check box group
        self.group_check_box1.stateChanged.connect(self.check_group_box_non_exclusive)
        self.group_check_box2.stateChanged.connect(self.check_group_box_exclusive)
        self.group_check_box3.stateChanged.connect(self.check_group_box_exclusive)

        # check box
        self.check_box1.stateChanged.connect(self.check_box_func)
        self.check_box2.stateChanged.connect(self.check_box_func)
        self.check_box3.stateChanged.connect(self.check_box_tri_state)

    def check_group_box_non_exclusive(self):
        if self.group_check_box1.isChecked():
            print("group Non-exclusive checked")
        else:
            print("group Non-exclusive unchecked")

    def check_group_box_exclusive(self):
        if self.group_check_box2.isChecked():
            print("group checkbox2 checked")
        elif self.group_check_box3.isChecked():
            print("group checkbox3 checked")

    def check_box_func(self):
        if self.check_box1.isChecked():
            print("checkbox1 checked")
        
        if self.check_box2.isChecked():
            self.check_box2.setText("Checked")
        else:
            self.check_box2.setText("Unchecked")

    def check_box_tri_state(self):
        if self.check_box3.checkState():
            print("Enable")
        else:
            print("Disable")


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

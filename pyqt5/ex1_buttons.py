import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/buttons.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # push button signal
        self.push_btn1.clicked.connect(self.push_btn1_func)
        self.push_btn2.clicked.connect(self.push_btn2_func)

        # radio button signal
        self.radio_btn1.clicked.connect(self.radio_group_box_func)
        self.radio_btn2.clicked.connect(self.radio_group_box_func)
        self.radio_btn3.clicked.connect(self.radio_group_box_func)

    def push_btn1_func(self):
        print("btn1 clicked")

    def push_btn2_func(self):
        print("btn2 clicked")

    def radio_group_box_func(self):
        if self.radio_btn1.isChecked(): print("radio1 checked")
        elif self.radio_btn2.isChecked(): print("radio2 checked")
        elif self.radio_btn3.isChecked(): print("radio3 checked")


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
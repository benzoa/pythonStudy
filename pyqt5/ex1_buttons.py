import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("ui/buttons.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
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
        if self.push_btn1.isChecked():
            self.push_btn1.setChecked(False)
        else:
            self.push_btn1.setChecked(True)

        self.push_btn1.toggle()

    def push_btn2_func(self):
        if self.push_btn2.isChecked():
            self.push_btn2.setStyleSheet("color: blue;"
                                         "border-style: solid;"
                                         "border-width: 2px;"
                                         "border-color: #FA8072;"
                                         "background-color: #7FFFD4;"
                                         "border-radius: 3px")
        else:
            self.push_btn2.setStyleSheet("")

    def radio_group_box_func(self):
        if self.radio_btn1.isChecked():
            print("radio1 checked")
        elif self.radio_btn2.isChecked():
            print("radio2 checked")
        elif self.radio_btn3.isChecked():
            print("radio3 checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

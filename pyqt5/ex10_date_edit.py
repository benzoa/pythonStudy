import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5 import uic

form_class = uic.loadUiType("ui/date_edit.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # DateEdit
        self.dateVar = QDate.currentDate()
        self.date_edit.setDate(self.dateVar)

        self.date_edit.dateChanged.connect(self.de_changed)

        self.date_info.clicked.connect(self.de_info_disp)
        self.date_set_date.clicked.connect(self.de_set_date)
        self.date_change_format.clicked.connect(self.de_change_format)
        self.date_print_range.clicked.connect(self.de_print_range)
        self.date_edit_max.clicked.connect(self.de_max)
        self.date_edit_min.clicked.connect(self.de_min)

    def de_changed(self):
        print(self.date_edit.date())

    def de_info_disp(self):
        self.dateVar = self.date_edit.date()
        self.fmt = "yy-MM-dd"
        self.date_lb.setText(self.dateVar.toString(self.fmt))

    def de_set_date(self):
        self.le_date = self.date_date_le.text()
        self.le_date_var = QDate.fromString(self.le_date, "yyyy-MM-dd")
        self.date_edit.setDate(self.le_date_var)

    def de_change_format(self):
        self.new_format = self.date_disp_format_le.text()
        self.date_edit.setDisplayFormat(self.new_format)

    def de_print_range(self):
        print("maximumDateTime: {}".format(self.date_edit.maximumDate()))
        print("minimumDateTime: {}".format(self.date_edit.minimumDate()))

    def de_max(self):
        self.cur_maximum_date = self.date_edit.maximumDate()
        self.cur_maximum_date = self.cur_maximum_date.addDays(10)
        self.date_edit.setMaximumDate(self.cur_maximum_date)

    def de_min(self):
        self.cur_minimum_date = self.date_edit.minimumDate()
        self.cur_minimum_date = self.cur_minimum_date.addDays(-10)
        self.date_edit.setMinimumDate(self.cur_minimum_date)


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
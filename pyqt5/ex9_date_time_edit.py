import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QDateTime, QDate, QTime
from PyQt5 import uic

form_class = uic.loadUiType("ui/time_date_edit.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # DateTimeEdit
        self.dateTimeVar = QDateTime.currentDateTime()
        self.date_time_edit.setDateTime(self.dateTimeVar)

        self.date_time_edit.dateTimeChanged.connect(self.dte_date_time_changed)
        self.date_time_edit.dateChanged.connect(self.dte_date_changed)
        self.date_time_edit.timeChanged.connect(self.dte_time_changed)

        self.date_time_info.clicked.connect(self.dte_info_display)
        self.date_time_set_date_time.clicked.connect(self.dte_set_date_time)
        self.date_time_set_date.clicked.connect(self.dte_set_date)
        self.date_time_set_time.clicked.connect(self.dte_set_time)
        self.date_time_change_format.clicked.connect(self.dte_change_format)
        self.date_time_print_range.clicked.connect(self.dte_print_range)
        self.date_time_plus_10day.clicked.connect(self.dte_plus_10days)
        self.date_time_minus_10days.clicked.connect(self.dte_minus_10days)

    def dte_date_time_changed(self):
        print("DateTime Changed: {}".format(self.date_time_edit.dateTime()))

    def dte_date_changed(self):
        print("Date Changed: {}".format(self.date_time_edit.date()))

    def dte_time_changed(self):
        print("Time Changed: {}".format(self.date_time_edit.time()))

    def dte_info_display(self):
        self.disp_date_time = self.date_time_edit.dateTime()
        self.fmt = "yyyy-MM-dd hh:mm:ss"
        self.date_time_date_time_lb.setText(self.disp_date_time.toString(self.fmt))

        self.disp_date = self.date_time_edit.date()
        self.fmt = "yy-MM-dd"
        self.date_time_date_lb.setText(self.disp_date.toString(self.fmt))

        self.disp_time = self.date_time_edit.time()
        self.fmt = "AP hh:mm:ss"
        self.date_time_time_lb.setText(self.disp_time.toString(self.fmt))

    def dte_set_date_time(self):
        self.date_and_time = self.date_time_date_time_le.text()
        self.le_date_time_var = QDateTime.fromString(self.date_and_time, "yyyy-MM-dd AP hh:mm:ss")
        self.date_time_edit.setDateTime(self.le_date_time_var)

    def dte_set_date(self):
        self.le_date = self.date_time_date_le.text()
        self.le_date_var = QDate.fromString(self.le_date, "yyyy-MM-dd")
        self.date_time_edit.setDate(self.le_date_var)

    def dte_set_time(self):
        self.le_time = self.date_time_time_le.text()
        self.le_time_var = QTime.fromString(self.le_time, "AP hh:mm:ss")
        self.date_time_edit.setTime(self.le_time_var)

    def dte_change_format(self):
        self.new_format = self.date_time_disp_format_le.text()
        self.date_time_edit.setDisplayFormat(self.new_format)

    def dte_print_range(self):
        print("maximumDateTime: {}".format(self.date_time_edit.maximumDateTime()))
        print("minimumDateTime: {}".format(self.date_time_edit.minimumDateTime()))

    def dte_plus_10days(self):
        self.cur_maximum_date_time = self.date_time_edit.maximumDateTime()
        self.cur_maximum_date_time = self.cur_maximum_date_time.addDays(10)
        self.date_time_edit.setMaximumDateTime(self.cur_maximum_date_time)

    def dte_minus_10days(self):
        self.cur_minimum_date_time = self.date_time_edit.minimumDateTime()
        self.cur_minimum_date_time = self.cur_minimum_date_time.addDays(-10)
        self.date_time_edit.setMinimumDateTime(self.cur_minimum_date_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

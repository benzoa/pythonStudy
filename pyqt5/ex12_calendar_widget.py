import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QDate
from PyQt5 import uic

form_class = uic.loadUiType("ui/calendar_widget.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Calendar Widget
        self.today = QDate.currentDate()
        self.cal_widget.setCurrentPage(self.today.year(), self.today.month())

        self.cal_selected()
        self.cal_page_changed()

        self.cal_widget.setGridVisible(True)

        self.cal_widget.clicked.connect(self.cal_day_clicked)
        self.cal_widget.selectionChanged.connect(self.cal_selected)
        self.cal_widget.currentPageChanged.connect(self.cal_page_changed)

        self.cal_prev_month.clicked.connect(self.cal_move_prev_month)
        self.cal_today.clicked.connect(self.cal_move_today)
        self.cal_next_month.clicked.connect(self.cal_move_next_month)
        self.cal_onoff_grid.clicked.connect(self.cal_toggle_grid)
        self.cal_set_day.clicked.connect(self.cal_set_new_day)
        self.cal_set_range.clicked.connect(self.cal_set_new_range)

    def cal_day_clicked(self):
        print("Clicked Day: {}".format(self.cal_widget.selectedDate()))

    def cal_selected(self):
        self.selected_day = self.cal_widget.selectedDate()
        self.fmt = "yyyy-MM-dd"
        self.cal_selected_lb.setText(self.selected_day.toString(self.fmt))

    def cal_page_changed(self):
        self.changed_page_year = str(self.cal_widget.yearShown())
        self.changed_page_month = str(self.cal_widget.monthShown())
        self.cal_cur_page_lb.setText(self.changed_page_year + '년' + ' ' +self.changed_page_month + '월')

    def cal_move_prev_month(self):
        self.cal_widget.showPreviousMonth()

    def cal_move_today(self):
        self.cal_widget.showToday()

    def cal_move_next_month(self):
        self.cal_widget.showNextMonth()

    def cal_toggle_grid(self):
        self.grid_visible_stat = self.cal_widget.isGridVisible()
        self.cal_widget.setGridVisible(not self.grid_visible_stat)

    def cal_set_new_day(self):
        self.update_day = QDate(2021, 10, 10)
        self.cal_widget.setSelectedDate(self.update_day)

    def cal_set_new_range(self):
        self.cal_widget.setMinimumDate(self.today.addDays(-7))
        self.cal_widget.setMaximumDate(self.today.addDays(7))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

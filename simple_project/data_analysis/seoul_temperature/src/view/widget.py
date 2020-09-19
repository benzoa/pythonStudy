from PyQt5.QtWidgets import QLabel, QDateEdit, QComboBox 
from PyQt5.QtCore import QDate, Qt
from control import *


def init_widget(self):
    # private methods
    self.__update_start_year = update_start_year
    self.__update_end_year = update_end_year
    self.__update_start_month = update_start_month
    self.__update_end_month = update_end_month
    self.__update_season = update_season
    self.__radio_group_data_form = radio_group_data_form
    self.__checkbox_group_data_type = checkbox_group_data_type
    self.__radio_group_graph_type = radio_group_graph_type
    self.__btn_search_clicked = btn_search_clicked
    self.__btn_save_graph_clicked = btn_save_graph_clicked
    self.__btn_search_processing = btn_search_processing


    self.de_start = QDateEdit(self)
    self.de_end = QDateEdit(self)

    self.cur_date = QDate.currentDate()
    self.de_start.setDate(self.cur_date.addMonths(-1))
    self.de_start.setDate(self.de_start.date().addDays(1))
    self.de_start.setCalendarPopup(True)

    self.de_end_minimum_date = self.cur_date.addDays(-1)
    self.de_end.setDate(self.de_end_minimum_date)
    self.de_end.setMaximumDate(self.de_end_minimum_date)
    self.de_end.setCalendarPopup(True)

    self.gridLayout.addWidget(self.de_start, 0, 0)
    self.period = QLabel('~', self)
    self.period.setAlignment(Qt.AlignCenter)
    self.gridLayout.addWidget(self.period, 0, 1)
    self.gridLayout.addWidget(self.de_end, 0, 2)

    # comboBox
    self.cb_start = QComboBox(self)
    self.this_year = int(self.cur_date.toString("yyyy"))

    items = [str(i) for i in range(
        int(self.this_year), int(self.this_year) - 20, -1)]
    self.cb_start.addItems(items)
    self.gridLayout.addWidget(self.cb_start, 0, 0)
    self.cb_start.setCurrentIndex(10)
    self.cb_start.setVisible(False)
    self.start_year = self.cb_start.currentText()
    self.cb_start.currentIndexChanged.connect(lambda: self.__update_start_year(self))

    self.cb_end = QComboBox(self)
    items = [str(i) for i in range(
        int(self.this_year), int(self.this_year) - 20, -1)]
    self.cb_end.addItems(items)
    self.gridLayout.addWidget(self.cb_end, 0, 2)
    self.cb_end.setVisible(False)
    self.end_year = self.cb_end.currentText()
    self.cb_end.currentIndexChanged.connect(lambda: self.__update_end_year(self))

    self.cb_month_start = QComboBox(self)
    items = ["{:02d}".format(i) for i in range(1, 13)]
    self.cb_month_start.addItems(items)
    self.gridLayout.addWidget(self.cb_month_start, 0, 3)
    self.cb_month_start.setVisible(False)
    self.start_month = self.cb_month_start.currentText()
    self.cb_month_start.currentIndexChanged.connect(
        lambda: self.__update_start_month(self))

    self.period_month = QLabel('~', self)
    self.period_month.setAlignment(Qt.AlignCenter)
    self.gridLayout.addWidget(self.period_month, 0, 4)
    self.period_month.setVisible(False)

    self.cb_month_end = QComboBox(self)
    self.cb_month_end.addItems(items)
    self.gridLayout.addWidget(self.cb_month_end, 0, 5)
    self.cb_month_end.setCurrentIndex(11)
    self.cb_month_end.setVisible(False)
    self.end_month = self.cb_month_end.currentText()
    self.cb_month_end.currentIndexChanged.connect(lambda: self.__update_end_month(self))

    self.season = QComboBox(self)
    ssaw = ['All', 'Spring', 'Summer', 'Autumn', 'Winter']
    self.season.addItems(ssaw)
    self.gridLayout.addWidget(self.season, 0, 3)
    self.season.setVisible(False)
    self.seasonCd = '0'  # All
    self.season.currentIndexChanged.connect(lambda: self.__update_season(self))

    self.radio_day.clicked.connect(lambda: self.__radio_group_data_form(self))
    self.radio_month.clicked.connect(lambda: self.__radio_group_data_form(self))
    self.radio_year.clicked.connect(lambda: self.__radio_group_data_form(self))
    self.radio_season.clicked.connect(lambda: self.__radio_group_data_form(self))

    self.checkBox_standard.stateChanged.connect(
        lambda: self.__checkbox_group_data_type(self))
    self.checkBox_deviation.stateChanged.connect(
        lambda: self.__checkbox_group_data_type(self))
    self.checkBox_deviation.setCheckable(False)

    self.radio_plot.clicked.connect(lambda: self.__radio_group_graph_type(self))
    self.radio_hist.clicked.connect(lambda: self.__radio_group_graph_type(self))
    self.radio_boxplot.clicked.connect(lambda: self.__radio_group_graph_type(self))

    self.btn_search.clicked.connect(lambda: self.__btn_search_clicked(self))
    self.btn_save_graph.clicked.connect(lambda: self.__btn_save_graph_clicked(self))

    self.start_day = self.de_start.date().toString("yyyyMMdd")
    self.end_day = self.de_end.date().toString("yyyyMMdd")

import sys
from enum import Enum
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtGui import *
from urllib.request import urlopen
from urllib.parse import urlparse, urlencode
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

form_class = uic.loadUiType("ui/seoul_temp_graph.ui")[0]

Idx = Enum("Idx", "DATE LOC MEAN_TEMP MIN_TEMP MAX_TEMP", start=0)

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dataFormCd = 'F00501'
        self.dataTypeCd = 'standard'
        
        self.setWindowTitle("Seoul Temperature Analyzer v0.1")
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout.addWidget(self.canvas)
        
        # period
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

        items = [str(i) for i in range(int(self.this_year), int(self.this_year) - 20, -1)]
        self.cb_start.addItems(items)
        self.gridLayout.addWidget(self.cb_start, 0, 0)
        self.cb_start.setCurrentIndex(10)
        self.cb_start.setVisible(False)
        self.start_year = self.cb_start.currentText()
        self.cb_start.currentIndexChanged.connect(self.update_start_year)

        self.cb_end = QComboBox(self)
        items = [str(i) for i in range(int(self.this_year), int(self.this_year) - 20, -1)]
        self.cb_end.addItems(items)
        self.gridLayout.addWidget(self.cb_end, 0, 2)
        self.cb_end.setVisible(False)
        self.end_year = self.cb_end.currentText()
        self.cb_end.currentIndexChanged.connect(self.update_end_year)

        self.cb_month_start = QComboBox(self)
        items = ["{:02d}".format(i) for i in range(1, 13)]
        self.cb_month_start.addItems(items)
        self.gridLayout.addWidget(self.cb_month_start, 0, 3)
        self.cb_month_start.setVisible(False)
        self.start_month = self.cb_month_start.currentText()
        self.cb_month_start.currentIndexChanged.connect(self.update_start_month)

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
        self.cb_month_end.currentIndexChanged.connect(self.update_end_month)

        self.season = QComboBox(self)
        ssaw = ['All', 'Spring', 'Summer', 'Autumn', 'Winter']
        self.season.addItems(ssaw)
        self.gridLayout.addWidget(self.season, 0, 3)
        self.season.setVisible(False)
        self.seasonCd = '0' # All
        self.season.currentIndexChanged.connect(self.update_season)

        self.radio_day.clicked.connect(self.radio_group_data_form)
        self.radio_month.clicked.connect(self.radio_group_data_form)
        self.radio_year.clicked.connect(self.radio_group_data_form)
        self.radio_season.clicked.connect(self.radio_group_data_form)

        self.checkBox_standard.stateChanged.connect(self.checkbox_group_data_type)
        self.checkBox_deviation.stateChanged.connect(self.checkbox_group_data_type)
        self.checkBox_deviation.setCheckable(False)

        self.radio_plot.clicked.connect(self.radio_group_graph_type)
        self.radio_hist.clicked.connect(self.radio_group_graph_type)
        self.radio_boxplot.clicked.connect(self.radio_group_graph_type)

        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_save_graph.clicked.connect(self.btn_save_graph_clicked)
        
        self.start_day = self.de_start.date().toString("yyyyMMdd")
        self.end_day = self.de_end.date().toString("yyyyMMdd")

    def radio_group_data_form(self):
        self.de_start.setVisible(False)
        self.period.setVisible(False)
        self.de_end.setVisible(False)

        self.cb_start.setVisible(False)
        self.cb_end.setVisible(False)
        self.cb_month_start.setVisible(False)
        self.period_month.setVisible(False)
        self.cb_month_end.setVisible(False)

        self.season.setVisible(False)

        if self.radio_day.isChecked():
            if self.de_start.isVisible() == False:                
                self.de_start.setVisible(True)
                self.period.setVisible(True)
                self.de_end.setVisible(True)
                self.dataFormCd = 'F00501'
                self.checkBox_standard.setChecked(True)
                self.checkBox_deviation.setCheckable(False)
        else:
            if self.radio_month.isChecked():
                self.cb_start.setVisible(True)
                self.cb_end.setVisible(True)
                self.cb_month_start.setVisible(True)
                self.period_month.setVisible(True)
                self.cb_month_end.setVisible(True)
                self.dataFormCd = 'F00513'
            elif self.radio_year.isChecked():
                self.cb_start.setVisible(True)
                self.cb_end.setVisible(True)
                self.dataFormCd = 'F00512'
            elif self.radio_season.isChecked():
                self.cb_start.setVisible(True)
                self.cb_end.setVisible(True)
                self.season.setVisible(True)
                self.dataFormCd = 'F00514'
            
            self.checkBox_deviation.setCheckable(True)

    def checkbox_group_data_type(self):
        if self.checkBox_standard.isChecked():
            self.dataTypeCd = 'standard'
        else: 
            self.dataTypeCd = 'deviation'

    def update_start_year(self):
        self.start_year = self.cb_start.currentText()

    def update_end_year(self):
        self.end_year = self.cb_end.currentText()
    
    def update_start_month(self):
        self.start_month = self.cb_month_start.currentText()
    
    def update_end_month(self):
        self.end_month = self.cb_month_end.currentText()
    
    def update_season(self):
        if self.season.currentText() == 'All':
            self.seasonCd = 0
        elif self.season.currentText() == 'Spring':
            self.seasonCd = 'DB004001'
        elif self.season.currentText() == 'Summer':
            self.seasonCd = 'DB004002'
        elif self.season.currentText() == 'Autumn':
            self.seasonCd = 'DB004003'
        else:
            self.seasonCd = 'DB004004'

    def radio_group_graph_type(self):
        if self.radio_plot.isChecked():
            self.graphType = 'plot'
        elif self.radio_hist.isChecked():
            self.graphType = 'hist'
        elif self.radio_boxplot.isChecked():
            self.graphType = 'boxplot'

    def btn_search_clicked(self):
        start_date = self.de_start.date()
        end_date = self.de_end.date()
        if self.dataFormCd == 'F00501':
            dt_fmt = "yyyyMMdd"
            self.start_dt = start_date.toString(dt_fmt)
            self.end_dt = end_date.toString(dt_fmt)
        else:
            if self.dataFormCd == 'F00513':
                dt_fmt = "yyyyMM"
                self.start_year = self.cb_start.currentText()
                self.start_month = self.cb_month_start.currentText()
                self.end_year = self.cb_end.currentText()
                self.end_month = self.cb_month_end.currentText()
            elif self.dataFormCd == 'F00514' or self.dataFormCd == 'F00512':
                dt_fmt = "yyyy"

            self.start_dt = self.cb_start.currentText()
            self.end_dt = self.cb_end.currentText()

        values = {
            'fileType': '',
            'pgmNo': '70', 'menuNo': '432', 'serviceSe': 'F00101', 'stdrMg': '99999',
            'startDt': '', 'endDt': '',
            # 'taElement': 'MIN', 'taElement': 'AVG', 
            'taElement': 'MAX', 'stnGroupSns': '',
            'selectType': '1', 'mddlClssCd': 'SFC01',
            'dataFormCd': '', 'dataTypeCd': '',
            'startDay': '', 'startYear': '', 'endDay': '', 'endYear': '', 'startMonth': '', 'endMonth': '',
            'sesnCd': '', 'txtStnNm': '서울', 'stnId': '108', 'areaId':'', 'gFontSize':''
            }
        
        if self.dataFormCd == 'F00501':
            self.start_day = self.start_dt
            self.end_day = self.end_dt
        
        # Common values
        values['startDt'] = self.start_dt
        values['endDt'] = self.end_dt
        values['dataFormCd'] = self.dataFormCd
        values['dataTypeCd'] = self.dataTypeCd
        values['startDay'] = self.start_day
        values['startYear'] = self.start_year
        values['endDay'] = self.end_day
        values['endYear'] = self.end_year
        values['startMonth'] = self.start_month
        values['endMonth'] = self.end_month
        
        values['sesnCd'] = self.seasonCd

        params = urlencode(values)
        print(f"After urlencode : {params}")
        API = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do"
        url = API + "?" + params

        response = urlopen(url)
        data = response.read()

        # # print("Before decode response :", data)
        text = data.decode("cp949")
        # print("After decode response :", text)
        data = text.split("\r\n")
        # print(len(data))

        # remove header
        del data[:8]
        del data[-2:]

        i = 0
        # make 2dList
        tmp = []
        for row in data:
            add = row.split(',')
            tmp.append(add)

            print(f"{i}: {row}")
            i += 1
        
        # print(f"tmp: {tmp}")
        high = []
        low = []

        for row in tmp:
            if row[Idx.MAX_TEMP.value] != '':
                row[Idx.MAX_TEMP.value] = float(row[Idx.MAX_TEMP.value])
                high.append(row[Idx.MAX_TEMP.value])
        
            if row[Idx.MIN_TEMP.value] == '':
                continue
        
            row[Idx.MIN_TEMP.value] = float(row[Idx.MIN_TEMP.value])
            low.append(row[Idx.MIN_TEMP.value])
        
        print(f"high: {high}")
        print(f"low: {low}")

        ax = self.fig.add_subplot(111)
        ax.plot(high, 'red', label='High')
        ax.plot(low, 'skyblue', label='Low')
        ax.legend(loc = "best")
        self.canvas.draw()


        # savename = 'temperature_from_' + start_dt + '_to_' + end_dt + '.csv'
        # with open(savename, mode ="wb") as f:
	    #     f.write(data)
    
    def btn_save_graph_clicked(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

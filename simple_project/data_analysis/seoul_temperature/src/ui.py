import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtGui import *
from urllib.request import urlopen
from urllib.parse import urlparse, urlencode
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

form_class = uic.loadUiType("ui/seoul_temp_graph.ui")[0]

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

        self.cur_date = QDate.currentDate()
        self.de_start.setDate(self.cur_date.addMonths(-1))
        self.de_end_minimum_date = self.cur_date.addDays(-1)
        self.de_end.setDate(self.de_end_minimum_date)
        self.de_end.setMaximumDate(self.de_end_minimum_date)

        self.radio_day.clicked.connect(self.radio_group_data_form)
        self.radio_month.clicked.connect(self.radio_group_data_form)
        self.radio_year.clicked.connect(self.radio_group_data_form)
        self.radio_season.clicked.connect(self.radio_group_data_form)
        self.radio_standard.clicked.connect(self.radio_group_data_type)
        self.radio_deviation.clicked.connect(self.radio_group_data_type)

        self.radio_plot.clicked.connect(self.radio_group_graph_type)
        self.radio_hist.clicked.connect(self.radio_group_graph_type)
        self.radio_boxplot.clicked.connect(self.radio_group_graph_type)

        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_save_graph.clicked.connect(self.btn_save_graph_clicked)


    def radio_group_data_form(self):
        if self.radio_day.isChecked():
            self.dataFormCd = 'F00501'
        elif self.radio_month.isChecked():
            self.dataFormCd = 'F00513'
        elif self.radio_year.isChecked():
            self.dataFormCd = 'F00514'
        elif self.radio_season.isChecked():
            self.dataFormCd = 'F00512'

    def radio_group_data_type(self):
        if self.radio_standard.isChecked():
            self.dataTypeCd = 'standard'
        elif self.radio_deviation.isChecked():
            self.dataTypeCd = 'deviation'

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
        fmt = "yyyyMM"
        start_dt = start_date.toString(fmt)
        end_dt = end_date.toString(fmt)

        values = {
            'fileType': 'csv',
            'pgmNo': '70', 'menuNo': '432', 'serviceSe': 'F00101', 'stdrMg': '99999',
            'startDt': start_dt,
            'endDt': end_dt,
            'taElement': 'MIN', 'taElement': 'AVG', 'taElement': 'MAX', 'stnGroupSns': '',
            'selectType': '1', 'mddlClssCd': 'SFC01',
            'dataFormCd': self.dataFormCd,
            'dataTypeCd': self.dataTypeCd,
            'startDay': '20000701',
            'startYear': '2010',
            'endDay': '20200821',
            'endYear': '2020',
            'startMonth': '01',
            'endMonth': '12',
            'sesnCd': '0',
            'txtStnNm': '서울',
            'stnId': '108',
            'areaId':'', 
            'gFontSize':''
            }
        
        params = urlencode(values)
        print(f"After urlencode : {params}")
        # API = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do"
        # url = API + "?" + params

        # response = urlopen(url)
        # data = response.read()

        # # print("Before decode response :", data)
        # text = data.decode("cp949")
        # # print("After decode response :", text)

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

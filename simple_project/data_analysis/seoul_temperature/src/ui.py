import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

form_class = uic.loadUiType("ui/seoul_temp_graph.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Seoul Temperature Analyzer v0.1")
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout.addWidget(self.canvas)

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
        pass
    
    def btn_save_graph_clicked(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

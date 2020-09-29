import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from view.widget import init_widget, btn_search_clicked

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

form_class = uic.loadUiType("ui/seoul_temp_graph.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        init_widget(self)
        btn_search_clicked(self)

    def init_ui(self):
        self.dataFormCd = 'F00501'
        self.dataTypeCd = 'standard'
        self.setWindowTitle("Seoul Temperature Analyzer v0.1")

        # font
        path = 'C:\\WINDOWS\\Fonts\\malgunsl.ttf'
        font_name = fm.FontProperties(fname=path, size=50).get_name()
        plt.rc('font', family=font_name)

        # minus
        plt.rcParams['axes.unicode_minus'] = False

        # graph
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout.addWidget(self.canvas)
        self.ax = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

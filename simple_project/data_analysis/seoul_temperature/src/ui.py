import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Seoul Temperature Analyzer v0.1")
        self.pushButton.clicked.connect(self.pushButtonClicked)


    def radio_group_box_func(self):
        if self.radio_day.isChecked():
            self.dataFormCd = F00501
        elif self.radio_month.isChecked():
            self.dataFormCd = F00513
        elif self.radio_year.isChecked():
            self.dataFormCd = F00514
        elif self.radio_season.isChecked():
            self.dataFormCd = F00512
		
    def pushButtonClicked(self):
        pass
		
	def save_file_btn_clicked(self):
        pass		

	def save_image_btn_clicked(self):
        pass
	

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/slider_and_dial.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # Vertical Slider
        self.v_slider.sliderMoved.connect(self.v_slider_move)
        self.v_slider.valueChanged.connect(self.v_slider_val_change)
        self.v_slider.rangeChanged.connect(self.v_slider_range_change)
        self.v_slider_info.clicked.connect(self.vslider_info)
        self.v_slider_range.clicked.connect(self.vslider_range)

        # Horizontal Slider
        self.h_slider.valueChanged.connect(self.h_slider_val_change)
        # self.h_slider.rangeChanged.connect(self.h_slider_range_change)
        self.h_slider_info.clicked.connect(self.hslider_info)
        self.h_slider_range.clicked.connect(self.hslider_range)

        # Dial
        self.dial.valueChanged.connect(self.dial_val_change)
        self.dial_info.clicked.connect(self.dial_info_print)
        self.dial_range.clicked.connect(self.dial_range_change)

    def v_slider_move(self):
        print("V Slider moved: {}".format(self.v_slider.value()))

    def v_slider_val_change(self):
        self.v_real_time.setText(str(self.v_slider.value()))

    def v_slider_range_change(self):
        print("Vertical Range Changed")

    def vslider_info(self):
        print("Vertical Slider ---")
        print("minimum: {}".format(self.v_slider.minimum()))
        print("maximum: {}".format(self.v_slider.maximum()))
        print("singleStep: {}".format(self.v_slider.singleStep()))
        print("pageStep: {}".format(self.v_slider.pageStep()))

    def vslider_range(self):
        self.v_slider.setRange(1, 200)
        self.v_slider.setSingleStep(10)
        self.v_slider.setPageStep(20)

    def h_slider_val_change(self):
        self.h_real_time.setText(str(self.h_slider.value()))

    def h_slider_range_change(self):
        print("Horizontal Range Changed")

    def hslider_info(self):
        print("Horizontal Slider ---")
        print("minimum: {}".format(self.h_slider.minimum()))
        print("maximum: {}".format(self.h_slider.maximum()))
        print("singleStep: {}".format(self.h_slider.singleStep()))
        print("pageStep: {}".format(self.h_slider.pageStep()))

    def hslider_range(self):
        self.h_slider.setRange(1, 200)
        self.h_slider.setSingleStep(10)
        self.h_slider.setPageStep(20)

    def dial_val_change(self):
        self.dial_real_time.setText(str(self.dial.value()))

    def dial_info_print(self):
        print("Dial ---")
        print("minimum: {}".format(self.dial.minimum()))
        print("maximum: {}".format(self.dial.maximum()))
        print("singleStep: {}".format(self.dial.singleStep()))
        print("pageStep: {}".format(self.dial.pageStep()))

    def dial_range_change(self):
        self.dial.setRange(1, 200)
        self.dial.setSingleStep(10)
        self.dial.setPageStep(20)


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
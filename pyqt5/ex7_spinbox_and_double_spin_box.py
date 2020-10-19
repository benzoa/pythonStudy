import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("ui/spin_box_and_double_spin_box.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Spin Box
        self.spin_box.valueChanged.connect(self.spbox_print)
        self.spin_box_info.clicked.connect(self.spbox_info)
        self.spin_box_change.clicked.connect(self.spbox_change)

        # Double Spin Box
        self.double_spin_box.valueChanged.connect(self.dspbox_print)
        self.double_spin_box_info.clicked.connect(self.dspbox_info)
        self.double_spin_box_change.clicked.connect(self.dspbox_change)

    def spbox_print(self):
        print("Spin Box: {}".format(self.spin_box.value()))

    def spbox_info(self):
        print("spin box ----")
        print("minimum: {}".format(self.spin_box.minimum()))
        print("maximum: {}".format(self.spin_box.maximum()))
        print("singleStep: {}".format(self.spin_box.singleStep()))

    def spbox_change(self):
        self.spin_box.setRange(1, 1000)
        self.spin_box.setSingleStep(10)

    def dspbox_print(self):
        print("Double Spin Box: {}".format(self.double_spin_box.value()))

    def dspbox_info(self):
        print("double spin box ----")
        print("minimum: {}".format(self.double_spin_box.minimum()))
        print("maximum: {}".format(self.double_spin_box.maximum()))
        print("singleStep: {}".format(self.double_spin_box.singleStep()))

    def dspbox_change(self):
        self.double_spin_box.setRange(1.0, 1000.0)
        self.double_spin_box.setSingleStep(0.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

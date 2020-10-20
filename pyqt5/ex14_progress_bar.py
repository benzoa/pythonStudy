import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5.QtCore import QTimer

form_class = uic.loadUiType("ui/progress_bar.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ProgressBar
        self.timer_start()

        self.progress_bar.valueChanged.connect(self.progress_bar_value_change)
        self.progress_bar_reset.clicked.connect(self.progress_bar_reset_val)
        self.progress_bar_range.clicked.connect(self.progress_bar_print_range)
        self.progress_bar_set_50.clicked.connect(self.progress_bar_set_val_50)
        self.progress_bar_new_range.clicked.connect(self.progress_bar_set_range)

    def timer_start(self):
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timer_timeout)
        self.timer.start()

    def timer_timeout(self):
        self.time = self.progress_bar.value()
        self.time += 1
        self.progress_bar.setValue(self.time)

        if self.time > self.progress_bar.maximum():
            self.timer.stop()

    def progress_bar_value_change(self):
        print(self.progress_bar.value())

    def progress_bar_reset_val(self):
        self.progress_bar.reset()

    def progress_bar_print_range(self):
        print("minimum: {}".format(self.progress_bar.minimum()))
        print("maximum: {}".format(self.progress_bar.maximum()))

    def progress_bar_set_val_50(self):
        self.progress_bar.setValue(50)

    def progress_bar_set_range(self):
        self.progress_bar.setRange(20, 90)
        self.progress_bar.setValue(self.progress_bar.value() + 20)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

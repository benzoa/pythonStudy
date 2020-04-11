import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/label_textbrowser.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # Label
        self.push_btn_change.clicked.connect(self.label_change)
        self.push_btn_print.clicked.connect(self.label_print)

        # TextBrowser
        self.text_brow__append.clicked.connect(self.tb_append)
        self.text_brow__to_plain_text.clicked.connect(self.tb_to_plain_text)
        self.text_brow__set_plain_text.clicked.connect(self.tb_set_plain_text)
        self.text_brow__clear.clicked.connect(self.tb_clear)

    def label_change(self):
        self.label.setText("Changed Label")

    def label_print(self):
        print(self.label.text())

    def tb_append(self):
        self.text_browers.append("Append Text")

    def tb_to_plain_text(self):
        print("TextBrowser: {}".format(self.text_browers.toPlainText()))

    def tb_set_plain_text(self):
        self.text_browers.setPlainText("TextBrowser")

    def tb_clear(self):
        self.text_browers.clear()


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
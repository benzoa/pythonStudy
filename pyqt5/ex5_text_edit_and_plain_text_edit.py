import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QColor
from PyQt5 import uic

form_class = uic.loadUiType("ui/text_edit_plain_text_edit.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # Text Edit
        self.fontSize = 10
        self.text_edit__print.clicked.connect(self.te_print)
        self.text_edit__clear.clicked.connect(self.te_clear)
        self.text_edit__set_font.clicked.connect(self.te_set_font)
        self.text_edit__set_red_color.clicked.connect(self.te_set_red_color)
        self.text_edit__set_italic.clicked.connect(self.te_set_italic)
        self.text_edit__set_underline.clicked.connect(self.te_set_underline)
        self.text_edit__size_up.clicked.connect(self.te_size_up)
        self.text_edit__size_down.clicked.connect(self.te_size_down)
        self.text_edit__set_text.clicked.connect(self.te_set_plain_text)
        self.text_edit__append.clicked.connect(self.te_append)

        # Plain Text Edit
        self.plain_text_edit__print.clicked.connect(self.pte_print)
        self.plain_text_edit__clear.clicked.connect(self.pte_clear)
        self.plain_text_edit__set_text.clicked.connect(self.pte_set_plain_text)
        self.plain_text_edit__append.clicked.connect(self.pte_append)

    def te_print(self):
        print("Text Edit: {}".format(self.text_edit.toPlainText()))

    def te_clear(self):
        self.text_edit.clear()

    def te_set_font(self):
        fontvar = QFont("Monaco", 10)
        self.text_edit.setCurrentFont(fontvar)

    def te_set_italic(self):
        self.text_edit.setFontItalic(True)

    def te_set_underline(self):
        self.text_edit.setFontUnderline(True)

    def te_set_red_color(self):
        te_color = QColor(255, 0, 0)
        self.text_edit.setTextColor(te_color)

    def te_size_up(self):
        self.fontSize += 1
        self.text_edit.setFontPointSize(self.fontSize)

    def te_size_down(self):
        self.fontSize -= 1
        self.text_edit.setFontPointSize(self.fontSize)

    def te_set_plain_text(self):
        self.text_edit.setText("This is Text Edit")

    def te_append(self):
        self.text_edit.append("Add Text")

    def pte_print(self):
        print("Plain Text Edit: {}".format(self.plain_text_edit.toPlainText()))

    def pte_clear(self):
        self.plain_text_edit.clear()

    def pte_set_plain_text(self):
        self.plain_text_edit.setPlainText("This is Plain Text Edit")

    def pte_append(self):
        self.plain_text_edit.appendPlainText("Append Text")


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
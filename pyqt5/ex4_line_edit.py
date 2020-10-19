import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("ui/line_edit.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # LineEdit
        self.le.textChanged.connect(self.le_change_label_text)
        self.le.returnPressed.connect(self.le_change_label)
        self.le_btn.clicked.connect(self.le_print)

    def le_change_label_text(self):
        self.le_label.setText(self.le.text())

    def le_change_label(self):
        self.le_label.setText("Changed Label" + self.le.text())

    def le_print(self):
        print("Line Edit: {}".format(self.le_label.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

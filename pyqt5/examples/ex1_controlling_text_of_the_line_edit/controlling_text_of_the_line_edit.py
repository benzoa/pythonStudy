import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5 import uic

form_class = uic.loadUiType("controlling_text_of_the_line_edit.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.echo_le.setFocus()

        self.echo_cb.activated.connect(self.echo_changed)
        self.validator_cb.activated.connect(self.validator_changed)
        self.alignment_cb.activated.connect(self.alignment_changed)
        self.input_mask_cb.activated.connect(self.input_mask_changed)
        self.access_cb.activated.connect(self.access_changed)

    def echo_changed(self, index):
        if index == 0:
            self.echo_le.setEchoMode(QLineEdit.Normal)
        elif index == 1:
            self.echo_le.setEchoMode(QLineEdit.NoEcho)
        elif index == 2:
            self.echo_le.setEchoMode(QLineEdit.Password)
        elif index == 3:
            self.echo_le.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    def validator_changed(self, index):
        if index == 0:
            self.validator_le.setValidator(None)
        elif index == 1:
            self.validator_le.setValidator(QIntValidator(-99, 99))
        elif index == 2:
            double_validator = QDoubleValidator(-999.0, 999.0, 2)
            double_validator.setNotation(QDoubleValidator.StandardNotation)
            self.validator_le.setValidator(double_validator)

        self.validator_le.clear()

    def alignment_changed(self, index):
        if index == 0:
            self.alignment_le.setAlignment(Qt.AlignLeft)
        elif index == 1:
            self.alignment_le.setAlignment(Qt.AlignCenter)
        elif index == 2:
            self.alignment_le.setAlignment(Qt.AlignRight)

    def input_mask_changed(self, index):
        if index == 0:
            self.input_mask_le.setInputMask('')
        elif index == 1:
            self.input_mask_le.setInputMask('000-0000-0000')
        elif index == 2:
            self.input_mask_le.setInputMask('0000-00-00')
            self.input_mask_le.setText('20190410')
            self.input_mask_le.setCursorPosition(0)
        elif index == 3:
            self.input_mask_le.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA;#')

    def access_changed(self, index):
        if index == 0:
            self.access_le.setReadOnly(False)
        elif index == 1:
            self.access_le.setReadOnly(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

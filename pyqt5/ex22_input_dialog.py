import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QInputDialog, QVBoxLayout, QApplication


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.pushButton = QPushButton("Input number")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        text, ok = QInputDialog.getInt(self, 'This is title', 'Content')
        if ok:
            self.label.setText(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

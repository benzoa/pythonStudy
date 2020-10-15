from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QComboBox


class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class QVLine(QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)


if __name__ == "__main__":
    app = QApplication([])
    widget = QWidget()
    layout = QGridLayout()

    layout.addWidget(QLabel("Test 1"), 0, 0, 1, 1)
    layout.addWidget(QComboBox(), 0, 1, 1, 1)
    layout.addWidget(QHLine(), 1, 0, 1, 2)
    layout.addWidget(QLabel("Test 2"), 2, 0, 1, 1)
    layout.addWidget(QComboBox(), 2, 1, 1, 1)

    widget.setLayout(layout)
    widget.show()
    app.exec_()

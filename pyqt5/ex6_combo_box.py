import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("ui/combo_box.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Combo Box
        self.sync_combo_box()
        self.combo_box.currentIndexChanged.connect(self.combo_change)
        self.combo_box_print.clicked.connect(self.combo_print)
        self.combo_box_clear.clicked.connect(self.combo_clear)
        self.combo_box_add.clicked.connect(self.combo_add)
        self.combo_box_delete.clicked.connect(self.combo_delete)

    def sync_combo_box(self):
        for i in range(self.combo_box.count()):
            self.combo_box2.addItem(self.combo_box.itemText(i))

    def combo_change(self):
        self.combo_label.setText(self.combo_box.currentText())

    def combo_print(self):
        print("Combo Box: {}".format(self.combo_box.currentText()))

    def combo_clear(self):
        self.combo_box.clear()
        self.combo_box2.clear()

    def combo_add(self):
        self.combo_box.addItem(self.combo_box_line_edit.text())
        self.combo_box2.addItem(self.combo_box_line_edit.text())

    def combo_delete(self):
        self.delidx = self.combo_box2.currentIndex()
        self.combo_box.removeItem(self.delidx)
        self.combo_box2.removeItem(self.delidx)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

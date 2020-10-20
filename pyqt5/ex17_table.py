import sys
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QApplication, QStyleFactory
from PyQt5 import uic
from PyQt5.QtCore import Qt

form_class = uic.loadUiType("ui/table.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # TableWidget
        self.old_col = 255

        column_cnt = self.tableWidget.columnCount()
        for i in range(column_cnt):
            header_item = self.tableWidget.horizontalHeaderItem(i)
            header_item.setBackground(Qt.lightGray)

        # self.tableWidget.cellChanged.connect(self.cellChanged)
        self.tableWidget.currentCellChanged.connect(self.curCellChanged)
        self.tableWidget.cellClicked.connect(self.cellClicked)
        self.tableWidget.cellDoubleClicked.connect(self.cellDoubleClicked)

        self.btn_tb_addItem.clicked.connect(self.addTableWidget)
        self.btn_tb_InsertItem.clicked.connect(self.insertTableWidget)

    def cellChanged(self):
        print("updated:", self.tableWidget.currentItem().text())

    def curCellChanged(self):
        print("changed:", self.tableWidget.currentItem().text())

    def cellClicked(self):
        print("clicked:", self.tableWidget.currentItem().text())
        cur_col = self.tableWidget.currentColumn()
        if cur_col != self.old_col:
            if self.old_col != 255:
                self.tableWidget.horizontalHeaderItem(self.old_col).setBackground(Qt.lightGray)
            self.old_col = cur_col

        self.tableWidget.horizontalHeaderItem(cur_col).setBackground(Qt.red)

    def cellDoubleClicked(self):
        print("double clicked:", self.tableWidget.currentItem().text())

    def addTableItem(self, tbRowCnt, name, skills, hobbies):
        self.tableWidget.setVerticalHeaderItem(tbRowCnt, QTableWidgetItem(name))
        self.tableWidget.setItem(tbRowCnt, 0, QTableWidgetItem(skills))
        self.tableWidget.setItem(tbRowCnt, 1, QTableWidgetItem(hobbies))

        newItemRow = self.tableWidget.item(tbRowCnt, 0)
        newItemRow.setTextAlignment(Qt.AlignCenter)

        newItemCol = self.tableWidget.item(tbRowCnt, 1)
        newItemCol.setTextAlignment(Qt.AlignCenter)

    def addTableWidget(self):
        tbRowCnt = self.tableWidget.rowCount()
        self.tableWidget.insertRow(tbRowCnt)

        name = self.tb_line_addItem_name.text()
        skills = self.tb_line_addItem_skills.text()
        hobbies = self.tb_line_addItem_hobbies.text()
        self.addTableItem(tbRowCnt, name, skills, hobbies)

    def insertTableWidget(self):
        tbInsertRow = self.tb_spin_insertRow.value()
        self.tableWidget.insertRow(tbInsertRow)
        self.addTableItem(tbInsertRow, "Kim", "Rust", "Boxing")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

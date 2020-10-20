import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("ui/list.ui")[0]


class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ListWidget
        self.listWidget.itemClicked.connect(self.chkItemClicked)
        self.listWidget.itemDoubleClicked.connect(self.chkItemDoubleClicked)
        self.listWidget.currentItemChanged.connect(self.chkCurrentItemChanged)

        self.btn_addItem.clicked.connect(self.addListWidget)
        self.btn_insertItem.clicked.connect(self.insertListWidget)

        self.btn_printItem.clicked.connect(self.printCurrentItem)
        self.btn_printMultiItems.clicked.connect(self.printMultiItems)
        self.btn_removeItem.clicked.connect(self.removeCurrentItem)
        self.btn_clearItem.clicked.connect(self.clearItem)

    def chkItemClicked(self):
        print(self.listWidget.currentItem().text())

    def chkItemDoubleClicked(self):
        print(str(self.listWidget.currentRow()) + " : " + self.listWidget.currentItem().text())

    def chkCurrentItemChanged(self):
        print("Current Row : " + str(self.listWidget.currentRow()))

    def addListWidget(self):
        self.addItemText = self.line_addItem.text()
        self.listWidget.addItem(self.addItemText)

    def insertListWidget(self):
        self.insertRow = self.spin_insertRow.value()
        self.insertText = self.line_insertItem.text()
        self.listWidget.insertItem(self.insertRow, self.insertText)

    def printCurrentItem(self):
        print(self.listWidget.currentItem().text())

    def printMultiItems(self):
        self.selectedList = self.listWidget.selectedItems()
        for i in self.selectedList:
            print(i.text())

    def removeCurrentItem(self):
        self.removeItemRow = self.listWidget.currentRow()
        self.listWidget.takeItem(self.removeItemRow)

    def clearItem(self):
        self.listWidget.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()

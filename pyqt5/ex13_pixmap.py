import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/pixmap.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # Pixmap
        self.pixmap_load_start_image()

        self.pixmap_load_file.clicked.connect(self.pixmap_load_local_img)
        self.pixmap_save.clicked.connect(self.pixmap_save_img)

    def pixmap_load_start_image(self):
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("resources/cat.jpg")
        self.img_size = self.qPixmapVar.size()
        print("start img: {}, {}".format(self.img_size.width(), self.img_size.height()))

        self.new_img = self.qPixmapVar.scaledToHeight(200)
        self.pixmap_lb.setPixmap(self.new_img)

    def pixmap_load_local_img(self):
        self.qPixmapVar.load("resources/cat-2143332_640.jpg")
        self.new_img = self.qPixmapVar.scaledToWidth(290)
        self.pixmap_lb.setPixmap(self.new_img)

    def pixmap_save_img(self):
        self.save_img = self.pixmap_lb.pixmap()
        self.save_img.save("img_cat.jpg")


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()

    app.exec_()
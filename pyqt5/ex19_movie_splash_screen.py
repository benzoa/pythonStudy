import sys
from PyQt5.QtGui import QPixmap, QPainter, QMovie
from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import QTimer


class MovieSplashScreen(QSplashScreen):
    def __init__(self, movie, parent=None):
        movie.jumpToFrame(0)
        pixmap = QPixmap(movie.frameRect().size())
        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self, event):
        self.movie.stop()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)

    def sizeHint(self):
        return self.movie.scaledSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    movie = QMovie("resources/cat2.gif")
    splash = MovieSplashScreen(movie)
    splash.show()

    def showWindow():
        splash.close()
        app.quit()
        # form.show()

    QTimer.singleShot(3000, showWindow)
    # form = MainWindow()
    app.exec_()

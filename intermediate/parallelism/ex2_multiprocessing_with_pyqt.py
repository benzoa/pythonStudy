import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal
from multiprocessing import Process, Queue, current_process
import datetime
import time


def producer(queue: Queue):
    proc = current_process()
    print(proc.name)

    while True:
        now = datetime.datetime.now()
        data = str(now)
        queue.put(data)
        time.sleep(1)


class Consumer(QThread):
    # make signal
    poped = pyqtSignal(str)

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.empty():
                data = self.queue.get()
                self.poped.emit(data)


class MyWindow(QMainWindow):
    def __init__(self, queue):
        super().__init__()
        self.setGeometry(200, 200, 300, 200)

        # thread for data consumer
        self.consumer = Consumer(queue)
        self.consumer.poped.connect(self.print_data)
        self.consumer.start()

    @pyqtSlot(str)
    def print_data(self, data):
        self.statusBar().showMessage(data)


if __name__ == "__main__":
    q = Queue()

    # producer process
    p = Process(name="Producer", target=producer, args=(q, ), daemon=True)
    p.start()

    # Main process
    app = QApplication(sys.argv)
    mywindow = MyWindow(q)
    mywindow.show()
    app.exec_()

from multiprocessing import Process, Queue
import time
import ctypes


STD_OUTPUT_HANDLE  = -11

PRODUCER    = 1
CONSUMER    = 2
TX          = 1
RX          = 2

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

def c_print(type, txrx, data):
    fmt = ''

    if type == PRODUCER:
        set_color(1)
        if txrx == TX:
            fmt = "<< Producer: {}".format(data)
        else:
            fmt = ">> Producer: {}\n".format(data)
    else:
        set_color(2)
        if txrx == TX:
            fmt = "<< Consumer: {}".format(data)
        else:
            fmt = ">> Consumer: {}".format(data)

    print(fmt)
    set_color(7)


def producer(queue):
    rx_data = 0
    tx_data = 1

    while True:
        if tx_data == 4:
            tx_data = 0xff
            c_print(PRODUCER, TX, tx_data)
            queue.put(tx_data)
            break

        c_print(PRODUCER, TX, tx_data)
        queue.put(tx_data)
        time.sleep(0.1)
        rx_data = queue.get()
        c_print(PRODUCER, RX, rx_data)
        tx_data += 1


def consumer(queue):
    rx_data = 0
    tx_data = 0

    while True:
        rx_data = queue.get()   # block=True, timeout=300
        c_print(CONSUMER, RX, rx_data)

        if rx_data == 0xff:
            break

        tx_data = rx_data * 2
        queue.put(tx_data)
        c_print(CONSUMER, TX, tx_data)
        time.sleep(0.1)


if __name__ == "__main__":
    queue = Queue()
    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))
    p1.start()
    p2.start()
    
    queue.close()
    queue.join_thread()

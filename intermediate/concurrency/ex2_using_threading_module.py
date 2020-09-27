import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
        print("sub thread start ", threading.currentThread().getName())
        time.sleep(3)
        print("sub thread end ", threading.currentThread().getName())


threads = []

print("main thread start")
for i in range(5):
    name = "thread {}".format(i)
    t = Worker(name)                # sub thread 생성
    t.daemon = True                 # sub thread를 daemon 스레드(메인 종료 시 함께 종료)로 생성
    t.start()                       # sub thread의 run 메서드 호출
    threads.append(t)

for thread in threads:
    thread.join()                   # sub thread가 종료될 때까지 대기

print("main thread post job")
print("main thread end")

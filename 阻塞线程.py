import threading
import time


def test():
    time.sleep(5)
    for i in range(10):
        print(i)


thread1 = threading.Thread(target=test)
thread1.start()
thread1.join()

print("主线程完成了")
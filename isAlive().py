import time
import threading


def test():
    time.sleep(5)
    for i in range(5):
        print(i)


thread1 = threading.Thread(target=test)
print('1. 当前的线程是否是活动的：', thread1.isAlive())
thread1.start()
print('2. 当前线程是否是活动的：', thread1.isAlive())
print('当前线程：', thread1.getName())
thread1.join()

print('The main thread has already completed!')
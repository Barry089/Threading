import time
import threading


class myThread(threading.Thread):
    def run(self):
        global x
        lock.acquire()
        for i in range(5):
            x += 10
        time.sleep(1)
        print(x)
        lock.release()


x = 0
lock = threading.RLock()


def main():
    threadLists = []
    for i in range(8):
        threadLists.append(myThread())

    for item in threadLists:
        item.start()

if __name__ == "__main__":
    main()

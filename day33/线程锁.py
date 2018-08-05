import threading
import time


def reduce():
    global s
    lock.acquire()
    temp = s
    time.sleep(0.01)
    s = temp - 1
    lock.release()


if __name__ == "__main__":
    l = []
    s = 100
    lock = threading.Lock()
    for i in range(100):
        t = threading.Thread(target=reduce)
        t.start()
        l.append(t)
    for i in l:
        i.join()

    print(s)


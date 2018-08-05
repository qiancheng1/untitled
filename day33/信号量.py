import threading
import time


class MyThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(2)
            semaphore.release()


if __name__ == "__main__":
    semaphore = threading.Semaphore(5)

    thrss =[]
    for i in range(100):
        thrss.append(MyThread())
    for t in thrss:
        t.start()

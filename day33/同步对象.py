import threading
import time


class Boss(threading.Thread):
    def run(self):
        print("i am boss,今天要加班到10点")
        print(event.isSet())
        event.set()
        time.sleep(5)
        print("<10:00 pm> now is time,众loser们可以下班了")
        event.set()
        # event.clear()

class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("%s 黑心老板又要加班,擦" % self.name)
        time.sleep(1)
        event.clear()
        event.wait()
        print("oh %s 下班了" % self.name)



if __name__ == '__main__':
    event = threading.Event()

    men_list = []
    for w in range(5):
        men_list.append(Worker())
    men_list.append(Boss())
    for w in men_list:
        w.start()
    for t in men_list:
        t.join()

    print("all done")
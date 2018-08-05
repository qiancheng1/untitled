# import threading
# import time
#
#
# class Mythread(threading.Thread):
#     def actionA(self):
#         a_lock.acquire()
#         print("%s got a_lock %s" %(self.name,time.ctime()))
#         time.sleep(0.5)
#
#         b_lock.acquire()
#         print("%s got b_lock %s" % (self.name, time.ctime()))
#         time.sleep(0.75)
#
#         a_lock.release()
#         b_lock.release()
#
#     def actionB(self):
#         b_lock.acquire()
#         print("%s got b_lock %s" % (self.name, time.ctime()))
#         time.sleep(1)
#
#         a_lock.acquire()
#
#
#     def run(self):
#         self.actionA()
#         self.actionB()
#
#
# if __name__ == "__main__":
#     a_lock = threading.Lock()
#     b_lock = threading.Lock()
#
#     l = []
#     for i in range(10):
#         t = Mythread()
#         t.start()
#         l.append(t)
#
#     for t in l:
#         t.join()
#
#     print("all ending")

############################################################
import threading
import time


class Mythread(threading.Thread):
    def actionA(self):
        r_lock.acquire()
        print("%s got a_lock %s" %(self.name,time.ctime()))
        time.sleep(0.5)

        r_lock.acquire()
        print("%s got b_lock %s" % (self.name, time.ctime()))
        time.sleep(0.75)

        r_lock.release()
        r_lock.release()

    def actionB(self):
        r_lock.acquire()
        print("%s got b_lock %s" % (self.name, time.ctime()))
        time.sleep(1)

        r_lock.acquire()
        print("%s got a_lock %s" % (self.name, time.ctime()))
        time.sleep(0.75)

        r_lock.release()
        r_lock.release()


    def run(self):
        self.actionA()
        self.actionB()


if __name__ == "__main__":
    r_lock = threading.RLock()

    l = []
    for i in range(5):
        t = Mythread()
        t.start()
        l.append(t)

    for t in l:
        t.join()

    print("all ending")
# import threading
# import time
# import random
# import queue
#
# mqueque = queue.Queue()
#
# def productor(name):
#     print('start to product,plz wait....')
#     time.sleep(random.randrange(4))
#     for i in range(100):
#         print('%s is product baozi' % name)
#         mqueque.put(i)
#
# def consumer(name):
#     print('start to eat baozi...')
#     time.sleep(random.randrange(3))
#     for i in range(100):
#         print("%s is eating baozi" % name)
#         if not mqueque.empty():
#             mqueque.get(i)
#
#
# if __name__ == '__main__':
#     chushi = threading.Thread(target=productor, args=('dahan',))
#     xiaofeizhe = threading.Thread(target=consumer, args=('big master',))
#     chushi.start()
#     xiaofeizhe.start()
#     chushi.join()
#     xiaofeizhe.join()
#
#     print("all done!")

##########################################################################
from queue import Queue
import random,threading,time

#生产者类
class Producer(threading.Thread):
    def __init__(self, name,queue):
        threading.Thread.__init__(self, name=name)
        self.data=queue

    def run(self):
        for i in range(5):
            print("%s is producing %d to the queue!" % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.randrange(10)/5)
        print("%s finished!" % self.getName())

#消费者类
class Consumer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            val = self.data.get()
            print("%s is consuming. %d in the queue is consumed!" % (self.getName(),val))
            time.sleep(random.randrange(10))
        print("%s finished!" % self.getName())

def main():
    queue = Queue()
    producer = Producer('Producer',queue)
    consumer = Consumer('Consumer',queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print('All threads finished!')

if __name__ == '__main__':
    main()
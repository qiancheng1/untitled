import threading
import time
import random

# 如果不用Queue该怎么实现
def productor():
    n = 0
    print('正在生产baozi...')
    while n<10:
        time.sleep(random.randrange(1, 3))
        n = n+3
        print("生产了 %s" % n)

def consumer(n):
    print('正在吃baozi....')
    while n<10:
        time.sleep(random.randrange(2,5))
        n = n -2
        print('%s吃了2个baozi' % threading.currentThread())
        if n == 0:
            print('溜了溜了')
            break


if __name__ == '__main__':
    chushi = threading.Thread(target=productor)
    chushi.start()
    consumer_list = []
    for i in range(5):
        consumers = threading.Thread(target=consumer)
        consumers.start()
        consumer_list.append(consumers)

    chushi.join()
    for i in consumer_list:
        i.join()

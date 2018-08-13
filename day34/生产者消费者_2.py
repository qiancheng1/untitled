import queue
import threading
import random
import time

mqueue = queue.Queue()

def product(name):
    n = 0
    while n < 10:
        print('%s zhengzai zhengchan baozi %s' %(name,n))
        mqueue.put(n)
        n += 1
        time.sleep(random.randrange(3))


def consumer(name):
    n = 0
    while n < 10:
        time.sleep(random.randrange(3))
        if not mqueue.empty():
            print('%s 正在吃包子 %s' %(name,n))
            mqueue.get(n)
        else:
            print('包子已经没有了,正在等待')
        n += 1



if __name__ == '__main__':
    chushi = threading.Thread(target=product,args=('娜美',))
    xiao = threading.Thread(target=consumer,args=('青雉',))

    chushi.start()
    xiao.start()

    chushi.join()
    xiao.join()

    print('all done ?')
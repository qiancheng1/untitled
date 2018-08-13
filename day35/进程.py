import multiprocessing
import time


def foo(name):
    time.sleep(1)
    print('%s was execute' % name)

if __name__ == '__main__':
    mlist = []
    for i in range(3):
        p = multiprocessing.Process(target=foo,args=('大熊%d' % (i+1),))
        p.start()
        mlist.append(p)
    for i in mlist:
        i.join()

    print('end')
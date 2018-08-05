'''
线程的join和setDaemon方法
'''
import threading
import time


def listening():
    print("start listening",time.ctime())
    time.sleep(3) #sleep等同于IO操作
    print('ending listening',time.ctime())

def recording():
    print('start to recording', time.ctime())
    time.sleep(5)
    print('ending recording',time.ctime())


if __name__ == '__main__':

    thread_list = []
    t1 = threading.Thread(target=listening)
    t2 = threading.Thread(target=recording)
    t2.setDaemon(True)
    thread_list.append(t1)
    thread_list.append(t2)
    for m_thread in thread_list:
        m_thread.start()
        # m_thread.join() #加成这样就变成线性的执行了,要等t1执行完才会执行t2
    # 加join的方法会阻塞住main,当两个都执行完才会执行线程之后的代码,否则的话main会立马结束,不会等待
    # 两个线程执行完.
    # 而setDaemon则会和main共进退.
    '''
    join方法就是阻塞的意思,其实执行完之后主线程还是要看两个线程的,从某种意义上来说主线程没有真正的结束,
    所以setDaemon和join方法不是相反的两个方法.
    '''
    print(threading.active_count())
    print('main thread ending')
    print(t2.isAlive())

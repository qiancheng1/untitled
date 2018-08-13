# 用列表来操作是线程不安全的.所以要用队列
# import threading,time
#
# li=[1,2,3,4,5]
#
# def pri():
#     while li:
#         a=li[-1]
#         print(a)
#         time.sleep(1)
#         try:
#             li.remove(a)
#         except Exception as e:
#             print('----',a,e)
#
# t1=threading.Thread(target=pri,args=())
# t1.start()
# t2=threading.Thread(target=pri,args=())
# t2.start()

##########################################################################
'''
Python Queue模块有三种队列及构造函数:
1、Python Queue模块的FIFO队列先进先出。   class queue.Queue(maxsize)
2、LIFO类似于堆，即先进后出。               class queue.LifoQueue(maxsize)
3、还有一种是优先级队列级别越低越先出来。        class queue.PriorityQueue(maxsize)

此包中的常用方法(q = Queue.Queue()):
q.qsize() 返回队列的大小
q.empty() 如果队列为空，返回True,反之False
q.full() 如果队列满了，返回True,反之False
q.full 与 maxsize 大小对应
q.get([block[, timeout]]) 获取队列，timeout等待时间
q.get_nowait() 相当q.get(False)
非阻塞 q.put(item) 写入队列，timeout等待时间
q.put_nowait(item) 相当q.put(item, False)
q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
q.join() 实际上意味着等到队列为空，再执行别的操作
'''
import queue #是线程队列 默认模式是FIFO

q = queue.Queue(5)
q.put('1')
q.put('2')
q.put('name')
q.put({"name":"dasha"})
q.put('',False)
# q.put('',False)

while True:
    # data = q.get(block=False)
    data = q.get()
    print(data)


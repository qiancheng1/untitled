from multiprocessing import Process,Queue

def foo(name,que):
    for i in range(10):
        que.put(i)

def smart(name,que):
    for i in range(10):
        print(que.get())

if __name__ == '__main__':
    q = Queue()
    p = Process(target=foo,args=('as',q))
    c = Process(target=smart,args=('s',q))
    p.start()
    c.start()
    # for i in range(10):
    #     print(q.get())
    p.join()
    c.join()
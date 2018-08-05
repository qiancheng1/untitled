# 用列表来操作是线程不安全的.所以要用队列

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


l= ["a","b","c","d"]

def test():
    return l.pop()

# 这里指的是运行到b的时候就结束了.
x = iter(test,"b")
print(x.__next__())
print(x.__next__())
# print(x.__next__()) #StopIteration


# 偏函数,用来固定函数的第一个参数
from functools import partial

def add(x,y):
    return x+y

fuc = partial(add,1)

print(fuc(1))
print(fuc(10))


# 所以之前的socket可以写成为:
# "".join(iter(partial(socket_service.recv,1024),b''))
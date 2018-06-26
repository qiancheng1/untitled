import datetime
import time
'''
函数对象有一个__name__属性,是属性不是函数,func.__name__() error
相当于执行 now = log(now)
'''
# def log(func):
#     def wapper(*args,**kw):
#         print("call %s" % func.__name__)
#         return func(*args,**kw)
#     return wapper

# #这个不行,error: TypeError: 'NoneType' object is not callable
# # 知道为什么不行吗 因为return wapper 缩进错误 ..........
# def deco(func):
#     def wapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         msec = (end_time - start_time) * 1000
#         print("count time is {0}".format(msec))
#     return wapper
#
# @deco
# def now():
#     time.sleep(2)
#     print(time.strftime("%Y%m%d"))
#     print(datetime.date(2012,9,12))
#
#
# #now = deco(now)
# now()
##########################################################################
'''
要为函数添加一个功能的话,就接收一个函数作为参数,在另一个函数中拓展功能
不改变函数的调用方式的话,就返回一个函数的引用,这样函数还能按照原来的方式来调用
'''
# import time
#
# def timmer(func):
#     def wapper(*args,**kw):
#         start = time.time()
#         func(*args,**kw)
#         end = time.time()
#         print("cost time {0}".format(end - start))
#         return func
#     return wapper
#
# @timmer
# def tes(l):
#     sum = 0
#     for i in l:
#         time.sleep(0.1)
#         sum += i
#     print(sum)
#
#
# l = [1,2,3,4,5]
# tes(l)



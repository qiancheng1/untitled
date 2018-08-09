import select

r,w,e = select.select([sk,],[],[])

# r监听的是socket对象,如果没有变化的话,r就为空,后面的for循环也不会执行.
for i in r:
    pass
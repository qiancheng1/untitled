from socket import *
import select

sk = socket(AF_INET,SOCK_STREAM)
sk.bind(('127.0.0.1',8086))
sk.listen(5)

while True:
    # 这个sk发生变化是什么时候? 当客户端调用connect()的时候,sk就会发生变化.
    # 如果在这后面加个时间,则注释掉14,15则不会发生变化,为什么? 因为在时间完成之后就结束了!?
    r,w,e = select.select([sk,],[],[],) #5表示监听事件,监听5s就不监听了,和sleep是有区别的.

    for i in r:
        # conn,addr = i.accept()
        # print(conn)
        print('sk')
    print(">")


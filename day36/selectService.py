import socket
import selectors

sel = selectors.DefaultSelector()

def accept(sk,mask):
    conn,addr = sk.accept()
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
    # data = conn.recv(1024)
    # if data:
    #     data = data.decode('utf-8')
    #     print(data)
    #     conn.send(str('answer','utf-8'))
    # else:
    #     print('close',conn)
    #     sel.unregister()
    #     conn.close()
    try:
        data = conn.recv(1024)
        if not data:
            raise Exception
        print('echo data',repr(data),'to',conn)
        conn.send(data.encode('utf8'))
    except Exception as e:
        sel.unregister(conn)
        conn.close()


sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('127.0.0.1',9090))
sk.listen(5)
sk.setblocking(False)

sel.register(sk,selectors.EVENT_READ,accept)

while True:
    event = sel.select()
    print("event >>>",event)
    for key,mask in event:
        callback = key.data #刚才注册绑定的函数
        callback(key.fileobj,mask) # fileobj是有反应的文件描述符

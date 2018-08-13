import socket
import select

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('127.0.0.1',9090))
sk.listen(5)
connections = [sk,]
while True:
    r,w,e = select.select(connections,[],[])
    print(len(r))

    for i in connections:
        if i == sk:
            conn,addr = i.accept()
            print(conn)
            connections.append(conn)
        else:
            data = conn.recv(1024)
            print(str(data,"utf-8"))
            inp = input('回答%s号客户>>' % connections.index(i))
            i.sendall(bytes(inp,'utf-8'))
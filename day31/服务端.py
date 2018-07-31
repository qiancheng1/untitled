import socket
# http://www.cnblogs.com/linhaifeng/articles/6129246.html#_label4
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 显示为timeout就用这个方法来解决
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(("127.0.0.1",8080))

phone.listen(3)

print("--->")
conn,addr = phone.accept() # 触发三次握手


msg = conn.recv(1024)
print("接收到的信息是",msg)

conn.send(msg.upper())

conn.close() # 触发四次挥手
phone.close()

# backlog 叫半链接池
# 三次握手发生在accept()阶段,剩下的就是传输了.已经建立了可靠链接

import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(("127.0.0.1",8080)) # 拨通电话

phone.send('hello'.encode("utf-8"))

msg = phone.recv(1024)
print("收到服务端信息为:",msg)
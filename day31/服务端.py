import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(("127.0.0.1",8080))

phone.listen(3)

print("--->")
conn,addr = phone.accept()


msg = conn.recv(1024)
print("接收到的信息是",msg)

conn.send(msg.upper())

conn.close()
phone.close()

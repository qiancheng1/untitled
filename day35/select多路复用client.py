import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('127.0.0.1',8086))

while True:
    inp = input(">>>").strip()
    sk.send(inp.encode('utf-8'))
    data = sk.recv(1024)
    print(data.encode('utf-8'))

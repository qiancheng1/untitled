import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9090))
while True:
    inp = input("<<<<")
    sk.send(inp.encode('utf-8'))
    data = sk.recv(1024)
    print(data.decode('utf-8'))
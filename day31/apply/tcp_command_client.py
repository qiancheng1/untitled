from socket import *

ip_port = ("127.0.0.1",8002)
buffer_size =1024

comm_client = socket(AF_INET,SOCK_STREAM)
comm_client.connect(ip_port)

while True:
    msg = input(">>>:").strip()
    if not msg:continue
    if msg == "quit":break
    comm_client.send(msg.encode("utf-8"))

    msg = comm_client.recv(buffer_size)
    print(msg.decode("gbk"))

comm_client.close()
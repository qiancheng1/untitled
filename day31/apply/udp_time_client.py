from socket import *
import time

ip_port = ("127.0.0.1",8081)
buffer_size = 1024

time_client = socket(AF_INET,SOCK_DGRAM)

while True:
    msg = input(">>>:").strip()
    if not msg:continue
    # 不起作用
    if msg == "quit":break
    time_client.sendto(msg.encode("utf-8"),ip_port)
    data,addr = time_client.recvfrom(buffer_size)

    # 没有达到想要的效果
    print(data.decode("utf-8"))

time_client.close()
from socket import *

ip_port = ("127.0.0.1",8002)
buffer_size =1024

comm_client = socket(AF_INET,SOCK_DGRAM)

while True:
    msg = input(">>>:").strip()
    if not msg:continue
    if msg == "quit":break
    comm_client.sendto(msg.encode("utf-8"),ip_port)

    msg,addr = comm_client.recvfrom(buffer_size)
    print("执行结果为:",msg)

comm_client.close()
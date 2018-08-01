from socket import *
import time

ip_port = ("127.0.0.1",8081)
buffer_size = 1024

time_service = socket(AF_INET,SOCK_DGRAM)
time_service.bind(ip_port)

while True:
    data,addr = time_service.recvfrom(buffer_size)
    if not data:break
    else:
        print(data)
    str_data = data.decode("utf-8")
    msg = time.strftime(str_data)
    time_service.sendto(msg.encode("utf-8"),addr)
time_service.close()
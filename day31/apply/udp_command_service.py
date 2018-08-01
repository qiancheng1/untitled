import subprocess
from socket import *

'''
recv()在接收为空时,阻塞
recvfrom()在接收为空是,输出空
'''
ip_port = ("127.0.0.1",8002)
buffer_size = 1024
back_log = 5

com_service = socket(AF_INET,SOCK_DGRAM)
com_service.bind(ip_port)

while True:
    data,addr = com_service.recvfrom(buffer_size)
    print(data,addr)
    if not data:
        break
    str_data = data.decode("utf-8")
    res = subprocess.Popen(str_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    err = res.stderr.read()
    print(res.stdout.read())
    if not err:
        msg = err
    else:
        msg = res.stdout.read()
    com_service.sendto(msg,addr)
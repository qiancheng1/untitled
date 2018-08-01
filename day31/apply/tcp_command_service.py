import subprocess
from socket import *


ip_port = ("127.0.0.1",8002)
buffer_size = 1024
back_log = 5

com_service = socket(AF_INET,SOCK_STREAM)
com_service.bind(ip_port)
com_service.listen(back_log)

while True:
    conn,addr = com_service.accept()
    print("新客户端连接:",addr)
    while True:
        try:
            data = conn.recv(buffer_size)
            if not data:
                break
            str_data = data.decode("utf-8")
            print(str_data)
            res = subprocess.Popen(str_data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            if not res.stderr.read():
                print(res.stderr.read())
            else:
                msg = res.stdout.read()
            conn.send(msg)
        except Exception as e:
            print(e)
            conn.close()

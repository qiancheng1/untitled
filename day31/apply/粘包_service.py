import subprocess
from socket import *

ip_port =("127.0.0.1",8011)
back_log = 5
buffer_size = 1024

ser = socket(AF_INET,SOCK_STREAM)
ser.bind(ip_port)
ser.listen(back_log)

while True:
    conn,addr = ser.accept()
    print("client addr is:",addr)

    while True:
        msg = conn.recv(buffer_size)
        if not msg:break
        print(msg)

        s = subprocess.Popen(msg.decode("utf-8"),shell=True,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        err = s.stderr.read()
        if err:
            ret = err
        else:
            ret = s.stdout.read()

        ret_len = len(ret)
        conn.send(str(ret_len).encode("utf-8"))

        data = conn.recv(buffer_size)
        if data.decode("utf-8") == "recv_ready":
            conn.sendall(ret)

    conn.close()

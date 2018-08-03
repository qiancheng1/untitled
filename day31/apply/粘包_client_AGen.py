from socket import *
import struct

ip_port =("127.0.0.1",8011)
back_log = 5
buffer_size = 1024

cli = socket(AF_INET,SOCK_STREAM)
cli.connect(ip_port)

while True:
    msg = input(">>>:").strip()
    if not msg:continue
    if msg == "quit":break

    cli.send(msg.encode("utf-8"))

    data = cli.recv(4)

    data_len = struct.unpack("i",data)[0]

    cli.send("recv_ready".encode("utf-8"))

    content = b''
    content_length = 0
    if content_length < data_len:
        content += cli.recv(buffer_size)
        content_length = len(content)

    print(content.decode("gbk"))
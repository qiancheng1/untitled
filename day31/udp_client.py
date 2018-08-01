from socket import *

ip_port = ("127.0.0.1",8080)

client = socket(AF_INET,SOCK_DGRAM)

while True:
    msg = input(">>>:").strip()
    client.sendto(msg.encode("utf-8"),ip_port)
    print("skr info was send")

client.close()
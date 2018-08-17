import socket

def main():
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # sk.bind(('localhost',8081))
    sk.bind(('localhost',8082))
    sk.listen(5)

    while True:
        conn,addr = sk.accept()
        conn.send(bytes("HTTP/1.1 201 OK\r\n\r\n","utf8"))
        conn.send('hello reboot'.encode('utf-8'))
        conn.close()

if __name__ == '__main__':
    main()
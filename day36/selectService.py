import socket
import selectors

sel = selectors.DefaultSelector()

def accept():
    pass

def read():
    pass


sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('127.0.0.1',9090))
sk.listen(5)
sk.setblocking(False)

sel.register(sk,selectors.EVENT_READ,accept)

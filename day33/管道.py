from multiprocessing import Process,Pipe
import time

def foo(conn):
    conn.send({"name":"you","things":None})
    print("child id <<<<",id(conn))
    print(conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    print('child id >>>>',id(child_conn))
    p = Process(target=foo,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    parent_conn.send('skr skr')
    p.join()
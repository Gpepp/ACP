from abc import ABC, abstractmethod
from interfaceSkeleton import InterfaceSkeleton
import multiprocessing as mp
import socket


def run_fun(conn, sk):
    msg = (conn.recv(sk.buffsize)).decode('utf-8')
    msg = msg.split('-')
    print(f"[Server] msg recive: {msg}")
    if msg[0] == "deposita":
        print(';boooo')
        resp = sk.deposita(msg[1])
    elif msg[0] == "preleva":
        resp = sk.preleva()
    else:
        resp = "CommandNotFound"
    
    conn.send(resp.encode('utf-8'))
    conn.close()

class Skeleton (InterfaceSkeleton, ABC):
    def __init__(self):
        self.buffsize = 1024

    @abstractmethod
    def deposita(self,id):
        raise NotImplementedError
    
    @abstractmethod
    def preleva(self):
        raise NotImplementedError
    

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost',0))

        print(f"[Server] Start at port: {s.getsockname()[1]}")

        s.listen(10)

        while True:
            conn, addr = s.accept()

            proc = mp.Process(target=run_fun, args=(conn, self))

            proc.start()

        s.close()
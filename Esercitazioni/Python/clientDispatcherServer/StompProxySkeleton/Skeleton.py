from SkeletonInterface import SkeletonInterface
from abc import ABC, abstractmethod
import multiprocessing as mp
import socket

def run_mp(conn, sk):
    msg = conn.recv(sk.buffsize).decode('utf-8')
    msg = msg.split('-')
    print(msg)
    response = 0
    if msg[0] == "deposita":
        response = sk.deposita(msg[1]).encode('utf-8')

    if msg[0] == "preleva":
        response = str(sk.preleva()).encode('utf-8')
    

    conn.send(response)
    conn.close()


class Skeleton(SkeletonInterface, ABC):
    def __init__(self, queue):
        self.queue = queue
        self.buffsize = 1024

    def deposita():
        pass
    def preleva():
        pass

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost',50501))


        s.listen(5)

        print("Sokcet start: ", s.getsockname())

        while True:
            conn, addr = s.accept()

            proc = mp.Process(target=run_mp, args=(conn,self))
            proc.start()

        s.close()

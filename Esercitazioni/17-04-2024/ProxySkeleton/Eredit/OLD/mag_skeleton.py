import socket, sys, time

from abc import ABC, abstractmethod
import threading as mt

from mag_services import MagServices

nreq = 30

def run_thread(conn, sk):
    msg = conn.recv(sk.buff)

    msg_split = msg.decode('utf-8').split('-')
    print("splitttttttttt ", msg_split)
    if msg_split[0] == 'deposita':
        sk.deposita(msg_split[1],msg_split[2])
        rsp = "ACK"
        conn.send(rsp.encode("utf-8"))
    elif msg_split[0] == 'preleva':
        el = sk.preleva(msg_split[1].encode("utf-8"))
        conn.send(el.encode("utf-8"))
    conn.close()

class MagSkeleton(MagServices, ABC):

    def __init__(self, host, port, buff):
        self.host = host
        self.port = port
        self.buff = buff
    
    @abstractmethod
    def deposita(self, art, id):
        pass
    
    @abstractmethod
    def preleva(self,id):
        pass
    

    def run_skeleton(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))

        print("host and port", s.getsockname()[0], s.getsockname()[1])

        s.listen(nreq)

        while True:
            conn, addr = s.accept()
            ths = []
            
            for i in range(nreq):
                t = mt.Thread(target=run_thread, args=(conn,self))
                t.start()
                ths.append(t)

            for i in range(nreq):
                ths[i].join()

        s.close()

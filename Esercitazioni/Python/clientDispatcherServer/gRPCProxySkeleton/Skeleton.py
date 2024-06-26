from SkeletonInterface import SkeletonInterface
import socket
import multiprocess as mp


def process_run(conn, sk):
    msg = conn.recv(sk.buffsize).decode('utf-8')
    msg = msg.split('-')
    print(msg)
    response = "error"
    if msg[0] == "deposita":
        response = sk.deposita(msg[1])
    if msg[0] == "preleva":
        response = sk.preleva()

    conn.send(response.encode('utf-8'))
    conn.close()
    

class Skeleton(SkeletonInterface):
    def __init__(self, impl, ip, port):
        self.delegate = impl
        self.host = ip
        self.port = port
        self.buffsize = 1024
    
    def deposita(self,id):
        return self.delegate.deposita(id)

    def preleva(self):
        return self.delegate.preleva()

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))

        s.listen(10)
        

        while True:
            conn, addr = s.accept()
            p = mp.Process(target = process_run, args=(conn,self))
            p.start()
        
        s.close()

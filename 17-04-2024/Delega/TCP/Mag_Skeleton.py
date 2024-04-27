from Mag_Interface import MagInterface
import socket
import logging as log
from Mag_Threads import MagThreads as thd

class MagSkeleton(MagInterface):
    def __init__(self, ip, port, obj):
        self.host = ip
        self.port = port
        self.delegate = obj
        self.buff = 1024

    def deposita(self, art, id_art):
        return self.delegate.deposita(art, id_art)

    def preleva(self, art):
        return self.delegate.preleva(art)

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        self.port = s.getsockname()[1]
        print(f'run_skeleton {self.host}:{self.port}') 
        log.warning('[SKELETON] SOCKET - START')

        s.listen(20)
        while True:
            conn, addr = s.accept()
            log.warning(f'[SKELETON] SOCKET - CONN_ACCEPT - {addr}')
            
            msg = conn.recv(self.buff).decode('utf-8')
            

            t = thd(conn, msg, self)
            t.start()

from interfaceSkeleton import IPrint
import socket
import threading as mt


def run_fun(msg, sk):
    msg = (msg.decode('utf-8')).split('-')
    print(f"[Server] recived msg {msg}")
    sk.print(msg[0],msg[1])

    
    

class Skeleton(IPrint):
    def __init__(self, _delegate):
        self.buffsize = 1024
        self.delegate = _delegate
    
    def print(self, path:str, tipo:str):
        self.delegate.print(path,tipo)
    

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('localhost', 0))

        print(f'[Server] Start printer at port: {s.getsockname()[1]}')

        while True:
            msg, addr = s.recvfrom(self.buffsize)

            th = mt.Thread(target=run_fun, args=(msg, self))
            th.start()

        s.close()
    

    
    
from ILogging import ILogging
from abc import ABC, abstractmethod
import socket
import multiprocessing as mp


def consumer_proc(servicer):
    print("Consuma start", servicer.buff)
    servicer.consuma()

def client_proc(servicer, conn):
    msg = conn.recv(servicer.buff).decode('utf-8')
    msg = msg.split('-')
    print(f"[Server - socket] messaggio ricevuto <{msg}>")
    servicer.log(msg[0], msg[1])

class LoggingServer(ILogging, ABC):
    def __init__(self):
        self.buff = 1024
        
    

    @abstractmethod
    def log(self, msgLog, tipo):
        pass
    
    @abstractmethod
    def consuma(self):
        pass


    def run(self):
        consumer = mp.Process(target=consumer_proc, args=(self,))
        consumer.start()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind(('localhost', 0))

        print(f"[Server] start at port: {s.getsockname()[1]}")

        s.listen(10)

        while True:
            conn, addr = s.accept()

            proc = mp.Process(target=client_proc, args=(self,conn))
            proc.start()

        s.close()

    
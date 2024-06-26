from abc import ABC, abstractmethod
import socket
import threading
from IPrinter import IPrinter_class

#todo opzionali
# send ack da server a client

class printerServerSkeleton_class(IPrinter_class, ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def print(self, pathFile: str, tipo: str):
        raise NotImplementedError
    
    def runSkeleton(self):
        # apri socket
        with socket.socket() as serverSock:
            serverSock.bind(('0.0.0.0', 0))
            print(f'[server] in ascolto su {serverSock.getsockname()}')
            serverSock.listen()
            while True:
                clientConn, clientAddr = serverSock.accept()
                worker = threading.Thread(target=runFunction, args=(clientConn, self))
                worker.start()
        # bind
        # listen
        # accept
        # gestisci

def runFunction(clientSock: socket.socket, skeleton: printerServerSkeleton_class):
    print('[server-worker] avviato')
    with clientSock as client:
        data = client.recv(1024).decode()
        print(data)

        #supponiamo data = pathfile-tipo
        skeleton.print(data.split('-')[0], data.split('-')[1])


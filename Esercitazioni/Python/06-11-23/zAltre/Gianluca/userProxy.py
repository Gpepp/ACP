import socket
from IPrinter import IPrinter_class

#todo opzionali: ricevi ack da server
class userProxy_class(IPrinter_class):

    def __init__(self, port) -> None:
        super().__init__()
        self.port = int(port)


    def print(self, pathFile: str, tipo: str):
        # apri socket
        with socket.socket() as sock:
            sock.connect(('0.0.0.0', self.port))
            request = f'{pathFile}-{tipo}'
            sock.send(request.encode())
            print(f'[client] invio {request=}')
        #connetti
        #manda dati
from Mag_Interface import MagInterface
import socket
import logging as log

class MagProxy (MagInterface):

    def __init__(self, ip, port):
        self.host = ip
        self.port = port

        self.bufsize = 1024

    def deposita(self, art, id_art):

        msg = '-'.join(['deposita',art, str(id_art)])

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self.host, self.port))

        s.send(msg.encode('utf-8'))

        return (s.recv(self.bufsize)).decode('utf-8')

    def preleva(self, art):
        
        msg = '-'.join(['preleva',art])

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self.host, self.port))

        s.send(msg.encode('utf-8'))

        return (s.recv(self.bufsize)).decode('utf-8')

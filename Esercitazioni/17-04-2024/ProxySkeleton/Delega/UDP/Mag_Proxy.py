from Mag_Interface import MagInterface
import socket
import logging as log

class MagProxy (MagInterface):

    def __init__(self, ip, port):
        self.addr = (ip, port)

        self.bufsize = 1024

    def deposita(self, art, id_art):

        msg = '-'.join(['deposita',art, str(id_art)])

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.sendto(msg.encode('utf-8'), self.addr)

        response, addr = s.recvfrom(self.bufsize)

        return response.decode('utf-8')


    def preleva(self, art):
        
        msg = '-'.join(['preleva',art])

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.sendto(msg.encode('utf-8'), self.addr)

        response, addr = s.recvfrom(self.bufsize)

        return response.decode('utf-8')

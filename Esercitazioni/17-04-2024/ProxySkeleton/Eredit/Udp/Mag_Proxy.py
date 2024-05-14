from Mag_Services import MagServices
import socket

class MagProxy(MagServices):

    def __init__(self, ip, _port):
        self.host = ip
        self.port = _port
        self.buff = 1024

    def deposita(self, art, id_art):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        address = (self.host, self.port)

        msg = '-'.join(['deposita',art,str(id_art)])
        s.sendto(msg.encode('utf-8'),address)

        response, addr = s.recvfrom(self.buff)
        return bool(response)

    def preleva(self, art):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (self.host, self.port)
    
        msg = '-'.join(['preleva',art])
        s.sendto(msg.encode('utf-8'), address)
        
        response, addr = s.recvfrom(self.buff)
        return int(response)

from Mag_Services import MagServices
import socket

class MagProxy(MagServices):

    def __init__(self, ip, _port):
        self.host = ip
        self.port = _port
        self.buff = 1024

    def deposita(self, art, id_art):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))

        msg = '-'.join(['deposita',art,str(id_art)])
        s.send(msg.encode('utf-8'))

        response = s.recv(self.buff)
        return bool(response)

    def preleva(self, art):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
    
        msg = '-'.join(['preleva',art])
        s.send(msg.encode('utf-8'))
        
        response = s.recv(self.buff)
        return int(response)

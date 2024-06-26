from mag_services import MagServices
import socket

class Proxy_Mag(MagServices):
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.buff = 1024


    def deposita(self, art, id):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        msg = '-'.join(['deposita',art,id])
        s.send(msg.encode('utf-8'))
        res = s.recv(self.buff)
        print("[Proxy] - deposita -", res.decode('utf-8'))
        return res.decode('utf-8')


    def preleva(self, articolo):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        msg = '-'.join(['preleva',articolo])

        s.send(msg.encode('utf-8'))

        res = s.recv(self.buff)
        print('[Proxy] - preleva -', res.decode('utf-8'))
        return res.decode('utf-8')



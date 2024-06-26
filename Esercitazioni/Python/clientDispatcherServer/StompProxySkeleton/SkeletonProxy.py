import socket
from SkeletonInterface import SkeletonInterface


class SkeletonProxy(SkeletonInterface):
    def __init__(self, ip, port):
        self.host = ip
        self.port = port
        self.buffsize = 1024
    
    def deposita(self, id):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host,self.port))
        msg = "deposita-" + id
        s.send(msg.encode('utf-8'))

        response = s.recv(self.buffsize)
        s.close()
        return response.decode('utf-8')

    def preleva(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host,self.port))
        msg = "preleva-"
        s.send(msg.encode('utf-8'))

        response = s.recv(self.buffsize)

        s.close()
        return response.decode('utf-8')
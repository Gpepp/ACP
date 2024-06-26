from interfaceSkeleton import IPrint
import socket

class Proxy (IPrint):
    def __init__(self, port, host):
        self.address = (host,port)
    
    def print(self, path:str, tipo:str):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        msg = '-'.join([path, tipo])
        print(f"[Proxy] send message: {msg}")
        s.sendto(msg.encode('utf-8'),self.address)
    
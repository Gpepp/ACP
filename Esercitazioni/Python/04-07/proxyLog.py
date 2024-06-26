from ILogging import ILogging
import socket


class ProxyLog(ILogging):
    def __init__(self, host, port):
        self.host = host
        self.port = port
    

    def log(self, msgLog, tipo):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))

        msg = '-'.join([msgLog, str(tipo)])

        s.send(msg.encode('utf-8'))
        s.close()
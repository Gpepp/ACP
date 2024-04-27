from Mag_Services import MagServices
from abc import ABC, abstractmethod
import socket
import threading as mt
import logging as log
log.basicConfig(filename='info.log',format='%(levelname)s - %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def run_thread(conn, sk):
    log.warning('[SKELETON] thread run_fun')
    msg = conn.recv(sk.buffsize)
    msg_split = msg.decode('utf-8').split('-')
    print(msg_split)

    if msg_split[0] == 'deposita':
        log.info('[SKELETON] - deposito')
        response = sk.deposita(msg_split[1], msg_split[2])
        print(f'[SKELETON] depositato - {msg_split[1]} - {msg_split[2]}')
        log.warning(f'[SKELETON] depositato - {msg_split[1]} - {msg_split[2]}')
    elif msg_split[0] == 'preleva':
        response = sk.preleva(msg_split[1])
        print(f'[SKELETON] prelevato - {msg_split[1]} - {response}')
        log.warning(f'[SKELETON] prelevato - {msg_split[1]} - {response}')
    else:

        response = 'Incorrect Command'
        print('[SKELETON] IncorrectCommand')
        log.critical('[SKELETON] IncorrectCommand')

    response = str(response).encode('utf-8')

    conn.send(response)
    conn.close()

class MagSkeleton(MagServices, ABC):

    def __init__(self, ip, _port):
        self.host = ip
        self.port = _port
        self.buffsize = 1024
        self.req = 30


    @abstractmethod
    def deposita(self, art, id_art):
        pass

    @abstractmethod
    def preleva(self, art):
        pass

    def run_skeleton(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        self.port = s.getsockname()[1]
        print(f"Socket start:  {self.host}:{self.port}")

        s.listen(self.req)

        while True:
            conn, addr = s.accept()
            log.info(f'[SKELETON] connection accept {conn}, {addr}')
            t = mt.Thread(target = run_thread, args=(conn, self))
            t.start()


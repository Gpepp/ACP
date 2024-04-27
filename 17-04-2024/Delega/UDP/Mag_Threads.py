import threading as mt
import logging as log

class MagThreads(mt.Thread):
    
    def __init__(self, s, msg, addr, ref):
        super().__init__()
        self.conn = s
        self.addr = addr
        self.msg = msg
        self.ref = ref

    def run(self):
        
        log.info('[THREAD_SKELETON] - START')
        self.msg = self.msg.split('-')

        if self.msg[0] == 'deposita':
            response = (str(self.ref.deposita(self.msg[1], self.msg[2]))).encode('utf-8')
            log.warning('[THREAD_SKELETON] - SEND - DEPOSITA')
            self.conn.sendto(response, self.addr)

        elif self.msg[0] == 'preleva':
            response = (self.ref.preleva(self.msg[1])).encode('utf-8')
            self.conn.sendto(response, self.addr)
            log.warning('[THREAD_SKELETON] - SEND - PRELEVA')
        else:
            resposne = 'COMMAND NOT FOUND'.encode('utf-8')
            self.conn.sendto(response, self.addr)
            log.warning('[THREAD_SKELETON] - SEND - COMMAND_NOT_FOUND')

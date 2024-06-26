from loggingServer import LoggingServer

import multiprocessing as mp

import stomp

class ImplLoggingServer(LoggingServer):
    def __init__(self):
        super().__init__()
        self.process_safe = mp.Queue()

    
    def log(self, msgLog, tipo):
        messaggioLog = '-'.join([msgLog,tipo])
        self.process_safe.put(messaggioLog)

    def stompConnection(self):
        self.conn = stomp.Connection([('localhost', 61613)])
        self.conn.connect(wait=True)

    def stompSend(self, queue, message):
        
        self.conn.send(f'/queue/{queue}', message)
        print(f"[Server - Consuma] Messaggio <{message}> inviato su coda <{queue}>")

    def consuma(self):
        self.stompConnection()
        while True:
            if not self.process_safe.empty():
                msg = self.process_safe.get()
                print(f"[Server - Consuma] messaggio prelevato {msg}")
                msg_split = msg.split('-')
                if int(msg_split[1]) == 2:
                    self.stompSend('error', msg)
                else:
                    self.stompSend('info', msg)



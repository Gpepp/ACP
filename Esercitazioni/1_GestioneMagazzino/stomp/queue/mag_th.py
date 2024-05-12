from threading import Thread

class MagTh(Thread):
    
    def run(self):
        try:
            self.conn = stomp.Connection([(self.host,61613)], auto_content_length=False)
            self.conn.connect(wait=True)
        except:
            print('Errore in connessione')
            raise 
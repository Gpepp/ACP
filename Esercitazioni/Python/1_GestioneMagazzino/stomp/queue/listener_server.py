import stomp
import threading 

class Listener_server(stomp.ConnectionListener, threading.Thread):

    def __init__(self, nam, mag):
        self.name = nam
        self.do = mag

    def run(self):
        try:
            self.conn = stomp.Connection([(self.host,61613)], auto_content_length=False)
            self.conn.connect(wait=True)
        except:
            print('Errore in connessione')
            raise 

    def on_connected(self, frame):
        print('Connessione avvenuta', frame)


    def on_message(self, frame):
        print('Recived Frame')
        print(frame)
        if msg.split('-')[0] == 'deposita':
            msg = f'deposited {msg.split('-')[1]}'
        if msg.split('-')[0] == 'preleva':
            msg = 'prelevato'
        else:
            pass
        self.conn.send('/queue/response', msg)

    #def on_send(self,frame):
    #    print('on_send:',frame)

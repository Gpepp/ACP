import stomp


class Listener(stomp.ConnectionListener):

    def __init__(self, conn):
        self.con = conn

    def on_message(self, frame):
        print('Recived Frame')
        print(frame)

    def on_send(self,frame):
        print('on_send:',frame)

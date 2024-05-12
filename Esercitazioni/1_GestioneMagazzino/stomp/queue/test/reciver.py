import time, stomp

exit = False

class Listener(stomp.ConnectionListener):

    def __init__(self, conn):
        self.con = conn

    def on_message(self, frame):
        print('Recived Frame')
        print(frame)
        if frame.body == 'exit':
            self.con.disconnect()
            exit = True

    def on_send(self,frame):
        print('on_send:',frame)

    def on_connected(self, frame):
        print('connessione avvenuta', frame)


if __name__ == '__main__':

    my_con = stomp.Connection([('127.0.0.1',61613)])
    my_con.set_listener('', Listener(my_con))

    my_con.connect(wait=True)
    my_con.subscribe(destination='/queue/my_test', id=1, ack='auto')


    while not exit:
        time.sleep(10)
        print(exit) 

    

    my_con.disconnect()

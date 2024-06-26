import stomp, time

class MyListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print("Messaggio ricevuto: ", frame.body)


con = stomp.Connection([('localhost', 61613)])
con.set_listener('', MyListener())
con.connect(wait=True)

con.subscribe('/queue/error',1)
con.subscribe('/queue/info',2)

time.sleep(20000)
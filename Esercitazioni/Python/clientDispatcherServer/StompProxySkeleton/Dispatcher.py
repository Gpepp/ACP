import stomp, socket, time
import multiprocess as mp
from SkeletonProxy import SkeletonProxy as Proxy

class MyListener(stomp.ConnectionListener):

    def __init__(self, conn, host, port):
        self.MOM = conn
        self.host = host
        self.port = port

    def on_message(self, frame):
        print(frame.body)

        p = mp.Process(target=processCall, args=(frame.body, self.MOM, self.host, self.port))
        p.start()


def processCall(msg, MOM, h, p):
    px = Proxy(h,p)
    msg = msg.split('-')
    print(f"messaggio - {msg}")
    response = -1
    if msg[0] == "deposita":
        response = px.deposita(msg[1])
    if msg[0] == "preleva":
        response = px.preleva()

    MOM.send('/queue/response', response)


if __name__ == "__main__":
    port = 50501
    host = "localhost"
    conn = stomp.Connection([(host, 61613)])
    conn.set_listener('', MyListener(conn, host, port))
    conn.connect()
    
    conn.subscribe(destination='/queue/requests', id=3, ack='auto')
    

    time.sleep(20000)





import stomp, time
from random import randint


class Listener(stomp.ConnectionListener):
    def on_message(self,frame):
        print(frame.body)
    
prod = ['Laptop', "Smartphone"]

def deposita(conn):

    for i in range(10):
        id = randint(0, 20)
        msg = '-'.join(["deposita",prod[id%2], str(id)])
        conn.send('/queue/requests', msg)


def preleva(conn):
    for i in range(5):
        msg = "preleva"
        conn.send('/queue/requests', msg)


def svuota(conn):
    msg = "svuota"
    conn.send('/queue/requests', msg)



if __name__ == "__main__":
    conn = stomp.Connection([("localhost", '61613')])
    conn.set_listener("", Listener())
    conn.connect()

    conn.subscribe("/queue/response", id =3)

    deposita(conn)
    preleva(conn)
    svuota(conn)

    time.sleep(20000)
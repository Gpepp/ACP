import stomp, time
from uuid import uuid4 as genID


class MyListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print("[CLIENT] Recivedresponse: ", frame.body)


if __name__ == "__main__":
    ip = 'localhost'
    stomp_Port = 61613

    MOM = stomp.Connection([(ip,stomp_Port)])
    MOM.set_listener('', MyListener())
    MOM.connect()

    MOM.subscribe('/queue/response', id=2, ack='auto')

    for i in range(10):
        if i%2:
            id = genID()
            msg = "deposita-"+id.hex

            MOM.send("/queue/requests", msg)
        else:
            MOM.send("/queue/requests", "preleva-")
    

    time.sleep(20000)

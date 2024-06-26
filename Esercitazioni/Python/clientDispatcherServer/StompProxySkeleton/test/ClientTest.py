import stomp, time
from uuid import uuid4 as genID


class MyListener(stomp.ConnectionListener):

    def on_message(self, frame):
        print("[TEST] Recivedresponse: ", frame.body)


if __name__ == "__main__":
    ip = 'localhost'
    stomp_Port = 61613

    MOM = stomp.Connection([(ip,stomp_Port)])
    MOM.set_listener('', MyListener())
    MOM.connect()

    MOM.subscribe(destination='/queue/requests',id=1, ack='auto')

    for i in range(10):
        if i%2==0:
            msg = "deposited"
            MOM.send("/queue/response", msg)
        else:
            MOM.send("/queue/response", "id")
    

    time.sleep(20000)

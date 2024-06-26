import stomp, time

class MyListener(stomp.ConnectionListener):

    def __init__(self, conn) -> None:
        self.conn = conn

    def on_message(self, frame):
        msg = (frame.body).split('-')
        print(f"Mesage: {msg}\nheaders {frame.headers}")

        if msg[0] == "deposita":
            conn.send(frame.headers['reply-to'],'/'.join(msg))
        else:
            conn.send(frame.headers['reply-to'],'/'.join(msg))


conn = stomp.Connection([('127.0.0.1', 61613)])
conn.set_listener('', MyListener(conn))
conn.connect(wait=True)
conn.subscribe("/queue/requests",2)


time.sleep(20000)


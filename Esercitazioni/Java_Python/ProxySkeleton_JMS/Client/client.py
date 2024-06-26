import stomp, time, sys
from random import randint

class myListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print(f"Messaggio ricevuto: {frame.body}")



def run(conn):
    for _ in range(10):
        id = randint(0,100)
        if id%2 ==0:
            msg = f"deposita-{id}"
        else:
            msg = "preleva"
        
        print(f"[Client] msg: {msg}")
        conn.send('/queue/requests', body=msg, headers={'reply-to': '/queue/response'})




if __name__ == "__main__":

    
    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    conn.set_listener('', myListener())
    conn.connect(wait=True)
    conn.subscribe('/queue/response',1)


    run(conn)
    time.sleep(20000)
    

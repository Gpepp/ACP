import stomp, time

class MyListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print("[Error Chcker] message: ", frame.body)
        with open("error.txt", mode='a') as file:
            file.write(frame.body+'\n')



if __name__ == "__main__":
    
    conn = stomp.Connection([('localhost', 61613)])
    conn.set_listener('', MyListener())
    conn.connect(wait=True)

    conn.subscribe('/queue/error',1)
    time.sleep(20000)
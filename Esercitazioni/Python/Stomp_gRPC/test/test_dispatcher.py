import stomp, time


class Listener(stomp.ConnectionListener):
    def on_message(self,frame):
        print(frame.body)
    


if __name__ == "__main__":
    conn = stomp.Connection([("localhost","61613")])
    conn.set_listener("", Listener())
    conn.connect()

    conn.subscribe("/queue/response", id=2)

    conn.send("/queue/requests", "deposita-laptop-10")

    time.sleep(10)
    print("resumeProgram...")

    conn.send("/queue/requests", "preleva")

    time.sleep(30000)

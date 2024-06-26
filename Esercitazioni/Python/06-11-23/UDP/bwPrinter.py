import sys, stomp, time

accepted_cmd = ['bw', 'sg']

class MyListener(stomp.ConnectionListener):
    def __init__(self, command) -> None:
        self.command = command
    
    def on_message(self, frame):
        if (frame.body).split('-')[1] == str(self.command):
            print(f"messaggio da coda {self.command}: ", frame.body)
            with open(f'{self.command}.txt', mode='a') as file:
                file.write(frame.body+'\n')
    

if __name__ == "__main__":

    try:
        cmd = sys.argv[1]
        if cmd not in accepted_cmd:
            raise ValueError
    except IndexError:
        print("Insert command")
        sys.exit(-2)
    except ValueError:
        print("Insert valid command ", accepted_cmd)
        sys.exit(-1)
    

    with open(f'{cmd}.txt', mode='a') as file:
        file.write(f'--------- {cmd}/{time.time()} ---------\n')

    conn = stomp.Connection([("localhost", 61613)])
    conn.set_listener('', MyListener(cmd))
    conn.connect(wait=True)
    conn.subscribe('/queue/bw',1)

    time.sleep(2000)
    conn.disconnect()
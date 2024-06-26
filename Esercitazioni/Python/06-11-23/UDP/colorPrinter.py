import sys, stomp, time

accepted_cmd = ['doc', 'txt']

class MyListener(stomp.ConnectionListener):
    def __init__(self, command) -> None:
        self.command = command
    
    def on_message(self, frame):
        if (frame.body.split('-')[0]).split('.')[1] == self.command:
            print(f"Messaggio da coda {self.command}: ", frame.body)
            with open('color.txt', mode='a') as file:
                file.write(frame.body+'\n')
    

if __name__ == "__main__":

    try:
        cmd = sys.argv[1]
        if cmd not in accepted_cmd:
            raise ValueError
    except IndexError:
        print("Insert command")
    except ValueError:
        print("Insert valid command ", accepted_cmd)
    

    with open('color.txt', mode='a') as file:
        file.write(f'--------- {cmd}/{time.time()} ---------\n')
    

    conn = stomp.Connection([("localhost", 61613)])
    conn.set_listener('', MyListener(cmd))
    conn.connect(wait=True)
    conn.subscribe('/queue/color',1)

    time.sleep(2000)
    conn.disconnect()
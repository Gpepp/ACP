import threading
import stomp


class ConsumerThread(threading.Thread):
    def __init__(self, queue, lock, cvCons):
        super().__init__()
        self.queue = queue
        self.lock = lock
        self.cvCons = cvCons

    def run(self):
        conn = stomp.Connection([('localhost', 61613)])
        conn.connect(wait=True)

        while True:
            with self.cvCons:
                while len(self.queue) == 0:
                    self.cvCons.wait()
                
                msg = self.queue.pop()
            
            msg_split = msg.split('-')

            print(f"[Consumer - Thread] messaggio perlevato: {msg_split}")

            if msg_split[1] == 'color':
                conn.send('/queue/color', msg)
            else:
                conn.send('/queue/bw', msg)
        

        conn.disconnect()

            
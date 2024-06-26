import sys
from time import sleep
import stomp

class bwListener(stomp.ConnectionListener):
    def __init__(self, stringaTerminale) -> None:
        super().__init__()
        self.stringTerminale = stringaTerminale

    def on_message(self, frame):
        # estrai contenuto messaggio
        msg = frame.body
        # confronto con stringa passata da terminale
        if msg.split('-')[1] == self.stringTerminale:
            with open('bw.txt', 'a') as file:
                file.write(f'{msg}\n')
                print(f'Ricevuto {msg=}')
                # if true, scrive su bw.txt e stampa il messagiio ricevuto

TIPI = ('bw', 'gs')

if __name__ == '__main__':
    try:
        stringaTerminale = sys.argv[1]
        if stringaTerminale not in TIPI:
            raise TypeError
    except IndexError:
        print('specificare stringa terminale')
        sys.exit(-1)
    except TypeError:
        print('specificare correttamente la stringa')
        sys.exit(-2)


    connection = stomp.Connection([('127.0.0.1', 61613)])
    connection.set_listener('', bwListener(stringaTerminale))
    connection.connect(wait=True)
    connection.subscribe('/queue/bw', id = 1)
    while True:
        sleep(10)
    connection.disconnect()

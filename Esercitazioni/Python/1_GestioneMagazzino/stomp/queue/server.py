import logging as log
from mag import Magazzino
import stomp
import sys
from listener_server import Listener_server

     
        
'''
def start_analyzer():
    log.warning('Analyzer Start')

    conn = stomp.Connection([('127.0.0.1',61613)], auto_content_length=False)
    conn.connect(wait=True)
'''

if __name__ == "__main__":
   
    mag = Magazzino()
    log.debug("[SERVER] - Magazzino avviato")

    ls = Listener_server(nam='Server', mag=mag)
    ls.start()
    log.debug("[SERVER] - Listener avviato")

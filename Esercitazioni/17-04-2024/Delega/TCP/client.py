from Mag_Proxy import MagProxy
from threading import Thread
import logging as log, sys
from random import randint


thn = 5
articles = ['smartphone', 'laptop']

def run_thd(ip, Port, type_r):
    for n in range(3):
        art = articles[randint(0,1)]
        px = MagProxy(ip, Port)
        if type_r == 'd':
            id_art = randint(1,100)
            resp = px.deposita(art,id_art)
            print(f'Articolo - {art}_{id_art} - Depositato: {resp}')
            
        elif type_r == 'p':
            resp = px.preleva(art)
            print(f'Articolo - {art} - Prelevato: {resp}')
        


if __name__ == "__main__":

    try:
        host = sys.argv[1].split(':')[0]
        port = int(sys.argv[1].split(':')[1])

        type_req = sys.argv[2]
    except:
        print("Insert valid host:port type_req (p, d)")

        
    thds = []

    for i in range(thn):
        t = Thread(target = run_thd, args = (host, port, type_req))
        t.start()

    for i in thds:
        i.join()

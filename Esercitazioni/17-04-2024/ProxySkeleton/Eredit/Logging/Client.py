import sys, random, time
from Mag_Proxy import MagProxy as proxy
import threading as mt
import logging as log

log.basicConfig(filename='info.log', format='%(levelname)s - %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

n_req = 5
articoli = ['smartphone', 'laptop']

def run_fun(ip, _port, req):
    log.info('[CLIENT] run_fun thread start')
    rrand = random.randint(2, 4)
    time.sleep(rrand)
    px = proxy(ip, _port)
    for i in range(3):
        art = random.randint(0,1)
        if req == 'd':
            response = px.deposita(articoli[art], random.randint(1,100))
            print(f'[CLIENT] - deposito - {articoli[art]} - {response}')
            log.warning(f'[CLIENT] - deposito - {articoli[art]} - {response}')

        elif req == 'p':
            response = px.preleva(articoli[art])
            print(f'[CLIENT] - prelievo - {articoli[art]} - {response}')
            log.warning(f'[CLIENT] - prelievo - {articoli[art]} - {response}')
        


if __name__ == '__main__':

    try:
        host = sys.argv[1].split(':')[0]
        port = int(sys.argv[1].split(':')[1])
        type_req = sys.argv[2]
    except:
        print('Error: insert host:port type_req (d/p)')
        log.critical('[CLIENT] Error: insert host:port type_req (d/p)')
        sys.exit(-1)

    print(type_req)
#    if type_req != 'p' or type_req !='d':
#        print('Invalid type_req')
#        sys.exit(-1)
    

    ths = []

    for i in range(n_req):
        t = mt.Thread(target = run_fun, args = (host, port, type_req))
        t.start()
        log.info('[CLIENT] Thread create')
        ths.append(t)

    for th in ths:
        th.join()
        

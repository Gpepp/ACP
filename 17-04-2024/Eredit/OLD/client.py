import threading as mt
from mag_proxy import Proxy_Mag as px
import sys, time, random

nclient = 5

def client_req(host, port, type_req):
    n = 0
    dispositivi = ['Smartphone', 'Laptop']
    
    if type_req == 'd':
        while n<3:
            rrand = random.randint(2,4)
            time.sleep(rrand)
            req_px = px(host, port)
            
            response = req_px.deposita(dispositivi[rrand%2], str(random.randint(1,100)))
            print('[Client]: deposito -', response)
            n = n + 1
    elif type_req == 'p':
        while n < 3:
            rrand = random.randint(2,4)
            time.sleep(rrand)
            req_px = px(host,port)
            response = req_px.preleva(dispositivi[rrand%2])
            
            print('[Client]: prelievo -', response)
            n = n + 1



if __name__ == "__main__":
    try:
        h = sys.argv[1].split(':')[0]
        p = sys.argv[1].split(':')[1]
        r = sys.argv[2]
    except IndexError:
        print("Specify host:port e tipo_req (d, p)")
        sys.exit(-1)
    

    clients=[]

    for i in range(nclient):
        cl = mt.Thread(target=client_req, args=(h, int(p), r))
        cl.start()
        clients.append(cl)

    for i in range(nclient):
        clients[i].join()





import sys, time
from random import randint
from proxyLog import ProxyLog as proxy

msgLog_accepted  = ['success', 'checking', 'fatal', 'exception']


def run(port):
    px = proxy("localhost", port=port)

    for i in range(10):
        tipo = randint(0,2)
        msgLog = ''
        if tipo == 2:
            r = randint(0,10)%2
            msgLog = msgLog_accepted[(r+2)]
        else:
            msgLog = msgLog_accepted[tipo%2]
        
        px.log(msgLog, tipo)
        time.sleep(1)



if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except IndexError:
        print("Insert Valid port")

    run(int(port))
    

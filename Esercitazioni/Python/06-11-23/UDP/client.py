import socket, sys, time
from random import randint
from proxy import Proxy 

accepted_tipo = ['doc', 'txt']
accepted_color = ['bw', 'sg', 'color']

def run(port):
    for _ in range(10):
        num_file = randint(0, 100)
        tipo = accepted_tipo[randint(0,1)]
        color = accepted_color[randint(0,2)]
        path = f"/user/file_{num_file}.{tipo}"
        px = Proxy(port, "localhost")
        px.print(path=path, tipo=color)
        
        time.sleep(1)


if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except IndexError:
        print("Insert port")
        sys.exit(-2)
    run(port)

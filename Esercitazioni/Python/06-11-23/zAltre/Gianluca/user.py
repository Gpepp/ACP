import random
import sys

from userProxy import userProxy_class

TIPI = ('bw','gs', 'color')
ESTENSIONI = ('doc', 'txt')

NUM_RICHIESTE_STAMPA = 10
SLEEP_TIME = 1


if __name__ == '__main__':
    try:
        serverPort = sys.argv[1]
    except IndexError:
        print('specifica serverPort')
        sys.exit(-1)

    proxy = userProxy_class(serverPort)
    for _ in range(NUM_RICHIESTE_STAMPA):
        pathFile = f'/user/file_{random.randint(0,100)}.{ESTENSIONI[random.randint(0,1)]}'
        tipo = TIPI[random.randint(0,2)]
        proxy.print(pathFile, tipo)
    
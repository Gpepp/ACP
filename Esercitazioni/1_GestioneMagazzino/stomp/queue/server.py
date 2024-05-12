import threading as mt
import logging as log

def start_sender():
    log.warning('Sender start')
    
    conn = stomp.Connection([('127.0.0.1',61613)], auto_content_length=False)
    conn.connect(wait=True)
    while True:
        msg = input('Inserisci comando-tipo: ')
        if msg.split('-')[0] == 'deposita':
            con



def start_reciver():
    log.warning('Reciver Start')
    
    conn = stomp.Connection([('127.0.0.1',61613)], auto_content_length=False)
    conn.connect(wait=True)

def start_analyzer():
    log.warning('Analyzer Start')

    conn = stomp.Connection([('127.0.0.1',61613)], auto_content_length=False)
    conn.connect(wait=True)

if __name__ == "__main__":
    ths = []

    th = mt.Thread(name='Analyzer', target = start_analyzer)
    ths.append(th)
    th = mt.Thread(name='Sender', target=start_sender)
    ths.append(th)
    th = mt.Thread(name='Reciver', target=start_reciver)
    ths.append(th)

    # Start thread
    for th in ths:
        th.start()
        log.warning(f'Thread {th.name} start')


    # join Thread
    for th in ths:
        th.join()

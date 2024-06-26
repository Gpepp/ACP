import multiprocess
import multiprocess.queues

from printerServerImpl import printerServerImpl_class
import stomp

def consuma(queue: multiprocess.queues.Queue):
    print('[processo-consumatore] avviato')
    connection = stomp.Connection([('127.0.0.1', 61613)])
    print('[server] connessione stomp stabilita')
    while True:
        # preleva la stringa
        request = queue.get()
        print(request)
        # inserisi in messaggio stomp
        connection.connect(wait=True)
        print(request.split('-')[1] )
        if request.split('-')[1] == 'color':
            connection.send('/queue/color', request)
            print(f'[server] inviato {request} su /queue/color')
            # in queue.color se tipo==color
        else:
            connection.send('/queue/bw', request)
            print(f'[server] inviato {request} su /queue/bw')
            # in queue.bw else
    


if __name__ == '__main__':
    impl = printerServerImpl_class()
    # avvia processo consumatore

    consumatore = multiprocess.context.Process(target=consuma, args=(impl.coda,))
    consumatore.start()

    impl.runSkeleton()

    
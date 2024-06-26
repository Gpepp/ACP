import multiprocess.queues
from printerServerSkeleton import printerServerSkeleton_class
import multiprocess

class printerServerImpl_class(printerServerSkeleton_class):
    def __init__(self) -> None:
        super().__init__()
        self.coda = multiprocess.Queue(100)

    def print(self, pathFile: str, tipo: str):
        print('[printeserverImpl] avviato')
        produttore = multiprocess.context.Process(target=self.produci, args=(pathFile, tipo))
        produttore.start()


    def produci(self, pathfile, tipo):
        print('[processo-produttore] avviato')
        msgConcat = f'{pathfile}-{tipo}'
        self.coda.put(msgConcat)
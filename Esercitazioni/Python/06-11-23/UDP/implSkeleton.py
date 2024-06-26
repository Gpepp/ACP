from interfaceSkeleton import IPrint
import threading as mt


class ImplSkeleton(IPrint):
    def __init__(self, queue, lock, cvCons):
        self.queue = queue
        self.lock = lock
        self.cvCons = cvCons

    def print(self, path:str, tipo:str):
        msg = '-'.join([path, tipo])
        with self.lock:
            self.queue.append(msg)
            self.cvCons.notify()
        
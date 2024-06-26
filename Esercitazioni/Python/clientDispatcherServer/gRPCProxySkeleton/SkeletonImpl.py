from SkeletonInterface import SkeletonInterface
import multiprocess as mp

class SkeletonImpl (SkeletonInterface):

    def __init__(self, queue_size):
        self.queue = mp.Queue()
    

    def deposita(self, id):
        self.queue.put(id)
        return "deposited"
    
    def preleva(self):
        el = self.queue.get()
        return el

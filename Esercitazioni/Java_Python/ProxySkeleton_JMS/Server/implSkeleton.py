from skeleton import Skeleton

import multiprocessing as mp


class ImplSkeleton (Skeleton):
    def __init__(self):
        super().__init__()
        self.queue = mp.Queue(5)
    
    def deposita(self,id):
        self.queue.put(id)
        return "deposited"
    
    def preleva(self):
        return self.queue.get()
    

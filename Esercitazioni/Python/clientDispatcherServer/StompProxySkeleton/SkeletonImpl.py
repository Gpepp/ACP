from Skeleton import Skeleton

class SkeletonImpl(Skeleton):
    def deposita(self, id):
        self.queue.put(id)
        return "deposited"

    def preleva(self):
        el = self.queue.get()
        return el
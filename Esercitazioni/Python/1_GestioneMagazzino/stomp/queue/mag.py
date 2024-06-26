from threading import Lock, Condition

class Magazzino():

    def __init__(self):
        self.lap = []
        self.smart = []

        self.lock_lap = Lock()
        self.empty_lap = Condition(self.lock_lap)
        self.lock_smart = Lock()
        self.empty_smart = Condition(self.lock_smart)

    def deposita(self, id, art):
        if art == 'laptop':
            with self.lock_lap:
                self.lap.append(id)
                self.empty_lap.notify()
            resp = id
        if art == 'smartphone':
            with self.lock_smart:
                self.smart.append(id)
                self.empty_smart.notify()
            resp = id
        else:
            resp = -1

        return resp
    
    def preleva(self, art):
        if art == 'laptop':
            with self.empty_lap:
                while len(self.lap) == 0:
                    self.empty_lap.wait()

                resp = self.lap.pop()
        if art == 'smartphone':
            with self.empty_smart:
                while len(self.smart) == 0:
                    self.empty_smart.wait()

                resp = self.smart.pop()
        else:
            resp = -1

        return resp
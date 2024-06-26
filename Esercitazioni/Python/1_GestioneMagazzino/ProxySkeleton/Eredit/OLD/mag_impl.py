from mag_skeleton import MagSkeleton
import threading as mt
import queue as Q

class MagImpl(MagSkeleton):
    def __init__ (self, host, port, buff, queueSmartphone=Q.Queue(5), queueLaptop=Q.Queue(5)):
        super().__init__(host, port, buff)
        self.queueS = queueSmartphone
        self.queueL = queueLaptop
        self.lockS = mt.Lock()
        self.lockL = mt.Lock()
        self.condSD = mt.Condition(self.lockS)
        self.condSP = mt.Condition(self.lockS)
        self.condLD = mt.Condition(self.lockL)
        self.condLP = mt.Condition(self.lockL)

    def deposita(self, art, id):
        if art == "Smartphone":
            with self.condSD:
                while self.queueS.full():
                    self.condSD.wait()
                
                self.queueS.put(id)
                self.condSP.notify()


        if art == "Laptop":
            with self.condLD:
                while self.queueL.full():
                    self.condLD.wait()

                self.queueL.put(id)
                self.condLP.notify()

        else:
            pass


    def preleva(self, art):
        el = -1
        if art == "Smartphone":
            with self.condSP:
                while queueS.empty():
                    print("Wait_Smartphone")
                    self.condSP.wait()
                el = self.queueS.get()
                self.condSD.notify()
        if art == "Laptop":
            with self.condLP:
                while self.queueL.empty():
                    print("Wait_Laptop")
                    self.condSP.wait()
                    self.condLP.wait()

                el = self.queueL.get()
                self.condLD.notify()
        else:
            pass
        return str(el)

from Mag_Interface import MagInterface
from threading import Lock, Condition as cv
import logging as log

class MagImplement(MagInterface):
    
    def __init__(self, que_max_size):
        self.que_max = que_max_size
        self.laptop = []
        self.smartphone = []

        #Define Lock
        self.lockS = Lock()
        self.lockL = Lock()
        
        #Define Condition
        self.cv_smart_prod = cv(lock = self.lockS)
        self.cv_smart_cons = cv(lock = self.lockS)
        self.cv_laptop_prod = cv(lock = self.lockL)
        self.cv_laptop_cons = cv(lock = self.lockL)

        #Log initalized
        log.info("[MAG_IMPL] Initialized")


    def deposita(self, art, id_art):

        if art == 'smartphone':
            with self.cv_smart_prod:
                while len(self.smartphone) == self.que_max:
                    log.warning("[MAG_IMPL] DEPOSITA - QUEUE_SMARRPHONE - FULL - WAIT")
                    self.cv_smart_prod.wait()

                self.smartphone.append(id_art)
                log.warning(f"[MAG_IMPL] DEPOSITA - QUEUE_SMARTPHONE - {id_art}")
                self.cv_smart_cons.notify()
                return True
        elif art == 'laptop':
            with self.cv_laptop_prod:
                while len(self.laptop) == self.que_max:
                    log.warning("[MAG_IMPL] DEPOSITA - QUEUE_LAPTOP - FULL - WAIT")
                    self.cv_laptop_prod.wait()

                self.laptop.append(id_art)
                log.warning(f"[MAG_IMPL] DEPOSITA - QUEUE_LAPTOP - {id_art}")
                self.cv_laptop_cons.notify()
                return True
        else:
                log.critical("[MAG_IMPL] DEPOSITA - ERROR_ART")
                return False 
    

    def preleva(self, art):

        if art == 'smartphone':
            with self.cv_smart_cons:
                while len(self.smartphone) == 0:
                    log.warning("[MAG_IMPL] PRELEVA - QUEUE_SMARTPHONE - EMPTY - WAIT")
                    self.cv_smart_cons.wait()

                el = self.smartphone.pop(0)
                log.warning(f"[MAG_IMPL] PRELEVA - QUEUE_SMARTPHONE - {el}")
                self.cv_smart_prod.notify()
                return el

        elif art == 'laptop':
            with self.cv_laptop_cons:
                while len(self.laptop) == 0:
                    log.warning("[MAG_IMPL] PRELEVA - QUEUE_LAPTOP - EMPTY - WAIT")
                    self.cv_laptop_cons.wait()

                el = self.laptop.pop(0)
                log.warning(f"[MAG_IMPL] PRELEVA - QUEUE_LAPTOP - {el}")
                self.cv_laptop_prod.notify()
                return el
        else:
                log.critical("[MAG_IMPL] PRELEVA - ERROR_ART")
                return -1

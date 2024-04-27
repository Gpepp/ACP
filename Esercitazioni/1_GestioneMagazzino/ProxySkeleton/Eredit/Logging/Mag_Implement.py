from Mag_Skeleton import MagSkeleton
import threading as mt
import logging as log
log.basicConfig(filename='info.log',format='%(levelname)s - %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class MagImplement(MagSkeleton):

    def __init__(self, ip, port):
        super().__init__(ip, port)
        self.max = 5
        self.smartphone = []
        self.smartphone_count = 0
        self.laptop = []
        self.laptop_count = 0
        self.lock_s = mt.Lock()
        self.lock_l = mt.Lock()
        self.cond_s_p = mt.Condition(lock= self.lock_s)
        self.cond_s_c = mt.Condition(lock= self.lock_s)
        self.cond_l_p = mt.Condition(lock= self.lock_l)
        self.cond_l_c = mt.Condition(lock= self.lock_l)
        self.fileS = 'smartphone.txt'
        self.fileL = 'laptop.txt'
        log.info('[MAG_IMPL] Initialized')

    def deposita(self, art, id_art):
        log.info('[MAG_IMPL] Deposita')
        if art == 'smartphone':
            with self.cond_s_p:
                while len(self.smartphone) == self.max:
                    self.cond_s_p.wait()
                self.smartphone.append(id_art)
                self.cond_s_c.notify()
            return True
        elif art == 'laptop':
            with self.cond_l_p:
                while len(self.laptop) == self.max:
                    self.cond_l_p.wait()
                self.laptop.append(id_art)
                self.cond_l_c.notify()
            return True
        else:
            log.critical('[MAG_IMPL] - Deposita - Type of art err')
            return False

    def preleva(self, art):
        el = - 1
        if art == 'smartphone':
            with self.cond_s_c:

                while len(self.smartphone) == 0:
                    self.cond_s_c.wait()

                el = self.smartphone.pop(0)

                with open(self.fileS, mode = 'a') as file:
                    file.write(f'{art} - {el}')
                self.cond_s_p.notify()
            
            return el

        elif art == 'laptop':
            with self.cond_l_c:
                while  len(self.laptop) == 0:
                    self.cond_l_c.wait()
                el = self.laptop.pop(0)

                with open(self.fileL, mode = 'a') as file:
                    file.write(f'{art} - {el}')
                
                self.cond_l_p.notify()
            return el
        else:
            log.critical('[MAG_IMPL] - Preleva - Type of art err')
            return el



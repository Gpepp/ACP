from abc import ABC, abstractmethod

class SkeletonInterface(ABC):
    
    @abstractmethod
    def deposita(self, id):
        pass

    @abstractmethod
    def preleva(self):
        pass
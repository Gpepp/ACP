from abc import ABC, abstractmethod

class SkeletonInterface(ABC):

    @abstractmethod
    def deposita(self, id):
        raise NotImplementedError
        
    @abstractmethod
    def preleva(self):
        raise NotImplementedError
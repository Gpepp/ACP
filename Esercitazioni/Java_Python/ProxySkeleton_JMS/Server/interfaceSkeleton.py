from abc import ABC, abstractmethod

class InterfaceSkeleton(ABC):
    
    @abstractmethod
    def deposita(self,id):
        raise NotImplementedError
    
    @abstractmethod
    def preleva(self):
        raise NotImplementedError
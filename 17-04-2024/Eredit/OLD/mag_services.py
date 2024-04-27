from abc import ABC, abstractmethod



class MagServices(ABC):

    @abstractmethod
    def deposita(self, art, id):
        raise NotImplementedError
    
    @abstractmethod
    def preleva(self,id):
        raise NotImplementedError
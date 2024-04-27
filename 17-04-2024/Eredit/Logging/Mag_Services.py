from abc import ABC, abstractmethod

class MagServices(ABC):

    @abstractmethod
    def deposita(self, art, id_art):
        raise NotImplementedError
    
    @abstractmethod
    def preleva(self, art):
        raise NotImplementedError

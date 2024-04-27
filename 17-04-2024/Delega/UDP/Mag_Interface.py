from abc import ABC, abstractmethod

class MagInterface(ABC):

    @abstractmethod
    def deposita(self, art, id_art):
        pass

    @abstractmethod
    def preleva(self, art):
        pass

from abc import ABC, abstractmethod

class IPrint(ABC):
    def print(self, path:str, tipo:str):
        raise NotImplementedError
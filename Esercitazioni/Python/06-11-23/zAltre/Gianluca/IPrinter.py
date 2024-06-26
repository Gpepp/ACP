from abc import ABC, abstractmethod


class IPrinter_class(ABC):
    @abstractmethod
    def print(self, pathFile: str, tipo:str):
        raise NotImplementedError
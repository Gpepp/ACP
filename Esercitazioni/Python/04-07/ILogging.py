from abc import ABC, abstractmethod


class ILogging(ABC):

    @abstractmethod
    def log(self, msgLog, tipo):
        raise NotImplementedError
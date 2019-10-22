from abc import ABC
from abc import abstractmethod

class Robot(ABC):
    """
    Classe Robot

    Classe qui modélise un robot comme un object abstrait
    """

    @abstractmethod
    def k(self, masse) :
        pass

    @abstractmethod
    def peutTransporter(self, masse) :
        pass



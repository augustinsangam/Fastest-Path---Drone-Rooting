from abc import ABC
from abc import abstractmethod

from Masse import Masse
from Entrepot import Entrepot

class Robot(ABC):
    """
    Classe Robot

    Classe qui modélise un robot comme un object abstrait
    """

    def __init__(self, poidsMax) :
        self.poidsMax = poidsMax

    @abstractmethod
    def k(self, masse) :
        pass

    @abstractmethod
    def peutTransporter(self, masse) :
        pass

    def tempsNecessaire(self, Recolte) :
        temps = 0
        masse = 0
        for i in range(len(Recolte) - 1) :
            temps += distanceEntre(Recolte[i], Recolte[i+1]) * self.k(masse)
            masse += Masse.masse(Recolte[i+1].nA, Recolte[i+1].nB, Recolte[i+1].nC)
        
        return temps

           
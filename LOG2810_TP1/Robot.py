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

    def tempsNecessaire(self, recolte) :
        temps = 0
        masse = 0
        for i in range(len(recolte) - 1) :
            temps += Entrepot().distanceEntre(recolte[i].noeud, recolte[i+1].noeud) * self.k(masse)
            masse += Masse.masse(recolte[i+1].nA, recolte[i+1].nB, recolte[i+1].nC)
        
        return temps

           
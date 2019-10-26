from abc import ABC
from abc import abstractmethod

from Masse import Masse
from Entrepot import Entrepot

class Robot(ABC):
    """
    Classe Robot

    Classe qui modélise un robot comme un object abstrait
    """

    tempsDeRamassageUnObjet = 10

    def __init__(self, poidsMax) :
        self.poidsMax = poidsMax

    @abstractmethod
    def nom(self) :
        pass

    @abstractmethod
    def k(self, masse) :
        pass

    @abstractmethod
    def peutTransporter(self, masse) :
        pass

    def tempsNecessaire(self, masse, noeudDepart, noeudArrivee, nObjets) :
        return Entrepot().distanceEntre(noeudDepart, noeudArrivee) * self.k(masse) + Robot.tempsDeRamassageUnObjet * nObjets

           
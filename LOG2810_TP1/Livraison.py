class Ceuillete(object):
    """
    Classe Livraison

    Classe qui représente une ceuillete d'un robot.
    Une ceuillette est défini comme étant le nombre d'objects 
    de chaque type receuilli à un certain noeud donné
    
    """

    def __init__(self, noeud, nA, nB, nC) :
        """
        Constructueur
        param  noeud  :    Le noeud auquel se fait la ceuillete
        param    nA   :    Le nombre d'objet de type A
        param    nB   :    Le nombre d'objet de type B
        param    nC   :    Le nombre d'objet de type C

        """
        self.noeud    = noeud
        self.nA       = nA
        self.nB       = nB
        self.nC       = nC



class Commande(object):
    """
    Classe Commande

    Classe qui représente une commande de l'utilisateur
    """

    def __init__(self, idNoeudDest, nA, nB, nC) :
        """
        Constructueur
        param   idNoeudDest :    Le numero du noeud de destination
        param   nA :             Le nombre d'objet de type A
        param   nB :             Le nombre d'objet de type B
        param   nC :             Le nombre d'objet de type C

        """
        self.idNoeudDest = idNoeudDest
        self.nA          = nA
        self.nB          = nB
        self.nC          = nC




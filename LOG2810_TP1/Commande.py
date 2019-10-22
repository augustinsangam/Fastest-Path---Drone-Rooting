class Commande(object):
    """
    Classe Commande

    Classe qui représente une commande de l'utilisateur
    Une commande est définie comme étant le nombre
    d'objets de chaque type
    """

    def __init__(self, nA, nB, nC) :
        """
        Constructueur
        param   nA :             Le nombre d'objet de type A
        param   nB :             Le nombre d'objet de type B
        param   nC :             Le nombre d'objet de type C

        """
        self.nA          = nA
        self.nB          = nB
        self.nC          = nC




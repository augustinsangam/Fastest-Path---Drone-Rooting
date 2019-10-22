class Noeud(object):
    """
    Classe Noeud

    Classe qui représente un noeud
    Un noeud est caractérisé par un identifiant entier et
    un stock d'objets de chaque type
    """

    def __init__(self, id, nA, nB, nC) :
        """
        Constructueur
        param   id :    Le numero du noeud
        param   nA :    Le nombre d'objet de type A
        param   nB :    Le nombre d'objet de type B
        param   nC :    Le nombre d'objet de type C

        """
        self.id = id
        self.nA = nA
        self.nB = nB
        self.nC = nC




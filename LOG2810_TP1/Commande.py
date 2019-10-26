class Commande(object):
    """
    Classe Commande

    Classe qui représente une commande de l'utilisateur
    Une commande est définie comme étant le nombre
    d'objets de chaque type
    """

    def __init__(self, nA=0, nB=0, nC=0) :
        """
        Constructueur
        param   nA :             Le nombre d'objet de type A
        param   nB :             Le nombre d'objet de type B
        param   nC :             Le nombre d'objet de type C

        """
        self.nA          = nA
        self.nB          = nB
        self.nC          = nC
        self.commandeEstVide= self.nA is 0 and self.nB is 0 and self.nC is 0


    def afficherCommande(self):
        if(self.commandeEstVide):
            return "Aucune commande n'a encore été passée"
        else:
            return ("""Vous avez commander:\n  {>2} colis de type A\n  {>2} colis de type B\n  {>2} colis de type C
            """.format(self.nA,self.nB,self.nC))




from Masse      import Masse
from Entrepot   import Entrepot

class Recolte() :
    """
    Classe Recolte

    Classe qui définit une recolte
    Une recolte n'est rien d'autre qu'une liste de Noeuds
    et de ceuilletes. On lui asscocie le nombre d'objets 
    ramassés et leur masse totale

    """

    def __init__(self, ceuilletes = []):
        self.nA         = 0
        self.nB         = 0
        self.nC         = 0
        self.distance   = 0
        self.ceuilletes = tuple()

        for i, ceuillete in enumerate(ceuilletes) :
            self.nA         += ceuillete.nA
            self.nB         += ceuillete.nB
            self.nC         += ceuillete.nC
            if i != 0 :
                self.distance   += Entrepot().distanceEntre(self.ceuilletes[-1].noeud, ceuillete.noeud) # Precédente - Actuelle
            self.ceuilletes += (ceuillete, )

        self.masse  = Masse.masse(self.nA, self.nB, self.nC)
        

    def __add__(self, ceuillete) :
        return Recolte(list(self.ceuilletes) + [ceuillete])

   

    def estValable(self, nA, nB, nC) :
        rammassageComplete = (self.nA == nA and self.nB == nB and self.nC == nC)
        noeud0 = Entrepot().noeuds[0]
        cheminValide = (self.ceuilletes[0].noeud == noeud0) and (self.ceuilletes[-1].noeud == noeud0)
        return rammassageComplete and cheminValide and (len(self.ceuilletes) > 1)

    #
    # def __repr__(self) :
    #     recolte = ''
    #     for ceuillete in self.ceuilletes:
    #         recolte += '{} | {} {} {} ---> '.format(ceuillete.noeud.id, ceuillete.nA, ceuillete.nB, ceuillete.nC)
    #     return recolte[:-5]

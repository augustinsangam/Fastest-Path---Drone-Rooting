from Masse import Masse

class Recolte(list) :
    """
    Classe Recolte

    Classe qui définit une recolte
    Une recolte n'est rien d'autre qu'une liste de Noeuds
    et de ceuilletes. On lui associe une masse également

    """
    def __init__(self):
        super().__init__()
        self.masse = 0

    def ajouter(self, ceuillete) :
        super().append(ceuillete)
        self.masse += Masse.masse(ceuillete.nA, ceuillete.nB, ceuillete.nC)





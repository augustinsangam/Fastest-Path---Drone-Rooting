from Masse import Masse

class Recolte(list) :
    """
    Classe Recolte

    Classe qui définit une recolte
    Une recolte n'est rien d'autre qu'une liste de Noeuds
    et de ceuilletes.

    """
    def __init__(self):
        super().__init__()

    def ajouter(self, ceuillete) :
        super().append(ceuillete)





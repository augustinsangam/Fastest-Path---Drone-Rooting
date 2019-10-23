"""
Classe Masse

Modélise les masses.

"""
class Masse(object):
    """
    Classe Masse
    
    Classe qui définit les objets et leur masse"""

    mA = 1   # Masse des objets de type A
    mB = 3   # Masse des objets de type B
    mC = 6   # Masse des objets de type C

    @staticmethod
    def masse(nA, nB, nC) : 
        """
        Fonction statique masse

        Calcule la masse d'une distribution d'objets

        param       nA :    Le nombre d'objets de type A
        param       nB :    Le nombre d'objets de type B
        param       nC :    Le nombre d'objets de type C
        return      La masse de la distribution 

        """
        return self.mA * nA + self.mB * nB + self.mC * nC




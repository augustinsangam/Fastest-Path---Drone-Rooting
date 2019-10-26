from Robot import Robot

class RobotX(Robot):
    """
    Classe Robot X

    Classe qui modélise un robot de type X
    """

    def __init__(self) :
        """Constructeur"""
        super().__init__(5)   # poidsMax = 5 ; Poids maximal en Kg

    def nom(self) :
        return "Robot X"


    def k(self, masse) :
        """ 
        Fonction qui calcule la caractéristique associée au robot X

        param       masse : est la masse que le robot transporte
        return      La caractéristique k associée

        """
        return 1 + masse


    def peutTransporter(self, masse) :
        """
        Fonction qui détermine si le robot X peut transporter une certaine charge

        param       masse : est la masse qu'on veut que le robot transporte
        return      True si c'est possibe, False sinon
        """
        return masse <= self.poidsMax





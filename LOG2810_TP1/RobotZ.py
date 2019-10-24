from Robot import Robot


class RobotZ(Robot):
    """
    Classe RobotZ

    Classe qui modélise un robot de type Z
    """

    def __init__(self) :
        """Constructeur"""
        super().__init__(25)   # poidsMax = 25 ; Poids maximal en Kg


    def k(self, masse) :
        """ 
        Fonction qui calcule la caractéristique associée au robot Z

        param       masse : est la masse que le robot transporte
        return      La caractéristique k associée

        """
        return 2.5 + 0.2 * masse


    def peutTransporter(self, masse) :
        """
        Fonction qui détermine si le robot Z peut transporter une certaine charge

        param       masse : est la masse qu'on veut que le robot transporte
        return      True si c'est possibe, False sinon
        """
        return masse <= self.poidsMax






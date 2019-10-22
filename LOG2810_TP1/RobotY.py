from Robot import Robot

class RobotY(Robot):
    """
    Classe RobotY

    Classe qui modélise un robot de type Y
    """

    poidsMax = 10 # Poids maximal en Kg


    def k(self, masse) :
        """ 
        Fonction qui calcule la caractéristique associée au robot Y

        param       masse : est la masse que le robot transporte
        return      La caractéristique k associée

        """
        return 1.5 + 0.6 * masse


    def peutTransporter(self, masse) :
        """
        Fonction qui détermine si le robot Y peut transporter une certaine charge

        param       masse : est la masse qu'on veut que le robot transporte
        return      True si c'est possibe, False sinon
        """
        return masse <= self.poidsMax






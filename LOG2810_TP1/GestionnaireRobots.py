from RobotX import RobotX
from RobotY import RobotY
from RobotZ import RobotZ

from Masse import Masse

class GestionnaireRobots(object):
    """
    Classe GestionnaireRobots

    Classe qui met en relation tous les robots
    """

    tousLesRobots = {RobotX(), RobotY(), RobotZ()} 
    
    @staticmethod
    def robotsPossibles(nA, nB, nC) :
        """
        Méthode statique robotsPossible(nA, nB, nC)

        qui permet de donner les robots possibles
        pour une repartitions d'objets de tous les types

        return  Un set contenant les robots possibles

        """
        masseDesObjets  = Masse.masse(nA, nB, nC)
        robotsPossibles = set()

        for robot in GestionnaireRobots.tousLesRobots : # On parcours tous les robots
            if robot.peutTransporter(masseDesObjets) :
                robotsPossibles.add(robot)

        return robotsPossibles




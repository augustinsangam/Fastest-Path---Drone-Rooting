from Entrepot import Entrepot
from Robot import Robot
from RobotX import RobotX
from RobotY import RobotY
from RobotZ import RobotZ
from Recolte import Recolte
from Ceuillete import Ceuillete
from GestionnaireRobots import GestionnaireRobots
from Commande import Commande
from Interface import Interface
import tkinter



def test():
    entrepot = Entrepot()
    recolte = Recolte()

    recolte.ajouter(Ceuillete(entrepot.noeuds[0], 0, 0, 0))
    recolte.ajouter(Ceuillete(entrepot.noeuds[1], 1, 0, 0))
    recolte.ajouter(Ceuillete(entrepot.noeuds[2], 2, 0, 0))

    print(RobotX().tempsNecessaire(recolte))
    print(RobotY().tempsNecessaire(recolte))
    print(RobotZ().tempsNecessaire(recolte))

    print('Les robots ')
    for robot in GestionnaireRobots.tousLesRobots:
        print(robot)

    print('Les robots possibles pour 1 kg ')
    for robot in GestionnaireRobots.robotsPossibles(1, 0, 0):
        print(robot)

    print('Les robots possibles pour 6 kg ')
    for robot in GestionnaireRobots.robotsPossibles(0, 0, 1):
        print(robot)

    print('Les robots possibles pour 11 kg ')
    for robot in GestionnaireRobots.robotsPossibles(2, 3, 0):
        print(robot)

    print('Les robots possibles pour 20 kg ')
    for robot in GestionnaireRobots.robotsPossibles(2, 0, 3):
        print(robot)

    print('Les robots possibles pour 30 kg ')
    for robot in GestionnaireRobots.robotsPossibles(0, 0, 5):
        print(robot)

if __name__ == "__main__" :
    commande= Commande()
    interface=Interface(commande)
    interface.mainloop()
    interface.destroy()



        
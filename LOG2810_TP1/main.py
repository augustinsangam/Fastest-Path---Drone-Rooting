from    Entrepot           import Entrepot
from    Robot              import Robot
from    RobotX             import RobotX
from    RobotY             import RobotY
from    RobotZ             import RobotZ
from    Recolte            import Recolte
from    Ceuillete          import Ceuillete
from    GestionnaireRobots import GestionnaireRobots
from    Chemin             import Chemin

if __name__ == "__main__" :
    entrepot    = Entrepot()
    entrepot.afficher()
    #recolte1    = Recolte([Ceuillete(entrepot.noeuds[0], 1, 0, 0), Ceuillete(entrepot.noeuds[1], 2, 0, 0)])
    ##print(recolte1.estvalable(3, 0, 0))
    #ceuillete2  = Ceuillete(entrepot.noeuds[0], 0, 0, 0)
    ##print(recolte(ceuillete2).estvalable(0, 0, 0))
    #recolte3    = recolte1 + ceuillete2
    ##print(recolte3.estvalable(3, 0, 0))
    #ceuillete4  = Ceuillete(entrepot.noeuds[1], 5, 0, 0)
    #recolte5    = sorted(recolte3)

    #print(RobotX().tempsNecessaire(recolte))
    #print(RobotY().tempsNecessaire(recolte))
    #print(RobotZ().tempsNecessaire(recolte))


    #print('Les robots ')
    #for robot in GestionnaireRobots.tousLesRobots :
    #    print(robot)
    
    #print('Les robots possibles pour 1 kg ')
    #for robot in GestionnaireRobots.robotsPossibles(1, 0, 0) :
    #    print(robot)
    
    #print('Les robots possibles pour 6 kg ')
    #for robot in GestionnaireRobots.robotsPossibles(0, 0, 1) :
    #    print(robot)
    
    #print('Les robots possibles pour 11 kg ')
    #for robot in GestionnaireRobots.robotsPossibles(2, 3, 0) :
    #    print(robot)
    
    #print('Les robots possibles pour 20 kg ')
    #for robot in GestionnaireRobots.robotsPossibles(2, 0, 3) :
    #    print(robot)
        
    
    #print('Les robots possibles pour 30 kg ')
    #for robot in GestionnaireRobots.robotsPossibles(0, 0, 5) :
    #    print(robot)

    print(Chemin().cheminLePlusRapide(1, 1, 0))
    

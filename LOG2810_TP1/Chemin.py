from    GestionnaireRobots  import GestionnaireRobots
from    Entrepot            import Entrepot
from    Ceuillete           import Ceuillete
from    Recolte             import Recolte
from    Masse               import Masse


class Chemin(object):
    """
    Classe ParcoursDrone

    Classe qui modélise tout ce qui a rapport avec le parcours du drone
    """


    @staticmethod
    def cheminLePlusRapide(nA, nB, nC) :
        """
        Algorithme pour trouver les chemins possible
        Algorithme de Djikstra lourdement modifié
        La logique est expliquée en psoeudo code dans le fichier Algoritme.txt
        """
        meilleurStatistiques    = None
        meilleurRobot           = None
        meilleurTemps           = float('inf')

        robotsPossibles         = GestionnaireRobots.robotsPossibles(nA, nB, nC)

        if len(robotsPossibles) == 0 :
            raise Exception('PasDeRobotsPossiblesError')

        for robot in robotsPossibles :
            statitistiquesRobot = Chemin.djikstraModifie(robot, nA, nB, nC)
            if statitistiquesRobot is not None : # Par securité , pas obligatoire
                if statitistiquesRobot[0] < meilleurTemps :
                    meilleurTemps           = statitistiquesRobot[0] 
                    meilleurStatistiques    = statitistiquesRobot
                    meilleurRobot           = robot

        return {'nom' : meilleurRobot.nom(), 'temps' : meilleurStatistiques[0], 'parcours' : meilleurStatistiques[1]}




    @staticmethod
    def djikstraModifie(robot, nA, nB, nC) :

        memoire = dict() # Censé être un map < Ceuillete , tuple < Recolte, temps, estTraitee > >
                         # La clé est une ceuillete. Cette ceuillete est spéciale.
                         # Le noeud représente le noeud courant
                         # Ses attributs nA, nB et nC représentent les cumuls des objets ramassé
                         # Sur toute la recolte

                         # On l'appelera dans tout la suite un etat

        # On commence au noeud 0
        # C'est équivalent à une ceuillete de 0 kg
        etatInitial          = Ceuillete(Entrepot().noeuds[0], 0, 0, 0)
        recolteDeDepart      = Recolte([Ceuillete(Entrepot().noeuds[0], 0, 0, 0)])

        memoire[Ceuillete.freeze(etatInitial)] = [recolteDeDepart, 0, False]

        while True :

            # On chosit l'etat étent associé au plus petit temps et n'ayant 
            # pas été traitée

            plusPetitTemps = float('inf')
            etat = None
            for unEtat, (recolte, temps, estTraitee) in memoire.items() :
                if (estTraitee == False) and (temps < plusPetitTemps) :
                    plusPetitTemps = temps
                    etat = Ceuillete.unfreeze(unEtat)

            # Si on en trouve pas, c'est qu'on ne peut pas completer la 
            # commande
            if plusPetitTemps == float('inf') :
                raise Exception('CommandeImpossibleError')

            ###Debug

            #print("\n\nEtat Actuel : {} {} {} {}".format(etat.noeud.id, etat.nA, etat.nB, etat.nC))

            ###Debug

            noeudCourant                = etat.noeud
            recolte, temps, estTraitee  = memoire[Ceuillete.freeze(etat)]

            # On doit trouver le nombre d'objets restants à ramasser
            nARestant, nBRestant, nCRestant = nA - recolte.nA, nB - recolte.nB, nC - recolte.nC


            for noeudVoisin, distance in Entrepot().graphe[noeudCourant] :
                # Cas spécial : on est déja passé par le noeud voisin.
                # On doit s'assurer de ne pas prendre plus de colis qu'il 
                # n'est possible
                    
                nAPossible, nBPossible, nCPossible = noeudVoisin.nA, noeudVoisin.nB, noeudVoisin.nC
                for uneCeuillete in recolte.ceuilletes :
                    if uneCeuillete.noeud == noeudVoisin :
                        nAPossible -= uneCeuillete.noeud.nA
                        nBPossible -= uneCeuillete.noeud.nB
                        nCPossible -= uneCeuillete.noeud.nC

                # On génère toutes les combinaisons de ceuilletes voisines
                for nACeuillis in range(min(nAPossible, nARestant) + 1) :
                    for nBCeuillis in range(min(nBPossible, nBRestant) + 1) :
                        for nCCeuillis in range(min(nCPossible, nCRestant) + 1) :

                            nouvelleCeuillete   = Ceuillete(noeudVoisin, nACeuillis, nBCeuillis, nCCeuillis)
                            nouveauTemps        = temps + robot.tempsNecessaire(recolte.masse, noeudCourant, noeudVoisin, etat.nA + etat.nB + etat.nC)
                            nouvelleRecolte     = recolte + nouvelleCeuillete

                            nouvelEtat          = Ceuillete(noeudVoisin, nACeuillis + etat.nA, nBCeuillis + etat.nB, nCCeuillis + etat.nC)

                            if Ceuillete.freeze(nouvelEtat) not in memoire :
                                memoire[Ceuillete.freeze(nouvelEtat)] = [nouvelleRecolte, nouveauTemps, False]
                                
                                ###Debug

                                #print("\nNouveaux etats : {} {} {} {}".format(nouvelEtat.noeud.id, nouvelEtat.nA, nouvelEtat.nB, nouvelEtat.nC))

                                ###Debug
                            else :
                                uneRecolte, unTemps, unStatut = memoire[Ceuillete.freeze(nouvelEtat)]
                                if nouveauTemps < unTemps :
                                    memoire[Ceuillete.freeze(nouvelEtat)] = [nouvelleRecolte, nouveauTemps, unStatut]
                                ###Debug

                                #print("\nEtats mémorisés : {} {} {} {}".format(nouvelEtat.noeud.id, nouvelEtat.nA, nouvelEtat.nB, nouvelEtat.nC))

                                ###Debug

                                
            memoire[Ceuillete.freeze(etat)][2] = True

            if etat.noeud == Entrepot().noeuds[0] and etat.nA == nA and etat.nB == nB and etat.nC == nC :
                #nouvelleRecolte.afficherRecolte()
                return (temps, recolte)

        return None

            



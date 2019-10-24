from Commande import Commande
from Entrepot import Entrepot

class Interface(object):
    """
    Classe Interface

    Classe utilisé pour l'affichage de l'interface. Celle-ci sera appelée avec en paramètre un objet Commande
    et un objet Entrepot. Ensuite elle est responsable de manipuler ces deux instances en fonction du choix de
    l'utilisateur
    """

    def __init__(self, commande) :
        """
        Constructueur
        param   commande :       La commande de l'utilisateur
        param   nB :             Le nombre d'objet de type B

        Attribut

        quitterPrograme: indique si l'utilisateur veut quitter le programme


        """
        self.commande=commande
        self.entrepot= None    #on ne génére pas l'entrepot tant que cela n'a pas été demandé explicitement
        self.programmeFinit= False
        self.afficherEntete()


    def demarrer(self):
        self.affichierChoix()
        self.executerChoix()
        print('\n ')
        return self.programmeFinit

    def afficherEntete(self):
        print("*" * 200)
        phraseBienvenu = '        Bienvenue     dans      notre      programme   '
        for c in phraseBienvenu: print(c, end='  ')
        print('\n')
        print("*" * 200)


    def affichierChoix(self):
        print('Veuillez choisir une des options suivantes:')
        print(' 1: Creer le graphe')
        print(' 2: Afficher le graphe')
        print(' 3: Prendre la commande')
        print(' 4: Afficher la commande')
        print(' 5: Trouver le plus cours chemin')
        print(' 6: Quitter')

    def executerChoix(self):
        options = {
            '1': self.creerGraphe,
            '2': self.afficherGraphe,
            '3': self.recupererCommande,
            '4': self.commande.afficherCommande,
            '5': 'A implementer',
            '6': self.quitterProgramme
        }
        choix= input()

        try:
            options.get(choix)()
        except TypeError:
            print("Cette option n'est pas disponible")

    def recupererCommande(self):
        nA,nB,nC= input("Indiquer le nombre de colis A,B et C que vous désirer commander (séparer par un espace) \n").split()
        self.commande.__dict__=Commande(nA,nB,nB).__dict__

    def creerGraphe(self):
        self.entrepot=Entrepot()
        print("Le graphe à bien été créer  ")

    def afficherGraphe(self):
        if self.entrepot==None:
            print("Il faut d'abord créer un graph avant de l'afficher")
        else:
            self.entrepot.afficher()

    def quitterProgramme(self):
        self.programmeFinit=True
        print("Fermeture du programme ")
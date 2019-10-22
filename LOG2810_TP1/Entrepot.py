from Noeud import Noeud    

class Entrepot(object):
    """
    Classe Entrepot

    Classe qui modélise un entrepôt
    """


    def __init__(self):
        self.noeuds         = []        # La liste des noeuds du grape
        self.graphe         = None      # Le graphe asscocié à l'entrepôt. Il s'agit d'un graphe valué
        self.nonDefini      = 'X'
        self.lireFichier("entrepot.txt")


    def lireFichier(self, nomFichier) :

        with open (nomFichier, 'r') as fichier :
            lignes = fichier.readlines()

        # On va trouver index rupture
        for i, ligne in enumerate(lignes) :
            if ligne.strip() == '' : 
                indexRupture = i
                break

        self.lireNoeuds(lignes[:indexRupture])
        self.lireGraphe(lignes[indexRupture + 1:])
       

    def lireNoeuds(self, lignes) :
        for ligne in lignes :
            ligne = ligne.strip()
            self.noeuds.append(Noeud(*(list(map(int, ligne.strip().split(','))))))

    def lireGraphe(self, lignes) :
        nbNoeuds = len(self.noeuds)
        self.graphe = [[self.nonDefini for _ in range(nbNoeuds)] for _ in range(nbNoeuds)]
        for ligne in lignes :
            idNoeud1, idNoeud2, distance = map(int, ligne.strip().split(','))
            self.graphe[idNoeud1][idNoeud2] = distance
            self.graphe[idNoeud2][idNoeud1] = distance


    def afficherCarte(self) :
        for noeud in self.noeuds :
            idNoeud = noeud.id
            print('(Noeud {:>2} , {} , {} , {} , ('.format(idNoeud, noeud.nA, noeud.nB, noeud.nC), end='')
            noeudsIncidents = ''
            for idNoeudIncident, distance in enumerate(self.graphe[idNoeud]) :
                if distance != self.nonDefini :
                    noeudsIncidents += '(Noeud {:>2}, {:>2}) , '.format(idNoeudIncident, distance) 
            print(noeudsIncidents[:-3], end='')
            print(')')

    



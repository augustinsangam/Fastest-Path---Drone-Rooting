from Noeud import Noeud    

class Entrepot(object):
    """

    Classe Entrepot

    Classe qui modélise un entrepôt
    Un entrepôt n'est rien d'autre qu'une liste de noeuds reliés dans un graphe

    """
    instance = None       # Attribut statique de classe

    def __new__(cls): 
        """
        Méthode de construction standard en Python
        Elle suit l'implémentation d'une classe Singleton comme défini ici :
        https://fr.wikipedia.org/wiki/Singleton_(patron_de_conception)#Python
        """

        if cls.instance is None:
            cls.instance        = object.__new__(cls)
            cls.instance.noeuds = []            # La liste des noeuds du grape
            cls.instance.grape  = None          # Le graphe asscocié à l'entrepôt. Il s'agit d'un graphe valué
                                                # Il est censé être une map<Noeud, set<NoueudIncident, Distance>>
            cls.instance.lireFichier("entrepot.txt")

        return cls.instance


    def lireFichier(self, nomFichier) :
        """
        Méthode lireFichier(nomFichier)
        Permet de lire le fichier et de remplir les deux attributs de la classe

        param nomFichier    : Le chemin vers le fichier contenant les données
        """
        # On ouvre le fichier et on lit tous les lignes du fichier
        with open (nomFichier, 'r') as fichier :
            lignes = fichier.readlines()

        # On va trouver l'index de rupture dans le fichier
        # Il s'agit de la ligne de séparation entre les noeuds et
        # les relations entre les noeuds
        for i, ligne in enumerate(lignes) :
            if ligne.strip() == '' :  # strip() pour enlever les espaces inutiles
                indexRupture = i
                break

        self.lireNoeuds(lignes[:indexRupture])          # On lit les noeuds
        self.lireGraphe(lignes[indexRupture + 1:])      # On lit les relations entre les noeuds
                                                        # (le graphe)

       

    def lireNoeuds(self, lignes) :
        """
        Méthode lireNoeuds(lignes)

        Permet de lire la première partie du fichier contenant les 
        détails sur les noeuds. Elle remplit automatiquement l'attribut noeuds

        param lignes : les lignes correspondantes à la première partie du fichier

        """
        for ligne in lignes :
            ligne = ligne.strip()
            # Noeud : (id, nA, nB, nC)
            self.noeuds.append(Noeud(*(list(map(int, ligne.strip().split(',')))))) 




    def lireGraphe(self, lignes) :
        """
        Méthode lireGraphe(lignes)

        Permet de lire la deuxième partie du fichier contenant les détails sur les
        relations entre les noeuds. Elle remplit automatiquement l'attribut graphe


        param lignes : les lignes correspondantes à la deuxième partie du fichier

        """
        # graphe :  map<Noeud, set<NoueudIncident, Distance>>
        self.graphe = {noeud : set() for noeud in self.noeuds}
        for ligne in lignes :
            idNoeud1, idNoeud2, distance = map(int, ligne.strip().split(','))
            self.graphe[self.noeuds[idNoeud1]].add((self.noeuds[idNoeud2], distance))
            self.graphe[self.noeuds[idNoeud2]].add((self.noeuds[idNoeud1], distance))




    def afficher(self) :
        """
        Méthode afficherEntreprot()

        Permet d'afficher l'entrepôt selon la méthode demandée par l'ennoncé du TP
        """
        for noeud in self.noeuds :
            print('(Noeud {:>2} , {} , {} , {} , ('.format(noeud.id, noeud.nA, noeud.nB, noeud.nC), end='')
            noeudsIncidents = ''
            for noeudIncident, distance in self.graphe[noeud] :
                noeudsIncidents += '(Noeud {:>2}, {:>2}) , '.format(noeudIncident.id, distance) 
            print(noeudsIncidents[:-3], end='')
            print(')')

    



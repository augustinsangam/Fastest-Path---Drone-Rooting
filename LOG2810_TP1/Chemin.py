from collections import deque

class Chemin(object):
    """
    Classe ParcoursDrone

    Classe qui modélise tout ce qui a rapport avec le parcours du drone
    """


    def __init__(self, entrepot) :
        self.entrepot       = entrepot



    def parcoursOrdonne(self, idNoeudSource):

        solution            = deque()
        previous, idFin     = self.dijkstra(idNoeudSource)

        while previous[idFin] != None:
            solution.appendleft(idFin)
            idFin = previous[idFin]
        
        solution.appendleft(idFin)

        return solution


    def trouverVoisins(self, nbNoeuds):
        voisins     =   {id : set() for id in range(nbNoeuds)}
        
        for idNoeud, noeudsIncidents in enumerate(self.entrepot.graphe) :
            for idNoeudIncident, distance in enumerate(noeudsIncidents) :
                if self.entrepot.graphe[idNoeud][idNoeudIncident] != self.entrepot.nonDefini :
                    voisins[idNoeud].add((idNoeudIncident, distance))

        return voisins


    def dijkstra(self, idNoeudSource) :
        """
        Algorithme pour trouver le chemin le plus cours entre le noeud source et destination

        param       idNoeudSource   :   Le numero du noeud de depart
        param       idNoeudDest     :   Le numero du noeud de destination

        return      :   une liste contenant la liste des numeros de noeuds à traverser 
                        pour arriver à la destination

        L'implémentation est inspirée de celle faite sur le site Rosettacode
        https://rosettacode.org/wiki/Dijkstra%27s_algorithm#Python
        """
        nbNoeuds                    = len(self.entrepot.noeuds)
        infini                      = float('inf')
        distances                   = {id : infini   for id in range(nbNoeuds)}
        distances[idNoeudSource]    = 0
        previous                    = {id : None     for id in range(nbNoeuds)}
        noeudsNonVisites            = {id : distances[id] for id in range(nbNoeuds)}
        voisins                     = self.trouverVoisins(nbNoeuds)

        visites                     = []
        
 

        while noeudsNonVisites :

            idNoeudVoisinLePlusPorche = min(noeudsNonVisites.items(), key = lambda x : x[1])[0]
            visites.append(idNoeudVoisinLePlusPorche)
            del noeudsNonVisites[idNoeudVoisinLePlusPorche]

            if distances[idNoeudVoisinLePlusPorche] == infini:
                break

            for v, distance in voisins[idNoeudVoisinLePlusPorche]:
                minimum = distances[idNoeudVoisinLePlusPorche] + distance
                if minimum < distances[v]:            
                    distances[v]        = minimum
                    noeudsNonVisites[v] = minimum
                    previous[v]         = idNoeudVoisinLePlusPorche
        
        print(visites)
        return previous, idNoeudVoisinLePlusPorche



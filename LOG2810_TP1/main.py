from Entrepot import Entrepot

if __name__ == "__main__" :
    entrepot1 = Entrepot()
    entrepot2 = Entrepot()
    assert(entrepot1 == entrepot2)
    #entrepot1.afficher()
    print('+'*100)
    for noeud1 in entrepot1.graphe.keys() :
        for noeud2 in entrepot1.graphe.keys() :
            print("Distance entre {} et {} = {}".format(noeud1.id, noeud2.id, entrepot1.distanceEntre(noeud1, noeud2)))




from Chemin import Chemin
from Commande import Commande
from Entrepot import Entrepot
from tkinter import *
from tkinter import messagebox
from PasDeRobotsPossibleError import PasDeRobotsPossiblesError
from    CommandeImpossibleError            import CommandeImpossibleError

class Interface(Frame):
    """
    Classe Interface

    Classe utilisé pour l'affichage de l'interface. On utilise la bibliotèque tkinter
    qui est destiné à créer des interfaces graphiques.
    """

    def __init__(self,commande):

        """
                Constructueur
                param   commande :       La commande de l'utilisateur.
                """

        self.commande=commande
        self.entrepot= None    #on ne génére pas l'entrepot tant que cela n'a pas été demandé explicitement
        self.fenetrePrincipale=Tk()
        self.canvas=None       #le widget principale.
        self.initialiserGUI()  #Place les bouttons sur la page d'acceuil


        """ 
        Fonction qui initialise l'affichage de l'acceuil (au niveau des titres et des dimensions)

        return          aucun
        
        paramètres      liste de widget fournis par la librairie
        """

    def initialiserGUI(self, **kwargs):

        Frame.__init__(self, self.fenetrePrincipale, **kwargs)
        self.pack(fill=BOTH)
        self.master.title('Livraison')
        self.canvas = Canvas(self.fenetrePrincipale, width=1200, height=576, background='white')
        self.canvas.create_text(610, 30, text="Bienvenue dans notre système de livraison", font="Arial 20 bold",
                           fill="black")
        self.canvas.create_text(210, 100, text="Veuillez choisir une des options suivantes:", font="Arial 14 bold",
                           fill="black")
        self.canvas.create_text(580, 565, text="@Verbaere Nicolas, Sangam Augustin, Abdelrahman Bassiouni", font="Arial 10 bold",
                                fill="black")

        self.insererBouttons()

    """ 
            Fonction qui insere tous les bouttons de l'interface, et les relient à leurs méthodes

            return          aucun

            paramètres      aucun
            """
    def insererBouttons(self):

        listeBouttons = []
        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Créer le graphe", command=self.creerGraphe, anchor=W, cursor="hand2"))

        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Afficher le graphe", command=self.afficherGraphe, anchor=W,
                   cursor="hand2"))
        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Prendre la commande", command=self.recupererCommande, anchor=W,
                   cursor="hand2"))

        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Afficher la commande", command=self.afficherCommande, anchor=W,
                   cursor="hand2"))

        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Trouver le plus cours chemin", command=self.cheminLePlusCours,
                   anchor=W,
                   cursor="hand2"))

        listeBouttons.append(
            Button(self.fenetrePrincipale, text="Quitter", command=self.fenetrePrincipale.quit, anchor=W))

        [boutton.configure(width=40, height=2, activebackground="#33B5E5", cursor="hand2", foreground="red") for boutton
         in listeBouttons]

        height = 130
        for element in listeBouttons:
            self.canvas.create_window(20, height, anchor=NW, window=element)
            height += 50
        self.canvas.pack()


    """ 
            Fonction qui affiche la commande de l'utilisateur

            return          aucun

            paramètres      aucun
    """


    def afficherCommande(self):
        if self.commande.commandeEstVide:
            messagebox.showerror("Erreur", "Aucune commande n'a encore été passée")
        else :
            texte = Text(self.fenetrePrincipale, width=400, borderwidth=0, font="Arial 13 ", foreground="blue")
            message="""Vous avez commander:\n  -{:>2} colis de type A\n  -{:>2} colis de type B\n  -{:>2} colis de type C
            """.format(self.commande.nA,self.commande.nB,self.commande.nC)
            texte.insert(END, message)
            texte.config(state=DISABLED)
            self.canvas.create_window(350, 150, anchor=NW, window=texte, tag="affichageCommande")
            self.activerWidjet("affichageCommande")

    """ 
            Fonction qui initialise la classe Entrepot, donc on va construire l'entrepot à partir du fichier texte

            return          aucun

            paramètres      aucun
    """


    def creerGraphe(self):
        self.entrepot=Entrepot()
        texte= Text(self.fenetrePrincipale, width=400, borderwidth=0, font="Arial 13 ", foreground="blue")
        texte.insert(END,"Le graphe à bien été créer ")
        texte.config(state=DISABLED)
        self.canvas.create_window(350, 150, anchor=NW, window=texte, tag="creationGraphe")
        self.activerWidjet("creationGraphe")


    """ 
            Fonction qui affiche fait appel a la fonction d'affichage du reseau de la classe Entrepot

            return          aucun

            paramètres      aucun
    """


    def afficherGraphe(self):

        texte = Text(self.fenetrePrincipale,width=400, borderwidth=0,font="Arial 13 ", foreground="blue")
        try:
            for ligne in self.entrepot.afficher():
                texte.insert(END, ligne+ '\n')
        except AttributeError:
            messagebox.showerror("Erreur", "Il faut d'abord créer un graphe avant de l'afficher")
        texte.config(state=DISABLED)
        self.canvas.create_window(350, 150, anchor=NW, window=texte, tag="graphe")
        self.activerWidjet("graphe")


    """ 
            Fonction pour afficher les textes approprié en fonction de la situation

            return          aucun

            paramètres      le tag du texte à appelé
    """


    def activerWidjet(self, tag):
        self.canvas.itemconfigure("graphe", state='hidden')
        self.canvas.itemconfigure("creationGraphe", state='hidden')
        self.canvas.itemconfigure("affichageCommande", state='hidden')
        self.canvas.itemconfigure("affichageChemin", state='hidden')

        self.canvas.itemconfigure(tag, state='normal')


    """ 
            Fonction déclanchée pour recupérer la commande de l'utilisateur.
            Elle gère la fenetre des inputs.

            return          aucun

            paramètres      aucun
    """


    def recupererCommande(self):

        master = Tk()
        master.geometry("350x100+300+300")
        master.title('Commande')
        self.initialiserEntree(master)

        master.mainloop()
        master.destroy()


    """ 
             Fonction qui initialise les entrées lorsqu'on propose d'entrer la commande.

             return          aucun

             paramètres      master (la fenetre des inputs)
     """


    def initialiserEntree(self, master):
        Label(master,
              text="objet de type A  ").grid(row=0)
        Label(master,
              text="objet de type B  ").grid(row=1)
        Label(master,
              text="objet de type C  ").grid(row=2)

        nA = Entry(master)
        nB = Entry(master)
        nC = Entry(master)
        nA.insert(10, 0)
        nB.insert(10, 0)
        nC.insert(10, 0)

        nA.grid(row=0, column=1)
        nB.grid(row=1, column=1)
        nC.grid(row=2, column=1)

        """ 
                 Fonction qui construit la commande à partir des informations entrées par l'utilisateur

                 return          aucun

                 paramètres      aucun
         """
        def creerCommande():

            noeudsA, noeudsB, noeudsC = int(nA.get()), int(nB.get()), int(nC.get())
            if (noeudsA < 0 or noeudsB < 0 or noeudsC < 0):
                messagebox.showerror("Erreur", "Il faut fournir des nombres positifs")
            else:
                self.commande.__dict__ = Commande(noeudsA, noeudsB, noeudsC).__dict__
            master.quit()

        Button(master, text='Quitter', command=master.quit).grid(row=3,
                                                                 column=0, sticky=W, pady=4)

        Button(master, text='OK', command=creerCommande).grid(row=3,
                                                              column=1, sticky=W, pady=4)





    """ 
             Fonction qui fait l'affichage du plus cours chemin. Elle appelle les
             algorithmes de la classe Chemin, qui s'occupe de faire les calculs

             return          aucun

             paramètres      aucun
     """

    def cheminLePlusCours(self):
        chemin = Chemin()
        if self.commande.commandeEstVide:
            messagebox.showerror("Erreur",
                                 "Vous devez d'abord faire une commande avant de trouver le meilleur chemin")
        else:

            try :
                resultat= chemin.cheminLePlusRapide(self.commande.nA,self.commande.nB,self.commande.nC)
            except CommandeImpossibleError:
                messagebox.showerror("Erreur",
                                     "Notre entrepot n'a pas en stock tout les objets que vous désirer. Veuillez sélectioner moin de colis")
            except PasDeRobotsPossiblesError:
                messagebox.showerror("Erreur",
                                     "Nos robots n'ont pas la capacité nécessaire pour satisfaires à la masse de votre commande. Veuillez sélectioner moin de colis")

            texte = Text(self.fenetrePrincipale, width=400, borderwidth=0, font="Arial 13 bold ", foreground="black")


            texte.insert(END, "Robot utilisé :     "+str(resultat["nom"])+ '\n')
            texte.insert(END, "Meilleur temps :  "+ str(resultat["temps"])+ " secondes" '\n\n')
            texte.insert(END, "Parcours (du haut vers le bas): \n")


            for ceuillette in resultat["parcours"].ceuilletes:
                detailCeuillette=ceuillette.afficherLeNombreDObjetCeuillis()
                if detailCeuillette != "":
                    detailCeuillette=' ('+detailCeuillette+') '

                texte.insert(END, "Noeud "+ str(ceuillette.noeud.id)+ detailCeuillette + '\n')

            texte.config(state=DISABLED)
            self.canvas.create_window(350, 150, anchor=NW, window=texte, tag="affichageChemin")
            self.activerWidjet("affichageChemin")



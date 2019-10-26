from tkinter import *
from Commande import Commande
from Entrepot import Entrepot
from tkinter import *
from tkinter import messagebox

class Interface(Frame):
    """
    Classe Interface

    Classe utilisé pour l'affichage de l'interface. Celle-ci sera appelée avec en paramètre un objet Commande
    et un objet Entrepot. Ensuite elle est responsable de manipuler ces deux instances en fonction du choix de
    l'utilisateur
    """

    def __init__(self,commande):

        """
                Constructueur
                param   commande :       La commande de l'utilisateur
                """

        self.commande=commande
        self.entrepot= None    #on ne génére pas l'entrepot tant que cela n'a pas été demandé explicitement
        self.fenetrePrincipale=Tk()
        self.canvas=None
        self.initialiserGUI()


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

        listeBouttons=[]
        listeBouttons.append(Button(self.fenetrePrincipale, text="Créer le graphe", command=self.creerGraphe, anchor=W, cursor="hand2"))

        listeBouttons.append(Button(self.fenetrePrincipale, text="Afficher le graphe", command=self.afficherGraphe, anchor=W,
                                       cursor="hand2"))
        listeBouttons.append(Button(self.fenetrePrincipale, text="Prendre la commande", command=self.recupererCommande, anchor=W,
                                        cursor="hand2"))

        listeBouttons.append(Button(self.fenetrePrincipale, text="Afficher la commande", command=self.afficherCommande, anchor=W,
                                        cursor="hand2"))

        listeBouttons.append(Button(self.fenetrePrincipale, text="Trouver le plus cours chemin", command=self.fenetrePrincipale.quit, anchor=W,
                                        cursor="hand2"))

        listeBouttons.append(Button(self.fenetrePrincipale, text="Quitter", command=self.fenetrePrincipale.quit, anchor=W))

        [boutton.configure(width=40, height=2, activebackground="#33B5E5", cursor="hand2",foreground="red") for boutton in listeBouttons]

        height=130
        for element in listeBouttons:
            self.canvas.create_window(20, height, anchor=NW, window=element)
            height+=50
        self.canvas.pack()



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

    def creerGraphe(self):
        self.entrepot=Entrepot()
        texte= Text(self.fenetrePrincipale, width=400, borderwidth=0, font="Arial 13 ", foreground="blue")
        texte.insert(END,"Le graphe à bien été créer ")
        texte.config(state=DISABLED)
        self.canvas.create_window(350, 150, anchor=NW, window=texte, tag="creationGraphe")
        self.activerWidjet("creationGraphe")


    def afficherGraphe(self):
        if self.entrepot==None:
            messagebox.showerror("Erreur", "Il faut d'abord créer un graphe avant de l'afficher")
        else:
            texte = Text(self.fenetrePrincipale,width=400, borderwidth=0,font="Arial 13 ", foreground="blue")
            for ligne in self.entrepot.afficher():
                texte.insert(END, ligne+ '\n')
            texte.config(state=DISABLED)
            self.canvas.create_window(350, 150, anchor=NW, window=texte, tag="graphe")
            self.activerWidjet("graphe")



    def activerWidjet(self, tag):
        self.canvas.itemconfigure("graphe", state='hidden')
        self.canvas.itemconfigure("creationGraphe", state='hidden')
        self.canvas.itemconfigure("affichageCommande", state='hidden')
        self.canvas.itemconfigure(tag, state='normal')

    def recupererCommande(self):

        master = Tk()
        master.geometry("350x100+300+300")
        master.title('Commande')

        def creerCommande():
            noeudsA, noeudsB, noeudsC = int(nA.get()), int(nB.get()), int(nC.get())
            if (noeudsA < 0 or noeudsB < 0 or noeudsC < 0):
                messagebox.showerror("Erreur", "Il faut fournir des nombres positifs")
            else:
                self.commande.__dict__ = Commande(noeudsA, noeudsB, noeudsC).__dict__
            master.quit()

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

        Button(master,text='Quitter', command=master.quit).grid(row=3,
                                                                 column=0, sticky=W, pady=4)

        Button(master, text='OK', command=creerCommande).grid(row=3,
                                                              column=1, sticky=W, pady=4)

        master.mainloop()
        master.destroy()



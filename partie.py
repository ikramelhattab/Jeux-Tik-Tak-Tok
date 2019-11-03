

"""Ce fichier permet de modéliser une partie du jeu entre deux joueurs """
from plateau import Plateau
from joueur import Joueur

class Partie:
    """
    Classe modélisant une partie du jeu Tic-Tac-Toe utilisant
    un plateau et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        plateau (Plateau): Le plateau du jeu contenant les 9 cases.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None)
        nb_parties_nulles (int): Le nombre de parties nulles (aucun joueur n'a gagné).
    """

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Tic-Tac-Toe.
        """
        self.plateau = Plateau()    # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []       # La liste des deux joueurs (initialement une liste vide).
                                # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
                                    # Pendant le jeu et à chaque tour d'un joueur,
                                    # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def jouer(self):
        """
        Permet de démarrer la partie en commençant par l'affichage de ce texte:

        Bienvenue au jeu Tic Tac Toe.
        ---------------Menu---------------
        1- Jouer avec l'ordinateur.
        2- Jouter avec une autre personne.
        0- Quitter.
        -----------------------------------
        Entrez s.v.p. un nombre entre 0 et 2:?

        Cette méthode doit donc utiliser la méthode saisir_nombre().
        Elle doit par la suite demander à l'utilisateur les noms des joueurs.
        Veuillez utiliser 'Colosse' comme nom pour l'ordinateur.
        Il faut créer des instances de la classe Joueur et les ajouter à la liste joueurs.
        Il faut utiliser entre autres ces méthodes:
            *- demander_forme_pion(): pour demander au premier joueur la forme de son pion (X ou O).
              (Pas besoin de demander à l'autre joueur ou à l'ordinateur cela, car on peut le déduire).
            *- plateau.non_plein(): afin d'arrêter le jeu si le plateau est plein (partie nulle).
            *- tour(): afin d'exécuter le tour du joueur courant.
            *- plateau.est_gagnant(): afin de savoir si un joueur a gagné et donc arrêter le jeu.
        Il faut alterner entre le premier joueur et le deuxième joueur à chaque appel de tour()
        en utilisant l'attribut joueur_courant.
        Après la fin de chaque partie, il faut afficher les statistiques sur le jeu.
        Voici un exemple:

        Partie terminée! Le joueur gagnant est: Colosse
        Parties gagnées par Mondher : 2
        Parties gagnées par Colosse : 1
        Parties nulles: 1
        Voulez-vous recommencer (O,N)?

        Il ne faut pas oublier d'initialiser le plateau avant de recommencer le jeu.
        Si l'utilisateur ne veut plus recommencer, il faut afficher ce message:
        ***Merci et au revoir !***
        """

        print("Bienvenue au jeu Tic Tac Toe.")
        print("------------------Menu------------------.")
        print(" 1- Jouer avec l'ordinateur.")
        print(" 2- Jouter avec une autre personne.")
        print(" 0- Quitter.") 
        print("--------------------------------------------.")
        choix=saisir_nombre(self,0,2)
        if(choix==0):
             print("***Merci et au revoir !***")
        elif(choix==1):
                           demande=input("Entrez s.v.p. votre nom:?")
                           car=demander_forme_pion(self)
                           joueur1=Joueur(str(demande),"Personne",str(car.upper()))
                           if(car.upper()=="X"):
                              print(self.plateau)
                              joueur2=Joueur('colosse',"Ordinateur","O")
                           else:
                              joueur2=Joueur('colosse',"Ordinateur","X")
        else:
                           demande1=input("Entrer s.v.p. votre nom")
                           car=demander_forme_pion(self)
                           joueur1=Joueur(str(demande1),"Personne",str(car.upper()))
                           demande2=input("Entrez s.v.p. le nom de l'autre joueur:?")
                           print(self.plateau)
                           if(car.upper()=="X"):
                              joueur2=Joueur(str(demande2),"Personne","O")
                           else:
                              joueur2=Joueur(str(demande2),"Personne","X")
        
                           

        if(choix!=0):                                       
         self.joueurs.append(joueur1)
         self.joueurs.append(joueur2)
         self.joueur_courant=self.joueurs[0]
         tour(self,choix)
          

          
   

def saisir_nombre(self, nb_min, nb_max):
        """
        Permet de demander à l'utilisateur un nombre et doit le valider.
        Ce nombre doit être une valeur entre nb_min et nb_max.
        Vous devez utiliser la méthode isnumeric() afin de vous assurer que l'utilisateur entre
        une valeur numérique et non pas une chaîne de caractères.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Args:
            nb_min (int): Un entier représentant le minimum du nombre à entrer.
            nb_max (int): Un entier représentant le maximum du nombre à entrer.

        Returns:
            int: Le nombre saisi par l'utilisateur après validation.
        """
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."

        nombres=input(" Entrez s.v.p. un nombre entre 0 et 2:?")

        while  ( nombres.isnumeric()==False or int(nombres)<nb_min or int(nombres)>=nb_max+1) :
         print(" ***Valeur incorrecte!***")
         nombres=input(" Entrez s.v.p. un nombre entre 0 et 2:?")

        return int(nombres)
       


def demander_forme_pion(self):
        """
        Permet de demander à l'utilisateur un caractère et doit le valider.
        Ce caractère doit être soit 'O' soit 'X'.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Returns:
            string: Le catactère saisi par l'utilisateur après validation.
        """
        carctere=""
        while not(carctere.upper()=="O" or  carctere.upper()=="X"):
         carctere=input(" Sélectionnez s.v.p.  la forme de votre pion(x,o):?")
        return carctere
       

def tour(self, choix):
       

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."
        test=True
        while(test and not(self.plateau.est_gagnant(self.joueur_courant.pion))):
          if(choix==1):
                   if self.joueur_courant==self.joueurs[1] :
                    ligne,colonne=self.plateau.choisir_prochaine_case(self.joueurs[1].pion)                                                                        
                    self.plateau.selectionner_case(ligne, colonne,self.joueurs[1].pion)
                    print("ce le tour maintenant de l'ordinateur colosse!")
                    print(self.plateau)
                    #tester si le joueur_courant est gagnant
                    if(self.plateau.est_gagnant(self.joueur_courant.pion)):
                          self.joueur_courant.nb_parties_gagnees=self.joueur_courant.nb_parties_gagnees+1
                          print("-----------------------------------------------------------------")
                          print("partie terminer! Le joueur gagnant est:",self.joueur_courant.nom)
                          print("parties gagnées par",self.joueurs[0].nom,":",self.joueurs[0].nb_parties_gagnees)
                          print("parties gagnées par",self.joueurs[1].nom,":",self.joueurs[1].nb_parties_gagnees)
                          print("parties nulles:",self.nb_parties_nulles)
                        
                          recommencer=""
                          while not(recommencer.upper()=="O" or recommencer.upper()=="N"):
                             recommencer=input("Voulez-vous recommencer(O,N)?")
                          if(recommencer.upper()=="O"):
                                self.plateau.initialiser()
                                self.joueur_courant=self.joueurs[0]
                                tour(self, choix)
                                
                          else:
                               test=False
                               print("***Merci et au revoir !***")
                    elif self.plateau.non_plein()==False:#si le plateau est pleine en quitte le boucle et on incremente le nb_partie_null
                               test=False
                    else:
                         
                         self.joueur_courant=self.joueurs[0]  #donner le tour  a l'utilisateur 
                   else:
                        ligne,colonne=demander_postion(self) #exectuer par la personne
                        self.plateau.selectionner_case(ligne, colonne, self.joueur_courant.pion)
                        print(self.plateau)
                        if(self.plateau.est_gagnant(self.joueur_courant.pion)):
                          self.joueur_courant.nb_parties_gagnees=self.joueur_courant.nb_parties_gagnees+1
                          print("-----------------------------------------------------------------")
                          print("partie terminer! Le joueur gagnant est:",self.joueur_courant.nom)
                          print("parties gagnées par",self.joueurs[0].nom,":",self.joueurs[0].nb_parties_gagnees)
                          print("parties gagnées par",self.joueurs[1].nom,":",self.joueurs[1].nb_parties_gagnees)
                          print("parties nulles:",self.nb_parties_nulles)
                          recommencer=""
                          while not(recommencer.upper()=="O" or recommencer.upper()=="N"):
                             recommencer=input("Voulez-vous recommencer(O,N)?")
                          if(recommencer.upper()=="O"):
                                self.plateau.initialiser()
                                tour(self, choix)
                                
                          else:
                               test=False
                               print("***Merci et au revoir !***")
                        elif self.plateau.non_plein()==False :
                            test=False
                        else:
                            self.joueur_courant=self.joueurs[1] #donner le tour  a l'ordinateur
          elif choix==2:
                     if self.joueur_courant==self.joueurs[0]:
                        ligne,colonne=demander_postion(self)
                        self.plateau.selectionner_case(ligne, colonne, self.joueur_courant.pion)  
                        print(self.plateau)
                        if(self.plateau.est_gagnant(self.joueur_courant.pion)):
                          self.joueur_courant.nb_parties_gagnees=self.joueur_courant.nb_parties_gagnees+1
                          print("-----------------------------------------------------------------")
                          print("partie terminer! Le joueur gagnant est:",self.joueur_courant.nom)
                          print("parties gagnées par",self.joueurs[0].nom,":",self.joueurs[0].nb_parties_gagnees)
                          print("parties gagnées par",self.joueurs[1].nom,":",self.joueurs[1].nb_parties_gagnees)
                          print("parties nulles:",self.nb_parties_nulles)
                          recommencer=""
                          while not(recommencer.upper()=="O" or recommencer.upper()=="N"):
                           recommencer=input("Voulez-vous recommencer(O,N)?")
                          if(recommencer.upper()=="O"):
                             self.plateau.initialiser()
                             tour(self, choix)
                                
                          else:
                               test=False
                               print("***Merci et au revoir !***")
                        elif self.plateau.non_plein()==False:
                    
                              test=False
                        else:
                             self.joueur_courant=self.joueurs[1]
                              
                              
                     else:
                           ligne,colonne=demander_postion(self)
                           self.plateau.selectionner_case(ligne, colonne, self.joueur_courant.pion) 
                           print(self.plateau)
                           if(self.plateau.est_gagnant(self.joueur_courant.pion)):
                             self.joueur_courant.nb_parties_gagnees=self.joueur_courant.nb_parties_gagnees+1
                             print("-----------------------------------------------------------------")
                             print("partie terminer! Le joueur gagnant est:",self.joueur_courant.nom)
                             print("parties gagnées par",self.joueurs[0].nom,":",self.joueurs[0].nb_parties_gagnees)
                             print("parties gagnées par",self.joueurs[1].nom,":",self.joueurs[1].nb_parties_gagnees)
                             print("parties nulles:",self.nb_parties_nulles)
                             recommencer=""
                             while not(recommencer.upper()=="O" or recommencer.upper()=="N"):
                              recommencer=input("Voulez-vous recommencer(O,N)?")
                             if(recommencer.upper()=="O"):
                               self.plateau.initialiser()
                               tour(self, choix)
                                
                             else:
                                 test=False
                                 print("***Merci et au revoir !***")
                           elif self.plateau.non_plein()==False:
                                test=False
                           else:
                                self.joueur_courant=self.joueurs[0]  
        if(self.plateau.non_plein()==False or not(self.plateau.est_gagnant(self.joueur_courant.pion))):
             self.nb_parties_nulles = self.nb_parties_nulles+1
             print("-----------------------------------------------------------------")
             print("partie terminer! Aucun joueur n 'a gagné!")
             print("parties gagnées par",self.joueurs[0].nom,":",self.joueurs[0].nb_parties_gagnees)
             print("parties gagnées par",self.joueurs[1].nom,":",self.joueurs[1].nb_parties_gagnees)
             print("parties nulles:",self.nb_parties_nulles)
             recommencer=""
             while not(recommencer.upper()=="O" or recommencer.upper()=="N"):
              recommencer=input("Voulez-vous recommencer(O,N)?")
             if( recommencer.upper()=="O"):
               self.plateau.initialiser()
               tour(self,choix)
                       
             else:
                 test=False
                 print("***Merci et au revoir !***")
                          
def demander_postion(self):
        """
        Permet de demander à l'utilisateur les coordonnées de la case qu'il veut jouer.
        Cette méthode doit valider ces coordonnées (ligne,colonne).
        Voici un exemple de ce qu'il faut afficher afin de demander cette position:

        Mondher : Entrez s.v.p. les coordonnées de la case à utiliser:
        Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? 0
        Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? 0

        Il faut utiliser la méthode saisir_nombre() et position_valide().

        Returns:
            (int,int):  Une paire d'entiers représentant les
                        coordonnées (ligne, colonne) de la case choisie.
        """
        print(self. joueur_courant.nom,": Entrez s.v.p. les coordonnees de la case à utiliser:")
        while(True):
            print(" Numéro de la ligne:",end=' ')
            ligne=saisir_nombre(self,0,2)
            print(" Numéro de la colonne:",end=' ')
            colonne=saisir_nombre(self,0,2)
        
            if(self.plateau.position_valide(ligne,colonne)):
                return ligne,colonne
            
        


if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()
    partie.jouer()


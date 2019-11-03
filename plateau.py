
"""
Ce fichier permet de modeliser le plateau de jeu qui contient 9 cases
"""

from case import Case
from random import randrange

class Plateau:
 def __init__(self):
        """
        Méthode spéciale initialisant un nouveau plateau contenant les 9 cases du jeu.
        """

        # Dictionnaire de cases.
        # La clé est une position (ligne, colonne), et la valeur est une instance de la classe Case.
        self.cases = {}

        # Appel d'une méthode qui initialise un plateau contenant des cases vides.
        self.initialiser()
 def initialiser(self):
        """
        Méthode fournie permettant d'initialiser le plateau avec des cases vides (contenant des espaces).
        """

        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.cases.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Case.
        # dont l'attribut "contenu" serait un espace (" ").
        for i in range(0, 3):
            for j in range(0, 3):
                self.cases[i,j] = Case(" ")
 def __str__(self):
        """Méthode spéciale fournie indiquant à Python comment représenter une instance de Plateau
        sous la forme d'une chaîne de caractères. Permet donc d'afficher le plateau du jeu
        à l'écran en faisant par exemple:
        p1 = Plateau()
        print(p1)
        Donc, lorsque vous affichez un objet, Python invoque automatiquement la méthode __str__
        Voici un exemple d'affichage:
         +-0-+-1-+-2-+
        0|   | X | X |
         +---+---+---+
        1| O | O | X |
         +---+---+---+
        2|   |   | O |
         +---+---+---+

        Returns:
            string: Retourne la chaîne de caractères à afficher.
        """
        s = " +-0-+-1-+-2-+\n"
        for i in range(0, 3):
            s += str(i)+ "| "
            for j in range(0, 3):
                s += self.cases[(i,j)].contenu + " | "
            if i<=1:
                s += "\n +---+---+---+\n"
            else:
                s += "\n +---+---+---+"
        return s
      

 def non_plein(self):
        """
        Retourne si le plateau n'est pas encore plein.
        Il y a donc encore des cases vides (contenant des espaces et non des "X" ou des "O").

        Returns:
            bool: True si le plateau n'est pas plein, False autrement.
        """
        
        

        for i in range(0,3):
         for j in range(0,3):
            if self.cases[(i,j)].est_vide():
                return True
  
        return False                 
            
 def position_valide(self, ligne, colonne):
     

        if(self.cases[(ligne,colonne)].est_vide()):
           return True
        else:
            return False
 def selectionner_case(self, ligne, colonne, pion):
       
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        if(self.position_valide(ligne,colonne)):
           self.cases[(ligne,colonne)].contenu=pion
        else:
            print("***case plein!***")

 def est_gagnant(self, pion):
        """
        Permet de vérifier si un joueur a gagné le jeu.
        Il faut vérifier toutes les lignes, colonnes et diagonales du plateau.

        Args:
            pion (string): La forme du pion utilisé par le joueur en question ("X" ou "O").

        Returns:
            bool: True si le joueur a gagné, False autrement.
        """

        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        return((self.cases[(0,0)].contenu==pion and self.cases[(0,1)].contenu==pion and self.cases[(0,2)].contenu==pion)
               or (self.cases[(1,0)].contenu==pion and self.cases[(1,1)].contenu==pion and self.cases[(1,2)].contenu==pion)
               or (self.cases[(2,0)].contenu==pion and self.cases[(2,1)].contenu==pion and self.cases[(2,2)].contenu==pion)
               or(self.cases[(0,0)].contenu==pion and self.cases[(1,0)].contenu==pion and self.cases[(2,0)].contenu==pion)
               or (self.cases[(0,1)].contenu==pion and self.cases[(1,1)].contenu==pion and self.cases[(2,1)].contenu==pion)
               or (self.cases[(0,2)].contenu==pion and self.cases[(1,2)].contenu==pion and self.cases[(2,2)].contenu==pion)
               or (self.cases[(0,0)].contenu==pion and self.cases[(1,1)].contenu ==pion and self.cases[(2,2)].contenu==pion)
               or (self.cases[(0,2)].contenu==pion and self.cases[(1,1)].contenu==pion and self.cases[(2,0)].contenu==pion))
  #cette fonction utiliser pour dupliquer un plateau*/
    
 def dup_plateau(self):
     copy_plateau=Plateau()
     for i in range(0,3):
       for j in range(0,3):
         copy_plateau.cases[(i,j)].contenu=self.cases[(i,j)].contenu
     return copy_plateau
    
 def choisir_prochaine_case(self, pion):
     import random   
     if(pion.upper()=="O"):
      pion_joueur="X"
     else:
      pion_joueur="O"
#ce bloc d'instruction permet a l'ordinateur de choisir le bon case pour gangner si a deux case remplie
     for i in range(0,3):
      for j in range(0,3):
       plateau_copy=self.dup_plateau() #c'est une duplication de plateau plateau_copy est un tableau utiliser par
                                       #l'ordinateur pour choisir le bon position pour avoir une plus de chance pour gangne
       if(plateau_copy.cases[(i,j)].est_vide()):
        plateau_copy.selectionner_case(i, j, pion)
        if plateau_copy.est_gagnant(pion):
            return[i,j]
        
                
            
    
#ce bloc d'instruction permet a l'ordinateur de bloquer le prochain deplacment  de personne
#cad il doit choisir le position qui gangne l'utilisateur
     for i in range(0,3):
      for j in range(0,3):
        plateau_copy=self.dup_plateau()
        if(plateau_copy.cases[(i,j)].est_vide()):
             plateau_copy.selectionner_case(i, j, pion_joueur)
             if plateau_copy.est_gagnant(pion_joueur):
                return[i,j]
      #ce block pour choisir la valeur de center      
     if(self.cases[(1,1)].est_vide()):
        return [1,1]
               
  #ce block pour choisir une valeur aleatoire aux corner
     corner_open=[]
     for i in range(0,3):
      for j in range(0,3):
       if [i,j] in [[0,0],[0,2],[2,0],[2,2]]:
        if(self.cases[(i,j)].est_vide()):
         corner_open.append([i,j])
     if len(corner_open)>0:
        ligne,colonne=random.choice(corner_open)
        corner_open.remove([ligne,colonne])
        return [ligne,colonne]    
     
      
#ce bloc c'est pour choisir des valeur aleatoire aux edge
     edges_open=[]
     for i in range(0,3):
      for j in range(0,3):
       if [i,j] in [[0,1],[1,0],[1,2],[2,1]]:
        if(self.cases[(i,j)].est_vide()):

         edges_open.append([i,j])
     if len(edges_open)>0:
        ligne,colonne=random.choice(edges_open)
        edges_open.remove([ligne,colonne])
        return [ligne,colonne]



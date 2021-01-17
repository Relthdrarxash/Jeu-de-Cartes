import pygame

fenetre = pygame.display.set_mode((800,600))

class Couleurs:
    def __init__(self, fenetre):
        self.couleurs =  ["Trèfle", "Carreau", "Coeur", "Pique"]
        self.selected_color = False
        self.rectangle = pygame.Rect(510, 110, 80, 390)
        self.selected = False
        self.i = None
        self.fenetre = fenetre
        
    def __repr__(self):
        return self.selected_color
        
    def affichage(self, fenetre):
        """
        Affichage des couleurs

        Returns
        -------
        None.

        """
        pygame.draw.rect(self.fenetre, (188,255,145), self.rectangle)
        pygame.draw.rect(self.fenetre, (0, 0, 0), self.rectangle, 1)
        #dessin du rectangle autour des cartes
        for i in range(4):
            # boucle pour afficher les couleurs
            couleur = pygame.image.load(f"Cartes/choix_{i}.png")
            espace_couleur = couleur.get_rect(center=(550, (150 + (i * 100))))
            self.fenetre.blit(couleur,(espace_couleur))
            
        if self.selected == True:
            # check if a color has been selected, then draws a circle around the selected one
            # thanks to self.i I can save the index of the selected color
            pygame.draw.circle(self.fenetre, (0,0,255), (550, (150 + (self.i * 100))), 30, 3)
        
    def circle(self, mousex, mousey):
        """
        Savoir quelle couleur a été selectionnée

        Parameters
        ----------
        mousex : int
            Position de la souris en x.
        mousey : int
            Position de la souris en y.

        Returns
        -------
        None.

        """
        for i in range(4):
            if mousex in range(530, 570) and mousey in range(130 + (i*100),170 + (i*100)):
                self.i = i
                self.selected_color = self.couleurs[i]
                self.selected = True
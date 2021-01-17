import pygame
import sys

class Mouse_Handling:
    def __init__(self, fenetre):
        self.mousex, self.mousey = pygame.mouse.get_pos()
        self.exit = False
        self.indicator = False
        self.fenetre = fenetre

    def handle_mouse(self, deck, textes, couleurs, couleur_carte, images, jeu, p1, p2, quit_screen):
        """
        

        Parameters
        ----------
        deck : class
            Objet contenant le deck avec les cartes et leur valeurs.
        textes : class
            Objet avec les textes (notamment le textes.fin qui sera utilisé ici "Exit")
        fenetre : pygame.Surface
            Fenêtre d'affichage.
        couleurs : class
            Objet avec les fonctions pour afficher les cercles, les couleurs.
        couleur_carte : list
            Liste avec les couleurs des cartes en fonction de leur nombre (pour le fichier Cartes)
        images : list
            Liste avec les images des cartes chargées.
        jeu : class
            Objet avec la fonction de jeu, gestion des points etc.
        p1 : class
            Objet avec les valeurs du Joueur 1.
        p2 : class
            Objet avec les valeurs .
        quit_screen : class
            Objet avec les fonctions pour quitter le jeu. et les écrans de fin

        Returns
        -------
        None.

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit('Partie interrompue par l\'utilisateur.')
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # On reprend les valeurs de la souris lorsque l'on clique
                self.mousex, self.mousey = pygame.mouse.get_pos()
                if couleurs.rectangle.collidepoint(pygame.mouse.get_pos()) and not self.exit:
                    # vérification que l'on n'est pas sur la fenêtre pour quitter le jeu
                    couleurs.circle(self.mousex, self.mousey)
                    # Trace le rond pour les couleurs
                    
                if deck.espace_carte.collidepoint(pygame.mouse.get_pos()) and not self.exit and couleurs.selected:
                    # Si pas sur l'écran pour quitter et qu'une couleur a été sélectionnée et que le deck a été cliqué
                    deck.tirage(images, couleur_carte)
                    deck.animation = True
                    deck.rect_carte_face = deck.carte_face.get_rect(center=(350, 250))
                    #Changement des coordonnées de la face de la carte, l'animation viendrait ici
                    jeu.jeu(couleurs.selected_color, self, deck, p1, p2, couleurs)
                    # Appel de la fonction de jeu pour les comparaisons et les points

                    
                if textes.fin.get_rect().collidepoint(pygame.mouse.get_pos()):
                    # quitter la partie
                    self.exit = True
                    # self.exit changera la boucle choisie dans la boucle de jeu pour celle pour quitter la partie
                    self.event = event

    
    def listener(self, textes):
        """
        

        Parameters
        ----------
        textes : class
            Objet avec les textes : la font, les règles.

        Returns
        -------
        None.

        """
        # écouter la touche pour passer les règles
        for event in pygame.event.get():
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    textes.rules_done = True
                    # fin des règles
                    textes.joueur = True
                    # début de l'affichage des joueurs
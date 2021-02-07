import pygame
from random import randint

class Jeu:
    def __init__(self, font, p1, p2, fenetre):
        self.font = font
        self.p1 = p1
        self.p2 = p2
        self.first_player = randint(0,1)
        self.text = f"Player {self.first_player + 1} starts"
        self.printed_text = font.render(self.text,True,pygame.Color("#000000"))
        self.espace_demarrage = self.printed_text.get_rect(center=(400, 300))
        self.consigne = self.font.render("Click on the deck",True,pygame.Color("#000000"))
        self.espace_consigne = self.consigne.get_rect(x=45, y=500)
        self.fenetre = fenetre
        self.players = ["Player 1", "Player 2"]
        self.vide = False
        
    def jeu(self, selected_color, mouse_h, deck, p1, p2, couleurs):
        """
        Fonction du jeu
        Compare les valeurs des cartes avec les couleurs sélectionnées
        
        Parameters
        ----------
        selected_color : TYPE
            DESCRIPTION.
        mouse_h : class
            Objet avec le management de la souris.
        deck : class
            Objet contenant le deck avec les cartes et leur valeurs.
        p1 : class
            Objet avec les propriétés du joueur 1.
        p2 : class
            Objet avec les propriétés du joueur 2.
        couleurs : class
            Objet avec les fonctions pour afficher les cercles, les couleurs.
        fenetre : pygame.Surface
            Fenêtre d'affichage.

        Returns
        -------
        None.

        """
        if self.p1.turn and couleurs.selected:
            # Au tour de p1 si une couleur a été selectionnée
            if selected_color == deck.carte_value:
                # Comparaison de la couleur sélectionnée avec la couleur de la carte
                self.p1.add_score(self.fenetre)
            self.p1.turn = False
            self.p2.turn = True
        elif self.p2.turn and couleurs.selected:
            if selected_color == deck.carte_value:
                self.p2.add_score(self.fenetre)
            self.p2.turn = False
            self.p1.turn = True
        couleurs.selected = False
        couleurs.selected_color = None
        # Remise à zéro de la couleur sélectionnée et de la sélection
        # J'aurais probablement pu mettre tout ça dans une seule et même variable
    
    def starting_player(self):
        """
        Lancement du premier joueur

        Returns
        -------
        None.

        """
        if self.first_player:
            self.p2.turn = True
        else:
            self.p1.turn = True
        
    def consignes(self, couleurs):
        if self.vide:
            self.text = None
            # Enlève la consigne si jeu.vide est vrai donc quand l'animation est en cours
        elif not couleurs.selected:
            self.text = "Veuillez selectionner une couleur"
        elif couleurs.selected:
            self.text = "Veuillez tirer une carte"
        self.consigne = self.font.render(self.text,True,pygame.Color("#000000"))
        self.espace_consigne = self.consigne.get_rect(x=45, y=500)
        self.fenetre.blit(self.consigne,(self.espace_consigne))
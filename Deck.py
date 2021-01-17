import pygame
from random import shuffle
fenetre = pygame.display.set_mode((800,600))

class Deck:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.carte = pygame.image.load("Cartes/back.png").convert_alpha()
        self.espace_carte = self.carte.get_rect(center=(150, 250))
        self.deck = list(i for i in range(52))
        
        self.carte_animee = pygame.image.load("Cartes/back.png").convert_alpha()
        self.rect_carte_animee = self.carte_animee.get_rect(center=(150, 250))
        self.animation = False
        
        self.carte_face = pygame.image.load("Cartes/back.png").convert_alpha()
        self.rect_carte_face = self.carte_face.get_rect(center=(150, 250))
        self.carte_value = None
        
        self.cartes_animees = pygame.image.load("Cartes/back.png").convert_alpha()
        self.rect_cartes_animees = self.cartes_animees.get_rect(center=(350, 250))
        self.animation_done = False
        self.authorization = False
        
    def affichage(self):
        self.fenetre.blit(self.carte, self.espace_carte)
        if self.animation_done:
            self.fenetre.blit(self.carte_face,(self.rect_carte_face))

    def animation_cartes(self):
        self.rect_carte_animee.move_ip(10,0)
        self.fenetre.blit(self.carte_animee, self.rect_carte_animee)
        if self.rect_carte_animee.centerx >= 350:
                self.animation = False
                self.rect_carte_animee.centerx = 150
                self.authorization = True
                self.animation_done = True
        
    def shuffle(self):
        shuffle(self.deck)
        
    def tirage(self, images, couleur_carte):
        self.carte_face = images[self.deck[0]]
        fenetre.blit(self.carte_face,(self.rect_carte_face))
        self.carte_value = self.deck[0]
        
        if self.deck[0] in couleur_carte["Trèfle"]:
            self.carte_value = "Trèfle"
            
        elif self.deck[0] in couleur_carte["Carreau"]:
            self.carte_value = "Carreau"
            
        elif self.deck[0] in couleur_carte["Coeur"]:
            self.carte_value = "Coeur"
            
        else:
            self.carte_value = "Pique"
            
        self.deck.pop(0)
        self.animation_done = False
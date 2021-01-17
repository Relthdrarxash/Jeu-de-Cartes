import pygame

class Defausse:
    def __init__(self, images):
        self.carte = "carte"
        self.empreinte_carte = pygame.Surface(images[0].get_size())
        self.rect_defausse = images[0].get_rect(center=(350, 250))
        
    def affichage(self, fenetre):
        fenetre.blit(self.empreinte_carte, self.rect_defausse)
        self.empreinte_carte.fill((188,255,145))
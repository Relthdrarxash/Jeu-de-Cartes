import pygame

class Display:
    
    def __init__(self):
        self.fenetre = pygame.display.set_mode((800,600))
        self.fin_demarrage = False
        
    def caption(self):
        pygame.display.set_caption("Jeu de cartes")
    
    def affichage_regles(self, textes, jeu):
        if not textes.joueur:
            # Affiche les règles
            self.affichage_demarrage(textes)
        elif textes.joueur:
            #Affiche les règles
            self.affichage_premier_joueur(jeu, textes)
        
    def affichage_demarrage(self, textes):
        self.fenetre.fill((148,216,45))
        textes.blit_text_rules((0, 100), self.fenetre, color=pygame.Color('black'))
            
    def affichage_premier_joueur(self, jeu, textes):
         self.fenetre.fill((148,216,45))
         self.fenetre.blit(jeu.printed_text,(jeu.espace_demarrage))
         self.joueur = False
         self.fin_demarrage = True
         
    def affichage(self, deck, p1, p2, defausse, couleurs, textes, mouse_h, jeu):
        self.fenetre.fill((148,216,45))
        self.fenetre.blit(deck.carte_face,(deck.rect_carte_face))    
        p1.affichage(self.fenetre)
        p2.affichage(self.fenetre)
        defausse.affichage(self.fenetre)
        couleurs.affichage(self.fenetre)
        textes.affichage()
        deck.affichage()
        if  p1.turn:
            pygame.draw.rect(p1.name, (255, 65 , 0), p1.rect, 2)
        elif p2.turn:
            pygame.draw.rect(p2.name, (255, 12 , 0), p2.rect, 2)
        jeu.consignes(couleurs)
            
    def affichage_fin(self, quit_screen):
        self.fenetre.fill((148,216,45))
        quit_screen.affichage()
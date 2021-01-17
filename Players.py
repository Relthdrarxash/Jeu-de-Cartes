import pygame

class Player_1:
    def __init__(self, font):
        self.font = font
        self.score = 0
        self.name = self.font.render(f"Player 1: {self.score} pts",True,pygame.Color("#000000"))
        self.rect = self.name.get_rect(x=50, y=30)
        self.turn = False
        self.color = "#000000"
        
    def affichage(self, fenetre):
        if self.turn:
            self.color = "#1d18f5"
            #Changement de couleur si c'est au tour du joueur
        elif not self.turn:
            self.color = "#000000"
        if self.score > 1:
            self.name = self.font.render(f"Player 1: {self.score} pts",True,pygame.Color(self.color))
        else:
            #removing the s if the score is lower than 2
            self.name = self.font.render(f"Player 1: {self.score} pt",True,pygame.Color(self.color))
        fenetre.blit(self.name,(self.rect))
        
    def add_score(self, fenetre):
        self.score += 1
        self.name = self.font.render(f"Player 1: {self.score} pts lol",True,pygame.Color(self.color))
        #Actualisation du score
        
class Player_2:
    def __init__(self, font):
        self.font = font
        self.score = 0
        self.name = font.render(f"Player 2: {self.score} pts",True,pygame.Color("#000000"))
        self.rect = self.name.get_rect(x=450, y=30)
        self.turn = False
        
    def affichage(self, fenetre):
        if self.turn:
            self.color = "#1d18f5"
            #Changement de couleur si c'est au tour du joueur
        elif not self.turn:
            self.color = "#000000"
        if self.score > 1:
            self.name = self.font.render(f"Player 1: {self.score} pts",True,pygame.Color(self.color))
        else:
            #removing the s if the score is lower than 2
            self.name = self.font.render(f"Player 1: {self.score} pt",True,pygame.Color(self.color))
        fenetre.blit(self.name,(self.rect))
        
    def add_score(self, fenetre):
        self.score += 1
        self.name = self.font.render(f"Player 2: {self.score} pts",True,pygame.Color("#000000"))
        #Actualisation du score
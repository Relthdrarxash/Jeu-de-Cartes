import pygame
import sys


class Quit_screen:
    def __init__(self, font, fenetre, p1, p2):
        # initialisation des variables pour pas avoir un appel super long
        # les variables en None seront définies dans les fonctions
        self.font = font
        self.want_quit = False
        self.choices =  ["Yes", "No"]
        self.fin = None
        self.espace_choices = None
        self.selected = None
        self.question = self.font.render("Do you really want to quit ?",True,pygame.Color("#FFFFFF"))
        self.espace_question = self.question.get_rect(center=(400, 250))
        self.text_colors = ["33f114", "f72c2c"]
        #couleurs pour le yes or no
        self.rectangle = pygame.Rect(195, 225, 410, 100)
        self.end_scores_text = None
        self.end_scores = None
        self.fenetre = fenetre
        self.p1 = p1
        self.p2 = p2
        
    def affichage(self):
        """
        Affiche l écran pour quitter avec Yes/No

        Returns
        -------
        None.

        """
        self.fenetre.fill((148,216,45)),
        pygame.draw.rect(self.fenetre, (0, 0, 0), self.rectangle)
        # le carré noir pcq c'est plus stylé
        self.fenetre.blit(self.question,(self.espace_question))
        #affichage de la question
        for i in range(2):
            #boucle pour afficher Yes/No
            self.fin = self.font.render(f"{self.choices[i]}",True,pygame.Color(f"#{self.text_colors[i]}"))
            self.espace_choices = self.fin.get_rect(center=((350 + i * 50), 300))
            self.fenetre.blit(self.fin,(self.espace_choices))
            
    def end(self, mouse_h,  event):
        #test de la réponse à la question avec la détection de Yes/No
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(2):
                #if i = 0 alors quitte, if i = 1 alors retour à l'écran précédent
                if mouse_h.mousex in range(325 + (i *50), 370 + (i * 50)) and mouse_h.mousey in range(290 ,350):
                    self.selected = self.choices[i]
        if self.selected == "Yes":
            pygame.quit()
            sys.exit('Partie interrompue par l\'utilisateur.')
        elif self.selected == "No":
            mouse_h.exit = False
            self.selected = None
    
    def gagnant(self):
        """
        Comparaisons pour trouver le joueur gagnant

        Returns
        -------
        str
            Le nom du gagnant

        """
        if self.p1.score > self.p2.score: 
            return "Player 1 a gagne !"
        elif self.p2.score > self.p1.score: 
            return "Player 2 a gagne !"
        else :
            return "Ex aeqo, plus de chances la prochaine fois !"
        
    def fin_partie(self):
        """
        Affiche un écran avec les scores et le gagnant de la partie
        à finir : problème d affichage, utiliser blit_text, définir un espace

        Returns
        -------
        None.

        """
        self.end_scores_text = f"Fin de partie, les scores sont : \n Player 1 : {self.p1.score}\n Player 2 : {self.p2.score} \n {self.gagnant()}"
        self.fenetre.fill((148,216,45))
        self.blit_text(self.end_scores_text, (200, 100), self.font)
        print("badaboum")
        # print(self.end_scores_text)
        
    def blit_text(self, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.fenetre.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                self.fenetre.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
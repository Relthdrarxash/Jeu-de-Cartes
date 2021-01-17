import pygame

class Textes:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.font = pygame.font.Font('Tytoon Mist.ttf', 30)
        self.fin = self.font.render("Exit game",True,pygame.Color("#000000"))
        self.espace_fin = self.fin.get_rect(x=0, y=0)
        self.texte_regles = "Le but du jeu est d’avoir le maximum de points lorsque la pioche est epuisee.\nOn dispose comme pioche un paquet de cartes standard de 52 cartes.\nLe premier joueur est choisi au hasard.\nA son tour de jeu, le joueur choisit une couleur parmi les quatre disponibles.\nIl pioche ensuite une carte dans le paquet.\nSi la couleur est la meme il marque un point.\nIl defausse alors la carte et passe la main"
        self.regles = self.font.render(self.texte_regles,True,pygame.Color("#000000"))
        self.espace_regles = pygame.Rect(100, 30, 600, 400)
        self.pass_screen = None
        self.espace_pass_screen = None
        self.rules_done = False
        self.joueur = False
        
    def affichage(self):
        """
        Affichage de "Exit"

        Returns
        -------
        None.

        """
        self.fenetre.blit(self.fin,(self.espace_fin))
    
    def blit_text_rules(self, pos, fenetre,  color=pygame.Color('black')):
        """
        Affichage des règles, retour à la ligne si le texte dépasse la fenêtre

        Parameters
        ----------
        pos : list
            list avec les coordonées en haut à gauche du rectangle d'affichage (<(800,600).
        fenetre : pygame.Surface
            Fenêtre d'affichage.
        color : pygame.Color
            The default color is black.

        Returns
        -------
        None.

        """
        self.pass_screen = self.font.render("Press Space to continue",True,pygame.Color("#000000"))
        self.espace_pass_screen = self.pass_screen.get_rect(x=0, y=0)
        self.fenetre.blit(self.pass_screen,(self.espace_pass_screen))
        # indiquer sur quelle touche il faut appuyer pour passer
        words = [word.split(' ') for word in self.texte_regles.splitlines()]  # 2D array where each row is a list of words.
        space = self.font.size(' ')[0]  # The width of a space.
        max_width, max_height = fenetre.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = self.font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                fenetre.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
        
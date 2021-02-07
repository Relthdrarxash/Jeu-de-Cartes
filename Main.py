# Import des bibliothèques
import pygame
import sys

from pygame import mouse 

from Couleurs import Couleurs
images = [pygame.image.load(f"Cartes/{i}.png").convert_alpha() for i in range(1, 53)]
from Deck import Deck
from Textes import Textes
from Players import Player_1, Player_2
from Defausse import Defausse
from Display import Display
from Mouse_Handling import Mouse_Handling
from Jeu import Jeu
from Quit_screen import Quit_screen

# Initialisation du module général
pygame.init()
# Initialisation du module texte
pygame.font.init()
# Initialisation de l'horloge pour le taux de rafraîchissement
clock = pygame.time.Clock()

# Chargement des classes
display = Display()
couleurs = Couleurs(display.fenetre)
couleur_carte =  {
    "Trèfle": [int(i) for i in range(13)], 
    "Carreau": [int(i) for i in range(13,26)], 
    "Coeur": [int(i) for i in range(26,39)],
    "Pique": [int(i) for i in range(39, 53)]}
deck = Deck(display.fenetre)
deck.shuffle()
textes = Textes(display.fenetre)
p1 = Player_1(textes.font)
p2 = Player_2(textes.font)
defausse = Defausse(images)
jeu = Jeu(textes.font, p1, p2, display.fenetre)
quit_screen = Quit_screen(textes.font, display.fenetre, p1, p2)
mouse_h = Mouse_Handling(display.fenetre)

# Titre de la fenêtre
display.caption()

# Tirage du premier joueur
jeu.starting_player()
fin_partie = False

# Boucle principale
while True : 
    # Taux de rafraîchissement
    clock.tick(60)
    
    # importer mouse_h.handle_keys avec tout 2 fois pour amener les nouvelles valeurs
    # je devrais juste faire ça pour mles valeurs qui changent pour raccourcir l'appel
    # Savoir si le bouton exit est cliqué puis afficher l'écran de sortie
    # try:
    print(mouse_h.compteur)
    if mouse_h.exit:
        display.affichage_fin(quit_screen)
        mouse_h.handle_mouse(deck, textes,  couleurs, couleur_carte, images, jeu, p1, p2, quit_screen)
        quit_screen.end(mouse_h, mouse_h.event)

    elif mouse_h.compteur == 2:
        quit_screen.fin_partie()
        pygame.display.update()
        clock.tick(0.3)
        pygame.quit()
        sys.exit()

    elif display.fin_demarrage:
        # fin_demarrage : démarrage fini, en gros la boucle principale c'est celle là
        mouse_h.handle_mouse(deck, textes,  couleurs, couleur_carte, images, jeu, p1, p2, quit_screen)
        display.affichage(deck, p1, p2, defausse, couleurs, textes, mouse_h, jeu)
        if deck.animation :
            jeu.vide = True
            deck.animation_cartes()
        else:
            jeu.vide = False
            # Pour avoir une consigne vide lors de l'animation
    
    else:
        # Test du démarrage, appuyer sur espace et enchainer les joueurs après les règles
        mouse_h.listener(textes)
        display.affichage_regles(textes, jeu)
        pygame.display.update()
        clock.tick(0.75)
        #Patiente 1.5 secondes pour lire le joueur qui commence
    # On met à jour l'affichage
    pygame.display.update()


"""    except Exception as e:
        print(e)
        # La fin du jeu provoque un erreur (index out of range puisqu'il n'y a plus de cartes)
        # Donc affichage des scores pour 2 secondes puis fin du jeu
        quit_screen.fin_partie()
        pygame.display.update()
        clock.tick(0.3)
        pygame.quit()
        sys.exit()"""
# Créer une classe avec toutes les variables qui changent ?
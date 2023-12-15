import pygame
import sys
from ia import ia

pygame.init()
fenetre_size = 600
fenetre = pygame.display.set_mode((fenetre_size, fenetre_size))
pygame.display.set_caption("Tic Tac Toe")

# La police
font = pygame.font.Font(None, 60)

# Initialise la grille de jeu
grille = [['' for _ in range(3)] for _ in range(3)]

# Nouvelle surface pour le résultat
nouvelle_surface = pygame.Surface((fenetre_size, 70))
nouvelle_surface.fill((225, 255, 255))

etat_jeu = "menu"

# Fonction pour le menu
def menu():
    background_image = pygame.image.load("images.png")
    background_image = pygame.transform.scale(background_image, (fenetre_size, fenetre_size))
    fenetre.blit(background_image, (0, 0))

    # Bouton 1 nouvelle partie
    nouvelle_partie = pygame.font.Font(None, 70).render("Nouvelle partie", True, (255, 165, 0))
    fenetre.blit(nouvelle_partie, (130, 205))

    # Bouton 2 quitter
    quitter = pygame.font.Font(None, 70).render("Quitter", True, (255, 165, 0))
    fenetre.blit(quitter, (225, 305))
    pygame.display.flip()

# Fonction pour l'arrière-plan
def arriere_plan():
    background_image = pygame.image.load("backround.webp")
    background_image = pygame.transform.scale(background_image, (fenetre_size, fenetre_size))
    fenetre.blit(background_image, (0, 0))
    for i in range(1, 3):
        pygame.draw.line(fenetre, (200, 235, 205), (i * fenetre_size // 3, 0), (i * fenetre_size // 3, fenetre_size), 2)
        pygame.draw.line(fenetre, (200, 235, 205), (0, i * fenetre_size // 3), (fenetre_size, i * fenetre_size // 3), 2)

# Fonction pour la logique d'exercice
def afficher_symboles():
    for i in range(3):
        for j in range(3):
            symbole = grille[i][j]
            if symbole != '':
                text = font.render(symbole, True, (255, 165, 0))
                text_rect = text.get_rect(center=(j * fenetre_size // 3 + fenetre_size // 6, i * fenetre_size // 3 + fenetre_size // 6))
                fenetre.blit(text, text_rect)

# Bouton retour et quitter
def afficher_boutons():
    retour_menu_text = pygame.font.Font(None, 40).render("Retour", True, (255, 165, 0))
    fenetre.blit(retour_menu_text, (75, 30))
    quitter_text = pygame.font.Font(None, 40).render("Quitter", True, (255, 165, 0))
    fenetre.blit(quitter_text, (fenetre_size - 190, 35))

# Fonction pour la vérification des colonnes et lignes
def verification_colonnes():
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != '':
            return True
        if grille[0][i] == grille[1][i] == grille[2][i] != '':
            return True

    # Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] != '':
        return True
    if grille[2][0] == grille[1][1] == grille[0][2] != '':
        return True
    return False

# Vérification de match nul
def verification_match_nul():
    return all(grille[i][j] != '' for i in range(3) for j in range(3))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gérez les événements du menu ici
        if etat_jeu == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= event.pos[0] <= 400 and 200 <= event.pos[1] <= 250:
                    # Clic sur le bouton "Nouvelle partie"
                    etat_jeu = "en_jeu"
                    grille = [['' for _ in range(3)] for _ in range(3)]  # Réinitialisez la grille
                elif 200 <= event.pos[0] <= 400 and 300 <= event.pos[1] <= 350:
                    # Clic sur le bouton "Quitter"
                    pygame.quit()
                    sys.exit()

        elif etat_jeu == "en_jeu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    un = mouse_pos[1] // (fenetre_size // 3)
                    deux = mouse_pos[0] // (fenetre_size // 3)

                    # Vérification si la case est vide avant de cliquer pour rajouter un X ou un O
                    if grille[un][deux] == '':
                        premier_joueur = 'X' if sum(un.count('X') for un in grille) <= sum(un.count('O') for un in grille) else 'O'
                        grille[un][deux] = premier_joueur

                        # Vérification de la victoire après chaque clic
                        if verification_colonnes():
                            arriere_plan()

    

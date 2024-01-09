import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
fenetre_size = 600
fenetre = pygame.display.set_mode((fenetre_size, fenetre_size))
pygame.display.set_caption("Tic Tac Toe")
font_menu = pygame.font.Font("dreamwish.ttf", 48)

# Police pour le texte
font = pygame.font.Font(None, 60)

# Initialisation de la grille de jeu
grille = [['' for _ in range(3)] for _ in range(3)]

# Nouvelle surface pour afficher le résultat
nouvelle_surface = pygame.Surface((fenetre_size, 70))
nouvelle_surface.fill((225, 255, 255))

# État du jeu ('menu' ou 'en_jeu')
etat_jeu = "menu"
mode_jeu = ""

# Fonction pour afficher le menu
def menu():
    background_image = pygame.image.load("Tissu Patchwork Pieces of Time Tic Tac Toe Moss.jpg")
    background_image = pygame.transform.scale(background_image, (fenetre_size, fenetre_size))
    fenetre.blit(background_image, (0, 0))

    nouvelle_partie = font_menu.render("Deux Joueurs", True, (0, 0, 0))
    fenetre.blit(nouvelle_partie, (130, 205))

    contre_ordi = font_menu.render("Contre l'Ordinateur", True, (0, 0, 0))
    fenetre.blit(contre_ordi, (70, 305))

    quitter = font_menu.render("Quitter", True, (0, 0, 0))
    fenetre.blit(quitter, (225, 405))
    pygame.display.flip()

# Fonction pour initialiser le mode de jeu (2 joueurs ou contre l'ordinateur)
def initialiser_mode_jeu():
    global joueur_actuel
    joueur_actuel = 'X'

# Fonction pour afficher l'arrière-plan du jeu
def arriere_plan():
    background_image = pygame.image.load("backround.webp")
    background_image = pygame.transform.scale(background_image, (fenetre_size, fenetre_size))
    fenetre.blit(background_image, (0, 0))
    for i in range(1, 3):
        pygame.draw.line(fenetre, (200, 235, 205), (i * fenetre_size // 3, 0), (i * fenetre_size // 3, fenetre_size), 2)
        pygame.draw.line(fenetre, (200, 235, 205), (0, i * fenetre_size // 3), (fenetre_size, i * fenetre_size // 3), 2)

# Fonction pour afficher les symboles sur la grille
def afficher_symboles():
    for i in range(3):
        for j in range(3):
            symbole = grille[i][j]
            if symbole != '':
                text = font.render(symbole, True, (255, 165, 0))
                text_rect = text.get_rect(center=(j * fenetre_size // 3 + fenetre_size // 6, i * fenetre_size // 3 + fenetre_size // 6))
                fenetre.blit(text, text_rect)

# Fonction pour afficher les boutons "Retour" et "Quitter"
def afficher_boutons():
    retour_menu_text = pygame.font.Font(None, 40).render("Retour", True, (255, 165, 0))
    fenetre.blit(retour_menu_text, (75, 30))
    quitter_text = pygame.font.Font(None, 40).render("Quitter", True, (255, 165, 0))
    fenetre.blit(quitter_text, (fenetre_size - 190, 35))

# Fonction pour vérifier les colonnes et les lignes
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

# Fonction pour vérifier s'il y a un match nul
def verification_match_nul():
    return all(grille[i][j] != '' for i in range(3) for j in range(3))

# Fonction pour afficher le résultat de la partie
def affichage_resultat():
    global etat_jeu
    arriere_plan()
    afficher_symboles()
    message = f"Le joueur {joueur_actuel} a gagné !"
    if verification_match_nul():
        message = "Match nul !"
    resultas_text = pygame.font.Font(None, 30).render(message, True, (100, 200, 230))
    nouvelle_surface.fill((225, 255, 255))  # Réinitialisation de la surface
    nouvelle_surface.blit(resultas_text, (fenetre_size // 2 - resultas_text.get_width() // 2, 25))
    fenetre.blit(nouvelle_surface, (0, 0))
    afficher_boutons()
    pygame.display.flip()
    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= event.pos[0] <= 250 and 20 <= event.pos[1] <= 70:
                    etat_jeu = "menu"
                    attente = False
                elif fenetre_size - 250 <= event.pos[0] <= fenetre_size - 50 and 50 <= event.pos[1] <= 70:
                    pygame.quit()
                    sys.exit()
        pygame.time.delay(10)


# Joueur actuel (X ou O)
joueur_actuel = 'X'

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if etat_jeu == "menu":
            # Gestion des événements dans l'état du menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Vérification des clics de souris pour les boutons du menu
                if 50 <= event.pos[0] <= 400 and 200 <= event.pos[1] <= 250:
                    etat_jeu = "en_jeu"
                    mode_jeu = "2_joueurs"
                    grille = [['' for _ in range(3)] for _ in range(3)]  # Réinitialisation de la grille
                    initialiser_mode_jeu()
                elif 50 <= event.pos[0] <= 550 and 300 <= event.pos[1] <= 350:
                    etat_jeu = "en_jeu"
                    mode_jeu = "contre_ordi"
                    grille = [['' for _ in range(3)] for _ in range(3)]  # Réinitialisation de la grille
                    initialiser_mode_jeu()
                elif 200 <= event.pos[0] <= 400 and 400 <= event.pos[1] <= 450:
                    pygame.quit()
                    sys.exit()

        elif etat_jeu == "en_jeu":
            # Gestion des événements dans l'état du jeu en cours
            if joueur_actuel == 'X':
                # Tour du joueur X
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    un = mouse_pos[1] // (fenetre_size // 3)
                    deux = mouse_pos[0] // (fenetre_size // 3)

                    if grille[un][deux] == '':
                        grille[un][deux] = joueur_actuel

                        # Vérification de la victoire ou match nul
                        if verification_colonnes():
                            # Affichage du résultat de la partie
                            affichage_resultat()
                        elif verification_match_nul():
                            # Affichage du résultat de la partie en cas de match nul
                            affichage_resultat()
                        else:
                            joueur_actuel = 'O'

            elif joueur_actuel == 'O':
                # Tour du joueur O (ou de l'ordinateur en mode 'contre_ordi')
                if mode_jeu == "2_joueurs":
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        un = mouse_pos[1] // (fenetre_size // 3)
                        deux = mouse_pos[0] // (fenetre_size // 3)

                        if grille[un][deux] == '':
                            grille[un][deux] = joueur_actuel

                            # Vérification de la victoire ou match nul
                            if verification_colonnes():
                                # Affichage du résultat de la partie
                                affichage_resultat()
                            elif verification_match_nul():
                                # Affichage du résultat de la partie en cas de match nul
                                affichage_resultat()
                            else:
                                joueur_actuel = 'X'
                elif mode_jeu == "contre_ordi":
                    if joueur_actuel == 'O':
                        # Tour de l'ordinateur (O)
                        cases_disponibles = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == '']
                        if cases_disponibles:
                            choix_ordi = random.choice(cases_disponibles)
                            grille[choix_ordi[0]][choix_ordi[1]] = joueur_actuel

                            # Vérification de la victoire ou match nul
                            if verification_colonnes():
                                # Affichage du résultat de la partie
                                affichage_resultat()
                            elif verification_match_nul():
                                # Affichage du résultat de la partie en cas de match nul
                                affichage_resultat()
                            else:
                                joueur_actuel = 'X'

    # Affichage du menu ou de l'arrière-plan du jeu
    if etat_jeu == "menu":
        menu()
    elif etat_jeu == "en_jeu":
        arriere_plan()
        afficher_symboles()

    pygame.display.flip()


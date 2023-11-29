import pygame
import math
from python_game.game import Game


pygame.init()

# Générer la fenêtre de notre jeu.
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# Importer l'arrière-plan du jeu.
background = pygame.image.load('PygameAssets-main/PygameAssets-main/bg.jpg')

# Importer la bannière.
banner = pygame.image.load('PygameAssets-main/PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 2 - banner.get_width() / 2)

# Importer le bouton pour lancer jeu.
play_button = pygame.image.load('PygameAssets-main/PygameAssets-main/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2 - play_button.get_width() / 2)
play_button_rect.y = math.ceil(screen.get_height() / 2)
# Charger notre jeu.
game = Game()

running = True

# Boucle tant que cette variable est vrai, le jeu tourne.
while running:

    # Applique l'arrière-plan du jeu.
    screen.blit(background, (0, -200))

    # Vérifier si le jeu a commencé ou non.
    if game.is_playing:
        # Déclencher les instructions de la partie
        game.update(screen)
    else:
        # Ajouter l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Mettre à jour l'écran.
    pygame.display.flip()

    # Si le joueur ferme la fenêtre.
    for event in pygame.event.get():
        # On vérifie que l'élément est la fermeture de la fenêtre.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu.")
        # Détecter si le joueur appuie sur une touche.
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détecter si c'est la touche espace qui est enclenché
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verification pour savoir si la souris est en collision avec le bouton de lancement
            if play_button_rect.collidepoint(event.pos):
                # Lancement du jeu.
                game.start()

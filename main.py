import pygame
import math
from game import Game
from highscore import Highscore


pygame.init()

save_file_name = "highscore.txt"
clock = pygame.time.Clock()
FPS = 120

# Générer la fenêtre de notre jeu.
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# Importer l'arrière-plan du jeu.
background = pygame.image.load('assets/bg.jpg')

# Importer la bannière.
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 2 - banner.get_width() / 2)

# Importer le fond pour les scores.
score_background = pygame.image.load('assets/score_screen.png')
score_background = pygame.transform.scale(score_background, (900, 600))
score_background_rect = score_background.get_rect()
score_background_rect.x = math.ceil(screen.get_width() / 2 - score_background.get_width() / 2)
score_background_rect.y = math.ceil(screen.get_height() / 2 - score_background.get_height() / 2)

# Importer le bouton pour lancer jeu.
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2 - play_button.get_width() / 2)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# Charger les highscores.
highscore = Highscore(save_file_name)

# Charger notre jeu.
game = Game(highscore)

running = True

# Boucle tant que cette variable est vrai, le jeu tourne.
while running:

    # Régule le framerate pour adapter la vitesse du jeu.
    clock.tick(FPS)

    # Applique l'arrière-plan du jeu.
    screen.blit(background, (0, -200))

    # Vérifier si le jeu a commencé ou non.
    if game.is_playing:
        # Déclencher les instructions de la partie
        game.update(screen)
    elif game.lose:
        screen.blit(score_background,score_background_rect)
        highscore.print(screen)
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
            highscore.save(save_file_name)
            running = False
            pygame.quit()
            print("Fermeture du jeu.")
        # Détecter si le joueur appuie sur une touche.
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détecter si c'est la touche espace qui est enclenché
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                elif game.lose:
                    # Retour à l'écran titre.
                    game.replay()
                else:
                    # Nettoyer le tableau des scores.
                    highscore.clean()
                    # Lancement du jeu.
                    game.start()
                    # Jouer le son de lancement.
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verification pour savoir si la souris est en collision avec le bouton de lancement
            if play_button_rect.collidepoint(event.pos) and not game.is_playing and not game.lose:
                # Nettoyer le tableau des scores.
                highscore.clean()
                # Lancement du jeu.
                game.start()
                # Jouer le son de lancement.
                game.sound_manager.play('click')
            elif game.lose:
                # Retour à l'écran titre
                game.replay()
                game.sound_manager.play('click')

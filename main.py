import pygame
from python_game.game import Game


pygame.init()

# Générer la fenètre de notre jeu.
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# Importer le l'arrière plan du jeux.
background = pygame.image.load('PygameAssets-main/PygameAssets-main/bg.jpg')

# Charger notre jeu.
game = Game()

running = True

# Boucle tant que cette variable est vrai, le jeu tourne.
while running:

    # Applique l'arrière plan du jeu.
    screen.blit(background, (0, -200))

    # Appliquer l'image de mon joueur.
    screen.blit(game.player.image, game.player.rect)

    # Récupérer tous les projectiles en cour et les faire avancer.
    for projectile in game.player.all_projectile:
        projectile.move()

    # Applique l'ensemble des image du groupe projectile.
    game.player.all_projectile.draw(screen)

    # Vérifier si le joueur veut aller à gauche ou à droite.
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x+game.player.rect.width < 1115:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -35:
        game.player.move_left()

    # Mettre à jour l'écran.
    pygame.display.flip()

    # Si le joueur ferme la fenetre.
    for event in pygame.event.get():
        # On verifie que l'élément est la fermeture de la fenètre.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu.")
        # Détécter si le joueur appuie sur un touche.
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détécter si c'est la touche espace qui est enclenché
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

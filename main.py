import pygame
pygame.init()

# Générer la fenètre de notre jeu.
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# Importer le l'arrière plan du jeux.
background = pygame.image.load('PygameAssets-main/PygameAssets-main/bg.jpg')


running = True

# Boucle tant que cette variable est vrai, le jeu tourne.
while running:

    # Applique l'arrière plan du jeu.
    screen.blit(background, (0,-200))

    # Mettre à jour l'écran.
    pygame.display.flip()

    # Si le joueur ferme la fenetre.
    for event in pygame.event.get():
        # On verifie que l'élément est la fermeture de la fenètre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu.")

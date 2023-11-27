import pygame
from projectile import Projectile


# Création d'une première classe qui va représenté le joueur.
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('PygameAssets-main/PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        # Créer une nouvelle instance de la classe Projectile dans le groupe
        self.all_projectile.add(Projectile(self))

    # Fonctions pour que le joueur puisse aller à gauche et à droites.
    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

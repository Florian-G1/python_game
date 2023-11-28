import pygame
from projectile import Projectile


# Création d'une première classe qui va représenter le joueur.
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('PygameAssets-main/PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_health_bar(self, surface):
        # Dessiner notre barre de vie.
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 8])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 8])

    def launch_projectile(self):
        # Créer une nouvelle instance de la classe Projectile dans le groupe.
        self.all_projectile.add(Projectile(self))

    # Fonctions pour que le joueur puisse aller à gauche et à droites.
    def move_right(self):
        # Le déplacement vers la droite est possible que s'il n'y a pas de collision.
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity

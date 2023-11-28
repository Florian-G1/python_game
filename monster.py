import pygame
import random


# Classe qui va gérer les monstres du jeu.
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self. game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = 1
        self.image = pygame.image.load('PygameAssets-main/PygameAssets-main/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            # Réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # Dessiner notre barre de vie.
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 15, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y - 20, self.health, 5])

    # Fonction qui fait avancer le monstre.
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # Si le monstre est en collision avec le joueur.
        else:
            # Inflige des dégâts au joueur.
            self.game.player.damage(self.attack)

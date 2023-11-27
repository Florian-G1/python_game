import pygame
from python_game.player import Player
from monster import Monster


# Création d'une classe qui va représenter le jeu.
class Game:

    def __init__(self):
        # Générer le joueur.
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # Fonction qui fait apparaitre un monstre.
    def spawn_monster(self):
        self.all_monster.add(Monster(self))
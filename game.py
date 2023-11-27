import pygame
from python_game.player import Player



# Création d'une classe qui va représenter le jeu.
class Game:

    def __init__(self):
        # Génerer le joueur.
        self.player = Player()
        self.pressed = {}
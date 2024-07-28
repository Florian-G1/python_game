import pygame
from comet import Comet


# Créer une classe qui va gérer l'évènement courant.
class CometFallEvent:

    # Lors du chargement, on crée un compteur.
    def __init__(self, game):
        self.game = game
        self.percent = 0
        self.percent_speed = 5
        self.fall_mode = False

        # Faire un groupe pour les comètes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += (self.percent_speed/100)

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # Définir le nombre de comètes selon la manche
        comet_number = 10 + self.game.current_wave
        for i in range(1,comet_number):
            # Faire apparaitre une comète.
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monster) == 0:
            print("Pluie de comètes !")
            self.meteor_fall()
            self.fall_mode = True # Active l'événement

    def update_bar(self, surface):
        self.add_percent()
        # barre noire (en arrière-plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # Axe des x.
            surface.get_height() - 20,  # Axe des y.
            surface.get_width(),  # Longueur de la barre.
            10  # Épaisseur de la barre.
        ])
        # Barre rouge (jauge d'évènement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # Axe des x.
            surface.get_height() - 20,  # Axe des y.
            (surface.get_width() / 100) * self.percent,  # Longueur de la barre.
            10  # Épaisseur de la barre.
        ])

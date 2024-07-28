import pygame
import random
import monster


# Créer une classe pour gérer la comète
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.comet_event = comet_event
        # Définir l'image assossié
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # Jouer le son
        self.comet_event.game.sound_manager.play('meteorite')
        if len(self.comet_event.all_comets) == 0:
            if len(self.comet_event.all_comets) == 0:
                print("L'évènement est fini !")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
                self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # Ne tombe pas sur le sol.
        if self.rect.y >= 520:
            self.remove()

        # S'il n'y a plus de boule de feu.
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("Joueur touché !")
            self.remove()
            # Retirer 20 points de vie
            self.comet_event.game.player.damage(20)

import pygame
import random
import animation


# Classe qui va gérer les monstres du jeu.
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self. game = game
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.max_health_bar_length = 100

    def set_max_heath(self, max_health, wave_multiplier=5):
        self.max_health = max_health + wave_multiplier * self.game.current_wave
        print(self.max_health)

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, self.default_speed)

    def set_loot_amount(self, loot_amount, wave_multiplier=5):
        self.loot_amount = loot_amount + wave_multiplier * self.game.current_wave

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            # Réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, self.default_speed)
            # Ajoute les points de score.
            self.game.add_score(self.loot_amount)

            # Si la barre d'évènement est pleine.
            if self.game.comet_event.is_full_loaded():
                # Retirer du jeu
                self.game.all_monster.remove(self)

                # Appel la méthode pour lancer l'évènement sans le déclencher en boucle
                self.game.comet_event.attempt_fall()

    def update(self, surface):
        # Dessiner notre barre de vie.
        health_bar_length = self.health * self.max_health_bar_length / self.max_health
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 15, self.rect.y - 20, self.max_health_bar_length, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y - 20, health_bar_length, 5])
        self.animate()

    # Fonction qui fait avancer le monstre.
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            self.start_animation()
        # Si le monstre est en collision avec le joueur.
        else:
            # Inflige des dégâts au joueur.
            self.game.player.damage(self.attack)


# Définir une classe pour la momie.
class Mummy(Monster):
    
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_max_heath(50)
        self.health = self.max_health
        self.set_speed(3)
        self.set_loot_amount(20)


# Définir une classe pour l'alien.
class Alien(Monster):
    
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.set_max_heath(100, 10)
        self.health = self.max_health
        self.set_speed(1)
        self.attack = 0.8
        self.set_loot_amount(50, 10)
        self.max_health_bar_length = 250
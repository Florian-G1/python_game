import pygame
from python_game.player import Player
from monster import Monster


# Création d'une classe qui va représenter le jeu.
class Game:

    def __init__(self):
        # Définir si le jeu a commencé ou non.
        self.is_playing = False
        # Générer le joueur.
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # Remettre le jeu à 0, retirer les monstres, remettre les pv au joueur...
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # Appliquer l'image de mon joueur.
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur.
        self.player.update_health_bar(screen)

        # Récupérer tous les projectiles en cours et les faire avancer.
        for projectile in self.player.all_projectile:
            projectile.move()

        # Récupérer tous les monstres en cours et les faire avancer.
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        # Applique l'ensemble des images du groupe projectile.
        self.player.all_projectile.draw(screen)

        # Applique l'ensemble des monstres du groupe de monstre.
        self.all_monster.draw(screen)

        # Vérifier si le joueur veut aller à gauche ou à droite.
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1115:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -35:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # Fonction qui fait apparaitre un monstre.
    def spawn_monster(self):
        self.all_monster.add(Monster(self))

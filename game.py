import pygame
from python_game.player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sound import SoundManager


# Création d'une classe qui va représenter le jeu.
class Game:

    def __init__(self):
        # Définir si le jeu a commencé ou non.
        self.is_playing = False
        # Générer le gestionnaire de son.
        self.sound_manager = SoundManager()
        # Générer le joueur.
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Générer les monstres.
        self.all_monster = pygame.sprite.Group()
        # Générer l'évènement.
        self.comet_event = CometFallEvent(self)
        # Générer le score.
        self.score = 0
        self.font = pygame.font.SysFont("monospace", 24)
        self.pressed = {}
        # Générer le décompte des vagues.
        self.current_wave = 0

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        self.increase_wave()

    def add_score(self, loot_amount):
        self.score += loot_amount

    def increase_wave(self):
        self.current_wave += 1

    def game_over(self):
        # Remettre le jeu à 0, retirer les monstres, remettre les pv au joueur...
        self.all_monster = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.fall_mode = False
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.current_wave = 0
        # Jouer le son de game over.
        self.sound_manager.play('game_over')

    def update(self, screen):
        # Afficher le score.
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0),)
        screen.blit(score_text, (20, 20))

        # Afficher la vague actuelle.
        current_wave_text = self.font.render(f"Vague : {self.current_wave}", 1, (0, 0, 0), )
        screen.blit(current_wave_text, (480, 20))

        # Appliquer l'image de mon joueur.
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur.
        self.player.update_health_bar(screen)

        # Actualiser l'animation du joueur
        self.player.update_animation()

        # Actualiser la barre de l'évènement.
        self.comet_event.update_bar(screen)

        # Récupérer tous les projectiles en cours et les faire avancer.
        for projectile in self.player.all_projectile:
            projectile.move()

        # Récupérer tous les monstres en cours et les faire avancer et actualiser leurs états.
        for monster in self.all_monster:
            monster.forward()
            monster.update(screen)

        # Récupérer toutes les comètes en cours et les faire avancer.
        for comets in self.comet_event.all_comets:
            comets.fall()

        # Applique l'ensemble des images du groupe projectile.
        self.player.all_projectile.draw(screen)

        # Applique l'ensemble des monstres du groupe de monstre.
        self.all_monster.draw(screen)

        # Applique l'ensemble des comètes du groupe de comète.
        self.comet_event.all_comets.draw(screen)

        # Vérifier si le joueur veut aller à gauche ou à droite.
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1115:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -35:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # Fonction qui fait apparaitre un monstre.
    def spawn_monster(self, monster_class_name):
        self.all_monster.add(monster_class_name.__call__(self))

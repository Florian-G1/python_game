import pygame


# Classe qui va gérer les monstres du jeu.
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self. game = game
        self.health = 100
        self.max_heath = 100
        self.attack = 5
        self.velocity = 1
        self.image = pygame.image.load('PygameAssets-main/PygameAssets-main/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540

    # Fonction qui fait avancer le monstre.
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

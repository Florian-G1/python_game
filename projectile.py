import pygame


# Définir la classe qui va gérer les projectiles du joueur.
class Projectile(pygame.sprite.Sprite):

    # Définir le constructeur de cette classe.
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('PygameAssets-main/PygameAssets-main/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    # Fait tourner le projectile.
    def rotate(self):
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    # Supprime le projectile.
    def remove(self):
        self.player.all_projectile.remove(self)

    # Déplace le projectile et le supprime quand nécessaire.
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # Suppression lors de la collision avec un monstre.
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            self.remove()
            # Inflige des dégâts.
            monster.damage(self.player.attack)
        # Suppression en sortie d'écran.
        if self.rect.x > 1080:
            self.remove()

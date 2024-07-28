import pygame


# Définir une classe qui va gérer les animations.
class AnimateSprite(pygame.sprite.Sprite):

    # Définir les choses à faire à la création de l'entité.
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.size = size
        # On commence l'animation à l'image 0.
        self.current_image = 0
        self.images = animation.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    # Méthode pour animer le sprite.
    def animate(self):
        # Vérifier si l'animation est activée pour cette entité
        if self.animation:

            # Passer à l'image suivante.
            self.current_image += 1

            # Vérifier si on a atteint la fin de l'animation.
            if self.current_image >= len(self.images):
                # Remettre l'animation au début.
                self.current_image = 0
                self.animation = False

            # Modifier l'image du sprite par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


def load_animation_image(sprite_name):
    # Charger les 24 image de ce sprite dans le dossier correspondant.
    images = []
    # Récupérer le chemin d'accès du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # Boucler sur chaque image dans le dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # Renvoyer le contenu de la liste d'image
    return images


# Définir un dictionnaire qui va contenir les images chargées de chaque entité.
animation = {
    'mummy': load_animation_image('mummy'),
    'player': load_animation_image('player'),
    'alien': load_animation_image('alien')
}

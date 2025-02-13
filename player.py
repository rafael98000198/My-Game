import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/player.png")
        self.image = pygame.transform.scale(self.image, [80, 30])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speed = 0
        self.acceleration = 0.1

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= 5
        elif keys[pygame.K_s]:
            self.rect.y += 5
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >480:
            self.rect.bottom = 480

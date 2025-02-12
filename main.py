import pygame

# Initializing pygame and creating the window
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My Game")

#
drawGroup = pygame.sprite.Group()

guy = pygame.sprite.Sprite(drawGroup)
guy.image = pygame.image.load("data/TestGuy.png")
guy.image = pygame.transform.scale(guy.image, [100, 100])
guy.rect = pygame.Rect(50, 50, 100, 100)


gameloop = True
if __name__ == "__main__":
    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            guy.rect.x -= 1

        if keys[pygame.K_d]:
            guy.rect.x += 1

        # draw()
        display.fill([46, 46, 46])

        drawGroup.draw(display)

        # player = pygame.Rect(50, 50, 100, 100)
        # pygame.draw.rect(display, [255, 255, 255, 255], player)

        pygame.display.update()

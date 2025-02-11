import pygame

# Initializing pygame and creating the window
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My Game")


def draw():
    display.fill([47, 212, 166])


gameloop = True
if __name__ == "__main__":
    while gameloop:
        draw()
        pygame.display.update()

import pygame
import random
from menu import show_menu
from player import Player
from enemies import Enemies
from shot import Shot

# Initializing pygame and creating the window
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My Game")

# Groups
objectGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

# music
pygame.mixer.music.load("data/music.mp3")
pygame.mixer.music.play(-1)

# sounds
shot = pygame.mixer.Sound("data/shot.wav")


def game_loop():
    player = Player(objectGroup)
    gameloop = True
    gameover = False
    timer = 20
    clock = pygame.time.Clock()

    while gameloop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameover:
                    shot.play()
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = player.rect.center

        if not gameover:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newEnemies = Enemies(objectGroup, enemiesGroup)
                    print("new enemies")

            collisions = pygame.sprite.spritecollide(player, enemiesGroup, False)

            if collisions:
                print("Game Over")
                gameover = True

            hits = pygame.sprite.groupcollide(shotGroup, enemiesGroup, True, True)

        display.fill([46, 46, 46])
        objectGroup.draw(display)
        pygame.display.update()


if __name__ == "__main__":
    action = show_menu()  # Display the menu
    if action == "start":
        game_loop()  # Start the game if the user presses "Start"

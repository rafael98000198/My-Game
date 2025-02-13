import pygame
import sys


def show_menu():
    pygame.init()

    # Define display and colors
    display = pygame.display.set_mode([840, 480])
    pygame.display.set_caption("My Game")

    # Colors
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Fonts
    font = pygame.font.SysFont('Arial', 40)
    title_font = pygame.font.SysFont('Arial', 70)

    # Button Rectangles
    start_button = pygame.Rect(320, 200, 200, 50)
    exit_button = pygame.Rect(320, 300, 200, 50)

    # Load background image
    background = pygame.image.load("data/background.png")  # Altere para o caminho do seu fundo
    background = pygame.transform.scale(background, (840, 480))  # Ajusta ao tamanho da tela

    # Music
    pygame.mixer.music.load("data/music.mp3")  # Altere para o caminho da música de fundo do menu
    pygame.mixer.music.play(-1)

    # Game loop for the menu
    while True:
        display.fill([0, 0, 0])

        # Draw background
        display.blit(background, (0, 0))

        # Draw the title (centered)
        title_text = title_font.render("Asteroid Hunter", True, WHITE)
        title_rect = title_text.get_rect(center=(420, 100))  # Centraliza o título
        display.blit(title_text, title_rect)

        # Draw buttons (centered)
        pygame.draw.rect(display, GREEN, start_button)
        pygame.draw.rect(display, RED, exit_button)

        start_text = font.render("Start", True, WHITE)
        exit_text = font.render("Exit", True, WHITE)

        start_rect = start_text.get_rect(center=start_button.center)
        exit_rect = exit_text.get_rect(center=exit_button.center)

        display.blit(start_text, start_rect)
        display.blit(exit_text, exit_rect)

        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "start"
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

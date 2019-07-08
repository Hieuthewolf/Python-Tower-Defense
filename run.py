import pygame

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((1350, 750))

    from starting_screen.starting_screen import StartingScreen
    starting_screen = StartingScreen(window)
    starting_screen.run_game()
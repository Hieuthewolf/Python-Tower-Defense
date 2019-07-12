import pygame
import os

# Initializing pygame
pygame.init()
background = pygame.image.load(os.path.join("images/screens", "bg.png")).convert_alpha()
darken_background = pygame.image.load(os.path.join("images/screens", "dark.png")).convert_alpha()

header_win = pygame.image.load(os.path.join("images/screens", "header_win.png")).convert_alpha()
header_lose = pygame.image.load(os.path.join("images/screens", "header_failed.png")).convert_alpha()

button_menu = pygame.image.load(os.path.join("images/screens", "button_menu.png")).convert_alpha()
empty_table =  pygame.image.load(os.path.join("images/screens", "table.png")).convert_alpha()

class EndingScreen:
    def __init__(self, window, game_status, username):
        self.window = window
        self.game_status = game_status
        self.username = username
        
        # Game dimensions
        self.width, self.height = 1350, 750 

        # Background images
        self.background = pygame.transform.scale(background, (self.width, self.height))
        self.background_darken = pygame.transform.scale(darken_background, (self.width, self.height))

        # Empty table for leaderboard
        self.empty_table = pygame.transform.scale(empty_table, (500, 650))

        # Indicating victory or defeat
        self.header_win = pygame.transform.scale(header_win, (325, 130))
        self.header_lose = pygame.transform.scale(header_lose, (325, 130))

        # To take back to main menu
        self.button_menu = pygame.transform.scale(button_menu, (120, 120))

    def draw(self):
        # Bliting the map
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.background_darken, (0, 0))

        # Bliting the scoreboard table
        self.window.blit(self.empty_table, (self.width // 2 - self.empty_table.get_width() // 2, self.height // 2 - self.empty_table.get_height() // 2))

        # Bliting victory or defeat sign
        if self.game_status == 'victory':
            self.window.blit(self.header_win, (self.width // 2 - self.header_win.get_width() // 2, self.height // 2 - self.empty_table.get_height() // 2))
        else:
            self.window.blit(self.header_lose, (self.width // 2 - self.header_win.get_width() // 2, self.height // 2 - self.empty_table.get_height() // 2))

        # Bliting menu and restart buttons
        self.window.blit(self.button_menu, (self.width // 2 - self.button_menu.get_width() // 2, self.height // 2 + self.empty_table.get_height() // 2 - 100))
        pygame.display.update()

    def run_game(self):
        ongoing = True

        while ongoing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ongoing = False

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    if self.width // 2 - self.button_menu.get_width() // 2 <= x <= self.width // 2 - self.button_menu.get_width() // 2 + self.button_menu.get_width():
                        if self.height // 2 + self.empty_table.get_height() // 2 - 100 <= y <= self.height // 2 + self.empty_table.get_height() // 2 - 100 + self.button_menu.get_height():
                            return 'restart'
            self.draw()

        pygame.quit()


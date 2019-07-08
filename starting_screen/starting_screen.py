import pygame
import os
from game import Game

# Initializing pygame
pygame.init()
game_font = pygame.font.SysFont('comicsans', 76)
start_btn = pygame.image.load(os.path.join("images", "button_play.png")).convert_alpha()
game_logo = pygame.transform.scale(pygame.image.load(os.path.join("images", "logo.png")), (632, 210)).convert_alpha()
dark_bg = pygame.image.load(os.path.join("images", "dark.png")).convert_alpha()

class StartingScreen:
    def __init__(self, window):
        self.width, self.height = 1350, 750 
        self.window = window
        self.background_img = pygame.image.load(os.path.join("images", "bg.png"))
        self.background_img = pygame.transform.scale(self.background_img, (self.width, self.height))

        self.font = game_font
        self.btn = (self.width/2 - start_btn.get_width()/2, self.height // 2, start_btn.get_width(), start_btn.get_height())

        self.map_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map_1_bg.png")), (self.width // 2, (self.height - game_logo.get_height()) // 2))
        self.map_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map_2_bg.png")), (self.width // 2, (self.height - game_logo.get_height()) // 2))
        self.map_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map_3_bg.png")), (self.width // 2, (self.height - game_logo.get_height()) // 2))
        self.map_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "map_4_bg.png")), (self.width // 2, (self.height - game_logo.get_height()) // 2))

        self.background_darken = pygame.transform.scale(dark_bg, (self.width, self.height))
        self.map_background_darken = pygame.transform.scale(dark_bg, (self.width // 2, self.map_1.get_height()))

        self.map_darken = [True, True, True, True] #Undarkens the appropriate map if selected

        self.selected = None

    def draw(self):
        self.window.blit(self.background_img, (0, 0)) #Background image
        self.window.blit(self.background_darken, (0, 0)) #Background image

        self.window.blit(game_logo, (self.width / 2 - game_logo.get_width() / 2, 0)) #Fantasy Game Logo

        # Bliting the maps
        self.window.blit(self.map_1, (0, game_logo.get_height()))
        self.window.blit(self.map_2, (0, game_logo.get_height() + self.map_1.get_height()))
        self.window.blit(self.map_3, (self.map_1.get_width(), game_logo.get_height()))
        self.window.blit(self.map_4, (self.map_1.get_width(), game_logo.get_height() + self.map_1.get_height()))

        # Bliting dark background for all the maps except the selected one
        if self.map_darken[0]:
            self.window.blit(self.map_background_darken, (0, game_logo.get_height()))
        if self.map_darken[1]:
            self.window.blit(self.map_background_darken, (0, game_logo.get_height() + self.map_1.get_height()))
        if self.map_darken[2]:
            self.window.blit(self.map_background_darken, (self.map_1.get_width(), game_logo.get_height()))
        if self.map_darken[3]:
            self.window.blit(self.map_background_darken, (self.map_1.get_width(), game_logo.get_height() + self.map_1.get_height()))

        # Drawing the white dividers
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(0, game_logo.get_height() + self.map_1.get_height(), self.width, 10))
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.map_1.get_width(), game_logo.get_height() + self.map_1.get_height(), self.width, 10))
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.map_1.get_width(), game_logo.get_height(), 10, self.map_1.get_height()))
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.map_1.get_width(), game_logo.get_height() + self.map_1.get_height(), 10, self.map_1.get_height()))

        self.window.blit(start_btn, (self.width // 2 - start_btn.get_width() / 2, self.height // 2 - start_btn.get_height() // 2 + 110))
        pygame.display.update()

    def run_game(self):
        ongoing = True

        while ongoing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ongoing = False

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()

                    if 0 <= x <= self.width // 2 - start_btn.get_width() // 2:
                        if game_logo.get_height() <= y <= game_logo.get_height() + self.map_1.get_height() - 10:
                            self.selected = 'map_1'

                    if 0 <= x <= self.width // 2 - start_btn.get_width() // 2:
                        if game_logo.get_height() + self.map_1.get_height() <= y <= self.height:
                            self.selected = 'map_2'

                    if self.width // 2 + start_btn.get_width() // 2 <= x <= self.width:
                        if game_logo.get_height() <= y <= game_logo.get_height() + self.map_1.get_height() - 10:
                            self.selected = 'map_3'

                    if self.width // 2 + start_btn.get_width() // 2 <= x <= self.width:
                        if game_logo.get_height() + self.map_1.get_height() <= y <= self.height:
                            self.selected = 'map_4'

                    if self.selected:
                        idx = int(self.selected[4]) - 1
                        self.map_darken[idx] = False

                        for i in range(len(self.map_darken)):
                            if i != idx:
                                self.map_darken[i] = True

                    if self.width // 2 - start_btn.get_width() // 2 + 75 <= x <= self.width // 2 + start_btn.get_width() // 2 - 75:
                        if self.height // 2 - start_btn.get_height() // 2 + 185 <= y <= self.height // 2 + start_btn.get_height() // 2 + 35:
                            if self.selected:       
                                game = Game(self.window, self.selected)
                                game.run_game()
                                del game

            self.draw()

        pygame.quit()

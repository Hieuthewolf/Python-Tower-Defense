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

game_font = pygame.font.SysFont('comicsans', 48)
sub_game_font = pygame.font.SysFont('comicsans', 32)

# For leaderboard stuff
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://hieuthewolf:hieutrung123@cluster0-qcx63.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["Python_Tower_Defense"]
collection = db["high_scores"]

class EndingScreen:
    """
    The very last screen that shows the leaderboard and game statistics 
    @param (SURFACE) window: pygame surface to render the screen
    @param (STR) game_status: either victoy or defeat to trigger "You Fail" or "You Win"
    @param (STR) username: unique username identifier to grab stats that pertain specifically for that user
    @param (STR) map_label: to indicate what map has been played
    """
    def __init__(self, window, game_status, username, map_label):
        self.window = window
        self.game_status = game_status
        self.username = username
        self.map_label = map_label

        # Game dimensions
        self.width, self.height = 1350, 750 

        # Background images
        self.background = pygame.transform.scale(background, (self.width, self.height))
        self.background_darken = pygame.transform.scale(darken_background, (self.width, self.height))

        # Empty table for leaderboard
        self.empty_table = pygame.transform.scale(empty_table, (500, 650))

        # Indicating victory or defeat
        self.header_win = pygame.transform.scale(header_win, (325, 115))
        self.header_lose = pygame.transform.scale(header_lose, (325, 115))

        # To take back to main menu
        self.button_menu = pygame.transform.scale(button_menu, (120, 120))

        self.font = game_font
        self.sub_font = sub_game_font

        self.leader_board = []

    def draw(self):
        """
        Draws the leaderboard and the various game statistics 

        --> return: None
        """

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

        txt_surface = self.font.render("Your Stats:", True, (255, 255, 255))
        self.window.blit(txt_surface, (self.width // 2 - txt_surface.get_width() // 2 + self.empty_table.get_width() - 35, self.height // 2 - 175 - txt_surface.get_height() // 2))

        txt_surface = self.font.render("Top 10 Leaderboard:", True, (255, 255, 255))
        self.window.blit(txt_surface, (self.width // 2 - txt_surface.get_width() // 2, self.height // 2 - 185 - txt_surface.get_height() // 2))

        username_surface = self.sub_font.render("Username", True, (255, 255, 255))
        wave_number_surface = self.sub_font.render("Wave #", True, (255, 255, 255))
        lives_surface = self.sub_font.render("Lives", True, (255, 255, 255))
        game_time_surface = self.sub_font.render("Time", True, (255, 255, 255))

        # Stats blitting for leaderboard
        self.window.blit(username_surface, (self.width // 2 - self.empty_table.get_width() // 2 + 50, self.height // 2 - 130 - txt_surface.get_height() // 2)) # username
        self.window.blit(wave_number_surface, (self.width // 2 - self.empty_table.get_width() // 2 + 190, self.height // 2 - 130 - txt_surface.get_height() // 2)) # wave_number
        self.window.blit(lives_surface, (self.width // 2 - self.empty_table.get_width() // 2 + 300, self.height // 2 - 130 - txt_surface.get_height() // 2)) # lives
        self.window.blit(game_time_surface, (self.width // 2 - self.empty_table.get_width() // 2 + 390, self.height // 2 - 130 - txt_surface.get_height() // 2)) # game_time

        # Stats blitting for individual stats
        self.window.blit(username_surface, (self.width // 2 - txt_surface.get_width() // 2 + self.empty_table.get_width() - 35, self.height // 2 - 125 - txt_surface.get_height() // 2)) # username
        self.window.blit(wave_number_surface, (self.width // 2 - txt_surface.get_width() // 2 + self.empty_table.get_width() - 35, self.height // 2 - 50 - txt_surface.get_height() // 2)) # wave_number
        self.window.blit(lives_surface, (self.width // 2 - txt_surface.get_width() // 2 + self.empty_table.get_width() - 35, self.height // 2 + 25 - txt_surface.get_height() // 2)) # lives
        self.window.blit(game_time_surface, (self.width // 2 - txt_surface.get_width() // 2 + self.empty_table.get_width() - 35, self.height // 2 + 100 - txt_surface.get_height() // 2)) # game_time

        # Drawing underline beneath stats
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.width // 2 - self.empty_table.get_width() // 2 + 50, self.height // 2 - 130 - txt_surface.get_height() // 2 + username_surface.get_height(), username_surface.get_width(), 3))
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.width // 2 - self.empty_table.get_width() // 2 + 190, self.height // 2 - 130 - txt_surface.get_height() // 2 + wave_number_surface.get_height(), wave_number_surface.get_width(), 3))
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.width // 2 - self.empty_table.get_width() // 2 + 300, self.height // 2 - 130 - txt_surface.get_height() // 2 + lives_surface.get_height(), lives_surface.get_width(), 3))
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.width // 2 - self.empty_table.get_width() // 2 + 390, self.height // 2 - 130 - txt_surface.get_height() // 2 + game_time_surface.get_height(), game_time_surface.get_width(), 3))

        for entry in self.leader_board[0:10]:
            username, wave_num, lives, time = entry['username'], entry['wave_number'], entry['lives'], entry['game_time']
            username_s= self.sub_font.render(username, True, (255, 255, 255))
            wave_number_s = self.sub_font.render(str(wave_num), True, (255, 255, 255))
            lives_s = self.sub_font.render(str(lives), True, (255, 255, 255))
            time_s = self.sub_font.render(str(time), True, (255, 255, 255))
            
            self.window.blit(username_s, (self.width // 2 - self.empty_table.get_width() // 2 + 50, self.height // 2 - 90 - txt_surface.get_height() // 2 + 35 * self.leader_board.index(entry))) # username
            self.window.blit(wave_number_s, (self.width // 2 - self.empty_table.get_width() // 2 + 215, self.height // 2 - 90 - txt_surface.get_height() // 2 + 35 * self.leader_board.index(entry))) # username
            self.window.blit(lives_s, (self.width // 2 - self.empty_table.get_width() // 2 + 325, self.height // 2 - 90 - txt_surface.get_height() // 2 + 35 * self.leader_board.index(entry))) # username
            self.window.blit(time_s, (self.width // 2 - self.empty_table.get_width() // 2 + 390, self.height // 2 - 90 - txt_surface.get_height() // 2 + 35 * self.leader_board.index(entry))) # username

            if entry['username'] == self.username:
                self.window.blit(username_s, (self.width - 100, self.height // 2 - 125 - txt_surface.get_height() // 2)) # username
                self.window.blit(wave_number_s, (self.width - 100 , self.height // 2 - 50 - txt_surface.get_height() // 2)) # username
                self.window.blit(lives_s, (self.width - 100, self.height // 2 + 25 - txt_surface.get_height() // 2)) # username
                self.window.blit(time_s, (self.width  - 100, self.height // 2 + 100 - txt_surface.get_height() // 2)) # username

        pygame.display.update()

    def run_game(self):
        """
        Main game loop to continuously run the ending_screen unless prompted to restart back to the beginning
        
        --> return: None
        """
        ongoing = True
        results = collection.find({"map_label": self.map_label})

        for entry in results.sort([('wave_number', pymongo.DESCENDING), ('lives', pymongo.DESCENDING), ('game_time', pymongo.ASCENDING)]):
            self.leader_board.append(entry)

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


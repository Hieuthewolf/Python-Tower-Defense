import pygame
from constants import Constants
import os

pygame.font.init()

upgrade_crystal = pygame.transform.scale(pygame.image.load(os.path.join("images/upgrade", "crystal_3.png")), (45, 45))
smaller_upgrade_crystal = pygame.transform.scale(pygame.image.load(os.path.join("images/upgrade", "crystal_3.png")), (15, 15))

class Button:
    """
    Button class for each of the menu objects
    """
    def __init__(self, name, image, menu):
        self.name = name
        self.image = image
        self.menu = menu
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.x = self.menu.x - Constants.DIMENSIONS['menu'][0] + self.width + 20

        # The vertical displacement distance varies if its att or sup tower b/c of added height of archers
        if self.menu.tower_name in Constants.SUP_TOWER_NAMES:
            self.y = self.menu.y - Constants.DIMENSIONS['supp_tower'][1] + 10
        else:
            self.y = self.menu.y - Constants.DIMENSIONS['att_tower'][1] + 10

    def click(self, X, Y):
        """
        returns True if mouse clicks on menu
        @param X: int
        @param Y: int
        :return: boolean
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def update_coordinates(self):
        self.x = self.menu.x - Constants.DIMENSIONS['menu'][0] + self.width + 20

        # The vertical displacement distance varies if its att or sup tower b/c of added height of archers
        if self.menu.tower_name in Constants.SUP_TOWER_NAMES:
            self.y = self.menu.y - Constants.DIMENSIONS['supp_tower'][1] + 10
        else:
            self.y = self.menu.y - Constants.DIMENSIONS['att_tower'][1] + 10

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
    

class MainButton(Button):
    def __init__(self, name, image, x, y, cost):
        self.name = name
        self.image = image
        self.x, self.y = x, y
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.cost = cost

class Menu:
    """
    Menu containing all the towers and items
    """
    def __init__(self, tower, menu_background):
        # Menu characteristics
        self.width, self.height = menu_background.get_width(), menu_background.get_height()
        self.buttons = []
        self.item_count = 0
        self.images = []
        self.font = pygame.font.SysFont("comicsans", 25)
        self.menu_background = menu_background

        # Tower characteristics
        self.tower_name = tower.name
        self.x, self.y = tower.x, tower.y
        self.tower_cost = tower.cost
        self.tower_level = tower.level
        self.tower_width = tower.width
        self.tower_height = tower.height

    def add_button(self, name, image):
        """
        Adds buttons to the menu board
        @param name: string
        @param image: surface
        :return: None
        """
        self.item_count += 1
        self.buttons.append(Button(name, image, self))

    def click(self, X, Y):
        """
        returns True if mouse clicks on menu
        @param X: int
        @param Y: int
        :return: boolean
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def get_clicked_item(self, X, Y):
        """
        returns the clicked item from the menu
        @param X: int
        @param Y: int
        :return: boolean
        """
        for it in self.buttons:
            if it.click(X, Y):
                return it.name

        return None

    def update_buttons(self):
        """
        Updates the menu and all of its button (x, y) coords
        :return: None
        """
        for btn in self.buttons:
            btn.update_coordinates()

    def draw(self, window):
        """
        Draws buttons and menu background
        @param window: surface
        :return: None
        """
        window.blit(self.menu_background, (self.x - self.menu_background.get_width() / 2, self.y - self.tower_height))
        for it in self.buttons:
            it.draw(window)
            window.blit(upgrade_crystal, (it.x + it.width + 5, it.y - 6)) #Positioning of the star

            txt = self.font.render(str(self.tower_cost[self.tower_level - 1]), 1, (255, 255, 255))
            window.blit(txt, (it.x + it.width + 30 - txt.get_width() / 2, it.y + upgrade_crystal.get_height() - 5))

class ShopMenu(Menu):
    """
    Sidebar shop menu to buy towers
    """
    def __init__(self, x, y, menu_background):
        # Menu characteristics
        self.x, self.y = x, y
        self.width, self.height = menu_background.get_width(), menu_background.get_height()
        self.buttons = []
        self.item_count = 0
        self.images = []
        self.font = pygame.font.SysFont("comicsans", 25)
        self.menu_background = menu_background

        self.start_new_line = 0
    
    def add_button(self, name, image, cost):
        """
        Adds buttons to the menu board
        @param name: string
        @param image: surface
        :return: None
        """
        x_btn_coord = ((self.item_count) % 2) * self.x + 5
        self.item_count += 1

        if self.item_count % 3 == 0:
            self.start_new_line += 1

        y_btn_coord = self.y + 15 + self.start_new_line * 100
        self.buttons.append(MainButton(name, image, x_btn_coord, y_btn_coord, cost))

    def get_it_cost(self, name):
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        return -1

    def draw(self, window):
        window.blit(self.menu_background, (self.x - self.width / 2, self.y))
        for it in self.buttons:
            it.draw(window)
            window.blit(smaller_upgrade_crystal, (it.x + 5, it.y + it.height + 5)) #Positioning of the star
            txt = self.font.render(str(it.cost), 1, (255, 255, 255))
            window.blit(txt, (it.x + smaller_upgrade_crystal.get_width() + 8, it.y + it.height + 5))

            


    

    

        





        
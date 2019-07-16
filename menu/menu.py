import pygame
from constants import GameConstants, TowerConstants
import os

pygame.font.init()

upgrade_crystal = pygame.transform.scale(pygame.image.load(os.path.join("images/upgrade", "crystal_3.png")), (20, 20))
smaller_upgrade_crystal = pygame.transform.scale(pygame.image.load(os.path.join("images/upgrade", "crystal_3.png")), (15, 15))

class Button:
    """
    Reusable button class for shop menu and tower menu
    @param (STR) name: name of button to be linked to a specific tower
    @param (SURFACE) image: button image to be displayed
    @param (OBJECT) menu: menu object that contains all information regarding towers and menu attributes
    @param (INT) item_count: integer to keep track of how many items are added to a menu
    """
    def __init__(self, name, image, menu, item_count):
        self.name = name
        self.image = image
        self.menu = menu
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.extra_padding = 10
        self.item_count = item_count 

        self.x = self.menu.x - GameConstants.DIMENSIONS['menu'][0] + self.item_count * (self.width + 1.3 * self.extra_padding)

        if self.menu.tower_name in TowerConstants.SUP_TOWER_NAMES:
            self.y = self.menu.y - GameConstants.DIMENSIONS['supp_tower'][1]
        elif self.menu.tower_name in TowerConstants.MAGIC_TOWER_NAMES:
            self.y = self.menu.y - GameConstants.DIMENSIONS['magic_tower'][1]  
        else:
            self.y = self.menu.y - GameConstants.DIMENSIONS['att_tower'][1] 

    def click(self, X, Y):
        """
        returns True if mouse clicks on button
        @param (INT) X: x-coordinate of mouse position
        @param (INT) Y: y-coordinate of mouse position

        --> return: Boolean
        """
        if X <= self.x + self.width - self.extra_padding and X >= self.x + self.extra_padding:
            if Y <= self.y + self.height - self.extra_padding and Y >= self.y + self.extra_padding:
                return True
        return False

    def update_coordinates(self):
        """
        Updates button coordinates for a specific tower once its been placed down

        --> return: None
        """
        self.x = self.menu.x - GameConstants.DIMENSIONS['menu'][0] + self.item_count * (self.width + 1.3 * self.extra_padding)

        if self.menu.tower_name in TowerConstants.SUP_TOWER_NAMES:
            self.y = self.menu.y - GameConstants.DIMENSIONS['supp_tower'][1] 
        elif self.menu.tower_name in TowerConstants.MAGIC_TOWER_NAMES:
            self.y = self.menu.y - GameConstants.DIMENSIONS['magic_tower'][1] 
        else:
            self.y = self.menu.y - GameConstants.DIMENSIONS['att_tower'][1] 

    def draw(self, window):
        """
        Draws the button image on the screen
        @param (SURFACE) window: surface for rendering the drawing

        --> return: None
        """
        window.blit(self.image, (self.x, self.y))
    

class ShopButton(Button):
    """
    Specific button for the shop menu to buy towers
    """
    def __init__(self, name, image, x, y, cost):
        self.name = name
        self.image = image
        self.x, self.y = x, y
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.cost = cost
        self.extra_padding = 10

class GameStateButton(Button):
    """
    Specific button to toggle spawning waves and playing music
    """
    def __init__(self, play_img, pause_img, x, y):
        self.images = [play_img, pause_img]
        self.x = x
        self.y = y
        self.image = self.images[0]
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.extra_padding = 10

    def switch_img(self):
        """
        Switches between the sound on/sound off icons for the image being displayed

        --> return : None
        """
        if self.image == self.images[0]:
            self.image = self.images[1]
        else:
            self.image = self.images[0]

class Menu:
    """
    Generic menu class 
    """
    def __init__(self, tower, menu_background):
        # Menu characteristics
        self.width, self.height = menu_background.get_width(), menu_background.get_height()
        self.buttons = [] #Contains all the buttons in our menu
        self.item_count = 0 
        self.images = []
        self.font = pygame.font.SysFont("comicsans", 22)
        self.menu_background = menu_background
        self.extra_padding = 10

        # Tower characteristics
        self.tower = tower
        self.x, self.y = tower.x, tower.y

        self.tower_name = tower.name
        self.tower_cost = tower.cost
        self.tower_level = tower.level
        self.tower_width = tower.width
        self.tower_height = tower.height
        self.tower_sell_price = tower.sell_price

    def add_button(self, name, image):
        """
        Adds buttons to our menu
        @param (STR) name: name of the button (specifically tower name)
        @param (SURFACE) image: image surface

        --> None
        """
        self.item_count += 1
        self.buttons.append(Button(name, image, self, self.item_count))

    def click(self, X, Y):
        """
        returns True if mouse clicks on button
        @param (INT) X: x-coordinate of mouse position
        @param (INT) Y: y-coordinate of mouse position

        --> return: Boolean
        """

        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def get_clicked_item(self, X, Y):
        """
        returns the clicked item from the menu
        @param (INT) X: x-coordinate of mouse position
        @param (INT) Y: y-coordinate of mouse position

        --> return: Boolean
        """
        for item in self.buttons:
            if item.click(X, Y):
                return item.name

        return None

    def update_buttons(self):
        """
        Updates the menu and all of its button (x, y) coords

        --> return: None
        """
        for btn in self.buttons:
            btn.update_coordinates()

    def draw(self, window):
        """
        Draws buttons and tower menu background
        @param (SURFACE) window: window surface

        --> return: None
        """
        window.blit(self.menu_background, (self.x - self.menu_background.get_width() / 2, self.y - self.tower_height - self.extra_padding))
        for it in self.buttons:
            it.draw(window)
            window.blit(upgrade_crystal, (it.x - self.extra_padding // 2, it.y + self.menu_background.get_height() // 2 + self.extra_padding)) #Positioning of the star
            if it.name == 'upgrade': # for upgrading a tower
                if isinstance(self.tower_cost[self.tower_level - 1], str):
                    txt = self.font.render(str(self.tower.get_upgrade_cost()), 1, (255, 255, 255))
                else:
                    txt = self.font.render("-" + str(self.tower.get_upgrade_cost()), 1, (255, 255, 255))
            else: # for selling a tower
                txt = self.font.render("+" + str(self.tower.get_sell_cost()), 1, (255, 255, 255))
            window.blit(txt, (it.x + upgrade_crystal.get_width() - self.extra_padding // 3, it.y + self.menu_background.get_height() // 2 + 1.2 * self.extra_padding))

class ShopMenu(Menu):
    """
    Sidebar shop menu to buy towers
    """
    def __init__(self, x, y, menu_background):
        # Menu characteristics
        self.x, self.y = x, y
        self.menu_background = menu_background
        self.width, self.height = menu_background.get_width(), menu_background.get_height()
        self.buttons = []

        self.item_count = 0
        self.images = []
        self.font = pygame.font.SysFont("comicsans", 25)

        self.start_new_line = 0
    
    def add_button(self, name, image, cost):
        """
        Adds buttons to the shop menu board and arranges them in a n x 2 configuration 
        @param (STR) name: name of the button (specifically tower name)
        @param (SURFACE) image: image surface
        
        --> return: None
        """
        if self.item_count % 2 == 0 and self.item_count != 0:
            self.start_new_line += 1

        self.item_count += 1

        if self.item_count % 2 == 0:
            x_btn_coord = self.x - self.width // 2 + 15
        else:
            x_btn_coord = self.x + 10

        y_btn_coord = self.y + 15 + self.start_new_line * 100
        self.buttons.append(ShopButton(name, image, x_btn_coord, y_btn_coord, cost))

    def get_item_cost(self, name):
        """
        Gets item cost associated with a specific tower when buying it from the shop
        @param (STR) name: name of the button (specifically tower name)

        --> return : Int
        """

        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        return -1

    def draw(self, window):
        """
        Draws buttons and shop menu background
        @param (SURFACE) window: window surface

        --> return: None
        """
        window.blit(self.menu_background, (self.x - self.width / 2, self.y))
        for it in self.buttons:
            it.draw(window)
            window.blit(smaller_upgrade_crystal, (it.x + 2, it.y + it.height + 5)) #Positioning of the star
            txt = self.font.render(str(it.cost), 1, (255, 255, 255))
            window.blit(txt, (it.x + smaller_upgrade_crystal.get_width() + 5, it.y + it.height + 5))

            


    

    

        





        
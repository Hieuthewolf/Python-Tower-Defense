from objectFormation import GameObjects
from constants import TowerConstants
from usefulFunctions import import_images_numbers
from menu.menu import Menu
import pygame
import os

menu_background = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "menu.png")), (130 , 70))
upgrade_button = pygame.transform.scale(pygame.image.load(os.path.join("images/upgrade", "upgrade.png")), (55 , 55))
level_up = import_images_numbers("images/level_up/", 1, 25, (300, 300))

class Tower(GameObjects):
    def __init__(self, name, coord):
        super().__init__(name, coord)
        # Tower coordinates
        self.x = self.coord[0]
        self.y = self.coord[1]

        # Characteristics
        self.sell_price = [0, 0, 0]
        self.level = 1

        # Cost
        self.cost = TowerConstants.UPGRADE_COST[name]

        # Tower dimensions
        self.width = self.dimensions[0]
        self.height = self.dimensions[1]

        # Clicking on a tower
        self.selected = False
        
        # Tower images
        self.tower_images = []

        # Specific range for each tower
        self.range = TowerConstants.TOWER_RADIUS_RANGE[name]

        # Leveling up animation
        self.level_up_animation = False
        self.level_animation = 0
        self.level_up = level_up

        # Menu logistics
        self.menu = Menu(self, menu_background)
        self.menu.add_button("upgrade", upgrade_button)

        # Damage for towers that deal damage
        self.base_damage = 0
        self.damage = self.base_damage

        # For moving the archer tower when purchasing from the shops
        self.being_dragged = False

    def draw(self, window):
        """
        Using our list of images, draws the tower
        :param window: surface
        :return: None
        """
        #Drawing menu
        if self.selected:
            self.menu.draw(window)

        tower_image = self.tower_images[self.level - 1]
        window.blit(tower_image, (self.x - tower_image.get_width() // 2, self.y - tower_image.get_height() // 2))

        if self.level_up_animation:
            window.blit(self.level_up[self.level_animation // 2], (self.x - tower_image.get_width() - 75, self.y - 225))
            self.level_animation += 1
            if self.level_animation == len(level_up) * 2:
                self.level_up_animation = False
                self.level_animation = 0

    def draw_tower_radius(self, window):    
        if self.selected:
            #tower transparent circular range indicator
            s = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(s, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            
            window.blit(s, (self.x - self.range, self.y - self.range))

    def click(self, X, Y):
        """
        returns a boolean if tower has been clicked on and selects the tower if it's clicked
        :param X: int
        :param Y: int
        :return: bool
        """
        tower_image = self.tower_images[self.level - 1]

        # Att tower dimensions will be different from that of support towers and magic towers

        if self.name in TowerConstants.ATT_TOWER_NAMES:
            if X <= self.x + tower_image.get_width() // 2  - 15 and X >= self.x - tower_image.get_width() // 2 + 5:
                if Y  <= self.y + self.height - tower_image.get_height() - 25 and Y >= self.y - tower_image.get_height() + 20:
                    return True
            return False

        elif self.name in TowerConstants.SUP_TOWER_NAMES:
            if X <= self.x + tower_image.get_width() // 2  and X >= self.x - tower_image.get_width() // 2 :
                if Y  <= self.y + tower_image.get_height() // 2 and Y >= self.y - tower_image.get_height() // 2:
                    return True
            return False

    def sell(self):
        """
        Sells the tower once it has been placed down and return the selling price
        :return: int
        """
        return self.sell_price[self.level - 1]

    def upgrade(self):
        """
        Upgrades tower for a certain cost
        :return: None
        """
        if self.level < len(self.tower_images):
            self.level_up_animation = True
            self.level += 1
            self.base_damage += 1
            self.damage = self.base_damage
            #Since level does not upgrade in menu we have to manually do it here
            self.menu.tower_level += 1
    
    def get_upgrade_cost(self):
        """
        Returns upgrade cost; 0 --> indicates that we can't upgrade
        :return: int
        """
        return self.cost[self.level - 1]

    def move(self, x, y):
        """
        Moves our tower to the coordinate (x, y)
        @param x: int
        @param y: int
        :return: None
        """
        self.menu.x, self.menu.y = x, y
        self.x, self.y = x, y
        self.menu.update_buttons()






    
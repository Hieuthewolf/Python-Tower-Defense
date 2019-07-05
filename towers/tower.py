from objectFormation import GameObjects
from constants import TowerConstants
from usefulFunctions import import_images_numbers, calculate_distance
from menu.menu import Menu
import pygame
import os

import math

menu_background = pygame.transform.scale(pygame.image.load(os.path.join("images/menu", "menu.png")), (145 , 90))
upgrade_button = pygame.transform.scale(pygame.image.load(os.path.join("images/upgrade", "upgrade.png")), (55, 55))
sell_button = pygame.transform.scale(pygame.image.load(os.path.join("images/upgrade", "undo.png")), (55, 55))

level_up = import_images_numbers("images/level_up/", 1, 25, (300, 300))

class Tower(GameObjects):
    """
    Base structural class for our towers
    @param (STR) name: name of object 
    @param (TUPLE) coord: (x, y) coordinates of object 
    """
    def __init__(self, name, coord):
        super().__init__(name, coord)
        # Tower coordinates
        self.x = self.coord[0]
        self.y = self.coord[1]
        
        # Allows for upgrade references
        self.level = 1

        # Upgrade Cost
        self.cost = TowerConstants.UPGRADE_COST[name]

        # Selling logistics
        self.original_price = TowerConstants.ORIGINAL_PRICE[name]
        self.sell_price = [self.original_price, self.cost[0], self.cost[1]]

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
        self.menu.add_button("sell", sell_button)

        # Damage for towers that deal damage
        self.base_damage = 0
        self.damage = self.base_damage

        # For moving the archer tower when purchasing from the shops
        self.being_dragged = False

        # Padding for clicking purposes
        self.extra_padding = 10

    def draw(self, window):
        """
        Draws the tower, menu, and level-up animation upon condition
        @param (SURFACE) window: surface for rendering the drawing
        
        --> return: None
        """
        if self.selected:
            self.menu.draw(window)  #Drawing menu

        tower_image = self.tower_images[self.level-1]

        if not self.level_up_animation: #Always draw the tower except when leveling up
            window.blit(tower_image, (self.x - tower_image.get_width() // 2, self.y - tower_image.get_height() // 2))

        else: #Leveling up animation procedure
            window.blit(self.level_up[self.level_animation // 2], (self.x - tower_image.get_width() - 75, self.y - 225))
            self.level_animation += 1
            if self.level_animation == len(level_up) * 2:
                self.level_up_animation = False
                self.level_animation = 0

    def click(self, X, Y):
        """
        returns True if tower has been selected else False
        @param (INT) X: mouse position's x-coordinate
        @param (INT) Y: mouse position's y-coordinate
        
        --> return: Bool
        """
        tower_image = self.tower_images[self.level - 1]

        if X <= self.x + tower_image.get_width() // 2  - 2 * self.extra_padding and X >= self.x - tower_image.get_width() // 2 + self.extra_padding // 2:
            if self.name in TowerConstants.MAGIC_TOWER_NAMES or self.name in TowerConstants.SUP_TOWER_NAMES:
                if Y <= self.y + self.height // 2 - (2 * self.extra_padding) and Y >= self.y - self.height // 2 + (2 * self.extra_padding):
                    return True
            else:
                if Y <= self.y + self.height // 2 - (4 * self.extra_padding) and Y >= self.y - self.height // 2 + (2 * self.extra_padding):
                    return True
        return False


    def get_sell_cost(self):
        """
        Sells the tower at a specific level at a reduced cost using our self.sell_price list of prices

        --> return: Int
        """
        return round(0.75 * self.sell_price[self.level - 1])

    def upgrade(self):
        """
        Upgrades our tower and increment certain tower characteristics 

        --> return: None
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
        Returns our upgrade cost for the next tower level

        --> return: Int
        """
        return self.cost[self.level - 1]

    def move(self, X, Y):
        """
        Moves our tower to the coordinate (x, y) and updates menu coordinates
        @param (INT) X: mouse position's x-coordinate
        @param (INT) Y: mouse position's y-coordinate
        
        --> return: None
        """
        self.menu.x, self.menu.y = X, Y
        self.x, self.y = X, Y
        self.menu.update_buttons()

    def get_closest_distance_to_path(self, path):
        """
        Gets the closest distance from a tower at any point to the path 
        @param (LIST) path: list of tuples containing path coordinates

        --> return: Float
        """
        game_path = path[:]
        game_path.sort(key = lambda coord: calculate_distance(self, coord))
        point_A = game_path[0] # Closest point out of all the points on the path to to the tower

        try:
            point_after_A = path[path.index(point_A) + 1]
            point_before_A = path[path.index(point_A) - 1]
            closest_to_A = min(point_after_A, point_before_A, key = lambda point: calculate_distance(point_A, point))
        except:
            if path.index(point_A) == 0:
                closest_to_A = path[path.index(point_A) + 1]
            
            elif path.index(point_A) == len(path) - 1:
                closest_to_A = path[path.index(point_A) - 1]
        finally:
            m = (closest_to_A[1] - point_A[1]) / (closest_to_A[0] - point_A[0])
            b = point_A[1] - m * point_A[0]

            closest_distance = abs(-m * self.x + self.y - b) / math.sqrt((-m) ** 2 + 1)
            return closest_distance
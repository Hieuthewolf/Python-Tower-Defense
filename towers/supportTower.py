import pygame
from .tower import Tower
import os
import math
import time
from usefulFunctions import import_images_numbers

# <-------------------------------------------- DAMAGE TOWER  -------------------------------------------------->
damage_tower = [pygame.transform.scale(pygame.image.load(os.path.join("images/towers/support_towers/damage_support_tower/", "1.png")), (80, 80)),
                pygame.transform.scale(pygame.image.load(os.path.join("images/towers/support_towers/damage_support_tower/", "2.png")), (80, 80)),
                pygame.transform.scale(pygame.image.load(os.path.join("images/towers/support_towers/damage_support_tower/", "3.png")), (80, 80))
                ]

class DamageTower(Tower):
    """
    Increase damage of nearby towers in a circular radius
    """
    def __init__(self, name, coord):
        super().__init__(name, coord)
        self.tower_images = damage_tower[:]
        self.damage_increase = [0.2, 0.4, 0.6]

    def draw(self, window):
        """
        Draws support towers as based on their specific level 
        @param (SURFACE) window: surface for rendering the drawing

        --> return: None
        """
        super().draw(window)

    def support(self, towers):
        """
        Increase nearby tower stats based on its support type (ranged vs damage)
        @param (LIST) towers: list of all attack towers (magic and archer)

        --> return: None
        """
        in_range = [tw for tw in towers if math.sqrt((self.x - tw.x) ** 2 + (self.y - tw.y) ** 2) <= self.range + tw.width // 2]

        for tw in in_range:
            tw.damage = tw.base_damage + round(tw.base_damage * self.damage_increase[self.level - 1])

# <-------------------------------------------- RANGE TOWER  -------------------------------------------------->
range_tower = [pygame.transform.scale(pygame.image.load(os.path.join("images/towers/support_towers/range_support_tower/", "1.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("images/towers/support_towers/range_support_tower/", "2.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("images/towers/support_towers/range_support_tower/", "3.png")), (80, 80))
               ]

class RangeTower(DamageTower):
    """
    Increase range of nearby towers in a circular radius
    """
    def __init__(self, name, coord):
        super().__init__(name, coord)
        self.tower_images = range_tower[:]
        self.increase = [0.2, 0.4, 0.6]

    def support(self, towers):
        """
        Increase nearby tower stats based on its support type (ranged vs damage)
        @param (LIST) towers: list of all attack towers (magic and archer)

        --> return: None
        """
        in_range = [tw for tw in towers if math.sqrt((self.x - tw.x) ** 2 + (self.y - tw.y) ** 2) <= self.range + tw.width // 2]

        for tw in in_range:
            tw.range = tw.base_range + round(tw.base_range * self.increase[self.level - 1])
        



    



    
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
    Increase damage of nearby towers
    """
    def __init__(self, name, coord):
        super().__init__(name, coord)
        self.tower_images = damage_tower[:]
        self.increase = [0.2, 0.4, "MAX"]

    def draw(self, window):
        super().draw_tower_radius(window)
        super().draw(window)

    def support(self, towers):
        """
        increase stats of nearby towers based on speciality
        @param towers: list
        :returns: None
        """
        in_range_towers = []
        for tw in towers:
            x, y = tw.x, tw.y
            dist = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dist <= self.range + tw.width / 2:
                in_range_towers.append(tw)

        for tw in in_range_towers:
            tw.damage = tw.base_damage + round(tw.base_damage * self.increase[self.level - 1])

# <-------------------------------------------- RANGE TOWER  -------------------------------------------------->
range_tower = [pygame.transform.scale(pygame.image.load(os.path.join("images/towers/support_towers/range_support_tower/", "1.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("images/towers/support_towers/range_support_tower/", "2.png")), (80, 80)),
               pygame.transform.scale(pygame.image.load(os.path.join("images/towers/support_towers/range_support_tower/", "3.png")), (80, 80))
               ]

class RangeTower(DamageTower):
    """
    Increase range of nearby towers
    """
    def __init__(self, name, coord):
        super().__init__(name, coord)
        self.tower_images = range_tower[:]
        self.increase = [0.2, 0.4, "MAX"]

    def support(self, towers):
        """
        increase stats of nearby towers based on speciality
        @param towers: list
        :returns: None
        """
        in_range_towers = []
        for tw in towers:
            x, y = tw.x, tw.y
            dist = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dist <= self.range + tw.width / 2:
                in_range_towers.append(tw)

        for tw in in_range_towers:
            tw.range = tw.base_range + round(tw.base_range * self.increase[self.level - 1])
        



    



    
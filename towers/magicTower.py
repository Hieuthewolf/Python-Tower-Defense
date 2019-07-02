from .tower import Tower
from usefulFunctions import import_images_numbers
import os
import pygame

# <-------------------------------------------- FIRE MAGIC TOWER  -------------------------------------------------->

fire_magic_tower = import_images_numbers("images/towers/magic_towers/fire/", 16, 19, (80, 80))

small_ball = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/fire", "small_ball.png")), (20, 20))

class FireMagicTower(Tower):
    def __init__(self, name, coord):
        super().__init__(name, coord)
        # Archer tower coordinates
        self.x = self.coord[0] 
        self.y = self.coord[1]

        self.tower_images = fire_magic_tower

        # Archer original stats
        self.base_range = self.range

        # Archer damage that gets updated
        self.base_damage = 3
        self.damage = self.base_damage

        self.enemy_in_range = False

    def draw(self, window):
        super().draw_tower_radius(window)
        super().draw(window)
  
        window.blit(small_ball, (self.x - small_ball.get_width() // 2 - 5,  self.y - self.dimensions[0] // 2))

    

    




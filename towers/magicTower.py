from .tower import Tower
from usefulFunctions import import_images_numbers, import_images_name
import math
import os
import pygame

# <-------------------------------------------- FIRE MAGIC TOWER  -------------------------------------------------->

fire_magic_tower = import_images_numbers("images/towers/magic_towers/fire/", 16, 19, (80, 90))

small_ball = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/fire", "small_ball.png")), (15, 15))
big_ball = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/fire", "big_ball.png")), (22, 22))
fire_spark = import_images_numbers("images/towers/magic_towers/fire/", 25, 27, (30, 35))
fire_flame = import_images_name("images/towers/magic_towers/fire", "1_effect_fire_0", 0, 19, (200, 250))

class FireTower(Tower):
    def __init__(self, name, coord):
        super().__init__(name, coord)
        self.x = self.coord[0] 
        self.y = self.coord[1]

        self.tower_images = fire_magic_tower

        # magic tower stats
        self.base_range = self.range
        self.base_damage = 3
        self.damage = self.base_damage
        self.area_of_effect = 150

        self.enemy_in_range = False

        # Animating tower attack
        self.fire_spark_images = fire_spark

        # Animating fire flame impact
        self.fire_flame_images = fire_flame
        self.fire_flame_count = 0
        self.aim_target = None

        self.locked = False
        
    def draw(self, window):
        super().draw(window)

        fire_flame = self.fire_flame_images[self.fire_flame_count // 4]

        if not self.level_up_animation:
            if self.level == 1:
                window.blit(small_ball, (self.x - small_ball.get_width() // 2 - 3,  self.y - self.dimensions[1] // 2 + small_ball.get_height() + 20))
                if self.enemy_in_range:
                    window.blit(self.fire_spark_images[1], (self.x - self.fire_spark_images[1].get_width() + 8,  self.y - self.dimensions[1] // 2 - small_ball.get_height() // 2 + 5))

            elif self.level == 2:
                window.blit(small_ball, (self.x - small_ball.get_width() // 2 - 3,  self.y - self.dimensions[1] // 2 + small_ball.get_height() + 15))
                if self.enemy_in_range:
                    window.blit(self.fire_spark_images[1], (self.x - self.fire_spark_images[1].get_width() + 8,  self.y - self.dimensions[1] // 2 - small_ball.get_height() // 2))

            else:
                window.blit(big_ball, (self.x - small_ball.get_width() // 2 - 7,  self.y - self.dimensions[1] // 2 + small_ball.get_height() + 27))
                if self.enemy_in_range:
                    window.blit(self.fire_spark_images[1], (self.x - self.fire_spark_images[1].get_width() + 8,  self.y - self.dimensions[1] // 2 - small_ball.get_height() // 2 + 10))

            if self.enemy_in_range:      
                window.blit(fire_flame, (self.aim_target.x - fire_flame.get_width() // 2 + 30 , self.aim_target.y - fire_flame.get_height() // 2 - 50))

    def attack(self, enemies, dead_enemies):
        """
        attacks enemy in enemy list, modifying the list
        :param enemies: list of enemies
        :return: None
        """
        current_enemies = enemies[:]

        self.enemy_in_range = False
        enemies_in_range = []

        for e in enemies:
            x, y = e.x, e.y

            dist = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dist <= self.range:
                self.enemy_in_range = True
                enemies_in_range.append(e)
        
        # Sorting by closest distance in a radial direction
        enemies_in_range.sort(key = lambda e: math.sqrt((self.x - e.x) ** 2 + (self.y - e.y) ** 2))
        
        total_loot = 0

        if enemies_in_range and not self.locked:
            self.aim_target = enemies_in_range[0]
            self.locked = True

        if self.locked and math.sqrt((self.x - self.aim_target.x) ** 2 + (self.y - self.aim_target.y) ** 2) <= self.range:
            self.fire_flame_count += 1
            if self.fire_flame_count >= len(self.fire_flame_images) * 4:
                self.fire_flame_count = 0

            #Decrements health bar of enemies only when the archer has finished its animation
            if self.fire_flame_count == 30:
                for e in current_enemies:
                    if math.sqrt((e.x - self.aim_target.x) ** 2 + (e.y - self.aim_target.y) ** 2) <= self.area_of_effect:
                        e.health -= self.damage

                        if e.health <= 0:
                            e.dead = True
                            dead_enemies.add(e)
                            enemies.remove(e)
                            total_loot += e.crystal_worth

                self.locked = False
        else:
            self.locked = False

        return total_loot



# <-------------------------------------------- ICE MAGIC TOWER  -------------------------------------------------->
ice_magic_tower = import_images_numbers("images/towers/magic_towers/ice/", 11, 14, (80, 80))

small_swiggle = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/ice", "swiggle.png")), (25, 25))
spike = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/ice", "spike.png")), (10, 30))
small_spike = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/ice", "spike.png")), (10, 20))

ice_spark = import_images_numbers("images/towers/magic_towers/ice/", 23, 25, (30, 35))
ice_freeze = import_images_name("images/towers/magic_towers/ice", "1_effect_freeze_0", 0, 16, (200, 200))

class IceTower(Tower):
    def __init__(self, name, coord):
        super().__init__(name, coord)
        self.x = self.coord[0] 
        self.y = self.coord[1]

        self.ice_spark_images = ice_spark
        self.tower_images = ice_magic_tower

        # Animating fire flame impact
        self.ice_freeze_images = ice_freeze
        self.ice_freeze_count = 0

        self.base_range = self.range
        self.base_damage = 1
        self.damage = self.base_damage
        self.area_of_effect = 150

        self.aim_target = None
        self.enemy_in_range = None
        self.locked = False

        self.horizontal_padding = 7
        self.vertical_padding = 15

    def draw(self, window):
        super().draw(window)

        ice_freeze = self.ice_freeze_images[self.ice_freeze_count // 4]

        if not self.level_up_animation:
            # Each level looks differently via pixels

            if self.level == 1:
                window.blit(small_swiggle, (self.x - small_swiggle.get_width() // 2 - self.horizontal_padding,  self.y - self.dimensions[1] // 2 + small_swiggle.get_height() + self.vertical_padding))

            elif self.level == 2:
                window.blit(small_swiggle, (self.x - small_swiggle.get_width() // 2 - self.horizontal_padding,  self.y - self.dimensions[1] // 2 + small_swiggle.get_height() + self.vertical_padding / 3 - 2))
                
            elif self.level == 3:
                # Main spike on top of tower
                window.blit(spike, (self.x - small_swiggle.get_width() // 2 + 4,  self.y - self.dimensions[1] // 2 + small_swiggle.get_height() + self.vertical_padding / 3 - 4))
                
                # 4 small spikes on the 4 "quadrants"
                window.blit(small_spike, (self.x + 8,  self.y - self.dimensions[1] // 2 + 35)) #Top-right spike
                window.blit(small_spike, (self.x - 23,  self.y - self.dimensions[1] // 2 + 35)) #Top-left spike
                window.blit(small_spike, (self.x + 10,  self.y - self.dimensions[1] // 2 + 55)) #Bottom-right spike
                window.blit(small_spike, (self.x - 25,  self.y - self.dimensions[1] // 2 + 55)) #Bottom-left spike     

            if self.enemy_in_range:
                if self.level == 2 or self.level == 3:
                    window.blit(self.ice_spark_images[1], (self.x - self.ice_spark_images[1].get_width() + self.horizontal_padding,  self.y - self.dimensions[1] // 2 - 10))
                else:
                    window.blit(self.ice_spark_images[1], (self.x - self.ice_spark_images[1].get_width() + self.horizontal_padding,  self.y - self.dimensions[1] // 2))

                window.blit(ice_freeze, (self.aim_target.x - ice_freeze.get_width() // 2 + 30 , self.aim_target.y - ice_freeze.get_height() // 2 - 50))

    def attack(self, enemies, dead_enemies):
        """
        attacks enemy in enemy list, modifying the list
        :param enemies: list of enemies
        :return: None
        """
        current_enemies = enemies[:]

        self.enemy_in_range = False
        enemies_in_range = []

        for e in enemies:
            x, y = e.x, e.y

            dist = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dist <= self.range:
                self.enemy_in_range = True
                enemies_in_range.append(e)
        
        # Sorting by closest distance in a radial direction
        enemies_in_range.sort(key = lambda e: math.sqrt((self.x - e.x) ** 2 + (self.y - e.y) ** 2))
        
        if enemies_in_range and not self.locked:
            self.aim_target = enemies_in_range[0]
            self.locked = True

        if self.locked and math.sqrt((self.x - self.aim_target.x) ** 2 + (self.y - self.aim_target.y) ** 2) <= self.range:
            self.ice_freeze_count += 1
            if self.ice_freeze_count >= len(self.ice_freeze_images) * 4:
                self.ice_freeze_count = 0

            #Decrements health bar of enemies only when the archer has finished its animation
            if self.ice_freeze_count == 30:
                for e in current_enemies:
                    if math.sqrt(((e.x - self.aim_target.x) ** 2 + (e.y - self.aim_target.y) ** 2)) <= self.area_of_effect:
                        e.move_speed = 1

                self.locked = False
        else:
            self.locked = False
            self.aim_target = None

        return 0




    


    

    

    

    




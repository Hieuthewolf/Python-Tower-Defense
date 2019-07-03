from .tower import Tower
from usefulFunctions import import_images_numbers, import_images_name
import math
import os
import pygame

# <-------------------------------------------- FIRE MAGIC TOWER  -------------------------------------------------->

fire_magic_tower = import_images_numbers("images/towers/magic_towers/fire/", 16, 19, (80, 80))

small_ball = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/fire", "small_ball.png")), (25, 25))
fire_spark = import_images_numbers("images/towers/magic_towers/fire/", 25, 27, (40, 40))
fire_flame = import_images_name("images/towers/magic_towers/fire", "1_effect_fire_0", 0, 19, (200, 200))

class FireTower(Tower):
    def __init__(self, name, coord):
        super().__init__(name, coord)
        # Archer tower coordinates
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
        super().draw_tower_radius(window)
        super().draw(window)

        fire_flame = self.fire_flame_images[self.fire_flame_count // 4]

        window.blit(small_ball, (self.x - small_ball.get_width() // 2 - 5,  self.y - self.dimensions[1] // 2))

        if not self.enemy_in_range:
            window.blit(self.fire_spark_images[0], (self.x - self.fire_spark_images[0].get_width() + 10,  self.y - self.dimensions[1] // 2 - self.fire_spark_images[0].get_height() // 2 - small_ball.get_height() // 2 - 10))
        else:
            window.blit(self.fire_spark_images[1], (self.x - self.fire_spark_images[1].get_width() + 10,  self.y - self.dimensions[1] // 2 - self.fire_spark_images[0].get_height() // 2 - small_ball.get_height() // 2 - 10))
            window.blit(fire_flame, (self.aim_target.x - fire_flame.get_width() // 2 + 30 , self.aim_target.y - fire_flame.get_height() // 2 - 30))

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
        enemies_in_range.sort(key = lambda e: math.sqrt((self.x - e.x) ** 2 + (self.y - y) ** 2))
        
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
                    if math.sqrt(((e.x - self.aim_target.x) ** 2 + (e.y - self.aim_target.y) ** 2)) <= self.area_of_effect:
                        e.health -= self.damage

                        if e.health <= 0:
                            e.dead = True
                            dead_enemies.add(e)
                            enemies.remove(e)
                            total_loot += e.crystal_worth

            self.locked = False

        return total_loot


    

    

    

    




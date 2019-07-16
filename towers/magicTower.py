from .tower import Tower
from usefulFunctions import import_images_numbers, import_images_name, calculate_distance
import math
import os
import pygame

# <-------------------------------------------- FIRE MAGIC TOWER  -------------------------------------------------->

fire_magic_tower = import_images_numbers("images/towers/magic_towers/fire/", 16, 19, (80, 90))

small_ball = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/fire", "small_ball.png")), (15, 15))
big_ball = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/fire", "big_ball.png")), (22, 22))
fire_spark = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/fire", "26.png")), (30, 35))
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

        # Toggle to determine if enemies are in range
        self.enemy_in_range = False

        # Appears over target's head to show the target that the tower is targeting
        self.fire_spark = fire_spark

        # Animating fire flame impact
        self.fire_flame_images = fire_flame
        self.fire_flame_count = 0
        self.aim_target = None

        # For locking fire animation on an aim target as long as the aim target is still in range
        self.locked = False
        
    def draw(self, window):
        """
        Draws magic towers as based on their specific level and animate the attack animation to sync up with enemies
        @param (SURFACE) window: surface for rendering the drawing

        --> return: None
        """

        super().draw(window)

        fire_flame = self.fire_flame_images[self.fire_flame_count // 4]

        if not self.level_up_animation:
            if self.level == 1:
                window.blit(small_ball, (self.x - small_ball.get_width() // 2 - 3,  self.y - self.dimensions[1] // 2 + small_ball.get_height() // 2 - 5))                    
            elif self.level == 2:
                window.blit(small_ball, (self.x - small_ball.get_width() // 2 - 3,  self.y - self.dimensions[1] // 2 + small_ball.get_height() // 2 - 10))
            else:
                window.blit(big_ball, (self.x - small_ball.get_width() // 2 - 7,  self.y - self.dimensions[1] // 2 + big_ball.get_height() // 2))


            if self.enemy_in_range:      
                window.blit(self.fire_spark, (self.aim_target.x - 20,  self.aim_target.y  - fire_spark.get_height() - self.aim_target.height // 2 - 20))
                window.blit(fire_flame, (self.aim_target.x - fire_flame.get_width() // 2 + 30 , self.aim_target.y - fire_flame.get_height() // 2 - 50))

    def attack(self, enemies, dead_enemies):
        """
        Attacks enemies in enemy list and modifies it and adds the enemies to dead_enemies list if they die
        Also syncs up the animation of the projectiles to that of the depletion of HP due to fireball

        @param (LIST) enemies: list of current enemies on the field
        @Param (SET) dead_enemies: set of dead enemies after going down to 0 hp

        --> return: Int (money currency)
        """
        current_enemies = enemies[:]
        enemies_in_range = [e for e in enemies if calculate_distance(self, e) <= self.range]
        self.enemy_in_range = True if enemies_in_range else False
        
        # Sorting by closest distance in a radial direction
        enemies_in_range.sort(key = lambda e: calculate_distance(self, e))
        
        total_loot = 0

        if enemies_in_range and not self.locked:
            self.aim_target = enemies_in_range[0]
            self.locked = True

        if self.locked and calculate_distance(self, self.aim_target) <= self.range:
            self.fire_flame_count += 1
            if self.fire_flame_count >= len(self.fire_flame_images) * 4:
                self.fire_flame_count = 0

            #Decrements health bar of enemies only when the archer has finished its animation
            if self.fire_flame_count == 30:
                for e in current_enemies:
                    if calculate_distance(e, self.aim_target) <= self.area_of_effect:
                        e.health -= self.damage

                        if e.health <= 0:
                            self.kill_count += 1
                            e.dead = True
                            dead_enemies.add(e)
                            enemies.remove(e)
                            total_loot += e.crystal_worth

                self.locked = False
        else:
            self.locked = False
            self.aim_target = None

        return total_loot


# <-------------------------------------------- ICE MAGIC TOWER  -------------------------------------------------->
ice_magic_tower = import_images_numbers("images/towers/magic_towers/ice/", 11, 14, (80, 80))

small_swiggle = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/ice", "swiggle.png")), (25, 25))
spike = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/ice", "spike.png")), (10, 30))
small_spike = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/ice", "spike.png")), (10, 20))
ice_spark = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/ice", "24.png")), (30, 35))
ice_freeze = import_images_name("images/towers/magic_towers/ice", "1_effect_freeze_0", 0, 16, (200, 200))

class IceTower(Tower):
    def __init__(self, name, coord):
        super().__init__(name, coord)
        self.x = self.coord[0] 
        self.y = self.coord[1]

        self.ice_spark=  ice_spark
        self.tower_images = ice_magic_tower

        # Animating fire flame impact
        self.ice_freeze_images = ice_freeze
        self.ice_freeze_count = 0

        self.base_range = self.range
        self.base_damage = 1
        self.damage = self.base_damage
        self.area_of_effect = 150

        self.aim_target = None
        self.enemy_in_range = False
        self.locked = False

    def draw(self, window):
        """
        Draws magic towers as based on their specific level and animate the attack animation to sync up with enemies
        @param (SURFACE) window: surface for rendering the drawing

        --> return: None
        """

        super().draw(window)

        ice_freeze = self.ice_freeze_images[self.ice_freeze_count // 4]

        if not self.level_up_animation:
            # Blits the swiggle in a different position based on tower level
            if self.level == 1:
                window.blit(small_swiggle, (self.x - small_swiggle.get_width() // 2 - 7,  self.y - self.dimensions[1] // 2 + small_swiggle.get_height() // 2 - 5))

            elif self.level == 2:
                window.blit(small_swiggle, (self.x - small_swiggle.get_width() // 2 - 7,  self.y - self.dimensions[1] // 2 + small_swiggle.get_height() // 2 - 15))
                
            elif self.level == 3:
                # Main spike on top of tower
                window.blit(spike, (self.x - small_swiggle.get_width() // 2 + 4,  self.y - self.dimensions[1] // 2 + small_swiggle.get_height() // 2 - 20))
                
                # 4 small spikes on the 4 "quadrants"
                window.blit(small_spike, (self.x + 8,  self.y - self.dimensions[1] // 2 + 5)) #Top-right spike
                window.blit(small_spike, (self.x - 23,  self.y - self.dimensions[1] // 2 + 5)) #Top-left spike
                window.blit(small_spike, (self.x + 10,  self.y - self.dimensions[1] // 2 + 22)) #Bottom-right spike
                window.blit(small_spike, (self.x - 25,  self.y - self.dimensions[1] // 2 + 22)) #Bottom-left spike     

            if self.aim_target:
                window.blit(self.ice_spark, (self.aim_target.x - 20,  self.aim_target.y  - ice_spark.get_height() - self.aim_target.height // 2 - 20))
                window.blit(ice_freeze, (self.aim_target.x - ice_freeze.get_width() // 2 + 30 , self.aim_target.y - ice_freeze.get_height() // 2 - 50))

    def attack(self, enemies, dead_enemies):
        """
        Attacks enemies in enemy list and modifies it and adds the enemies to dead_enemies list if they die
        Also syncs up the animation of the projectiles to that of the slowing effect of ice towers

        @param (LIST) enemies: list of current enemies on the field
        @Param (SET) dead_enemies: set of dead enemies after going down to 0 hp

        --> return: Int (money currency)
        """
        current_enemies = enemies[:]
        enemies_in_range = [e for e in enemies if calculate_distance(self, e) <= self.range]
        self.enemy_in_range = True if enemies_in_range else False
        
        # Sorting by closest distance in a radial direction
        enemies_in_range.sort(key = lambda e: calculate_distance(self, e))
        
        if enemies_in_range and not self.locked:
            self.aim_target = enemies_in_range[0]
            self.locked = True

        if self.locked and calculate_distance(self, self.aim_target) <= self.range:
            self.ice_freeze_count += 1
            if self.ice_freeze_count >= len(self.ice_freeze_images) * 4:
                self.ice_freeze_count = 0

            #Decrements health bar of enemies only when the archer has finished its animation
            if self.ice_freeze_count == 30:
                for e in current_enemies:
                    if calculate_distance(e, self.aim_target) <= self.area_of_effect:
                        e.move_speed = 1

                self.locked = False
        else:
            self.locked = False
            self.aim_target = None

        return 0




    


    

    

    

    




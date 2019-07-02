from .tower import Tower
from usefulFunctions import import_images_numbers
import os
import pygame

# <-------------------------------------------- FIRE MAGIC TOWER  -------------------------------------------------->

fire_magic_tower = import_images_numbers("images/towers/magic_towers/fire/", 16, 19, (80, 80))

small_ball = pygame.transform.scale(pygame.image.load(os.path.join("images/towers/magic_towers/fire", "small_ball.png")), (25, 25))
fire_spark = import_images_numbers("images/towers/magic_towers/fire/", 25, 27, (40, 80))
# fire_animation = 

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
        self.area_of_effect = 50

        self.enemy_in_range = False

        # Animating tower attack
        self.fire_spark_images = fire_spark
        self.fire_spark_count= 0
        
    def draw(self, window):
        super().draw_tower_radius(window)
        super().draw(window)

        fire_spark = self.fire_spark_images[self.fire_spark_count // 10] 

        window.blit(small_ball, (self.x - small_ball.get_width() // 2 - 5,  self.y - self.dimensions[1] // 2))
        window.blit(fire_spark, (self.x - small_ball.get_width() // 2 - 50,  self.y - self.dimensions[1] // 2 - 50))

    def attack(self, enemies, dead_enemies):
        """
        attacks enemy in enemy list, modifying the list
        :param enemies: list of enemies
        :return: None
        """
        self.enemy_in_range = False
        closest_enemies = []
        for e in enemies:
            x, y = e.x, e.y

            dist = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dist < self.range:
                self.enemy_in_range = True
                closest_enemies.append(e)

        if self.enemy_in_range and not self.being_dragged:  #Updating the blit image for the archers if enemies are in range
            self.archer_count += 1
            if self.archer_count >= len(self.archer_images) * 3: 
                self.archer_count = 0
        else:
            self.archer_count = 0
        
        # Sorting by horizontal distance so the archer tower knows what direction to face 
        closest_enemies.sort(key = lambda e: (self.x - e.x) ** 2 + (self.y - y) ** 2)
        
        if closest_enemies:
            target = closest_enemies[0]

            #Decrements health bar of enemies only when the archer has finished its animation
            if self.archer_count == 12: 
                target.health -= self.damage

            if target.health <= 0:
                self.last_arrow_animation_count += 1
                if self.last_arrow_animation_count >= 4:
                    target.dead = True
                    dead_enemies.add(target)
                    enemies.remove(target)

                    self.last_arrow_animation_count = 0
                    return target.crystal_worth

            if not self.flipped and self.x > target.x:
                self.flipped = True
                for i, image in enumerate(self.archer_images):
                    self.archer_images[i] = pygame.transform.flip(image, True, False)
        
            elif self.flipped and self.x < target.x:
                self.flipped = False
                for i, image in enumerate(self.archer_images):
                    self.archer_images[i] = pygame.transform.flip(image, True, False)

        return 0


    

    

    

    




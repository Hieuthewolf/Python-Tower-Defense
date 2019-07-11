import pygame
from .tower import Tower
import os
import math
from usefulFunctions import import_images_numbers, calculate_distance

# <-------------------------------------------- ARCHER TOWER FAR  -------------------------------------------------->

# Archer tower images
archer_tower_far = import_images_numbers("images/towers/archer_towers/archer_1/", 7, 10, (80, 80))

# Archers images
archers_far = import_images_numbers("images/towers/archer_towers/archer_top_1/", 37, 43)

class ArcherTowerFar(Tower):
    def __init__(self, name, coord):
        super().__init__(name, coord)
        self.archer_images = []
        self.archer_count = 0

        # Archer tower coordinates
        self.x = self.coord[0] 
        self.y = self.coord[1]

        # Flipping archer image to face direction of enemies
        self.flipped = False

        # Loading tower and archer images
        self.tower_images = archer_tower_far[:]
        self.archer_images = archers_far[:]

        # Archer original stats
        self.base_range = self.range

        # Archer damage that gets updated
        self.base_damage = 3
        self.damage = self.base_damage

        # Counter to sync up the last arrow with the monster dying
        self.last_arrow_animation_count = 0

        self.enemy_in_range = False
        self.arrow_hit_target = (None, None)

    def draw(self, window):
        """
        Draws archers on top of archer towers and the tower itself
        @param (SURFACE) window: surface for rendering the drawing

        --> return: None
        """
        super().draw(window)

        if not self.level_up_animation:
            archer = self.archer_images[self.archer_count // 3] 

            #Padding so that the archer stays static when switching directions
            if not self.flipped:
                padding = -25
            else:
                padding = - archer.get_width() + 15

            window.blit(archer, ((self.x + padding + 5), (self.y - archer.get_height() - 25)))
            
    def attack(self, enemies, dead_enemies):
        """
        Attacks enemies in enemy list and modifies it and adds the enemies to dead_enemies list if they die
        Also syncs up the animation of the archers to that of the depletion of enemy HP
        Lastly, syncs up the direction that the archers face based on which side the enemies are on 

        @param (LIST) enemies: list of current enemies on the field
        @Param (SET) dead_enemies: set of dead enemies after going down to 0 hp

        --> return: Int (money currency)
        """
        enemies_in_range = [e for e in enemies if calculate_distance(self, e) <= self.range]
        self.enemy_in_range = True if enemies_in_range else False

        if self.enemy_in_range and not self.being_dragged:  #Updating the blit image for the archers if enemies are in range
            self.archer_count += 1
            if self.archer_count >= len(self.archer_images) * 3: 
                self.archer_count = 0
        else:
            self.archer_count = 0
        
        # Sorting by horizontal distance so the archer tower knows what direction to face 
        enemies_in_range.sort(key = lambda e: calculate_distance(self, e))

        if enemies_in_range:
            target = enemies_in_range[0]

            #Decrements health bar of enemies only when the archer has finished its animation
            if self.archer_count == 12: 
                target.health -= self.damage

            if target.health <= 0:
                self.last_arrow_animation_count += 1
                if self.last_arrow_animation_count >= 2:
                    self.kill_count += 1
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


# <-------------------------------------------- ARCHER TOWER SHORT -------------------------------------------------->

# Archer tower images
archer_tower_short = import_images_numbers("images/towers/archer_towers/archer_2/", 10, 13, (80, 80))

# Archers images
archers_short = import_images_numbers("images/towers/archer_towers/archer_top_2/", 43, 49)

class ArcherTowerShort(ArcherTowerFar):
    """
    Inherits from ArcherTowerFar because the only attributes that change are the tower images, archer images, damage, and range
    """
    def __init__(self, name, coord):
        super().__init__(name, coord)
        # Loading tower and archer images
        self.tower_images = archer_tower_short[:]
        self.archer_images = archers_short[:]

        # Damage
        self.base_damage = 5
        self.damage = self.base_damage








        


    

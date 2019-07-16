from objectFormation import GameObjects
from constants import GameConstants, EnemyConstants
from usefulFunctions import calculate_distance
import pygame
import math
import random

class Enemy(GameObjects):
    def __init__(self, name, map_label):
        super().__init__(name, GameConstants.PATH[map_label][0][0])
        # Each enemy has access to the game path
        if len(GameConstants.PATH[map_label]) == 2: #Length of 2 means two possible routes
            self.path = GameConstants.PATH[map_label][random.randint(0, 1)]
        else:
            self.path = GameConstants.PATH[map_label][0] #Only one direct path to exit

        # Enemy coordinates
        self.x = self.coord[0]
        self.y = self.coord[1]

        # Enemy characteristics
        self.currentPathPos = 0
        
        # Animating/Modifying appearance of enemies
        self.images = EnemyConstants.ENEMY_MOVING_SPRITE_IMAGES[name][:]
        self.animation_count = 0
        self.image = None #The current image that's being shown at a specific time frame

        # Health
        self.max_health = EnemyConstants.HEALTH[name]
        self.health = self.max_health

        # Enemy crystal worth
        self.crystal_worth = EnemyConstants.ENEMY_CRYSTALS[name]

        # Death animation
        self.death = EnemyConstants.ENEMY_DEATH_SPRITE_IMAGES[name][:]
        self.death_animation_count = 0
        self.dead = False

        # Additional constants to slow down move or death animation
        if name in EnemyConstants.MONSTER_NAMES:
            # Higher means it will take longer to go through the images
            self.slow_down_move_animation = EnemyConstants.SLOW_ENEMY_MOVE_ANIMATION_BUFFER['monster'] #For monsters
            self.slow_down_death_animation = EnemyConstants.SLOW_ENEMY_DEATH_ANIMATION_BUFFER['monster']
        else:
            self.slow_down_move_animation = EnemyConstants.SLOW_ENEMY_MOVE_ANIMATION_BUFFER[name] # For bosses
            self.slow_down_death_animation = EnemyConstants.SLOW_ENEMY_DEATH_ANIMATION_BUFFER[name]

        # Flips the images based on the unit_vector they're facing
        self.flipped = False
        self.alter_image = None
    
        # For freezing logistics
        self.affected = False
        self.default_move_speed = 3
        self.move_speed = self.default_move_speed
        
    def die(self, window):
        if self.dead:
            window.blit(self.death[self.death_animation_count // self.slow_down_death_animation], (self.x - self.image.get_width() / 2 + 15, (self.y - (self.image.get_height() / 2) - 10)))
            self.death_animation_count += 1
            if self.death_animation_count == len(self.death) * self.slow_down_death_animation:
                self.dead = False
                self.death_animation_count = 0

    def move(self):
        """
        Moves our enemy along the path while also accounting for the unit_vectors that enemies face
        Will return true if the next coordinate is a valid coordinate in the path and false if the enemy is beyond the path goal
        :return: booleans
        """ 
        self.animation_count += 1
        if self.animation_count >= len(self.images) * self.slow_down_move_animation:
            self.animation_count = 0
        
        x1, y1 = self.path[self.currentPathPos]
        if self.currentPathPos + 1 >= len(self.path):
            return False
        else:
            x2, y2 = self.path[self.currentPathPos + 1]


        vector = ((x2 - x1), (y2 - y1))
        length = calculate_distance((x1, y1), (x2, y2))
        unit_vector = (self.move_speed * vector[0] / length, self.move_speed * vector[1] / length) #Determines direction as well

        move_x, move_y = ((self.x + unit_vector[0]), (self.y + unit_vector[1]))

        if unit_vector[0] < 0 and not self.flipped:
            self.flipped = True
            for x, img in enumerate(self.images):
                self.images[x] = pygame.transform.flip(img, True, False) #Flips moving sprite animations
            for x, img in enumerate(self.death): 
                self.death[x] = pygame.transform.flip(img, True, False) #Flips death sprite animations
        
        elif unit_vector[0] >= 0 and self.flipped:
            self.flipped = False
            for x, img in enumerate(self.images):
                self.images[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.death):
                self.death[x] = pygame.transform.flip(img, True, False)

        self.x = move_x
        self.y = move_y

        moving_up = (unit_vector[1] <= 0)
        moving_right = (unit_vector[0] > 0)
        no_delta_x = (unit_vector[0] == 0)

        if moving_right:
            if moving_up:
                if self.x >= x2:
                    self.currentPathPos += 1   
            else: #moving down
                if self.x >= x2:
                    self.currentPathPos += 1

        # Constantly moving up or down in a vertical line with no delta in x coordinate
        elif no_delta_x:
            if moving_up:
                if self.y  <= y2:
                    self.currentPathPos += 1
            else:
                if self.y >= y2:
                    self.currentPathPos += 1

        else:
            if moving_up:
                if self.x <= x2:
                    self.currentPathPos += 1
            else: #moving down
                if self.x <= x2:
                    self.currentPathPos += 1

        return True


    def draw(self, window):
        """
        Using our list of images, draws the enemy
        :param window: surface
        :return: None
        """
        self.image = self.images[self.animation_count // self.slow_down_move_animation]

        window.blit(self.image, (self.x - self.image.get_width() / 2 + 15, (self.y - (self.image.get_height() / 2) - 10)))

        self.health_bar(window)

    def health_bar(self, window):
        """
        Making the health bar 
        :param window: surface
        :return: None
        """
        length = 60
        each_section = length / self.max_health

        if self.health > 0:
            res = each_section * self.health
        else:
            self.health = 0
            res = 0

        pygame.draw.rect(window, (255, 0, 0), (self.x - 30, self.y - 50, length, 10), 0)
        
        if res:
            pygame.draw.rect(window, (0, 255, 0), (self.x - 30, self.y - 50, res, 10), 0)
    
    def update_speed_status(self, ice_towers):
        """
        Updates the current speed of the enemy if it is no longer under the effect of ice towers
        """
        not_affected = True
        for t in ice_towers:
            if t.aim_target:
                if calculate_distance(self, t.aim_target) <= t.area_of_effect:
                    not_affected = False
                    break

        if not_affected:
            self.move_speed = self.default_move_speed

class BossEnemy(Enemy):
    def __init__(self, name, map_label):
        super().__init__(name, map_label)
        self.flipped = True #Flips the enemy if not facing the correct unit_vector

    def health_bar(self, window):
        """
        Making the health bar 
        :param window: surface
        :return: None
        """
        length = 100
        each_section = length / self.max_health

        if self.health > 0:
            res = each_section * self.health
        else:
            self.health = 0
            res = 0

        pygame.draw.rect(window, (255, 0, 0), (self.x - 40, self.y - 75, length, 20), 0)
        
        if res:
            pygame.draw.rect(window, (0, 255, 0), (self.x - 40, self.y - 75, res, 20), 0)








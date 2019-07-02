from objectFormation import GameObjects
from constants import GameConstants, EnemyConstants, EnemyImagesConstants
# from usefulFunctions import createPathLayout
import pygame
import math

class Enemy(GameObjects):
    def __init__(self, name):
        super().__init__(name, GameConstants.PATH[0])
        # Each enemy has access to the game path
        # self.path = createPathLayout(Constants.PATH_CORNERS)
        self.path = GameConstants.PATH

        # Enemy coordinates
        self.x = self.coord[0]
        self.y = self.coord[1]

        # Enemy characteristics
        self.currentPathPos = 0
        # self.velocity = Constants.ENEMY_SPEED[name]
        
        # Animating/Modifying appearance of enemies
        self.images = EnemyImagesConstants.ENEMY_MOVING_SPRITE_IMAGES[name][:]
        self.animation_count = 0
        self.image = None #The current image that's being shown at a specific time frame

        # Health
        self.max_health = EnemyConstants.HEALTH[name]
        self.health = self.max_health

        # Enemy crystal worth
        self.crystal_worth = EnemyConstants.ENEMY_CRYSTALS[name]

        # Death animation
        self.death = EnemyImagesConstants.ENEMY_DEATH_SPRITE_IMAGES[name][:]
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

        # Flips the images based on the direction they're facing
        self.flipped = False
        
    def die(self, window):
        if self.dead:
            window.blit(self.death[self.death_animation_count // self.slow_down_death_animation], (self.x - self.image.get_width() / 2 + 15, (self.y - (self.image.get_height() / 2) - 10)))
            self.death_animation_count += 1
            if self.death_animation_count == len(self.death) * self.slow_down_death_animation:
                self.dead = False
                self.death_animation_count = 0


    def move(self):
        """
        Moves our enemy along the path while also accounting for the directions that enemies face
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
        length = math.sqrt((vector[0]) ** 2 + (vector[1]) ** 2)
        direction = (2 * vector[0] / length,  2 * vector[1] / length)

        if direction[0] < 0 and not self.flipped:
            self.flipped = True
            for x, img in enumerate(self.images):
                self.images[x] = pygame.transform.flip(img, True, False) #Flips moving sprite animations
            for x, img in enumerate(self.death): 
                self.death[x] = pygame.transform.flip(img, True, False) #Flips death sprite animations
        
        elif direction[0] >= 0 and self.flipped:
            self.flipped = False
            for x, img in enumerate(self.images):
                self.images[x] = pygame.transform.flip(img, True, False)
            for x, img in enumerate(self.death):
                self.death[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = ((self.x + direction[0]), (self.y + direction[1]))

        self.x = move_x
        self.y = move_y

        moving_up = (direction[1] <= 0)
        moving_right = (direction[0] >= 0)

        if moving_right:
            if moving_up:
                if self.x >= x2 and self.y <= y2:
                    self.currentPathPos += 1
            else: #moving down
                if self.x >= x2 and self.y >= y2:
                    self.currentPathPos += 1

        else:
            if moving_up:
                if self.x <= x2 and self.y <= y2:
                    self.currentPathPos += 1
            else: #moving down
                if self.x <= x2 and self.y >= y2:
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

class BossEnemy(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.flipped = True #Flips the enemy if not facing the correct direction

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








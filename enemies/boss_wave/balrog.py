import pygame
import os
from enemies.enemy import BossEnemy
from usefulFunctions import import_images_name

images = import_images_name("images/enemies/boss/balrog", "move_0", 1, 6, (150, 150))
death = import_images_name("images/enemies/boss/balrog", "die_0", 1, 3, (150, 150))


class Balrog(BossEnemy):
    def __init__(self, name):
        super().__init__(name)
        self.images = images[:]
        self.death = death[:]
        for x, img in enumerate(self.death):
            self.death[x] = pygame.transform.flip(img, True, False)
        self.death_animation_count = 0
        self.dead = False

    def die(self, window):
        if self.dead:
            window.blit(self.death[self.death_animation_count // 15], (self.x - self.image.get_width() / 2 + 15, (self.y - (self.image.get_height() / 2) - 10)))
            self.death_animation_count += 1
            if self.death_animation_count == len(self.death) * 15:
                self.dead = False
                self.death_animation_count = 0

    def draw(self, window):
        """
        Using our list of images, draws the enemy
        :param window: surface
        :return: None
        """
        self.image = self.images[self.animation_count // 5]
        self.animation_count += 1

        if self.animation_count >= len(self.images) * 5:
            self.animation_count = 0

        window.blit(self.image, (self.x - self.image.get_width() / 2 + 15, (self.y - (self.image.get_height() / 2) - 10)))

        self.health_bar(window)
        self.move()



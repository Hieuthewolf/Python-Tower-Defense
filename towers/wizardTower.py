import pygame
from .tower import Tower

class WizardTower(Tower):
    def __init__(self, name, coord):
        super().__init__(name, coord):
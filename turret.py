import pygame
from const import *


class TurretBase:
    def __init__(self, screen, name, pos, row, col):
        self.screen = screen
        self.name = name
        self.row = row
        self.col = col
        self.pos = pos
        self.image = pygame.image.load(TURRET_IMAGE[name])

    def draw(self):
        self.screen.blit(self.image, self.pos)

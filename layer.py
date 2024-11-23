import pygame
from const import *


class Layer:
    def __init__(self, screen, name, grid_size, offset):
        self.screen = screen
        self.name = name
        self.grid_size = grid_size
        self.offset = offset

    def draw(self):
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                pygame.draw.rect(self.screen, LIGHT_GREEN,
                                 (self.offset[0] + i * TILE_SIZE, self.offset[1] + j * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, BLACK,
                                 (self.offset[0] + i * TILE_SIZE, self.offset[1] + j * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

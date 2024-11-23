import pygame
from const import *


class Layer:
    def __init__(self, screen, name, grid_size, wall_width):
        self.screen = screen
        self.name = name
        self.grid_size = grid_size
        self.wall_width = wall_width

    def draw(self):
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                pygame.draw.rect(self.screen, LIGHT_GREEN,
                                 (self.wall_width + i * TILE_SIZE, self.wall_width + j * TILE_SIZE,
                                  TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, BLACK,
                                 (self.wall_width + i * TILE_SIZE, self.wall_width + j * TILE_SIZE,
                                  TILE_SIZE, TILE_SIZE), 1)

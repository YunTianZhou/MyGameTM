import pygame
from const import *


class Layer:
    def __init__(self, screen, name, grid_size, wall_width):
        self.screen = screen
        self.name = name
        self.grid_size = grid_size
        self.wall_width = wall_width

    def draw(self):
        grid_width = self.grid_size[0] * TILE_SIZE + 2 * self.wall_width
        grid_height = self.grid_size[1] * TILE_SIZE + 2 * self.wall_width
        pygame.draw.rect(self.screen,BROWN,(0, 0, self.wall_width, grid_height))
        pygame.draw.rect(self.screen,BROWN,(0, 0, grid_width, self.wall_width))
        pygame.draw.rect(self.screen,BROWN,(grid_width - self.wall_width, 0, self.wall_width, grid_height))
        pygame.draw.rect(self.screen,BROWN,(0, grid_height - self.wall_width, grid_width, self.wall_width))

        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                pygame.draw.rect(self.screen, LIGHT_GREEN,
                                 (self.wall_width + i * TILE_SIZE, self.wall_width + j * TILE_SIZE,
                                  TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, BLACK,
                                 (self.wall_width + i * TILE_SIZE, self.wall_width + j * TILE_SIZE,
                                  TILE_SIZE, TILE_SIZE), 1)


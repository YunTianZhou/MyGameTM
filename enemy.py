import pygame
import random
from const import *


class EnemyBase:
    def __init__(self, screen, name, layer, pos, grid_size):
        self.screen = screen
        self.name = name
        self.layer = layer
        self.pos = pos
        self.image = pygame.image.load(ENEMY_IMAGE[name])
        self.path = [(grid_size[1], 0)]

        while self.path[-1][0] > 0 and self.path[-1][1] < grid_size[0] - 1:
            if random.randint(0, 1) == 0:
                self.path.append((self.path[-1][0] - 1, self.path[-1][1]))
            else:
                self.path.append((self.path[-1][0], self.path[-1][1] + 1))

        while self.path[-1][0] > 0:
            self.path.append((self.path[-1][0] - 1, self.path[-1][1]))

        while self.path[-1][1] < grid_size[0] - 1:
            self.path.append((self.path[-1][0], self.path[-1][1] + 1))

        self.path = list(reversed(self.path))

    def update(self):
        ox, oy = self.path.pop(-1)
        step = ENEMY_SPEED // TILE_SIZE
        for _ in range(TILE_SIZE // ENEMY_SPEED):
            self.pos = (self.pos[0] + ox * step, self.pos[1])

    def draw(self):
        self.screen.blit(self.image, self.pos)

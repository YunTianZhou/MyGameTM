import pygame
from const import *
from card import Card
from turret import TurretBase

LAYER_COLORS = {
    "forecourt": ((34, 139, 34), (144, 238, 144)),  # dark_green, light_green
    "floor1": ((105, 105, 105), (169, 169, 169)),   # dark_gray, light_gray
    "passage": ((160, 82, 45), (222, 184, 135)),    # saddle_brown, burlywood
    "floor2": ((70, 130, 180), (176, 196, 222)),    # steel_blue, light_steel_blue
    "roof": ((139, 0, 0), (205, 92, 92)),           # dark_red, indian_red
}


class Layer:
    def __init__(self, screen, name, grid_size, wall_width):
        self.screen = screen
        self.name = name
        self.grid_size = grid_size
        self.wall_width = wall_width
        self.color = LAYER_COLORS[name]

        self.grid = [[None for _ in range(self.grid_size[1])] for _ in range(self.grid_size[0])]

    def draw(self):
        grid_width = self.grid_size[0] * TILE_SIZE + 2 * self.wall_width
        grid_height = self.grid_size[1] * TILE_SIZE + 2 * self.wall_width
        pygame.draw.rect(self.screen, BROWN, (0, 0, self.wall_width, grid_height))
        pygame.draw.rect(self.screen, BROWN, (0, 0, grid_width, self.wall_width))
        pygame.draw.rect(self.screen, BROWN, (grid_width - self.wall_width, 0, self.wall_width, grid_height))
        pygame.draw.rect(self.screen, BROWN, (0, grid_height - self.wall_width, grid_width, self.wall_width))

        for x, y in ((0, self.wall_width + TILE_SIZE * 4),
                     (grid_width - self.wall_width, self.wall_width)):
            pygame.draw.rect(self.screen, LIGHT_GRAY, (x, y, self.wall_width, TILE_SIZE * 2))
            pygame.draw.line(self.screen, BLACK, (x, y), (x + self.wall_width, y), 1)
            pygame.draw.line(self.screen, BLACK, (x, y + TILE_SIZE * 2), (x + self.wall_width, y + TILE_SIZE * 2), 1)

        pos = pygame.mouse.get_pos()
        row = (pos[1] - self.wall_width) // TILE_SIZE
        col = (pos[0] - self.wall_width) // TILE_SIZE

        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                color = self.color[(i % 2 == 1) ^ (j % 2 == 1)]

                if j == row and i == col:
                    color = tuple(map(lambda x: min(255, x + 50), color))

                pygame.draw.rect(self.screen, color,
                                 (self.wall_width + i * TILE_SIZE, self.wall_width + j * TILE_SIZE,
                                  TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, BLACK,
                                 (self.wall_width + i * TILE_SIZE, self.wall_width + j * TILE_SIZE,
                                  TILE_SIZE, TILE_SIZE), 1)

        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if self.grid[i][j] is not None:
                    self.grid[i][j].draw()

    def on_mouse_button_down(self, pos, card_set):
        if card_set.selected is None:
            return

        row = (pos[1] - self.wall_width) // TILE_SIZE
        col = (pos[0] - self.wall_width) // TILE_SIZE

        if 0 <= row < self.grid_size[1] and 0 <= col < self.grid_size[0]:
            if isinstance(card_set.selected, Card):
                i = 0
                for i, card in enumerate(card_set.cards):
                    if card_set.selected is card:
                        break

                if self.grid[col][row] is not None:
                    return

                self.grid[col][row] = TurretBase(self.screen, TURRET_NAME[i],  (
                                                 self.wall_width + col * TILE_SIZE,
                                                 self.wall_width + row * TILE_SIZE),
                                                 row, col)
            else:
                self.grid[col][row] = None

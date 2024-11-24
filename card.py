import pygame
from const import *


class Card:
    def __init__(self, screen, name, position):
        self.screen = screen
        self.name = name
        self.position = position
        self.rect = pygame.Rect(position[0], position[1],
                                CARD_SIZE[0], CARD_SIZE[1])
        self.image = pygame.image.load(CARD_IMAGE[name])

    def draw(self):
        self.screen.blit(self.image, self.position)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

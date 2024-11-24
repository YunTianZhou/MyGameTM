import pygame
from card import Card
from const import *


class CardSet:
    def __init__(self, screen):
        self.screen = screen
        self.cards = []
        self.selected = None
        start_x = 832
        start_y = 180
        for card, position in zip(TURRET_NAME, CARD_POSITIONS):
            x = 16 + start_x + position[0] * (CARD_SIZE[0] + 16)
            y = start_y + position[1] * (CARD_SIZE[1] + 16)
            self.cards.append(Card(screen, card, (x, y)))
        self.shovel = pygame.image.load(TOOLS_IMAGE["shovel"])
        self.up_arrow = pygame.image.load(TOOLS_IMAGE["up_arrow"])
        self.down_arrow = pygame.image.load(TOOLS_IMAGE["down_arrow"])

    def draw(self):
        for card in self.cards:
            card.draw()
            if card is self.selected:
                self.draw_selected(*card.rect)

        for (x, y), tool in zip(TOOL_POSITIONS, (self.shovel, self.up_arrow, self.down_arrow)):
            self.screen.blit(tool, (x, y))
        if self.selected is self.shovel:
            self.draw_selected(*TOOL_POSITIONS[0], *TOOL_SIZE)
            
    def draw_selected(self, x, y, width, height):
        corner_length = 40
        corners = [
            ((0, 0), (corner_length, 0)),
            ((0, 0), (0, corner_length)),
            ((width, 0), (width - corner_length, 0)),
            ((width, 0), (width, corner_length)),
            ((0, height), (corner_length, height)),
            ((0, height), (0, height - corner_length)),
            ((width, height), (width - corner_length, height)),
            ((width, height), (width, height - corner_length))
        ]

        for start, end in corners:
            pygame.draw.line(
                self.screen, BLUE,
                (x + start[0], y + start[1]),
                (x + end[0], y + end[1]),
                4
            )

    def on_mouse_button_down(self, pos, layer_set):
        for card in self.cards:
            if card.is_clicked(pos):
                self.selected = card
                break

        if pygame.rect.Rect(*TOOL_POSITIONS[1], *TOOL_SIZE).collidepoint(pos):
            layer_set.next_layer()

        if pygame.rect.Rect(*TOOL_POSITIONS[2], *TOOL_SIZE).collidepoint(pos):
            layer_set.prev_layer()

        if pygame.rect.Rect(*TOOL_POSITIONS[0], *TOOL_SIZE).collidepoint(pos):
            self.selected = self.shovel

import pygame
from const import *
from layer_set import LayerSet
from card_set import CardSet

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

layer_set = LayerSet(screen)
card_set = CardSet(screen)


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            card_set.on_mouse_button_down(event.pos, layer_set)
            layer_set.on_mouse_button_down(event.pos, card_set)


def draw():
    screen.fill(GRAY)
    layer_set.draw()
    card_set.draw()
    pygame.display.update()
    clock.tick(60)


def main():
    while True:
        draw()
        update()


if __name__ == "__main__":
    main()

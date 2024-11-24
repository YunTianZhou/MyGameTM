import pygame
from const import *
from layer import Layer


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    layyer = Layer(screen, "Floor 1", (8, 6), 32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(GRAY)
        layyer.draw()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

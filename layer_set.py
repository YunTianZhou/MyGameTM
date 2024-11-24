from layer import Layer
from const import *


class LayerSet:
    def __init__(self, screen):
        self.screen = screen
        self.layers = []
        self.current_layer = 0

        for name in LAYER_NAME:
            self.layers.append(Layer(self.screen, name, (8, 6), 32))

    def draw(self):
        self.layers[self.current_layer].draw()

    def next_layer(self):
        self.current_layer = min(len(self.layers) - 1, self.current_layer + 1)

    def prev_layer(self):
        self.current_layer = max(0, self.current_layer - 1)

    def on_mouse_button_down(self, pos, card_set):
        self.layers[self.current_layer].on_mouse_button_down(pos, card_set)

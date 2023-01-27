import pygame

# Holds the current state of the game
state = None


class GameState:
    def __init__(self):
        pass

    def update(self):
        pass

    def render(self, screen: pygame.Surface, font: pygame.font.Font):
        pass

    def key_input(self, event):
        pass

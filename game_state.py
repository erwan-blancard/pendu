import pygame

# Holds the current state of the game
state = None


def set_state(newstate):
    global state
    state = newstate


class GameState:
    def __init__(self):
        pass

    def update(self):
        pass

    def render(self, screen: pygame.Surface, fonts: list[pygame.font.Font]):
        pass

    def key_input(self, event):
        pass

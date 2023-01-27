import pygame

# Holds the current state ID of the game
state = 0

MENU = 0
INGAME = 1
ADDWORD = 2


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

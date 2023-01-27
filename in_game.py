import pygame
from game_state import GameState


class InGameState(GameState):
    def __init__(self):
        super().__init__()

    def update(self):
        pass

    def render(self, screen, font):
        pass

    def key_input(self, event):
        pass

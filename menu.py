import sys
import pygame

import game_state
from game_state import GameState

from button import Button


class MenuState(GameState):

    def __init__(self):
        super().__init__()
        self.buttons += [
            Button("Jouer", 980 / 2 - 128, 600 / 2 + 36, 256, 72, lambda: game_state.set_state(game_state.INGAME)),
            Button("Ajouter un mot...", 980 / 2 - 200, 600 / 2 + 108, 400, 72, lambda: game_state.set_state(game_state.ADDWORD)),
            Button("Quitter", 980 / 2 - 128, 600 / 2 + 180, 256, 72, lambda: sys.exit(0))
        ]

    def update(self):
        pass

    def render(self, screen, fonts):
        super().render(screen, fonts)

    def key_input(self, event):
        super().key_input(event)

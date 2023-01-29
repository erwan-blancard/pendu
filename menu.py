import math
import sys
import pygame

import game_state
from game_state import GameState

from button import Button

import time


class MenuState(GameState):

    def __init__(self):
        super().__init__()
        self.buttons += [
            Button("Jouer", 980 / 2 - 128, 600 / 2 + 36, 256, 72, lambda: game_state.set_state(game_state.INGAME)),
            Button("Ajouter un mot...", 980 / 2 - 200, 600 / 2 + 108, 400, 72, lambda: game_state.set_state(game_state.ADDWORD)),
            Button("Quitter", 980 / 2 - 128, 600 / 2 + 180, 256, 72, lambda: sys.exit(0))
        ]

        self.titlescreen = pygame.image.load("res/title.png")
        self.titlescreen = pygame.transform.scale(self.titlescreen, (600, 132))

    def update(self):
        pass

    def render(self, screen, fonts):
        super().render(screen, fonts)
        screen.blit(self.titlescreen, (190, 76 + (math.sin(time.time()*2)-0.5)*10))

    def key_input(self, event):
        super().key_input(event)

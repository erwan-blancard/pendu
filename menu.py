import sys
import pygame

import game_state
from game_state import GameState
from in_game import InGameState
from add_word import AddWordState

from button import Button


class MenuState(GameState):
    buttons: list[Button] = []
    current_button = 0

    def __init__(self):
        self.buttons += [
            Button("Jouer", 256, 72, lambda: game_state.set_state(InGameState())),
            Button("Ajouter un mot...", 384, 72, lambda: game_state.set_state(AddWordState())),
            Button("Quitter", 256, 72, lambda: sys.exit(0))
        ]

    def update(self):
        pass

    def render(self, screen, fonts):

        # render buttons
        for i in range(len(self.buttons)):
            x = screen.get_width() / 2 - self.buttons[i].width / 2
            y = screen.get_height() / 2 + 16 + i * self.buttons[i].height + 24

            if i == self.current_button:
                color = (0, 0, 0)
                pygame.draw.rect(screen, color, pygame.Rect(x, y, self.buttons[i].width, self.buttons[i].height),
                                 width=5, border_radius=8)

            self.buttons[i].render(x, y, screen, fonts)

    def key_input(self, event):
        if event.key == pygame.key.key_code("up"):
            if 0 <= self.current_button < len(self.buttons):
                if self.current_button - 1 < 0:
                    self.current_button = len(self.buttons) - 1
                else:
                    self.current_button -= 1
            else:
                self.current_button = 0
        elif event.key == pygame.key.key_code("down"):
            if 0 <= self.current_button < len(self.buttons):
                if self.current_button + 1 >= len(self.buttons):
                    self.current_button = 0
                else:
                    self.current_button += 1
            else:
                self.current_button = 0
        elif event.key == pygame.key.key_code("return"):
            if 0 <= self.current_button < len(self.buttons):
                self.buttons[self.current_button].execute()

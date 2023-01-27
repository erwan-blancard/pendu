import sys
import pygame

import game_state
from game_state import GameState


class MenuState(GameState):

    buttons = ["Jouer", "Quitter"]
    current_button = -1

    def __init__(self):
        super().__init__()

    def update(self):
        pass

    def render(self, screen, font):

        # render buttons
        for i in range(len(self.buttons)):
            b_width = 256
            b_height = 72
            x = screen.get_width() / 2 - b_width / 2
            y = screen.get_height() / 2 + 16 + i*b_height + 24

            color = (255, 255, 255)
            if i == self.current_button:
                color = (0, 0, 0)

            pygame.draw.rect(screen, color, pygame.Rect(x, y, b_width, b_height), width=5, border_radius=8)
            text = font.render(self.buttons[i], True, (0, 0, 0))
            screen.blit(text, (x + ((b_width-text.get_width()) / 2), y + ((b_height - text.get_height()) / 2)))

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
                if self.buttons[self.current_button] == self.buttons[0]:
                    game_state.state = GameState()
                elif self.buttons[self.current_button] == self.buttons[1]:
                    sys.exit(0)

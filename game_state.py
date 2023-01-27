import pygame
import button
# Holds the current state ID of the game
state = 0
force_update = False

MENU = 0
INGAME = 1
ADDWORD = 2


def set_state(newstate, force=False):
    global state
    global force_update
    state = newstate
    force_update = force


# base class for states with button support
class GameState:
    def __init__(self):
        self.current_button = 0
        self.buttons: list[button.Button] = []

    def update(self):
        pass

    def render(self, screen: pygame.Surface, fonts: list[pygame.font.Font]):
        # render buttons
        for i in range(len(self.buttons)):
            if i == self.current_button:
                color = (0, 0, 0)
                pygame.draw.rect(screen, color, pygame.Rect(self.buttons[i].x, self.buttons[i].y, self.buttons[i].width,
                                                            self.buttons[i].height),
                                 width=5, border_radius=8)

            self.buttons[i].render(screen, fonts)

    def key_input(self, event):
        # button inputs
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

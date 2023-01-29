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

    def key_input(self, event: pygame.event.Event):
        # button inputs

        # mouse
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(self.buttons)):
            if (self.buttons[i].x <= mouse_pos[0] <= self.buttons[i].x + self.buttons[i].width) and (self.buttons[i].y <= mouse_pos[1] <= self.buttons[i].y + self.buttons[i].height):
                self.current_button = i
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    self.buttons[i].execute()

        # keys
        if event.type == pygame.KEYDOWN:
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

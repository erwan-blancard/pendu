import pygame
import text


class Button:

    def __init__(self, label, width, height, command=None):
        self.label = label
        self.width = width
        self.height = height
        self.command = command

    def render(self, x, y, screen: pygame.Surface, fonts: list[pygame.font.Font]):
        text.draw_centered_text(self.label, x+(self.width/2), y+(self.height/2), screen, fonts[1])

    def execute(self):
        if self.command is not None:
            self.command()

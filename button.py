import pygame
import text


class Button:

    def __init__(self, label, x, y, width, height, command=None):
        self.label = label
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.command = command

    def render(self, screen: pygame.Surface, fonts: list[pygame.font.Font]):
        text.draw_centered_text(self.label, self.x+(self.width/2), self.y+(self.height/2), screen, fonts[1])

    def execute(self):
        if self.command is not None:
            self.command()

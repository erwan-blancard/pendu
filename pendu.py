import sys
import pygame

import game_state
from menu import MenuState

pygame.init()
pygame.font.init()

FONTS = [
    pygame.font.SysFont("Berlin Sans FB Demi", 32),
    pygame.font.SysFont("Berlin Sans FB Demi", 48),
    pygame.font.SysFont("Berlin Sans FB Demi", 72)
]

screen = pygame.display.set_mode((980, 600))

game_state.state = MenuState()


def draw_background(surface: pygame.Surface):
    surface.fill((255, 255, 255))


while True:

    # INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            game_state.state.key_input(event)

            # print(pygame.key.name(event.key))

    # LOGIC
    game_state.state.update()

    # RENDER
    draw_background(screen)
    game_state.state.render(screen, FONTS)

    # update screen
    pygame.display.flip()

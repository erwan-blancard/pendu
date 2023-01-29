import sys
import pygame

import game_state
from menu import MenuState
from in_game import InGameState
from add_word import AddWordState

pygame.init()
pygame.font.init()

FONTS = [
    pygame.font.SysFont("Berlin Sans FB Demi", 32),
    pygame.font.SysFont("Berlin Sans FB Demi", 48),
    pygame.font.SysFont("Berlin Sans FB Demi", 72)
]

screen = pygame.display.set_mode((980, 600))

pygame.display.set_caption("Pendu")

game_state.state = 0
prev_state_id = 0
state = MenuState()


def draw_background(surface: pygame.Surface):
    surface.fill((255, 255, 255))


while True:
    # Update state
    if game_state.state != prev_state_id or game_state.force_update:
        if game_state.state == game_state.MENU:
            prev_state_id = game_state.MENU
            state = MenuState()
        elif game_state.state == game_state.INGAME:
            prev_state_id = game_state.INGAME
            state = InGameState()
        elif game_state.state == game_state.ADDWORD:
            prev_state_id = game_state.ADDWORD
            state = AddWordState()
        else:
            print("Invalid state id:", game_state.state)
        game_state.force_update = False

    # INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        state.key_input(event)

    # LOGIC
    state.update()

    # RENDER
    draw_background(screen)
    state.render(screen, FONTS)

    # update screen
    pygame.display.flip()

import sys
import pygame

import game_state
from menu import MenuState
from in_game import InGameState
from game_over import GameOverState

pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont("Arial", 48)
screen = pygame.display.set_mode((980, 600))

MENU = 0
IN_GAME = 1
GAME_OVER = 2

game_state.state = MenuState()


def draw_background(screen):
    screen.fill((255, 255, 255))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            game_state.state.key_input(event)

            # print(pygame.key.name(event.key))

    draw_background(screen)

    # LOGIC AND RENDER
    game_state.state.update()
    game_state.state.render(screen, FONT)

    # update screen
    pygame.display.flip()

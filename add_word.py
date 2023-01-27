import pygame

import game_state
from game_state import GameState
import text


class AddWordState(GameState):

    word = ""

    def __init__(self):
        super().__init__()

    def update(self):
        pass

    def render(self, screen, fonts):
        text.draw_centered_text("Entrez le nouveau mot", screen.get_width()/2, screen.get_height()/4, screen, fonts[2])
        text.draw_centered_text("à ajouter:", screen.get_width()/2, screen.get_height()/4+84, screen, fonts[2])
        text.draw_centered_text(self.word, screen.get_width()/2, screen.get_height()/2, screen, fonts[1])

    def key_input(self, event):
        inputed_letter = pygame.key.name(event.key)
        if inputed_letter == "escape":
            print("True")
        if inputed_letter == "return":
            pass
        else:
            is_letter = False
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if inputed_letter == letter:
                    is_letter = True
                    break
            if is_letter:
                self.word += inputed_letter

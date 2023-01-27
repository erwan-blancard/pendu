import pygame

import game_state
from game_state import GameState
import text


class AddWordState(GameState):

    def __init__(self):
        super().__init__()
        self.word = ""
        self.message = ""

    def update(self):
        pass

    def render(self, screen, fonts):
        text.draw_centered_text("Entrez le nouveau mot", screen.get_width()/2, screen.get_height()/4, screen, fonts[2])
        text.draw_centered_text("à ajouter:", screen.get_width()/2, screen.get_height()/4+84, screen, fonts[2])
        text.draw_centered_text(self.word, screen.get_width()/2, screen.get_height()/2 + 16, screen, fonts[1])
        text.draw_centered_text(self.message, screen.get_width()/2, screen.get_height()/2 + 84, screen, fonts[0], (255, 0, 0))

    def key_input(self, event):
        inputed_letter = pygame.key.name(event.key)
        if inputed_letter == "escape":
            game_state.set_state(game_state.MENU)
        elif inputed_letter == "return":
            if len(self.word) < 4:
                self.message = "Le mot doit contenir au moins 4 lettres !"
            else:
                try:
                    file = open("mots.txt", "a")
                    file.write("\n" + self.word)
                    file.close()
                    game_state.set_state(game_state.MENU)
                except IOError as e:
                    self.message = str(e)
        elif inputed_letter == "backspace":
            self.word = self.word[:-1]
        else:
            is_letter = False
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if inputed_letter == letter:
                    is_letter = True
                    break
            if is_letter:
                self.word += inputed_letter

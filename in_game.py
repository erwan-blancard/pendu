import pygame

import game_state
from game_state import GameState
import text
import random


def load_new_word():
    word = ""
    try:
        file = open("mots.txt")
        lines = file.readlines()
        word = lines[random.randint(0, len(lines)-1)]
        word = word.replace("\n", "")
        file.close()
    except IOError as e:
        word = "default"
    return word.lower()


class InGameState(GameState):

    word_to_find = load_new_word()
    blank_word = ""
    for i in range(len(word_to_find)):
        blank_word += "_"

    frames: list[pygame.Surface] = []
    errors_count = 0
    failed_letters = ""

    def __init__(self):
        super().__init__()
        for i in range(7):
            frame = pygame.image.load("res/part_"+str(i)+".png")
            frame = pygame.transform.scale(frame, (300, 300))
            self.frames += [frame]

    def update(self):
        if self.errors_count >= len(self.frames)-1:
            # game_state.set_state(GameOverState("Perdu ! Le mot à trouver était " + self.word_to_find + " !"))
            pass
        if self.blank_word == self.word_to_find:
            # game_state.set_state(GameOverState("Bravo ! Le mot était bien "+self.word_to_find+" !"))
            pass

    def render(self, screen, fonts):
        screen.blit(self.frames[self.errors_count], (16, 48))
        i = 0
        while i < len(self.failed_letters):
            text.draw_text(self.failed_letters[i], 96+i*24, 400, screen, fonts[0], (255, 0, 0))
            i += 1
        text_spacing = 32
        font_index = 2
        # reduce used font size if text is too long
        if (fonts[font_index].size(self.blank_word)[0] + (text_spacing*len(self.blank_word))) > ((300 + screen.get_width()) / 2):
            font_index = 1
            text_spacing = 20
        text.draw_aligned_spaced_text(self.blank_word, (300 + screen.get_width()) / 2, screen.get_height()/2 - 16, text_spacing, screen, fonts[font_index])

    def key_input(self, event):
        inputed_letter = pygame.key.name(event.key)
        is_letter = False
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if inputed_letter == letter:
                is_letter = True
                break
        if is_letter:
            # check if letter has already been typed (is in failed_letters)
            already_typed = False
            for letter in self.failed_letters:
                if inputed_letter == letter:
                    already_typed = True
                    break
            if not already_typed:
                has_found_letter = False
                i = 0
                # finds the letter
                while i < len(self.word_to_find):
                    if self.word_to_find[i] == inputed_letter:
                        has_found_letter = True
                        break
                    i += 1
                if not has_found_letter:
                    self.errors_count += 1
                    self.failed_letters += inputed_letter
                else:
                    # rebuilds the blank_word
                    while i < len(self.word_to_find):
                        if self.word_to_find[i] == inputed_letter and self.blank_word != inputed_letter:
                            tmp = self.blank_word[:i] + inputed_letter + self.blank_word[i+1:]
                            self.blank_word = tmp
                        i += 1

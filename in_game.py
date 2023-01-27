import time

import pygame

import game_state
from game_state import GameState
import text
import random


def load_new_word():
    word = "missigno"
    try:
        file = open("mots.txt")
        lines = file.readlines()
        word = lines[random.randint(0, len(lines)-1)]
        word = word.replace("\n", "")
        file.close()
    except IOError as e:
        print(e)
    return word.lower()


def render_overlay(screen):
    rect_over = pygame.Surface((screen.get_width(), screen.get_height()))
    rect_over.set_alpha(178)
    rect_over.fill((255, 255, 255))
    screen.blit(rect_over, (0, 0))


class InGameState(GameState):

    def __init__(self):
        self.word_to_find = load_new_word()
        self.blank_word = ""
        for i in range(len(self.word_to_find)):
            self.blank_word += "_"
        self.frames = []
        self.errors_count = 0
        self.failed_letters = ""
        self.endgame_message = ""
        self.endgame = False
        self.endgame_timer = 0

        for i in range(10):
            frame = pygame.image.load("res/part_"+str(i)+".png")
            frame = pygame.transform.scale(frame, (300, 300))
            self.frames += [frame]

    def update(self):
        if self.endgame:
            if time.time() >= self.endgame_timer + 3:
                game_state.set_state(game_state.MENU)
        else:
            if self.errors_count >= len(self.frames)-1:
                self.endgame_message = "Perdu ! Le mot à trouver était " + self.word_to_find + " !"
                self.endgame = True
                self.endgame_timer = time.time()
            if self.blank_word == self.word_to_find:
                self.endgame_message = "Bravo ! Le mot était bien "+self.word_to_find+" !"
                self.endgame = True
                self.endgame_timer = time.time()

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

        if self.endgame:
            render_overlay(screen)
            text.draw_centered_text(self.endgame_message, screen.get_width()/2, screen.get_height() / 2, screen, fonts[1], (28, 207, 0))

    def key_input(self, event):
        if not self.endgame:
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

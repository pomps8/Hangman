# FileName: Driver.py
# Author: Anthony Pompili
# Date: February 14, 2020


class HangmanGui:

    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess

    def print_game_ui(self):
        print("The word to guess is " + self.word_to_guess)

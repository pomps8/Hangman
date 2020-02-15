# FileName: Driver.py
# Author: Anthony Pompili
# Date: February 14, 2020


class HangmanGui:

    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.word_with_blanks = ""

    def print_game_ui(self):
        print("The word to guess is " + self.get_blank_word(self.word_to_guess))

    def get_blank_word(self, word_to_guess):
        blanked_out_word = ""

        for value in range(0, len(word_to_guess)):
            if word_to_guess[value] == " ":
                blanked_out_word += "   "
            else:
                if value + 1 >= len(word_to_guess):
                    blanked_out_word += "_"
                elif word_to_guess[value + 1] == " ":
                    blanked_out_word += "_"
                else:
                    blanked_out_word += "_|"

        return blanked_out_word
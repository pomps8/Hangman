# Imports
from HangmanGui import HangmanGui

# FileName: Hangman.py
# Author: Anthony Pompili
# Date: February 14, 2020

'''
Description: This file will be the main logic behind our game. The user will get to input what they believe
are the characters of the word into a prompt, and see if they are correct or not. Users will have a maximum
amount of tries before they "lose". If they guess the world before running out of amount of tries, then
they will win!
'''


class Hangman:
    # In every game, the user will have a total of 6 guesses before the game will end and they lose.
    max_amount_wrong = 6

    # The word for the player to guess
    phrase = "The word to guess"

    # UI for game
    hangman_ui = None

    def __init__(self):
        # Int to keep track of incorrect input by user
        self.__current_amount_wrong = 0
        self.start_game()

    def start_game(self):
        print("Game starting... \n \n \n")
        hangman_ui = HangmanGui(self.phrase)
        hangman_ui.print_game_ui()

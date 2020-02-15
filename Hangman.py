# Imports
from HangmanGui import HangmanGui

# FileName: Hangman.py
# Author: Anthony Pompili
# Date: February 14, 2020
# Description: This file will be the main logic behind our game. The user will get to input what they believe
# are the characters of the word into a prompt, and see if they are correct or not. Users will have a maximum
# amount of tries before they "lose". If they guess the world before running out of amount of tries, then
# they will win!

class Hangman:
    # In every game, the user will have a total of 6 guesses before the game will end and they lose.
    max_amount_wrong = 6

    # The word for the player to guess
    # TODO: Make this more dynamic by adding a text file with more words / phrases to pick from.
    phrase = "The word to guess"

    # UI for game
    hangman_ui = None

    # Function Name: init
    # Parameters: NONE
    # Return type: Hangman object
    # Description: Start off our game by setting up the player with 0 incorrect guesses and start the game
    def __init__(self):
        # Int to keep track of incorrect input by user
        self.__current_amount_wrong = 0
        self.start_game()

    # Function Name: start_game
    # Parameters: NONE
    # Return type: NONE
    # Description: Start game will initialize the hangmanGui and print the game ui
    def start_game(self):
        hangman_ui = HangmanGui(self.phrase)
        hangman_ui.print_game_ui()

        # Check to see if they can keep guessing
        while self.__current_amount_wrong != self.max_amount_wrong:
            user_input = input("Enter 1 character: ")
            if self.check_input(user_input):
                print("Good")
            else:
                print("Bad input, please try again.")


    def check_input(self, user_input):
        # if input is not a single char, return false, otherwise return true
        # TODO: Better error handling here if they enter a non-ASCII character.
        if len(user_input) == 0 or len(user_input) > 1 or user_input == " ":
            return False
        return True

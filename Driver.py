# Imports
from Hangman import Hangman

# FileName: Driver.py
# Author: Anthony Pompili
# Date: February 14, 2020
# Description: This file is the main driver for the "Hangman" game. This will initialize the game, and prompt
# the user if they want to play a game and then create a game for them to play with a phrase.

user_input = input("Do you want to play Hangman? (Type \"yes\" to play, otherwise the game will quit): ")

while (user_input.lower() == "yes"):
    print("Ok, lets play!")
    game_instance = Hangman()
    user_input = input("Would you like to play again? (Type \"yes\" to play, otherwise the game will quit): ")

print("Ok, bye then!")

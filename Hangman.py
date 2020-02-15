# Imports
from HangmanGui import HangmanGui
import re
import random

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
    # Regular expression to check if char is between A - Z and a - z
    pattern = re.compile("[A-Za-z]")

    # Function Name: init
    # Parameters: NONE
    # Return type: Hangman object
    # Description: Start off our game by setting up the player with 0 incorrect guesses and start the game
    def __init__(self):
        # Int to keep track of incorrect input by user
        self.__current_amount_wrong = 0
        # A unique set of all the letters guessed
        self.letters_guessed = set()
        # A unique set of all the correct letters
        self.correct_letters_guessed = set()
        # A unique set of off the individual letters in the
        self.answer_set = set()
        # The word for the player to guess, this word will be chosen from a file.
        self.phrase = ""
        # UI for game. This prints the list of the characters guessed, amount of wrong answers,
        # and the word / phrase the user has to guess.
        self.hangman_ui = None
        # Start the game
        self.start_game()

    # Function Name: start_game
    # Parameters: NONE
    # Return type: NONE
    # Description: Start game will initialize the hangmanGui and print the game ui
    def start_game(self):
        # Choose a phrase / word from external file
        self.random_phrase_selector()
        # Put all unique characters in the answer set so we know once all these
        # letters are guessed, the game is over.
        self.initialize_answer_set(self.phrase)
        # Set up the game UI
        hangman_ui = HangmanGui(self.phrase, self.max_amount_wrong)
        # Print the first instance of the game board
        hangman_ui.print_game_ui(self.__current_amount_wrong, self.correct_letters_guessed, self.letters_guessed)

        # Check to see if they can keep guessing.
        # This acts as a game loop for the hangman game
        # The user cannot have used all their incorrect guesses or must submit all the
        # characters in the word to be done with the game.
        while self.__current_amount_wrong != self.max_amount_wrong and \
                len(self.answer_set) != len(self.correct_letters_guessed):

            user_input = input("Enter 1 character (Type \"quit\" to exit game): ")
            # If the user types quit, the game ends.
            if user_input.lower() == "quit":
                break
            # Checks if the input given is valid, if it is, then it is check with
            # the phrase to see if it is a viable solution.
            elif self.check_input(user_input):
                self.letter_contained_in_word(user_input)
            # Bad input, user needs to try again.
            else:
                print("Bad input, please try again.")
            hangman_ui.print_game_ui(self.__current_amount_wrong, self.correct_letters_guessed, self.letters_guessed)

        if self.__current_amount_wrong == self.max_amount_wrong:
            print("You lost! The phrase was: " + self.phrase)
        elif self.__current_amount_wrong < self.max_amount_wrong and len(self.correct_letters_guessed) == len(self.answer_set):
            print("You win!")
        else:
            print("Game quit.")

    # Function Name: check_input
    # Parameters: user_input
    # Return type: Boolean
    # Description: This is a validation method to make sure the input is correct ( correct is a - z and A - Z ).
    def check_input(self, user_input):
        # if input is not a single char that is acceptable, return false, otherwise return true
        if len(user_input) == 0 or len(user_input) > 1 or user_input == " ":
            return False
        return self.pattern.fullmatch(user_input) is not None

    # Function Name: letter_contained_in_word
    # Parameters: user_input
    # Return type: Boolean
    # Description: This method checks if the input has been guessed, if it's in the phrase to guess, or if it has not
    # been guessed. If it is in the word, it is added to both the correct_letters_guessed list and the letters_guessed
    # list. If it has already been guessed, feedback is given to the user. If the character is not in the phrase and has
    # not been guessed, it results in an incorrect guess.
    def letter_contained_in_word(self, user_input):
        # if the character has not been guess and it is in the word
        if not user_input.lower() in self.letters_guessed and user_input.lower() in self.phrase.lower():
            print("Its in there and has not been guessed")
            print("\n \n \n \n \n \n")
            self.correct_letters_guessed.add(user_input.lower())
            self.letters_guessed.add(user_input.lower())
        # if the character has been guessed already
        elif user_input.lower() in self.letters_guessed:
            print("Letter has been guessed already")
            print("\n \n \n \n \n \n")
        # any other case, the character is not in the word
        else:
            print("Its not in there")
            print("\n \n \n \n \n \n")
            self.letters_guessed.add(user_input.lower())
            self.__current_amount_wrong += 1

    # Function Name: initialize_answer_set
    # Parameters: phrase
    # Return type: NONE
    # Description: This method initializes the answer set which holds all the unique characters from the
    # phrase the user needs to guess.
    def initialize_answer_set(self, phrase):
        for char in self.phrase:
            if char != " ":
                self.answer_set.add(char.lower())

    def random_phrase_selector(self):
        file = open("wordsList.txt", "r")
        list_of_words = file.readlines()
        self.phrase = random.choice(list_of_words).rstrip()
        print("Phrase is: \"" + self.phrase + "\"")
        file.close()


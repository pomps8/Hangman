# FileName: HangmanGui.py
# Author: Anthony Pompili
# Date: February 14, 2020


class HangmanGui:

    # Function Name: init
    # Parameters: word_to_guess
    # Return type: HangmanGui object
    # Description: Takes in the word to guess and generates the "blank" word, which is the word / phrase with
    # underscores as the characters to keep the user from knowing exactly what the word is.
    def __init__(self, word_to_guess):
        print("Game starting... \n \n \n")
        self.word_to_guess = word_to_guess
        self.word_with_blanks = ""

    # Function Name: print_game_ui
    # Parameters: NONE
    # Return type: NONE
    # Description: Prints the game board ui to the screen for the user to see. This consists of the
    # current amount of incorrect submissions and the phrase with the letters illuminated that they
    # have guessed thus far.
    def print_game_ui(self):
        print("The word to guess is " + self.get_blank_word(self.word_to_guess))

    # Function Name: get_blank_word
    # Parameters: word_to_guess
    # Return type: String
    # Description: Take the word / phrase passed in, and will add underscores for all characters,
    # and add 3 blank spaces for a regular space.
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

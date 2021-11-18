"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{Tie Wang}} ({{s4621539}})"
__email__ = "tie.wang@uqconnect.edu.au"
__date__ = "26/8/2020"



# Write your code here (i.e. functions)

def select_word_at_random(word_select):
    
    """
       Given the word select is either “FIXED” or “ARBITRARY” this function will return a string randomly
       selected from WORDS FIXED.txt or WORDS ARBITRARY.txt respectively.
       If word_select is anything other then the expected input then this function should return None.

       Parameters:
           word_select (str): "FIXED" or "ARBITRARY" word sets.
       Returns:
           word (str): The word being guessed by the player.
           Return None if word_select is neither “FIXED” or “ARBITRARY”. 
    """
    import random
    
    word = ''
    
    if word_select == "FIXED":
        word = random.choice(load_words("FIXED"))
    elif word_select == "ARBITRARY":
        word = random.choice(load_words("ARBITRARY"))
    else:
        word = None
        
    return word
    
def create_guess_line(guess_no,word_length):
    
    """
       This function returns the string representing the display corresponding to the guess number integer, guess_no.

       Parameters:
           guess_no (int): An integer representing how many guesses the player has made.
           word_length (int): An integer representing the length of the word being guessed by the player.
       Returns:
           guess_line(str): the string representing the display corresponding to the guess_no.
           guess_line template: 'Guess 1| * | * | - | - | - | - | - | - |\n'
           Return Error if either guess_no or word_length is off-limit.
    """
    if word_length == 6:
        if guess_no == 1:
            guess_line = 'Guess 1| * | * | - | - | - | - |'
        elif guess_no == 2:
            guess_line = 'Guess 2| - | - | * | - | * | - |'
        elif guess_no == 3:
            guess_line = 'Guess 3| - | - | * | - | * | - |'
        elif guess_no == 4:
            guess_line = 'Guess 4| - | - | - | * | - | * |'
        elif guess_no == 5:
            guess_line = 'Guess 5| - | - | * | - | - | * |'
        elif guess_no == 6:
            guess_line = 'Guess 6| * | - | - | - | - | * |' 
    elif word_length == 7:
        if guess_no == 1:
            guess_line = 'Guess 1| * | * | - | - | - | - | - |'
        elif guess_no == 2:
            guess_line = 'Guess 2| - | * | * | - | - | - | - |'
        elif guess_no == 3:
            guess_line = 'Guess 3| - | - | - | - | * | - | * |'
        elif guess_no == 4:
            guess_line = 'Guess 4| - | - | * | - | - | * | - |'
        elif guess_no == 5:
            guess_line = 'Guess 5| - | - | - | * | - | - | * |'
        elif guess_no == 6:
            guess_line = 'Guess 6| - | - | * | - | - | - | * |'
        elif guess_no == 7:
            guess_line = 'Guess 7| * | - | - | - | - | - | * |'
    elif word_length == 8:
        if guess_no == 1:
            guess_line = 'Guess 1| * | * | - | - | - | - | - | - |'
        elif guess_no == 2:
            guess_line = 'Guess 2| - | * | - | * | - | - | - | - |'
        elif guess_no == 3:
            guess_line = 'Guess 3| - | - | - | - | * | - | - | * |'
        elif guess_no == 4:
            guess_line = 'Guess 4| - | - | - | * | - | * | - | - |'
        elif guess_no == 5:
            guess_line = 'Guess 5| - | - | - | * | - | - | * | - |'
        elif guess_no == 6:
            guess_line = 'Guess 6| - | - | - | - | - | * | - | * |'
        elif guess_no == 7:
            guess_line = 'Guess 7| - | - | * | - | - | - | - | * |'
        elif guess_no == 8:
            guess_line = 'Guess 8| * | - | - | - | - | - | - | * |'
    elif word_length == 9:
        if guess_no == 1:
            guess_line = 'Guess 1| * | * | - | - | - | - | - | - | - |'
        elif guess_no == 2:
            guess_line = 'Guess 2| - | * | - | * | - | - | - | - | - |'
        elif guess_no == 3:
            guess_line = 'Guess 3| - | - | - | - | * | - | - | * | - |'
        elif guess_no == 4:
            guess_line = 'Guess 4| - | - | - | * | - | * | - | - | - |'
        elif guess_no == 5:
            guess_line = 'Guess 5| - | - | - | * | - | - | * | - | - |'
        elif guess_no == 6:
            guess_line = 'Guess 6| - | - | - | - | - | * | - | * | - |'
        elif guess_no == 7:
            guess_line = 'Guess 7| - | - | - | * | - | - | - | * | - |'
        elif guess_no == 8:
            guess_line = 'Guess 8| - | - | * | - | - | - | - | - | * |'
        elif guess_no == 9:
            guess_line = 'Guess 9| * | - | - | - | - | - | - | - | * |'
    else:
        guess_line = 'Error'
    return guess_line
    
    
def display_guess_matrix(guess_no,word_length,scores):
    
    """
       This function prints the progress of the game.
       This includes all line strings for guesses up to guess_no with
       their corresponding scores (a tuple containing all previous scores), and the line string for guess_no (without
       a score).

       Parameters:
           guess_no (int): An integer representing how many guesses the player has made.
           word_length (int): An integer representing the length of the word being guessed by the player.
           scores(tuple): A tuple containing all previous scores.
       Print:
           guess_line(str):the string representing the display corresponding to the guess_no.
    """
    if word_length =
    print(blahblah)

    
def compute_value_for_guess(word,start_index,end_index,guess):
    
    """
       Return the score, an integer, the player is awarded for a specific guess.
       The word is a string representing the word the player has to guess.
       The substring to be guessed is determined by the start index and end index.
       The substring is created by slicing the word from the start index up to and including the end index.
       The guess is a string representing the guess attempt the player has made.

       Parameters:
           word (str): The word being guessed by the player.
           start_index (int): Where the slicing started
           end_index (int): Where the slicing ended
           guess (str): The guess attempt the player has made
       Returns:
           score(int): The score which the player is awarded for a specific guess.
    """
    






def main():
    
    """
       Handles top-level interaction with user.
       At the start of the game the player should be greeted with the Welcome message.
       Once the guessing sequence commences the game should loop for the correct number of rounds
       until either the player wins by guessing the correct word or loses by guessing the incorrect word.
    """
    # Write the code for your main function here



if __name__ == "__main__":
    main()

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
    """
    
    slot = word_length*' - |'
    
    """
    Set up the slots  
    """
    
    slot_change_index_1 = 4*GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0]+1
    slot_change_index_2 = 4*GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1]+1
    

    """
    Designate the indexes of slots which are to be replaced with *
    """

    for i in range(slot_change_index_1,slot_change_index_2+4,4) :
        slot = slot[:i]+'*'+slot[i+1:]
    

    
    """
    Replace specific slots with *
    """
    
    guess_line = 'Guess '+str(guess_no)+'|'+slot
    return guess_line

    """
    Return the guess_line
    """

   
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
           matrix:the strings representing the display corresponding to the guess_no.
    """

    matrix_start = '       |'
    for len_of_word in range(1,word_length+1):
        matrix_start += ' '+str(len_of_word)+' |'
    matrix_start += '\n'+(4*word_length+9)*'-'+'\n'
    
    """
    Set up the start line of matrix.
    """

    
    matrix_main = ''
    if guess_no > 1:
        for time_of_guess in range(1,guess_no):
            matrix_main += create_guess_line(time_of_guess,word_length)+'   '+str(scores[time_of_guess-1])+' Points'+'\n'+(4*word_length+9)*'-'+'\n'
    elif guess_no == 1:
        matrix_main = ''
        
    

    """
    Build up the main content of matrix.
    If the guess_no is 1, there would be no main lines.
    """

    matrix_end = create_guess_line(guess_no,word_length)+'\n'+(4*word_length+9)*'-'

    """
    Set up the end line of matrix
    """
    
    matrix = matrix_start + matrix_main + matrix_end
    print(matrix)
    
    """
    Print the matrix
    """
    
def compute_value_for_guess(word,start_index,end_index,guess):
    
    """
       Return the score, an integer, the player is awarded for a specific guess.
       The word is a string representing the word the player has to guess.
       The substring to be guessed is determined by the start index and end index.
       The substring is created by slicing the word from the start index up to and including the end index.
       The guess is a string representing the guess attempt the player has made.
       Each vowel guessed in the correct position gets 14 points. 
       Each consonant guessed in the correct position gets 12 points. 
       Each letter guessed correctly but in the wrong position gets 5 points. 


       Parameters:
           word (str): The word being guessed by the player.
           start_index (int): Where the slicing started
           end_index (int): Where the slicing ended. Included.
           guess (str): The guess attempt the player has made.
       Returns:
           point(int): The point which the player is awarded for a specific guess.
    """

    substring = word[start_index:end_index+1]
    points = 0
    
    """
    Set up
    """

    for guess_tuple in enumerate(guess):
        
        if guess_tuple in enumerate(substring):
            
            if guess_tuple[1] in VOWELS:
                points += 14     
            elif guess_tuple[1] in CONSONANTS:
                points += 12
        elif guess_tuple[1] in word:
            points += 5

    """
    If the letter is in right position.
    Check if it is in VOWELS or not.
    
    If the letter is not in right position.
    Check if it's in the word.
    """

    return points
            
def game_setup(choice):
    
    """
       The player needs to setup the game based on the length of word he/she chooses.
       By 's' Start Game,and give the word based on player's choice
       By 'h' The game rules will be printed out and then the game will commence.
       By 'q' Quit game.
       Other inputs would be handled in main()
       
       Parameters:
           choice (str): The choice made by the player.
       Returns:
           word_select(str): The word selected from the words'pool based on player choice.
                             Either 'FIXED' or 'ARBITRARY'.
       Exit:
           If the player enters 'q' the game will end.

    """

    if choice == 's':
        answer = ''
        while True:
            answer = input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
            if answer == 'FIXED':
                break
            elif answer == 'ARBITRARY':
                break
        word_select = select_word_at_random(answer)
        return word_select
    elif choice == 'h':
        print(HELP)
        answer = ''
        while True:
            answer = input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
            if answer == 'FIXED':
                break
            elif answer == 'ARBITRARY':
                break
        word_select = select_word_at_random(answer)
        return word_select
    elif choice == 'q':
        exit()
   
def main():
    
    """
       Handles top-level interaction with user.
       At the start of the game the player should be greeted with the Welcome message.
       Once the guessing sequence commences the game should loop for the correct number of rounds
       until either the player wins by guessing the correct word or loses by guessing the incorrect word.
    """
    # Write the code for your main function here
    print(WELCOME)
    action = ''

    while True:
        action = input(INPUT_ACTION)
        if action == 's':
            break
        elif action == 'h':
            break
        elif action == 'q':
            break
        print(INVALID)
            
    word = game_setup(action)
    
    print('Now try and guess the word, step by step!!')

    
    """
       The part where the game is set up.
       As mentioned before inputs other than 's' or 'h' or 'q' will be handled here, as invalid input.
       Invalid input would lead to printing invalid command message (see below) and restart.
       “Please enter a valid command: “
    """
    scores = ()
    guess_no = 0
    word_length = len(word)
    
    while True:
        guess_no += 1
        
        if guess_no == word_length:
            break
        
        display_guess_matrix(guess_no,word_length,scores)
        
        answer_alert = 'Now enter Guess '+str(guess_no)+': '
        guess = input(answer_alert)

        start_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0]
        end_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1]
        scores += (compute_value_for_guess(word,start_index,end_index,guess),)
        
    display_guess_matrix(word_length,word_length,scores)    
    last_guess = input('Now enter your final guess. i.e. guess the whole word: ')
    
    if last_guess == word:
        print('You have guessed the word correctly. Congratulations.')
    else:
        print('Your guess was wrong. The correct word was ','"',word,'"',sep='')
        
    """
       The part where the game is commencing.
       The user will be prompted to guess the word, step by step.
       The guessing procedure involves n steps for word_length N,where the guess slices will depend on the GUESS INDEX TUPLE.
       At each of the N-1 first steps the user guesses a subsection of the word and receives feedback (their score) for that guess.
       The final Nth step involves guessing the whole word.
       After the Nth guess, the user is informed of whether they ‘won’ (i.e. guessed the word correctly) or ‘lost’ (in which case they are told what the word was).
       If, at any stage, the player enters a guess that is of the incorrect length,
       then the game should repeatedly prompt for the correct word length until the player enters a guess that matches the length of the substring to be guessed in that step.
       
    """
    
if __name__ == "__main__":
    main()


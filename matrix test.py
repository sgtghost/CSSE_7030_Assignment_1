from a1_support import *
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
            matrix_main += create_guess_line(time_of_guess,word_length)+'   '+str(scores[time_of_guess])+' Points'+'\n'+(4*word_length+9)*'-'+'\n'
    elif guess_no == 1:
        matrix_main = ''
        
    

    """
    Build up the main content of matrix.
    If the guess_no is 1, there would be no main lines.
    """

    matrix_end = create_guess_line(guess_no,word_length)+'\n'+(4*word_length+9)*'-'+'\n'

    """
    Set up the end line of matrix
    """
    
    matrix = matrix_start + matrix_main + matrix_end
    print(matrix)
    
    """
    Print the matrix
    """

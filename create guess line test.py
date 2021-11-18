GUESS_INDEX_TUPLE = (
    ((0,1),(2,4),(2,4),(3,5),(2,5),(0,5)),	    		# word length 6
    ((0,1),(1,2),(4,6),(2,5),(3,6),(2,6),(0,6)),	    	# word length 7
    ((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(2,7),(0,7)),	        # word length 8
    ((0,1),(1,3),(4,7),(3,5),(3,6),(5,7),(3,7),(2,8),(0,8))     # word length 9
)
def create_guess_line(guess_no,word_length):
    xxx = word_length*' - |'
    index_1 = 4*GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0]+1
    index_2 = 4*GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1]+1
    xxx = xxx[:index_1]+'*'+xxx[index_1+1:]
    xxx = xxx[:index_2]+'*'+xxx[index_2+1:]
    guess_line = 'Guess '+str(guess_no)+'|'+xxx
    return guess_line

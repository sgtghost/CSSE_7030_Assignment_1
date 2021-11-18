from a1_support import *
print(WELCOME)
action =''

def game_setup(action):
    if action == 's':
        answer = ''
        while True:
            answer = input("Do you want a 'FIXED' or 'ARBITRARY' length word?:")
            if answer == 'FIXED':
                break
            elif answer == 'ARBITRARY':
                break
        load_words(answer)
    elif action == 'h':
        print(HELP)
        answer = ''
        while True:
            answer = input("Do you want a 'FIXED' or 'ARBITRARY' length word?:")
            if answer == 'FIXED':
                break
            elif answer == 'ARBITRARY':
                break
        load_words(answer)    
    elif action == 'q':
        exit()


while True:
    action = input(INPUT_ACTION)
    if action == 's':
        break
    elif action == 'h':
        break
    elif action == 'q':
        break
    print(INVALID)

game_setup(action)
print('Now try and guess the word, step by step!!')
        
  
        
        

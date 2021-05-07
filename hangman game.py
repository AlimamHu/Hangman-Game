import time 
import random
'''
this is indroduction area about the game
& getting name of the user
& pretentation  
'''
print('\n\nWelcome to the Hangman game by AlimamHu')
name=input('Enter you name : ')
print('hello ' , name, ' !!best of luck')
time.sleep(2)
print('\nthis is starting \nwait a few second...')
time.sleep(3)



def main():
    '''
    in main function we use global function before the variable 
    because after calling the function 
    we eassily access the variable by name 
    example :-
        >>>main()
        >>>word        # type the variable name which are global call
    '''
    global word          
    global length
    global already_guess
    global play_game
    global display
    global count
    
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word=random.choice([words_to_guess])
    length=len(word)
    count=0
    display='_'*length
    already_guess=[]
    play_game=''


def play_loop():
    global play_game
    play_game=input('Do you want to play game enter the yes=y  or no=n\n ')
    while play_game  not in ['y','n','Y','N']:
        play_game=input('Do you want to play game enter the yes=y  or no=n\n ')

    if play_game=='y' or 'Y':
        main()
    elif play_game=='n' or 'N':
        print('Thanks for playing over game  !!I hope you play again')
        exit()


def hangman():
    global word
    global length
    global already_guess
    global play_game
    global display
    global count

    guss=input('This is Hangman word: '+display+ 'Enter you guess word \n\n')

    guss=guss.strip()
    if len(guss.strip)==0 or (guss)<='9':
        print('Invalid input , Try again\n ')
        hangman()


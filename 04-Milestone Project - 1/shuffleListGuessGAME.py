from random import shuffle

#initial list
alist = ['','x','']

def shuffle_list(aList):
    #take a list and return shuffled version
    shuffle(alist)
    return alist

def player_guess():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input ( "Pick a number: 0,1, or 2: ")

    return int(guess) 

def check_guess(mylist,guess):
    if mylist[guess] == 'x':
        print('Correct Guess!')
        print(mylist)
    else:
        print('Wrong! Better luck next time')
        print(mylist)

#shuffle mylist
mixedup_list = shuffle_list(alist)
#get user's guess
guess = player_guess()
# Check User's Guess
#------------------------
# Notice how this function takes in the input 
# based on the output of other functions!
check_guess(mixedup_list,guess)
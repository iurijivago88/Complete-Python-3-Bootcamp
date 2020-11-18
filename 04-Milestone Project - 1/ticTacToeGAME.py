import os
import random

"""function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number 
#/1/  on a number pad, so you get a 3 by 3 board representation"""
def display_board(board):
    os.system('cls')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('___________')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('___________')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = [' ']*10
# display_board(test_board)

"""" function that can take in a player input and assign their marker as 'X' or 'O'. 
#/2/ Think about using while loops to continually ask until you get a correct answer.  """
def player_input():
    marker = ''                                                          #anything is not equal to x or o.
    ''' output = ( player 1 marker, player 2 marker ) tuple type'''
    while not (marker == 'X' or marker == 'O'):                          # while user don't choose x or o, keep asking for it.
        marker = input('Player 1: Do you want to be X or O? ').upper()   # take user's input and capitalize it.

    if marker == 'X':                                                    # once one user 1 picked x, user 2 is o
        return ('X', 'O')
    else:
        return ('O', 'X')                                                # or the other way around: user 1 is o, user 2 is x
                                                    
""" function that takes in the board list object (tuple), a marker ('X' or 'O'), and a desired position (number 1-9) 
#/3/ and assigns it to the board."""
def place_marker(tabuleiro, marker, position):
    tabuleiro[position] = marker

#// TEST place_marker(test_board,'X',1)           #testboard: a object, marker: what to place, x or o,  position: where to place, 1-9
#display_board(test_board)

""" function that takes in a board and checks to see if someone has won.
#/4/"""
def win_check(board,mark):
    
    return ((board[7] == board[8] == board[9] == mark) or # across the top
    (board[4] ==  board[5] ==  board[6] == mark) or # across the middle
    (board[1] ==  board[2] ==  board[3] == mark) or # across the bottom
    (board[7] ==  board[4] ==  board[1] == mark) or # down the middle
    (board[8] ==  board[5] ==  board[2] == mark) or # down the middle
    (board[9] ==  board[6] ==  board[3] == mark) or # down the right side
    (board[7] ==  board[5] ==  board[3] == mark) or # diagonal
    (board[9] ==  board[5] ==  board[1] == mark))   # diagonal

#win_check(test_board,'X')
"""  function that uses the random module to randomly decide which player goes first.
#/5/ """
def choose_first():
    if random.randint(0, 1) == 0:             # heads or tails to start the game.
        return 'Player 1'
    else:
        return 'Player 2'

""" function that returns a boolean indicating whether a space on the board is freely available.
#/6/ """
def space_check(board, position):             # take board and its position, check availability   
    return board[position] == ' '             # true if it is EMPTY. 

""" function that checks if the board is full and returns a boolean value. True if full, False otherwise.
#/7/ """
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            #If there is space, board is not full, then returns False.
            return False
    #If board is full, returns True.
    return True

""" function that asks for a player's next position (as a number 1-9) and then uses the function 
#/8/ from step 6 to check if its a free position. If it is, then return the position for later use."""

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

#/9/ """ function that asks the player if they want to play again and returns a boolean True if they do want to play again."""
def replay():    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
#_______________________________________________________________________________________________________________________________
#start the actual game

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print(' Player 1 has won! ')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won! ')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        print("Thanks for playing Tic Tac Toe!")
        break
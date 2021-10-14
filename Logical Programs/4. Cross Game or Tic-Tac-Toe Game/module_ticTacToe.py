'''
@Author: Amit Shendge
@Date: 14-10-2021 1:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 14-10-2021 1:32PM
@Title : Tic Tac Toe program
'''

import random

def function_intInput(string):
    """
Description:
    Function is used to take user input with input validation chaecks for valueError
Parameter:
      string which should be shown in terminal
Return:
       user Input
"""

    while True:
        try: 
            return int(input(string))
        except ValueError:
            print('Plz enter valid integer input')
            continue


import random
board = []
ins = []
for i in range(9):
    board.append('-')


def function_print():
    """
Description:
    Function is used to print the board of tic tac toe
Parameter:
      no parameters required
Return:
       does not return anything this function prints board without returning
"""

    for i in range(3):
        print(board[i],end=' ')
    print()
    for i in range(3,6):
        print(board[i],end=' ')
    print()
    for i in range(6,9):
        print(board[i],end=' ')
    print('\n')

def function_rand():
    """
Description:
    Function is used to pick random number between 0 to 8 to demonstrate cpu players move
Parameter:
      no parameters required
Return:
       returns random number between 0 to 8
"""

    return random.randint(0,8)
    
def function_pcPlay():
    """
Description:
    Function is used to demonstrate pc players move
Parameter:
      no parameters required
Return:
       does not return anything
"""

    while True:
        pcInput = function_rand()
        if pcInput not in ins:
            board[pcInput] = 'o'
            ins.append(pcInput)
            break


def function_ourPlay():
    """
Description:
    Function is used to demonstrate players move on board by taking user input
Parameter:
      no parameters required
Return:
       does not return anything
"""

    while True:
        text = 'Enter your option : '
        userInput = function_intInput(text)
        if userInput in ins:
            print('this position is taken')
        else:
            board[userInput] = 'x'
            ins.append(userInput)
            break


def function_is_win():
    """
Description:
    Function is used to identify winner between player and cpu player
Parameter:
      no parameters required
Return:
       this function returns True when someone Wins!!!
"""

    if (board[0]=='x' and board[1]=='x' and board[2]=='x') or (board[3]=='x' and board[4]=='x' and board[5]=='x') or (board[6]=='x' and board[7]=='x' and board[8]=='x') or (board[0]=='x' and board[4]=='x' and board[8]=='x') or (board[2]=='x' and board[4]=='x' and board[6]=='x')or (board[0]=='x' and board[3]=='x' and board[6]=='x')or (board[1]=='x' and board[4]=='x' and board[7]=='x')or (board[2]=='x' and board[5]=='x' and board[8]=='x'):
        return True
    elif (board[0]=='o' and board[1]=='o' and board[2]=='o') or (board[3]=='o' and board[4]=='o' and board[5]=='o') or (board[6]=='o' and board[7]=='o' and board[8]=='o') or (board[0]=='o' and board[4]=='o' and board[8]=='o') or (board[2]=='o' and board[4]=='o' and board[6]=='o')or (board[0]=='o' and board[3]=='o' and board[6]=='o')or (board[1]=='o' and board[4]=='o' and board[7]=='o')or (board[2]=='o' and board[5]=='o' and board[8]=='o'):
        return True


function_print()

for num in range(9):
    if num%2==0:
        function_ourPlay()
        function_print()
        if function_is_win():
            print('You Won Congrats !!!')
            break

    else:
        function_pcPlay()
        function_print()
        if function_is_win():
            print('CPU Won !!!')
            break

if function_is_win():
    print('You won Thank You for Playing')
else:
    print('Game Tied !!!')

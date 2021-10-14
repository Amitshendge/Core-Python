'''
@Author: Amit Shendge
@Date: 14-10-2021 12:32AM
@Last Modified by: Amit Shendge
@Last Modified time: 14-10-2021 12:32AM
@Title : Gambler Program
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

text = 'Enter strating ammount : '
var_stakes = function_intInput(text)
text = 'Enter goal ammount : '
var_goal = function_intInput(text)

def function_gambling(stakes,goal):
    """
Description:
    Function is used to demonstrate a gambling situatuion.
    In which a coin is tossed and if heads our fair doubles
    and if it's tails we loose our fair
Parameter:
      starting ammount and goal to be reached
Return:
       string which demonstrates whether you reached your goal or not
       and how many coin toss you needed to either reach a goal or loose all your money
"""

    n=0
    temp_ammount = stakes
    while temp_ammount != 0 and temp_ammount != goal:
        coin_toss = random.random()
        if coin_toss < 0.5 :
            temp_ammount = temp_ammount + 1
        else:
            temp_ammount = temp_ammount - 1
        n = n + 1
    if temp_ammount == 0:
        return ('Sorry you lost all you money in ' + str(n) + ' plays')
    else:
        return ('Congrats You reached your goal in ' + str(n) + ' plays')


print(function_gambling(var_stakes,var_goal))
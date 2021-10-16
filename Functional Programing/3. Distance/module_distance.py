'''
@Author: Amit Shendge
@Date: 14-10-2021 11:11AM
@Last Modified by: Amit Shendge
@Last Modified time: 14-10-2021 11:11AM
@Title : Distance between origin and given point
'''
import math

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


def function_distance(x,y):
    """
Description:
    Function is used to find Distance between origin and given point
Parameter:
      x and y User inputs
Return:
       distance between given point to origin
"""
    return (math.sqrt((x*x) + (y*y)))

if __name__ == '__main__':

    a='Enter x : '
    x = function_intInput(a)
    a='Enter y : '
    y = function_intInput(a)

    print(function_distance(x,y))
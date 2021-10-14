'''
@Author: Amit Shendge
@Date: 14-10-2021 11:27AM
@Last Modified by: Amit Shendge
@Last Modified time: 14-10-2021 11:27AM
@Title : Roots of a Quadratic equation
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


def function_roots(a,b,c,delta):
    """
Description:
    Function is used to find roots of quadratic eqn
Parameter:
      values of a , b , c from user
Return:
       List of roots of given quadratic eqn
"""

    result_arr = []

    root1 = ((-b + math.sqrt(delta))/(2*a))
    result_arr.append(float(root1))

    root2 = ((-b - math.sqrt(delta))/(2*a))
    result_arr.append(float(root2))
    return result_arr


print('Quadratic eqn in form : a*x*x + b*x + c = 0')
aa = 'Enter value of a : '
a = function_intInput(aa)
aa = 'Enter value of b : '
b = function_intInput(aa)
aa = 'Enter value of c : '
c = function_intInput(aa)

delta = abs((b*b) - (4*a*c))

print('Roots are : ' + str(function_roots(a,b,c,delta)))
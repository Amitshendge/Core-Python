'''
@Author: Amit Shendge
@Date: 14-10-2021 11:54AM
@Last Modified by: Amit Shendge
@Last Modified time: 14-10-2021 11:54AM
@Title : Identify Wind Chill
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


def function_windchill(t,v):
    """
Description:
    Function is used to identify wind chill from formula
Parameter:
      temperature t (in Fahrenheit) and the wind speed v (in miles per hour)
Return:
       wind chill value in float
"""
    return 35.74 + (0.6215*t) + (0.4275*t - 35.75)*(v**0.16)


if __name__ == '__main__':
    while True:
        a = 'Enter value of temperature "t" (in Fahrenheit) : '
        t = function_intInput(a)
        if t <50 and t > 0 :
            break
        else:
            print('Keep it in range of 0 < t < 50')

    while True:
        a = 'Enter value of wind speed v (in miles per hour) : '
        v = function_intInput(a)
        if v < 120 and v > 3 :
            break
        else:
            print('Keep it in range of 3 < v < 120')

    print('Wind Chill : ' + str(function_windchill(t,v)))
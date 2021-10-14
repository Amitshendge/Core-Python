'''
@Author: Amit Shendge
@Date: 13-10-2021 10:15PM
@Last Modified by: Amit Shendge
@Last Modified time: 13-10-2021 10:15PM
@Title : 2D Array Demonstration
'''

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


a = 'Enter Column length : '
var_col = function_intInput(a)
a = 'Enter Row length : '
var_row = function_intInput(a)


def function_List(col,row):
    """
Description:
    Function is used to form a Two dimentional List and user inputs data to it
Parameter:
      number of columns and rows of Two dimentional List
Return:
       formed Two dimentional List
"""
    var_arr = []
    var_tempArr = []
    for i in range(0,row):
        for j in range(0,col):
            a = 'enter number : '
            var_tempArr.append(function_intInput(a)) 
        var_arr.append(var_tempArr)
        var_tempArr = []
    return var_arr


print(function_List(var_col,var_row))

'''
@Author: Amit Shendge
@Date: 14-10-2021 10:32AM
@Last Modified by: Amit Shendge
@Last Modified time: 14-10-2021 10:32AM
@Title : Sum of three Integer adds to ZERO
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


def function_Triplets(arr, n):
    """
Description:
    Function is used to find Triplets whose sum will be zero from given List
Parameter:
      List of numbers
Return:
       List of Triplets found in given List and If not found it says Triplets does not exist
"""
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    temp_arr = [arr[i], arr[j], arr[k]]
                    result_arr.append(temp_arr)
                    found = True


    if (found == False):
        return "Triplets does not exist"
    else:
        return result_arr

if __name__ == '__main__':
    var_arr = []
    result_arr = []

    a = 'How many Number you want to Enter : '
    var_number = function_intInput(a)
    for i in range(var_number):
        a = 'Enter Number : '
        var_arr.append(function_intInput(a))
    n = len(var_arr)

    print(function_Triplets(var_arr,n))
 

'''
@Author: Amit Shendge
@Date: 13-10-2021 07:40PM
@Last Modified by: Amit Shendge
@Last Modified time: 13-10-2021 07:40PM
@Title : Power of 2 List of numbers
'''

var_number = int(input('Enter the Number : '))
var_list = []

for i in range(1,var_number+1):
    var_list.append(int(i**2))

print(var_list)
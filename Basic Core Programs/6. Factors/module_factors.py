'''
@Author: Amit Shendge
@Date: 13-10-2021 08:25PM
@Last Modified by: Amit Shendge
@Last Modified time: 13-10-2021 08:25PM
@Title : Prime Factors of given Number Program
'''

var_number = int(input('Enter Number : '))
var_temp = var_number
var_factors=[]
while var_temp != 1:
    for i in range(2,var_number):
        if var_temp % i == 0 :
            while var_temp % i == 0:
                var_factors.append(i)
                var_temp = var_temp / i
    var_temp=1

if len(var_factors) == 0:
    print(str(var_number) + ' is a Prime Number')
else:
    print(var_factors)
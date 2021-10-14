'''
@Author: Amit Shendge
@Date: 14-10-2021 09:30AM
@Last Modified by: Amit Shendge
@Last Modified time: 14-10-2021 09:30AM
@Title : Unique Coupon Numbers Generator Program
'''

import random
result_list = []

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


def function_couponGenerator(total_coupons):
    count = 0
    for i in range(total_coupons):
        while True:
            count += 1
            num = random.randint(10000000,99999999)
            if num not in result_list:
                result_list.append(num)
                break
    return count


text = 'How many Unique Coupon codes you want to Generate : '
var_numberOfCoupons = function_intInput(text)
randoms = function_couponGenerator(var_numberOfCoupons)

print(result_list)
print('Total ', randoms , ' random numbers needed to generate unique coupons')
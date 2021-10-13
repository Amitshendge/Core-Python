'''
@Author: Amit Shendge
@Date: 13-10-2021 08:00PM
@Last Modified by: Amit Shendge
@Last Modified time: 13-10-2021 08:00PM
@Title : Harmonic Number Program
'''

from fractions import Fraction
var_number = int(input('Enter the Number : '))
var_harmonic = 0

for i in range(1,var_number+1):
    var_harmonic = var_harmonic + (1/i)

print("Harmonic number is : " + str(Fraction(var_harmonic).limit_denominator(10000)))
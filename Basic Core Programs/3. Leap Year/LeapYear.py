'''
@Author: Amit Shendge
@Date: 13-10-2021 08:40AM
@Last Modified by: Amit Shendge
@Last Modified time: 13-10-2021 08:40AM
@Title : Leap Year or Not a Leap Year
'''

year = int(input('Enter Year : '))

if (year%100 != 0 and year%4 == 0) or year%400 == 0:
    print(str(year) + ' is a Leap Year')
else:
    print(str(year) + ' is Not a Leap Year')
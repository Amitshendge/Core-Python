'''
@Author: Amit Shendge
@Date: 12-10-2021 08:54PM
@Last Modified by: Amit Shendge
@Last Modified time: 12-10-2021 08:54PM
@Title : User Input Demonstartion
'''
isCorect=True
while isCorect==True :
    name = input('Enter your name : ')
    if len(name) > 3 :
        print('Hello ' + name + ', How are you')
        isCorect=False
    else:
        print('Wrong name Entered name should be minimum 3 characters')
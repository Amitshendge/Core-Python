'''
@Author: Amit Shendge
@Date: 12-10-2021 09:34PM
@Last Modified by: Amit Shendge
@Last Modified time: 12-10-2021 09:34PM
@Title : User Input Demonstartion
'''

import random

userInput = int(input('Enter How many times a coint to be tossed : '))
heads=0
tails=0

for x in range(userInput) :
    coin = random.random()

    if coin<0.5 :
        heads=heads+1
    else :
        tails=tails+1

headsPercentage = int(heads / userInput *100)
tailsPercentage = 100-headsPercentage
print('Heads Percentage is : ' + str(headsPercentage))
print('Tails Percentage is : ' + str(tailsPercentage))
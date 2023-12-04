"""
Name: Leonard (Lenny) Muldoon
Date: 12/2/2023
"""

import math
import random

#calculates the probability of rolling the same number on rolling a number of sided dice (in this case 5 6 sided dice) without rerolling
def probabilityOfDiceNoReroll(amountOfDice, sides):
    return ((1/sides) ** amountOfDice) * sides

#rolls a number of dice
def rollDice(amountOfDice, sides):
    return [random.randint(1, sides) for i in range(amountOfDice)]

#returns true if all dice are the same
def allSame(diceRolls):
    return all(d == diceRolls[0] for d in diceRolls)

def findHighestCount(diceRolls):
    num = 0
    count = 0
    highestCount = 0
    for i in range(len(diceRolls)):
        count = 0
        num = diceRolls[0]
        for d in diceRolls:
            if diceRolls[i] == num:
                count += 1
        if count > highestCount:
            highestCount = num
    return num

def main():
    numOfDice = 5
    sidesOfDice = 6
    timesAllFive = 0
    #part 1 answers
    print("The probability of rolling the same number on", numOfDice, sidesOfDice, "sided dice is:", probabilityOfDiceNoReroll(numOfDice, sidesOfDice))
    dice = rollDice(numOfDice, sidesOfDice)
    for i in range(100000):
        if allSame(dice):
            timesAllFive += 1
        dice = rollDice(numOfDice, sidesOfDice)

    print("Number of times out of 100000 rolls that dice were the same:", timesAllFive)
    print(dice)
    print(findHighestCount(dice))

    #part 2 answers
    #for d in dice:



main()

"""
Name: Leonard (Lenny) Muldoon
Date: 12/2/2023
"""

import math
import random

numOfDice = 5
sidesOfDice = 6
timesAllFive = 0

#calculates the probability of rolling the same number on rolling a number of sided dice (in this case 5 6 sided dice) without rerolling
def probabilityOfDiceNoReroll(amountOfDice, sides):
    return ((1/sides) ** amountOfDice) * sides

#rolls a number of dice
def rollDice(amountOfDice):
    return [random.randint(1, 6) for i in range(amountOfDice)]

#returns true if all dice are the same
def allSame(diceRolls):
    return all(d == diceRolls[0] for d in diceRolls)


dice = rollDice(numOfDice)
print(dice)
    



print("The probability of rolling the same number on ", numOfDice, " ", sidesOfDice, " sided dice is: ", probabilityOfDiceNoReroll(numOfDice, sidesOfDice))
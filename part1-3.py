"""
Name: Leonard (Lenny) Muldoon
Date: 12/2/2023
"""

import math

numOfDice = 5
sidesOfDice = 6

#calculates the probability of rolling the same number on rolling a number of sided dice (in this case 5 6 sided dice)
def probabilityOfDiceNoReroll(amountOfDice, sides):
    return ((1/sides) ** amountOfDice) * sides





print("The probability of rolling the same number on ", numOfDice, " ", sidesOfDice, " sided dice is: ", probabilityOfDiceNoReroll(numOfDice, sidesOfDice))
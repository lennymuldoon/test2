"""
Name: Leonard (Lenny) Muldoon
Date: 12/2/2023
"""

import math

numOfDice = 5

#calculates the probability of rolling the same number on rolling a number of 6 sided dice (in this case 5)
def probabilityOfDiceNoReroll(amountOfDice):
    return ((1/6) ** amountOfDice) * 6





print("The probability of rolling the same number on ", numOfDice, " dice is: ", probabilityOfDiceNoReroll(numOfDice))
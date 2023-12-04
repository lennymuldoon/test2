"""
Name: Leonard (Lenny) Muldoon
Date: 12/2/2023
"""

import math
import random

#calculates the probability of rolling the same number on rolling a number of sided dice (in this case 5 6 sided dice) without rerolling
def probabilityOfDiceNoReroll(amountOfDice, sides):
    return (1/(sides ** amountOfDice)) * sides

def probabilityOfDiceReroll(amountOfDice, sides):
    return (1/((sides ** amountOfDice)** 2)) * sides

#rolls a number of dice
def rollDice(amountOfDice, sides):
    return [random.randint(1, sides) for i in range(amountOfDice)]

def rerollDie(die, sides):
    die = random.randint(1, sides)

#returns true if all dice are the same
def allSame(diceRolls):
    return all(d == diceRolls[0] for d in diceRolls)

#returns number with highest count in rolls
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
    print("The probability of rolling the same number on", numOfDice, sidesOfDice, "sided dice with no reroll is:", probabilityOfDiceNoReroll(numOfDice, sidesOfDice))
    dice = rollDice(numOfDice, sidesOfDice)
    for i in range(100000):
        if allSame(dice):
            timesAllFive += 1
        dice = rollDice(numOfDice, sidesOfDice)

    print("Number of times out of 100000 rolls that dice were the same without reroll:", timesAllFive)

    #part 2 answers
    print("The probability of rolling the same number on", numOfDice, sidesOfDice, "sided dice with reroll is:", probabilityOfDiceReroll(numOfDice, sidesOfDice))
    timesAllFive = 0
    dice = rollDice(numOfDice, sidesOfDice)
    for i in range(100000):
        if allSame(dice):
            timesAllFive += 1
        else:
            highestNum = findHighestCount(dice)
            for d in dice:
                if d != highestNum:
                    rerollDie(d, sidesOfDice)
            if allSame(dice):
                timesAllFive += 1
        dice = rollDice(numOfDice, sidesOfDice)
    print("Number of times out of 100000 rolls that dice were the same with reroll:", timesAllFive)

    #part 3 answers
    stayWins = 0
    switchWins = 0

    for i in range(100000):
        doors = [0, 0, 0] 
        prizePosition = random.randint(0, 2)
        doors[prizePosition] = 1  # 1 represents the prize
        contestantChoice = random.randint(0, 2)
        doorsOpened = [i for i in range(3) if i != contestantChoice and doors[i] == 0]
        montyOpens = random.choice(doorsOpened)
        switchChoice = next(i for i in range(3) if i != contestantChoice and i != montyOpens)
        stayWins += doors[contestantChoice]
        switchWins += doors[switchChoice]

    stayWinPercentage = stayWins / 100000 * 100
    switchWinPercentage = switchWins / 100000 * 100
    print("Win percentage if staying:", stayWinPercentage)
    print("Win percentage if switching:", switchWinPercentage)

main()

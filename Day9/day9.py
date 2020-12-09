import sys

f = open("C:\\Users\\Erika\\Documents\\AdventOfCode\\Day9\\input.txt", "r")

lines = f.readlines()
lines = [int(s.replace("\n", '')) for s in lines]

nbrsBefore = 25

def HasValidAddition(nbrsToCheck, result):
    for nbr1 in nbrsToCheck:
        for nbr2 in nbrsToCheck:
            if nbr1 != nbr2 and nbr1+nbr2 == result:
                return True
    return False

def HasValidAdditionSet(result):
    for firstIndex in range(0, len(lines)-1):
        numberToTry = [lines[firstIndex]]
        for secondIndex in range(firstIndex+1, len(lines)-1):
            numberToTry.append(lines[secondIndex])
            if sum(numberToTry) == result:
                return numberToTry
    return []

for index in range(nbrsBefore, len(lines)-1):
    if not HasValidAddition(lines[index-nbrsBefore: index],lines[index]):
        print(lines[index])
        validSet = HasValidAdditionSet(lines[index])
        print(min(validSet) + max(validSet))
        break
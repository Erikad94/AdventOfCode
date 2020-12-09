import sys

f = open("C:\\Users\\Erika\\Documents\\AdventOfCode\\Day8\\input.txt", "r")

lines = f.readlines()

def part1(linesToCheck):
    pastLines = []
    currentLine = 0
    acc = 0
    while repeat == False:
        if currentLine in pastLines or currentLine == len(linesToCheck):
            return (acc, currentLine)
        else:
            pastLines.append(currentLine)

        if linesToCheck[currentLine][0:3] == "acc":
            acc += int(linesToCheck[currentLine][4:])
            currentLine += 1
        elif linesToCheck[currentLine][0:3] == "jmp":
            nextLine = currentLine + int(linesToCheck[currentLine][4:])
            currentLine += int(linesToCheck[currentLine][4:])
        elif linesToCheck[currentLine][0:3] == "nop":
            currentLine += 1

def part2(linesToCheck):
    currentLine = 0
    acc = (0,0)
    while acc[1] != len(linesToCheck):
        if lines[currentLine][0:3] == "jmp":
            linesCopy = lines.copy()
            linesCopy[currentLine] = "nop" + linesToCheck[currentLine][3:]
            acc = part1(linesCopy)
        elif linesToCheck[currentLine][0:3] == "nop":
            linesCopy = linesToCheck.copy()
            linesCopy[currentLine] = "jmp" + linesToCheck[currentLine][3:]
            acc = part1(linesCopy)
        currentLine+=1
    return acc

print(part1(lines)[0])
print(part2(lines)[0])
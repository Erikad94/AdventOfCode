import sys
f = open("input.txt", "r")
lines = f.readlines()

def calculateTrees(right, down):
    posX = 0
    posY = 0
    answer = 0
    length = len(lines[posY])-1
    while posY < len(lines):
        if(lines[posY][posX] == "#"):
            answer+=1
        posX = (posX + right) % length
        posY += down
    return answer

print(calculateTrees(3, 1))
print(calculateTrees(1, 1)*calculateTrees(3, 1)*calculateTrees(5, 1)*calculateTrees(7, 1)*calculateTrees(1, 2))
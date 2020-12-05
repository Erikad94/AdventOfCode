import sys
import math
f = open("input.txt", "r")

rowMax = 127
seatMax = 7

seatIdMax = 0

def FindRowOrSeat(input, max):
    min = 0
    for letter in input: 
        dif = (max-min)/2
        if (letter == "F" or letter == "L"):
            max = max-math.ceil(dif)
        else :
            min = min+math.ceil(dif)
    return min

for line in f.readlines():
    row = FindRowOrSeat(line[0:7], rowMax)
    seat = FindRowOrSeat(line[7:], seatMax)
    id = row*8+seat

    if seatIdMax < id:
        seatIdMax = id
print(seatIdMax)

import sys
import math
f = open("input.txt", "r")

rowMax = 127
seatMax = 7
seatIdMax = 0
seats = []

def FindRowOrSeat(input, max):
    min = 0
    for letter in input: 
        dif = (max-min)/2
        if (letter == "F" or letter == "L"):
            max = max-math.ceil(dif)
        else :
            min = min+math.ceil(dif)
    return min

def FindSeat():
    seats.sort()

    if(seats[0] != seats[1]-1):
        return seats[1]-1
    for x in range(1, len(seats)-2):
        if(seats[x+1] != seats[x]+1):
            return seats[x]+1

for line in f.readlines():
    row = FindRowOrSeat(line[0:7], rowMax)
    seat = FindRowOrSeat(line[7:], seatMax)
    id = row*8+seat

    if(row>0 and row <127):
        seats.append(id)
    if seatIdMax < id:
        seatIdMax = id
print(seatIdMax)
print(FindSeat())



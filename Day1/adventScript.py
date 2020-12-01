import sys
f = open("input.txt", "r")

lines = []
for val in f.readlines():
    lines.append(int(val))
for a in lines:
    for b in lines:
        if a+b==2020:
            print("the answer :", a*b) 
            sys.exit("You have found the answer")
import sys
f = open("input.txt", "r")

lines = []
answer1 = ""
for val in f.readlines():
    lines.append(int(val))
for a in lines:
    for b in lines:
        if a+b==2020:
            answer1 = str(a*b) 
            break
for a in lines:
    for b in lines:
        for c in lines:
            if a+b+c==2020:
                print("the answers are :", answer1, "and", a*b*c) 
                sys.exit("You have found the answers")
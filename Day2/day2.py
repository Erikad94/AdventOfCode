import sys
f = open("input.txt", "r")

answer1 = 0
answer2 = 0
for val in f.readlines():
    line = val.split()
    lowest = int(line[0].split("-")[0])
    highest = int(line[0].split("-")[1])
    letter = line[1].split(":")[0]
    stringToEvaluate = line[2]

    if(stringToEvaluate.count(letter) <= highest and stringToEvaluate.count(letter) >= lowest):
        answer1+=1
    if(stringToEvaluate[lowest-1] == letter and not stringToEvaluate[highest-1] == letter) or (not stringToEvaluate[lowest-1] == letter and stringToEvaluate[highest-1] == letter):
        print(line)
        answer2+=1
print(answer1)
print(answer2)
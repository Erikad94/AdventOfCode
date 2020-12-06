import sys

f = open("input.txt", "r")

answers1 = ""
count1 = 0
answers2 = ""
count2 = 0
countNumOfPeople = 0

def CountAndRemove(answers, numOfPeople):
    count = 0
    while len(answers)> 0:
        numAnswers = answers.count(answers[0])
        if(numAnswers == numOfPeople):
            count+=1
        answers = answers.replace(answers[0], '')
    return count

for line in f.readlines():
    if line == "\n":
        answers1 = ""
        count2+= CountAndRemove(answers2, countNumOfPeople)
        answers2 = ""
        countNumOfPeople = 0
    else:
        countNumOfPeople+=1
        line = line.strip('\n')
        for letter in line:
            answers2 += letter
            if letter not in answers1:
                answers1 += letter
                count1 +=1
count2+= CountAndRemove(answers2, countNumOfPeople)
print(count1)
print(count2)
import sys
import re

f = open("input.txt", "r")
reg = r'^([\w]+ [\w]+)'

def hasColoredBag(bags, rules, colorToFind):
    for bag in bags:
        if (bag[0] == colorToFind):
            return True
    for bag in bags:
        if hasColoredBag(rules[bag[0]], rules, colorToFind):
            return True
    return False

def countBags(bag, rules):
    bagsInside = rules[bag]
    totalBagsInside = 0
    for bagInside in bagsInside:
        totalBagsInside += countBags(bagInside[0], rules) * bagInside[1]
    return 1 + totalBagsInside

rules = {}
for line in f.readlines():
    bagPos = re.search(r"\d", line)
    if bagPos is not None:
        for bag in line[bagPos.start():].split(", "):
            bagColor = " ".join(bag.split(" ")[1:3])
            parentBag = re.match(reg, line).group()
            number = int(bag.split(" ")[0])
            if parentBag in rules:
                bagList = rules[parentBag]
                bagList.append((bagColor, number))
                rules[parentBag] = bagList
            else:
                rules[parentBag] = [(bagColor, number)]
    else:
        parentBag = re.match(reg, line).group()
        rules[parentBag] = []

nbrBag = 0
for bag in rules:
    if hasColoredBag(rules[bag], rules, "shiny gold"):
        nbrBag += 1

print(nbrBag)
print(countBags("shiny gold", rules)-1)
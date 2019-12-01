import math
import functools
f = open("day1_input.txt", "r")


def calculateFuel(mass):
    return math.floor(int(mass)/3)-2


# Part1
fuelList = [calculateFuel(line) for line in f]
part1Answer = functools.reduce(lambda a, b: a+b, fuelList)
print(part1Answer)
# 3457681

# Part2
#fuelList = [calculateFuel(line) for line in f]
finalList = [x for x in fuelList]
while len(fuelList) > 0:
    fuelCost = calculateFuel(fuelList.pop())
    if fuelCost > 0:
        finalList.append(fuelCost)
        fuelList.append(fuelCost)

part2Answer = functools.reduce(lambda a, b: a+b, finalList)
print(part2Answer)

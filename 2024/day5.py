from collections import defaultdict
file = open("day5.txt", "r")
relations = ([''], [''])*1176

index = 0

for line in file:
    if line == "\n":
        break
    left = line[0:2]
    right = line[3:].strip("\n")
    relations[index][0] = index
    relations[index][1] = index-1
    print(relations[index], index)
    index += 1

file = open("day1.txt", "r")
data = []
for line in file:
    data.append(line.strip("\n").split())

left_side = []
right_side = []

for i in data:
    left_side.append(int(i[0]))
    right_side.append(int(i[1]))

left_side = sorted(left_side)
right_side = sorted(right_side)

distance = 0
for i in range(len(left_side)):
    distance += abs(right_side[i] - left_side[i])
print(distance)


### task2
result = 0

for i in range(len(left_side)):
    for j in range(i, len(left_side)):
        if left_side[i] == right_side[j]:
            result += left_side[i]
print(result)
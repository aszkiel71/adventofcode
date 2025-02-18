import re
file = open("day3.txt", "r")
data = ""
for line in file:
    data += line.strip("'\n")

print(sum(eval(f"{a}*{b}") for a, b in re.findall(r"mul\((\d+),(\d+)\)", data)))

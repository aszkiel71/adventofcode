import re


with open("day3.txt", "r") as file:
    data = file.read().strip()


def mul(a, b):
    return a * b


def is_correct(s):
    if not (s.startswith("mul(") and s.endswith(")")):
        return False
    tmp_s = s[4:-1]  # Usuwamy "mul(" i ")"
    if ',' not in tmp_s:
        return False
    left_segment, right_segment = tmp_s.split(',', 1)
    return left_segment.isdigit() and right_segment.isdigit()


pattern = r'mul\(\d+,\d+\)'
instructions = re.findall(pattern, data)


result = 0
for instruction in instructions:
    if is_correct(instruction):
        numbers = instruction[4:-1].split(',')
        a, b = int(numbers[0]), int(numbers[1])
        result += mul(a, b)

print(result)

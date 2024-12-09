import re


with open("day3.txt", "r") as file:
    data = file.read().strip()


def mul(a, b):
    return a * b


def is_correct(s):
    if not (s.startswith("mul(") and s.endswith(")")):
        return False
    tmp_s = s[4:-1]
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


import re

# Read and process the input data
with open("day3.txt", "r") as file:
    data = file.read().strip()

# Function to perform multiplication
def mul(a, b):
    return a * b

# Function to check if a "mul" instruction is syntactically correct
def is_correct(s):
    if not (s.startswith("mul(") and s.endswith(")")):
        return False
    tmp_s = s[4:-1]
    if ',' not in tmp_s:
        return False
    left_segment, right_segment = tmp_s.split(',', 1)
    return left_segment.isdigit() and right_segment.isdigit()

# Define patterns for instructions
mul_pattern = r'mul\(\d+,\d+\)'
do_pattern = r'do\(\)'
dont_pattern = r"don't\(\)"

# Extract instructions in sequence
instructions = re.findall(rf'{mul_pattern}|{do_pattern}|{dont_pattern}', data)

# Initialize state and result
mul_enabled = True
result = 0

# Process each instruction
for instruction in instructions:
    if instruction == 'do()':
        mul_enabled = True
    elif instruction == "don't()":
        mul_enabled = False
    elif is_correct(instruction):
        if mul_enabled:
            numbers = instruction[4:-1].split(',')
            a, b = int(numbers[0]), int(numbers[1])
            result += mul(a, b)

# Output the final result
print(result)

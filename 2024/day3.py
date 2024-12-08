file = open("day3.txt", "r")
data = ""
for line in file:
    data = line.strip()

def mul(a, b):
    return a * b

def is_digita(s):
    if s in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return True
    return False

def is_correct(s):
    tmp_s = s[4:-1]
    streak = 0
    comma_index = 0
    while True:
        if tmp_s[comma_index] == ',':
            break
        else:
            comma_index += 1
        if comma_index == len(tmp_s):
            return False

    left_segment = tmp_s[0:comma_index]
    right_segment = tmp_s[comma_index+1:]
    for i in left_segment:
        if not is_digita(i):
            return False
    for i in right_segment:
        if not is_digita(i):
            return False
    return True



instructions = []


for i in range(len(data)-2):
    if data[i] + data[i+1] + data[i+2] == 'mul':
        index = i+3
        tmp_str = data[i] + data[i+1] + data[i+2]
        while True:
            if data[i+3] != "(":
                break
            else:
                tmp_str += data[index]
                index += 1
            if data[index] == ")":
                tmp_str += ")"
                instructions.append(tmp_str)
                break


result = 0
for i in instructions:
    if is_correct(i):
        result += eval(i)
print(result)
file = open("day4.txt", 'r')
data = []
am_of_lines = 0
for line in file:
    data.append(line.strip())
    am_of_lines += 1

def occur_straight_or_backwards(s):
    counter = 0
    for i in range(len(s)-3):
        if (s[i] + s[i+1] + s[i+2] + s[i+3]).lower() in ('xmas', 'samx'):
            counter += 1
    return counter


def occur_to_up_or_down(S):
    counter = 0
    for i in range(len(S)-3):
        for j in range(len(S[i])):
            x, m, a, s = S[i], S[i+1], S[i+2], S[i+3]
            if (x[j] + m[j] + a[j] + s[j]).lower() in ('xmas', 'samx'):
                counter += 1
    return counter

def occur_diagonal(S):
    counter = 0
    for i in range(len(S)-3):
        for j in range(len(S[i])-3):
            x, m, a, s = S[i], S[i+1], S[i+2], S[i+3]
            if (x[j] + m[j+1] + a[j+2] + s[j+3]).lower() in ('xmas', 'samx'):
                counter += 1
            if (x[j+3] + m[j + 2] + a[j + 1] + s[j]).lower() in ('xmas', 'samx'):
                counter += 1
    return counter

licznik = 0
for i in data:
    licznik += occur_straight_or_backwards(i)
licznik += occur_diagonal(data)
licznik += occur_to_up_or_down(data)
print(licznik)
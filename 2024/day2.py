from collections import defaultdict as dd
file = open("day2.txt", "r")
data = []

def rozklad(s):
    distribution = dd(int)
    for i in s.lower():
        distribution[i] += 1
    return distribution

def minus(s1, s2):
    res = ""
    rozklad_s1 = rozklad(s1)
    rozklad_s2 = rozklad(s2)
    for i in rozklad_s1:
        rozklad_s1[i] -= rozklad_s2[i]
    for i in rozklad_s1:
        tmp = rozklad_s1[i]
        res += tmp*i
    return res


for line in file:
    data.append(line.strip("\n"))

def to_array(s):
    tab = list(map(int, s.split()))
    return tab

def is_safe(tab):
    czy_rosnaca = 0
    if tab[1] > tab[0]:
        czy_rosnaca = 1

    for i in range(len(tab)-1):
        if czy_rosnaca:
            if tab[i] >= tab[i+1] or tab[i+1] - tab[i] not in (1, 2, 3):
                return False
        else:
            if tab[i] <= tab[i+1] or tab[i] - tab[i+1] not in (1, 2, 3):
                return False
    return True


def is_almost_safe(tab):
    x = tab
    tmp_tab = tab
    for i in tab:
        tmp_tab.remove(i)
        print(tmp_tab, x)
        if is_safe(tmp_tab):
            return True
        tmp_tab = x
    return False

def permutations(tab):
    result = []
    for i in tab:
        x = tab
        result.append(i)
print(permutations([3, 2, 1]))


counter = 0
counter2 = 0
for i in data:
    if is_safe(to_array(i)):
        counter += 1
print(counter)

x = to_array(data[3])
print(x)
print(is_almost_safe(x))
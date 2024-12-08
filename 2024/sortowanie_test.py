import random

counter_of_operations = 0

# Generowanie tablicy
random_numbers = [random.randint(1, 1000000) for _ in range(100)]

print(random_numbers)
max_element = random_numbers[0]
for i in range(len(random_numbers)):
    counter_of_operations += 1
    if random_numbers[i] > max_element:
        max_element = random_numbers[i]


a = [0]*max_element
for i in range(len(random_numbers)):
    counter_of_operations += 1
    a[random_numbers[i]-1] += 1

posortowana = [0]*len(random_numbers)

index = 0
k = 0
for i in range(len(a)):
    counter_of_operations += 1
    if a[i] >= 1:
        while k < a[i]:
            posortowana[index] += i+1
            index += 1
            k += 1
        k = 0
print(posortowana)
#print(sorted(random_numbers))
print(f"Liczba operacji: {counter_of_operations}")
print(f"Max value : {max(posortowana)}")


def znajdz_minimum(tablica, lewy, prawy):
    # Przypadek bazowy: tylko jeden element w przedziale
    if lewy == prawy:
        return tablica[lewy]

    # Znajdź środek
    srodek = (lewy + prawy) // 2

    # Rekurencyjnie znajdź minimum w lewej i prawej części
    lewy_min = znajdz_minimum(tablica, lewy, srodek)
    prawy_min = znajdz_minimum(tablica, srodek + 1, prawy)

    # Porównaj i zwróć mniejsze z dwóch wartości
    if lewy_min < prawy_min:
        return lewy_min
    else:
        return prawy_min

#print(znajdz_minimum(random_numbers, 0, len(random_numbers)-1))
#print(min(random_numbers))
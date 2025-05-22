import random

my_numbers = []

for i in range(100):
    my_numbers.append(random.randint(1, 1001))


def insert_sort(tab):
    for i in range(len(tab)):
        key = tab[i]
        j = i - 1
        while tab[j] > key and j >= 0:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab


my_numbers = insert_sort(my_numbers)

print(my_numbers)

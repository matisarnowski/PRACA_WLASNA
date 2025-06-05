import random

my_numbers = []
for i in range(100):
    my_numbers.append(random.randint(1, 1001))


def buuble_sort(tab):
    for j in range(0, len(tab)):
        for k in range(0, len(tab) - 1):
            if tab[k] > tab[k + 1]:
                tab[k], tab[k + 1] = tab[k + 1], tab[k]


buuble_sort(my_numbers)
print(my_numbers)

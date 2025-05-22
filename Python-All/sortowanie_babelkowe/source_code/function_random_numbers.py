import random


def random_numbers(n=2):
    tab = []
    for i in range(0, n):
        tab.append(random.randint(0, 101))
    return tab

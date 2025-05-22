#!/usr/bin/python3


def potega(x):
    liczba = 2**x
    return liczba


def formowanie_TABLICY(liczba):
    for i in range(1, liczba):
        y = i
        tab = []
        z = 1
        while y > 0:
            if y % 2 == 1:
                tab.append(z)
            y = int(y / 2)
            z = z + 1
        print(i + 1, tab)


x = int(input())

liczba = potega(x)
print("0 Zbiór pusty")
formowanie_TABLICY(liczba)

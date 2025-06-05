#!/usr/bin/python3.7


def collatz(n):
    i = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
            i += 1
        else:
            n = 3 * n + 1
            print(n)
            i += 1
    print("Liczba kroków, to:  ", i)
    return None


try:
    x = int(input("Podaj liczbę, dla której chcesz zastosować funkcję Collatza: "))
except ValueError:
    print("Podaj liczbę nie ciąg tekstowy: ")
    x = int(input("Podaj liczbę, dla której chcesz zastosować funkcję Collatza: "))

collatz(x)

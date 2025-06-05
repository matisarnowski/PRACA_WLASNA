#!/usr/bin/python3

from math import sqrt as pierwiastek


def delta(w_1, w_2, w_3):
    wyznacznik = w_2**2 - 4 * w_1 * w_3
    return wyznacznik


def rozw(liczba, w_1, w_2):
    if liczba > 0:
        miejsce_zerowe_1 = (-1 * w_2 + pierwiastek(liczba)) / (2 * w_1)
        miejsce_zerowe_2 = (-1 * w_2 - pierwiastek(liczba)) / (2 * w_1)
        return miejsce_zerowe_1, miejsce_zerowe_2
    elif liczba == 0:
        miejsce_zerowe_0 = (-1 * w_2) / (2 * w_1)
        return miejsce_zerowe_0
    else:
        return "Nie ma rozwiązań, dla liczb rzeczywistych. "


print("Ten program liczy rozwiązania równania dwumianu kwadratowego! ")

a = float(input("Podaj współczynnik przy x do potęgi drugiej: "))

b = float(input("Podaj współczynnik przy x: "))

c = float(input("Podaj wyraz wolny: "))

liczba = delta(a, b, c)

if liczba > 0:
    print(
        "Ponieważ wyznacznik dwumianu jest większy od zera, istnieją dwa rozwiązania równania:",
        rozw(liczba, b, a),
        "!",
    )
elif liczba == 0:
    print(
        "Ponieważ wyznacznik dwumianu jest równy zeru, istnieje tylko jedno rozwiązanie równania:",
        rozw(liczba, a, b),
        "!",
    )
else:
    print(rozw(liczba, b, a))

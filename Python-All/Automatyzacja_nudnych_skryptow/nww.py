#! /usr/bin/python3


def nwd(a, b):
    while a != 0:
        if a <= b:
            b = b % a
        else:
            c = b
            b = a
            a = c
    return b


liczba_1 = int(
    input("Podaj pierwszą liczbę, do obliczenia największej wspólnej wielokrotności: ")
)
liczba_2 = int(
    input("Podaj drugą liczbę, do obliczenia największej wspólnej wielokrotności: ")
)

dzielnik = nwd(liczba_1, liczba_2)
nww = (liczba_1 * liczba_2) / dzielnik
nww = int(nww)

print(
    "Największa wspólna wielokrotność, liczb: ", liczba_1, " i ", liczba_2, " to: ", nww
)

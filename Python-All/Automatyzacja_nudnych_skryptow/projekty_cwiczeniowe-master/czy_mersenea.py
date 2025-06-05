#!/usr/bin/python3

from math import sqrt

print("Czy liczba jest liczbą Mersene'a? ")
print("Liczby Mersene'a to liczby postaci 2^p - 1, gdzie p jest liczbą pierwszą. ")

licz = int(input("Podaj liczbę, zostanie sprawdzone, czy jest t liczna Mersene'a: "))

p = 0
if licz % 2 == 1:
    spr = licz

    while spr > 0:
        spr /= 2
        p += 1
        spr = int(spr)

    licznik = 0
    dod_p = sqrt(p)
    dod_p = int(dod_p)

    for i in range(2, dod_p):
        if p % i == 0:
            licznik += 1

    if licznik > 0:
        print("Liczba ", licz, " nie jest liczbą Mersene'a. ")
    else:
        print("Liczba ", licz, " jest liczbą Mersene'a. ")
else:
    print("Ta liczba, nie może być liczbą Mersene'a, gdyż jest liczbą parzystą. ")

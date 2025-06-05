#!/usr/bin/python3

wynik = 1


def silnia(a, wynik):
    for i in range(1, a + 1):
        wynik = wynik * i
        wynik = wynik % 100
    return wynik


c = int(input())

lista = []
wynik1 = []
wynik10 = []

for k in range(c):
    a = int(input())
    lista.insert(k, silnia(a, wynik))

for j in range(c):
    wynik1.insert(j, lista[j] % 10)
    wynik10.insert(j, (lista[j] % 100 - lista[j] % 10) / 10)

for m in range(c):
    print(int(wynik10[m]), int(wynik1[m]), "\n")

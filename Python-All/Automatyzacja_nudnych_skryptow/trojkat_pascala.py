#!/usr/bin/python3
import math

potega_dwumianu = int(
    input(
        "Wprowadź potęgę dla , której chcesz wygenerować ostatni wiersz 'Trójkąta Pascala.': "
    )
)
ilosc = potega_dwumianu + 1

for i in range(ilosc):
    liczba = i + 1
    for j in range(liczba):
        print(
            int(math.factorial(i) / (math.factorial(j) * math.factorial(i - j))),
            end=" ",
        )
    print("\n")

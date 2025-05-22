#! /usr/bin/python3

import math


def pola_trapezow(a, b, n):
    wszystkie_pola = 0
    for k in range(n):
        podstawa_dolna = 0
        podstawa_gorna = 0
        j = 0
        odwrocony_stopien = stopien
        while j <= stopien and odwrocony_stopien >= 0:
            podstawa_dolna += tablica_wsp[j] * (
                (a + k * (b - a) / n) ** odwrocony_stopien
            )
            podstawa_gorna += tablica_wsp[j] * (
                (a + (k + 1) * (b - a) / n) ** odwrocony_stopien
            )
            j += 1
            odwrocony_stopien -= 1
        pole = ((math.fabs(podstawa_dolna + podstawa_gorna)) / 2) * ((b - a) / n)
        wszystkie_pola = wszystkie_pola + pole

    return wszystkie_pola


print(
    "Policzymy pole figury ograniczonej osią X pod wykresem funkcji, będącej wielomianem stopnia n."
)

stopien = int(
    input(
        "Podaj liczbę naturalną będącą stopniem wielomianu pod, którego wykresem policzymy pole: "
    )
)

print("Teraz podaj kolejno współczynniki: ")

tablica_wsp = []
for i in range(stopien + 1):
    wsp = float(
        input(
            "Podaj współczynnik przy x^"
            + str(stopien - i)
            + " może to być dowolna liczba wymierna. "
        )
    )
    tablica_wsp.append(wsp)

print("Teraz podaj w jakim zakresie osi x, chcesz policzyć pole pod wykresem: ")

a = int(input("Podaj pierwszą liczbę, musi to być liczba całkowita: "))
b = int(input("Podaj drugą liczbę, musi to być liczba całkowita: "))

print(
    "Jak bardzo dokładnie chcesz policzyć pole, wpisz na ile trapezów program ma podzielić pole pod wykresem: "
)

n = int(input("Podaj liczbę naturalną: "))

calka = pola_trapezow(a, b, n)

print("Pole figury pod wykresem tej funkcji jest równe: " + str(calka))

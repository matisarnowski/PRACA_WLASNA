#! /usr/bin/python3

while True:
    dokladnosc = input(
        "Ludolfina zostanie wyliczona przy pomocy szeregu Leibniza podaj liczbę naturalną większą od jedynki, im większa liczba tym większa dokładność przybliżenia liczby Pi!: "
    )
    if dokladnosc.isdecimal() == True:
        dokladnosc = int(dokladnosc)
        break
    else:
        print("Podaj liczbę naturalną większą od jedynki")

while True:
    if dokladnosc == 1:
        liczba_pi = 1
        break
    elif dokladnosc > 1:
        liczba_pi = 1
        dokladnosc += 1
        for i in range(1, dokladnosc + 1):
            if i % 2 == 1:
                liczba_pi = liczba_pi - 1 / (i * 2 + 1)
            else:
                liczba_pi = liczba_pi + 1 / (i * 2 + 1)
        break
    else:
        print("Podaj liczbe naturalną większą od jedynki!")
        continue

liczba_pi = 4 * liczba_pi

print(liczba_pi)

#! /usr/bin/python3

import math

print(
    "Ustal dokładność z jaką chcesz obliczyć przybliżenie liczby Eulera. 0 będzie oznaczać najmniejszą dokładność, wyniesie ona 1. Im większą liczbę naturalną wybierzesz tym dłuższy szereg służący do obliczeń. "
)

while True:
    dokladnosc = input("Podaj liczbę naturalną lub 0: ")
    if dokladnosc.isdecimal() == True:
        dokladnosc = int(dokladnosc)
        break
    else:
        print("Nie podałeś liczby naturalnej lub zera. To niezbędne do obliczeń.")

e = 0

for i in range(dokladnosc + 1):
    e = e + 1 / (math.factorial(i))

dokladnosc = str(dokladnosc + 1)
e = str(e)

print(
    "Po dokladnie "
    + dokladnosc
    + " zsumowaniu elementów ciągu, przybliżenie liczby Eulera wyniosło: "
    + e
)

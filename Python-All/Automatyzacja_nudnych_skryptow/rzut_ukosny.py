#! /usr/bin/python3

import math


def predkosc_poczatkowa(odleglosc):
    for pomoc in range(1, 90):
        kat = float(pomoc)
        kat = math.radians(kat)
        sinus_kata = math.sin(kat)
        predkosc = math.sqrt((odleglosc * 9.81) / sinus_kata)

        pomoc = str(pomoc)
        predkosc = str(predkosc)

        print(
            "Dla kątu: "
            + pomoc
            + " należy nadać predkość początkową "
            + predkosc
            + " m/s^2. "
        )


print(
    "Program liczy jaką trzeba nadać prędkość początkową, aby program osiągnął podaną odległość d dla różnych kątów. "
)

odleglosc_1 = float(
    input(
        "Podaj jaką odległość ma osiągnąć wyrzucony przedmiot, może to być liczba wymierna dodatnia. "
    )
)

predkosc_poczatkowa(odleglosc_1)

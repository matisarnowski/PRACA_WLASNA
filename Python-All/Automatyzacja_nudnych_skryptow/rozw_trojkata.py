#! /usr/bin/python3

import math

while True:
    bok_a = float(
        input(
            "Podaj długość pierwszego boku, trójkąta (dowolna liczba dodatnia wymierna): "
        )
    )
    bok_b = float(
        input(
            "Podaj długość drugiego boku, trójkąta (dowolna liczba dodatnia wymierna): "
        )
    )
    bok_c = float(
        input(
            "Podaj długość trzeciego boku, trójkąta (dowolna liczba dodatnia wymierna): "
        )
    )

    if bok_a + bok_b > bok_c and bok_b + bok_c > bok_a and bok_c + bok_a and bok_b:
        print(
            "Taki trójkąt, może istnieć w naszej rzeczywistości. Przystępujemy do obliczeń."
        )
        break
    else:
        print(
            "Niestety nie może zasitnieć trójkąt, o takich bokach. spróbuj jeszcze raz: "
        )

obwod = bok_a + bok_b + bok_c

p = 0.5 * obwod

kw_a = bok_a**2
kw_b = bok_b**2
kw_c = bok_c**2

kat_AB = math.acos((kw_a + kw_b - kw_c) / (2 * bok_a * bok_b))
kat_BC = math.acos((kw_b + kw_c - kw_a) / (2 * bok_b * bok_c))
kat_AC = math.acos((kw_a + kw_c - kw_b) / (2 * bok_a * bok_c))

kat_AB = math.degrees(kat_AB)
kat_BC = math.degrees(kat_BC)
kat_AC = math.degrees(kat_AC)

pole = math.sqrt(p * (p - bok_a) * (p - bok_b) * (p - bok_c))

print("Obwód zadanego trójkąta, wynosi: " + str(obwod))
print("Pole zadanego trojkata, wynosi: " + str(pole))
print("Kąt naprzeciw pierwszego boku ma miarę w stopniach: " + str(kat_BC))
print("Kąt naprzeciw drugiego boku ma miarę w stopniach: " + str(kat_AC))
print("Kąt naprzeciw trzeciego boku ma miarę w stopniach: " + str(kat_AB))

if kat_BC == 90.0 or kat_AC == 90.0 or kat_AB == 90.0:
    print("Ponadto jest, to trójkąt prostokątny. ")
if (
    (bok_a == bok_b and bok_a != bok_c)
    or (bok_b == bok_c and bok_b != bok_a)
    or (bok_a == bok_c and bok_a != bok_b)
):
    print("Jest to trójkąt równoramienny . ")
if bok_a == bok_b == bok_c:
    print("jest to, trójkąt równoboczny. ")

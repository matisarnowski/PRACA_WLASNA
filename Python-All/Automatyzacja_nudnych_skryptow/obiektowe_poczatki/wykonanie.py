#!/usr/bin/python3

import circle
import triangle
import hexagon

try:
    r = float(input("Podaj promień koła: "))
    a = float(input("Podaj długość podstawy, trójkąta prostokątnego: "))
    h = float(input("Podaj długość wysokości, opuszczonej na podstawę tego trójkąta: "))
    b = float(input("Podaj długość boku sześciokąta foremnego: "))

except:
    print("Nie podałeś liczby.")

kolo = circle.Circle(r)
trojkat = triangle.Triangle(a, h)
szesciokat = hexagon.Hexagon(b)

print(
    "Pole koła o zadanym promieniu wynosi: ",
    round(kolo.pole(), 2),
    ". Obwód koła to: ",
    round(kolo.obwod(), 2),
    ".",
)
print(
    "Pole zadanego trójkąta wynosi: ",
    round(trojkat.pole(), 2),
    ". Obwód trójkąta prostokątnego wynosi: ",
    round(trojkat.obwod(), 2),
    ".",
)
print(
    "Pole zadanego sześciokąta wynosi: ",
    round(szesciokat.pole(), 2),
    ". Obwód trójkąta prostokątnego wynosi: ",
    round(szesciokat.obwod(), 2),
    ".",
)

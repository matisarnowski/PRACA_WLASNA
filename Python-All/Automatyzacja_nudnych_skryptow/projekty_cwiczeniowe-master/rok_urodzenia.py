#!/usr/bin/python3
import datetime

teraz = datetime.datetime.now()
rok = int(teraz.year)

imie = input("Podaj swoje imie: ")
nazwisko = input("Podaj swoje nazwisko: ")
wiek = int(input("Podaj swoj wiek: "))


print("Witaj, " + imie + " " + nazwisko)
print("Rok Twojego urodzenia to: ", rok - wiek)

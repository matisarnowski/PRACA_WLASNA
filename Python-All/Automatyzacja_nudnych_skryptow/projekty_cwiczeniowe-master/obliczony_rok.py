#!/usr/bin/python3

drugieCyfry = input("Podaj dwie ostatnie cyfry aktualnego roku: ")
pierwszeCyfry = input("Podaj dwie pierwsze cyfry aktualnego roku: ")

rok = pierwszeCyfry + drugieCyfry

rok1 = int(rok)

wiek = int(input("Podaj swoj wiek: "))

rok_urodzenia = rok1 - wiek

print(rok_urodzenia)
